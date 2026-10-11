# Erklärvideo 6: Stapel und Schlange

> Schnittstellen nach EH §4, Casts und Laufzeitfehler vermeiden

| | |
|---|---|
| **Welt** | Welt 4 · Der Hafen |
| **Zielgruppe** | Informatik eA (LK), Welt 4; auch zur Wiederholung vor Boss, Klausur und Abitur |
| **Länge** | Ziel 9–11 min · Sprechtext ca. 10:11 min (bei 130 Wörtern/min, inkl. Pausen) |
| **Einsatz** | Welt 4, DS 24 und 26 · Lab-Level 4.1 „Kistenturm und Schiffsschlange“ und 4.3 „Inventur“ · AB W4·1 „Stapel und Schlange“, AB W4·2 Teil 1 |
| **Folien** | `AQ_Video06_Stapel_und_Schlange_Folien.pptx` (15 Folien, Sprechertext auch in den Notizen) |

## Lernziele

- Den Begriff abstrakter Datentyp erklären: Schnittstelle statt Implementierung
- Die Schnittstellen von Stapel (Stack) und Schlange (Queue) nach EH §4 bzw. der Bibliothek „Niedersachsen“ sicher verwenden
- LIFO und FIFO unterscheiden und Befehlsfolgen (auch gemischt) Schritt für Schritt ausführen
- Inhalte richtig casten, weil die Klassen nicht generisch sind (P4)
- Laufzeitfehler durch isEmpty-Abfragen ausschließen (P1) und eine Struktur mit Hilfsstapel unverändert zurücklassen (P2)

## Hinweise für die Aufnahme

- Alle Beispiele (Heiltränke im Rucksack als Stapel vom Inhaltstyp Ganzzahl, Gäste am Tresen als Schlange vom Inhaltstyp Zeichenkette, die Methoden bediene und gesamtHeilung, beide Mischaufgaben) sind eigens für das Video gewählt und kommen in Lab, Arbeitsblättern, Bossen und Warm-up nicht vor.
- Code kompiliert und ausgeführt mit javac/java gegen den Nachbau der Bibliothek „Niedersachsen“ (werkzeuge/ide-pruefung/java, Paket aq.ni); geprüft auch, dass `int x = s.pop();` ohne Cast nicht übersetzt (incompatible types: Object cannot be converted to int).
- Geprüfte Werte: rucksack nach push(20), push(50), push(10) = 10 50 20 (oben zuerst), pop() liefert 10, danach top() = 50; tresen Ork, Elfe, Zwerg: dequeue() liefert "Ork", danach head() = "Elfe".
- Mischaufgabe 1 (q = 5 1 8, s leer): 1: q 1 8 | s 5 · 2: q 8 | s 1 5 · 3: q 8 1 | s 5 · 4: q 8 1 5 | s 5 · 5: q 1 5 | s leer, x = 3.
- Mischaufgabe 2 (Pause; s = 2 9 4 oben zuerst, q leer): 1: q 2 | s 9 4 · 2: q 2 9 | s 4 · 3: q 9 | s 2 4 · 4: q 9 2 | s 2 4 · 5: q 9 2 | s 4, y = 11.
- bediene(Ork, Elfe; 3) = 2, Schlange danach leer; bediene(Ork, Elfe, Zwerg; 2) = 2, übrig Zwerg; bediene(leer, 2) = 0; dequeue auf leerer Schlange → IllegalStateException.
- gesamtHeilung(10 50 20) = 80, Stapel danach wieder 10 50 20 (dieselben Objekte); Zwischenstände der Tabelle per instrumentiertem Programm geprüft; Fassung ohne Zurückschichten liefert ebenfalls 80, der Stapel ist danach aber leer. Schlange 1 2 3 über einen Hilfsstapel zurückgeschichtet: 3 2 1.
- Pause-Folie: im Schnitt einen Hinweis „Video anhalten“ einblenden; die Auflösung kommt erst auf der nächsten Folie.

## YouTube

**Titel:** Stapel und Schlange (Stack und Queue) fürs Informatik-Abitur Niedersachsen | Algo Quest #6

**Beschreibung:**

```
Stapel und Schlange sind die Klassiker unter den abstrakten Datentypen im Informatik-Abitur in Niedersachsen. In diesem Video lernst du die Schnittstellen nach den Ergänzenden Hinweisen (§4) bzw. der Bibliothek „Niedersachsen“ der Online-IDE kennen: push, pop, top, enqueue, dequeue, head und isEmpty. Du siehst, warum du casten musst (die Klassen sind nicht generisch), wie du Laufzeitfehler mit isEmpty vermeidest und wie du eine Struktur mit einem Hilfsstapel unverändert zurücklässt. Dazu eine Mischaufgabe zum Mitmachen.

Teil der Unterrichtsreihe „Algo Quest – Das Dungeon der Datenstrukturen“ (Informatik eA).
Üben mit sofortiger Rückmeldung: https://algoquest.frankjuchim.de/themen

Kapitel:
0:00 Einstieg
1:00 Abstrakter Datentyp
1:43 LIFO und FIFO
2:26 Schnittstellen
3:12 Casten
4:04 Mischaufgabe
5:00 Selbst ausprobieren
6:16 Laufzeitfehler vermeiden
6:59 Unverändert lassen
8:32 Typische Fehler
9:08 Zusammenfassung
```

_Zeitmarken sind aus der Textlänge geschätzt – nach dem Schnitt anpassen._

**Tags:** Informatik Abitur, Niedersachsen, Stapel, Schlange, Stack, Queue, abstrakter Datentyp, Java, Informatik LK, Algo Quest

## Drehbuch

### Folie 1 · 0:00 – Stapel und Schlange

*Regie: Kamera unten rechts, Titelfolie im Hintergrund.*

Willkommen im Hafen der Algo Quest! Heute geht es um zwei Datenstrukturen, die im Abitur fast immer vorkommen: den Stapel und die Schlange. Sie sehen harmlos aus – aber genau hier gehen viele Punkte verloren: durch fehlende Casts, durch Laufzeitfehler bei leeren Strukturen und durch Methoden, die eine Struktur heimlich zerstören. Nach diesem Video weißt du, wie du das alles vermeidest.

### Folie 2 · 0:28 – Stapel und Schlange im Abitur

Im Abitur begegnen dir Stapel und Schlange vor allem in zwei Aufgabentypen. Erstens: Geben Sie den Inhalt der Strukturen nach Ausführung der Anweisungen an. Zweitens: Implementieren Sie eine Methode – und oft steht dabei: Nach dem Aufruf muss der Stapel unverändert sein. Welche Methoden du verwenden darfst, legen die Ergänzenden Hinweise im Paragrafen vier fest. Und es gilt: Laufzeitfehler müssen ausgeschlossen werden. Rechts siehst du unseren Plan für heute.

### Folie 3 · 1:00 – Abstrakter Datentyp: Man sieht nur die Schnittstelle

Stapel und Schlange sind abstrakte Datentypen. Das bedeutet: Sie werden nur durch ihre Operationen beschrieben – also dadurch, was man mit ihnen machen kann. Wie sie innen gebaut sind, mit einer Reihung oder mit verketteten Knoten, bleibt verborgen und ist für dich egal. Du kommst an die Daten nur über die Schnittstelle heran. Das ist wie bei einem Getränkeautomaten: Du kennst die Knöpfe, aber nicht das Innenleben. Für dich heißt das vor allem: Es gibt keinen Index und keinen Zugriff in die Mitte. Was du nicht über die Schnittstelle erreichst, erreichst du gar nicht.

### Folie 4 · 1:43 – LIFO und FIFO

*Regie: Erst auf den Stapel zeigen (oben = zuletzt hineingelegt), dann auf die Schlange (vorn = zuerst angestellt).*

Unser Held hat Heiltränke im Rucksack, gestapelt. Jede Zahl ist die Heilkraft eines Tranks. Er hat erst den Zwanziger hineingelegt, dann den Fünfziger, dann den Zehner. Oben liegt also der Zehner – und den bekommt er auch als Erstes wieder heraus. Das ist das Prinzip des Stapels: LIFO, last in, first out. Rechts die Schlange am Tresen der Hafentaverne: Zuerst hat sich der Ork angestellt, dann die Elfe, dann der Zwerg. Bedient wird vorne, also zuerst der Ork. Wer sich neu anstellt, kommt nach hinten. Das ist FIFO, first in, first out.

### Folie 5 · 2:26 – Die Schnittstellen nach EH §4

Hier die Schnittstellen nach EH Paragraf vier, so wie sie auch die Bibliothek Niedersachsen der Online-IDE anbietet. Erzeugt wird mit new Stack beziehungsweise new Queue. Mit isEmpty fragst du, ob die Struktur leer ist. Hineinlegen heißt beim Stapel push – oben drauf –, bei der Schlange enqueue – hinten anstellen. Ansehen, ohne zu entnehmen: top beim Stapel, head bei der Schlange. Und herausnehmen: pop und dequeue. Die roten Zeilen sind gefährlich: Auf einer leeren Struktur führen sie zu einem Laufzeitfehler. Merk dir außerdem den Unterschied: top und head schauen nur nach, die Struktur bleibt gleich. pop und dequeue entnehmen das Element.

### Folie 6 · 3:12 – Nicht generisch: Inhalte sind Object (P4)

Jetzt kommt eine Besonderheit, die im Abitur ständig geprüft wird. Die Klassen Stack und Queue sind nicht generisch. Es gibt also keine spitzen Klammern wie Stack von Integer. Alles, was du hineinlegst, wird als Object gespeichert – und genauso kommt es auch wieder heraus. Deshalb musst du beim Herausnehmen casten, also sagen, welcher Typ es wirklich ist. Bei Ganzzahlen schreibst du Klammer Integer, bei Zeichenketten Klammer String. Ohne Cast übersetzt Java das Programm gar nicht – das ist Falle P4. Und wenn du Zeichenketten vergleichst, dann immer mit equals, nicht mit dem doppelten Gleichheitszeichen – das ist Falle P5. Im Kommentar notierst du den Inhaltstyp, so wie es auch in Abituraufgaben steht.

### Folie 7 · 4:04 – Mischaufgabe: Stapel und Schlange zusammen

*Regie: Zeile für Zeile zeigen; bei Zeile 4 betonen, dass top() nicht entnimmt.*

Jetzt eine typische Mischaufgabe. In der Schlange q stehen fünf, eins, acht – fünf vorne. Der Stapel s ist leer. Rechts notieren wir nach jeder Zeile beide Zustände: den Stapel von oben gelesen, die Schlange von vorne. Zeile eins: dequeue nimmt die Fünf vorne heraus, push legt sie auf den Stapel. Zeile zwei: Die Eins wandert genauso auf den Stapel, jetzt oben. Zeile drei: pop nimmt die Eins vom Stapel, enqueue stellt sie hinten an die Schlange: acht, eins. Zeile vier: top schaut die Fünf nur an – sie bleibt im Stapel – und eine Fünf wird hinten angestellt. Zeile fünf: dequeue liefert die Acht, pop die Fünf. x ist acht minus fünf, also drei. Am Ende: Schlange eins, fünf, Stapel leer.

### Folie 8 · 5:00 – Kurz pausieren: Jetzt du!

Jetzt bist du dran. Diesmal liegen auf dem Stapel zwei, neun, vier – die Zwei oben –, und die Schlange ist leer. Halte das Video an und notiere nach jeder Zeile beide Zustände. Welchen Wert hat y am Ende? Danach geht es weiter mit der Auflösung.

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 9 · 5:27 – Auflösung

Die Auflösung. Zeile eins: Die Zwei geht vom Stapel in die Schlange. Zeile zwei: die Neun hinterher, die Schlange ist jetzt zwei, neun. Zeile drei: Die Zwei vorne aus der Schlange kommt wieder oben auf den Stapel: zwei, vier. Zeile vier: top schaut die Zwei nur an, sie bleibt liegen, und eine Zwei wird hinten angestellt: neun, zwei. Zeile fünf: pop nimmt die Zwei vom Stapel, head schaut die Neun nur an. y ist zwei plus neun, also elf. Am Ende bleibt die Schlange neun, zwei, und im Stapel liegt nur noch die Vier. Hast du bei Zeile vier und fünf aufgepasst? Genau da liegen die Fallen.

### Folie 10 · 6:16 – Laufzeitfehler vermeiden: erst fragen, dann nehmen (P1)

Kommen wir zu Falle P1: Laufzeitfehler. Rufst du pop, top, dequeue oder head auf einer leeren Struktur auf, bricht das Programm ab – in der Online-IDE mit einer IllegalStateException. Im Abitur musst du solche Fehler durch eine Abfrage ausschließen. Ein Beispiel: Der Wirt bedient höchstens n Gäste. Stehen aber nur zwei Gäste am Tresen und n ist drei, dann würde der dritte dequeue-Aufruf abstürzen. Deshalb steht in der markierten Zeile zusätzlich: und nicht q punkt isEmpty. Dann endet die Schleife rechtzeitig, und die Methode liefert zwei. Die Regel lautet: Erst fragen, dann nehmen.

### Folie 11 · 6:59 – Muster: Struktur unverändert lassen (P2)

Jetzt zum wichtigsten Muster, Falle P2. Der Held will wissen, wie viel Heilkraft alle Tränke zusammen haben. An die unteren Tränke kommt er nur, wenn er die oberen herausnimmt. Danach soll der Rucksack aber wieder genauso aussehen wie vorher. Die Lösung ist ein Hilfsstapel. In der ersten Schleife nimmst du jeden Trank heraus, addierst seine Heilkraft und legst ihn auf den Hilfsstapel. In der zweiten Schleife schichtest du alles zurück. Weil die Reihenfolge dabei zweimal umgedreht wird, ist am Ende alles wie vorher. Fehlt die zweite Schleife, liefert die Methode zwar die richtige Summe – aber der Rucksack ist leer. Genau das kostet im Abitur Punkte.

### Folie 12 · 7:48 – gesamtHeilung: Schritt für Schritt

So sieht das Schritt für Schritt aus. Am Anfang liegen zehn, fünfzig, zwanzig im Rucksack, der Hilfsstapel ist leer. Beim Abbauen wandert der Zehner auf den Hilfsstapel, die Summe ist zehn. Dann der Fünfziger: sechzig. Dann der Zwanziger: achtzig. Jetzt ist der Rucksack leer und auf dem Hilfsstapel liegt alles in umgekehrter Reihenfolge – der Zwanziger oben. Beim Zurückschichten kommt zuerst der Zwanziger zurück, dann der Fünfziger, dann der Zehner. Und siehe da: zehn, fünfzig, zwanzig – genau wie vorher. Bei einer Schlange geht es übrigens mit einer Hilfsschlange. Ein Hilfsstapel würde die Schlange umdrehen.

### Folie 13 · 8:32 – Typische Fehler – und wie du sie vermeidest

Zum Schluss die typischen Fehler mit ihren Fallen-Nummern. P1: entnehmen, ohne vorher mit isEmpty zu fragen. P2: die Struktur abbauen und nicht zurückschichten. P4: den Cast vergessen – int x gleich s punkt pop übersetzt nicht. P5: Zeichenketten mit dem doppelten Gleichheitszeichen vergleichen statt mit equals. Und bei Mischaufgaben besonders häufig: top und head verwechselt mit pop und dequeue. Rechts der Abi-Check – und denk daran: Verwende nur die Methoden aus der Schnittstelle, also nichts wie size oder get.

### Folie 14 · 9:08 – Das nimmst du mit

Fassen wir zusammen. Stapel und Schlange sind abstrakte Datentypen – du arbeitest nur mit ihren Schnittstellen. Der Stapel arbeitet nach LIFO, die Schlange nach FIFO. Weil die Klassen nicht generisch sind, castest du beim Herausnehmen. Bevor du etwas entnimmst, fragst du mit isEmpty. Und wenn eine Struktur unverändert bleiben soll, schichtest du über einen Hilfsstapel beziehungsweise eine Hilfsschlange zurück.

### Folie 15 · 9:35 – 

Und jetzt ab ins Lab! In Level vier Punkt eins übst du Befehlsfolgen und Mischaufgaben mit Stapel und Schlange, in Level vier Punkt drei, der Inventur, das Muster unverändert lassen. Auf den Arbeitsblättern findest du alles zum Nachlesen. Und wenn du in der Online-IDE programmierst: Schalte die Bibliothek Niedersachsen ein – wie das geht, zeigt Video zwei. Im nächsten Video geht es in den Wald: zu Binärbäumen und Suchbäumen. Bis dahin – gute Fahrt im Hafen!
