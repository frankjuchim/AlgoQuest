**Lehrerexemplar · Boss-Kampf 0 · Welt 0 · DS 7**

**Erwartungshorizont: Die Bibliothek der Akademie**

Erwartungshorizont / Bewertungsbogen für \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Gilde: \_\_\_\_\_\_\_\_\_\_\_\_

I, II, III: erreichbare Bewertungseinheiten im jeweiligen Anforderungsbereich · BE: vom Prüfling erreichte Bewertungseinheiten

<table>
<colgroup>
<col style="width: 58%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Erwartete Prüfungsleistungen</strong></th>
<th><strong>I</strong></th>
<th><strong>II</strong></th>
<th><strong>III</strong></th>
<th><strong>BE</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>a) Übersetzen von Signaturen; Parameter und Argumente; Typprüfung</strong></p>
<p>Kernpunkte: public static double durchschnitt(int[] ausleihen); public static String[] neueAuflage(String[] titel, int[] ausleihen, int grenze); markiere(titel: Reihung von Zeichenkette, index: Ganzzahl, zeichen: Zeichen): nichts; Parameter ausleihen, start, ende (Variablen im Methodenkopf) – Argumente werte, 2, 6 (Werte beim Aufruf, die den Parametern der Reihe nach zugewiesen werden); Kommazahl passt ohne Cast nicht in eine Ganzzahl-Variable (Verlust der Nachkommastellen), eine Ganzzahl wird dagegen automatisch in eine Kommazahl umgewandelt.</p></td>
<td>2</td>
<td>2</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p><strong>b) Dokumentation des Aufrufs mit Hilfsmethode; Analyse; Laufzeitfehler</strong></p>
<p>Kernpunkte: Fünf Einträge (i = 2 bis 6): sterne(7) → s = 2, Rückgabe 2, summe 2; sterne(25) → s = 6, Rückgabe 5, summe 7; sterne(3) → 1, 1, 8; sterne(0) → s nicht belegt, Rückgabe 0, summe 8; sterne(18) → 4, 4, 12; Rückgabewert 12. sterne liefert 5 genau für n ≥ 20; bei sterneSumme(ausleihen, 5, 8) Laufzeitfehler beim Zugriff auf ausleihen[8].</p></td>
<td>1</td>
<td>3</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p><strong>c) Wertübergabe und Referenz</strong></p>
<p>Kernpunkte: Ausgaben 11 4 · 12 · 0; anzahl ist eine Kopie von n (Wertübergabe), anzahl = 0 wirkt nicht auf n; ausleihen erhält eine Kopie der Referenz und verweist auf dieselbe Reihung wie a, die Änderung von ausleihen[2] wirkt nach außen (7 + 4 = 11); jahresabschluss lenkt nur die lokale Referenz auf eine neue Reihung um – a bleibt unverändert; b = a kopiert die Referenz, b[0] = 0 ändert auch a[0]; jahresabschluss erfüllt die Anforderung nicht, Korrektur durch Überschreiben jedes Elements.</p></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td></td>
</tr>
<tr class="even">
<td><p><strong>d) Entwicklung eines Struktogramms</strong></p>
<p>Kernpunkte: Kopf mit Signatur; Leer-Abfrage mit „gib −1 zurück“ vor dem ersten Zugriff; maxIndex ← 0; Zählschleife von 1 bis Länge von ausleihen − 1; Vergleich ausleihen[i] &gt; ausleihen[maxIndex] mit echtem &gt; (kleinster Index bei Gleichstand); „gib maxIndex zurück“ nach der Schleife; Notation nach EH §5.</p></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td></td>
</tr>
<tr class="odd">
<td><p><strong>e) Implementierung der Operation neueAuflage</strong></p>
<p>Kernpunkte: Methodenkopf mit Rückgabetyp String[]; Länge vorab bestimmen (anzahlMindestens oder eigene Zählschleife); neue Reihung genau dieser Länge erzeugen; Durchlauf über alle Indizes 0 bis titel.length − 1 mit Vergleich ≥ grenze; eigener Schreibindex k für erg; Rückgabe der Reihung (bei keinem Treffer Länge 0, nicht null); titel und ausleihen werden nur gelesen.</p></td>
<td>1</td>
<td>3</td>
<td>1</td>
<td></td>
</tr>
<tr class="even">
<td><p><strong>f) Fehleranalyse und Korrektur der Operation durchschnitt</strong></p>
<p>Kernpunkte: Fehler 1: fehlender Rückgabepfad bei leerer Reihung (Compilerfehler „missing return statement“); Fehler 2: Schleife beginnt bei i = 1, ausleihen[0] = 12 fehlt in der Summe; Fehler 3: summe / ausleihen.length ist ganzzahlige Division, die Nachkommastellen gehen verloren; mit Abbildung 1: korrekt 74 / 8 = 9,25, mit beiden Fehlern 62 / 8 → 7 → 7.0; Korrektur mit return 0.0, Start bei 0 und Division als Kommazahl.</p></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Summe</strong></td>
<td>7</td>
<td>13</td>
<td>4</td>
<td><strong>/ 24</strong></td>
</tr>
</tbody>
</table>

AFB-Verteilung: I 7 BE (29 %) · II 13 BE (54 %) · III 4 BE (17 %) – Abitur-Richtwert 30 / 53 / 17 %. Zeitbudget: 24 BE · 2,5 min = 60 min.

*Die gewählten Lösungsansätze und -wege müssen nicht mit den dargestellten Lösungen identisch sein. Fachlich richtige Alternativen sind unter Berücksichtigung der verbindlichen Vorgaben (EH 2025) entsprechend zu bewerten.*

**Umrechnung BE → XP**

| **BE** | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** |
|--------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|--------|--------|
| XP     | 0     | 2     | 4     | 6     | 8     | 10    | 12    | 14    | 16    | 18    | 20     | 22     | 24     |

| **BE** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** | **24** |     |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|-----|
| XP     | 26     | 28     | 30     | 32     | 34     | 36     | 38     | 40     | 42     | 44     | 46     | 48     |     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>XP und Badges aus dem Boss-Kampf (fließen nicht in die Note ein)</strong></p>
<ul>
<li><p>Boss-Kampf: <strong>2 XP je erreichter BE</strong> (max. 48 XP), gutgeschrieben dem Prüfling und seiner Gilde.</p></li>
<li><p>Papier-Compiler zu e): Handschrift unverändert abgetippt, alle 8 Tests grün → <strong>30 XP</strong>, beim ersten Versuch <strong>+10 XP</strong> und Badge <strong>Papier-Compiler</strong>.</p></li>
<li><p>Badge <strong>Fehlerjäger</strong>: In e) und f) sind alle Leer- und Index-Abfragen und alle Rückgabepfade korrekt (e: leere Reihung/kein Treffer liefert Länge 0, Schreibindex k; f: return 0.0 für die leere Reihung, Start bei 0, Kommazahl-Division).</p></li>
<li><p>Orientierung (informativ, Abi-Skala): ab 95 % 15 P · 85 % 13 P · 75 % 11 P · 65 % 9 P · 55 % 7 P · 45 % 5 P · 40 % 4 P · 27 % 2 P. Für 24 BE: 23 BE ≈ 15 P, 18 BE ≈ 11 P, 10 BE ≈ 4 P.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Musterlösungen, Kernpunkte und typische Fehler**

**a) Übersetzen von Signaturen; Parameter und Argumente; Typprüfung** 4 BE (I 2 · II 2 · III 0)

**Musterlösung**

\(1\) public static double durchschnitt(int\[\] ausleihen) · public static String\[\] neueAuflage(String\[\] titel, int\[\] ausleihen, int grenze)

\(2\) markiere(titel: Reihung von Zeichenkette, index: Ganzzahl, zeichen: Zeichen): nichts

\(3\) Parameter sind die im Methodenkopf deklarierten Variablen ausleihen, start und ende. Argumente sind die beim Aufruf übergebenen Werte werte, 2 und 6. Beim Aufruf erhält der Parameter ausleihen eine Kopie der Referenz in werte (beide verweisen auf dieselbe Reihung), start den Wert 2 und ende den Wert 6. Zuordnung über die Reihenfolge, nicht über den Namen.

\(4\) durchschnitt liefert eine Kommazahl. Die Zuweisung an eine Ganzzahl-Variable könnte die Nachkommastellen verlieren (z. B. 9,25 → 9) und wird deshalb ohne ausdrücklichen Cast abgelehnt. sterneSumme liefert eine Ganzzahl; sie lässt sich ohne Verlust als Kommazahl darstellen und wird automatisch umgewandelt (s = 10.0). Geprüft mit javac: „possible lossy conversion from double to int“.

**Kernpunkte und BE-Verteilung**

| **Kernpunkt**                                     | **AFB** | **BE** | **erreicht** |
|---------------------------------------------------|---------|--------|--------------|
| Methodenköpfe von durchschnitt und neueAuflage    | I       | 1      | ☐            |
| Signatur von markiere (Zeichen, nichts)           | I       | 1      | ☐            |
| Parameter und Argumente benannt und unterschieden | II      | 1      | ☐            |
| Begründung über Rückgabetyp und Typumwandlung     | II      | 1      | ☐            |

**Alternativen / Teilpunkte:** Ohne static ist ein Methodenkopf gleichwertig, sofern Rückgabetyp, Name und Parameterliste stimmen; Parameternamen dürfen abweichen, Reihenfolge und Typen nicht. „Formale/aktuelle Parameter“ statt Parameter/Argument ist gleichwertig. Für (4) reicht der Hinweis „double passt nicht ohne Verlust in int, int passt in double“; ein Cast als Lösungsvorschlag ist nicht gefordert.

**Typische Fehler**

- Rückgabetyp int bzw. String statt int\[\] bzw. String\[\] („Reihung von …“ übersehen).

- „nichts“ als Typname in Java statt void bzw. void in der Signatur.

- Parameter und Argumente vertauscht oder nur „die Werte in der Klammer“ genannt.

- „sterneSumme liefert eine Ganzzahl, also wird auch die Zuweisung an double abgelehnt“.

**b) Dokumentation des Aufrufs mit Hilfsmethode; Analyse; Laufzeitfehler** 4 BE (I 1 · II 3 · III 0)

**Musterlösung**

Tracetabelle (geprüft durch Ausführen einer instrumentierten Java-Fassung von Abbildung 3):

| **i**            | **Aufruf von sterne** | **s (in sterne)** | **Rückgabe von sterne** | **summe** |
|------------------|-----------------------|-------------------|-------------------------|-----------|
| vor der Schleife | –                     | –                 | –                       | 0         |
| 2                | sterne(7)             | 2                 | 2                       | 2         |
| 3                | sterne(25)            | 6                 | 5                       | 7         |
| 4                | sterne(3)             | 1                 | 1                       | 8         |
| 5                | sterne(0)             | –                 | 0                       | 8         |
| 6                | sterne(18)            | 4                 | 4                       | 12        |

Rückgabewert von sterneSumme(ausleihen, 2, 6): **12**.

sterne liefert 5 **genau für n ≥ 20**: Für n \> 0 ist s = n / 5 + 1 (Division ohne Rest). s ≥ 5 gilt genau dann, wenn n / 5 ≥ 4, also n ≥ 20. Für n = 20 bis 24 ist s = 5 und wird mit „gib s zurück“ geliefert; ab n = 25 ist s \> 5 und es wird auf 5 begrenzt. Für n ≤ 19 ist s ≤ 4 (z. B. sterne(19) = 4).

sterneSumme(ausleihen, 5, 8): Die Zählschleife läuft einschließlich ende. Für i = 5, 6, 7 wird summe auf 0, 4 und 6 erhöht. Bei i = 8 wird auf ausleihen\[8\] zugegriffen; die Reihung hat aber nur die Indizes 0 bis 7. Es kommt zu einem Laufzeitfehler (in Java ArrayIndexOutOfBoundsException), die Operation liefert keinen Wert.

**Kernpunkte und BE-Verteilung**

| **Kernpunkt**                                                           | **AFB** | **BE** | **erreicht** |
|-------------------------------------------------------------------------|---------|--------|--------------|
| Einträge für i = 2 und i = 3 (inkl. Begrenzung: s = 6, Rückgabe 5)      | I       | 1      | ☐            |
| Einträge i = 4 bis 6 (s bei n = 0 nicht belegt) und Rückgabewert 12     | II      | 1      | ☐            |
| sterne liefert 5 genau für n ≥ 20, begründet mit der Division ohne Rest | II      | 1      | ☐            |
| Laufzeitfehler bei i = 8 (Index außerhalb 0 bis 7) erläutert            | II      | 1      | ☐            |

**Alternativen / Teilpunkte:** Folgefehler werden nicht erneut abgezogen. Eine Begründung über Beispiele (19 → 4, 20 → 5, 24 → 5, 25 → 6 → 5) ist gleichwertig, wenn klar wird, dass s mit n nicht kleiner wird. Der Name der Ausnahme ist nicht gefordert.

**Typische Fehler**

- n / 5 als Kommazahl gerechnet (sterne(7) = 2,4).

- Begrenzung übersehen: sterne(25) liefert 6.

- Für sterne(0) wird s = 1 eingetragen, obwohl die Operation bereits mit „gib 0 zurück“ endet.

- „bis ende“ als „bis ende − 1“ gelesen (nur vier Einträge, Rückgabe 8).

- „Bei i = 8 wird 0 addiert“ statt Laufzeitfehler.

**c) Wertübergabe und Referenz** 3 BE (I 1 · II 1 · III 1)

**Musterlösung**

Ausgaben (geprüft durch Ausführen): **11 4** · **12** · **0**.

1\. Ausgabe: Der Parameter ausleihen erhält eine Kopie der Referenz in a – beide verweisen auf dieselbe Reihung. ausleihen\[2\] = 7 + 4 = 11 verändert also die Reihung von a. anzahl ist dagegen eine Kopie des Wertes von n (Wertübergabe); anzahl = 0 ändert nur diese Kopie, n bleibt 4.

2\. Ausgabe: In jahresabschluss wird nur die lokale Variable ausleihen auf eine neue Reihung umgelenkt. a verweist weiterhin auf die alte Reihung, a\[0\] ist 12.

3\. Ausgabe: int\[\] b = a kopiert die Referenz, nicht die Reihung. b\[0\] = 0 ändert die Reihung, auf die auch a verweist – a\[0\] ist 0.

Beurteilung: jahresabschluss setzt die Ausleihzahlen des Aufrufers nicht auf 0 – die neue Reihung ist nach dem Ende der Operation nicht mehr erreichbar. Die Operation ist wirkungslos. Korrekt ist, jedes Element der übergebenen Reihung zu überschreiben:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static void jahresabschluss(int[] ausleihen) {</p>
<p>for (int i = 0; i &lt; ausleihen.length; i++) {</p>
<p>ausleihen[i] = 0;</p>
<p>}</p>
<p>}</p></td>
</tr>
</tbody>
</table>

**Kernpunkte und BE-Verteilung**

| **Kernpunkt**                                                    | **AFB** | **BE** | **erreicht** |
|------------------------------------------------------------------|---------|--------|--------------|
| Drei Ausgaben 11 4 · 12 · 0                                      | I       | 1      | ☐            |
| Begründung mit Wertübergabe (anzahl) und Referenz (ausleihen, b) | II      | 1      | ☐            |
| Beurteilung von jahresabschluss und korrigierte Implementierung  | III     | 1      | ☐            |

**Alternativen / Teilpunkte:** Gleichwertig: Rückgabe einer neuen Reihung (public static int\[\] jahresabschluss(int\[\] ausleihen) { return new int\[ausleihen.length\]; }), dann muss der geänderte Aufruf a = jahresabschluss(a); angegeben werden. Eine for-each-Schleife (for (int x : ausleihen) x = 0;) ist keine Korrektur.

**Typische Fehler**

- „11 0“: Annahme, anzahl = 0 verändere n.

- „0“ als zweite Ausgabe: jahresabschluss wirke wie gewünscht.

- „12“ als dritte Ausgabe: b als Kopie der Reihung statt der Referenz verstanden.

- Korrektur mit for-each-Schleife, die nur die Kopie x verändert.

**d) Entwicklung eines Struktogramms** 4 BE (I 1 · II 2 · III 1)

**Musterlösung**

Musterlösung (in Java übersetzt und geprüft: Abbildung 1 → 3, leere Reihung → −1, \[4, 9, 9, 2\] → 1):

<img src="media/d6f36f06669f9eb42f0bf24838b418ff059ebcbd.png" style="width:4.57292in;height:2.63542in" />

*Abbildung EH.1: Struktogramm der Operation indexMeistgeliehen*

*Zum Vergleich in Java:*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int indexMeistgeliehen(int[] ausleihen) {</p>
<p>if (ausleihen.length == 0) {</p>
<p>return -1;</p>
<p>}</p>
<p>int maxIndex = 0;</p>
<p>for (int i = 1; i &lt; ausleihen.length; i++) {</p>
<p>if (ausleihen[i] &gt; ausleihen[maxIndex]) {</p>
<p>maxIndex = i;</p>
<p>}</p>
<p>}</p>
<p>return maxIndex;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

**Kernpunkte und BE-Verteilung**

| **Kernpunkt**                                                                 | **AFB** | **BE** | **erreicht** |
|-------------------------------------------------------------------------------|---------|--------|--------------|
| Kopf mit Signatur, Startwert maxIndex ← 0 und Rückgabe nach der Schleife      | I       | 1      | ☐            |
| Schleife über alle weiteren Indizes mit Vergleich gegen das bisherige Maximum | II      | 1      | ☐            |
| Echter Vergleich \> (kleinster Index bei Gleichstand); Notation nach EH §5    | II      | 1      | ☐            |
| Leer-Abfrage vor dem ersten Zugriff mit Rückgabe −1                           | III     | 1      | ☐            |

**Alternativen / Teilpunkte:** Gleichwertig: zusätzliche Variable max für den bisher größten Wert; Schleife ab 0; Leer-Abfrage als Verzweigung, deren falsch-Zweig den restlichen Algorithmus enthält; Startwert max ← 0 (zulässig, da Ausleihzahlen nicht negativ sind). Java statt Struktogramm: höchstens 3 BE.

**Typische Fehler**

- ≥ statt \> (liefert bei Gleichstand den letzten Index).

- Leer-Abfrage fehlt oder steht erst nach dem Zugriff auf ausleihen\[0\].

- Rückgabe des Wertes (25) statt des Index (3).

- „gib maxIndex zurück“ innerhalb der Schleife.

- Java-Syntax im Struktogramm (=, ++, length) statt EH-Notation; leerer falsch-Zweig fehlt.

**e) Implementierung der Operation neueAuflage** 5 BE (I 1 · II 3 · III 1)

**Musterlösung**

Musterlösung (Java, mit javac und den Papier-Compiler-Tests geprüft: 8/8 grün):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static String[] neueAuflage(String[] titel, int[] ausleihen, int grenze) {</p>
<p>int anzahl = anzahlMindestens(ausleihen, grenze);</p>
<p>String[] erg = new String[anzahl];</p>
<p>int k = 0;</p>
<p>for (int i = 0; i &lt; titel.length; i++) {</p>
<p>if (ausleihen[i] &gt;= grenze) {</p>
<p>erg[k] = titel[i];</p>
<p>k++;</p>
<p>}</p>
<p>}</p>
<p>return erg;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

**Kernpunkte und BE-Verteilung**

| **Kernpunkt**                                                                                          | **AFB** | **BE** | **erreicht** |
|--------------------------------------------------------------------------------------------------------|---------|--------|--------------|
| Methodenkopf; Rückgabe der neuen Reihung in jedem Pfad                                                 | I       | 1      | ☐            |
| Länge bestimmen (Hilfsmethode oder Zählschleife) und neue Reihung passender Länge erzeugen             | II      | 1      | ☐            |
| Durchlauf über alle Indizes mit Vergleich ≥ grenze                                                     | II      | 1      | ☐            |
| Eigener Schreibindex k für erg (nicht i)                                                               | II      | 1      | ☐            |
| Randfälle: leere Reihungen und kein Treffer liefern Länge 0 ohne Laufzeitfehler; Originale unverändert | III     | 1      | ☐            |

**Alternativen / Teilpunkte:** Gleichwertig (beide ebenfalls 8/8 Tests grün): (1) eigene Zählschleife statt anzahlMindestens; (2) Treffer zunächst in eine Zwischenreihung der Länge titel.length schreiben und danach in eine Reihung der Länge k kopieren. Struktogramm statt Java: höchstens 3 BE (vgl. Abbildung EH.2). Kleinere Syntaxfehler führen nicht zu Abzug, wenn die Logik eindeutig ist – beim Papier-Compiler zählen sie aber!

*Alternative (1): eigene Zählschleife*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static String[] neueAuflage(String[] titel, int[] ausleihen, int grenze) {</p>
<p>int anzahl = 0;</p>
<p>for (int x : ausleihen) {</p>
<p>if (x &gt;= grenze) {</p>
<p>anzahl++;</p>
<p>}</p>
<p>}</p>
<p>String[] erg = new String[anzahl];</p>
<p>int k = 0;</p>
<p>for (int i = 0; i &lt; titel.length; i++) {</p>
<p>if (ausleihen[i] &gt;= grenze) {</p>
<p>erg[k] = titel[i];</p>
<p>k++;</p>
<p>}</p>
<p>}</p>
<p>return erg;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

*Alternative (2): Zwischenreihung, danach kopieren*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static String[] neueAuflage(String[] titel, int[] ausleihen, int grenze) {</p>
<p>String[] zwischen = new String[titel.length];</p>
<p>int k = 0;</p>
<p>for (int i = 0; i &lt; titel.length; i++) {</p>
<p>if (ausleihen[i] &gt;= grenze) {</p>
<p>zwischen[k] = titel[i];</p>
<p>k++;</p>
<p>}</p>
<p>}</p>
<p>String[] erg = new String[k];</p>
<p>for (int j = 0; j &lt; k; j++) {</p>
<p>erg[j] = zwischen[j];</p>
<p>}</p>
<p>return erg;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

<img src="media/358dd26e7938926f4634225cb5056449c3c6c631.png" style="width:6.625in;height:2.35417in" />

*Abbildung EH.2: neueAuflage als Struktogramm (bei Abgabe als Struktogramm höchstens 3 BE)*

**Typische Fehler**

- \> statt ≥ – Bücher mit genau grenze Ausleihen fehlen (Test grenzeZaehltMit rot).

- erg mit Länge titel.length → null-Einträge am Ende.

- erg\[i\] statt erg\[k\] → ArrayIndexOutOfBoundsException.

- k++ vergessen → jeder Treffer überschreibt erg\[0\].

- return null statt leerer Reihung, wenn kein Buch passt.

- Rückgabetyp String statt String\[\] bzw. Ergebnisreihung als int\[\] deklariert.

**f) Fehleranalyse und Korrektur der Operation durchschnitt** 4 BE (I 1 · II 2 · III 1)

**Musterlösung**

Fehler 1 (fehlender Rückgabepfad): Ist die Reihung leer, ist die Bedingung falsch und die Operation endet ohne return. Der Compiler lehnt die Methode deshalb mit „missing return statement“ ab. Korrektur: return 0.0 für die leere Reihung.

Fehler 2 (Off-by-one): Die Schleife beginnt bei i = 1, ausleihen\[0\] wird nie addiert. Mit Abbildung 1 ist summe = 62 statt 74.

Fehler 3 (ganzzahlige Division): summe und ausleihen.length sind Ganzzahlen, summe / ausleihen.length wird ohne Rest gerechnet; erst das Ergebnis wird in eine Kommazahl umgewandelt. Mit Abbildung 1 ergibt sich 62 / 8 = 7 → **7.0** statt **9.25** (allein wirkt Fehler 2 mit 7.75, Fehler 3 mit 9.0). Alle Werte durch Ausführen geprüft.

Korrigierte Implementierung:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static double durchschnitt(int[] ausleihen) {</p>
<p>if (ausleihen.length == 0) {</p>
<p>return 0.0;</p>
<p>}</p>
<p>int summe = 0;</p>
<p>for (int i = 0; i &lt; ausleihen.length; i++) {</p>
<p>summe = summe + ausleihen[i];</p>
<p>}</p>
<p>return (double) summe / ausleihen.length;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

**Kernpunkte und BE-Verteilung**

| **Kernpunkt**                                                                    | **AFB** | **BE** | **erreicht** |
|----------------------------------------------------------------------------------|---------|--------|--------------|
| Identifikation der drei Fehler                                                   | I       | 1      | ☐            |
| Auswirkung des fehlenden Rückgabepfads (Compilerfehler, leere Reihung)           | II      | 1      | ☐            |
| Auswirkungen von Off-by-one und ganzzahliger Division mit Werten aus Abbildung 1 | II      | 1      | ☐            |
| Vollständig korrigierte Implementierung                                          | III     | 1      | ☐            |

**Alternativen / Teilpunkte:** Gleichwertige Korrekturen der Division: summe als double deklarieren; 1.0 \* summe / ausleihen.length. Nicht ausreichend: (double) (summe / ausleihen.length) – der Cast wirkt erst nach der ganzzahligen Division. Die Struktur mit if … else und return in beiden Zweigen ist ebenso richtig.

**Typische Fehler**

- Fehlender Rückgabepfad übersehen, weil „eine leere Reihung ja nicht vorkommt“.

- Korrektur (double) (summe / ausleihen.length).

- Off-by-one als „das letzte Element fehlt“ beschrieben.

- Nur return 0.0 ergänzt – die beiden logischen Fehler bleiben (Ergebnis 7.0).

**Anhang: Papier-Compiler-Workspace zu e)**

Für den Papier-Compiler legst du in der Online-IDE einen Workspace „W0 Boss 0 – Papier-Compiler“ mit der Klasse Bibliothek (Gerüst unten, neueAuflage mit leerem Rumpf und return null;) und der Testklasse BossTest an und verteilst ihn über „An Klasse austeilen“. Die Lernenden tippen ihre Handschrift **unverändert** in den Rumpf ab und starten die Tests im Reiter „Testrunner“. Erst danach dürfen Fehler korrigiert werden (dann ohne Erster-Versuch-Bonus).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Vor Einsatz prüfen</strong></p>
<p>JUnit-Dialekt der Online-IDE (parameterloser Konstruktor der Testklasse, @Test, globale assertEquals/assertTrue mit Meldung als letztem Argument) vor dem ersten Einsatz mit einem Probedurchlauf testen – insbesondere den Aufruf der Klassenoperation über Bibliothek.neueAuflage(…), Reihungs-Literale new String[] {…} und assertEquals mit Zeichenketten. Die Hilfsmethoden titel(), ausleihen() und text(…) der Testklasse sind private und ohne @Test – prüfen, dass der Testrunner sie nicht als Tests aufführt. Die Bibliothek „niedersachsen“ wird nicht benötigt.</p></td>
</tr>
</tbody>
</table>

**Klasse Bibliothek (Gerüst für den Workspace; sterne, sterneSumme und anzahlMindestens sind vorhanden)**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public class Bibliothek {</p>
<p>public static int sterne(int n) {</p>
<p>if (n == 0) {</p>
<p>return 0;</p>
<p>}</p>
<p>int s = n / 5 + 1;</p>
<p>if (s &gt; 5) {</p>
<p>return 5;</p>
<p>}</p>
<p>return s;</p>
<p>}</p>
<p>public static int sterneSumme(int[] ausleihen, int start, int ende) {</p>
<p>int summe = 0;</p>
<p>for (int i = start; i &lt;= ende; i++) {</p>
<p>summe = summe + sterne(ausleihen[i]);</p>
<p>}</p>
<p>return summe;</p>
<p>}</p>
<p>public static int anzahlMindestens(int[] ausleihen, int grenze) {</p>
<p>int anzahl = 0;</p>
<p>for (int i = 0; i &lt; ausleihen.length; i++) {</p>
<p>if (ausleihen[i] &gt;= grenze) {</p>
<p>anzahl++;</p>
<p>}</p>
<p>}</p>
<p>return anzahl;</p>
<p>}</p>
<p>public static String[] neueAuflage(String[] titel, int[] ausleihen, int grenze) {</p>
<p>// HIER die Handschrift aus Aufgabe e) UNVERAENDERT abtippen</p>
<p>return null;</p>
<p>}</p>
<p>}</p></td>
</tr>
</tbody>
</table>

**Testklasse BossTest (8 Tests; mit der Musterlösung und beiden Alternativen alle grün, typische Fehler werden erkannt – geprüft mit javac, siehe Tabelle)**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public class BossTest {</p>
<p>public BossTest() {</p>
<p>}</p>
<p>private String[] titel() {</p>
<p>return new String[] {"Feuerkunde", "Trankbuch", "Runenlehre", "Sternkarten",</p>
<p>"Kräuterfibel", "Drachenrecht", "Zahlenmagie", "Nebelpfade"};</p>
<p>}</p>
<p>private int[] ausleihen() {</p>
<p>return new int[] {12, 0, 7, 25, 3, 0, 18, 9};</p>
<p>}</p>
<p>private String text(String[] r) {</p>
<p>String s = "";</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>s = s + r[i] + " ";</p>
<p>}</p>
<p>return s;</p>
<p>}</p>
<p>@Test</p>
<p>public void beispielGrenze9() {</p>
<p>String[] e = Bibliothek.neueAuflage(titel(), ausleihen(), 9);</p>
<p>assertEquals(4, e.length, "Laenge 4 erwartet");</p>
<p>assertEquals("Feuerkunde Sternkarten Zahlenmagie Nebelpfade ", text(e),</p>
<p>"Titel in der Reihenfolge von titel erwartet");</p>
<p>}</p>
<p>@Test</p>
<p>public void grenzeZaehltMit() {</p>
<p>String[] e = Bibliothek.neueAuflage(titel(), ausleihen(), 25);</p>
<p>assertEquals(1, e.length, "mindestens 25: genau Sternkarten");</p>
<p>assertEquals("Sternkarten", e[0], "Sternkarten (25) zaehlt mit");</p>
<p>}</p>
<p>@Test</p>
<p>public void keinTrefferLiefertLeereReihung() {</p>
<p>String[] e = Bibliothek.neueAuflage(titel(), ausleihen(), 100);</p>
<p>assertTrue(e != null, "nicht null, sondern eine leere Reihung erwartet");</p>
<p>assertEquals(0, e.length, "Laenge 0 erwartet");</p>
<p>}</p>
<p>@Test</p>
<p>public void leereReihungen() {</p>
<p>String[] e = Bibliothek.neueAuflage(new String[0], new int[0], 5);</p>
<p>assertTrue(e != null, "nicht null erwartet");</p>
<p>assertEquals(0, e.length, "Laenge 0 erwartet");</p>
<p>}</p>
<p>@Test</p>
<p>public void grenzeNullAlleTitel() {</p>
<p>String[] e = Bibliothek.neueAuflage(titel(), ausleihen(), 0);</p>
<p>assertEquals(8, e.length, "alle 8 Titel erwartet");</p>
<p>assertEquals("Feuerkunde", e[0], "erster Titel");</p>
<p>assertEquals("Nebelpfade", e[7], "letzter Titel");</p>
<p>}</p>
<p>@Test</p>
<p>public void originaleBleibenUnveraendert() {</p>
<p>String[] t = titel();</p>
<p>int[] a = ausleihen();</p>
<p>Bibliothek.neueAuflage(t, a, 9);</p>
<p>assertEquals(text(titel()), text(t), "titel darf nicht veraendert werden");</p>
<p>assertEquals(25, a[3], "ausleihen darf nicht veraendert werden");</p>
<p>}</p>
<p>@Test</p>
<p>public void ersterUndLetzterTreffer() {</p>
<p>String[] t = {"A", "B", "C"};</p>
<p>int[] a = {5, 1, 5};</p>
<p>String[] e = Bibliothek.neueAuflage(t, a, 5);</p>
<p>assertEquals("A C ", text(e), "A und C erwartet");</p>
<p>}</p>
<p>@Test</p>
<p>public void trefferNurHinten() {</p>
<p>String[] t = {"X", "Y", "Z"};</p>
<p>int[] a = {1, 9, 9};</p>
<p>String[] e = Bibliothek.neueAuflage(t, a, 2);</p>
<p>assertEquals("Y Z ", text(e), "Y und Z erwartet");</p>
<p>}</p>
<p>}</p></td>
</tr>
</tbody>
</table>

**Kontrolle der Testklasse mit typischen Fehlvarianten (Mutanten)**

| **Variante von neueAuflage**                                        | **Tests grün** |
|---------------------------------------------------------------------|----------------|
| Musterlösung (mit Hilfsmethode anzahlMindestens)                    | 8/8            |
| Alternative (1): eigene Zählschleife statt anzahlMindestens         | 8/8            |
| Alternative (2): Zwischenreihung, danach in passende Länge kopieren | 8/8            |
| \> statt \>= (Bücher mit genau grenze Ausleihen fehlen)             | 4/8            |
| neue Reihung mit Länge titel.length (null-Einträge)                 | 3/8            |
| erg\[i\] statt erg\[k\] (Index der Quelle verwendet)                | 3/8            |
| k++ vergessen (alle Treffer landen in erg\[0\])                     | 4/8            |
| null statt leerer Reihung, wenn kein Buch passt                     | 6/8            |
| Schleife beginnt bei i = 1                                          | 5/8            |
| Original verändert (Treffer in titel nach vorne geschrieben)        | 7/8            |
| leerer Rumpf (Gerüst, return null;)                                 | 1/8            |
