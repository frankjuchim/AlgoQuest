# SPEC – Algo Quest, Welt 6 „Der Endgegner“ (Probeklausur, Korrektur, Klausur, Abschluss)

Grundkonventionen (LIES ZUERST VOLLSTÄNDIG): …/scratchpad/SPEC_AlgoQuest_W0_W1.md; ergänzend SPEC_AlgoQuest_W4.md §0 (VERIFIZIERTE,
NICHT generische Object-API der Niedersachsen-Bibliothek: Stack, Queue, DynArray, BinTree – exakt so, mit Casts), SPEC_AlgoQuest_W3.md
(Rekursionstiefe: Erstaufruf = Tiefe 0; rekursive Struktogramme nach EH §5), SPEC_AlgoQuest_W5.md §0 (BinTree-Nutzung, Basisfall isEmpty).
Scratchpad = /tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad
Vorbilder: /mnt/user-data/outputs/AlgoQuest/Welt0 … Welt5, Werkzeuge, WebApp. Bosse (Abitur-Stil) v. a. Welt4/AQ_W4_Boss4_* und
Welt5/AQ_W5_Boss5_*; Generatoren in …/scratchpad/w4_boss, w5_boss, w5_ab, w5_pptx – in eigenen Unterordner …/scratchpad/w6_<name>/
kopieren. Ausgabe: /mnt/user-data/outputs/AlgoQuest/Welt6/ (Kata/Lehrerhinweise/Gesamtübersicht in Werkzeuge/). Andere Welten NICHT ändern.

Abitur-Referenz (Projekt „Informatik LK – Algorithmik“, mit dem Projects-Tool lesbar: project_read): 2025_Informatik_eA_1B.pdf
(Feld/Felderverwaltung – sehr gutes Strukturvorbild: Klasse erläutern, Stapel, Schlange, 2D-Reihung, DynArray, Trace, Rekursion),
2026_Informatik_eA_1A.pdf (Max-Heap), 2023InformatikEA1L.pdf / 2022InformatikEA1L.pdf (Erwartungshorizonte mit Kernpunkten),
INF_2024Abi_Operatoren.pdf, INF_Ergaenzende-Hinweise_GO_Neufassung_2025.pdf. NUR als Formvorbild – eigene Kontexte und Daten!
Abitur-Stil: Einleitungstext zum Kontext, Teilaufgaben a), b), … mit [x BE], Operatoren nach Operatorenliste, Material am Ende
(„Abbildung n“, Klassenkarten nach §6, Struktogramme nach §5, Tabellen zur Vervollständigung), Anrede „Sie“.
„Implementieren Sie … in einer im Unterricht verwendeten Programmiersprache.“ Laufzeitfehler müssen explizit ausgeschlossen werden.

## 1. Didaktischer Ort
Welt 6 – Der Endgegner (W13–14, 4 DS). Ziel: Abiturbedingungen erleben und die eigene Fehlerliste kennen.
| DS | Wo | Inhalt | Material |
| 37 | 13 | Probeklausur „Paketstation“ (35 BE, 90 min, Abi-Bedingungen, Hilfsmittel nur Ergänzende Hinweise) = Boss 6 (2 XP je BE) | Probeklausur + EH |
| 38 | 13 | Selbst- und Peer-Korrektur nach Kernpunkten; Fehlerstatistik der Gilde; „Top 10 Punktverluste“ gezielt trainieren; persönliche Checkliste; Papier-Compiler der Implementierungen | AB1 Korrektur und Fehlerjagd + LSG |
| 39–40 | 14 | Klausur „Ladepark“ im Abitur-Format (60 BE, 180 min, Doppel-DS); Nachschreibklausur „Kletterhalle“; danach Abschluss: Endstand-Board, Urkunden, Rückblick | Klausur(en) + EH, WebApp-Urkunden |
Klausur bringt KEINE XP (Note); der Endstand für Urkunden wird VOR der Klausur festgeschrieben. Peer-Korrektor:in: Mentor-XP (10).
Gilde mit der größten Verbesserung zwischen Gildenstatistik (Probeklausur) und Kata-Nachtest: Gildenbonus 30 XP.

## 2. Top 10 Punktverluste (VERBINDLICH, gleiche Nummern/Kurztitel in pptx, AB1, Kata, Lehrerhinweisen, EH-Hinweisen)
P1 Laufzeitfehler nicht ausgeschlossen (isEmpty vor top/pop/head/dequeue/getItem/getLeft; Indexgrenzen 0 … getLength()−1)
P2 Struktur zerstört statt unverändert (Stapel/Schlange nach dem Durchlauf nicht wiederhergestellt, obwohl gefordert)
P3 Signatur verfehlt (Rückgabetyp, Parameter, Name, static/Sichtbarkeit; Rückgabe fehlt auf einem Pfad)
P4 Typen und Casts ((Integer) vergessen, Zeichen vs. Zeichenkette, ganzzahlige Division)
P5 Zeichenketten mit == statt equals; nicht erlaubte String-Operationen
P6 Off-by-one (< statt <=, getLength() statt getLength()−1, Startindex)
P7 Rekursion: Basisfall fehlt/falsch, Ergebnis des rekursiven Aufrufs nicht verwendet, Rekursionstiefe falsch (Erstaufruf = 0)
P8 Trace-/Dokumentationstabelle unvollständig oder Konvention verletzt (vorgegebene Spalten, jede Wertänderung, Endwerte)
P9 Struktogramm nicht nach EH §5 (←, „gib … zurück“, Schleifenarten, Fallunterscheidung; Java-Syntax im Struktogramm)
P10 Operator verfehlt („erläutern“ als bloße Nennung, „begründen“ ohne Begründung, kein Bezug zum Material, Fachbegriffe fehlen)

## 3. Probeklausur „Paketstation“ (DS 37) – Welt6/AQ_W6_Probeklausur_Paketstation.docx + AQ_W6_Probeklausur_Erwartungshorizont.docx
35 BE, 90 min, AFB ≈ 10/19/6 BE. Deckblatt im Algo-Quest-Stil („Boss 6 – Generalprobe“, Hinweise, Hilfsmittel, BE-Tabelle mit
Platz für erreichte Punkte), danach reiner Abi-Stil. Kontext: Paketstation mit Fächern (Klassenkarte Fach/Paket/Paketstation),
DynArray von Fächern, Schlange von Zustellaufträgen, ggf. Stapel (Rücksendungen). Pflichtbausteine: Klasse erläutern, Implementieren
auf DynArray (mit Objekten + Casts), Struktogramm entwickeln (Schlange, Struktur unverändert!), Trace eines gegebenen Algorithmus,
Rekursion (Rekursionstabelle oder Erläutern), Fehler finden. Jede Teilaufgabe im EH: Kernpunkte als abhakbare Liste mit BE je
Kernpunkt (Korrekturbogen für DS 38), AFB, typischer Fehler mit Verweis P1–P10. Anhang EH: Musterlösungen (per Harness getestet).
Welt6/AQ_W6_Probeklausur_Papier-Compiler.txt (Gerüst + Testklasse, Online-IDE-JUnit-Dialekt, Ausgabe an Schüler erst in DS 38) +
Welt6/AQ_W6_Probeklausur_Papier-Compiler_LSG.txt.

## 4. AB1 „Korrektur und Fehlerjagd“ (DS 38) – Welt6/AQ_W6_AB1_Korrektur_und_Fehlerjagd.docx + AQ_W6_AB1_LSG.docx
Ablauf: (1) Selbstkorrektur mit Korrekturbogen (Kernpunkte aus dem EH der Probeklausur – ohne Musterlösungs-Code), (2) Peer-Check
in der Gilde (Zweitkorrektur, Abweichungen klären), (3) Fehlerstatistik der Gilde (Strichliste P1–P10, Diagramm-Vorlage),
(4) Fehlerjagd: je P1–P10 eine kurze Trainingsaufgabe (handschriftlich, 2–5 min, Abi-nah, Code/Struktogramm/Tabelle), (5) persönliche
Checkliste „Mein Abi-Fahrplan“ (Top-3-Fehler, Gegenmaßnahme, Zeitplan 2,5 min/BE, Vorgehen in der Prüfung), (6) Papier-Compiler der
eigenen Implementierungen aus der Probeklausur. LSG: Lösungen der Fehlerjagd + Moderationshinweise.

## 5. Klausur „Ladepark“ (DS 39–40) – Welt6/AQ_W6_Klausur_Ladepark.docx + AQ_W6_Klausur_Erwartungshorizont.docx
Abitur-Format Block 1 OHNE Zusatzthema: 60 BE, 180 min (inkl. Einlesezeit), AFB 18/32/10 BE. Kontext: Ladepark mit E-Ladesäulen
(Klassen z. B. Ladesaeule, Ladevorgang, Ladepark; Vererbung höchstens leicht). Abdeckung (Abi-Häufigkeit!): Klasse erläutern /
Klassendiagramm ergänzen, Implementieren auf DynArray, Stapel ODER Schlange (Struktur unverändert), 2D-Reihung (z. B. Auslastung
Säule × Stunde), Trace (Tracetabelle zur Vervollständigung), Rekursion (Rekursionstabelle + Erläutern/Begründen), Struktogramm
entwickeln, Effizienz durch Zählen (Verdopplung, „abschätzen“), BinTree/BST (Implementieren rekursiv ODER Analyse), Sortieren
(Analyse eines gegebenen Verfahrens), Fehler finden. Deckblatt schlicht (Schulklausur), Notenschlüssel im EH
(Niedersachsen üblich: 15 ≥ 95 %, 14 ≥ 90, 13 ≥ 85, 12 ≥ 80, 11 ≥ 75, 10 ≥ 70, 9 ≥ 65, 8 ≥ 60, 7 ≥ 55, 6 ≥ 50, 5 ≥ 45, 4 ≥ 40,
3 ≥ 33, 2 ≥ 27, 1 ≥ 20, sonst 0 – „an Schulvorgabe anpassen“), Bewertungsbogen je Teilaufgabe, Kernpunkte, AFB, Musterlösungen
(per Harness getestet), Hinweise auf P1–P10. Welt6/AQ_W6_Klausur_Papier-Compiler.txt (nur Lehrkraft: Testklasse für die
Implementierungsaufgaben, damit Korrekturfragen schnell entschieden werden können) inkl. Musterlösung.

## 6. Nachschreibklausur „Kletterhalle“ – Welt6/AQ_W6_Nachschreibklausur_Kletterhalle.docx + AQ_W6_Nachschreibklausur_Erwartungshorizont.docx
Gleiches Format und gleiche Kompetenzabdeckung wie §5 (60 BE, 180 min, AFB 18/32/10), andere Gewichtung/Datenstrukturen-Rollen
(z. B. Stapel statt Schlange, BST statt 2D-Reihung als Implementierung). Kontext: Kletterhalle (Routen, Kletternde, Wartelisten,
Bestenliste). + Welt6/AQ_W6_Nachschreibklausur_Papier-Compiler.txt (Lehrkraft).

## 7. Präsentation – Welt6/AQ_W6_Endgegner.pptx (≈ 25–30 Folien)
DS 37 Briefing (Ablauf Abitur Block 1, Operatoren, 2,5 min/BE, Strategie: überfliegen → Material markieren → BE-Plan → Reserve),
DS 38 Korrektur nach Kernpunkten, Gildenstatistik, Top 10 Punktverluste je mit Bug-Hunt-Beispiel (falsch → richtig) und
Gegenmaßnahme, persönliche Checkliste, DS 39–40 Klausur-Briefing (ohne Inhalte!), Abschluss: Weltkarte aller 7 Welten als Rückblick,
Endstand-Board (Platzhalter), Ränge, Badges, Urkunden, Ausblick Abitur (Wiederholungsplan mit Kata-Trainer, YouTube-Playlist).

## 8. Kata-Karten W6 – Werkzeuge/kata_w6.json ("welt": 6, ids W6-01 … W6-14) + Werkzeuge/AQ_Kata-Karten_W6.docx
„Endgegner-Mix“: je Karte ein Abi-Klassiker aus Welt 0–5 mit gezielter Falle aus P1–P10 (P-Nummer im Text nennen), Kategorien nur aus
KATA_CATEGORIES (WebApp/src/domain.js), DS 37–40, Boss-Training.

## 9. Lehrerhinweise + Gesamtübersicht
Werkzeuge/AQ_W6_Lehrerhinweise.docx (DS 37–40 wie W5: Ablauf, Material, Organisation Abi-Bedingungen, Korrektur-Workflow,
Nachschreibtermin, Abschlussfeier mit WebApp-Urkunden, Videos, Stolpersteine).
Werkzeuge/AQ_Gesamtuebersicht_DS1-40.docx: Gesamtplan der Einheit (Welten, Wochen, alle 40 DS mit Inhalt, Level, Material-
Dateinamen [tatsächlich in /mnt/user-data/outputs/AlgoQuest vorhandene Dateien!], Kür-DS 20/25/29/33, Bosse, XP-System, Ränge,
Badges, Abi-Bezugsmatrix, Video-Liste, Checkliste „Vor dem ersten Einsatz prüfen“).

## 10. WebApp v1.6
seed/kata_w6.json; neu: Abschluss-Urkunden (Admin, druckbar, je Spieler: Pseudonym, Gilde, Rang, XP, Badges, Kursname, Datum,
Unterschriftslinie, Feld für Namen handschriftlich; Gilden-Siegerurkunde für Platz 1–3). Keine Klarnamen speichern.
