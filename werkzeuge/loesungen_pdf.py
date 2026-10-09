#!/usr/bin/env python3
"""Erzeugt alle Lösungen (docx) als PDF in zwei Sortierungen – NUR für die Lehrkraft, nicht öffentlich:

  materialien/Loesungen_Portal/         spiegelt materialien/Arbeitsblaetter_PDF (die Schüler-PDFs auf /themen):
                                        je Welt zu jeder Schüler-PDF die passende Lösung, gleicher Name + Zusatz
                                        (_Loesung bzw. _Erwartungshorizont, Warm-up: _Loesungen)
  materialien/Loesungen_Arbeitsblaetter/ nach Materialart: 01_Arbeitsblaetter, 02_Bosse_und_Probeklausur,
                                        03_Klausuren (Klausur + Nachschreibklausur), 04_Warm-up-Karten

Zuordnung aus seed/arbeitsblaetter.json nach dem Namensschema in 5_Loesungen (AQ_W<n>_AB<k>_LSG.docx,
AQ_W<n>_Boss<n>_Erwartungshorizont.docx …). Warm-up-Lösungen = Seiten ab „Lösungen der Warm-up-Karten“.
Beide Ordner liegen außerhalb von Arbeitsblaetter_PDF und kommen nicht ins Docker-Image (.dockerignore).

Aufruf: python3 werkzeuge/loesungen_pdf.py [--pruefen]   (--pruefen: nur Vollständigkeit, ohne LibreOffice)
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MAT = REPO / "materialien"
PORTAL = MAT / "Loesungen_Portal"
NACH_ART = MAT / "Loesungen_Arbeitsblaetter"
LOESUNGSTEIL = "Lösungen der Warm-up-Karten"

KLAUSUREN = [
    ("Welt6_Endgegner/5_Loesungen/AQ_W6_Klausur_Erwartungshorizont.docx", "AQ_W6-Klausur_Ladepark_Erwartungshorizont.pdf"),
    ("Welt6_Endgegner/5_Loesungen/AQ_W6_Nachschreibklausur_Erwartungshorizont.docx",
     "AQ_W6-Nachschreibklausur_Kletterhalle_Erwartungshorizont.pdf"),
]


def loesung_von(quelle, art):
    """Pfad der Lösungs-docx zu einer Schülerdatei (relativ zu materialien/)."""
    ordner, datei = quelle.split("/")[0], Path(quelle).name
    if art == "ab":
        m = re.match(r"(AQ_W\d_AB\d*(?:_Portal)?)", datei)
        return f"{ordner}/5_Loesungen/{m.group(1)}_LSG.docx"
    if art == "boss":
        m = re.match(r"(AQ_W\d_Boss\d)", datei)
        return f"{ordner}/5_Loesungen/{m.group(1)}_Erwartungshorizont.docx"
    if art == "probeklausur":
        m = re.match(r"(AQ_W\d_Probeklausur)", datei)
        return f"{ordner}/5_Loesungen/{m.group(1)}_Erwartungshorizont.docx"
    if art == "warmup":
        return quelle  # gleiche Datei, nur der Lösungsteil
    raise ValueError(art)


def mit_zusatz(datei, zusatz):
    return datei[:-4] + zusatz + ".pdf"


def eintraege():
    """Liste (quelle_docx, nur_loesungsteil, [ziele relativ zu materialien/])."""
    v = json.loads((REPO / "seed" / "arbeitsblaetter.json").read_text(encoding="utf-8"))
    erg = []
    for w in v["welten"]:
        o = w["ordner"]
        for ab in w["arbeitsblaetter"]:
            name = mit_zusatz(ab["datei"], "_Loesung")
            erg.append((loesung_von(ab["quelle"], "ab"), False,
                        [f"Loesungen_Portal/{o}/{name}", f"Loesungen_Arbeitsblaetter/01_Arbeitsblaetter/{name}"]))
        for x in w.get("weitere", []):
            if x["art"] == "warmup":
                name = mit_zusatz(x["datei"], "_Loesungen")
                erg.append((loesung_von(x["quelle"], "warmup"), True,
                            [f"Loesungen_Portal/{o}/{name}", f"Loesungen_Arbeitsblaetter/04_Warm-up-Karten/{name}"]))
            else:
                name = mit_zusatz(x["datei"], "_Erwartungshorizont")
                erg.append((loesung_von(x["quelle"], x["art"]), False,
                            [f"Loesungen_Portal/{o}/{name}", f"Loesungen_Arbeitsblaetter/02_Bosse_und_Probeklausur/{name}"]))
    for quelle, name in KLAUSUREN:
        erg.append((quelle, False, [f"Loesungen_Arbeitsblaetter/03_Klausuren/{name}"]))
    return erg


def nur_loesungsteil(pdf):
    from pypdf import PdfReader, PdfWriter
    r = PdfReader(str(pdf))
    ab = next((i for i, s in enumerate(r.pages) if LOESUNGSTEIL in (s.extract_text() or "")), None)
    if ab is None:
        sys.exit(f"Lösungsteil „{LOESUNGSTEIL}“ nicht gefunden in {pdf.name}")
    w = PdfWriter()
    for s in r.pages[ab:]:
        w.add_page(s)
    with open(pdf, "wb") as f:
        w.write(f)
    return len(r.pages) - ab


def vorhanden():
    return {str(p.relative_to(MAT)) for d in (PORTAL, NACH_ART) if d.exists() for p in d.rglob("*.pdf")}


def main():
    soll = eintraege()
    fehlt = [q for q, _, _ in soll if not (MAT / q).exists()]
    if fehlt:
        sys.exit("Lösungsdatei fehlt: " + ", ".join(fehlt))
    ziele = {z for _, _, zs in soll for z in zs}
    da = vorhanden()
    if "--pruefen" in sys.argv:
        probleme = sorted(ziele - da) + sorted(da - ziele)
        for p in probleme:
            print(f"✘ {'fehlt' if p in ziele else 'überzählig'}: materialien/{p}")
        print(f"{len(ziele)} Lösungs-PDFs erwartet, {len(probleme)} Problem(e).")
        sys.exit(1 if probleme else 0)
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        sys.exit("soffice (LibreOffice) nicht gefunden.")
    with tempfile.TemporaryDirectory(prefix="lsg-pdf-") as tmp:
        profil = Path(tmp) / "profil"
        for quelle, kuerzen, zs in soll:
            aus = Path(tmp) / "aus"
            aus.mkdir(exist_ok=True)
            r = subprocess.run([soffice, f"-env:UserInstallation=file://{profil}", "--headless", "--convert-to", "pdf",
                                "--outdir", str(aus), str(MAT / quelle)], capture_output=True, text=True, timeout=300)
            pdf = aus / (Path(quelle).stem + ".pdf")
            if r.returncode or not pdf.exists():
                sys.exit(f"Umwandlung fehlgeschlagen: {quelle}\n{r.stderr}")
            zusatz = f" (nur Lösungsteil, {nur_loesungsteil(pdf)} Seiten)" if kuerzen else ""
            for z in zs:
                (MAT / z).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(pdf, MAT / z)
            pdf.unlink()
            print(f"✔ {quelle} → {', '.join(zs)}{zusatz}")
    for rel in sorted(da - ziele):
        (MAT / rel).unlink()
        print(f"− entfernt: {rel}")
    print(f"{len(ziele)} Lösungs-PDFs in materialien/Loesungen_Portal und materialien/Loesungen_Arbeitsblaetter.")


if __name__ == "__main__":
    main()
