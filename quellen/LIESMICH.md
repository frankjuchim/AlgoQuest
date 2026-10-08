# Algo Quest – Quellen (für das GitHub-Repository)

- `specs/` – Planungs- und Format-Spezifikationen aller Welten (SPEC_AlgoQuest_W*.md), Lab-Spezifikation (SPEC_AlgoLab.md),
  Materialanpassung (SPEC_Materialanpassung.md), Lab-Level-Zuordnung (LAB_LEVELS.md) und das Umbenennungsskript warmup.py.
- `lab-inhalte-generatoren/` – Python-Skripte, die die Lab-Aufgaben (seed/welten/welt*.json) erzeugt und per javac geprüft haben.
  Hinweis: Nach der Erzeugung wurden in den JSON-Dateien noch Begriffe angepasst („Gilde“ → Team/Heldenschmiede,
  „Kata“ → „Warm-up“). **Maßgeblich sind die JSON-Dateien in seed/welten/** (im Hauptverzeichnis des Repos), nicht ein erneuter Generatorlauf.
- Die Word-/PowerPoint-Dateien im Materialpaket sind ebenfalls die maßgebliche Fassung (nachträgliche Änderungen wie
  Lab-Adresse, Warm-up, Team wurden direkt in den Dateien vorgenommen).
- Hinweis zu den Specs: Pfadangaben wie `/mnt/user-data/outputs/AlgoQuest/…`, `SCRATCH/…` oder `…/scratchpad/…` stammen aus der
  ursprünglichen Erstellungsumgebung und existieren im Repo nicht. Entsprechungen: `outputs/AlgoQuest/Welt<N>/` →
  `materialien/Welt<N>_<Name>/`, `Werkzeuge/` → `materialien/Werkzeuge/` bzw. `materialien/00_Lehrerhinweise/`,
  `WebApp/` → Hauptverzeichnis. Begriffe in den Specs („Gilde“, „XP“, „Kata“) sind historisch; gültig sind „Team“,
  automatische Lab-Punkte und „Warm-up“.
