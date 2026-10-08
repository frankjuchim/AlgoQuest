# SPEC – Materialanpassung an „Algo Quest Lab“ (WebApp v2.0): Gilden und XP-Buchung entfallen

Der Auftraggeber hat das Spielsystem geändert. ALLE Materialien (docx/pptx) unter /mnt/user-data/outputs/AlgoQuest/ müssen
konsistent dazu passen. Inhalte (Fachaufgaben, Lösungen, Abi-Bezug) bleiben unverändert – nur das Spielsystem drumherum ändert sich.
SCRATCH = /tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad
Referenz neues System: SCRATCH/SPEC_AlgoLab.md (§1, §2, §7, §8), README der neuen App: /mnt/user-data/outputs/AlgoQuest/WebApp/README.md,
Screenshots /mnt/user-data/outputs/AlgoQuest/WebApp/docs/*.png, Lab-Level-Zuordnung: SCRATCH/algolab/LAB_LEVELS.md (VERBINDLICH: Nummern,
Titel, Online-Boss-Titel je Welt).

## 1. Das neue System (so formulieren)
- **Algo Quest Lab** (kurz „Lab“), Web-Adresse als Platzhalter „[Lab-Adresse]“. Beitritt: Kurscode + Name (Vorname + Initial, z. B. „Lena S.“)
  → persönlicher Code (z. B. K7M-42Q) → notieren! Weiterspielen auf jedem Gerät mit Kurscode + Name + Code.
- **Weltkarte** mit Lab-Leveln je Welt (Nummern/Titel aus LAB_LEVELS.md), interaktive Aufgaben werden automatisch geprüft,
  **Punkte** gibt es automatisch beim ersten Lösen (Stufe 1/2/3 = 10/20/30 Punkte; Abzug für Fehlversuche/Tipps; „Lösung zeigen“ = 0 Punkte).
  Trainingsplatz mit Zufallsaufgaben (Welten 0, 2, 4, 5, 6). **Online-Boss** je Welt (Zeitlimit, Auswertung am Ende, bester Versuch zählt;
  Titel aus LAB_LEVELS.md). **Kata-Trainer** im Lab (Leitner, Selbsteinschätzung, ohne Punkte).
- **Ränge** automatisch: Novize / Lehrling / Geselle / Meister / Großmeister ab 0 / 10 / 30 / 55 / 80 % der Level-Punkte der freigeschalteten Welten.
- **Abzeichen** automatisch: Erste Schritte, Zehnerserie, Fleißig, Unermüdlich, Weltenbummler, „<Welt> gemeistert“, „<Boss> besiegt“, Makellos,
  Fallensucher, Trainingsprofi, Ohne Tipp, Kata-Meister.
- **Scoreboard** im Lab (Namen, Punkte; Lehrkraft kann es ausblenden) und optional Beamer-Board. **Profil** mit „Deine Fallen“ (P1–P10).
- **Lehrkraft** trägt KEINE Punkte ein: Kurs anlegen (Kurscode + QR), Einstellungen (Welten/Bosse freischalten, Scoreboard an/aus),
  Schüler umbenennen/löschen/Code anzeigen, Auswertung (Fortschrittsmatrix, Aufgabenstatistik, Fallen-Profil, CSV), Aufgaben-Vorschau mit
  Lösungen, Urkunden drucken. Weitere Lehrkräfte registrieren sich und werden vom Superadmin freigeschaltet.
- Online-IDE bleibt extern (Gerüste aus den Ordnern 3_Online-IDE); Lab-Level zeigen das passende IDE-Level als Hinweis (ohne Punkte).

## 2. Ersetzungsregeln
- **XP** verschwinden überall. „+10 XP“-Chips/Spalten/Summen entfernen. IDE-Level-Kennzeichnungen bleiben („IDE-Level 4.1 Basis/Erweiterung/
  Experte“), Papier-Kata, Papier-Compiler, Handschrift-Phasen bleiben – nur ohne XP. XP-Kästen auf ABs werden zu einem Kasten
  „🎯 Im Lab üben: Level x.y „Titel“ – Punkte gibt es dort automatisch“ (passende Level aus LAB_LEVELS.md, Feld „AB:“ beachten).
- **Gilde(n)** → „Team(s)“ (Tischgruppe aus 3–4 Personen) bei Arbeitsformen; „Gildenstatistik“ → „Team-Statistik“ bzw. „Kursstatistik“;
  „Gildenbonus“, „Gildenwertung“, „Gilden-Board“ entfallen ersatzlos (ggf. auf Lab-Scoreboard bzw. Fallen-Profil verweisen).
- **Mentor (+XP)** → Rolle „Helfer:in“ ohne Punkte. **Bug-Bounty** → „Bug-Meldung: Wer einen Fehler im Material findet, meldet ihn – ohne Punkte“.
- **Badges** → „Abzeichen“ (automatisch im Lab, Namen aus §1); manuell vergebene Badges entfallen.
- **Papier-Bosse** bleiben als handschriftliches Abi-Training (Auswertung durch Lehrkraft oder Selbst-/Peer-Korrektur nach EH), aber ohne XP;
  ergänzen: „Zusätzlich im Lab: Online-Boss „<Titel>““. Erwartungshorizonte: XP-Umrechnung streichen.
- **WebApp/Board/XP-Buchung/Schnellerfassung/Wettbewerbe (Sortier-Duell, Dungeon-Rennen als Gilden-Wettbewerb)** → Lab-Funktionen laut §1.
  Sortier-Duell und Dungeon-Rennen bleiben als Unterrichtsspiel (Team-Wettbewerb an der Tafel/im Beamer), Ergebnisse ohne WebApp-Wertung.
- **Urkunden**: im Lab (Lehrkraft → Kurs → „🏅 Urkunden“) mit Name, Rang, Punkten, Abzeichen.
- Prüfungen (Probeklausur, Klausuren): XP-Hinweise streichen; Probeklausur bleibt „Generalprobe“ (Papier) + Hinweis auf Online-Boss W6.
- Klausuren „Ladepark“/„Kletterhalle“ und deren EH: nur XP-Erwähnung entfernen, sonst nichts ändern.

## 3. Vorgehen und Qualität
- Bevorzugt den ursprünglichen Generator anpassen und neu erzeugen (Generatoren liegen in SCRATCH: w0a_*, ab/, boss/, pptx/, code/, renum/,
  w2_*, w3_*, w4_*, w5_*, w5_ab23/, w6_*); vorher prüfen, dass der Generator exakt die aktuelle Ausgabedatei erzeugt (Text vergleichen),
  sonst die Ausgabedatei direkt bearbeiten (docx/pptx entpacken, XML per Python ändern, packen – docx-/pptx-Skill unter /mnt/skills/public
  lesen). Keine Inhalte verlieren; Layout sauber halten (keine leeren Kästen, keine verwaisten Überschriften).
- Nach jeder Datei: Validator des docx-/pptx-Skills, alle Seiten/Folien rendern (soffice → PDF → pdftoppm), mit Read ansehen.
- Abschlussprüfung per Skript: in allen bearbeiteten Dateien keine Treffer mehr für /Gilde|Gilden|XP\b|Badge|Mentor-XP|Bug-Bounty|Schnellerfassung|
  Gildenbonus/ (Ausnahme: wörtlich zitierte Aufgabenkontexte ohne Spielbezug – begründen). Lab-Level-Verweise stimmen mit LAB_LEVELS.md überein.
- Ausgabe: gleiche Dateinamen an gleicher Stelle überschreiben. Nur die eigenen zugewiesenen Dateien bearbeiten.
