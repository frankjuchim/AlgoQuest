# Erklärvideo 8: Abi-Check: die 10 Fallen

> Operatoren, Zeitplanung und die Fallen P1–P10 – damit du keine BE verschenkst

| | |
|---|---|
| **Welt** | Welt 6 · Der Endgegner |
| **Zielgruppe** | Informatik eA (LK), Welt 6 vor der Generalprobe; Wiederholung vor Klausur und Abitur |
| **Länge** | Ziel 9–11 min · Sprechtext ca. 9:28 min (bei 130 Wörtern/min, inkl. Pausen) |
| **Einsatz** | Welt 6, DS 37–38 · Lab-Level 6.1 und 6.2 (Fallenjagd) · AB W6·1 „Korrektur und Fehlerjagd“, Werkzeugkarte 1 „Abi-Check“ |
| **Folien** | `AQ_Video08_Abi-Check_Fallen_P1-P10_Folien.pptx` (16 Folien, Sprechertext auch in den Notizen) |

## Lernziele

- Wissen, was die Operatoren „Nennen“, „Beschreiben“, „Erläutern“, „Begründen“, „Dokumentieren“, „Implementieren“, „Entwickeln“ und „Beurteilen“ verlangen
- Die Bearbeitungszeit mit 2,5 Minuten je BE planen
- Die zehn Fallen P1–P10 an Mini-Beispielen erkennen und korrigieren
- Vor der Abgabe eine eigene Lösung mit der Checkliste prüfen

## Hinweise für die Aufnahme

- Alle Fehlerbeispiele (letzter, summe über eine Schlange, punkteFuer, startetMitA, endetAuf, summeVonBis, ranke, Gold-Trace, Struktogramm summeVonBis, zaehleAnfang) sind eigens für das Video gewählt; sie übernehmen keine Bug-Hunts aus Lab (Level 6.1/6.2), Präsentation W6 (Folien 12–17), AB W6·1, Warm-up oder Klausuren.
- Nummern und Kurztitel P1–P10 exakt nach CLAUDE.md bzw. SPEC_AlgoQuest_W6.md §2.
- Geprüft mit javac/java (NI-Klassen gegen den Nachbau werkzeuge/ide-pruefung/java/aq/ni): letzter(leere DynArray) wirft IndexOutOfBoundsException (Index −1), korrigiert −1, für [4, 9] → 9; summe der Schlange 5, 2, 8 = 15, falsche Version leert die Schlange, korrigierte lässt 5 2 8 stehen; punkteFuer(4) = 12; `int x = s.pop();` und `wort.charAt(0) == "A"` werden vom Compiler abgelehnt; endetAuf: Rüstung → wahr, Schwert → falsch, „un“ → falsch; summeVonBis(3, 6): falsch 12, richtig 18, summeVonBis(5, 2) = 0.
- ranke ohne Basisfall → StackOverflowError; ranke(2) = 7 mit Tiefe 0: ranke(2) → 7, Tiefe 1: ranke(1) → 4, Tiefe 2: ranke(0) → 1. Gold-Trace (gold = 50, −12 je Tag): 50/0, 38/1, 26/2, 14/3, 2/4.
- Pause „Finde die Falle“: zaehleAnfang mit i = 1 (P6), == bei Zeichenketten (P5) und substring(0, 1) bei leerer Zeichenkette (P1, StringIndexOutOfBoundsException). Korrigiert: zaehleAnfang({"Ork", "Elf", "Oger", "Orakel"}, "O") = 3. Hinweis: In echtem Java liefert die falsche Version 0 (== vergleicht Referenzen), in der Online-IDE 2 (== vergleicht inhaltlich, nur „Ork“ an Index 0 fehlt) – beides falsch.
- Pause-Folie: im Schnitt „Video anhalten“ einblenden; die Auflösung kommt erst auf der nächsten Folie.

## YouTube

**Titel:** Abi-Check Informatik: die 10 häufigsten Fallen im Abitur (Niedersachsen) | Algo Quest #8

**Beschreibung:**

```
Wo gehen im Informatik-Abitur Niedersachsen die meisten Punkte verloren? In diesem Video: was die Operatoren verlangen, wie du deine Zeit mit 2,5 Minuten je BE planst, und die zehn typischen Fallen P1 bis P10 – jeweils mit Mini-Beispiel und Korrektur. Dazu eine Pause-Aufgabe „Finde die Falle“ und eine Checkliste für die Abgabe.

Teil der Unterrichtsreihe „Algo Quest – Das Dungeon der Datenstrukturen“ (Informatik eA).
Üben mit sofortiger Rückmeldung: https://algoquest.frankjuchim.de/themen

Kapitel:
0:00 Einstieg
0:28 Operatoren
1:29 Zeitplanung
2:18 Die zehn Fallen
2:41 P1 bis P4
4:03 P5 bis P8
5:58 P9 und P10
7:17 Finde die Falle
8:04 Checkliste
8:33 Zusammenfassung
```

_Zeitmarken sind aus der Textlänge geschätzt – nach dem Schnitt anpassen._

**Tags:** Informatik Abitur, Niedersachsen, Abi-Check, Operatoren, typische Fehler, Java, Struktogramm, Tracetabelle, Informatik LK, Algo Quest

## Drehbuch

### Folie 1 · 0:00 – Abi-Check: die 10 Fallen

*Regie: Kamera unten rechts, Titelfolie im Hintergrund.*

Hallo und willkommen zum Endgegner der Algo Quest! Im Abitur gehen die meisten Punkte nicht verloren, weil jemand gar nichts weiß – sondern durch kleine, immer gleiche Fehler. In diesem Video schauen wir uns an, was die Operatoren von dir verlangen, wie du deine Zeit planst, und dann die zehn Fallen P1 bis P10 – jeweils mit einem kleinen Beispiel.

### Folie 2 · 0:28 – Operatoren: Was wird erwartet?

Jede Teilaufgabe beginnt mit einem Operator, und der legt fest, was du liefern musst. Nennen oder Angeben heißt: kurz aufzählen, ohne Erklärung. Beschreiben heißt: in eigenen Worten, mit Fachsprache. Erläutern ist mehr: Du machst etwas verständlich – wie funktioniert es, warum – am besten mit einem Beispiel aus dem Material. Begründen heißt: auf eine Regel zurückführen, mit einer Weil-deshalb-Kette. Dokumentieren heißt: den Ablauf strukturiert festhalten, etwa in einer Tracetabelle. Implementieren heißt: in Java umsetzen, mit genau der vorgegebenen Signatur. Entwickeln heißt: einen Algorithmus selbst erarbeiten, oft als Struktogramm. Und Beurteilen verlangt ein eigenes Urteil – mit Kriterien und Begründung. Die Anforderungen steigen also: Nennen ist weniger als Beschreiben, Beschreiben weniger als Erläutern, und Begründen und Beurteilen verlangen am meisten. Unterstreiche den Operator beim Lesen – das kostet zwei Sekunden und spart Punkte.

### Folie 3 · 1:29 – Zeitplanung: 2,5 Minuten je BE

Zur Zeit: Rechne mit zweieinhalb Minuten pro Bewertungseinheit. Eine Aufgabe mit vier BE bekommt also zehn Minuten, eine mit acht BE zwanzig. Für sechzig BE sind das hundertfünfzig Minuten reine Bearbeitungszeit. Schreib dir beim Einlesen neben jede Teilaufgabe ihre Zielzeit. Fang mit dem an, was du sicher kannst, und markiere Stellen, an denen du hängst. Und plane am Ende eine Reserve ein – für den Abi-Check, um den es jetzt geht. Ein Tipp noch: Wenn du bei einer Teilaufgabe deine Zielzeit deutlich überschreitest, mach einen Strich an den Rand und geh weiter. Spätere Teilaufgaben bauen oft gar nicht darauf auf, und am Ende kannst du zurückkommen.

### Folie 4 · 2:18 – Die zehn Fallen

Hier sind die zehn Fallen, wie du sie aus dem Lab und von den Arbeitsblättern kennst. Die ersten sieben betreffen vor allem deinen Code, P8 und P9 die Notation – Tracetabelle und Struktogramm – und P10 die Textaufgaben. Wir gehen sie jetzt paarweise durch, immer mit einem Fehler und seiner Korrektur.

### Folie 5 · 2:41 – P1 und P2

Falle P1: Laufzeitfehler nicht ausgeschlossen. Ist die dynamische Reihung leer, greift getItem auf den Index minus eins zu – Absturz. Vor jedem Zugriff fragst du: Leer? Index gültig? Hier also zuerst isEmpty prüfen. Falle P2: Struktur zerstört statt unverändert. Die Summe stimmt, aber danach ist die Schlange leer. Steht in der Aufgabe unverändert, musst du die Werte in einer Hilfsschlange sammeln und am Ende zurückstellen. Das gilt genauso für Stapel und Bäume: vor top, pop, head, dequeue oder getItem immer erst die Leer-Abfrage.

### Folie 6 · 3:19 – P3 und P4

Falle P3: Signatur verfehlt. Verlangt ist eine Methode, die eine Ganzzahl zurückgibt. Hier steht void, und das Ergebnis wird nur ausgegeben. Ausgeben ist nicht zurückgeben! Übersetze den Kopf eins zu eins und prüfe, ob jeder Weg mit return endet. Falle P4: Typen und Casts. Die Klassen der Bibliothek Niedersachsen sind nicht generisch – pop liefert ein Object, also musst du auf Integer casten. Und charAt liefert ein Zeichen, kein Wort: Vergleiche mit A in einfachen Hochkommas. Übrigens auch typisch für P4: die ganzzahlige Division. Sieben durch zwei ist in Java drei, nicht drei Komma fünf.

### Folie 7 · 4:03 – P5 und P6

Falle P5: Zeichenketten. Erlaubt sind nur wenige Operationen: length, charAt, substring, equals, contains, compareTo und das Plus. endsWith gehört nicht dazu. Also: Länge prüfen, die letzten drei Zeichen mit substring holen und mit equals vergleichen. Und Zeichenketten nie mit doppeltem Gleichheitszeichen vergleichen – die Online-IDE verzeiht das, das Abitur nicht. Falle P6: Off-by-one. Die Schleife soll bis einschließlich b laufen. Mit kleiner statt kleiner gleich fehlt die letzte Zahl: Für drei bis sechs kommt zwölf heraus statt achtzehn. Teste Schleifengrenzen deshalb immer mit einem kleinen Beispiel: erster und letzter Wert.

### Folie 8 · 4:45 – P7: Rekursion

Falle P7: Rekursion. Oben fehlt der Basisfall – die Methode ruft sich endlos auf, bis der Speicher überläuft. Unten ist er da: Bei null Tagen gibt es ein Blatt. Ebenso wichtig: Das Ergebnis des rekursiven Aufrufs muss verwendet werden, hier mit plus drei. Und in der Rekursionstabelle beginnt die Tiefe beim Erstaufruf mit null: ranke von zwei hat Tiefe null und liefert sieben. Wenn du eine Rekursion schreibst, fang deshalb immer mit dem Basisfall an und frage dich: Was liefert der kleinste Fall?

### Folie 9 · 5:23 – P8: Tracetabelle

Falle P8: Tracetabelle unvollständig oder Konvention verletzt. Unsere Regel: nur Variablen, keine Spalte für die Bedingung, und eine Zeile genau an jeder markierten Stelle. Typische Fehler sind eine Spalte gold größer gleich zwölf oder die fehlende Startzeile. Richtig sind hier fünf Zeilen: Start mit fünfzig und null, dann achtunddreißig, sechsundzwanzig, vierzehn und zwei. Prüfe am Ende auch, ob die letzte Zeile zum Abbruch passt: Zwei ist kleiner als zwölf, die Schleife endet, tage ist vier.

### Folie 10 · 5:58 – P9: Struktogramm nach EH §5

Falle P9: Struktogramm nicht nach EH Paragraf fünf. Ein häufiger Fehler: Man schreibt einfach Java in die Kästen – int, das Gleichheitszeichen, for mit i plus plus, plus gleich und return. Das ist sprachabhängig und kostet Punkte. Rechts die richtige Form: der Kopf mit Namen, Parametern und deutschen Typnamen, Zuweisung mit dem Pfeil, die Zählschleife für i von a bis b und am Ende gib s zurück. Mein Tipp: Lies dein fertiges Struktogramm einmal durch und suche nach Semikolons, doppelten Gleichheitszeichen oder plus plus.

### Folie 11 · 6:36 – P10: Operator verfehlt

Falle P10: Operator verfehlt. Beurteilen Sie, ob die korrigierte Methode für a größer b ein sinnvolles Ergebnis liefert. Ja, sie funktioniert – das ist ein Urteil ohne Begründung. Die Schleife läuft nicht, Rückgabe null – das ist nur beschrieben. Ein Urteil braucht ein Kriterium, eine Begründung am Code und dann das Urteil selbst: Ein leerer Bereich hat die Summe null. Für a größer b ist die Schleifenbedingung sofort falsch, s bleibt null. Also ist das Ergebnis sinnvoll. Genau diese drei Schritte bringen bei Beurteilen die volle Punktzahl.

### Folie 12 · 7:17 – Finde die Falle!

Jetzt du! In dieser kurzen Methode stecken drei Fallen. Halte das Video an, finde sie und nenne jeweils die P-Nummer. Kleiner Tipp: Denk auch an ungewöhnliche Eingaben.

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 13 · 7:34 – Auflösung: drei Fallen

Auflösung. Erstens P6: Die Schleife beginnt bei eins, das erste Wort wird nie geprüft. Richtig ist null. Zweitens P5: Zeichenketten vergleicht man mit equals. Drittens P1: Ist ein Wort leer, löst substring von null bis eins einen Laufzeitfehler aus. Deshalb zuerst prüfen, ob die Länge größer als null ist. Für Ork, Elf, Oger und Orakel mit dem Anfang O liefert die korrigierte Methode drei.

### Folie 14 · 8:04 – Checkliste vor der Abgabe

Und hier die Checkliste für deine Reserve-Zeit am Ende. Geh jede Implementierung durch: Leer? Index? Struktur unverändert? Stimmt die Signatur, endet jeder Weg mit return? Casts und equals? Bei Rekursion: Basisfall und Ergebnis verwendet? Bei Tabellen die Startzeile, beim Struktogramm kein Java. Und zuletzt: Hast du getan, was der Operator verlangt? Am besten ergänzt du die Liste um deine eigenen Top-3-Fehler aus der Generalprobe.

### Folie 15 · 8:33 – Das nimmst du mit

Fassen wir zusammen. Lies jeden Operator genau – er bestimmt, wie viel du schreiben musst: Nennen ist kurz, Erläutern und Begründen brauchen Zusammenhänge, Beurteilen ein begründetes Urteil. Plane zweieinhalb Minuten pro BE und halte Reserve. Und kenne deine Fallen: Für jede gibt es eine einfache Gegenmaßnahme, und die Checkliste hilft dir, sie am Ende anzuwenden.

### Folie 16 · 8:59 – 

Jetzt bist du dran! Im Lab findest du die Level sechs eins und sechs zwei, die Fallenjagd – dort trainierst du jede Falle mit sofortiger Rückmeldung. Das Arbeitsblatt Korrektur und Fehlerjagd und die Werkzeugkarte Abi-Check helfen dir zusätzlich. Und zum Wiederholen: Schau dir in der Playlist die Videos zu deinen drei häufigsten Fallen noch einmal an. Viel Erfolg im Abitur – du schaffst das!
