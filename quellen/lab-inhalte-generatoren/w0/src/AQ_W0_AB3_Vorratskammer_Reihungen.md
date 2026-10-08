<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>WELT 0 · DOPPELSTUNDE 3 · LEVEL 0.3</strong></p>
<p><strong>W0·3 – Die Vorratskammer: Reihungen und Zeichenketten</strong></p>
<p>Datei: AQ_W0_Akademie_Geruest.txt (Klasse Vorrat) · IDE-Level 0.3: bis <strong>+60 XP</strong> · Papier-Aufgaben: je <strong>+5 XP</strong></p></td>
</tr>
</tbody>
</table>

Unter der Werkstatt liegt die **Vorratskammer** der Akademie: lange Regale mit nummerierten Fächern voller Kräuter, Kristalle und Tränke. Der Kammermeister führt über jedes Regal Buch – nicht mit hundert einzelnen Variablen, sondern mit einer **Reihung**: ein Name, viele Fächer, jedes mit seiner Nummer.

Reihungen stecken in fast jeder Abituraufgabe. Wer hier sauber mit Index, Länge und Schleifengrenzen umgeht, verschenkt später keine BE. Und weil auf den Etiketten Text steht, lernst du auch, welche **Zeichenketten-Operationen** im Abitur erlaubt sind.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 1: Reihungen anlegen, lesen, schreiben</strong></p>
<p><img src="media/75157958ee762c0335bc42bf3b150cff4ee14ec6.png" title="p3_regal.png" style="width:4.53125in;height:0.8125in" alt="p3_regal.png" /></p>
<p><em>Abbildung 1: Die Variable vorrat verweist auf eine Reihung mit fünf Fächern</em></p>
<ul>
<li><p><strong>Anlegen mit Werten:</strong> int[] vorrat = {4, 0, 7, 0, 12}; – die Länge (5) ergibt sich aus den Werten.</p></li>
<li><p><strong>Anlegen mit Länge:</strong> int[] regal = new int[6]; – alle Fächer sind mit dem Standardwert gefüllt: 0 bei Ganzzahlen, 0.0 bei Kommazahlen, false bei Wahrheitswerten, null bei Zeichenketten und Objekten. Die Länge ist danach <strong>fest</strong>.</p></li>
<li><p><strong>Zugriff über den Index:</strong> vorrat[2] liefert 7, vorrat[1] = 5; schreibt in das zweite Fach. Der Index läuft von <strong>0 bis Länge − 1</strong>.</p></li>
<li><p><strong>Länge:</strong> vorrat.length (ohne Klammern!) – bei Zeichenketten dagegen s.length() mit Klammern. Das letzte Element ist vorrat[vorrat.length - 1].</p></li>
<li><p><strong>Ungültiger Index</strong> (z. B. −1 oder 5): Das Programm bricht mit einer <strong>ArrayIndexOutOfBoundsException</strong> ab.</p></li>
</ul>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Java</strong></th>
<th><strong>Struktogramm (wie im Abitur)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>r.length</td>
<td>Länge von r</td>
</tr>
<tr class="even">
<td>int[] neu = new int[n];</td>
<td>neu ← neue Reihung von Ganzzahl der Länge n</td>
</tr>
<tr class="odd">
<td>r[i] = r[i] + 1;</td>
<td>r[i] ← r[i] + 1</td>
</tr>
<tr class="even">
<td>for (int i = 0; i &lt; r.length; i++)</td>
<td>für i von 0 bis Länge von r − 1</td>
</tr>
<tr class="odd">
<td>for (int x : r)</td>
<td>für jedes x in r</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

**Aufgabe 0: Blitz-Kata: Fach für Fach** **PAPIER** ★ **+5 XP**

Gegeben sind int\[\] r = {8, 3, 0, 5, 1}; und String s = "Vorrat";. Gib den Wert jedes Ausdrucks an. Führt ein Ausdruck zu einem Fehler, schreibe „Fehler“.

| **Ausdruck** | **r.length** | **r\[r.length - 1\]** | **r\[r\[4\]\]** | **r\[2\] + r\[3\]** | **r\[5\]** |
|--------------|--------------|-----------------------|-----------------|---------------------|------------|
| **Wert**     |              |                       |                 |                     |            |

| **Ausdruck** | **s.length()** | **s.charAt(2)** | **s.substring(1, 4)** | **s.charAt(s.length() - 1)** | **(int) s.charAt(0)** |
|--------------|----------------|-----------------|-----------------------|------------------------------|-----------------------|
| **Wert**     |                |                 |                       |                              |                       |

**Tipp:** 'V' hat den ASCII-Wert 86, 'A' den Wert 65, 'a' den Wert 97.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 2: for oder for-each?</strong></p>
<p>Beide Schleifen besuchen alle Elemente. Die <strong>for-each-Schleife</strong> liefert dir in x aber nur eine <strong>Kopie des Werts</strong> – keinen Index und keinen Zugriff auf das Fach selbst.</p></td>
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
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
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
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int summe = 0;</p>
<p>for (int x : r) {</p>
<p>summe = summe + x;</p>
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

| **Du willst …**                                            | **Zählschleife mit Index** | **for-each**                   |
|------------------------------------------------------------|----------------------------|--------------------------------|
| alle Werte nur **lesen** (Summe, Zählen, Suchen nach Wert) | ✓                          | ✓                              |
| Werte **verändern** (r\[i\] = …)                           | ✓                          | ✗ – x = … ändert nur die Kopie |
| die **Position** wissen (Index liefern)                    | ✓                          | ✗                              |
| mit **Nachbarn** vergleichen (r\[i - 1\], r\[i + 1\])      | ✓ (Grenzen anpassen!)      | ✗                              |
| nur einen **Teil** durchlaufen oder rückwärts              | ✓                          | ✗                              |

**Aufgabe 1: Regalbau** **PAPIER** ★ **+5 XP**

Der Kammermeister baut ein neues Regal und befüllt es.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 int[] regal = new int[6];</p>
<p>2 regal[0] = 5;</p>
<p>3 regal[regal.length - 1] = 2;</p>
<p>4 regal[2] = regal[0] + regal[5];</p>
<p>5 for (int i = 1; i &lt; regal.length; i = i + 2) {</p>
<p>6 regal[i] = regal[i - 1] * 2;</p>
<p>7 }</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                         |              |
|--------|-------------------------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Trage den Inhalt der Reihung nach jeder Anweisung ein. Für die Schleife: eine Zeile pro Durchlauf (mit dem Wert von i). | **\[4 BE\]** |

| **Zeitpunkt**    | **Index 0** | **Index 1** | **Index 2** | **Index 3** | **Index 4** | **Index 5** |     |
|------------------|-------------|-------------|-------------|-------------|-------------|-------------|-----|
| **nach Zeile 1** |             |             |             |             |             |             |     |
| **nach Zeile 2** |             |             |             |             |             |             |     |
| **nach Zeile 3** |             |             |             |             |             |             |     |
| **nach Zeile 4** |             |             |             |             |             |             |     |
| **i = \_\_\_\_** |             |             |             |             |             |             |     |
| **i = \_\_\_\_** |             |             |             |             |             |             |     |
| **i = \_\_\_\_** |             |             |             |             |             |             |     |

|        |                                                                                      |              |
|--------|--------------------------------------------------------------------------------------|--------------|
| **b)** | Ergänzt man die Anweisung regal\[6\] = 1;, bricht das Programm ab. Erläutere, warum. | **\[1 BE\]** |

|     |
|-----|
|     |
|     |

|        |                                                                                                                                           |              |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **c)** | Nach String\[\] namen = new String\[3\]; wird println(namen\[0\].length()); ausgeführt. Gib an, was in namen\[0\] steht und was passiert. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

**Aufgabe 2: for oder for-each?** **PAPIER** ★★ **+5 XP**

Für jede Aufgabe auf der Reihung vorrat soll eine Schleife geschrieben werden. Entscheide, welche Schleife geeignet ist, notiere den **Schleifenkopf** in Java und begründe kurz.

| **Nr.** | **Aufgabe**                                                        | **for / for-each** | **Schleifenkopf in Java** | **Begründung** |
|---------|--------------------------------------------------------------------|--------------------|---------------------------|----------------|
| 1       | Summe aller Vorräte bilden                                         |                    |                           |                |
| 2       | jeden Vorrat um 1 erhöhen                                          |                    |                           |                |
| 3       | Index des ersten leeren Fachs finden                               |                    |                           |                |
| 4       | prüfen, ob ein Fach mehr als 10 enthält                            |                    |                           |                |
| 5       | zählen, wie oft ein Fach mehr enthält als sein **rechter** Nachbar |                    |                           |                |

**Bewertung: \[5 BE\]**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 3: Referenz oder Kopie?</strong></p>
<p>Eine Reihungsvariable enthält <strong>nicht die Reihung selbst</strong>, sondern einen <strong>Verweis (Referenz)</strong> auf sie – im Bild ein Pfeil. Das hat Folgen:</p></td>
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
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int[] a = {1, 2, 3};</p>
<p>int[] b = a; // kopiert nur den Pfeil!</p>
<p>b[0] = 99; // a[0] ist jetzt auch 99</p></td>
</tr>
</tbody>
</table>
<p><img src="media/4da672bac62bf15d662c20bdcf25fa0fb0257e5b.png" title="p3_ref.png" style="width:2.98958in;height:1.05208in" alt="p3_ref.png" /></p></td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int[] a = {1, 2, 3};</p>
<p>int[] c = new int[a.length];</p>
<p>for (int i = 0; i &lt; a.length; i++) {</p>
<p>c[i] = a[i]; // Wert für Wert kopieren</p>
<p>}</p>
<p>c[0] = 99; // a bleibt {1, 2, 3}</p></td>
</tr>
</tbody>
</table>
<p><img src="media/51dfd846932d6dc48d511c57f36f9b8aff6ce0e8.png" title="p3_kopie.png" style="width:2.98958in;height:1.05208in" alt="p3_kopie.png" /></p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

- int\[\] b = a; erzeugt **keine** neue Reihung: a und b verweisen auf **dieselbe** Reihung. Jede Änderung über b ist auch über a sichtbar.

- Eine **echte Kopie** braucht new und eine Schleife, die jeden Wert einzeln überträgt.

- a == b vergleicht bei Reihungen die **Pfeile**, nicht die Inhalte. Zwei Reihungen mit gleichen Werten sind mit == verschieden.

**Aufgabe 3: Das Regal-Rätsel** **PAPIER** ★★ **+5 XP**

Ein Lehrling hat mit drei Etiketten und zwei Regalen experimentiert. Überlege zuerst – starte nichts!

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 int[] links = {2, 4, 6};</p>
<p>2 int[] rechts = links;</p>
<p>3 int[] neu = {2, 4, 6};</p>
<p>4 rechts[1] = 40;</p>
<p>5 neu[2] = 60;</p>
<p>6 links = neu;</p>
<p>7 links[0] = 20;</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                    |              |
|--------|--------------------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Zeichne das Speicherbild nach Zeile 7: Variablen als Kästchen, Reihungen als Kästchenreihe, Referenzen als Pfeile. | **\[3 BE\]** |

<img src="media/a20dbaa7a2a8c601a370f61b461e5647fba5eb49.png" title="grid_17_5.png" style="width:6.69792in;height:1.96875in" alt="grid_17_5.png" />

|        |                                                                                             |              |
|--------|---------------------------------------------------------------------------------------------|--------------|
| **b)** | Gib den Inhalt der drei Reihungen an, auf die links, rechts und neu nach Zeile 7 verweisen. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

|        |                                                                                                                                                                                                |              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **c)** | Gib die Werte von links == neu und rechts == neu an. Erläutere, warum {2, 4, 6} == {2, 4, 6} in diesem Sinn falsch wäre, und beschreibe, wie man zwei Reihungen auf **gleichen Inhalt** prüft. | **\[3 BE\]** |

|     |
|-----|
|     |
|     |
|     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 4: Eine neue Reihung zurückgeben</strong></p>
<p>Viele Abituraufgaben verlangen: „… liefert eine <strong>neue</strong> Reihung …; r bleibt unverändert.“ Das Muster hat immer drei Schritte:</p>
<p><strong>1.</strong> Neue Reihung der passenden Länge anlegen: int[] neu = new int[r.length];</p>
<p><strong>2.</strong> In einer Schleife aus r <strong>lesen</strong> und in neu <strong>schreiben</strong> – r selbst wird nie verändert.</p>
<p><strong>3.</strong> Die neue Reihung zurückgeben: return neu;</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int[] quadrate(int[] r) {</p>
<p>int[] neu = new int[r.length];</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>neu[i] = r[i] * r[i];</p>
<p>}</p>
<p>return neu;</p>
<p>}</p>
<p>// quadrate({3, -2, 5}) liefert {9, 4, 25}; die leere Reihung liefert eine leere Reihung</p></td>
</tr>
</tbody>
</table>
<p>Achtung: int[] neu = r; ist <strong>keine</strong> neue Reihung (Infoteil 3) – dann würde r verändert.</p></td>
</tr>
</tbody>
</table>

**Aufgabe 4: Ein Fach weiterrücken** **PAPIER** ★★★ **+5 XP**

Bei der Inventur rückt jeder Vorrat ein Fach nach rechts; der letzte wandert ganz nach vorn.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static int[] verschoben(int[] r) {</p>
<p>2 int[] neu = new int[r.length];</p>
<p>3 for (int i = 0; i &lt; r.length; i++) {</p>
<p>4 neu[(i + 1) % r.length] = r[i];</p>
<p>5 }</p>
<p>6 return neu;</p>
<p>7 }</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                  |              |
|--------|------------------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Erstelle eine Tracetabelle für den Aufruf verschoben(r) mit r = {7, 1, 5} und gib die zurückgegebene Reihung an. | **\[3 BE\]** |

| **i** | **(i + 1) % r.length** | **r\[i\]** | **neu (nach dem Durchlauf)** |
|-------|------------------------|------------|------------------------------|
|       |                        |            |                              |
|       |                        |            |                              |
|       |                        |            |                              |

|        |                                                                                                               |              |
|--------|---------------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Begründe, dass r unverändert bleibt. Erläutere, was sich ändern würde, wenn Zeile 2 int\[\] neu = r; lautete. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

|        |                                                                                                                                          |              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **c)** | Für die leere Reihung wäre % r.length eine Division durch 0. Begründe, warum verschoben trotzdem ohne Fehler eine leere Reihung liefert. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

|        |                                                      |              |
|--------|------------------------------------------------------|--------------|
| **d)** | Stelle die Methode als Struktogramm nach EH § 5 dar. | **\[3 BE\]** |

<img src="media/a20dbaa7a2a8c601a370f61b461e5647fba5eb49.png" title="grid_17_5.png" style="width:6.69792in;height:1.96875in" alt="grid_17_5.png" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 5: Zeichenketten – erlaubt oder verboten?</strong></p>
<p>Im Abitur ist die Liste der Zeichenketten-Operationen <strong>abschließend</strong> (AB 1, Teil B, Infoteil 4). Alles andere musst du aus den erlaubten Operationen selbst bauen:</p>
<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>verboten (Beispiele)</strong></th>
<th><strong>So geht es mit erlaubten Operationen</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>s.toLowerCase(), s.toUpperCase()</td>
<td>beide Fälle prüfen: c == 'a' || c == 'A'; umwandeln über ASCII: (char) (c + 32) macht aus 'D' ein 'd'</td>
</tr>
<tr class="even">
<td>s.indexOf(t)</td>
<td>Schleife über i mit charAt(i) bzw. substring(i, i + t.length()).equals(t)</td>
</tr>
<tr class="odd">
<td>s.replace(…), s.split(…), s.trim()</td>
<td>Schleife über die Zeichen, Ergebnis mit + zusammensetzen</td>
</tr>
<tr class="even">
<td>s.startsWith(t), s.endsWith(t)</td>
<td>erst die Längen prüfen, dann substring(…) und equals</td>
</tr>
<tr class="odd">
<td>s.isEmpty()</td>
<td>s.length() == 0</td>
</tr>
<tr class="even">
<td>Character.isDigit(c) u. Ä.</td>
<td>Bereich prüfen: c &gt;= '0' &amp;&amp; c &lt;= '9'</td>
</tr>
</tbody>
</table>
<ul>
<li><p><strong>Zeichen</strong> (char, einfache Anführungszeichen) vergleichst du mit ==: s.charAt(i) == 'e'. <strong>Zeichenketten</strong> vergleichst du mit equals.</p></li>
<li><p>s.charAt(i) == "e" kompiliert nicht: Zeichen und Zeichenkette sind verschiedene Typen.</p></li>
<li><p>s.compareTo(t) ist negativ, wenn s im Wörterbuch (genauer: nach ASCII-Werten) <strong>vor</strong> t steht, 0 bei Gleichheit, sonst positiv. Großbuchstaben stehen vor Kleinbuchstaben.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Aufgabe 5: Die verbotenen Etiketten** **PAPIER** ★★ **+5 XP**

Der Zauberlehrling hat drei Etiketten-Methoden mit **verbotenen** Operationen geschrieben:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static boolean endetMit(String s, String ende) {</p>
<p>return s.endsWith(ende);</p>
<p>}</p>
<p>public static int anzahlLeerzeichen(String s) {</p>
<p>return s.split(" ").length - 1;</p>
<p>}</p>
<p>public static boolean istGrossbuchstabe(char c) {</p>
<p>return Character.isUpperCase(c);</p>
<p>}</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                                              |              |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Schreibe alle drei Methoden so um, dass sie nur erlaubte Operationen verwenden. Achte bei endetMit darauf, dass ende länger als s sein kann. | **\[5 BE\]** |

<img src="media/a52d20433da9521b7b995f3a35505725a0462040.png" title="grid_17_8.png" style="width:6.69792in;height:3.14583in" alt="grid_17_8.png" />

|        |                                                      |              |
|--------|------------------------------------------------------|--------------|
| **b)** | Gib an, ob der Ausdruck negativ, 0 oder positiv ist. | **\[2 BE\]** |

| **Ausdruck**                  | **negativ, 0 oder positiv?** | **Ausdruck**             | **negativ, 0 oder positiv?** |
|-------------------------------|------------------------------|--------------------------|------------------------------|
| "Drache".compareTo("Drachen") |                              | "Eis".compareTo("Feuer") |                              |
| "elf".compareTo("Elf")        |                              | "Rune".compareTo("Rune") |                              |

|        |                                                                         |              |
|--------|-------------------------------------------------------------------------|--------------|
| **c)** | Gib den Wert an: (int) 'a' · (char) ('a' + 2) · (char) ((int) 'D' + 32) | **\[1 BE\]** |

|     |
|-----|
|     |

**Aufgabe 6: Level 0.3 – Die Vorratskammer** **IDE** ★ – ★★★ **bis +60 XP**

|        |                                                                                                             |
|--------|-------------------------------------------------------------------------------------------------------------|
| **a)** | Öffne deine Akademie-Datei aus DS 2. Heute arbeitest du in der Klasse **Vorrat**; Testklasse L03VorratTest. |

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
<td><p>anzahlLeer(r: Reihung von Ganzzahl): Ganzzahl</p>
<p>letzterWert(r: Reihung von Ganzzahl): Ganzzahl</p>
<p>enthaelt(r: Reihung von Ganzzahl, x: Ganzzahl): Wahrheitswert</p></td>
<td>basis_</td>
<td><strong>+10</strong></td>
</tr>
<tr class="even">
<td>★★ Erweiterung</td>
<td><p>umgedreht(r: Reihung von Ganzzahl): Reihung von Ganzzahl</p>
<p>verdopple(r: Reihung von Ganzzahl): nichts</p>
<p>anzahlAnstiege(r: Reihung von Ganzzahl): Ganzzahl</p></td>
<td>erweiterung_</td>
<td><strong>+20</strong></td>
</tr>
<tr class="odd">
<td>★★★ Experte</td>
<td><p>zaehleZeichen(s: Zeichenkette, c: Zeichen): Ganzzahl</p>
<p>ohneVokale(s: Zeichenkette): Zeichenkette</p>
<p>beginntMit(s: Zeichenkette, anfang: Zeichenkette): Wahrheitswert</p></td>
<td>experte_</td>
<td><strong>+30</strong></td>
</tr>
</tbody>
</table>

|        |                                                                                                                                                                                                                                         |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **b)** | **Vorhersage ohne Gerät:** Das Hauptprogramm enthält ein „Referenz-Rätsel“ (int\[\] b = a; b\[0\] = 99;) und gibt den Vorrat {4, 0, 7, 0, 12, 9} nach Vorrat.verdopple(vorrat) aus. Notiere beide Ausgaben, dann starte und vergleiche. |

|     |
|-----|
|     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Tipps aus der Vorratskammer</strong></p>
<ul>
<li><p><strong>Leere Reihung zuerst:</strong> Wo du auf r[0] oder r[r.length - 1] zugreifst, frage vorher r.length == 0 ab.</p></li>
<li><p><strong>Suche:</strong> return false gehört <strong>hinter</strong> die Schleife – nicht in einen else-Zweig.</p></li>
<li><p><strong>verdopple:</strong> Mit for-each änderst du nur Kopien (Infoteil 2).</p></li>
<li><p><strong>Zeichenketten:</strong> nur die erlaubten Operationen (Infoteil 5) – die Tests merken einen Verstoß nicht, das Abitur schon.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Aufgabe 7: Bug-Hunt in der Vorratskammer** **PAPIER** ★★ **+5 XP**

In jeder Methode steckt **genau ein** Fehler.

**Methode A** – soll true liefern, wenn r aufsteigend sortiert ist:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static boolean istSortiert(int[] r) {</p>
<p>2 for (int i = 0; i &lt; r.length; i++) {</p>
<p>3 if (r[i] &gt; r[i + 1]) {</p>
<p>4 return false;</p>
<p>5 }</p>
<p>6 }</p>
<p>7 return true;</p>
<p>8 }</p></td>
</tr>
</tbody>
</table>

**Methode B** – soll eine **neue** Reihung mit den dreifachen Werten liefern; r bleibt unverändert:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static int[] verdreifacht(int[] r) {</p>
<p>2 int[] neu = r;</p>
<p>3 for (int i = 0; i &lt; r.length; i++) {</p>
<p>4 neu[i] = r[i] * 3;</p>
<p>5 }</p>
<p>6 return neu;</p>
<p>7 }</p></td>
</tr>
</tbody>
</table>

**Methode C** – soll zählen, wie oft e oder E in s vorkommt:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static int anzahlE(String s) {</p>
<p>2 int anzahl = 0;</p>
<p>3 for (int i = 0; i &lt; s.length(); i++) {</p>
<p>4 if (s.charAt(i) == "e" || s.charAt(i) == 'E') {</p>
<p>5 anzahl++;</p>
<p>6 }</p>
<p>7 }</p>
<p>8 return anzahl;</p>
<p>9 }</p></td>
</tr>
</tbody>
</table>

**Methode D** – soll true liefern, wenn a und b gleich lang sind und an jeder Stelle denselben Wert haben:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static boolean gleicherInhalt(int[] a, int[] b) {</p>
<p>2 return a == b;</p>
<p>3 }</p></td>
</tr>
</tbody>
</table>

|        |                                                                          |              |
|--------|--------------------------------------------------------------------------|--------------|
| **a)** | Gib für jede Methode die fehlerhafte Zeile an und beschreibe den Fehler. | **\[4 BE\]** |

| **Methode** | **Zeile** | **Fehler** |
|-------------|-----------|------------|
| A           |           |            |
| B           |           |            |
| C           |           |            |
| D           |           |            |

|        |                                                                                                           |              |
|--------|-----------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Gib eine Reihung an, für die Methode A ohne Absturz ein Ergebnis liefert, und eine, bei der sie abbricht. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

|        |                                                                                                         |              |
|--------|---------------------------------------------------------------------------------------------------------|--------------|
| **c)** | Gib die Ausgabe an: int\[\] b = {1, 2, 3}; int\[\] c = verdreifacht(b); println(b\[0\] + " " + c\[0\]); | **\[1 BE\]** |

|     |
|-----|
|     |

|        |                                                                                             |              |
|--------|---------------------------------------------------------------------------------------------|--------------|
| **d)** | Korrigiere die Methoden A, B und C jeweils in einer Zeile. Implementiere Methode D korrekt. | **\[4 BE\]** |

<img src="media/7e19c3e3ed8ca9cbdd84b5f72c30f298eeca92a5.png" title="grid_17_6.png" style="width:6.69792in;height:2.36458in" alt="grid_17_6.png" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Für Schnelle: Die Lotterie der Kammer</strong></p>
<ul>
<li><p><strong>6 aus 49:</strong> Fülle eine Reihung der Länge 6 mit Zufallszahlen von 1 bis 49 – <strong>ohne</strong> doppelte Zahlen. Welche Methode aus deiner Klasse Vorrat hilft beim Prüfen?</p></li>
<li><p><strong>Der Reindrängler:</strong> eingefuegt(r: Reihung von Ganzzahl, pos: Ganzzahl, wert: Ganzzahl): Reihung von Ganzzahl liefert eine neue, um 1 längere Reihung, in der wert an Index pos steht; alle Werte ab pos rücken nach hinten. Zeichne dir die beiden Reihungen zuerst untereinander und verbinde alte und neue Indizes mit Pfeilen.</p></li>
<li><p><strong>Geheimschrift (Caesar):</strong> verschluessle(text: Zeichenkette, k: Ganzzahl): Zeichenkette verschiebt jeden Kleinbuchstaben um k Stellen im Alphabet („xyz“ mit k = 3 wird „abc“), alle anderen Zeichen bleiben. Nur mit charAt, +, (int), (char) und %. Knacke damit: „kdoor zhow“.</p></li>
</ul>
<p>Side-Quest: <strong>+15 bis +40 XP</strong> je nach Umfang.</p></td>
</tr>
</tbody>
</table>
