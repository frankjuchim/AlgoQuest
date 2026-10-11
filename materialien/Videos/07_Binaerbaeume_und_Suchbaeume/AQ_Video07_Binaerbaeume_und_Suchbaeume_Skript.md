# Erklärvideo 7: Binärbäume und Suchbäume

> Begriffe, BinTree, Traversierungen und der binäre Suchbaum

| | |
|---|---|
| **Welt** | Welt 5 · Der Wald |
| **Zielgruppe** | Informatik eA (LK), Welt 5; auch zur Wiederholung vor dem Abitur |
| **Länge** | Ziel 10–12 min · Sprechtext ca. 10:31 min (bei 130 Wörtern/min, inkl. Pausen) |
| **Einsatz** | Welt 5, DS 31–34 · Lab-Level 5.1, 5.2 und 5.4 · AB W5·1 „Binärbäume“, AB W5·2 „Suchbäume“ |
| **Folien** | `AQ_Video07_Binaerbaeume_und_Suchbaeume_Folien.pptx` (18 Folien, Sprechertext auch in den Notizen) |

## Lernziele

- Baumbegriffe sicher verwenden: Wurzel, Blatt, innerer Knoten, Teilbaum, Ebene (Wurzel = Ebene 0) und Höhe (leerer Baum 0, Blatt 1)
- Einen Baum mit der BinTree-Schnittstelle nach EH §4 aufbauen und Inhalte casten (nicht generisch)
- Pre-, In- und Postorder eines Baums von Hand angeben
- Rekursive Baummethoden nach dem Muster „erst isEmpty, dann links und rechts“ schreiben
- Im binären Suchbaum suchen und einfügen; wissen, warum die Inorder sortiert ist; P1 und P7 vermeiden

## Hinweise für die Aufnahme

- Alle Bäume und Zahlen sind eigens für das Video gewählt: Beispielbaum 11(6(2,9(5,-)),3(-,8)), Pause-Baum 7(1(-,4),9(3,-)), Suchbaum aus 27, 14, 39, 9, 21, 33, 45, 17. Sie kommen in Lab, Arbeitsblättern, Warm-up und Bossen nicht vor (geprüft gegen seed/welten/welt5.json, Baumschule der Spec und die W5-Materialien); beispielBST() und zahlenbaum() werden bewusst nicht verwendet.
- Geprüft mit javac/java gegen den Nachbau der NI-Bibliothek (werkzeuge/ide-pruefung/java/aq/ni): Aufbau-Code ergibt 11(6(2,9(5,-)),3(-,8)), x = 6; preorder 11 6 2 9 5 3 8, inorder 2 6 5 9 11 3 8, postorder 2 5 9 6 8 3 11; 7 Knoten, Höhe 4, Blätter 2, 5, 8; Ebene von 5 ist 3; summeBlaetter = 15 (Zwischenwerte 9 → 5, 6 → 7, 3 → 8, 11 → 15); Höhe leerer Baum 0, Blatt 1.
- Pause 1 geprüft: 7(1(-,4),9(3,-)) → preorder 7 1 4 9 3, inorder 1 4 7 3 9, postorder 4 1 3 9 7.
- Pause 2 geprüft: 42, 12, 30 in den Suchbaum (ohne 36) → 27(14(9(-,12),21(17,-)),39(33(30,-),45(42,-))), Wege 42: 27 39 45 · 12: 27 14 9 · 30: 27 39 33; inorder 9 12 14 17 21 27 30 33 39 42 45; Höhe bleibt 4; erneutes Einfügen von 21 ändert nichts.
- Fehlerfolie geprüft: die fehlerhafte Methode wirft beim ersten leeren Teilbaum IllegalStateException (getItem auf leerem Baum); ohne diesen Fehler liefert die Version ohne verwendete Ergebnisse für den Beispielbaum 0 statt 15.
- Pause-Folien: im Schnitt „Video anhalten“ einblenden; die Lösung kommt jeweils erst auf der nächsten Folie. Bei den Suchwegen die Knoten mit dem Mauszeiger nachfahren (der Renderer kann Knoten nicht farbig markieren).
- Suchen und Einfügen im Suchbaum bewusst ohne Java-Code (der Code ist die Lösung von IDE-Level 5.4) – nur das Verfahren und die Suchwege.

## YouTube

**Titel:** Binärbäume und binäre Suchbäume fürs Informatik-Abitur (Niedersachsen) | Algo Quest #7

**Beschreibung:**

```
Binärbäume im Informatik-Abitur Niedersachsen: Begriffe wie Wurzel, Blatt, Ebene und Höhe, die Schnittstelle BinTree nach den Ergänzenden Hinweisen (§4), die Traversierungen preorder, inorder und postorder, das rekursive Muster für Baummethoden und der binäre Suchbaum mit Suchen und Einfügen – mit Pause-Aufgaben zum Mitmachen.

Teil der Unterrichtsreihe „Algo Quest – Das Dungeon der Datenstrukturen“ (Informatik eA).
Üben mit sofortiger Rückmeldung: https://algoquest.frankjuchim.de/themen

Kapitel:
0:00 Einstieg
0:47 Begriffe und Höhe
1:50 BinTree
3:12 Traversierungen
3:56 Selbst ausprobieren: Traversierungen
4:43 Rekursives Muster
5:57 Suchbaum
7:58 Selbst ausprobieren: Einfügen
8:45 Typische Fehler
9:31 Zusammenfassung
```

_Zeitmarken sind aus der Textlänge geschätzt – nach dem Schnitt anpassen._

**Tags:** Informatik Abitur, Niedersachsen, Binärbaum, binärer Suchbaum, Traversierung, preorder inorder postorder, Rekursion, Java, Informatik LK, Algo Quest

## Drehbuch

### Folie 1 · 0:00 – Binärbäume und Suchbäume

*Regie: Kamera unten rechts, Titelfolie im Hintergrund.*

Hallo und willkommen zur Algo Quest! Heute geht es in den Wald – zu den Binärbäumen. Bäume stecken in Dateisystemen, in Entscheidungen und in schnellen Datenbanken. Im Abitur kommen sie fast jedes Jahr vor. Am Ende dieses Videos kannst du einen Baum beschreiben, durchlaufen, rekursiv auswerten – und im Suchbaum blitzschnell suchen.

### Folie 2 · 0:24 – Bäume im Abitur

Typische Aufträge lauten etwa: Geben Sie die Ausgabe der Inorder-Traversierung an. Implementieren Sie die Methode rekursiv. Oder: Fügen Sie die Werte in den Suchbaum ein und stellen Sie ihn dar. Programmiert wird mit der Klasse BinTree aus den Ergänzenden Hinweisen, Paragraf vier. Rechts siehst du unseren Weg durch dieses Video.

### Folie 3 · 0:47 – Begriffe, Ebene und Höhe

*Regie: Begriffe am Bild zeigen; bei der Höhe die vier Ebenen von oben nach unten abzählen.*

Hier ist unser Beispielbaum. Ganz oben steht die Wurzel, die Elf. Knoten ohne Kinder heißen Blätter – das sind die Zwei, die Fünf und die Acht. Alle anderen sind innere Knoten. Jedes Kind bildet mit allem, was darunter hängt, einen Teilbaum: Die Sechs ist zum Beispiel die Wurzel des linken Teilbaums. Die Ebene gibt den Abstand zur Wurzel an: Die Wurzel liegt auf Ebene null, die Sechs und die Drei auf Ebene eins, die Fünf auf Ebene drei. Die Höhe zählt die Ebenen: Unser Baum hat die Höhe vier. Merke dir die Konvention, die wir in der ganzen Algo Quest verwenden: Der leere Baum hat die Höhe null, ein einzelnes Blatt die Höhe eins. Sonst ist die Höhe eins plus die größere der beiden Teilbaum-Höhen. Achtung, Verwechslungsgefahr: Ebenen zählen ab null, die Höhe zählt die Ebenen.

### Folie 4 · 1:50 – Die Schnittstelle BinTree nach EH §4

Die Schnittstelle ist klein. Der eine Konstruktor erzeugt einen leeren Baum, der andere ein Blatt mit einem Inhalt. isEmpty fragt, ob der Baum leer ist, isLeaf, ob beide Teilbäume leer sind. Mit getItem liest du den Inhalt der Wurzel, mit getLeft und getRight die Teilbäume, mit setLeft und setRight hängst du Teilbäume an. Wichtig: Diese Methoden lösen bei einem leeren Baum einen Laufzeitfehler aus – das sind die rot markierten Zeilen. Ein nicht leerer Baum hat übrigens immer zwei Teilbäume. Die können leer sein, aber sie sind nie null. Und: BinTree ist nicht generisch. Der Inhalt ist ein Object, also musst du casten, zum Beispiel int x gleich Klammer Integer b punkt getItem.

### Folie 5 · 2:42 – Einen Baum aufbauen

So entsteht unser Baum im Code. Zuerst die Wurzel elf, dann links die Sechs und rechts die Drei. Mit getLeft punkt setLeft hängst du eine Ebene tiefer an. Spannend ist Zeile sieben: Der rechte Teilbaum der Drei ist leer – er existiert aber. setItem macht ihn direkt zum Blatt mit der Acht. In Zeile acht lesen wir die Sechs wieder aus – mit Cast auf Integer.

### Folie 6 · 3:12 – Drei Wege durch den Baum

*Regie: Bei preorder den Weg im Bild nachfahren: 11, links hinab bis 2, dann 9, 5, zurück zur 3, dann 8.*

Wie gibt man alle Knoten aus? Es gibt drei Reihenfolgen. Bei preorder kommt zuerst die Wurzel, dann der linke, dann der rechte Teilbaum. Und das gilt in jedem Teilbaum erneut. Also: elf, dann der linke Teilbaum mit der Sechs: sechs, zwei, neun, fünf. Dann rechts: drei, acht. Bei inorder steht die Wurzel in der Mitte: erst alles links, dann die Elf, dann rechts. Bei postorder kommt die Wurzel zum Schluss – die Elf steht also ganz hinten. Ein Tipp für die Prüfung: Kontrolliere am Ende, ob jede Folge alle sieben Werte genau einmal enthält.

### Folie 7 · 3:56 – Kurz pausieren: Jetzt du!

Jetzt du! Halte das Video an und gib für diesen Baum alle drei Traversierungen an. Tipp: Jede Folge muss alle fünf Werte genau einmal enthalten.

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 8 · 4:12 – Auflösung: Traversierungen

Preorder: Wurzel sieben, dann der linke Teilbaum – die Eins und ihr rechtes Kind, die Vier –, dann rechts neun und drei. Inorder: Wir gehen von der Sieben nach links. Die Eins hat links nichts, also kommt zuerst die Eins, dann die Vier, dann die Sieben, dann drei, neun. Postorder: vier, eins, drei, neun – und die Sieben ganz zum Schluss. Hattest du überall fünf Werte? Prima.

### Folie 9 · 4:43 – Das Muster: erst isEmpty, dann links und rechts

Fast jede Baummethode folgt demselben Muster. Unser Beispiel: summeBlaetter addiert die Werte aller Blätter. Schritt eins: Ist der Baum leer? Dann ist das Ergebnis null – der Basisfall. Erst danach darfst du auf getItem und die Teilbäume zugreifen. Hier gibt es noch einen Sonderfall: Ein Blatt liefert seinen eigenen Wert. Schritt zwei: Die Methode ruft sich für den linken und den rechten Teilbaum auf. Schritt drei: Die beiden Ergebnisse werden verwendet und kombiniert – hier addiert.

### Folie 10 · 5:18 – So rechnet summeBlaetter

So läuft das für unseren Baum. Die Methode steigt zuerst ganz nach links hinab. Das Blatt zwei liefert seinen Wert. Dann geht es zur Neun: Ihr linkes Kind, das Blatt fünf, liefert fünf, ihr rechter Teilbaum ist leer und liefert null – also gibt die Neun fünf zurück. Die Sechs bekommt zwei und fünf, macht sieben. Rechts liefert die Drei null und acht, also acht. Und die Wurzel addiert sieben und acht: fünfzehn. Die Rückgaben entstehen also von unten nach oben – in Postorder.

### Folie 11 · 5:57 – Der binäre Suchbaum

Jetzt der binäre Suchbaum, die wichtigste Baumart im Abitur. Hier gilt für jeden Knoten: Alles im linken Teilbaum ist kleiner, alles im rechten Teilbaum größer. Und zwar nicht nur bei den direkten Kindern, sondern bis ganz unten: Auch die Siebzehn ist kleiner als die Siebenundzwanzig, weil sie im linken Teilbaum der Wurzel liegt. Diesen Baum haben wir durch Einfügen der Werte in genau dieser Reihenfolge gebaut. Eine andere Reihenfolge ergibt einen anderen Baum. Und schau dir die Inorder an: Sie ist sortiert. Warum, klären wir gleich.

### Folie 12 · 6:37 – Suchen: immer nur ein Teilbaum

*Regie: Suchwege im Bild mit der Maus nachfahren.*

Diese Ordnung macht das Suchen schnell. Wieder zuerst: Ist der Baum leer, ist der Wert nicht da. Sonst vergleichen wir mit der Wurzel. Gleich? Gefunden. Kleiner? Dann kann der Wert nur links liegen – rechts müssen wir gar nicht suchen. Suchen wir die Siebzehn: siebenundzwanzig, nach links zur Vierzehn, nach rechts zur Einundzwanzig, nach links – gefunden. Die Fünfunddreißig: siebenundzwanzig, neununddreißig, dreiunddreißig, dann rechts ein leerer Baum – falsch. Höchstens so viele Vergleiche, wie der Baum hoch ist. Bei einem ausgeglichenen Baum mit tausend Werten sind das nur etwa zehn Vergleiche.

### Folie 13 · 7:19 – Einfügen: suchen, bis es leer wird

Einfügen heißt: so tun, als ob man sucht – bis ein leerer Teilbaum kommt. Dort wird der neue Wert als Blatt angehängt – und zwar automatisch an der richtigen Stelle. Fügen wir sechsunddreißig ein: größer als siebenundzwanzig, kleiner als neununddreißig, größer als dreiunddreißig – und rechts von der Dreiunddreißig ist es leer. Ist der Wert schon da, passiert nichts. Beachte: Der neue Wert wird immer als Blatt angehängt – bestehende Knoten verschieben sich nie. Deshalb hängt die Form des Baums von der Einfügereihenfolge ab.

### Folie 14 · 7:58 – Kurz pausieren: Jetzt du!

Jetzt du! Nimm den Suchbaum ohne die Sechsunddreißig. Füge nacheinander zweiundvierzig, zwölf und dreißig ein, zeichne den Baum und gib die Inorder an. Halte das Video an!

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 15 · 8:15 – Auflösung: 42, 12 und 30 eingefügt

Die Zweiundvierzig wandert nach rechts, rechts, und landet links an der Fünfundvierzig. Die Zwölf geht links, links und landet rechts an der Neun. Die Dreißig landet links an der Dreiunddreißig. Und die Inorder ist wieder sortiert. Warum? Inorder gibt erst den linken Teilbaum aus, dann die Wurzel, dann den rechten. Links ist alles kleiner, rechts alles größer – und das gilt in jedem Teilbaum.

### Folie 16 · 8:45 – Typische Fehler

Zum Schluss die Fallen. In dieser Version stecken zwei. Falle P1: getItem steht vor der Abfrage isEmpty. Beim ersten leeren Teilbaum gibt es einen Laufzeitfehler – die Abfrage kommt zu spät. Falle P7: Die rekursiven Aufrufe werden zwar gemacht, aber ihre Ergebnisse landen nirgends. Die Methode liefert null statt fünfzehn. Und denk an P4: ohne Cast auf Integer meckert der Compiler. Im Suchbaum gilt außerdem: nur in einen Teilbaum absteigen, sonst verschenkst du den Vorteil. Mein Tipp für die Prüfung: Schreib bei jeder Baummethode als Erstes die Zeile if b punkt isEmpty hin – dann bist du auf der sicheren Seite.

### Folie 17 · 9:31 – Das nimmst du mit

Fassen wir zusammen. Die Wurzel liegt auf Ebene null, der leere Baum hat Höhe null, ein Blatt Höhe eins. BinTree ist nicht generisch, also immer casten. Die drei Traversierungen unterscheiden sich nur darin, wann die Wurzel drankommt: vorher, in der Mitte oder danach. Rekursive Baummethoden prüfen zuerst isEmpty, rufen sich für links und rechts auf und verwenden die Ergebnisse. Und im Suchbaum gehst du immer nur in einen Teilbaum – deshalb ist er so schnell.

### Folie 18 · 10:06 – 

Und jetzt ab in den Wald! Im Algo Quest Lab warten Level fünf eins, fünf zwei und fünf vier auf dich – mit sofortiger Rückmeldung. Auf den Arbeitsblättern Binärbäume und Suchbäume kannst du alles nachlesen. Im nächsten Video machen wir den Abi-Check: die zehn Fallen, die im Abitur am meisten Punkte kosten. Bis dahin!
