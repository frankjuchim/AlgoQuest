#!/usr/bin/env python3
"""Erzeugt materialien/Lehrkraft_PDF – NUR für Lehrkräfte (Lab: Lehrkraft-Bereich → Materialien):

  Lehrkraft_PDF/00_Allgemein/        Gesamtübersicht DS 1–40
  Lehrkraft_PDF/Welt_<n>_<Name>/     Präsentationen (pptx → PDF), Lehrerhinweise der Welt,
                                     in Welt 6 zusätzlich Klausur und Nachschreibklausur (Aufgaben)
  Lehrkraft_PDF/verzeichnis.json     Verzeichnis für das Lab: je Welt alle Materialien mit Schülerfassung
                                     (Arbeitsblaetter_PDF, öffentlich) und Lehrkraft-Dateien (Lösungen aus
                                     Loesungen_Portal, Präsentationen, Lehrerhinweise, Klausuren)

Die Lösungs-PDFs selbst erzeugt loesungen_pdf.py (Loesungen_Portal); hier werden sie nur verzeichnet.
Lehrkraft_PDF und Loesungen_Portal kommen ins Docker-Image; der Server liefert sie ausschließlich an angemeldete
Lehrkräfte aus und nur Dateien, die in verzeichnis.json stehen.

Aufruf: python3 werkzeuge/lehrkraft_pdf.py [--pruefen]
  --pruefen: nichts erzeugen; Exit-Code 1, wenn verzeichnis.json veraltet ist oder eine PDF fehlt/überzählig ist.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import loesungen_pdf as L  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
MAT = REPO / "materialien"
ZIEL = MAT / "Lehrkraft_PDF"
VERZEICHNIS = ZIEL / "verzeichnis.json"
AB_PDF = "Arbeitsblaetter_PDF"
PORTAL = "Loesungen_Portal"

KLAUSUREN = [  # (Quelle, PDF-Name, Titel) – Aufgaben; Erwartungshorizonte stehen in loesungen_pdf.KLAUSUREN
    ("Welt6_Endgegner/4_Boss/AQ_W6_Klausur_Ladepark.docx", "AQ_W6-Klausur_Ladepark.pdf", "Klausur „Ladepark“"),
    ("Welt6_Endgegner/4_Boss/AQ_W6_Nachschreibklausur_Kletterhalle.docx", "AQ_W6-Nachschreibklausur_Kletterhalle.pdf",
     "Nachschreibklausur „Kletterhalle“"),
]
GESAMT = ("00_Lehrerhinweise/AQ_Gesamtuebersicht_DS1-40.docx", "00_Allgemein/AQ_Gesamtuebersicht_DS1-40.pdf",
          "Gesamtübersicht DS 1–40 (Einstieg in die Einheit)")


def welt_quellordner(nr):
    treffer = sorted(MAT.glob(f"Welt{nr}_*"))
    if len(treffer) != 1:
        sys.exit(f"Materialordner für Welt {nr} nicht eindeutig: {treffer}")
    return treffer[0]


def datei(label, pfad):
    return {"label": label, "pfad": pfad}


def plan():
    """(zu rendernde Dateien [(quelle, ziel relativ zu materialien/)], Verzeichnis)."""
    v = json.loads((REPO / "seed" / "arbeitsblaetter.json").read_text(encoding="utf-8"))
    render = [(GESAMT[0], f"Lehrkraft_PDF/{GESAMT[1]}")]
    wz = v["werkzeugkarten"]
    allgemein = [
        {"art": "hinweise", "titel": GESAMT[2], "dateien": [datei("Lehrerhinweise", f"Lehrkraft_PDF/{GESAMT[1]}")]},
        {"art": "werkzeug", "titel": wz["titel"], "dateien": [datei("Werkzeugkarten", f"{AB_PDF}/{wz['datei']}")]},
    ]
    welten = []
    for w in v["welten"]:
        nr, o = w["welt"], w["ordner"]
        quelle = welt_quellordner(nr)
        eintraege = []
        for pptx in sorted((quelle / "1_Praesentation").glob("*.pptx"), key=lambda p: ("Kickoff" not in p.stem, p.stem)):
            rest = re.sub(r"^AQ_W\d_", "", pptx.stem)
            ziel = f"Lehrkraft_PDF/{o}/AQ_W{nr}-Praesentation_{rest}.pdf"
            render.append((str(pptx.relative_to(MAT)), ziel))
            titel = "Kickoff-Präsentation (Start der Einheit)" if rest == "Kickoff" else f"Präsentation „{rest.replace('_', ' ')}“"
            eintraege.append({"art": "praesentation", "titel": titel, "dateien": [datei("Folien", ziel)]})
        hinweise = MAT / "00_Lehrerhinweise" / f"AQ_W{nr}_Lehrerhinweise.docx"
        if hinweise.exists():
            ziel = f"Lehrkraft_PDF/{o}/AQ_W{nr}-Lehrerhinweise.pdf"
            render.append((str(hinweise.relative_to(MAT)), ziel))
            eintraege.append({"art": "hinweise", "titel": f"Lehrerhinweise Welt {nr}", "dateien": [datei("Lehrerhinweise", ziel)]})
        for ab in w["arbeitsblaetter"]:
            eintraege.append({"art": "ab", "titel": f"AB {ab['nr']}: {ab['titel']}", "ds": ab.get("ds", []), "dateien": [
                datei("Arbeitsblatt", f"{AB_PDF}/{o}/{ab['datei']}"),
                datei("Lösung", f"{PORTAL}/{o}/{L.mit_zusatz(ab['datei'], '_Loesung')}")]})
        for x in w.get("weitere", []):
            if x["art"] == "warmup":
                dateien = [datei("Karten (ohne Lösungen)", f"{AB_PDF}/{o}/{x['datei']}"),
                           datei("Lösungen", f"{PORTAL}/{o}/{L.mit_zusatz(x['datei'], '_Loesungen')}")]
            else:
                dateien = [datei("Papier-Boss" if x["art"] == "boss" else "Probeklausur", f"{AB_PDF}/{o}/{x['datei']}"),
                           datei("Erwartungshorizont", f"{PORTAL}/{o}/{L.mit_zusatz(x['datei'], '_Erwartungshorizont')}")]
            eintraege.append({"art": x["art"], "titel": x["titel"], "dateien": dateien})
        if nr == 6:
            for (q, name, titel), (_, eh) in zip(KLAUSUREN, L.KLAUSUREN):
                ziel = f"Lehrkraft_PDF/{o}/{name}"
                render.append((q, ziel))
                eintraege.append({"art": "klausur", "titel": titel, "dateien": [
                    datei("Klausur", ziel), datei("Erwartungshorizont", f"{PORTAL}/{o}/{eh}")]})
        # Reihenfolge: Präsentationen, Lehrerhinweise, Arbeitsblätter, Boss/Probeklausur, Klausuren, Warm-up
        rang = {"praesentation": 0, "hinweise": 1, "ab": 2, "boss": 3, "probeklausur": 3, "klausur": 4, "warmup": 5}
        eintraege.sort(key=lambda e: rang[e["art"]])
        welten.append({"welt": nr, "ordner": o, "eintraege": eintraege})
    verzeichnis = {
        "_hinweis": "ERZEUGT von werkzeuge/lehrkraft_pdf.py – nicht von Hand ändern. Pfade relativ zu materialien/. "
                    "Arbeitsblaetter_PDF/… ist öffentlich (/arbeitsblaetter/…), alles andere liefert das Lab nur an "
                    "angemeldete Lehrkräfte aus.",
        "allgemein": allgemein,
        "welten": welten,
    }
    return render, verzeichnis


def alle_pfade(verzeichnis):
    eintraege = verzeichnis["allgemein"] + [e for w in verzeichnis["welten"] for e in w["eintraege"]]
    return [d["pfad"] for e in eintraege for d in e["dateien"]]


def main():
    render, verzeichnis = plan()
    fehlt = [q for q, _ in render if not (MAT / q).exists()]
    if fehlt:
        sys.exit("Quelle fehlt: " + ", ".join(fehlt))
    text = json.dumps(verzeichnis, ensure_ascii=False, indent=1) + "\n"
    soll = {z for _, z in render}
    if "--pruefen" in sys.argv:
        probleme = []
        if not VERZEICHNIS.exists() or VERZEICHNIS.read_text(encoding="utf-8") != text:
            probleme.append("materialien/Lehrkraft_PDF/verzeichnis.json veraltet (npm run lehrkraft)")
        da = {f"Lehrkraft_PDF/{p.relative_to(ZIEL)}" for p in ZIEL.rglob("*.pdf")} if ZIEL.exists() else set()
        probleme += [f"überzählig: materialien/{p}" for p in sorted(da - soll)]
        probleme += [f"fehlt: materialien/{p}" for p in alle_pfade(verzeichnis) if not (MAT / p).exists()]
        for p in probleme:
            print("✘ " + p)
        print(f"{len(alle_pfade(verzeichnis))} Lehrkraft-Downloads verzeichnet, {len(probleme)} Problem(e).")
        sys.exit(1 if probleme else 0)
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        sys.exit("soffice (LibreOffice) nicht gefunden.")
    with tempfile.TemporaryDirectory(prefix="lk-pdf-") as tmp:
        profil = Path(tmp) / "profil"
        for quelle, ziel in render:
            aus = Path(tmp) / "aus"
            aus.mkdir(exist_ok=True)
            r = subprocess.run([soffice, f"-env:UserInstallation=file://{profil}", "--headless", "--convert-to", "pdf",
                                "--outdir", str(aus), str(MAT / quelle)], capture_output=True, text=True, timeout=600)
            pdf = aus / (Path(quelle).stem + ".pdf")
            if r.returncode or not pdf.exists():
                sys.exit(f"Umwandlung fehlgeschlagen: {quelle}\n{r.stderr}")
            (MAT / ziel).parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(pdf), MAT / ziel)
            print(f"✔ {quelle} → materialien/{ziel}")
    for p in ZIEL.rglob("*.pdf"):
        if f"Lehrkraft_PDF/{p.relative_to(ZIEL)}" not in soll:
            p.unlink()
            print(f"− entfernt: {p.relative_to(MAT)}")
    VERZEICHNIS.write_text(text, encoding="utf-8")
    fehlend = [p for p in alle_pfade(verzeichnis) if not (MAT / p).exists()]
    if fehlend:
        sys.exit("Verzeichnis verweist auf fehlende PDFs (erst npm run arbeitsblaetter / loesungen): " + ", ".join(fehlend))
    print(f"{len(soll)} PDFs in materialien/Lehrkraft_PDF, {len(alle_pfade(verzeichnis))} Downloads verzeichnet.")


if __name__ == "__main__":
    main()
