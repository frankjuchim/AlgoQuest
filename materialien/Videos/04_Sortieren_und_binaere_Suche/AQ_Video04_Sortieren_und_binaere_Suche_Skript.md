# Erklärvideo 4: Sortieren und binäre Suche

> Drei Sortierverfahren, Vergleiche zählen und halbieren statt durchsuchen

| | |
|---|---|
| **Welt** | Welt 2 · Die Rangliste |
| **Zielgruppe** | Informatik eA (LK), Welt 2; auch zur Wiederholung vor Boss, Klausur und Abitur |
| **Länge** | Ziel 10–12 min · Sprechtext ca. 11:33 min (bei 130 Wörtern/min, inkl. Pausen) |
| **Einsatz** | Welt 2, DS 14–16 · Lab-Level 2.2–2.4 · AB W2·2 „Sortieren“, AB W2·3 „Effizienz und binäre Suche“ |
| **Folien** | `AQ_Video04_Sortieren_und_binaere_Suche_Folien.pptx` (20 Folien, Sprechertext auch in den Notizen) |

## Lernziele

- Selection-, Insertion- und Bubblesort (mit Abbruch) erklären und den Zustand der Reihung nach jedem Durchlauf angeben
- Vergleiche zählen: n(n − 1)/2 im schlechtesten Fall, n − 1 im besten Fall (Insertion, Bubble mit Abbruch); Verdopplung von n → etwa vierfacher Aufwand
- Die binäre Suche mit lo, hi und mid als Tracetabelle dokumentieren (nur Variablen, eine Zeile an jeder mit „// → Tabellenzeile“ markierten Stelle)
- Lineare und binäre Suche vergleichen und die Voraussetzung „sortiert“ beachten

## Hinweise für die Aufnahme

- Alle Zahlenbeispiele sind eigens für das Video gewählt (Sortieren: 64, 27, 85, 12, 49; Pause: 31, 17, 46, 58, 52; Suche: 3, 8, 14, 19, 25, 32, 40, 47, 53, 61, 68, 76, 82) und kommen in Lab, Arbeitsblättern, Folien und Bossen nicht vor.
- Varianten wie in SPEC_AlgoQuest_W2 und der LSG: Selectionsort mit Auswahl (hier Minimum, aufsteigend; tauschen nur bei minIndex ≠ i), Insertionsort mit Tausch benachbarter Elemente, Bubblesort mit Abbruch und verkürztem Bereich (r.length − 1 − durchlauf), binäre Suche iterativ mit mid = (lo + hi) / 2. Gezählt werden Vergleiche zweier Reihungselemente. Im Lab sortiert die Rangliste absteigend – nur der Vergleich dreht sich um (im Video erwähnt).
- Geprüft mit javac/java (genau der Code der Folien, instrumentiert): Selectionsort 64, 27, 85, 12, 49 → i = 0: 12, 27, 85, 64, 49 (V 4) · i = 1: unverändert (V 7) · i = 2: 12, 27, 49, 64, 85 (V 9) · i = 3: unverändert (V 10); 2 Vertauschungen.
- Insertionsort 64, 27, 85, 12, 49 → i = 1: 27, 64, 85, 12, 49 (V 1) · i = 2: unverändert (V 2) · i = 3: 12, 27, 64, 85, 49 (V 5) · i = 4: 12, 27, 49, 64, 85 (V 8); 6 Vertauschungen.
- Bubblesort 64, 27, 85, 12, 49 → Lauf 1: 27, 64, 12, 49, 85 (V 4) · Lauf 2: 27, 12, 49, 64, 85 (V 7) · Lauf 3: 12, 27, 49, 64, 85 (V 9) · Lauf 4 ohne Tausch (V 10) → Abbruch; 6 Vertauschungen.
- Pause 1 (Bubblesort 31, 17, 46, 58, 52): Lauf 1: 17, 31, 46, 52, 58 (V 4, T 2) · Lauf 2 ohne Tausch (V 7) → Ende, 7 Vergleiche.
- Vergleichszahlen per Programm: Selectionsort immer n(n − 1)/2; Insertion- und Bubblesort sortiert n − 1, umgekehrt n(n − 1)/2. n = 5 → 10, n = 30 → 435, n = 60 → 1770 (Faktor ≈ 4,07).
- Binäre Suche in r (n = 13): Suche 47 → (lo, hi, mid) = (0, 12, 6), (7, 12, 9), (7, 8, 7) → Rückgabe 7. Pause 2: Suche 20 → (0, 12, 6), (0, 5, 2), (3, 5, 4), (3, 3, 3), danach lo = 4 > hi = 3 → Rückgabe −1. Höchstens 4 Durchläufe bei n = 13, 5 bei n = 30, 6 bei n = 60, 10 bei n = 1000, 20 bei n = 1 000 000 (alle Suchwerte durchprobiert).
- Folien „Kurz pausieren“: im Schnitt einen Hinweis „Video anhalten“ einblenden; die Lösung kommt erst auf der nächsten Folie.

## YouTube

**Titel:** Sortieren und binäre Suche fürs Informatik-Abitur (Niedersachsen) | Algo Quest #4

**Beschreibung:**

```
Selectionsort, Insertionsort und Bubblesort im direkten Vergleich: Wie arbeiten sie, wie sieht die Reihung nach jedem Durchlauf aus, und wie viele Vergleiche brauchen sie? Dazu: warum doppelt so viele Daten viermal so viel Arbeit bedeuten und wie die binäre Suche mit lo, hi und mid funktioniert – mit Tracetabelle, so wie es das Informatik-Abitur in Niedersachsen verlangt.

Teil der Unterrichtsreihe „Algo Quest – Das Dungeon der Datenstrukturen“ (Informatik eA).
Üben mit sofortiger Rückmeldung: https://algoquest.frankjuchim.de/themen

Kapitel:
0:00 Einstieg
0:59 Selectionsort
2:11 Insertionsort
3:19 Bubblesort
4:31 Vergleiche zählen
5:54 Selbst ausprobieren
6:44 Binäre Suche
9:13 Linear oder binär?
9:48 Typische Fehler
10:23 Zusammenfassung
```

_Zeitmarken sind aus der Textlänge geschätzt – nach dem Schnitt anpassen._

**Tags:** Informatik Abitur, Niedersachsen, Sortieren, Selectionsort, Insertionsort, Bubblesort, binäre Suche, Effizienz, Java, Informatik LK, Algo Quest

## Drehbuch

### Folie 1 · 0:00 – Sortieren und binäre Suche

*Regie: Kamera unten rechts, freundlicher Einstieg, Titelfolie im Hintergrund.*

Hallo und willkommen zur Algo Quest! Heute geht es in die Rangliste: ums Sortieren und ums Suchen. Du lernst drei Sortierverfahren kennen – Selectionsort, Insertionsort und Bubblesort – und wie du ihren Aufwand bestimmst, indem du Vergleiche zählst. Danach zeige ich dir die binäre Suche, die in einer sortierten Reihung unglaublich schnell findet, was sie sucht. Alles genau so, wie es im Abitur verlangt wird.

### Folie 2 · 0:30 – Worum geht es im Abitur?

Im Abitur heißt es zum Beispiel: Geben Sie den Zustand der Reihung nach jedem Durchlauf an. Bestimmen Sie die Anzahl der Vergleiche. Beurteilen Sie, wie sich der Aufwand bei doppelt so vielen Elementen ändert. Oder: Dokumentieren Sie die binäre Suche in einer Tracetabelle. Effizienz wird dabei immer durch Zählen untersucht – du brauchst keine O-Notation. Wir sortieren heute immer dieselbe Reihung aufsteigend.

### Folie 3 · 0:59 – Selectionsort: das Kleinste nach vorn

Beginnen wir mit Selectionsort, dem Sortieren durch Auswahl. Die Idee: Suche im unsortierten Rest das kleinste Element und tausche es an die erste Stelle dieses Rests. Die äußere Schleife läuft mit i von links nach rechts. Die innere Schleife sucht ab i plus eins den Index des Minimums. Getauscht wird nur, wenn das Minimum nicht schon an der Stelle i steht. tausche vertauscht zwei Elemente. Im Lab sortiert die Rangliste übrigens absteigend – dann suchst du das Maximum.

### Folie 4 · 1:35 – Selectionsort: Zustand nach jedem Durchlauf

*Regie: Zeilen nacheinander zeigen; bei i = 1 betonen, dass 27 schon richtig steht.*

So entwickelt sich die Reihung. Im ersten Durchlauf ist zwölf das Minimum, es tauscht mit vierundsechzig. Dafür waren vier Vergleiche nötig. Im zweiten Durchlauf ist siebenundzwanzig schon das Minimum – kein Tausch, aber trotzdem drei Vergleiche. Dann wandert neunundvierzig nach vorn, und im letzten Durchlauf bleibt alles, wie es ist. Insgesamt vier plus drei plus zwei plus eins gleich zehn Vergleiche – und das bei jeder Eingabe, selbst wenn die Reihung schon sortiert ist. Dafür tauscht Selectionsort sehr selten.

### Folie 5 · 2:11 – Insertionsort: einsortieren wie Spielkarten

Insertionsort arbeitet wie beim Sortieren von Spielkarten auf der Hand. Du nimmst das nächste Element und lässt es so lange nach links wandern, wie es kleiner ist als sein linker Nachbar. Im Code startet i bei eins, denn ein einzelnes Element ist schon sortiert. Die while-Schleife tauscht das Element Schritt für Schritt nach links. j größer null steht zuerst, damit wir nie vor den Anfang der Reihung greifen. Auch der letzte Vergleich, der die Schleife beendet, zählt mit.

### Folie 6 · 2:47 – Insertionsort: Zustand nach jedem Durchlauf

Die siebenundzwanzig wandert an der vierundsechzig vorbei nach vorn: ein Vergleich. Die fünfundachtzig bleibt stehen, denn sie ist größer als ihr Nachbar – wieder nur ein Vergleich. Die zwölf dagegen wandert ganz nach vorn: drei Vergleiche, jetzt sind es fünf. Und die neunundvierzig wandert zwei Plätze nach links und stoppt an der siebenundzwanzig: drei Vergleiche, insgesamt acht. Insertionsort hängt also von den Daten ab: sortiert nur vier Vergleiche, umgekehrt zehn.

### Folie 7 · 3:19 – Bubblesort: Nachbarn tauschen – mit Abbruch

Das dritte Verfahren ist Bubblesort. Hier vergleichst du immer zwei Nachbarn von links nach rechts und tauschst, wenn der rechte kleiner ist. So steigt das größte Element wie eine Blase nach hinten auf. Nach jedem Lauf steht also ein Element mehr am Ende fest, deshalb wird der Bereich um durchlauf kürzer. Und unsere Variante hat einen Abbruch: Die Variable getauscht merkt sich, ob in einem Lauf überhaupt getauscht wurde. Wenn nicht, ist die Reihung sortiert, und die Schleife endet.

### Folie 8 · 3:56 – Bubblesort: Zustand nach jedem Lauf

Im ersten Lauf steigt die fünfundachtzig bis ans Ende auf. Dabei werden vier Nachbarpaare verglichen. Im zweiten Lauf landet die vierundsechzig auf ihrem Platz, drei Vergleiche. Im dritten Lauf rutscht die zwölf nach vorn. Jetzt ist sie sortiert – aber das weiß der Algorithmus noch nicht. Erst Lauf vier ohne einen einzigen Tausch löst den Abbruch aus. Insgesamt zehn Vergleiche. Ist die Reihung von Anfang an sortiert, reicht ein einziger Lauf mit n minus eins Vergleichen.

### Folie 9 · 4:31 – Vergleiche zählen

Fassen wir das Zählen zusammen. Selectionsort braucht immer n mal n minus eins halbe Vergleiche, egal wie die Daten aussehen. Insertionsort und Bubblesort mit Abbruch sind im besten Fall viel schneller: Bei einer schon sortierten Reihung brauchen sie nur n minus eins Vergleiche. Im schlechtesten Fall, bei umgekehrt sortierten Daten, sind es auch dort n mal n minus eins halbe. Die Formel kommt daher, dass jeder Durchlauf einen Vergleich weniger braucht: vier plus drei plus zwei plus eins gleich zehn. Wichtig im Abitur: Gib zum schlechtesten Fall immer eine konkrete Eingabe an, zum Beispiel eine absteigend sortierte Reihung.

### Folie 10 · 5:16 – Doppelt so viele Elemente – viermal so viel Arbeit

Und was passiert, wenn die Rangliste doppelt so lang wird? Rechnen wir: Dreißig Elemente brauchen im schlechtesten Fall dreißig mal neunundzwanzig halbe, also vierhundertfünfunddreißig Vergleiche. Sechzig Elemente brauchen sechzig mal neunundfünfzig halbe, also tausendsiebenhundertsiebzig. Das ist ungefähr das Vierfache. Der Grund: Die Formel enthält n mal n, sie wächst quadratisch. Doppelt so viele Elemente bedeuten also etwa viermal so viel Arbeit. Im besten Fall mit n minus eins Vergleichen verdoppelt sich der Aufwand dagegen nur. Rechts steht eine passende Formulierung fürs Abitur.

### Folie 11 · 5:54 – Kurz pausieren: Jetzt du!

Jetzt bist du dran. Halte das Video an und sortiere die Reihung einunddreißig, siebzehn, sechsundvierzig, achtundfünfzig, zweiundfünfzig mit Bubblesort mit Abbruch. Gib den Zustand nach jedem Lauf an und zähle die Vergleiche. Denk daran: Der Bereich wird in jedem Lauf um eins kürzer.

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 12 · 6:19 – Auflösung: Bubblesort mit Abbruch

Hier die Auflösung. Im ersten Lauf werden einunddreißig und siebzehn getauscht, dann achtundfünfzig und zweiundfünfzig. Danach ist die Reihung schon sortiert, nach vier Vergleichen. Der zweite Lauf vergleicht noch drei Paare, findet nichts zum Tauschen – und bricht ab. Insgesamt sieben Vergleiche statt zehn. Hattest du einen dritten Lauf? Dann hast du den Abbruch übersehen.

### Folie 13 · 6:44 – Binäre Suche: halbieren statt durchsuchen

Jetzt zum Suchen. Statt ein Element nach dem anderen zu prüfen, geht es in einer sortierten Reihung viel schneller – mit der binären Suche. lo und hi begrenzen den Bereich, in dem der gesuchte Wert noch liegen kann. In jedem Durchlauf schauen wir in die Mitte, mid, ganzzahlig berechnet. Treffer? Dann geben wir mid zurück. Ist der Wert in der Mitte zu klein, suchen wir rechts weiter, lo wird mid plus eins. Sonst links, hi wird mid minus eins. Wird lo größer als hi, ist der Bereich leer, und wir geben minus eins zurück. Das funktioniert nur auf sortierten Daten.

### Folie 14 · 7:30 – Trace: binaer(r, 47)

*Regie: Mit dem Mauszeiger die besuchten Felder 6, 9 und 7 zeigen; danach die Tabellenzeilen.*

Probieren wir es aus: Wir suchen siebenundvierzig in dieser Reihung mit dreizehn Elementen. Eine Zeile entsteht an der Markierung hinter mid. Erster Durchlauf: lo null, hi zwölf, mid sechs. An der Stelle sechs steht vierzig, das ist kleiner als siebenundvierzig, also lo gleich sieben. Zweiter Durchlauf: lo sieben, hi zwölf, mid neun. Dort steht einundsechzig, zu groß, also hi gleich acht. Dritter Durchlauf: lo sieben, hi acht, mid sieben – und dort steht siebenundvierzig. Treffer, Rückgabe sieben. Beachte: In der Tabelle stehen nur Variablen, keine Spalte für Bedingungen.

### Folie 15 · 8:11 – Kurz pausieren: Jetzt du!

Und noch einmal du. Halte das Video an und führe die Tracetabelle für die Suche nach zwanzig in derselben Reihung. Zwanzig kommt dort nicht vor – überlege genau, wann die Schleife endet und was zurückgegeben wird.

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 16 · 8:33 – Auflösung: binaer(r, 20)

Hier die Auflösung. Erster Durchlauf: mid sechs, vierzig ist zu groß, hi wird fünf. Zweiter Durchlauf: lo null, hi fünf, mid zwei. Vierzehn ist zu klein, lo wird drei. Dritter Durchlauf: lo drei, hi fünf, mid vier. Fünfundzwanzig ist zu groß, hi wird drei. Vierter Durchlauf: lo und hi sind beide drei, mid drei. Neunzehn ist zu klein, lo wird vier. Jetzt ist lo größer als hi, die Schleife endet, und die Methode gibt minus eins zurück. Mehr als vier Durchläufe braucht es bei dreizehn Elementen nie.

### Folie 17 · 9:13 – Linear oder binär?

Lineare und binäre Suche im Vergleich. Die lineare Suche braucht im schlechtesten Fall so viele Durchläufe, wie es Elemente gibt. Die binäre Suche halbiert den Bereich in jedem Durchlauf. Verdoppelst du n, kommt nur ein einziger Durchlauf dazu: bei dreißig Elementen höchstens fünf, bei sechzig höchstens sechs. Bei einer Million Elementen sind es höchstens zwanzig statt einer Million. Aber denk an die Voraussetzung: Die Daten müssen sortiert sein. Wer nur einmal sucht, sortiert dafür nicht extra.

### Folie 18 · 9:48 – Typische Fehler – und wie du sie vermeidest

Zum Schluss die typischen Fehler. P6, Off-by-one: Die Grenzen der Schleifen sind entscheidend – bei Bubblesort r Punkt length minus eins minus durchlauf, bei der binären Suche lo kleiner gleich hi, bei Insertionsort j größer null. P8: Zustand zum falschen Zeitpunkt, Startzeile vergessen oder eine Bedingungsspalte. P4: mid wird ganzzahlig berechnet, null plus fünf durch zwei ist zwei. P10: Beim schlechtesten Fall fehlt die konkrete Eingabe, oder beim Beurteilen fehlt die Begründung. Und: Vertauschungen sind keine Vergleiche.

### Folie 19 · 10:23 – Das nimmst du mit

Fassen wir zusammen. Selectionsort holt das Minimum nach vorn, Insertionsort lässt Elemente nach links wandern, Bubblesort tauscht Nachbarn und bricht ab, wenn ein Lauf ohne Tausch bleibt. Im schlechtesten Fall brauchen alle drei n mal n minus eins halbe Vergleiche, doppelt so viele Elemente bedeuten etwa viermal so viel Arbeit. Die binäre Suche funktioniert nur auf sortierten Daten, halbiert den Bereich in jedem Schritt und braucht bei doppelter Länge nur einen Durchlauf mehr.

### Folie 20 · 10:57 – 

Und jetzt du! Im Algo Quest Lab findest du dazu Level zwei Punkt zwei, Ordnung im Ranking, das Sortier-Duell in Level zwei Punkt drei und die binäre Suche in Level zwei Punkt vier – jeweils mit sofortiger Rückmeldung. Auf den Arbeitsblättern Sortieren sowie Effizienz und binäre Suche kannst du weiter üben. Im nächsten Video geht es ins Labyrinth: Wir lernen die Rekursion kennen – Methoden, die sich selbst aufrufen. Bis dahin – viel Erfolg in der Rangliste!
