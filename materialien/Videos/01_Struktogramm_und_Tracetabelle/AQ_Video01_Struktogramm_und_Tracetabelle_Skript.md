# Erklärvideo 1: Struktogramm und Tracetabelle

> So schreibst du Algorithmen auf, wie es das Abitur verlangt

| | |
|---|---|
| **Welt** | Welt 0 · Die Akademie |
| **Zielgruppe** | Informatik eA (LK), Beginn der Einheit; auch zur Wiederholung vor dem Abitur |
| **Länge** | Ziel 8–10 min · Sprechtext ca. 9:00 min (bei 130 Wörtern/min, inkl. Pausen) |
| **Einsatz** | Welt 0, DS 1–2 (Portal, Werkstatt) · Lab-Level 0.1 und 0.2 · AB W0·1 „Das Portal“, Werkzeugkarten |
| **Folien** | `AQ_Video01_Struktogramm_und_Tracetabelle_Folien.pptx` (15 Folien, Sprechertext auch in den Notizen) |

## Lernziele

- Bausteine eines Struktogramms nach EH §5 kennen: Kopf mit Signatur, Zuweisung mit ←, „gib … zurück“, Verzweigung, Schleifen
- Eine Java-Methode in ein Struktogramm übersetzen – ohne Java-Syntax
- Eine Tracetabelle nach unserer Konvention führen: nur Variablen, eine Zeile an jeder mit „// → Tabellenzeile“ markierten Stelle
- Typische Punktverluste (P4, P6, P8, P9) vermeiden

## Hinweise für die Aufnahme

- Alle Beispiele (jahreBisZiel, anzahlInBereich) sind eigens für das Video gewählt und kommen in Lab, Arbeitsblättern und Bossen nicht vor – so verrät das Video keine Lösungen.
- Werte geprüft mit javac/java: jahreBisZiel(100, 150) = 5, jahreBisZiel(50, 70) = 4, anzahlInBereich({12, 4, 18, 9, 15}, 5, 15) = 3.
- Folie „Kurz pausieren“: im Schnitt einen Hinweis „Video anhalten“ einblenden; die Lösung kommt erst auf der nächsten Folie.
- Folie „Trace: jahreBisZiel(100, 150)“: die Tabellenzeilen nacheinander mit Laserpointer bzw. Maus zeigen.

## YouTube

**Titel:** Struktogramm und Tracetabelle fürs Informatik-Abitur (Niedersachsen) | Algo Quest #1

**Beschreibung:**

```
Wie schreibt man Algorithmen so auf, wie es das Informatik-Abitur in Niedersachsen verlangt? In diesem Video lernst du die Struktogramm-Notation nach den Ergänzenden Hinweisen (§5) und wie du eine Tracetabelle sauber führst – nur Variablen, eine Zeile an jeder markierten Stelle.

Teil der Unterrichtsreihe „Algo Quest – Das Dungeon der Datenstrukturen“ (Informatik eA).
Üben mit sofortiger Rückmeldung: https://algoquest.frankjuchim.de/themen

Kapitel:
0:00 Einstieg
1:07 Bausteine
2:06 Von Java zum Struktogramm
4:43 Tracetabelle
6:18 Selbst ausprobieren
7:11 Typische Fehler
7:58 Zusammenfassung
```

_Zeitmarken sind aus der Textlänge geschätzt – nach dem Schnitt anpassen._

**Tags:** Informatik Abitur, Niedersachsen, Struktogramm, Tracetabelle, Java, Informatik LK, Algo Quest

## Drehbuch

### Folie 1 · 0:00 – Struktogramm und Tracetabelle

*Regie: Kamera unten rechts, freundlicher Einstieg, Titelfolie im Hintergrund.*

Hallo und willkommen zur Algo Quest! In diesem Video geht es um zwei Werkzeuge, die du im Informatik-Abitur ständig brauchst: das Struktogramm und die Tracetabelle. Mit dem Struktogramm schreibst du einen Algorithmus so auf, dass jeder ihn versteht – ganz ohne Programmiersprache. Und mit der Tracetabelle zeigst du Schritt für Schritt, was ein Programm tatsächlich tut. Am Ende des Videos weißt du, wie beides aussehen muss, damit du keine Punkte verschenkst.

### Folie 2 · 0:33 – Worum geht es im Abitur?

Im Abitur begegnen dir dazu vor allem zwei Arbeitsaufträge. Erstens: Stellen Sie den Algorithmus als Struktogramm dar. Zweitens: Dokumentieren Sie den Ablauf in einer Tracetabelle. Wie ein Struktogramm genau aussehen soll, ist in den Ergänzenden Hinweisen zum Abitur festgelegt, im Paragrafen fünf. Das Wichtigste vorweg: Ein Struktogramm ist sprachunabhängig. Es enthält also keine Java-Syntax – kein Gleichheitszeichen als Zuweisung, kein i plus plus, keine geschweiften Klammern. Schauen wir uns an, welche Bausteine es gibt.

### Folie 3 · 1:07 – Die Bausteine nach EH §5

Ganz oben steht der Kopf mit der Signatur: der Name, in Klammern die Parameter mit ihrem Typ und hinter dem Doppelpunkt der Rückgabetyp. Als Typnamen verwendest du die deutschen Namen: Ganzzahl, Kommazahl, Wahrheitswert, Zeichen, Zeichenkette – und nichts, wenn nichts zurückgegeben wird. Darunter folgen die Anweisungen von oben nach unten. Eine Zuweisung schreibst du mit dem Pfeil nach links: x bekommt den Wert null. Die Verzweigung erkennst du am Dreieck: Oben steht die Bedingung, links geht es weiter, wenn sie wahr ist, rechts, wenn sie falsch ist. Für Schleifen gibt es die Zählschleife – für i von null bis n minus eins – und die Solange-Schleife, die vor jedem Durchlauf ihre Bedingung prüft. Der Rumpf einer Schleife ist eingerückt. Und mit gib x zurück endet die Methode.

### Folie 4 · 2:06 – Von Java zum Struktogramm

Jetzt ein Beispiel aus dem Dungeon: Ein Held legt sein Gold an und bekommt jedes Jahr zehn Prozent Zinsen. Die Methode jahreBisZiel berechnet, wie viele Jahre es dauert, bis er sein Ziel erreicht. Achte schon jetzt auf die Zeile gold gleich gold plus gold durch zehn: Das ist eine ganzzahlige Division, der Rest fällt weg. Übersetzen wir das Ganze jetzt Zeile für Zeile in ein Struktogramm.

### Folie 5 · 2:36 – … als Struktogramm

Der Methodenkopf wird zur Signatur: jahreBisZiel, gold vom Typ Ganzzahl, ziel vom Typ Ganzzahl, Rückgabetyp Ganzzahl. Aus int jahre gleich null wird jahre bekommt null – mit dem Pfeil. Die while-Schleife wird zur Solange-Schleife: solange gold kleiner als ziel. Ihr Rumpf ist eingerückt. Darin steht gold bekommt gold plus gold durch zehn, und aus jahre plus plus wird jahre bekommt jahre plus eins. Am Ende steht: gib jahre zurück. Fertig ist das Struktogramm – ohne eine einzige Zeile Java-Syntax.

### Folie 6 · 3:12 – Spickzettel: Java → Struktogramm

Diese Übersetzungen brauchst du immer wieder, deshalb hier als Spickzettel. Die Zuweisung wird zum Pfeil. Ein Vergleich auf Gleichheit, in Java das doppelte Gleichheitszeichen, wird im Struktogramm zu einem einfachen Gleichheitszeichen. Ungleich, kleiner gleich und größer gleich schreibst du mit den mathematischen Zeichen. Die logischen Operatoren schreibst du aus: und, oder, nicht. Der Rest einer Division heißt mod. Und besonders wichtig: Die for-Schleife von null bis kleiner n wird zu für i von null bis n minus eins. Das minus eins vergisst man leicht – dazu gleich mehr bei den Fehlern.

### Folie 7 · 3:54 – Zweites Beispiel: mit Verzweigung

Ein zweites Beispiel, diesmal mit Verzweigung. Die Methode zählt, wie viele Werte einer Reihung zwischen lo und hi liegen. Für die Reihung zwölf, vier, achtzehn, neun, fünfzehn und den Bereich fünf bis fünfzehn sind das drei Werte: zwölf, neun und fünfzehn.

### Folie 8 · 4:13 – … als Struktogramm

Die for-Schleife wird zur Zählschleife: für i von null bis Länge von r minus eins. Das if wird zum Dreieck mit der Bedingung oben. In der Bedingung schreibst du nicht das doppelte kaufmännische Und, sondern das Wort und. Der Wahr-Zweig erhöht anzahl um eins. Der Falsch-Zweig ist leer – im Struktogramm steht dort das Zeichen für die leere Menge. Ganz unten wieder: gib anzahl zurück.

### Folie 9 · 4:43 – Die Tracetabelle: unsere Regeln

Kommen wir zur Tracetabelle. Wir halten uns in der Algo Quest an feste Regeln. Erstens: Es gibt eine Spalte für jede Variable, dazu bei Bedarf eine Spalte für den Durchlauf und am Ende die Rückgabe. Zweitens: Bedingungen bekommen keine eigene Spalte. Ob gold kleiner als ziel ist, siehst du ja an den Werten. Drittens: Wann eine neue Zeile entsteht, steht im Code. An jeder Stelle mit dem Kommentar Pfeil Tabellenzeile trägst du eine Zeile ein. Die Markierung mit Startwerte steht vor der Schleife, die andere am Ende des Schleifenrumpfs. So bleibt die Tabelle klein, und jede Zeile zeigt einen klar festgelegten Zeitpunkt.

### Folie 10 · 5:30 – Trace: jahreBisZiel(100, 150)

*Regie: Zeilen der Tabelle nacheinander zeigen; bei Zeile 3 auf 121 / 10 = 12 hinweisen.*

Probieren wir es aus: jahreBisZiel mit hundert Gold und dem Ziel hundertfünfzig. Die erste Markierung steht vor der Schleife. Hier tragen wir die Startwerte ein: gold hundert, jahre null. Jetzt läuft die Schleife. Hundert ist kleiner als hundertfünfzig, also rechnen wir: hundert plus zehn gleich hundertzehn, jahre wird eins. Am Ende des Rumpfs steht die Markierung – neue Zeile. Nächster Durchlauf: hundertzehn plus elf gleich hunderteinundzwanzig. Dann hunderteinundzwanzig durch zehn – ganzzahlig! – ist zwölf, also hundertdreiunddreißig. Dann plus dreizehn: hundertsechsundvierzig. Und schließlich plus vierzehn: hundertsechzig, jahre ist fünf. Jetzt ist hundertsechzig nicht mehr kleiner als hundertfünfzig, die Schleife endet. Rückgabe: fünf.

### Folie 11 · 6:18 – Kurz pausieren: Jetzt du!

Jetzt bist du dran. Halte das Video an und führe die Tracetabelle für jahreBisZiel mit fünfzig Gold und dem Ziel siebzig. Denk an die Startzeile und an die ganzzahlige Division. Wenn du fertig bist, geht es weiter mit der Auflösung.

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 12 · 6:41 – Auflösung: jahreBisZiel(50, 70)

Hier die Auflösung. Start: gold fünfzig, jahre null. Fünfzig durch zehn ist fünf, also fünfundfünfzig. Fünfundfünfzig durch zehn ist ebenfalls fünf – der Rest fällt weg – also sechzig. Dann sechzig plus sechs: sechsundsechzig. Und sechsundsechzig plus sechs: zweiundsiebzig. Zweiundsiebzig ist nicht kleiner als siebzig, die Schleife endet. Die Methode gibt vier zurück. Hattest du fünf Zeilen, also auch die Startzeile? Dann ist deine Tabelle vollständig.

### Folie 13 · 7:11 – Typische Fehler – und wie du sie vermeidest

Zum Schluss die häufigsten Fehler – mit den Nummern aus unserer Fallen-Liste. Falle P9: Java-Syntax im Struktogramm, etwa ein Gleichheitszeichen statt des Pfeils, i plus plus oder das doppelte kaufmännische Und. Falle P6, der Klassiker: für i von null bis n. Richtig ist bis n minus eins, sonst greifst du hinter das Ende der Reihung. Falle P8: In der Tracetabelle fehlt die Startzeile, oder es gibt doch eine Spalte für die Bedingung. Falle P4: die ganzzahlige Division übersehen. Und ganz banal: den Rückgabewert nicht angeben. Rechts siehst du einen kleinen Abi-Check, mit dem du deine Lösung vor der Abgabe prüfen kannst.

### Folie 14 · 7:58 – Das nimmst du mit

Fassen wir zusammen. Ein Struktogramm nach EH Paragraf fünf hat einen Kopf mit Signatur und deutschen Typnamen, Zuweisungen mit dem Pfeil und endet mit gib zurück. Verzweigungen sind Dreiecke, Schleifen werden eingerückt. Java-Syntax hat im Struktogramm nichts zu suchen. Und in der Tracetabelle stehen nur Variablen – eine neue Zeile gibt es genau an den markierten Stellen.

### Folie 15 · 8:24 – 

Und jetzt du! Im Algo Quest Lab findest du dazu Level null Punkt eins, das Portal, und Level null Punkt zwei, die Werkstatt. Dort bekommst du zu jeder Aufgabe sofort eine Rückmeldung. Auf dem Arbeitsblatt Das Portal findest du die Regeln noch einmal zum Nachlesen, und auf den Werkzeugkarten hast du den Spickzettel immer dabei. Im nächsten Video zeige ich dir die Online-IDE, mit der wir programmieren und testen. Bis dahin – viel Erfolg in der Akademie!
