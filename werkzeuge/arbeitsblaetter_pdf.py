#!/usr/bin/env python3
"""Erzeugt materialien/Arbeitsblaetter_PDF: alle Schülermaterialien als PDF – Arbeitsblätter, Werkzeugkarten,
Papier-Bosse, Probeklausur und Warm-up-Karten (ohne Lösungsteil) –, sortiert nach Welten, mit sprechenden
Dateinamen ohne Umlaute (für Upload-Plattformen).

Quelle der Namen und Zuordnung: seed/arbeitsblaetter.json (dieselbe Datei nutzt die Themenseite /themen im Lab).
Umwandlung mit LibreOffice (soffice); Calibri wird dabei durch das maßgleiche Carlito ersetzt.

Aufruf: python3 werkzeuge/arbeitsblaetter_pdf.py [--pruefen]
  --pruefen: nichts erzeugen; Exit-Code 1, wenn eine PDF fehlt oder überzählig ist (nur Vollständigkeit – für die
             GitHub-Prüfung ohne LibreOffice). Nach Änderungen an einem Arbeitsblatt das Skript ohne --pruefen laufen lassen.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MAT = REPO / "materialien"
ZIEL = MAT / "Arbeitsblaetter_PDF"


def eintraege():
    v = json.loads((REPO / "seed" / "arbeitsblaetter.json").read_text(encoding="utf-8"))
    erg = [(v["werkzeugkarten"]["quelle"], v["werkzeugkarten"]["datei"], False)]
    for w in v["welten"]:
        for ab in w["arbeitsblaetter"]:
            erg.append((ab["quelle"], f"{w['ordner']}/{ab['datei']}", False))
        for x in w.get("weitere", []):
            erg.append((x["quelle"], f"{w['ordner']}/{x['datei']}", bool(x.get("ohneLoesungsteil"))))
    return erg


LOESUNGSTEIL = "Lösungen der Warm-up-Karten"


def ohne_loesungsteil(pdf):
    """Schneidet die PDF vor der ersten Seite mit der Überschrift des Lösungsteils ab (beginnt stets auf neuer Seite)."""
    from pypdf import PdfReader, PdfWriter  # nur zum Erzeugen nötig, nicht für --pruefen
    r = PdfReader(str(pdf))
    ab = next((i for i, seite in enumerate(r.pages) if LOESUNGSTEIL in (seite.extract_text() or "")), None)
    if not ab:
        sys.exit(f"Lösungsteil „{LOESUNGSTEIL}“ nicht gefunden in {pdf.name} – Abschneiden unmöglich, nichts veröffentlichen.")
    w = PdfWriter()
    for seite in r.pages[:ab]:
        w.add_page(seite)
    with open(pdf, "wb") as f:
        w.write(f)
    return ab, len(r.pages)


def main():
    pruefen = "--pruefen" in sys.argv
    soll = eintraege()
    fehlt = [q for q, _, _ in soll if not (MAT / q).exists()]
    if fehlt:
        sys.exit("Quelle fehlt: " + ", ".join(fehlt))
    soll_pfade = {d for _, d, _ in soll}
    vorhanden = {str(p.relative_to(ZIEL)) for p in ZIEL.rglob("*.pdf")} if ZIEL.exists() else set()
    if pruefen:
        probleme = sorted(soll_pfade - vorhanden)
        extra = sorted(vorhanden - soll_pfade)
        for p in probleme:
            print(f"✘ fehlt: materialien/Arbeitsblaetter_PDF/{p}")
        for p in extra:
            print(f"✘ nicht im Verzeichnis seed/arbeitsblaetter.json: materialien/Arbeitsblaetter_PDF/{p}")
        print(f"{len(soll)} PDFs erwartet, {len(probleme) + len(extra)} Problem(e).")
        sys.exit(1 if probleme or extra else 0)

    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        sys.exit("soffice (LibreOffice) nicht gefunden.")
    with tempfile.TemporaryDirectory(prefix="ab-pdf-") as tmp:
        profil = Path(tmp) / "profil"
        for quelle, datei, kuerzen in soll:
            aus = Path(tmp) / "aus"
            aus.mkdir(exist_ok=True)
            r = subprocess.run([soffice, f"-env:UserInstallation=file://{profil}", "--headless", "--convert-to", "pdf",
                                "--outdir", str(aus), str(MAT / quelle)], capture_output=True, text=True, timeout=300)
            pdf = aus / (Path(quelle).stem + ".pdf")
            if r.returncode or not pdf.exists():
                sys.exit(f"Umwandlung fehlgeschlagen: {quelle}\n{r.stderr}")
            zusatz = ""
            if kuerzen:
                behalten, gesamt = ohne_loesungsteil(pdf)
                zusatz = f" (Seiten 1–{behalten} von {gesamt}, ohne Lösungsteil)"
            ziel = ZIEL / datei
            ziel.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(pdf), ziel)
            print(f"✔ {ziel.relative_to(REPO)}{zusatz}")
    for rel in sorted(vorhanden - soll_pfade):
        (ZIEL / rel).unlink()
        print(f"− entfernt: {rel}")
    for ordner in sorted(ZIEL.rglob("*"), reverse=True):
        if ordner.is_dir() and not any(ordner.iterdir()):
            ordner.rmdir()
    print(f"{len(soll)} PDFs in materialien/Arbeitsblaetter_PDF.")


if __name__ == "__main__":
    main()
