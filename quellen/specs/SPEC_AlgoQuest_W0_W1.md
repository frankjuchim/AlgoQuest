# SPEC – Algo Quest, Welt 0 + Welt 1 (verbindlich für alle Teil-Agenten)

Auftraggeber: Frank, Informatiklehrer (LK Informatik eA, Niedersachsen, Max-Planck-Gymnasium Delmenhorst).
Einheit „Algo Quest – Das Dungeon der Datenstrukturen“: neue LK-Einheit Algorithmik & Datenstrukturen
(35 DS à 90 min, 14 Wochen), ab Abitur 2027. Grundlage: KC 2017 + Ergänzende Hinweise Neufassung 2025 (EH).
Schüler arbeiten in der Online-IDE (online-ide.de, Java-Dialekt von Martin Pabst), im Abitur aber ALLES
handschriftlich (Java-Implementierungen, Struktogramme, Tracetabellen).

Ausgabeordner: /mnt/user-data/outputs/AlgoQuest/
  Welt0/  Welt1/  Werkzeuge/  WebApp/
Arbeitsdateien/Skripte NICHT dort, sondern im Scratchpad:
/tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad/<deinname>/

## 1. Didaktischer Rahmen (Kurzfassung)
- Kurs = Game-Studio, baut ein Dungeon-Spiel. 7 Welten: 0 Portal (Kick-off, Werkzeug, Notation) ·
  1 Heldenschmiede (Klassen/Objekte, Vererbung) · 2 Rangliste (Suchen, Sortieren, Effizienz) ·
  3 Labyrinth (Rekursion, Teile und herrsche, 2D) · 4 Hafen (Stack, Queue, DynArray) ·
  5 Wald (BinTree, BST, Transfer) · 6 Endgegner (Probeklausur, Klausur).
- Gilden (3–4 Personen, fest, leistungsgemischt). XP fließen NICHT in die Note ein. Öffentlich nur Gilden-Rangliste.
- XP: IDE-Level Basis/Erweiterung/Experte = 10/20/30 · Papier-Kata korrekt = 5 · Papier-Compiler (Handschrift
  unverändert abgetippt, alle Tests grün) = 30, +10 beim ersten Versuch · Boss-Kampf = 2 XP je erreichter BE ·
  Side-Quest 15–40 · Mentor 10 · Bug-Bounty (Fehler im Material gefunden) 15.
- Ränge: Novize → Lehrling → Geselle → Meister → Großmeister („abiturbereit“).
- Badges: Trace-Detektiv (5 fehlerfreie Tracetabellen in Folge), Struktogramm-Architekt (3 Struktogramme ohne
  Notationsfehler), Rekursions-Magier, Fehlerjäger (Boss-Implementierung mit allen Leer-/Indexabfragen),
  Papier-Compiler (Handschrift läuft beim ersten Abtippen), Speedrunner (wenigste Vergleiche im Sortier-Duell),
  Baumflüsterer, Mentor (3x Mentor-XP).
- DS-Rhythmus: 10' Papier-Kata (ohne Gerät) · 15' Input/Unplugged · 50' Online-IDE-Level · 15' Sicherung.
- Handschrift-Stufen: 1 Lesen/Tracen · 2 Lücken/Parsons-Puzzle · 3 Papier-first („Papier-Compiler“) · 4 Abi auf Zeit (Boss).
- Abi-Check (Checkliste): Signatur wie gefordert, Rückgabe in jedem Pfad · vor jedem Zugriff Leer-/Index-/Blatt-Abfrage ·
  Schleifengrenzen 0 bis length-1 · Struktur am Ende unverändert, falls gefordert · nur erlaubte
  Zeichenketten-Operationen, Vergleich mit equals · unsichere Stellen kurz kommentieren.
- Zeitbudget Abitur: ≈ 2,5 min pro BE. AFB-Verteilung Abi: I/II/III = 30/53/17 %.

## 2. Fachliche Konventionen (EH 2025 – bitte exakt einhalten)
- Signatur-Notation: `name(p: Typ, …): Rückgabetyp`. Typnamen deutsch: Ganzzahl, Kommazahl, Wahrheitswert,
  Zeichen, Zeichenkette, nichts (für void), „Reihung von Gegenstand“, Klassennamen.
- Es heißt immer „Reihung“, nie „Array“. Index ab 0, 2D: [Zeile][Spalte], Länge auslesen erlaubt, for-each erlaubt.
- Erlaubte Zeichenketten-Operationen (abschließend!): Länge, Zeichen an Position, Teilzeichenkette, Verketten,
  Gleichheit, enthält Teilzeichenkette, lexikographischer Vergleich, ASCII-Wert ↔ Zeichen.
  (In Java: length(), charAt(i), substring(a,b), +, equals(...), contains(...), compareTo(...), (int) c / (char) n.)
  NICHT verwenden: toLowerCase, toUpperCase, split, indexOf, trim, replace usw.
- Mathe: `/` bei Ganzzahlen ganzzahlig, `%` (mod) Rest; ganzzahlige Zufallszahl im Bereich; ganzzahliges Runden.
- Struktogramm-Notation (EH §5): sprachunabhängig; Zuweisung mit `←` (z. B. `anzahl ← anzahl + 1`);
  „gib … zurück“ beendet die Operation; „erzeuge …“ ruft Konstruktor auf; Kommentare mit `//`;
  Zählschleife „für i von 0 bis n−1“, for-each „für jedes x in r“; Verzweigung als Dreieck-Block
  (Bedingung, wahr/falsch); Kopf mit Signatur `name(p: Typ): Typ`.
- Klassendiagramm/Klassenkarte (EH §6): Sichtbarkeit `+`/`-` Pflicht; Konstruktoren mit vorangestelltem `c`
  (z. B. `+ c Held(name: Zeichenkette)`); Attribute `- leben: Ganzzahl`; Methoden `+ getLeben(): Ganzzahl`;
  nicht gezeigte Elemente als „…“; Assoziationen nur als einfache, unbeschriftete Linien OHNE Kardinalitäten;
  Vererbung mit Pfeil mit hohler Dreiecksspitze zur Oberklasse. Objektkarte: `held1: Held` mit konkreten Werten
  (`name = "Aria"`, `leben = 100`, …), Referenzen als Pfeil auf andere Objektkarte, `null` als Wort.
- Online-IDE-Besonderheiten: `println(...)` ohne System.out; Anweisungen außerhalb von Klassen = Hauptprogramm;
  `==` vergleicht dort Zeichenketten inhaltlich (anders als echtes Java!) → wir verlangen IMMER `equals`.
  JUnit in der Online-IDE: Testklasse mit parameterlosem Konstruktor; Testmethoden parameterlos, `void`,
  mit `@Test`; globale Methoden `assertEquals(expected, actual, "Meldung")`, `assertTrue(bed, "Meldung")`,
  `assertFalse(bed, "Meldung")`, `fail("Meldung")`; ausführen im Reiter „Testrunner“ (grüne Dreieckspfeile).
  Bibliothek „niedersachsen“ (Stack, Queue, DynArray, BinTree) wird pro Workspace aktiviert (Rechtsklick auf
  Workspace → Einstellungen) – in Welt 0/1 noch nicht nötig, nur erwähnen; als „vor Einsatz prüfen“ markieren.
- Code auf Arbeitsblättern/Folien: normales Java mit `public`/`private`, Ausgabe mit `println(...)`.

## 3. Domäne Welt 1 „Heldenschmiede“ – EXAKTE Klassen-API (alle Materialien identisch!)
Alle Attribute private (-), alle Methoden public (+).

class Gegenstand
  - name: Zeichenkette; - wert: Ganzzahl            (wert in Gold)
  + c Gegenstand(name: Zeichenkette, wert: Ganzzahl)
  + getName(): Zeichenkette;  + getWert(): Ganzzahl
  + beschreibung(): Zeichenkette   → name + " (" + wert + " Gold)"      z. B. "Fackel (5 Gold)"

class Waffe extends Gegenstand
  - schaden: Ganzzahl
  + c Waffe(name: Zeichenkette, wert: Ganzzahl, schaden: Ganzzahl)    (ruft super(name, wert) auf)
  + getSchaden(): Ganzzahl
  + beschreibung(): Zeichenkette  (überschrieben) → "Waffe: " + super.beschreibung() + ", Schaden " + schaden
                                   z. B. "Waffe: Schwert (50 Gold), Schaden 12"

class Trank extends Gegenstand
  - heilwert: Ganzzahl
  + c Trank(name: Zeichenkette, wert: Ganzzahl, heilwert: Ganzzahl)
  + getHeilwert(): Ganzzahl
  + beschreibung(): Zeichenkette  (überschrieben) → "Trank: " + super.beschreibung() + ", heilt " + heilwert
                                   z. B. "Trank: Heiltrank (20 Gold), heilt 30"

class Schluessel extends Gegenstand
  - tuer: Ganzzahl
  + c Schluessel(name: Zeichenkette, wert: Ganzzahl, tuer: Ganzzahl)
  + getTuer(): Ganzzahl
  (beschreibung() wird NICHT überschrieben → geerbte Version, z. B. "Rostiger Schlüssel (2 Gold)")

class Monster
  - name: Zeichenkette; - leben: Ganzzahl; - staerke: Ganzzahl
  + c Monster(name: Zeichenkette, leben: Ganzzahl, staerke: Ganzzahl)
  + getName(), getLeben(), getStaerke()
  + nimmSchaden(schaden: Ganzzahl): nichts     → leben verringern, nie unter 0
  + istBesiegt(): Wahrheitswert                → leben <= 0
  + angreifen(h: Held): nichts                 → h.nimmSchaden(staerke)

class Held
  - name: Zeichenkette; - leben: Ganzzahl; - maxLeben: Ganzzahl; - staerke: Ganzzahl; - gold: Ganzzahl
  - inventar: Reihung von Gegenstand (Länge 5); - anzahl: Ganzzahl; - waffe: Waffe (anfangs null)
  + c Held(name: Zeichenkette)                                  → maxLeben=100, leben=100, staerke=10, gold=0,
                                                                  inventar = neue Reihung der Länge 5, anzahl=0, waffe=null
  + c Held(name: Zeichenkette, maxLeben: Ganzzahl, staerke: Ganzzahl) → leben=maxLeben, Rest wie oben
  + getName(), getLeben(), getMaxLeben(), getStaerke(), getGold(), getAnzahl(), getWaffe()
  + erhalteGold(betrag: Ganzzahl): nichts      → nur wenn betrag > 0: gold += betrag
  + istBesiegt(): Wahrheitswert                → leben <= 0
  + nimmSchaden(schaden: Ganzzahl): nichts     → leben -= schaden, nie unter 0
  + heilen(punkte: Ganzzahl): nichts           → leben += punkte, nie über maxLeben
  + angriffswert(): Ganzzahl                   → staerke + Schaden der ausgerüsteten Waffe (0 ohne Waffe)
  + angreifen(m: Monster): nichts              → m.nimmSchaden(angriffswert())
  + aufnehmen(g: Gegenstand): Wahrheitswert    → false, wenn g == null oder Inventar voll; sonst ans Ende, anzahl++, true
  + gesamtWert(): Ganzzahl                     → Summe der Werte aller Gegenstände im Inventar
  + wertvollsterGegenstand(): Gegenstand       → null, wenn anzahl == 0; bei Gleichstand der erste
  + enthaelt(name: Zeichenkette): Wahrheitswert → mit equals
  + ausruesten(w: Waffe): nichts               → waffe = w
  + trinken(t: Trank): nichts                  → heilen(t.getHeilwert())
  + inventarAusgeben(): nichts                 → println(beschreibung()) für jeden Gegenstand (Polymorphie-Demo)

class Wuerfel
  + static wuerfeln(seiten: Ganzzahl): Ganzzahl  → (int)(Math.random() * seiten) + 1   (1..seiten)

Hauptprogramm-Demo (Online-IDE): Held „Aria“ gegen Monster „Goblin“ (30, 6), Kampfrunden mit Konsolenausgabe.

Level-Einteilung Welt 1 (Online-IDE, je eigene Testklasse):
  L1.1 (DS 3)  Held: Attribute, Konstruktor Held(name), Getter, istBesiegt, nimmSchaden, heilen, erhalteGold
  L1.2 (DS 4)  Überladener Konstruktor Held(name, maxLeben, staerke), Klasse Monster, angriffswert (erst nur staerke),
               angreifen; Referenz-Aufgabe (zwei Variablen → ein Objekt)
  L1.3 (DS 5)  Gegenstand, Inventar: aufnehmen, getAnzahl, gesamtWert, wertvollsterGegenstand, enthaelt
  L1.4 (DS 6)  Vererbung: Waffe, Trank, Schluessel, beschreibung überschreiben, ausruesten, angriffswert mit Waffe,
               trinken, inventarAusgeben
  Stufen je Level: Basis (10 XP) / Erweiterung (20 XP) / Experte (30 XP) – Tests danach gruppieren/benennen.

Level 0 (Welt 0, DS 1) „Diagnose“: class Diagnose mit static-Methoden:
  Basis:       summe(r: Reihung von Ganzzahl): Ganzzahl · maximum(r): Ganzzahl (r nicht leer) · zaehle(r, x): Ganzzahl
  Erweiterung: indexVon(r, x): Ganzzahl (erstes Vorkommen, sonst -1) · istAufsteigendSortiert(r): Wahrheitswert
               · durchschnitt(r): Kommazahl (leere Reihung → 0.0)
  Experte:     anzahlVokale(s: Zeichenkette): Ganzzahl (a,e,i,o,u groß und klein; nur charAt/length, KEIN toLowerCase)
               · istPalindrom(s): Wahrheitswert (exakter Zeichenvergleich, "" und 1 Zeichen → true)

## 4. Boss 1 (DS 7, für Kata/Boss-Agent) – NEUER Kontext (Transfer!)
„Die Gildenhalle – das Auftragsbrett“: Klasse Auftrag (titel, belohnung, schwierigkeit 1–5, erledigt; zwei Konstruktoren),
Klasse Auftragsbrett (Reihung von Auftrag, anzahl), Unterklasse Eilauftrag extends Auftrag (frist in Tagen, belohnung
überschrieben/Bonus). ≈ 24 BE, 60 min, Abi-Operatoren, BE-Angaben, AFB-Mix. Teilaufgaben-Typen: Klasse erläutern
(Konstruktoren, Sichtbarkeit), Objektkarten nach Code (Referenzfalle), Klassendiagramm erweitern (Vererbung + Assoziation),
Methode implementieren auf Reihung (mit Leer-/null-Abfrage), Fehler in Methode finden (== statt equals, Off-by-one).

## 5. Kata-Karten – JSON-Schema (gemeinsam für docx und WebApp)
Datei: /mnt/user-data/outputs/AlgoQuest/Werkzeuge/kata_w0_w1.json
{
  "version": 1,
  "karten": [
    { "id": "W1-07", "welt": 1, "kategorie": "<eine aus Liste>", "titel": "kurz",
      "aufgabe": "Text, Absätze mit \n", "code": "Java-Code oder Struktogramm als Text oder \"\"",
      "loesung": "Text", "loesungCode": "Code oder \"\"", "minuten": 5 }
  ]
}
Kategorien (exakt diese Strings): "Klasse vs. Objekt", "Bestandteile einer Klasse", "Objektkarten und Referenzen",
"Klassendiagramm", "Struktogramm lesen", "Code ↔ Struktogramm", "Tracetabelle", "Fehler im Java-Code",
"Fehler im Struktogramm", "Lückencode", "Methode implementieren", "Verändern und Erweitern", "Funktionsweise erläutern".

## 6. Gestaltung (ABs .docx und Folien .pptx)
- Farben: Primär Dunkelblau #1F4E79 · Grün (ok) #548235 · Rot (Fehler/Achtung) #C00000 · Kastenhintergrund #DBE7F5 ·
  Grau #F0F0F0 · Spiel-Akzent Gold #B8860B (sparsam: XP, Badges, Boss).
- Schrift: Calibri (Fließtext 11 pt), Code: Consolas 10 pt auf grauem Hintergrund.
- AB-Kopfzeile: „Informatik LK · Algo Quest · Welt N – <Name>“ rechts „Name: ____  Gilde: ____  Datum: ____“.
  Titel: „W1·1 – Die Heldenschmiede: Klassen und Objekte“ (Muster).
- Bausteine wie in der bestehenden Reihe: Einleitungsabsatz mit Story-Bezug; Kasten „Infoteil“ (blau hinterlegt);
  „Merke:“, „Tipp:“, „Achtung Abi:“ (rot umrandet), „Für Schnelle“, „Denkanstoß“; Aufgaben „Aufgabe N: Kreativer Titel“
  mit Teilaufgaben a), b) …; Kennzeichnung jeder Aufgabe mit Arbeitsform [IDE] oder [PAPIER] (als farbiges Label,
  Papier = ohne Gerät) und Level ★ / ★★ / ★★★ und XP („+10 XP“) in Gold.
- Ansprache: duzen. Keine Lösungen auf Schülerblättern (Lösungen = eigene LSG-Dateien).
- Online-IDE-Dateien (.txt) im Stil der vorhandenen Gerüste: Kopfblock `// ====…`, Titel, „Informatik LK · Online-IDE ·
  Algo Quest“, ANLEITUNG; Abschnitte „GERÜST – hier nichts verändern“ und „DEIN TEIL – hier arbeitest du!“ mit
  `// TODO Level 1.1 …`; Lehrerexemplar heißt „MUSTERLÖSUNG (Lehrerexemplar)“ mit Hinweisen zu häufigen Schülerfehlern.
  Umlaute in Code-Kommentaren als ae/oe/ue/ss (wie Bestand), Bezeichner ohne Umlaute.

## 7. Dateinamen (verbindlich)
Welt0/AQ_W0_Kickoff.pptx · Welt0/AQ_W0_AB_Portal.docx · Welt0/AQ_W0_L0_Diagnose_Geruest.txt · Welt0/AQ_W0_L0_Diagnose_LSG.txt
Welt1/AQ_W1_Heldenschmiede.pptx · Welt1/AQ_W1_AB1_Klassen_und_Objekte.docx · Welt1/AQ_W1_AB2_Vererbung.docx
Welt1/AQ_W1_L1_Heldenschmiede_Geruest.txt · Welt1/AQ_W1_L1_Heldenschmiede_LSG.txt
Welt1/AQ_W1_Boss1_Gildenhalle.docx · Welt1/AQ_W1_Boss1_Erwartungshorizont.docx
Werkzeuge/AQ_Werkzeugkarten.docx (Abi-Check-Karte, Struktogramm-Spickblatt §5, Signatur-/Typnamen, erlaubte
  Zeichenketten-Operationen, Klassendiagramm-Konventionen §6, Vorlagen: Tracetabelle + leeres Struktogramm-Raster)
Werkzeuge/kata_w0_w1.json · Werkzeuge/AQ_Kata-Karten_W0-W1.docx (Karten zum Ausschneiden, Lösungen auf Rückseiten-/Extraseiten)
Werkzeuge/AQ_W0-W1_Lehrerhinweise.docx (DS-Verläufe DS 1–7)
WebApp/ (Quellcode, Dockerfile, captain-definition, README.md)
