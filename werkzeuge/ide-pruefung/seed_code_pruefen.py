#!/usr/bin/env python3
"""Kompiliert die Java-Code-Blöcke der Lab-Aufgaben (seed/welten/welt*.json) mit javac.

Jeder Block (in `inhalt`, in Teil-`inhalt` mehrteiliger Aufgaben und in `erklaerung`) wird im Kontext der Klassen
seiner Welt übersetzt – die Kontexte stammen aus den Musterlösungen der Online-IDE (materialien/…/5_Loesungen), damit
Aufgaben und IDE dieselbe Klassen-API benutzen. Lückencode wird mit der ersten akzeptierten Lösung gefüllt.

Kandidaten je Block (der erste fehlerfreie zählt):
  - Klassen des Blocks ersetzen gleichnamige Kontextklassen,
  - Methoden in einer Hilfsklasse oder anstelle/zusätzlich in einer Kontextklasse (Zugriff auf Attribute),
  - Anweisungen als Rumpf einer Methode (Hauptprogramm-Ausschnitt).

Absichtlich fehlerhafter Code (Kategorie „Fehler im Java-Code“, Bug-Hunt-Blöcke) wird nur informativ geprüft.
Exit-Code 1, wenn ein Block, der kompilieren muss, in keinem Kontext kompiliert.

Aufruf: python3 werkzeuge/ide-pruefung/seed_code_pruefen.py [--alle] [--json]
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ide_pruefen as ide  # noqa: E402

REPO = ide.REPO
KONTEXTE = {
    0: ["Welt0_Akademie/5_Loesungen/AQ_W0_Akademie_LSG.txt", "Welt0_Akademie/5_Loesungen/AQ_W0_L0_Diagnose_LSG.txt"],
    1: ["Welt1_Heldenschmiede/5_Loesungen/AQ_W1_L1_Heldenschmiede_LSG.txt"],
    2: ["Welt2_Rangliste/5_Loesungen/AQ_W2_L2_Rangliste_LSG.txt", "Welt2_Rangliste/5_Loesungen/AQ_W2_SortierDuell_LSG.txt"],
    3: ["Welt3_Labyrinth/5_Loesungen/AQ_W3_L3_Labyrinth_LSG.txt", "Welt3_Labyrinth/5_Loesungen/AQ_W3_DungeonRennen_LSG.txt",
        "Welt3_Labyrinth/5_Loesungen/AQ_W3_Fraktale_LSG.txt"],
    4: ["Welt4_Hafen/5_Loesungen/AQ_W4_L4_Hafen_LSG.txt"],
    5: ["Welt5_Wald/5_Loesungen/AQ_W5_L5_Wald_LSG.txt", "Welt5_Wald/5_Loesungen/AQ_W5_Baumzeichner_LSG.txt"],
    6: ["Welt6_Endgegner/5_Loesungen/AQ_W6_Probeklausur_Papier-Compiler_LSG.txt",
        "Welt6_Endgegner/5_Loesungen/AQ_W6_Klausur_Papier-Compiler.txt",
        "Welt6_Endgegner/5_Loesungen/AQ_W6_Nachschreibklausur_Papier-Compiler.txt"],
}
SEED_KONTEXT = Path(__file__).resolve().parent / "seed_kontext"
KOPF = "package aq.prog;\nimport static aq.ide.IDE.*;\nimport aq.ide.Test;\nimport aq.ni.*;\nimport aq.grafik.*;\n"


def kontext_typen(datei):
    """Typdeklarationen (ohne Testklassen) einer IDE-Datei, Musterlösung ggf. eingesetzt: {name: quelltext}."""
    text = Path(datei).read_text(encoding="utf-8") if Path(datei).is_absolute() else \
        (REPO / "materialien" / datei).read_text(encoding="utf-8")
    mit_muster, _ = ide.musterloesung_einsetzen(text)
    text = mit_muster or text
    typen = {}
    for art, name, a, b in ide.zerlege(text):
        stueck = text[a:b]
        if art == "typ" and not re.search(r"@Test\b", stueck):
            typen[name] = re.sub(r"^((?:@\w+\s*)*)public\s+", r"\1", stueck)
    return typen


def code_bloecke(aufgabe):
    """(ort, code, absichtlich_fehlerhaft, interaktions_teil) für alle Code-Blöcke einer Aufgabe."""
    teile = aufgabe["interaktion"] if isinstance(aufgabe["interaktion"], list) else [aufgabe["interaktion"]]
    fehler_kat = aufgabe.get("kategorie") == "Fehler im Java-Code"
    for i, b in enumerate(aufgabe.get("inhalt", [])):
        if b.get("t") == "code":
            bughunt = any(t.get("kind") == "lines" and t.get("block") == i for t in teile)
            yield f"inhalt[{i}]", b["code"], fehler_kat or bughunt
    for k, t in enumerate(teile):
        for i, b in enumerate(t.get("inhalt", []) or []):
            if b.get("t") == "code":
                yield f"teil{k}.inhalt[{i}]", b["code"], fehler_kat
    for i, b in enumerate(aufgabe.get("erklaerung", []) or []):
        if b.get("t") == "code":
            yield f"erklaerung[{i}]", b["code"], fehler_kat


def luecken_fuellen(aufgabe, code):
    """Ersetzt [[id]] durch die erste akzeptierte Lösung; None, wenn eine Lücke keine Textlösung hat."""
    teile = aufgabe["interaktion"] if isinstance(aufgabe["interaktion"], list) else [aufgabe["interaktion"]]
    loesungen = aufgabe["loesung"] if isinstance(aufgabe["loesung"], list) else [aufgabe["loesung"]]
    werte = {}
    for t, l in zip(teile, loesungen):
        if t.get("kind") == "gaps":
            for fid in t.get("felder", {}):
                v = l.get(fid)
                werte[fid] = v[0] if isinstance(v, list) else v
    fehlend = []

    def ersetze(m):
        if m.group(1) in werte and werte[m.group(1)] is not None:
            return str(werte[m.group(1)])
        fehlend.append(m.group(1))
        return m.group(0)
    erg = re.sub(r"\[\[([A-Za-z0-9_-]+)\]\]", ersetze, code)
    return None if fehlend else erg


def ist_auszug(code):
    """Auszüge („…“, Rümpfe „{ ... }“, abgebrochene Blöcke, reine Methodenköpfe) sind kein vollständiger Code und werden nicht kompiliert."""
    ohne = ide.ohne_kommentare(code)
    if "..." in ohne or "…" in ohne or ohne.count("{") != ohne.count("}"):
        return True
    return bool(re.search(r"^[ \t]*(?:public|private|protected|static)[^;{}=]*\)[ \t]*(?://[^\n]*)?$", code, re.M)) and \
        not re.search(r"\)\s*(?://[^\n]*)?\n\s*\{", code)


def kandidaten(code, kontexte, umgebung="", zusatz=None):
    """Liefert Liste von {dateiname: quelltext} – je ein Übersetzungsversuch. `umgebung`: weitere Code-Blöcke derselben
    Aufgabe (deren Klassen/Methoden dürfen benutzt werden); `zusatz`: Ergänzungen aus seed_kontext/aufgaben.json."""
    zusatz = zusatz or {}
    abschnitte = ide.zerlege(code)
    typen = {n: re.sub(r"^((?:@\w+\s*)*)(?:public\s+|static\s+)+", r"\1", code[a:b])
             for art, n, a, b in abschnitte if art == "typ"}
    methoden = [(n, code[a:b]) for art, n, a, b in abschnitte if art == "methode"]
    anweisungen = zusatz.get("vorspann", "") + "\n" + \
        "\n".join(code[a:b] for art, n, a, b in abschnitte if art == "anweisung")
    for art, n, a, b in ide.zerlege(umgebung):
        if art == "typ" and n not in typen:
            typen[n] = re.sub(r"^((?:@\w+\s*)*)(?:public\s+|static\s+)+", r"\1", umgebung[a:b])
    hilfsmethoden = zusatz.get("methoden", "")
    erg = []
    for kontext in kontexte:
        basis = {n: q for n, q in kontext.items() if n not in typen}
        basis.update(typen)
        hilfs = "class AQBlock {\n" + hilfsmethoden + "\n" + "\n".join(q for _, q in methoden) + \
                "\nvoid aqAnweisungen() throws Exception {\n" + anweisungen + "\n}\n}\n"
        erg.append(dict(basis, AQBlock=hilfs))
        if not methoden and anweisungen.strip():
            # Anweisungen als Methode einer Kontextklasse (unqualifizierte Aufrufe wie lernen(...))
            for ziel, quelle in kontext.items():
                if ziel in typen:
                    continue
                v = dict(basis)
                v[ziel] = quelle[:quelle.rstrip().rfind("}")] + "\nvoid aqAnweisungen() throws Exception {\n" + \
                    anweisungen + "\n}\n}\n"
                erg.append(v)
        if methoden:
            # Methoden in eine Kontextklasse einsetzen (gleichnamige ersetzen), Anweisungen in AQBlock
            for ziel, quelle in kontext.items():
                if ziel in typen:
                    continue
                neu = quelle
                for name, q in methoden:
                    gleich = [m for m in ide.METHODE_IN_ZEILE.finditer(neu) if m.group(2) == name]
                    if gleich:
                        m = gleich[0]
                        neu = neu[:m.start()] + q + neu[ide.klammerende(neu, m.end() - 1):]
                    else:
                        neu = neu[:neu.rstrip().rfind("}")] + "\n" + q + "\n}\n"
                v = dict(basis)
                v[ziel] = neu
                v["AQBlock"] = "class AQBlock {\nvoid aqAnweisungen() throws Exception {\n" + anweisungen + "\n}\n}\n"
                erg.append(v)
    return erg


def main():
    alle, als_json = "--alle" in sys.argv, "--json" in sys.argv
    with tempfile.TemporaryDirectory(prefix="seed-code-") as tmp:
        tmp = Path(tmp)
        lib = tmp / "lib"
        ide.lib_kompilieren(lib)
        aufgaben_zusatz = json.loads((SEED_KONTEXT / "aufgaben.json").read_text(encoding="utf-8"))
        nur_aufgaben = kontext_typen(SEED_KONTEXT / "Klassen_aus_Aufgabentexten.txt")
        typen_je_datei = {d: dict(nur_aufgaben, **kontext_typen(d)) for ds in KONTEXTE.values() for d in ds}
        bloecke = {}
        wurzel = tmp / "bloecke"
        for datei in sorted((REPO / "seed" / "welten").glob("welt*.json")):
            welt = json.loads(datei.read_text(encoding="utf-8"))
            w = welt["welt"]
            reihenfolge = KONTEXTE.get(w, []) + [d for x, ds in sorted(KONTEXTE.items()) if x != w for d in ds]
            kontexte = [typen_je_datei[d] for d in reihenfolge]
            for a in welt["aufgaben"]:
                alle_bloecke = list(code_bloecke(a))
                for ort, code, fehlerhaft_erlaubt in alle_bloecke:
                    gefuellt = luecken_fuellen(a, code)
                    schluessel = f"b{len(bloecke):04d}"
                    eintrag = {"aufgabe": a["id"], "ort": ort, "fehlerhaft_erlaubt": fehlerhaft_erlaubt,
                               "luecken": "[[" in code}
                    bloecke[schluessel] = eintrag
                    if gefuellt is None:
                        eintrag["status"] = "übersprungen (Lücke ohne Textlösung)"
                        continue
                    if ist_auszug(gefuellt):
                        eintrag["status"] = "übersprungen (Auszug mit „…“ bzw. nur Methodenkopf)"
                        continue
                    umgebung = "\n".join(c for o, c, f in alle_bloecke
                                         if o != ort and o.startswith("inhalt") and "[[" not in c and not ist_auszug(c))
                    for k, dateien in enumerate(kandidaten(gefuellt, kontexte, umgebung, aufgaben_zusatz.get(a["id"]))):
                        ordner = wurzel / schluessel / f"k{k:03d}"
                        ordner.mkdir(parents=True)
                        for name, quelle in dateien.items():
                            (ordner / f"{name}.java").write_text(KOPF + quelle, encoding="utf-8")
        r = subprocess.run(["java", "-cp", str(lib), "aq.werkzeug.Stapelkompilierer", str(lib), str(wurzel)],
                           capture_output=True, text=True)
        if r.returncode:
            sys.exit("Stapelkompilierer fehlgeschlagen:\n" + r.stderr)
        for z in r.stdout.splitlines():
            _, schluessel, status, rest = z.split(" ", 3)
            bloecke[schluessel]["status"] = status
            bloecke[schluessel]["detail"] = rest
        shutil.rmtree(wurzel, ignore_errors=True)

    pflicht_fehler = [b for b in bloecke.values() if b.get("status") == "fehler" and not b["fehlerhaft_erlaubt"]]
    if als_json:
        print(json.dumps(list(bloecke.values()), ensure_ascii=False, indent=1))
    else:
        ok = sum(b.get("status") == "ok" for b in bloecke.values())
        absichtlich = [b for b in bloecke.values() if b.get("status") == "fehler" and b["fehlerhaft_erlaubt"]]
        uebersprungen = [b for b in bloecke.values() if str(b.get("status", "")).startswith("übersprungen")]
        print(f"{len(bloecke)} Code-Blöcke: {ok} kompilieren, {len(absichtlich)} absichtlich fehlerhaft "
              f"(Bug-Hunt/Fehler im Java-Code), {len(uebersprungen)} übersprungen, {len(pflicht_fehler)} Fehler.")
        for b in pflicht_fehler:
            print(f"  ✘ {b['aufgabe']} {b['ort']}{' (Lücken gefüllt)' if b['luecken'] else ''}: {b['detail']}")
        if alle:
            for b in absichtlich:
                print(f"  · {b['aufgabe']} {b['ort']} (absichtlich fehlerhaft): {b['detail']}")
            for b in uebersprungen:
                print(f"  · {b['aufgabe']} {b['ort']}: {b['status']}")
    sys.exit(1 if pflicht_fehler else 0)


if __name__ == "__main__":
    main()
