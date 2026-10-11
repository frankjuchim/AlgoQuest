# Erklärvideo 5: Rekursion verstehen

> Basisfall, Aufrufstapel, Rekursionstabelle und Aufrufbaum – so, wie es das Abitur verlangt

| | |
|---|---|
| **Welt** | Welt 3 · Das Labyrinth |
| **Zielgruppe** | Informatik eA (LK), Welt 3; auch zur Wiederholung vor Boss, Klausur und Abitur |
| **Länge** | Ziel 9–11 min · Sprechtext ca. 10:09 min (bei 130 Wörtern/min, inkl. Pausen) |
| **Einsatz** | Welt 3, DS 18 · Lab-Level 3.1 „Spiegelsaal“ und 3.2 „Hydra“ · AB W3·1 „Rekursion“ |
| **Folien** | `AQ_Video05_Rekursion_Folien.pptx` (16 Folien, Sprechertext auch in den Notizen) |

## Lernziele

- Basisfall und Rekursionsschritt einer rekursiven Methode benennen und erklären, warum das Teilproblem kleiner werden muss
- Den Aufrufstapel beschreiben: Abstieg bis zum Basisfall, Aufstieg mit den Rückgaben
- Eine Rekursionstabelle mit Rekursionstiefe führen (Erstaufruf = Tiefe 0, Rückgaben beim Aufstieg)
- Eine rekursive Methode als Struktogramm nach EH §5 darstellen
- Bei Baumrekursion den Aufrufbaum zeichnen, Aufrufe zählen und die größte Tiefe bestimmen
- Fallen P7 (Basisfall, Ergebnis nicht verwendet, Tiefe) und den StackOverflowError erkennen

## Hinweise für die Aufnahme

- Alle Beispiele (muenzen: Wechselgeld mit 5er- und 1er-Münzen, schleim: Schleim zerfällt in n / 2 und n / 3) sind eigens für das Video gewählt und kommen in Lab, Arbeitsblättern, Bossen und Warm-up nicht vor – das Video verrät keine Lösungen.
- Werte geprüft mit javac/java (instrumentiertes Programm, Tiefe und Aufrufe mitgezählt): muenzen(12) = 4 mit 5 Aufrufen, größte Tiefe 4 (Aufrufe 12, 7, 2, 1, 0); muenzen(9) = 5 mit 6 Aufrufen, größte Tiefe 5 (Aufrufe 9, 4, 3, 2, 1, 0).
- schleim geprüft: schleim(7) = 4, 7 Aufrufe, größte Tiefe 2, Baum s7(s3(s1,s1),s2(s1,s0)); schleim(10) = 5, 9 Aufrufe, größte Tiefe 3, Baum s10(s5(s2(s1,s0),s1),s3(s1,s1)), Beginn-Reihenfolge s10, s5, s2, s1, s0, s1, s3, s1, s1. Allgemein Aufrufe = 2 · Rückgabe − 1 (jeder innere Knoten hat zwei Kinder); gemessen: schleim(100) = 33 mit 65 Aufrufen, schleim(1000) = 200 mit 399 Aufrufen.
- Fehlerfolie geprüft: ohne Basisfall und mit nur 5er-Schritten (muenzen(12): 12, 7, 2, −3, …) jeweils StackOverflowError; Fassung „Ergebnis nicht verwendet“ liefert für muenzen(12) und muenzen(9) jeweils 1.
- Pause-Folien: im Schnitt einen Hinweis „Video anhalten“ einblenden; die Auflösung kommt erst auf der nächsten Folie.
- Folien „Aufrufstapel“ und „Rekursionstabelle“: beim Abstieg die Zeilen von oben nach unten zeigen, beim Aufstieg die Rückgaben von unten nach oben.

## YouTube

**Titel:** Rekursion verstehen: Rekursionstabelle, Aufrufstapel, Aufrufbaum (Informatik-Abitur Niedersachsen) | Algo Quest #5

**Beschreibung:**

```
Wie funktioniert Rekursion – und wie dokumentierst du einen Rekursionsverlauf so, wie es das Informatik-Abitur in Niedersachsen verlangt? In diesem Video lernst du Basisfall und Rekursionsschritt, verfolgst den Aufrufstapel, führst eine Rekursionstabelle mit Rekursionstiefe (Erstaufruf = Tiefe 0), stellst eine rekursive Methode als Struktogramm nach EH §5 dar und zählst Aufrufe im Aufrufbaum. Dazu die typischen Fehler: fehlender Basisfall, nicht verwendetes Ergebnis, falsche Tiefe – und der StackOverflowError.

Teil der Unterrichtsreihe „Algo Quest – Das Dungeon der Datenstrukturen“ (Informatik eA).
Üben mit sofortiger Rückmeldung: https://algoquest.frankjuchim.de/themen

Kapitel:
0:00 Einstieg
0:53 Basisfall und Rekursionsschritt
1:48 Aufrufstapel
2:39 Rekursionstabelle
3:30 Selbst ausprobieren: Rekursionstabelle
4:29 Struktogramm
5:14 Aufrufbaum
6:41 Selbst ausprobieren: Aufrufbaum
7:44 Typische Fehler
9:08 Zusammenfassung
```

_Zeitmarken sind aus der Textlänge geschätzt – nach dem Schnitt anpassen._

**Tags:** Informatik Abitur, Niedersachsen, Rekursion, Rekursionstabelle, Rekursionstiefe, Aufrufbaum, StackOverflowError, Java, Informatik LK, Algo Quest

## Drehbuch

### Folie 1 · 0:00 – Rekursion verstehen

*Regie: Kamera unten rechts, Titelfolie im Hintergrund.*

Willkommen im Labyrinth der Algo Quest! Heute geht es um Rekursion – also um Methoden, die sich selbst aufrufen. Das klingt erst einmal nach einem Zaubertrick. Im Abitur ist es aber ganz handfestes Handwerk: Du sollst einen Rekursionsverlauf dokumentieren, Aufrufe zählen und rekursive Struktogramme zeichnen. Nach diesem Video weißt du, wie das geht – und welche Fehler dich dabei Punkte kosten.

### Folie 2 · 0:28 – Rekursion im Abitur

Typische Arbeitsaufträge im Abitur lauten zum Beispiel: Dokumentieren Sie den Rekursionsverlauf in einer Rekursionstabelle mit Rekursionstiefe. Bestimmen Sie die Anzahl der Aufrufe. Oder: Stellen Sie die Methode als Struktogramm dar. Eine Konvention solltest du dir sofort merken: Der Erstaufruf hat die Rekursionstiefe null, nicht eins. Rechts siehst du, was wir uns heute vornehmen.

### Folie 3 · 0:53 – Basisfall und Rekursionsschritt

Unser Beispiel: Der Händler im Dungeon zahlt Wechselgeld mit Fünfer- und Einer-Münzen, und zwar mit möglichst wenigen. Die Methode muenzen berechnet, wie viele Münzen er braucht. Jede Rekursion hat zwei Zutaten. Erstens den Basisfall: Hier steht die Antwort sofort fest, ganz ohne Selbstaufruf. Ist der Betrag null, braucht der Händler null Münzen. Zweitens den Rekursionsschritt: Der Händler wählt eine Münze – eine Fünf, wenn das geht, sonst eine Eins – und lässt in der rot markierten Zeile den Rest von muenzen selbst ausrechnen. Wichtig: Der Rest ist echt kleiner, also kommt jeder Aufruf dem Basisfall näher. Und: Das Ergebnis des Selbstaufrufs wird verwendet – eins plus den Rest. Der Trick beim Entwerfen: Vertraue darauf, dass der Selbstaufruf richtig rechnet.

### Folie 4 · 1:48 – Der Aufrufstapel: muenzen(12)

*Regie: Stapel von unten nach oben zeigen (Abstieg), dann von oben nach unten die Rückgaben (Aufstieg).*

Was passiert beim Aufruf muenzen von zwölf? Zwölf ist mindestens fünf, also wartet dieser Aufruf auf muenzen von sieben. Der wiederum wartet auf muenzen von zwei, der auf muenzen von eins, und der auf muenzen von null. Jeder Aufruf legt dabei einen eigenen Rahmen auf den Aufrufstapel, mit einer eigenen Variable betrag. Das ist der Abstieg. Ganz oben liegt jetzt muenzen von null – der Basisfall. Er liefert sofort null. Jetzt beginnt der Aufstieg: Der oberste Rahmen verschwindet, und sein Ergebnis wird im Rahmen darunter eingesetzt. Eins plus null ist eins, dann eins plus eins ist zwei, dann drei, und schließlich liefert der Erstaufruf vier. Vier Münzen: fünf, fünf, eins, eins.

### Folie 5 · 2:39 – Die Rekursionstabelle: muenzen(12)

*Regie: Erst die Spalten Tiefe, Aufruf, betrag von oben nach unten zeigen, dann die Rückgaben von unten nach oben.*

Genau diesen Ablauf schreibst du im Abitur als Rekursionstabelle auf. Die Spalten sind: Rekursionstiefe, Aufruf, die Parameter – hier betrag – und die Rückgabe. Beim Abstieg füllst du die Zeilen von oben nach unten: Der Erstaufruf muenzen von zwölf hat die Tiefe null, jeder Selbstaufruf eine Tiefe mehr. Die Rückgaben kannst du beim Abstieg noch nicht eintragen – sie stehen erst fest, wenn der Aufruf darunter fertig ist. Deshalb füllst du die Spalte Rückgabe beim Aufstieg von unten nach oben: null im Basisfall, dann eins plus null, eins plus eins und so weiter. Schreib die Rechnung ruhig mit hin, das macht deine Lösung nachvollziehbar. Ergebnis: fünf Aufrufe, größte Rekursionstiefe vier.

### Folie 6 · 3:30 – Kurz pausieren: Jetzt du!

Jetzt bist du dran. Halte das Video an und führe die Rekursionstabelle für muenzen von neun. Denk daran: Der Erstaufruf hat die Tiefe null, und die Rückgaben trägst du erst beim Aufstieg ein. Wenn du fertig bist, geht es weiter mit der Auflösung.

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 7 · 3:54 – Auflösung: muenzen(9)

Hier die Auflösung. Neun ist mindestens fünf, also geht es mit vier weiter. Ab jetzt ist der Betrag kleiner als fünf, und es geht in Einerschritten abwärts: drei, zwei, eins, null. Das sind sechs Aufrufe mit den Tiefen null bis fünf. Beim Aufstieg: null, eins, zwei, drei, vier – und der Erstaufruf liefert fünf. Der Händler zahlt also eine Fünf und vier Einer. Hattest du auch die Zeile für den Basisfall? Sie gehört dazu.

### Folie 8 · 4:29 – Rekursive Struktogramme nach EH §5

Und wie sieht das als Struktogramm aus? Ganz oben steht wie immer der Kopf: muenzen, betrag vom Typ Ganzzahl, Rückgabetyp Ganzzahl. Dann kommt zuerst der Basisfall als Verzweigung: Ist betrag gleich null, gib null zurück. Im Falsch-Zweig steht der Rekursionsschritt: muenze bekommt eins, und wenn betrag mindestens fünf ist, bekommt muenze fünf. Der Selbstaufruf braucht kein besonderes Symbol – er ist eine ganz normale Anweisung, hier innerhalb von gib eins plus muenzen von betrag minus muenze zurück. Achte darauf, dass jeder Pfad mit gib zurück endet, und schreib keine Java-Syntax: Pfeil statt Gleichheitszeichen, größer gleich als ein Zeichen.

### Folie 9 · 5:14 – Baumrekursion: zwei Selbstaufrufe

Bisher hatte jeder Aufruf höchstens einen Selbstaufruf – die Aufrufe bilden eine Kette. Jetzt ein Monster aus dem Labyrinth: ein Schleim. Trifft man einen Schleim der Größe n, zerfällt er in zwei Schleime, einen der Größe n durch zwei und einen der Größe n durch drei, jeweils ganzzahlig. Schleime kleiner als zwei zerfallen nicht mehr. Die Methode schleim zählt, wie viele Mini-Schleime am Ende übrig sind. In der markierten Zeile stehen zwei Selbstaufrufe. Das nennt man Baumrekursion, denn die Aufrufe verzweigen sich wie ein Baum.

### Folie 10 · 5:53 – Der Aufrufbaum von schleim(7)

*Regie: Reihenfolge des Beginns mit dem Mauszeiger zeigen: s7, s3, s1, s1, s2, s1, s0.*

Hier der Aufrufbaum für schleim von sieben. Jeder Knoten ist ein Aufruf; s drei steht für schleim von drei. Die Wurzel ist der Erstaufruf mit Tiefe null. Sieben durch zwei ist drei, sieben durch drei ist zwei. Java wertet die Summe von links nach rechts aus: Erst wird der linke Teilbaum komplett abgearbeitet – s drei mit seinen beiden Kindern s eins und s eins –, erst danach beginnt s zwei mit s eins und s null. Zum Zählen der Aufrufe zählst du einfach alle Knoten: sieben Aufrufe. Die größte Tiefe ist zwei. Und jedes Blatt liefert eins, also ist schleim von sieben gleich vier.

### Folie 11 · 6:41 – Kurz pausieren: Zeichne den Aufrufbaum!

Jetzt du: Halte das Video an und zeichne den Aufrufbaum für schleim von zehn. Bestimme den Rückgabewert, die Anzahl aller Aufrufe und die größte Rekursionstiefe. Denk an die ganzzahlige Division.

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 12 · 7:00 – Auflösung: schleim(10)

Die Auflösung: Zehn zerfällt in fünf und drei. Fünf zerfällt in zwei und eins, zwei in eins und null, drei in eins und eins. Der Baum hat neun Knoten, also neun Aufrufe. Der längste Ast führt von s zehn über s fünf und s zwei bis s eins – das ist Tiefe drei, denn die Wurzel hat Tiefe null. Fünf Blätter, also liefert schleim von zehn den Wert fünf. Übrigens: Weil jeder innere Knoten genau zwei Kinder hat, gilt hier immer: Aufrufe gleich zwei mal Blätter minus eins. So kannst du dein Ergebnis kontrollieren.

### Folie 13 · 7:44 – Typische Fehler (P7) – und der StackOverflowError

Jetzt zu den typischen Fehlern, in unserer Fallen-Liste unter P7. Fehler eins: Der Basisfall fehlt. Dann ruft sich die Methode immer weiter selbst auf. Jeder Aufruf belegt einen Rahmen auf dem Aufrufstapel, bis der Speicher voll ist – Java bricht mit einem StackOverflowError ab. Fehler zwei ist tückischer: Der Basisfall ist da, wird aber übersprungen. Gibt es nur Fünferschritte, geht es von zwölf über sieben und zwei direkt zu minus drei – null wird nie getroffen, wieder ein StackOverflowError. Fehler drei: Der Selbstaufruf steht zwar da, aber sein Ergebnis wird weggeworfen. Das Programm läuft, liefert aber immer eins. Merke: Das Ergebnis des Selbstaufrufs muss verwendet werden.

### Folie 14 · 8:33 – Fehler in Tabelle, Baum und Struktogramm

Auch in Tabellen und Bäumen gehen schnell Punkte verloren. Falle P7: Die Tiefe beginnt bei eins statt bei null. Im Abitur gilt: Der Erstaufruf hat die Tiefe null. Falle P8: Die Rückgaben werden schon beim Abstieg eingetragen, oder die Zeile für den Basisfall fehlt. Beim Zählen der Aufrufe gilt: Der Erstaufruf und alle Basisfälle zählen mit – jeder Knoten im Aufrufbaum ist ein Aufruf. Und Falle P9: Java-Syntax im Struktogramm. Rechts der Abi-Check für deine Lösung.

### Folie 15 · 9:08 – Das nimmst du mit

Fassen wir zusammen. Jede Rekursion braucht einen Basisfall und einen Rekursionsschritt, der dem Basisfall näherkommt und das Ergebnis des Selbstaufrufs verwendet. Beim Ausführen geht es erst hinab bis zum Basisfall und dann mit den Rückgaben wieder hinauf. In der Rekursionstabelle steht der Erstaufruf mit Tiefe null, die Rückgaben füllst du von unten nach oben. Und bei Baumrekursion zeichnest du den Aufrufbaum: Jeder Knoten ist ein Aufruf.

### Folie 16 · 9:38 – 

Und jetzt ab ins Lab! In Level drei Punkt eins, dem Spiegelsaal, übst du Basisfall und Rekursionstabelle, in Level drei Punkt zwei, der Hydra, Aufrufbäume und das Zählen von Aufrufen. Auf dem Arbeitsblatt Rekursion findest du alles noch einmal zum Nachlesen. Im nächsten Video geht es um Stapel und Schlange – und übrigens: Den Aufrufstapel hast du heute schon kennengelernt. Bis dahin – viel Erfolg im Labyrinth!
