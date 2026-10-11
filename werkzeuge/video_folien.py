#!/usr/bin/env python3
"""Erklärvideos zur Algo Quest: Folien (pptx) und Sprechskript (md) aus einer Video-Beschreibung (JSON).

  materialien/Videos/<NN>_<Kurz>/video.json   Quelle (Folien, Sprechertext, Metadaten) – hier wird bearbeitet
  → <NN>_<Kurz>/AQ_Video<NN>_<Kurz>_Folien.pptx   Folien zum Abfilmen; Sprechertext steht in den Notizen
  → <NN>_<Kurz>/AQ_Video<NN>_<Kurz>_Skript.md     Drehbuch: Metadaten, YouTube-Text, Kapitel, Folie für Folie
  → <NN>_<Kurz>/bilder/*.png                       Struktogramme, Bäume, Reihungen … (Renderer des Labs)

Kamera-Zone: Unten rechts (ab x = 9,35 in, y = 4,55 in) bleibt auf jeder Folie frei – dort liegt das Kamerabild.
Nicht öffentlich: materialien/ kommt (bis auf die freigegebenen PDF-Ordner) nicht ins Docker-Image.

Aufruf: python3 werkzeuge/video_folien.py [Ordner …]   (ohne Angabe: alle Videos)
        python3 werkzeuge/video_folien.py --pruefen       (Kamera-Zone frei, Dateien aktuell – ohne Neuerzeugung)
Benötigt python-pptx, Pillow, Node + playwright-core (Bilder) und Chromium (CHROMIUM_PATH bzw. /opt/pw-browsers).
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

REPO = Path(__file__).resolve().parent.parent
VIDEOS = REPO / "materialien" / "Videos"
BILDER_JS = Path(__file__).resolve().parent / "video_bilder.js"

BLAU, GOLD, GRUEN, ROT = "1F4E79", "B8860B", "548235", "C00000"
KASTEN, GRAU, TEXT, CODE_BG = "DBE7F5", "7F7F7F", "1F2A37", "F3F4F6"
# Kamera-Zone (unten rechts) und Inhaltsbereiche
KAMERA_X, KAMERA_Y = 9.35, 4.55
W, H = 13.333, 7.5
LINKS, OBEN = 0.6, 1.45
BREITE_VOLL = W - 2 * LINKS          # oberhalb der Kamera-Zone
BREITE_LINKS = KAMERA_X - 0.25 - LINKS  # neben der Kamera-Zone (volle Höhe)
UNTEN = 7.0

WORTE_PRO_MINUTE = 130


def rgb(h):
    return RGBColor.from_string(h.lstrip("#").upper())


# ---------------------------------------------------------------- Bausteine
def textbox(folie, x, y, w, h, absaetze, groesse=20, farbe=TEXT, fett=False, schrift="Calibri", ausrichtung=None,
            anker=MSO_ANCHOR.TOP, zeilenabstand=None):
    """absaetze: Liste von Strings oder (Text, {fett, farbe, groesse, schrift, ebene}) bzw. Liste von Runs [(t, opts)]."""
    tb = folie.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anker
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, Inches(0.05))
    erste = True
    for a in absaetze:
        p = tf.paragraphs[0] if erste else tf.add_paragraph()
        erste = False
        if ausrichtung:
            p.alignment = ausrichtung
        if zeilenabstand:
            p.line_spacing = zeilenabstand
        runs = a if isinstance(a, list) else [a]
        for r in runs:
            t, o = (r, {}) if isinstance(r, str) else r
            run = p.add_run()
            run.text = t
            f = run.font
            f.name = o.get("schrift", schrift)
            f.size = Pt(o.get("groesse", groesse))
            f.bold = o.get("fett", fett)
            f.italic = o.get("kursiv", False)
            f.color.rgb = rgb(o.get("farbe", farbe))
            if o.get("abstand_nach") is not None:
                p.space_after = Pt(o["abstand_nach"])
    return tb


def kasten(folie, x, y, w, h, fuell=KASTEN, rand=None, form=MSO_SHAPE.ROUNDED_RECTANGLE):
    s = folie.shapes.add_shape(form, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid()
    s.fill.fore_color.rgb = rgb(fuell)
    if rand:
        s.line.color.rgb = rgb(rand)
        s.line.width = Pt(1.5)
    else:
        s.line.fill.background()
    s.shadow.inherit = False
    if form == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = 0.08
    return s


def inline(text, groesse, farbe=TEXT, fett=False):
    """`code` → Consolas, **fett** → fett."""
    runs = []
    for teil in re.split(r"(`[^`]+`|\*\*[^*]+\*\*)", text):
        if not teil:
            continue
        if teil.startswith("`"):
            runs.append((teil[1:-1], {"schrift": "Consolas", "groesse": groesse - 1, "farbe": BLAU, "fett": fett}))
        elif teil.startswith("**"):
            runs.append((teil[2:-2], {"groesse": groesse, "farbe": farbe, "fett": True}))
        else:
            runs.append((teil, {"groesse": groesse, "farbe": farbe, "fett": fett}))
    return runs


def text_hoehe(text, w, groesse, rand=0.1):
    """Geschätzte Höhe (in) eines Fließtexts (Calibri ≈ 0,48 em je Zeichen)."""
    zeichen_pro_zeile = max(10, int((w - 0.1) * 72 / (0.45 * groesse)))
    code = sum(len(m) - 2 for m in re.findall(r"`[^`]+`", text))  # Consolas ist breiter als Calibri
    laenge = len(re.sub(r"`[^`]+`|\*\*", "", text)) + code * 1.4
    zeilen = -(-int(laenge) // zeichen_pro_zeile)
    return zeilen * groesse * 1.17 / 72 + rand


def punkte(folie, x, y, w, h, liste, groesse=22):
    absaetze = []
    for p in liste:
        ebene = 0
        if p.startswith("  - "):
            ebene, p = 1, p[4:]
        zeichen = "▸ " if ebene == 0 else "      – "
        absaetze.append([(zeichen, {"groesse": groesse, "farbe": GOLD if ebene == 0 else GRAU, "fett": True})]
                        + inline(p, groesse - 3 * ebene) + [("", {"abstand_nach": 10})])
    return textbox(folie, x, y, w, h, absaetze, groesse)


def code_groesse(code, w, groesse, nummern=True):
    """Schriftgröße, bei der die längste Zeile ohne Umbruch in die Breite w (in) passt (Monospace ≈ 0,6 em)."""
    zeilen = code.split("\n")
    zeichen = max(len(z) for z in zeilen) + (len(str(len(zeilen))) + 2 if nummern else 0)
    return min(groesse, int((w - 0.35) * 72 / (0.6 * zeichen)))


def codebox(folie, x, y, w, code, markiere=(), groesse=16, nummern=True):
    zeilen = code.split("\n")
    groesse = code_groesse(code, w, groesse, nummern)
    h = 0.25 + len(zeilen) * groesse * 1.32 / 72
    kasten(folie, x, y, w, h, fuell=CODE_BG, rand="D0D5DD", form=MSO_SHAPE.RECTANGLE)
    breite_nr = len(str(len(zeilen)))
    absaetze = []
    for i, z in enumerate(zeilen, 1):
        runs = []
        if nummern:
            runs.append((f"{i:>{breite_nr}}  ", {"schrift": "Consolas", "groesse": groesse, "farbe": "A0A7B1"}))
        code_teil, kommentar = z, ""
        m = re.search(r"\s//.*$", z)
        if m:
            code_teil, kommentar = z[:m.start()], z[m.start():]
        hl = i in markiere
        runs.append((code_teil, {"schrift": "Consolas", "groesse": groesse, "farbe": ROT if hl else TEXT, "fett": hl}))
        if kommentar:
            runs.append((kommentar, {"schrift": "Consolas", "groesse": groesse, "farbe": "5F7F5F"}))
        absaetze.append(runs)
    textbox(folie, x + 0.1, y + 0.08, w - 0.2, h - 0.1, absaetze, groesse, zeilenabstand=1.0)
    return h


def tabelle(folie, x, y, w, kopf, zeilen, groesse=16, hervorheben=(), spaltenbreiten=None):
    zeilenhoehe = groesse * 1.9 / 72
    t = folie.shapes.add_table(len(zeilen) + 1, len(kopf), Inches(x), Inches(y), Inches(w),
                               Inches(zeilenhoehe * (len(zeilen) + 1))).table
    if spaltenbreiten:
        summe = sum(spaltenbreiten)
        for i, b in enumerate(spaltenbreiten):
            t.columns[i].width = Inches(w * b / summe)
    for r, werte in enumerate([kopf] + zeilen):
        t.rows[r].height = Inches(zeilenhoehe)
        for c, v in enumerate(werte):
            zelle = t.cell(r, c)
            zelle.margin_left = zelle.margin_right = Inches(0.06)
            zelle.margin_top = zelle.margin_bottom = Inches(0.02)
            zelle.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = zelle.text_frame
            tf.paragraphs[0].alignment = PP_ALIGN.CENTER
            run = tf.paragraphs[0].add_run()
            run.text = str(v)
            run.font.size = Pt(groesse)
            run.font.name = "Consolas" if r > 0 else "Calibri"
            run.font.bold = r == 0 or (r - 1) in hervorheben
            run.font.color.rgb = rgb("FFFFFF" if r == 0 else (ROT if (r - 1) in hervorheben else TEXT))
            zelle.fill.solid()
            zelle.fill.fore_color.rgb = rgb(BLAU if r == 0 else ("FFFFFF" if r % 2 else "EEF3FA"))
    return zeilenhoehe * (len(zeilen) + 1)


def bilddatei(ordner, name):
    """bilder/<name>.png oder eine kopierte Bilddatei bilder/<name>.<endung>."""
    for endung in (".png", ".jpg", ".jpeg"):
        p = ordner / "bilder" / f"{name}{endung}"
        if p.exists():
            return p
    raise FileNotFoundError(f"Bild „{name}“ fehlt in {ordner / 'bilder'}")


def bild(folie, datei, x, y, w_max, h_max):
    with Image.open(datei) as im:
        bw, bh = im.size
    f = min(w_max / bw, h_max / bh)
    w, h = bw * f, bh * f
    folie.shapes.add_picture(str(datei), Inches(x), Inches(y), Inches(w), Inches(h))
    return w, h


def kopfzeile(folie, titel, farbe):
    band = kasten(folie, 0, 0, 0.22, H, fuell=farbe, form=MSO_SHAPE.RECTANGLE)
    band.name = "Weltfarbe"
    textbox(folie, LINKS, 0.35, BREITE_VOLL, 0.8, [inline(titel, 32, BLAU, True)], 32, anker=MSO_ANCHOR.MIDDLE)
    linie = kasten(folie, LINKS, 1.18, 1.6, 0.06, fuell=GOLD, form=MSO_SHAPE.RECTANGLE)
    linie.name = "Goldlinie"


def fusszeile(folie, text):
    textbox(folie, LINKS, UNTEN + 0.08, 6.5, 0.3, [text], 11, farbe=GRAU)


# ---------------------------------------------------------------- Folientypen
def teilung(f, standard=8.2):
    return f.get("teilung", standard)


def hat_rechts(f):
    return any(f.get(k) for k in ("bild", "tabelle", "kasten"))


def rechte_spalte(folie, f, ordner, y0=OBEN, standard=8.2):
    """Optionaler Inhalt rechts oben (endet über der Kamera-Zone); beginnt bei f["teilung"] (in)."""
    x = teilung(f, standard)
    w = W - LINKS - x
    h_max = KAMERA_Y - 0.2 - y0
    if f.get("bild"):
        bild(folie, bilddatei(ordner, f["bild"]), x, y0, w, h_max)
    elif f.get("tabelle"):
        t = f["tabelle"]
        tabelle(folie, x, y0, w, t["kopf"], t["zeilen"], t.get("groesse", 15), t.get("hervorheben", ()), t.get("breiten"))
    elif f.get("kasten"):
        k = f["kasten"]
        farbe = {"gold": "FFF4D6", "gruen": "E2EFDA", "rot": "FBE3E3"}.get(k.get("farbe"), KASTEN)
        rand = {"gold": GOLD, "gruen": GRUEN, "rot": ROT}.get(k.get("farbe"), BLAU)
        kasten(folie, x, y0, w, h_max, fuell=farbe, rand=rand)
        g = k.get("groesse", 20)
        while g > 13:
            h = (text_hoehe(k.get("titel", ""), w - 0.4, g + 2, 0) + 0.11 if k.get("titel") else 0) + \
                sum(text_hoehe(z, w - 0.4, g, 0) + 0.085 for z in k.get("text", []))
            if h <= h_max - 0.35:
                break
            g -= 1
        absaetze = []
        if k.get("titel"):
            absaetze.append(inline(k["titel"], g + 2, rand, True) + [("", {"abstand_nach": 8})])
        for z in k.get("text", []):
            absaetze.append(inline(z, g) + [("", {"abstand_nach": 6})])
        textbox(folie, x + 0.2, y0 + 0.15, w - 0.4, h_max - 0.3, absaetze, g)


def folie_titel(prs, spec, f, ordner):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    farbe = spec["farbe"]
    kasten(s, 0, 0, W, 0.35, fuell=farbe, form=MSO_SHAPE.RECTANGLE)
    textbox(s, LINKS, 1.2, BREITE_VOLL, 0.5, [f"ALGO QUEST · ERKLÄRVIDEO {spec['nr']}"], 18, GOLD, True)
    textbox(s, LINKS, 1.8, BREITE_VOLL, 1.6, [inline(spec["titel"], 48, BLAU, True)], 48)
    textbox(s, LINKS, 3.35, BREITE_LINKS + 0.5, 1.0, [inline(spec.get("untertitel", ""), 26, TEXT)], 26)
    textbox(s, LINKS, 5.6, BREITE_LINKS, 0.9, [
        [(spec.get("weltname", ""), {"groesse": 20, "fett": True, "farbe": farbe})],
        [("Informatik LK · Abitur Niedersachsen", {"groesse": 16, "farbe": GRAU})]], 18)
    return s


def folie_punkte(prs, spec, f, ordner):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    kopfzeile(s, f["titel"], spec["farbe"])
    w = teilung(f) - LINKS - 0.3 if hat_rechts(f) else BREITE_LINKS
    punkte(s, LINKS, OBEN + 0.1, w, UNTEN - OBEN - 0.2, f.get("punkte", []), f.get("groesse", 24))
    rechte_spalte(s, f, ordner)
    return s


def folie_code(prs, spec, f, ordner):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    kopfzeile(s, f["titel"], spec["farbe"])
    groesse = f.get("groesse", 18)
    nummern = f.get("nummern", True)
    zeilen_ = f["code"].split("\n")
    zeichen_ = max(len(z) for z in zeilen_) + (len(str(len(zeilen_))) + 2 if nummern else 0)
    # Teilung so, dass der Code mindestens in 16 pt passt (rechts bleiben mindestens 4 in)
    standard = 8.2
    if hat_rechts(f):
        standard = min(W - LINKS - 4.0, max(5.6, LINKS + zeichen_ * 0.6 * min(groesse, 16) / 72 + 0.35 + 0.3))
    w = teilung(f, standard) - LINKS - 0.3 if hat_rechts(f) else BREITE_LINKS
    anordnung = f.get("anordnung", "nebeneinander")
    if anordnung == "untereinander":
        # Code oben (endet über der Kamera-Zone), Bild darunter links neben der Kamera-Zone
        zeilen = f["code"].split("\n")
        zeichen = max(len(z) for z in zeilen) + (len(str(len(zeilen))) + 2 if nummern else 0)
        while True:  # Code darf nicht in die Kamera-Zone ragen: notfalls kleiner
            w = min(BREITE_VOLL, zeichen * 0.6 * groesse / 72 + 0.45)
            h_code = 0.25 + len(zeilen) * code_groesse(f["code"], w, groesse, nummern) * 1.32 / 72
            if LINKS + w <= KAMERA_X - 0.1 or OBEN + 0.1 + h_code <= KAMERA_Y - 0.05 or groesse <= 12:
                break
            groesse -= 1
        h = codebox(s, LINKS, OBEN + 0.1, w, f["code"], f.get("markiere", ()), groesse, nummern)
        y = OBEN + 0.3 + h
        if f.get("unten"):
            hu = 0.45 * len(f["unten"])
            punkte(s, LINKS, y, BREITE_LINKS, hu, f["unten"], f.get("groesse_unten", 20))
            y += hu
        bild(s, bilddatei(ordner, f["bild"]), LINKS, y, BREITE_LINKS, UNTEN - y - 0.05)
        return s
    h = codebox(s, LINKS, OBEN + 0.1, w, f["code"], f.get("markiere", ()), groesse, nummern)
    if f.get("unten"):
        punkte(s, LINKS, OBEN + 0.25 + h, min(w, BREITE_LINKS), UNTEN - OBEN - h - 0.3, f["unten"], f.get("groesse_unten", 20))
    rechte_spalte(s, f, ordner, standard=standard)
    return s


def folie_bild(prs, spec, f, ordner):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    kopfzeile(s, f["titel"], spec["farbe"])
    y = OBEN + 0.1
    if f.get("text"):
        h = text_hoehe(f["text"], BREITE_LINKS, 22)
        textbox(s, LINKS, y, BREITE_LINKS, h, [inline(f["text"], 22)], 22)
        y += h + 0.1
    breite = teilung(f) - LINKS - 0.3 if (f.get("kasten") or f.get("tabelle") or f.get("bild2")) else BREITE_LINKS
    bild(s, bilddatei(ordner, f["bild"]), LINKS, y, breite, UNTEN - y - 0.1)
    rechts = {k: v for k, v in f.items() if k in ("kasten", "tabelle", "teilung")}
    if f.get("bild2"):
        rechts["bild"] = f["bild2"]
    rechte_spalte(s, rechts, ordner)
    return s


def folie_tabelle(prs, spec, f, ordner):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    kopfzeile(s, f["titel"], spec["farbe"])
    y = OBEN + 0.1
    if f.get("text"):
        h = text_hoehe(f["text"], BREITE_LINKS, 20)
        textbox(s, LINKS, y, BREITE_LINKS, h, [inline(f["text"], 20)], 20)
        y += h + 0.1
    t = f["tabelle"]
    tabelle(s, LINKS, y, f.get("tabellenbreite", BREITE_LINKS), t["kopf"], t["zeilen"], t.get("groesse", 16),
            t.get("hervorheben", ()), t.get("breiten"))
    rechte_spalte(s, {k: v for k, v in f.items() if k in ("kasten", "bild", "teilung")}, ordner)
    return s


def folie_pause(prs, spec, f, ordner):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    kopfzeile(s, f.get("titel", "Kurz pausieren: Jetzt du!"), spec["farbe"])
    badge = kasten(s, LINKS, OBEN + 0.15, 3.3, 0.6, fuell=GOLD)
    badge.text_frame.text = "⏸  Video anhalten"
    for p in badge.text_frame.paragraphs:
        for r in p.runs:
            r.font.size, r.font.bold, r.font.color.rgb, r.font.name = Pt(20), True, rgb("FFFFFF"), "Calibri"
    y = OBEN + 1.0
    breite = teilung(f) - LINKS - 0.3 if hat_rechts(f) else BREITE_LINKS
    h = text_hoehe(f["aufgabe"], breite, 24)
    textbox(s, LINKS, y, breite, h, [inline(f["aufgabe"], 24)], 24)
    if f.get("code"):
        codebox(s, LINKS, y + h + 0.15, breite, f["code"], (), f.get("groesse", 18), f.get("nummern", True))
    rechte_spalte(s, f, ordner)
    return s


def folie_merke(prs, spec, f, ordner):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    kopfzeile(s, f.get("titel", "Das nimmst du mit"), spec["farbe"])
    kasten(s, LINKS, OBEN + 0.1, BREITE_LINKS, UNTEN - OBEN - 0.3, fuell="E2EFDA", rand=GRUEN)
    punkte(s, LINKS + 0.25, OBEN + 0.3, BREITE_LINKS - 0.5, UNTEN - OBEN - 0.7, f["punkte"], f.get("groesse", 22))
    rechte_spalte(s, f, ordner)
    return s


def folie_ende(prs, spec, f, ordner):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    kopfzeile(s, f.get("titel", "Weiter geht’s im Algo Quest Lab"), spec["farbe"])
    zeilen = []
    for k, v in f.get("links", {}).items():
        zeilen.append([(k + ": ", {"groesse": 22, "fett": True, "farbe": BLAU})] + inline(v, 22) + [("", {"abstand_nach": 12})])
    textbox(s, LINKS, OBEN + 0.2, BREITE_LINKS, 3.5, zeilen, 22)
    if f.get("naechstes"):
        kasten(s, LINKS, 5.3, BREITE_LINKS, 1.3, fuell="FFF4D6", rand=GOLD)
        textbox(s, LINKS + 0.2, 5.4, BREITE_LINKS - 0.4, 1.1,
                [[("Nächstes Video: ", {"groesse": 20, "fett": True, "farbe": GOLD})] + inline(f["naechstes"], 20)], 20,
                anker=MSO_ANCHOR.MIDDLE)
    return s


TYPEN = {"titel": folie_titel, "punkte": folie_punkte, "code": folie_code, "bild": folie_bild, "tabelle": folie_tabelle,
         "pause": folie_pause, "merke": folie_merke, "ende": folie_ende}


# ---------------------------------------------------------------- Prüfung Kamera-Zone
def kamera_verletzungen(prs):
    """Formen, die in die Kamera-Zone ragen (Weltfarbband und Fußzeile ausgenommen)."""
    kx, ky = Inches(KAMERA_X), Inches(KAMERA_Y)
    fehler = []
    for i, s in enumerate(prs.slides, 1):
        for sh in s.shapes:
            if sh.name in ("Weltfarbe",):
                continue
            if sh.left + sh.width > kx + Emu(9000) and sh.top + sh.height > ky + Emu(9000):
                if sh.has_text_frame and not sh.text_frame.text.strip() and sh.shape_type == 17:
                    continue
                fehler.append(f"Folie {i}: „{sh.name}“ ragt in die Kamera-Zone")
    return fehler


# ---------------------------------------------------------------- Skript (Markdown)
def sekunden(text):
    return len(text.split()) / WORTE_PRO_MINUTE * 60


def mmss(s):
    s = int(round(s))
    return f"{s // 60}:{s % 60:02d}"


def skript_md(spec, pptx_name):
    folien = spec["folien"]
    dauer = sum(sekunden(f.get("sprechertext", "")) + f.get("pause_s", 0) for f in folien)
    z = [f"# Erklärvideo {spec['nr']}: {spec['titel']}", "",
         f"> {spec.get('untertitel', '')}", "",
         "| | |", "|---|---|",
         f"| **Welt** | {spec.get('weltname', '')} |",
         f"| **Zielgruppe** | {spec.get('zielgruppe', '')} |",
         f"| **Länge** | Ziel {spec.get('laenge', '')} · Sprechtext ca. {mmss(dauer)} min (bei {WORTE_PRO_MINUTE} Wörtern/min, inkl. Pausen) |",
         f"| **Einsatz** | {spec.get('einsatz', '')} |",
         f"| **Folien** | `{pptx_name}` ({len(folien)} Folien, Sprechertext auch in den Notizen) |", ""]
    z += ["## Lernziele", ""] + [f"- {x}" for x in spec.get("lernziele", [])] + [""]
    if spec.get("hinweise"):
        z += ["## Hinweise für die Aufnahme", ""] + [f"- {x}" for x in spec["hinweise"]] + [""]
    yt = spec.get("youtube", {})
    z += ["## YouTube", "", f"**Titel:** {yt.get('titel', spec['titel'])}", "", "**Beschreibung:**", "", "```"]
    z += [yt.get("beschreibung", "").rstrip(), "", "Kapitel:"]
    t = 0.0
    for f in folien:
        if f.get("kapitel"):
            z.append(f"{mmss(t)} {f['kapitel']}")
        t += sekunden(f.get("sprechertext", "")) + f.get("pause_s", 0)
    z += ["```", "", "_Zeitmarken sind aus der Textlänge geschätzt – nach dem Schnitt anpassen._", ""]
    if yt.get("tags"):
        z += [f"**Tags:** {', '.join(yt['tags'])}", ""]
    z += ["## Drehbuch", ""]
    t = 0.0
    for i, f in enumerate(folien, 1):
        titel = f.get("titel") or (spec["titel"] if f["typ"] == "titel" else "")
        z.append(f"### Folie {i} · {mmss(t)} – {titel}")
        z.append("")
        if f.get("regie"):
            z += [f"*Regie: {f['regie']}*", ""]
        if f.get("sprechertext"):
            z += [f["sprechertext"].strip(), ""]
        if f.get("pause_s"):
            z += [f"*(ca. {f['pause_s']} s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*", ""]
        t += sekunden(f.get("sprechertext", "")) + f.get("pause_s", 0)
    return "\n".join(z).rstrip() + "\n", dauer


# ---------------------------------------------------------------- Ablauf
def bilder_erzeugen(ordner, spec):
    bilder = spec.get("bilder", {})
    dateien = spec.get("bilddateien", {})  # {"name": "pfad/relativ/zum/repo.jpg"} – z. B. Screenshots des Labs
    ziel = ordner / "bilder"
    ziel.mkdir(exist_ok=True)
    for name, quelle in dateien.items():
        q = REPO / quelle
        (ziel / f"{name}{q.suffix.lower()}").write_bytes(q.read_bytes())
    erlaubt = set(bilder) | set(dateien)
    for p in ziel.iterdir():
        if p.stem not in erlaubt:
            p.unlink()
    if not bilder:
        return
    tmp = ordner / "_bilder.json"
    tmp.write_text(json.dumps(bilder, ensure_ascii=False), encoding="utf-8")
    try:
        subprocess.run(["node", str(BILDER_JS), str(tmp), str(ziel)], check=True)
    finally:
        tmp.unlink()
    for name in bilder:  # weißen Rand abschneiden
        p = ziel / f"{name}.png"
        with Image.open(p) as im:
            im = im.convert("RGB")
            from PIL import ImageChops
            diff = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255)))
            box = diff.getbbox()
            if box:
                rand = 12
                box = (max(0, box[0] - rand), max(0, box[1] - rand), min(im.width, box[2] + rand), min(im.height, box[3] + rand))
                im.crop(box).save(p, optimize=True)


def namen(ordner, spec):
    basis = f"AQ_Video{spec['nr']:02d}_{spec['kurz']}"
    return ordner / f"{basis}_Folien.pptx", ordner / f"{basis}_Skript.md"


def bauen(ordner, mit_bildern=True):
    spec = json.loads((ordner / "video.json").read_text(encoding="utf-8"))
    if mit_bildern:
        bilder_erzeugen(ordner, spec)
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(W), Inches(H)
    fuss = f"Algo Quest · Video {spec['nr']}: {spec['titel']}"
    for f in spec["folien"]:
        s = TYPEN[f["typ"]](prs, spec, f, ordner)
        if f["typ"] != "titel":
            fusszeile(s, fuss)
        s.notes_slide.notes_text_frame.text = ((f"[Regie: {f['regie']}]\n\n" if f.get("regie") else "")
                                               + f.get("sprechertext", "").strip())
    pptx, md = namen(ordner, spec)
    fehler = kamera_verletzungen(prs)
    if fehler:
        sys.exit(f"{ordner.name}: " + "; ".join(fehler))
    prs.core_properties.title = spec["titel"]
    prs.core_properties.author = "Algo Quest"
    prs.save(pptx)
    text, dauer = skript_md(spec, pptx.name)
    md.write_text(text, encoding="utf-8")
    print(f"✔ {ordner.name}: {len(spec['folien'])} Folien, Sprechtext ca. {mmss(dauer)} min → {pptx.name}, {md.name}")
    return spec, dauer


def pruefen():
    probleme = []
    for ordner in sorted(p for p in VIDEOS.iterdir() if (p / "video.json").exists()):
        spec = json.loads((ordner / "video.json").read_text(encoding="utf-8"))
        pptx, md = namen(ordner, spec)
        if not pptx.exists() or not md.exists():
            probleme.append(f"{ordner.name}: Folien/Skript fehlen (python3 werkzeuge/video_folien.py {ordner.name})")
            continue
        erwartet, _ = skript_md(spec, pptx.name)
        if md.read_text(encoding="utf-8") != erwartet:
            probleme.append(f"{ordner.name}: Skript veraltet – video.json geändert? (python3 werkzeuge/video_folien.py {ordner.name})")
        prs = Presentation(pptx)
        if len(prs.slides) != len(spec["folien"]):
            probleme.append(f"{ordner.name}: Folienzahl passt nicht zu video.json")
        probleme += [f"{ordner.name}: {x}" for x in kamera_verletzungen(prs)]
        for b in list(spec.get("bilder", {})) + list(spec.get("bilddateien", {})):
            try:
                bilddatei(ordner, b)
            except FileNotFoundError:
                probleme.append(f"{ordner.name}: Bild {b} fehlt")
    for p in probleme:
        print("✘ " + p)
    print(f"Videos geprüft: {len(probleme)} Problem(e).")
    sys.exit(1 if probleme else 0)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--pruefen" in sys.argv:
        return pruefen()
    ordner = [VIDEOS / a if not Path(a).is_absolute() else Path(a) for a in args] or \
        sorted(p for p in VIDEOS.iterdir() if (p / "video.json").exists())
    for o in ordner:
        bauen(o.resolve(), mit_bildern="--ohne-bilder" not in sys.argv)


if __name__ == "__main__":
    main()
