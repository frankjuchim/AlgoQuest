<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>LÖSUNGEN · LEHREREXEMPLAR</strong></p>
<p><strong>W0·1 – Das Portal: Lösungen zu den Papier-Aufgaben</strong></p>
<p>Zum Arbeitsblatt AQ_W0_AB_Portal.docx · Aufgaben 2c, 4–8 und Für Schnelle</p></td>
</tr>
</tbody>
</table>

**Aufgabe 2c – Testrunner**

Einige Tests sind sofort grün, weil die vorläufigen return-Werte zufällig passen (z. B. summe der leeren Reihung = 0, zaehle bei nicht enthaltenem Wert = 0). Das zählt noch nicht – Stufe erst geschafft, wenn alle Tests grün sind.

**Aufgabe 4 – Das Rätsel am Portaltor**

**a)** pos = 0 → i = 1: 3 \< 7 → pos = 1 · i = 2: 9 \< 3 nein · i = 3: 3 \< 3 nein · i = 4: 5 \< 3 nein → **Rückgabe 1**.

**b)** Die Methode liefert den Index des (ersten) kleinsten Elements. Name z. B. indexDesMinimums.

**c)** Bei Länge 0 läuft die Schleife „von 1 bis −1“ nicht; zurückgegeben wird 0 – ein Index, den es nicht gibt (Folgefehler beim Zugriff auf r\[0\]). Vorbedingung: r ist nicht leer.

**d)** Mit ≤ wird pos auch bei Gleichheit weitergesetzt: Ergebnis **3** (Index des letzten Minimums).

**Aufgabe 5 – Die Spur der Schatztruhen**

| **Schritt** | **i** | **summe** | **i \< truhe.length** | **summe \< ziel** | **Bedingung**  |
|-------------|-------|-----------|-----------------------|-------------------|----------------|
| 1           | 0     | 0         |                       |                   |                |
| 2           | 1     | 5         | w                     | w                 | w              |
| 3           | 2     | 13        | w                     | w                 | w              |
| 4           | 3     | 15        | w                     | w                 | w              |
| 5           |       |           | w                     | f                 | f → Rückgabe 3 |

Zeilen 2–4: Werte nach dem Schleifendurchlauf; die Bedingung wird jeweils vorher geprüft. **Rückgabe 3.**

**b)** Anzahl der Truhen, die von vorne geöffnet werden, bis mindestens ziel Gold zusammen ist – reicht alles Gold nicht, die Anzahl aller Truhen.

**c)** z. B. schatzSuche({5, 8, 2, 9, 4}, 100) → 5. Auf truhe\[i\] wird nur im Rumpf zugegriffen, und der wird nur betreten, wenn i \< truhe.length gilt. Bei i = 5 ist die Bedingung falsch, die Schleife endet.

**Aufgabe 6 – Vom Code zum Bauplan**

<img src="media/11d1c3821901b39daf6133364e494c53633ad4f2.png" title="w0_l_wertung.png" style="width:4.64583in;height:2.14583in" alt="w0_l_wertung.png" />

**Bewertung (5 BE):** Kopf mit Signatur (1) · Für-jedes-Schleife mit eingerücktem Rumpf (1) · geschachtelte Verzweigung mit wahr/falsch (2) · Zuweisungen mit ← und Rückgabe (1). Alternativ: Zählschleife „für i von 0 bis Länge von wuerfe − 1“ mit wuerfe\[i\].

**b)** {6, 1, 3} → 10 − 5 + 3 = **8** · {2, 6, 6, 1, 5} → 2 + 10 + 10 − 5 + 5 = **22**

**Aufgabe 7 – Bug-Hunt im Bauplan**

**a)** Die Zählschleife läuft „bis Länge von r“ statt „bis Länge von r − 1“. Bei r = {4, 2, 4, 1} wird für i = 4 auf r\[4\] zugegriffen – den Index gibt es nicht. Die Methode bricht mit einem Laufzeitfehler (Index außerhalb der Reihung) ab, bevor −1 zurückgegeben wird. Der Fehler tritt bei jedem Aufruf auf, egal welches x.

**b)** Schleifenkopf: **für i von 0 bis Länge von r − 1**.

**c)** Mögliche Lösung (Vorteil: Die Suche endet beim ersten Treffer von hinten; steht x weit hinten, spart das Vergleiche. „gib … zurück“ beendet die Methode sofort):

<img src="media/29774c00ddb84260ffa10859110237ec7862cd3f.png" title="w0_l_rueck.png" style="width:3.76042in;height:1.89583in" alt="w0_l_rueck.png" />

**Aufgabe 8 – Debugger (Erwartungen)**

Beim Haltepunkt (vor Ausführung der Zeile) zeigt die Variablenansicht: i = 0, summe = 0 → i = 1, summe = 5 → i = 2, summe = 13; danach endet die Schleife, Ausgabe 3. **d)** Mit i \<= truhe.length und ziel = 100 bricht das Programm bei **i = 5** ab (Zugriff auf truhe\[5\], Index außerhalb der Reihung). Den genauen Wortlaut der Fehlermeldung vorher in der Online-IDE prüfen.

**Für Schnelle – Struktogramm zu istPalindrom (eine mögliche Lösung)**

<img src="media/e03641cc328a06e6d6a6422e3a5b7589f8cd96fc.png" title="w0_l_palindrom.png" style="width:4.38542in;height:2.33333in" alt="w0_l_palindrom.png" />

In Java: s.charAt(links) != s.charAt(rechts) – Zeichen (char) dürfen mit ==/!= verglichen werden. Leere Zeichenkette und ein Zeichen: Schleife läuft nicht, Rückgabe wahr.
