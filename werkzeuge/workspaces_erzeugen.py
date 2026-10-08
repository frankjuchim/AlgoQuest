#!/usr/bin/env python3
"""Erzeugt Import-Dateien für die Online-IDE (online-ide.de) aus den Gerüsten in materialien/Welt*/3_Online-IDE.

Format wie der Workspace-Export der Online-IDE; eine Datei darf mehrere Workspaces enthalten (JSON-Array), der
Import-Dialog zeigt sie dann einzeln zur Auswahl an. Jede IDE-Datei wird ein eigener Workspace mit einer Datei
(zwei Gerüste in einem Workspace würden sich mit Hauptprogramm und Klassennamen in die Quere kommen). Nutzt eine
Datei Stack, Queue, DynArray oder BinTree, ist die Bibliothek „niedersachsen“ (Abiturklassen Niedersachsen) gleich
aktiviert.

Ausgabe: materialien/Online-IDE/
  AQ_Welt<N>_<Name>_Workspaces.json      Gerüste einer Welt (zum Austeilen)
  AQ_Alle_Welten_Workspaces.json         alle Gerüste
  Lehrkraft/AQ_Musterloesungen_Workspaces.json   Musterlösungen und Papier-Compiler der Klausuren (NICHT austeilen)

Aufruf: python3 werkzeuge/workspaces_erzeugen.py [--pruefen]
  --pruefen: nichts schreiben, Exit-Code 1, wenn die Dateien nicht zum Stand der .txt-Dateien passen.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MAT = REPO / "materialien"
ZIEL = MAT / "Online-IDE"

# (Welt-Ordner, Datei, Workspace-Name, Dateiname im Workspace)
GERUESTE = [
    ("Welt0_Akademie", "AQ_W0_L0_Diagnose_Geruest.txt", "W0 Diagnose – Das Portal (Level 0)", "Diagnose"),
    ("Welt0_Akademie", "AQ_W0_Akademie_Geruest.txt", "W0 Akademie (Level 0.2–0.5)", "Akademie"),
    ("Welt1_Heldenschmiede", "AQ_W1_L1_Heldenschmiede_Geruest.txt", "W1 Heldenschmiede (Level 1.1–1.4)", "Heldenschmiede"),
    ("Welt2_Rangliste", "AQ_W2_L2_Rangliste_Geruest.txt", "W2 Rangliste (Level 2.1–2.3)", "Rangliste"),
    ("Welt2_Rangliste", "AQ_W2_SortierDuell_Geruest.txt", "W2 Sortier-Duell (DS 15)", "SortierDuell"),
    ("Welt3_Labyrinth", "AQ_W3_L3_Labyrinth_Geruest.txt", "W3 Labyrinth (Level 3.1–3.3)", "Labyrinth"),
    ("Welt3_Labyrinth", "AQ_W3_Fraktale_Geruest.txt", "W3 Deko-Werkstatt: Fraktale (DS 18)", "Fraktale"),
    ("Welt3_Labyrinth", "AQ_W3_DungeonRennen_Geruest.txt", "W3 Dungeon-Rennen (DS 19–20)", "DungeonRennen"),
    ("Welt4_Hafen", "AQ_W4_L4_Hafen_Geruest.txt", "W4 Hafen (Level 4.1–4.6)", "Hafen"),
    ("Welt5_Wald", "AQ_W5_L5_Wald_Geruest.txt", "W5 Wald (Level 5.1–5.4)", "Wald"),
    ("Welt5_Wald", "AQ_W5_Baumzeichner_Geruest.txt", "W5 Baumzeichner (DS 31–35)", "Baumzeichner"),
    ("Welt5_Wald", "AQ_W5_AB3_Runenbuch_Testumgebung.txt", "W5 Runenbuch – Testumgebung (AB 3)", "Runenbuch"),
    ("Welt6_Endgegner", "AQ_W6_Probeklausur_Papier-Compiler.txt", "W6 Papier-Compiler Probeklausur", "Paketstation"),
]
LEHRKRAFT = [
    ("Welt0_Akademie", "AQ_W0_L0_Diagnose_LSG.txt", "LSG W0 Diagnose", "Diagnose"),
    ("Welt0_Akademie", "AQ_W0_Akademie_LSG.txt", "LSG W0 Akademie", "Akademie"),
    ("Welt1_Heldenschmiede", "AQ_W1_L1_Heldenschmiede_LSG.txt", "LSG W1 Heldenschmiede", "Heldenschmiede"),
    ("Welt2_Rangliste", "AQ_W2_L2_Rangliste_LSG.txt", "LSG W2 Rangliste", "Rangliste"),
    ("Welt2_Rangliste", "AQ_W2_SortierDuell_LSG.txt", "LSG W2 Sortier-Duell", "SortierDuell"),
    ("Welt3_Labyrinth", "AQ_W3_L3_Labyrinth_LSG.txt", "LSG W3 Labyrinth", "Labyrinth"),
    ("Welt3_Labyrinth", "AQ_W3_Fraktale_LSG.txt", "LSG W3 Fraktale", "Fraktale"),
    ("Welt3_Labyrinth", "AQ_W3_DungeonRennen_LSG.txt", "LSG W3 Dungeon-Rennen", "DungeonRennen"),
    ("Welt4_Hafen", "AQ_W4_L4_Hafen_LSG.txt", "LSG W4 Hafen", "Hafen"),
    ("Welt5_Wald", "AQ_W5_L5_Wald_LSG.txt", "LSG W5 Wald", "Wald"),
    ("Welt5_Wald", "AQ_W5_Baumzeichner_LSG.txt", "LSG W5 Baumzeichner", "Baumzeichner"),
    ("Welt6_Endgegner", "AQ_W6_Probeklausur_Papier-Compiler_LSG.txt", "LSG W6 Papier-Compiler Probeklausur", "Paketstation"),
    ("Welt6_Endgegner", "AQ_W6_Klausur_Papier-Compiler.txt", "Lehrkraft W6 Klausur Ladepark – Papier-Compiler", "Ladepark"),
    ("Welt6_Endgegner", "AQ_W6_Nachschreibklausur_Papier-Compiler.txt",
     "Lehrkraft W6 Nachschreibklausur Kletterhalle – Papier-Compiler", "Kletterhalle"),
]


def ohne_kommentare(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return re.sub(r"//[^\n]*", "", text)


def braucht_niedersachsen(text):
    code = ohne_kommentare(text)
    return bool(re.search(r"\b(Stack|Queue|DynArray|BinTree)\b\s*(\(|\w+\s*[=;,)])|new\s+(Stack|Queue|DynArray|BinTree)\b", code))


def finde(ordner, datei):
    for unter in ("3_Online-IDE", "5_Loesungen"):
        p = MAT / ordner / unter / datei
        if p.exists():
            return p
    raise SystemExit(f"Datei fehlt: {ordner}/…/{datei}")


def workspace(nr, ordner, datei, name, modul):
    text = finde(ordner, datei).read_text(encoding="utf-8").replace("\r\n", "\n")
    return {
        "name": name,
        "id": 1000 + nr,
        "modules": [{
            "name": modul,
            "text": text,
            "id": 5000 + nr,
            "identical_to_repository_version": False,
            "is_copy_of_id": None,
            "repository_file_version": None,
            "isFolder": False,
        }],
        "settings": {"language": "Java", "libraries": ["niedersachsen"] if braucht_niedersachsen(text) else []},
        "parent_folder_id": None,
        "isFolder": False,
    }


def dateien():
    """{relativer Pfad: Inhalt} aller zu erzeugenden Dateien."""
    erg = {}
    alle = [workspace(i, *g) for i, g in enumerate(GERUESTE, 1)]
    for ordner in dict.fromkeys(g[0] for g in GERUESTE):
        welt = [w for w, g in zip(alle, GERUESTE) if g[0] == ordner]
        erg[f"AQ_{ordner}_Workspaces.json"] = welt
    erg["AQ_Alle_Welten_Workspaces.json"] = alle
    erg["Lehrkraft/AQ_Musterloesungen_Workspaces.json"] = [workspace(100 + i, *g) for i, g in enumerate(LEHRKRAFT, 1)]
    return {k: json.dumps(v, ensure_ascii=False, indent=3) + "\n" for k, v in erg.items()}


def main():
    pruefen = "--pruefen" in sys.argv
    soll = dateien()
    abweichend = []
    for rel, inhalt in soll.items():
        pfad = ZIEL / rel
        if pfad.exists() and pfad.read_text(encoding="utf-8") == inhalt:
            continue
        abweichend.append(rel)
        if not pruefen:
            pfad.parent.mkdir(parents=True, exist_ok=True)
            pfad.write_text(inhalt, encoding="utf-8")
    vorhanden = {str(p.relative_to(ZIEL)) for p in ZIEL.rglob("*.json")} if ZIEL.exists() else set()
    veraltet = sorted(vorhanden - set(soll))
    if pruefen:
        for rel in abweichend + veraltet:
            print(f"✘ materialien/Online-IDE/{rel} passt nicht zu den .txt-Dateien – python3 werkzeuge/workspaces_erzeugen.py")
        print(f"{len(soll)} Workspace-Dateien geprüft, {len(abweichend) + len(veraltet)} veraltet.")
        sys.exit(1 if abweichend or veraltet else 0)
    for rel in veraltet:
        (ZIEL / rel).unlink()
    print(f"{len(soll)} Workspace-Dateien, {len(abweichend)} neu geschrieben, {len(veraltet)} entfernt.")


if __name__ == "__main__":
    main()
