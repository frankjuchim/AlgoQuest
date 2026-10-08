<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>WELT 0 · DOPPELSTUNDE 6 · PAPIER-COMPILER 0</strong></p>
<p><strong>W0·5 – Die Methoden-Werkstatt: Von der Aufgabe zur Methode</strong></p>
<p>Heute arbeitest du fast nur mit Stift · Papier-Compiler 0: <strong>+30 XP</strong> (+10 beim ersten Versuch) · Papier-Aufgaben: je <strong>+5 XP</strong> · Datei: AQ_W0_Akademie_Geruest.txt (Klasse Werkstattpruefung)</p></td>
</tr>
</tbody>
</table>

Die Aufnahmeprüfung der Akademie rückt näher. Dort – und im Abitur – liegt vor dir nur ein Aufgabentext: „**Implementieren Sie die Methode …**“. Kein Compiler sagt dir, dass ein return fehlt, kein Test meldet die vergessene leere Reihung. In der **Methoden-Werkstatt** lernst du deshalb ein festes Vorgehen, mit dem du jede Implementierungsaufgabe sicher löst – und du lernst die Fehler kennen, die in Prüfungen am häufigsten BE kosten.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 1: Das Rezept – von der Aufgabe zur Methode</strong></p>
<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 57%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Schritt</strong></th>
<th><strong>Was tust du?</strong></th>
<th><strong>Ergebnis</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1 Lesen und markieren</strong></td>
<td>Was geht hinein? Was kommt heraus? Welche Bedingungen gelten (echt größer oder größer gleich)? Steht dort „neue Reihung“ oder „verändert“? Welche Sonderfälle nennt der Text?</td>
<td>markierter Text</td>
</tr>
<tr class="even">
<td><strong>2 Signatur → Kopf</strong></td>
<td>Signatur in den Java-Methodenkopf übersetzen (AB 4, Infoteil 2).</td>
<td>Kopf</td>
</tr>
<tr class="odd">
<td><strong>3 Randfälle und Beispiele</strong></td>
<td>Eine kleine Tabelle Eingabe → erwartete Ausgabe: Normalfall, leere Reihung, ein Element, Gleichheit an der Grenze, negative Werte.</td>
<td>Testtabelle</td>
</tr>
<tr class="even">
<td><strong>4 Idee und Struktogramm</strong></td>
<td>Welche Bausteine stecken drin (Zählen, Summe, Maximum, Suche, neue Reihung)? Ablauf skizzieren oder als Struktogramm zeichnen.</td>
<td>Plan</td>
</tr>
<tr class="odd">
<td><strong>5 Java auf Papier</strong></td>
<td>Sauber einrücken, Klammern paarweise schließen, Variablen vor Gebrauch deklarieren.</td>
<td>Methode</td>
</tr>
<tr class="even">
<td><strong>6 Abi-Check</strong></td>
<td>Die Checkliste unten Punkt für Punkt durchgehen; die Testtabelle aus Schritt 3 von Hand durchspielen.</td>
<td>geprüfte Methode</td>
</tr>
<tr class="odd">
<td><strong>7 Papier-Compiler</strong></td>
<td>Unverändert abtippen, Tests starten, jeden Fehler ins Fehlerlogbuch.</td>
<td>Gewissheit</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Abi-Check (Schritt 6)</strong></p>
<p>☐ Kopf wie gefordert: Name, Parameter in Reihenfolge und Typ, Rückgabetyp („nichts“ = void).</p>
<p>☐ <strong>Rückgabe in jedem Pfad</strong> – auch wenn eine Schleife ohne Treffer endet.</p>
<p>☐ Vor jedem Zugriff auf r[0], r[r.length - 1] oder s.charAt(0): <strong>Leer-Abfrage</strong>.</p>
<p>☐ Schleifengrenzen: Index von <strong>0 bis length − 1</strong>; bei Nachbarn (i + 1, i - 1) Grenzen anpassen.</p>
<p>☐ Original <strong>unverändert</strong>, wenn gefordert („neue Reihung“ → new).</p>
<p>☐ Kommazahl, wo eine Kommazahl verlangt ist – keine ganzzahlige Division.</p>
<p>☐ Nur erlaubte Zeichenketten-Operationen; Zeichenketten mit equals vergleichen.</p>
<p>☐ Unsichere Stellen kurz kommentieren (// …) – das zeigt deine Absicht.</p></td>
</tr>
</tbody>
</table>

**Das Rezept in Aktion – ein vorgemachtes Beispiel**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Aufgabe (im Stil des Abiturs)</strong></p>
<p>Implementieren Sie die Methode laengsteSerie(r: Reihung von Ganzzahl, x: Ganzzahl): Ganzzahl. Sie liefert die <strong>Länge der längsten Folge direkt aufeinanderfolgender Elemente</strong> von r, die alle den Wert <strong>x</strong> haben. Kommt x <strong>nicht vor</strong> oder ist r <strong>leer</strong>, liefert sie <strong>0</strong>. Die Reihung wird nicht verändert.</p></td>
</tr>
</tbody>
</table>

**Schritt 1 – markieren:** hinein: eine Reihung und eine Zahl x · heraus: eine Ganzzahl (eine Länge) · „direkt aufeinanderfolgend“: Eine Serie bricht bei jedem anderen Wert ab · Sonderfälle: x kommt nicht vor, r leer → 0 · r nur lesen.

**Schritt 2 – Kopf:** public static int laengsteSerie(int\[\] r, int x)

**Schritt 3 – Randfälle und Beispiele** (mit x = 3):

| **r**    | **{3, 3, 1, 3, 3, 3, 2}** | **{ }** | **{1, 2}** | **{3}** | **{1, 3, 3}**      |
|----------|---------------------------|---------|------------|---------|--------------------|
| erwartet | 3                         | 0       | 0          | 1       | 2 (Serie am Ende!) |

**Schritt 4 – Idee:** zwei Zähler. aktuell zählt die laufende Serie und wird bei einem anderen Wert auf 0 gesetzt; beste merkt sich den Rekord (Baustein Maximum). Wichtig: Den Rekord **sofort** prüfen, nicht erst beim Abbruch der Serie – sonst geht eine Serie am Ende verloren.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td><img src="media/d810be431b12c56511fc147f3c3b5ccf14762940.png" title="s5_serie.png" style="width:3.30208in;height:2.07292in" alt="s5_serie.png" /></td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int laengsteSerie(int[] r, int x) {</p>
<p>int beste = 0;</p>
<p>int aktuell = 0;</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>if (r[i] == x) {</p>
<p>aktuell = aktuell + 1;</p>
<p>if (aktuell &gt; beste) {</p>
<p>beste = aktuell;</p>
<p>}</p>
<p>} else {</p>
<p>aktuell = 0;</p>
<p>}</p>
<p>}</p>
<p>return beste;</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

**Schritt 5 – Java:** siehe oben rechts. **Schritt 6 – Abi-Check:** Kopf ✓ · return beste nach der Schleife, also in jedem Pfad ✓ · kein Zugriff auf r\[0\], darum keine Leer-Abfrage nötig – die leere Reihung liefert 0 ✓ · Index 0 bis length − 1 ✓ · r wird nur gelesen ✓. Testtabelle von Hand für {3, 3, 1, 3, 3, 3, 2}:

| **i**   | **0** | **1** | **2** | **3** | **4** | **5** | **6** |
|---------|-------|-------|-------|-------|-------|-------|-------|
| r\[i\]  | 3     | 3     | 1     | 3     | 3     | 3     | 2     |
| aktuell | 1     | 2     | 0     | 1     | 2     | 3     | 0     |
| beste   | 1     | 2     | 2     | 2     | 2     | 3     | 3     |

**Merke:** Die Testtabelle aus Schritt 3 ist kein Schmuck. Wer beste nur im else-Zweig aktualisiert, liefert für {1, 3, 3} den Wert 0 – das fällt nur auf, wenn man den Fall „Serie am Ende“ wirklich durchspielt.

**Infoteil 2: Die Fehlergalerie**

Diese zehn Fehler kosten in Prüfungen die meisten BE. Präge dir ihre **Merkmale** ein – in Aufgabe 1 musst du sie wiedererkennen.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>F1 Fehlender Rückgabepfad</strong></p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FALSCH</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int indexVonNull(int[] r) {</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>if (r[i] == 0) {</p>
<p>return i;</p>
<p>}</p>
<p>}</p>
<p>} // Compiler: missing return statement</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>RICHTIG</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int indexVonNull(int[] r) {</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>if (r[i] == 0) {</p>
<p>return i;</p>
<p>}</p>
<p>}</p>
<p>return -1; // kein Treffer</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p><strong>Woran erkennst du ihn?</strong> Frage dich: Was liefert die Methode, wenn die Schleife ohne Treffer endet oder kein if zutrifft?</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>F2 Off-by-one: eine Runde zu viel oder zu wenig</strong></p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FALSCH</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int summe = 0;</p>
<p>for (int i = 0; i &lt;= r.length; i++) {</p>
<p>summe = summe + r[i]; // Absturz!</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>RICHTIG</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int summe = 0;</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>summe = summe + r[i];</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p><strong>Woran erkennst du ihn?</strong> &lt;= mit length, Start bei 1 statt 0, r[i + 1] ohne angepasste Grenze. Spiele den ersten und den letzten Durchlauf durch.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>F3 = statt == (Zuweisung statt Vergleich)</strong></p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FALSCH</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>if (gefunden = true) { // immer wahr!</p>
<p>return "ja";</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>RICHTIG</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>if (gefunden) { // == true geht auch</p>
<p>return "ja";</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p><strong>Woran erkennst du ihn?</strong> Bei Wahrheitswerten kompiliert = in der Bedingung und ist immer erfüllt; bei Zahlen meldet der Compiler einen Fehler.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>F4 Ganzzahlige Division</strong></p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FALSCH</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int treffer = 3;</p>
<p>int versuche = 4;</p>
<p>double anteil = treffer / versuche * 100;</p>
<p>// anteil ist 0.0</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>RICHTIG</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int treffer = 3;</p>
<p>int versuche = 4;</p>
<p>double anteil = 100.0 * treffer / versuche;</p>
<p>// anteil ist 75.0</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p><strong>Woran erkennst du ihn?</strong> Zwei Ganzzahlen werden mit / geteilt, das Ergebnis soll eine Kommazahl sein. Lösung: Cast <strong>vor</strong> der Division oder eine Kommazahl beteiligen.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>F5 Parameter überschrieben</strong></p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FALSCH</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int summeAb(int[] r, int start) {</p>
<p>int summe = 0;</p>
<p>for (start = 0; start &lt; r.length; start++) {</p>
<p>summe = summe + r[start];</p>
<p>}</p>
<p>return summe; // ignoriert start</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>RICHTIG</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int summeAb(int[] r, int start) {</p>
<p>int summe = 0;</p>
<p>for (int i = start; i &lt; r.length; i++) {</p>
<p>summe = summe + r[i];</p>
<p>}</p>
<p>return summe;</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p><strong>Woran erkennst du ihn?</strong> Einem Parameter wird ein fester Wert zugewiesen, bevor er benutzt wurde. Parameter sind Eingaben – lies sie, statt sie zu überschreiben.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>F6 Rückgabe in der Schleife zu früh</strong></p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FALSCH</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>if (r[i] &gt; 0) {</p>
<p>return true;</p>
<p>} else {</p>
<p>return false; // prüft nur r[0]</p>
<p>}</p>
<p>}</p>
<p>return true;</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>RICHTIG</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>if (r[i] &lt;= 0) {</p>
<p>return false; // Gegenbeispiel gefunden</p>
<p>}</p>
<p>}</p>
<p>return true; // erst nach der Schleife</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p><strong>Woran erkennst du ihn?</strong> Ein return in <strong>beiden</strong> Zweigen innerhalb der Schleife: Die Schleife läuft nur einmal. „Alle …“ ist erst nach der Schleife sicher.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>F7 Reihung verändert statt Kopie</strong></p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FALSCH</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int[] negiert(int[] r) {</p>
<p>int[] erg = r; // nur die Referenz!</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>erg[i] = -r[i];</p>
<p>}</p>
<p>return erg; // r ist jetzt auch negiert</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>RICHTIG</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int[] negiert(int[] r) {</p>
<p>int[] erg = new int[r.length];</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>erg[i] = -r[i];</p>
<p>}</p>
<p>return erg;</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p><strong>Woran erkennst du ihn?</strong> „liefert eine neue Reihung“ ohne new in der Methode.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>F8 == statt equals bei Zeichenketten</strong></p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FALSCH</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>if (woerter[i] == wort) {</p>
<p>anzahl++;</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>RICHTIG</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>if (woerter[i].equals(wort)) {</p>
<p>anzahl++;</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p><strong>Woran erkennst du ihn?</strong> == zwischen zwei Zeichenketten vergleicht Referenzen. Die Online-IDE verzeiht das, echtes Java und das Abitur nicht.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>F9 Leer-Abfrage vergessen</strong></p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FALSCH</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static char erstesZeichen(String s) {</p>
<p>return s.charAt(0); // Absturz bei ""</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>RICHTIG</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static char erstesZeichen(String s) {</p>
<p>if (s.length() == 0) {</p>
<p>return ' ';</p>
<p>}</p>
<p>return s.charAt(0);</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p><strong>Woran erkennst du ihn?</strong> Zugriff auf Index 0 oder auf das letzte Element ohne vorherige Prüfung der Länge.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>F10 Falscher Startwert bei Maximum/Minimum</strong></p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FALSCH</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int max = 0;</p>
<p>for (int x : r) {</p>
<p>if (x &gt; max) {</p>
<p>max = x; // {-4, -2, -9} liefert 0</p>
<p>}</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>RICHTIG</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int max = r[0]; // vorher: Leer-Abfrage!</p>
<p>for (int x : r) {</p>
<p>if (x &gt; max) {</p>
<p>max = x;</p>
<p>}</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
<p><strong>Woran erkennst du ihn?</strong> Der Startwert ist eine feste Zahl statt eines Elements der Reihung. 0 ist falsch, sobald alle Werte negativ (bzw. beim Minimum alle positiv) sind.</p></td>
</tr>
</tbody>
</table>

**Aufgabe 1: Fehler-Bingo** **PAPIER** ★ **+5 XP**

Jeder Schnipsel enthält **einen** Fehler aus der Galerie. Trage die Fehlernummer (F1 bis F10) ein und korrigiere die Stelle. Wer zuerst eine Zeile, Spalte oder Diagonale im Bingo-Feld unten voll hat, ruft „Bingo!“ – gewertet wird aber nur mit richtiger Korrektur.

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 57%" />
<col style="width: 8%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Nr.</strong></th>
<th><strong>Schnipsel (Absicht in Klammern)</strong></th>
<th><strong>F-Nr.</strong></th>
<th><strong>Korrektur</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>S1</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int summe = 0; // (Summe aller Werte)</p>
<p>for (int i = 1; i &lt; r.length; i++) {</p>
<p>summe = summe + r[i];</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>S2</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>if (name == "Aria") { // (Name prüfen)</p>
<p>bonus = 10;</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>S3</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int richtige = 7;</p>
<p>int gesamt = 8;</p>
<p>double prozent = richtige / gesamt * 100;</p></td>
</tr>
</tbody>
</table></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>S4</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>for (int wert : r) { // (kommt x vor?)</p>
<p>if (wert == x) {</p>
<p>return true;</p>
<p>} else {</p>
<p>return false;</p>
<p>}</p>
<p>}</p>
<p>return false;</p></td>
</tr>
</tbody>
</table></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>S5</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int max(int a, int b) {</p>
<p>if (a &gt; b) { return a; }</p>
<p>if (b &gt; a) { return b; }</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>S6</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int kleinstes = 0; // (Minimum von r)</p>
<p>for (int x : r) {</p>
<p>if (x &lt; kleinstes) { kleinstes = x; }</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>S7</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int[] kopie = original; // (original soll bleiben)</p>
<p>kopie[0] = 99;</p></td>
</tr>
</tbody>
</table></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>S8</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>if (fertig = false) { // (fertig ist boolean)</p>
<p>weiter();</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>S9</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int erstes(int[] r) {</p>
<p>return r[0]; // (leere Reihung: -1)</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>S10</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static String wiederhole(String text, int anzahl) {</p>
<p>anzahl = 3; // (anzahl-mal wiederholen)</p>
<p>String e = "";</p>
<p>for (int i = 0; i &lt; anzahl; i++) { e = e + text; }</p>
<p>return e;</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

**Bingo-Feld:** Trage die Schnipsel-Nummern ein, deren Fehler du gefunden und korrigiert hast.

| **F1** | **F2** | **F3** | **F4** | **F5** |
|--------|--------|--------|--------|--------|
|        |        |        |        |        |

| **F6** | **F7** | **F8** | **F9** | **F10** |
|--------|--------|--------|--------|---------|
|        |        |        |        |         |

**Aufgabe 2: Papier-Compiler 0: Die Werkstattprüfung** **PAPIER → IDE** ★★★ **+30 XP (+10)**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Regeln des Papier-Compilers</strong></p>
<p><strong>1.</strong> Schreibe die Methode <strong>vollständig von Hand</strong> – ohne Gerät, ohne Spickzettel außer den Werkzeugkarten.</p>
<p><strong>2.</strong> Gehe den Abi-Check durch (Infoteil 1).</p>
<p><strong>3.</strong> Tippe deine Lösung <strong>unverändert</strong> ab – Zeichen für Zeichen, auch mit Fehlern!</p>
<p><strong>4.</strong> Starte PapierCompiler0Test. <strong>Alle</strong> Tests grün beim ersten Lauf: <strong>+30 XP +10 XP</strong> und das Badge <strong>Papier-Compiler</strong>. Grün nach Korrektur: <strong>+30 XP</strong>.</p>
<p><strong>5.</strong> Jeder Fehler kommt ins Fehlerlogbuch – erst dann korrigierst du in der IDE.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Aufgabe (wie im Abitur)</strong></p>
<p>Implementieren Sie die Methode anzahlUeberDurchschnitt(r: Reihung von Ganzzahl): Ganzzahl. Sie liefert die Anzahl der Werte in r, die <strong>echt größer</strong> als der Durchschnitt aller Werte von r sind. Der Durchschnitt ist als <strong>Kommazahl</strong> zu berechnen. Für eine <strong>leere Reihung</strong> liefert die Methode 0. Die Reihung wird nicht verändert.</p></td>
</tr>
</tbody>
</table>

**Bewertung: \[5 BE\]**

|        |                                                                                                                |
|--------|----------------------------------------------------------------------------------------------------------------|
| **a)** | **Schritt 1 und 2:** Markiere im Aufgabentext die Bedingungen und Sonderfälle. Schreibe den Java-Methodenkopf. |

|     |
|-----|
|     |

|        |                                                   |
|--------|---------------------------------------------------|
| **b)** | **Schritt 3:** Ergänze die erwarteten Ergebnisse. |

| **r**        | **{12, 7, 15, 9, 3}** | **{5, 5, 5}** | **{ }** | **{-1, -2}** | **{7}** |
|--------------|-----------------------|---------------|---------|--------------|---------|
| Durchschnitt |                       |               | –       |              |         |
| erwartet     |                       |               |         |              |         |

|        |                                                                                                                                    |
|--------|------------------------------------------------------------------------------------------------------------------------------------|
| **c)** | **Schritt 4 und 5:** Implementiere die Methode in Java (bei Bedarf zuerst eine Skizze oder ein Struktogramm auf einem Extrablatt). |

<img src="media/38b1c5bdc176a116cef0457f67a3e02a780eff21.png" title="grid_17_10.png" style="width:6.69792in;height:3.9375in" alt="grid_17_10.png" />

|        |                                                                                                                                  |
|--------|----------------------------------------------------------------------------------------------------------------------------------|
| **d)** | **Schritt 6 – Abi-Check:** Spiele deine Methode mit {−1, −2} von Hand durch. Welchen Wert hat der Durchschnitt in deiner Lösung? |

|     |
|-----|
|     |

|        |                                                                                                                                                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **e)** | **Schritt 7 – Papier-Compiler:** Tippe die Methode **unverändert** in die Klasse Werkstattpruefung ab (mit Kopf). Schalte dann die beiden Blöcke frei – in der Testklasse **und** im Hauptprogramm – und starte PapierCompiler0Test: |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>/* PAPIER-COMPILER-0-START &lt;- diese ganze Zeile löschen</p>
<p>class PapierCompiler0Test {</p>
<p>...</p>
<p>}</p>
<p>PAPIER-COMPILER-0-ENDE */ &lt;- diese ganze Zeile löschen</p></td>
</tr>
</tbody>
</table>

Ergebnis: ☐ alle 6 Tests grün beim ersten Lauf ☐ grün nach Korrektur – Anzahl der Korrekturen: \_\_\_\_

**Fehlerlogbuch**

| **Nr.** | **Was war falsch?** | **Art: Syntax / Logik / Abi-Check** | **So vermeide ich es** |
|---------|---------------------|-------------------------------------|------------------------|
| 1       |                     |                                     |                        |
| 2       |                     |                                     |                        |
| 3       |                     |                                     |                        |

**Aufgabe 3–5: Drei Abi-Aufgaben zur Wahl** **PAPIER** ★★ – ★★★ **je +5 XP**

Wähle **mindestens eine** Aufgabe und bearbeite sie nach dem Rezept – ohne Gerät, mit Zeitlimit (≈ 2,5 min pro BE). Die übrigen sind dein Boss-Training. Notiere oben jeweils Kopf und Randfälle (Schritte 2 und 3).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Aufgabe 3: Die Treppe der Akademie ★★ [4 BE]</strong></p>
<p>Implementieren Sie die Methode istTreppe(r: Reihung von Ganzzahl): Wahrheitswert. Sie liefert wahr, wenn jedes Element von r (ab dem zweiten) <strong>genau um 1 größer</strong> ist als sein Vorgänger, z. B. für {4, 5, 6, 7}. Für Reihungen mit weniger als zwei Elementen liefert sie wahr.</p></td>
</tr>
</tbody>
</table>

Kopf und Randfälle:

|     |
|-----|
|     |
|     |

<img src="media/e4f8ffd0755f42868bd938f3fd23b0a1a8b4b6ae.png" title="grid_17_7.png" style="width:6.69792in;height:2.76042in" alt="grid_17_7.png" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Aufgabe 4: Das Zeichen im Zauberbuch ★★★ [5 BE]</strong></p>
<p>Die Methode anzahlMit(woerter: Reihung von Zeichenkette, c: Zeichen): Ganzzahl liefert die Anzahl der Wörter in woerter, in denen das Zeichen c <strong>mindestens einmal</strong> vorkommt (Groß- und Kleinschreibung werden unterschieden). Implementieren Sie zunächst eine geeignete Hilfsmethode enthaeltZeichen(s: Zeichenkette, c: Zeichen): Wahrheitswert und anschließend die Methode anzahlMit unter Verwendung dieser Hilfsmethode.</p></td>
</tr>
</tbody>
</table>

Kopf und Randfälle:

|     |
|-----|
|     |
|     |

<img src="media/5d5c9121bf8d67eb31ea7e0bd3355c363ba88d86.png" title="grid_17_9.png" style="width:6.69792in;height:3.54167in" alt="grid_17_9.png" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Aufgabe 5: Ohne Rand ★★ [4 BE]</strong></p>
<p>Implementieren Sie die Methode mitte(r: Reihung von Ganzzahl): Reihung von Ganzzahl. Sie liefert eine <strong>neue</strong> Reihung, die alle Elemente von r außer dem ersten und dem letzten in unveränderter Reihenfolge enthält, z. B. {8, 1} für {3, 8, 1, 9}. Hat r weniger als drei Elemente, wird eine leere Reihung (Länge 0) geliefert. r bleibt unverändert.</p></td>
</tr>
</tbody>
</table>

Kopf und Randfälle:

|     |
|-----|
|     |
|     |

<img src="media/e4f8ffd0755f42868bd938f3fd23b0a1a8b4b6ae.png" title="grid_17_7.png" style="width:6.69792in;height:2.76042in" alt="grid_17_7.png" />

**Aufgabe 6: Peer-Korrektur mit dem Kernpunkt-Bogen** **PAPIER** ★★ **Mentor-XP möglich**

Tauscht eure Lösungen zu Aufgabe 3, 4 oder 5 **gildenübergreifend**. Die Lehrkraft zeigt nach der Schreibphase die **Kernpunkte** der Aufgabe – erst dann wird korrigiert. Bewertet wird nur, was auf dem Papier steht, nicht, was gemeint war.

| **Kernpunkt-Bogen zu Aufgabe \_\_\_\_**                          | **erfüllt? (✓ / ✗ / teilweise)** | **Hinweis an die Autorin / den Autor** |
|------------------------------------------------------------------|----------------------------------|----------------------------------------|
| Kopf exakt wie in der Signatur (Name, Parameter, Rückgabetyp)    |                                  |                                        |
| Randfälle laut Aufgabentext korrekt und ohne Laufzeitfehler      |                                  |                                        |
| Schleifengrenzen korrekt (kein Off-by-one)                       |                                  |                                        |
| Rückgabe in jedem Pfad, richtiger Typ                            |                                  |                                        |
| Original unverändert bzw. neue Reihung korrekt (falls gefordert) |                                  |                                        |
| Hilfsmethode verwendet bzw. erlaubte Operationen und equals      |                                  |                                        |
| Kernpunkt 1 (Lehrkraft):                                         |                                  |                                        |
| Kernpunkt 2 (Lehrkraft):                                         |                                  |                                        |
| Kernpunkt 3 (Lehrkraft):                                         |                                  |                                        |

Vorschlag: \_\_\_\_ von \_\_\_\_ BE Korrigiert von (Pseudonym): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Tipp:** Eine Rückmeldung, die **erklärt** statt vorsagt („Spiel mal {1, 3, 3} durch – was liefert deine Methode?“), zählt als Mentor-Einsatz: **+10 XP** (Lehrkraft entscheidet). Fehler, die du bei dir selbst entdeckst, kommen ins Fehlerlogbuch.

**Mein Fehlerlogbuch – Methoden-Werkstatt**

Trage jeden Fehler aus Papier-Compiler, Peer-Korrektur und Bingo ein, den du **selbst** gemacht hast. Ordne ihn einer Nummer der Fehlergalerie zu (oder „neu“). Vor dem Boss-Kampf liest du diese Seite noch einmal.

| **Nr.** | **Aufgabe** | **Fehler (F-Nr. oder neu)** | **Was war falsch?** | **So vermeide ich es** |
|---------|-------------|-----------------------------|---------------------|------------------------|
| 1       |             |                             |                     |                        |
| 2       |             |                             |                     |                        |
| 3       |             |                             |                     |                        |
| 4       |             |                             |                     |                        |
| 5       |             |                             |                     |                        |
| 6       |             |                             |                     |                        |
