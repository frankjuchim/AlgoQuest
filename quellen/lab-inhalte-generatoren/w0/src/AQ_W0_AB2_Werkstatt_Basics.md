<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>WELT 0 · DOPPELSTUNDE 2 · LEVEL 0.2</strong></p>
<p><strong>W0·2 – Die Werkstatt: Datentypen, Operatoren, Verzweigungen, Schleifen</strong></p>
<p>Datei: AQ_W0_Akademie_Geruest.txt (Klasse Werkstatt) · IDE-Level 0.2: bis <strong>+60 XP</strong> · Papier-Aufgaben: je <strong>+5 XP</strong> · Notations-Referenz: AB 1 „Portal“, Teil B</p></td>
</tr>
</tbody>
</table>

Hinter dem Portal liegt die **Akademie der Baumeister**. Bevor euer Studio Helden schmieden darf, muss jede Gilde ihre Ausbildung bestehen – und die beginnt in der **Werkstatt**. Hier wird gerechnet, gewogen und gezählt: Wie viel Gold bleibt nach dem Einkauf übrig? Wie viele Kisten braucht der Trankhändler? Welchen Rang verdient ein Lehrling?

Die Werkzeuge dafür kennst du aus der Einführungsphase: Datentypen, Operatoren, Verzweigungen und Schleifen. Heute schärfst du sie – und zwar so, wie das Abitur sie verlangt: **genau**. Denn in Java ist 7 / 2 nicht 3.5, und -7 % 2 ist nicht 1.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 1: Datentypen und Variablen</strong></p>
<p>Jede Variable hat einen <strong>Datentyp</strong>. Er legt fest, welche Werte sie speichern kann. Die deutschen Typnamen brauchst du für Signaturen im Abitur (Übersicht: AB 1, Teil B, Infoteil 1).</p>
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 29%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Java</strong></th>
<th><strong>Abi-Typname</strong></th>
<th><strong>Beispielwerte</strong></th>
<th><strong>Achtung</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>int</td>
<td>Ganzzahl</td>
<td>0, -17, 2026</td>
<td>/ rechnet mit zwei Ganzzahlen <strong>ganzzahlig</strong></td>
</tr>
<tr class="even">
<td>double</td>
<td>Kommazahl</td>
<td>3.5, -0.25, 7.0</td>
<td>Dezimal<strong>punkt</strong>, kein Komma</td>
</tr>
<tr class="odd">
<td>boolean</td>
<td>Wahrheitswert</td>
<td>true, false</td>
<td>im Struktogramm: wahr / falsch</td>
</tr>
<tr class="even">
<td>char</td>
<td>Zeichen</td>
<td>'a', 'Z', '7', ' '</td>
<td><strong>einfache</strong> Anführungszeichen, genau ein Zeichen</td>
</tr>
<tr class="odd">
<td>String</td>
<td>Zeichenkette</td>
<td>"Drache", ""</td>
<td><strong>doppelte</strong> Anführungszeichen; Vergleich mit equals</td>
</tr>
</tbody>
</table>
<ul>
<li><p><strong>Deklaration und Zuweisung:</strong> int gold; legt die Variable an, gold = 50; weist einen Wert zu, int gold = 50; macht beides. Im Struktogramm schreibst du die Zuweisung mit Pfeil: gold ← 50.</p></li>
<li><p>= <strong>weist zu,</strong> == <strong>vergleicht.</strong> Im Struktogramm steht für den Vergleich ein einfaches =.</p></li>
<li><p><strong>Automatische Umwandlung:</strong> Eine Ganzzahl passt in eine Kommazahl-Variable (double d = 7; speichert 7.0). Umgekehrt braucht man einen <strong>Cast</strong> (int) – und der schneidet die Nachkommastellen ab.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Aufgabe 0: Blitz-Kata: Was rechnet Java?** **PAPIER** ★ **+5 XP**

Notiere zu jedem Ausdruck den Wert. Erst vermuten – dann mit Infoteil 2 prüfen und mit Farbe korrigieren. Kommazahlen schreibst du mit Punkt (z. B. 2.0), Wahrheitswerte als true / false.

| **Ausdruck** | **23 / 4** | **23 % 4** | **4 % 23** | **-9 / 2** | **-9 % 2** | **10 - 3 \* 2 % 4** |
|--------------|------------|------------|------------|------------|------------|---------------------|
| **Wert**     |            |            |            |            |            |                     |

| **Ausdruck** | **(double) 9 / 2** | **(double) (9 / 2)** | **(int) 7.9** | **1 / 2 \* 4.0** | **7 \> 3 && 2 \> 5** | **!(3 == 3) \|\| 4 != 4** |
|--------------|--------------------|----------------------|---------------|------------------|----------------------|---------------------------|
| **Wert**     |                    |                      |               |                  |                      |                           |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 2: Operatoren</strong></p>
<table style="width:100%;">
<colgroup>
<col style="width: 21%" />
<col style="width: 47%" />
<col style="width: 15%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Operator</strong></th>
<th><strong>Bedeutung</strong></th>
<th><strong>Beispiel</strong></th>
<th><strong>Ergebnis</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>+ - *</td>
<td>wie in der Mathematik, Punkt vor Strich</td>
<td>3 + 4 * 2</td>
<td>11</td>
</tr>
<tr class="even">
<td>/ mit zwei Ganzzahlen</td>
<td><strong>ganzzahlige Division</strong> – der Rest fällt weg</td>
<td>17 / 5</td>
<td>3</td>
</tr>
<tr class="odd">
<td>/ mit einer Kommazahl</td>
<td>normale Division</td>
<td>17 / 5.0</td>
<td>3.4</td>
</tr>
<tr class="even">
<td>% (mod)</td>
<td><strong>Rest</strong> der ganzzahligen Division; *, / und % haben gleichen Rang</td>
<td>17 % 5</td>
<td>2</td>
</tr>
<tr class="odd">
<td>% mit negativer Zahl</td>
<td>Der Rest hat das Vorzeichen der <strong>linken</strong> Zahl</td>
<td>-7 % 2</td>
<td>−1 (nicht 1!)</td>
</tr>
<tr class="even">
<td>(int) (double)</td>
<td>Typumwandlung (Cast); (int) schneidet ab, rundet nicht</td>
<td>(int) 3.99</td>
<td>3</td>
</tr>
</tbody>
</table>
<ul>
<li><p><strong>Vergleiche</strong> == != &lt; &lt;= &gt; &gt;= liefern einen Wahrheitswert. Im Struktogramm: = ≠ &lt; ≤ &gt; ≥.</p></li>
<li><p><strong>Logische Operatoren:</strong> &amp;&amp; (und), || (oder), ! (nicht). Java wertet von links aus und hört auf, sobald das Ergebnis feststeht: In i &lt; r.length &amp;&amp; r[i] &gt; 0 wird r[i] nur gelesen, wenn der Index gültig ist.</p></li>
<li><p><strong>Typische Anwendungen von</strong> %<strong>:</strong> n % 2 == 0 (gerade?), n % 10 (letzte Ziffer), n / 10 (letzte Ziffer streichen), a % b == 0 (b teilt a).</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Achtung Abi: Die Casting-Falle</strong></p>
<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 52%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Ausdruck (summe = 50)</strong></th>
<th><strong>Was passiert?</strong></th>
<th><strong>Ergebnis</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>(double) summe / 3</td>
<td>erst umwandeln, dann teilen → Kommazahl-Division</td>
<td>16.666… ✓</td>
</tr>
<tr class="even">
<td>summe / 3.0</td>
<td>eine Kommazahl beteiligt → Kommazahl-Division</td>
<td>16.666… ✓</td>
</tr>
<tr class="odd">
<td>(double) (summe / 3)</td>
<td>erst <strong>ganzzahlig</strong> teilen (16), dann umwandeln</td>
<td>16.0 ✗</td>
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
<td><p><strong>Infoteil 3: Zufall und Runden (EH 2025)</strong></p>
<p>Math.random() liefert eine Kommazahl z mit <strong>0 ≤ z &lt; 1</strong> – die 1 selbst kommt nie vor. Daraus baust du eine <strong>ganzzahlige Zufallszahl im Bereich</strong> Schritt für Schritt, hier für einen Würfel (1 bis 6):</p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Ausdruck</strong></th>
<th><strong>mögliche Werte</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Math.random()</td>
<td>0 ≤ z &lt; 1 (Kommazahl)</td>
</tr>
<tr class="even">
<td>Math.random() * 6</td>
<td>0 ≤ … &lt; 6 (Kommazahl)</td>
</tr>
<tr class="odd">
<td>(int) (Math.random() * 6)</td>
<td>0, 1, 2, 3, 4, 5 (Cast schneidet ab)</td>
</tr>
<tr class="even">
<td>(int) (Math.random() * 6) + 1</td>
<td>1, 2, 3, 4, 5, 6</td>
</tr>
</tbody>
</table>
<p><strong>Allgemein</strong> für eine Zahl von von bis bis (beide möglich, alle gleich wahrscheinlich): (int) (Math.random() * (bis - von + 1)) + von – denn bis - von + 1 ist die <strong>Anzahl</strong> der möglichen Werte.</p>
<p><strong>Ganzzahlig runden</strong> (kaufmännisch, für x ≥ 0): (int) (x + 0.5). Beispiel: 2.4 + 0.5 = 2.9 → 2 und 2.5 + 0.5 = 3.0 → 3. In der Akademie sind Math.round, Math.floor, Math.ceil und Math.pow tabu – du baust Runden und Potenzieren selbst.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Achtung Abi: Klammern beim Cast</strong></p>
<p>(int) Math.random() * 6 + 1 liefert <strong>immer 1</strong>: Der Cast wirkt nur auf Math.random() und macht daraus sofort 0. Die Klammer muss um das ganze Produkt: (int) (Math.random() * 6) + 1.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 4: Verzweigungen und Schleifen – Ergänzungen zu AB 1</strong></p>
<p>Die Grundelemente (Verzweigung, Solange-, Zähl- und Für-jedes-Schleife) stehen auf AB 1, Teil B, Infoteil 2. Neu sind hier die <strong>Verzweigungskette</strong> und die <strong>fußgesteuerte Schleife</strong>.</p>
<p><strong>else-if-Kette:</strong> Die Bedingungen werden <strong>der Reihe nach</strong> geprüft; nur der erste zutreffende Zweig wird ausgeführt. Im Struktogramm wird daraus eine <strong>geschachtelte</strong> Verzweigung im Falsch-Zweig.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static String temperaturText(int t) {</p>
<p>if (t &lt; 0) {</p>
<p>return "Frost";</p>
<p>} else if (t &lt; 20) {</p>
<p>return "mild";</p>
<p>} else {</p>
<p>return "heiß";</p>
<p>}</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td><img src="media/2086aac8e69c35bf33efafb65f9a2fe3847ff760.png" title="s2_kette.png" style="width:2.98958in;height:1.11458in" alt="s2_kette.png" /></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

| **Schleife**  | **Java**                           | **Struktogramm**             | **Wann?**                                                               |
|---------------|------------------------------------|------------------------------|-------------------------------------------------------------------------|
| kopfgesteuert | while (bed) { … }                  | solange bed                  | Anzahl der Durchläufe unbekannt; evtl. 0-mal                            |
| Zählschleife  | for (int i = 0; i \< n; i++) { … } | für i von 0 bis n − 1        | Anzahl bekannt; „bis“ ist **einschließlich**                            |
| fußgesteuert  | do { … } while (bed);              | – (im Abitur kaum verwendet) | Rumpf läuft **mindestens einmal**; lässt sich immer mit while schreiben |

**Aufgabe 1: Der Typ-Detektiv** **PAPIER** ★ **+5 XP**

Ein Lehrling hat zwölf Anweisungen in die Werkstatt-Datei getippt. Nicht alle nimmt der Compiler an.

|        |                                         |              |
|--------|-----------------------------------------|--------------|
| **a)** | Kreuze an, ob die Anweisung kompiliert. | **\[3 BE\]** |

|        |                                                                                            |              |
|--------|--------------------------------------------------------------------------------------------|--------------|
| **b)** | Gib bei kompilierenden Anweisungen den gespeicherten Wert an, sonst eine kurze Begründung. | **\[4 BE\]** |

| **Nr.** | **Anweisung**                | **kompiliert?** | **Wert bzw. Grund** |
|---------|------------------------------|-----------------|---------------------|
| 1       | int a = 7.0;                 | ☐ ja ☐ nein     |                     |
| 2       | double d = 7;                | ☐ ja ☐ nein     |                     |
| 3       | char c = "x";                | ☐ ja ☐ nein     |                     |
| 4       | String s = 'x';              | ☐ ja ☐ nein     |                     |
| 5       | boolean b = 0;               | ☐ ja ☐ nein     |                     |
| 6       | int n = (int) 7.9;           | ☐ ja ☐ nein     |                     |
| 7       | double q = 7 / 2;            | ☐ ja ☐ nein     |                     |
| 8       | int m = 10 / 4.0;            | ☐ ja ☐ nein     |                     |
| 9       | String t = "Gold: " + 5 + 3; | ☐ ja ☐ nein     |                     |
| 10      | String u = 5 + 3 + " Gold";  | ☐ ja ☐ nein     |                     |
| 11      | int k = (int) 'A' + 2;       | ☐ ja ☐ nein     |                     |
| 12      | boolean g = 3 \< 5 \< 7;     | ☐ ja ☐ nein     |                     |

**Tipp:** Bei 9 und 10 arbeitet + von links nach rechts: Sobald eine Zeichenkette beteiligt ist, wird **verkettet** statt addiert. Bei 11 hilft die ASCII-Tabelle: 'A' hat den Wert 65.

**Aufgabe 2: Wechselgeld in der Werkstatt** **PAPIER** ★★ **+5 XP**

In der Akademie gilt: 1 Gold = 100 Kupfer, 1 Silber = 10 Kupfer. Der Händler zahlt einen Betrag in möglichst wenigen Münzen aus.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 int betrag = 487;</p>
<p>2 int gold = betrag / 100;</p>
<p>3 betrag = betrag % 100;</p>
<p>4 int silber = betrag / 10;</p>
<p>5 int kupfer = betrag % 10;</p></td>
</tr>
</tbody>
</table>

|        |                                                                                           |              |
|--------|-------------------------------------------------------------------------------------------|--------------|
| **a)** | Erstelle eine Tracetabelle: eine Zeile pro Anweisung, eingetragen wird nur der neue Wert. | **\[2 BE\]** |

| **Zeile** | **betrag** | **gold** | **silber** | **kupfer** |
|-----------|------------|----------|------------|------------|
| 1         |            |          |            |            |
| 2         |            |          |            |            |
| 3         |            |          |            |            |
| 4         |            |          |            |            |
| 5         |            |          |            |            |

|        |                                                                                                         |              |
|--------|---------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Ein Lehrling vertauscht die Zeilen 3 und 4. Gib an, welcher Wert sich ändert, und nenne den neuen Wert. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

|        |                                                                                                                 |              |
|--------|-----------------------------------------------------------------------------------------------------------------|--------------|
| **c)** | Der Händler berechnet den Durchschnittspreis dreier Tränke und rundet ihn. Gib die Werte der vier Variablen an. | **\[3 BE\]** |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 60%" />
<col style="width: 39%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int summe = 50;</p>
<p>double schnitt = summe / 3;</p>
<p>double schnitt2 = (double) summe / 3;</p>
<p>int gerundet = (int) (schnitt2 + 0.5);</p>
<p>int abgeschnitten = (int) schnitt2;</p></td>
</tr>
</tbody>
</table></td>
<td><table>
<colgroup>
<col style="width: 55%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Variable</strong></th>
<th><strong>Wert</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>schnitt</td>
<td></td>
</tr>
<tr class="even">
<td>schnitt2</td>
<td></td>
</tr>
<tr class="odd">
<td>gerundet</td>
<td></td>
</tr>
<tr class="even">
<td>abgeschnitten</td>
<td></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

|        |                                                                        |              |
|--------|------------------------------------------------------------------------|--------------|
| **d)** | Gib gerundet für summe = 49 an und begründe mit einer kurzen Rechnung. | **\[1 BE\]** |

|     |
|-----|
|     |
|     |

**Aufgabe 3: Die Würfel der Werkstatt** **PAPIER** ★★ **+5 XP**

|        |                                                                         |              |
|--------|-------------------------------------------------------------------------|--------------|
| **a)** | Gib für jeden Ausdruck den kleinsten und den größten möglichen Wert an. | **\[3 BE\]** |

| **Ausdruck**                     | **kleinster Wert** | **größter Wert** |
|----------------------------------|--------------------|------------------|
| (int) (Math.random() \* 6)       |                    |                  |
| (int) (Math.random() \* 6) + 1   |                    |                  |
| (int) Math.random() \* 6 + 1     |                    |                  |
| (int) (Math.random() \* 11) - 5  |                    |                  |
| (int) (Math.random() \* 20) + 10 |                    |                  |

|        |                                                                                                                  |              |
|--------|------------------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Gib einen Ausdruck an, der eine ganzzahlige Zufallszahl von −3 bis 3 liefert (alle Werte gleich wahrscheinlich). | **\[2 BE\]** |

|     |
|-----|
|     |

|        |                                                                                                                                                           |              |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **c)** | Der Würfelmeister würfelt mit zwei Würfeln und addiert. Sein Lehrling meint: „Das ist dasselbe wie eine Zufallszahl von 2 bis 12.“ Beurteile die Aussage. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

**Aufgabe 4: Rangabzeichen – die Reihenfolge zählt** **PAPIER** ★★ **+5 XP**

Die Akademie vergibt Rangabzeichen nach XP: unter 100 Novize, ab 100 Lehrling, ab 250 Geselle, ab 500 Meister. Ein Lehrling hat dafür diese Methode geschrieben:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static String rang(int xp) {</p>
<p>2 String r = "Novize";</p>
<p>3 if (xp &gt;= 100) {</p>
<p>4 r = "Lehrling";</p>
<p>5 } else if (xp &gt;= 250) {</p>
<p>6 r = "Geselle";</p>
<p>7 } else if (xp &gt;= 500) {</p>
<p>8 r = "Meister";</p>
<p>9 }</p>
<p>10 return r;</p>
<p>11 }</p></td>
</tr>
</tbody>
</table>

|        |                           |              |
|--------|---------------------------|--------------|
| **a)** | Gib die Rückgabewerte an. | **\[2 BE\]** |

| **Aufruf**   | **rang(50)** | **rang(120)** | **rang(300)** | **rang(800)** |
|--------------|--------------|---------------|---------------|---------------|
| **Rückgabe** |              |               |               |               |

|        |                                                                     |              |
|--------|---------------------------------------------------------------------|--------------|
| **b)** | Erläutere, warum die Ränge Geselle und Meister nie vergeben werden. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

|        |                                                                                                                  |              |
|--------|------------------------------------------------------------------------------------------------------------------|--------------|
| **c)** | Stelle eine korrigierte Fassung der Methode als Struktogramm nach EH § 5 dar (mit Kopfzeile und „gib … zurück“). | **\[4 BE\]** |

<img src="media/e4f8ffd0755f42868bd938f3fd23b0a1a8b4b6ae.png" title="grid_17_7.png" style="width:6.69792in;height:2.76042in" alt="grid_17_7.png" />

|        |                                                                                                                                                                                            |              |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **d)** | Ein anderer Lehrling behält die Reihenfolge bei, ersetzt aber jedes else if durch ein einzelnes if. Prüfe mit rang(300) und rang(800), ob die Methode dann richtig arbeitet, und begründe. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

**Aufgabe 5: Die Zauberfolge – Schleifen tracen** **PAPIER** ★★ **+5 XP**

Ein alter Zauber verändert eine Zahl so lange, bis sie 1 ist: Gerade Zahlen werden halbiert, ungerade verdreifacht und um 1 erhöht. Die Methode zählt die Schritte.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static int schritte(int n) {</p>
<p>2 int s = 0;</p>
<p>3 while (n != 1) {</p>
<p>4 if (n % 2 == 0) {</p>
<p>5 n = n / 2;</p>
<p>6 } else {</p>
<p>7 n = 3 * n + 1;</p>
<p>8 }</p>
<p>9 s++;</p>
<p>10 }</p>
<p>11 return s;</p>
<p>12 }</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                                                         |              |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Erstelle eine Tracetabelle für den Aufruf schritte(6): erste Zeile vor der Schleife, dann eine Zeile am Ende jedes Durchlaufs. Gib den Rückgabewert an. | **\[3 BE\]** |

| **Durchlauf**    | **n % 2 == 0 (w/f)** | **n** | **s** |
|------------------|----------------------|-------|-------|
| vor der Schleife |                      |       |       |
|                  |                      |       |       |
|                  |                      |       |       |
|                  |                      |       |       |
|                  |                      |       |       |
|                  |                      |       |       |
|                  |                      |       |       |
|                  |                      |       |       |
|                  |                      |       |       |
|                  |                      |       |       |

Rückgabewert: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

|        |                                                                                                                                                                                                                                     |              |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **b)** | In einer zweiten Fassung wird die Schleife fußgesteuert: do { … } while (n != 1); – der Rumpf bleibt gleich. Gib einen Startwert n ≥ 1 an, für den beide Fassungen **verschiedene** Ergebnisse liefern, und nenne beide Ergebnisse. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

|        |                                                |              |
|--------|------------------------------------------------|--------------|
| **c)** | Gib die Ausgabe dieses Programmausschnitts an. | **\[2 BE\]** |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 64%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>for (int z = 1; z &lt;= 3; z++) {</p>
<p>String zeile = "";</p>
<p>for (int s = 1; s &lt;= 5; s++) {</p>
<p>if (s % z == 0) {</p>
<p>zeile = zeile + "#";</p>
<p>} else {</p>
<p>zeile = zeile + ".";</p>
<p>}</p>
<p>}</p>
<p>println(zeile);</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Ausgabe</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

**Aufgabe 6: Bauplan und Code** **PAPIER** ★★ **+5 XP**

Die Akademie verwahrt ihre Baupläne als Struktogramme. Übersetze in beide Richtungen.

<img src="media/d2edbf962899af527efed5a398f9651fa98e9360.png" title="s2_teiler.png" style="width:3.40625in;height:1.59375in" alt="s2_teiler.png" />

*Abbildung 1: Struktogramm der Methode anzahlTeiler*

|        |                                                                 |              |
|--------|-----------------------------------------------------------------|--------------|
| **a)** | Implementiere die Methode anzahlTeiler aus Abbildung 1 in Java. | **\[3 BE\]** |

<img src="media/a20dbaa7a2a8c601a370f61b461e5647fba5eb49.png" title="grid_17_5.png" style="width:6.69792in;height:1.96875in" alt="grid_17_5.png" />

|        |                                                                                                              |              |
|--------|--------------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Gib anzahlTeiler(12) und anzahlTeiler(7) an. Beschreibe, welche Zahlen n ≥ 2 genau den Rückgabewert 2 haben. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

Der Schatzmeister legt Gold an: Jedes Jahr kommt ein Zehntel (ganzzahlig) dazu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int jahreBisZiel(int gold, int ziel) {</p>
<p>int jahre = 0;</p>
<p>while (gold &lt; ziel) {</p>
<p>gold = gold + gold / 10;</p>
<p>jahre++;</p>
<p>}</p>
<p>return jahre;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

|        |                                                                   |              |
|--------|-------------------------------------------------------------------|--------------|
| **c)** | Stelle die Methode jahreBisZiel als Struktogramm nach EH § 5 dar. | **\[3 BE\]** |

<img src="media/a20dbaa7a2a8c601a370f61b461e5647fba5eb49.png" title="grid_17_5.png" style="width:6.69792in;height:1.96875in" alt="grid_17_5.png" />

|        |                                                                                 |              |
|--------|---------------------------------------------------------------------------------|--------------|
| **d)** | Gib jahreBisZiel(100, 150) an. Notiere dazu die Werte von gold nach jedem Jahr. | **\[2 BE\]** |

|     |
|-----|
|     |

|        |                                                                                                                     |              |
|--------|---------------------------------------------------------------------------------------------------------------------|--------------|
| **e)** | Für manche Startwerte endet die Methode nie (bei ziel \> gold). Gib alle diese Startwerte für gold an und begründe. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

**Aufgabe 7: Level 0.2 – Die Werkstatt** **IDE** ★ – ★★★ **bis +60 XP**

|        |                                                                                                                                                                                                                                                            |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **a)** | Lege in der Online-IDE den Workspace **AlgoQuest_W0_Akademie** an (oder öffne den ausgeteilten) und darin eine Datei mit dem Inhalt von AQ_W0_Akademie_Geruest.txt. Lies die ANLEITUNG am Dateianfang. Heute arbeitest du nur in der Klasse **Werkstatt**. |

|        |                                                                                                                                                                                                              |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **b)** | Über jeder Methode stehen ihre Signatur in Abi-Notation und eine Beschreibung. Ersetze // TODO Level 0.2 und das vorläufige return durch deine Lösung. Starte im Testrunner die Testklasse L02WerkstattTest. |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 55%" />
<col style="width: 18%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Stufe</strong></th>
<th><strong>Methoden (Signatur wie im Abitur)</strong></th>
<th><strong>Tests beginnen mit</strong></th>
<th><strong>XP</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>★ Basis</td>
<td><p>istGerade(n: Ganzzahl): Wahrheitswert</p>
<p>restGold(gold: Ganzzahl, preis: Ganzzahl): Ganzzahl</p>
<p>kistenBenoetigt(anzahl: Ganzzahl, proKiste: Ganzzahl): Ganzzahl</p></td>
<td>basis_</td>
<td><strong>+10</strong></td>
</tr>
<tr class="even">
<td>★★ Erweiterung</td>
<td><p>schadensstufe(schaden: Ganzzahl): Zeichenkette</p>
<p>durchschnitt(a: Ganzzahl, b: Ganzzahl, c: Ganzzahl): Kommazahl</p>
<p>quersumme(n: Ganzzahl): Ganzzahl</p></td>
<td>erweiterung_</td>
<td><strong>+20</strong></td>
</tr>
<tr class="odd">
<td>★★★ Experte</td>
<td><p>potenz(basis: Ganzzahl, exponent: Ganzzahl): Ganzzahl</p>
<p>ggT(a: Ganzzahl, b: Ganzzahl): Ganzzahl</p>
<p>istPrimzahl(n: Ganzzahl): Wahrheitswert</p></td>
<td>experte_</td>
<td><strong>+30</strong></td>
</tr>
</tbody>
</table>

Eine Stufe ist geschafft, wenn **alle** Tests mit diesem Anfang grün sind. Lies bei roten Tests die Meldung – sie nennt den Fall, der noch nicht klappt.

|        |                                                                                                                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **c)** | **Vorhersage ohne Gerät:** Im Hauptprogramm ganz unten steht das „Wert-Rätsel“ mit int jahr = 2026;. Notiere, welche Quersumme und welchen Wert von jahr das Programm ausgibt. Starte es erst danach und vergleiche. |

|     |
|-----|
|     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Tipps aus der Werkstatt</strong></p>
<ul>
<li><p><strong>istGerade:</strong> Teste auch negative Zahlen. -3 % 2 ergibt −1 – frage deshalb nach == 0.</p></li>
<li><p><strong>kistenBenoetigt:</strong> Ob eine angefangene Kiste dazukommt, verrät dir %. Ohne Math.ceil!</p></li>
<li><p><strong>durchschnitt:</strong> Die Casting-Falle aus Infoteil 2 wartet hier auf dich.</p></li>
<li><p><strong>quersumme:</strong> n % 10 ist die letzte Ziffer, n / 10 streicht sie.</p></li>
<li><p><strong>ggT (Euklid):</strong> ggT(a, b) = ggT(b, a % b) und ggT(a, 0) = a. Ersetze (a, b) so lange durch (b, a % b), bis b = 0 ist.</p></li>
<li><p><strong>istPrimzahl:</strong> Es genügt, Teiler t mit t * t &lt;= n zu prüfen.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Aufgabe 8: Bug-Hunt in der Werkstatt** **PAPIER** ★★ **+5 XP**

Vier Lehrlinge haben Werkstatt-Methoden abgegeben. In jeder steckt **genau ein** Fehler.

**Methode A** – soll true liefern, wenn n ungerade ist:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static boolean istUngerade(int n) {</p>
<p>2 return n % 2 == 1;</p>
<p>3 }</p></td>
</tr>
</tbody>
</table>

**Methode B** – soll die Summe 1 + 2 + … + n liefern:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static int summeBis(int n) {</p>
<p>2 int summe = 0;</p>
<p>3 int i = 1;</p>
<p>4 while (i &lt;= n) {</p>
<p>5 summe = summe + i;</p>
<p>6 }</p>
<p>7 return summe;</p>
<p>8 }</p></td>
</tr>
</tbody>
</table>

**Methode C** – soll „pleite“ liefern, wenn kein Gold mehr da ist, sonst „flüssig“:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static String kasse(int gold) {</p>
<p>2 if (gold = 0) {</p>
<p>3 return "pleite";</p>
<p>4 }</p>
<p>5 return "flüssig";</p>
<p>6 }</p></td>
</tr>
</tbody>
</table>

**Methode D** – soll true liefern, wenn jemand Jugendlicher ist (13 bis 17 Jahre):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static boolean istJugendlich(int alter) {</p>
<p>2 return alter &gt; 12 || alter &lt; 18;</p>
<p>3 }</p></td>
</tr>
</tbody>
</table>

|        |                                                                                          |              |
|--------|------------------------------------------------------------------------------------------|--------------|
| **a)** | Gib für jede Methode die fehlerhafte Zeile an, beschreibe den Fehler und korrigiere ihn. | **\[4 BE\]** |

| **Methode** | **Zeile** | **Fehler** | **Korrektur** |
|-------------|-----------|------------|---------------|
| A           |           |            |               |
| B           |           |            |               |
| C           |           |            |               |
| D           |           |            |               |

|        |                                                                                                                      |              |
|--------|----------------------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Welcher der vier Fehler wird schon vom **Compiler** gemeldet? Welcher fällt erst beim **Ausführen** auf – und woran? | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

|        |                                                                                          |              |
|--------|------------------------------------------------------------------------------------------|--------------|
| **c)** | Gib zu Methode A und zu Methode D je einen Aufruf an, der ein falsches Ergebnis liefert. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Für Schnelle: Zahlen mit Eigenschaften</strong></p>
<p>Schreibe in einer eigenen Klasse Zahlenkunde passende Methoden mit Signatur und teste sie im Hauptprogramm. Nutze dabei Methoden aus deiner Werkstatt (Aufruf z. B. Werkstatt.potenz(3, 3)).</p>
<ul>
<li><p><strong>Perfekte Zahlen:</strong> Eine Zahl ist perfekt, wenn sie gleich der Summe ihrer echten Teiler ist (6 = 1 + 2 + 3). Finde alle perfekten Zahlen unter 10 000. Es sind erstaunlich wenige.</p></li>
<li><p><strong>Armstrong-Zahlen:</strong> Eine dreistellige Zahl, die gleich der Summe der dritten Potenzen ihrer Ziffern ist: 153 = 1³ + 5³ + 3³. Finde alle vier.</p></li>
<li><p><strong>Rekordhalter der Zauberfolge:</strong> Welche Startzahl bis 1000 braucht mit schritte aus Aufgabe 5 die meisten Schritte? Probiere auch n = 27.</p></li>
</ul>
<p>Side-Quest: <strong>+15 bis +40 XP</strong> je nach Umfang.</p></td>
</tr>
</tbody>
</table>
