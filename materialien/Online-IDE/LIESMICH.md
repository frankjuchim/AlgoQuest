# Online-IDE-Workspaces zum Importieren

Fertige Workspaces für die Online-IDE (online-ide.de) – je Gerüst ein Workspace, bei Welt 4–6 ist die Bibliothek
„Abiturklassen Niedersachsen“ schon aktiviert.

| Datei | Inhalt |
|---|---|
| `AQ_Welt0_Akademie_Workspaces.json` … `AQ_Welt6_Endgegner_Workspaces.json` | Gerüste einer Welt (zum Austeilen) |
| `AQ_Alle_Welten_Workspaces.json` | alle 13 Gerüste in einer Datei |
| `Lehrkraft/AQ_Musterloesungen_Workspaces.json` | Musterlösungen und Papier-Compiler der Klausuren – **nicht austeilen** |

**Importieren:** In der Online-IDE Workspace-Bereich → „Workspace importieren“ → Datei wählen. Enthält eine Datei
mehrere Workspaces, kannst du im Dialog auswählen, welche übernommen werden. Danach wie gewohnt „An Klasse austeilen“.

**Nicht von Hand bearbeiten:** Die JSON-Dateien werden aus den `.txt`-Dateien in `Welt*/3_Online-IDE` und
`Welt*/5_Loesungen` erzeugt. Nach einer Änderung an einem Gerüst neu erzeugen mit

    python3 werkzeuge/workspaces_erzeugen.py

(die GitHub-Prüfung meldet veraltete Workspace-Dateien).
