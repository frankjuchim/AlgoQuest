<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>WELT 0 · DOPPELSTUNDEN 4 UND 5 · LEVEL 0.4 + 0.5</strong></p>
<p><strong>W0·4 – Die Zauberschule: Eigene Methoden</strong></p>
<p>Datei: AQ_W0_Akademie_Geruest.txt (Klassen Zauber und ZauberII) · IDE-Level 0.4 und 0.5: je bis <strong>+60 XP</strong> · Papier-Aufgaben: je <strong>+5 XP</strong> · Teil 1 in DS 4, Teil 2 in DS 5</p></td>
</tr>
</tbody>
</table>

Im obersten Turm der Akademie liegt die **Zauberschule**. Hier lernst du keine fertigen Zauber auswendig – hier erfindest du eigene **Zauberformeln**. Jede Formel hat einen **Namen**, braucht **Zutaten** und hat eine **Wirkung**: Ein Heilzauber der Stufe 3 heilt 45 Leben. In Java heißt eine solche Formel **Methode**: Die Zutaten sind die **Parameter**, die Wirkung ist der **Rückgabewert**.

Warum so viel Aufwand? In **allen 22 Abituraufgaben 2022–2026** musste implementiert werden – und jedes Mal war es eine Methode mit vorgegebener Signatur: „Implementieren Sie die Methode …“. Wer Signaturen sicher übersetzt, Rückgabepfade im Blick hat und weiß, was mit Parametern passiert, holt diese BE zuverlässig.

**Teil 1 – Zauberformeln: Methoden bauen und aufrufen (DS 4)**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 1: Die Anatomie einer Methode</strong></p>
<p><img src="media/f8896364abb156d098ec3de06d6a266e9dba01d2.png" title="a4_anatomie.png" style="width:6.45833in;height:3.1875in" alt="a4_anatomie.png" /></p>
<p><em>Abbildung 1: Bestandteile der Methode wiederhole</em></p>
<ul>
<li><p>Der <strong>Kopf</strong> legt fest, wie man die Methode benutzt: <strong>Rückgabetyp</strong> (was kommt heraus?), <strong>Name</strong>, <strong>Parameterliste</strong> (was muss man hineingeben?). Der <strong>Rumpf</strong> in geschweiften Klammern sagt, wie sie arbeitet.</p></li>
<li><p>Die <strong>Signatur</strong> im Abitur ist der Kopf in sprachunabhängiger Form: wiederhole(text: Zeichenkette, anzahl: Ganzzahl): Zeichenkette.</p></li>
<li><p>static bedeutet: Die Methode gehört zur Klasse selbst (eine <strong>Klassenoperation</strong>). In der Akademie sind alle Methoden public static; ab Welt 1 schreibst du Methoden für Objekte – dann ohne static.</p></li>
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
<td><p><strong>Infoteil 2: Von der Abi-Signatur zum Java-Methodenkopf</strong></p>
<p><img src="media/e1396961bc0be692033f100ff3111654d06a9d6b.png" title="a4_uebersetzung.png" style="width:6.45833in;height:1.47917in" alt="a4_uebersetzung.png" /></p>
<p><em>Abbildung 2: Was wohin wandert</em></p>
<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Abi-Signatur</strong></th>
<th><strong>Java-Methodenkopf</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>istLeer(r: Reihung von Ganzzahl): Wahrheitswert</td>
<td>public static boolean istLeer(int[] r)</td>
</tr>
<tr class="even">
<td>mittel(a: Kommazahl, b: Kommazahl): Kommazahl</td>
<td>public static double mittel(double a, double b)</td>
</tr>
<tr class="odd">
<td>zeigeMenue(): nichts</td>
<td>public static void zeigeMenue()</td>
</tr>
<tr class="even">
<td>initiale(name: Zeichenkette): Zeichen</td>
<td>public static char initiale(String name)</td>
</tr>
<tr class="odd">
<td>titelListe(n: Ganzzahl): Reihung von Zeichenkette</td>
<td>public static String[] titelListe(int n)</td>
</tr>
</tbody>
</table>
<p><strong>1.</strong> Der <strong>Rückgabetyp</strong> wandert von hinten nach vorn; „nichts“ wird zu void.</p>
<p><strong>2.</strong> Bei jedem <strong>Parameter</strong> steht erst der Typ, dann der Name – ohne Doppelpunkt. <strong>Jeder</strong> Parameter bekommt seinen eigenen Typ: int a, int b (nicht int a, b).</p>
<p><strong>3.</strong> Die <strong>Reihenfolge</strong> der Parameter bleibt genau gleich. Keine Parameter: leere Klammern ().</p>
<p><strong>4.</strong> Typnamen übersetzen: Ganzzahl → int, Kommazahl → double, Wahrheitswert → boolean, Zeichen → char, Zeichenkette → String, Reihung von X → X[] (vollständige Liste: AB 1, Teil B).</p></td>
</tr>
</tbody>
</table>

**Aufgabe 0: Blitz-Kata: Den Kopf zerlegen** **PAPIER** ★ **+5 XP**

Gegeben ist der Kopf public static double trankPreis(int menge, boolean eilig, String sorte).

| **Name** | **Rückgabetyp** | **Anzahl der Parameter** | **Typ des 2. Parameters** | **Signatur in Abi-Notation** |
|----------|-----------------|--------------------------|---------------------------|------------------------------|
|          |                 |                          |                           |                              |

**Aufgabe 1: Das Übersetzungsbüro der Zauberschule** **PAPIER** ★ **+5 XP**

|        |                                                                                    |              |
|--------|------------------------------------------------------------------------------------|--------------|
| **a)** | Gib zu jeder Signatur den Java-Methodenkopf an (alle Methoden sind public static). | **\[3 BE\]** |

| **Nr.** | **Abi-Signatur**                                                      | **Java-Methodenkopf** |
|---------|-----------------------------------------------------------------------|-----------------------|
| 1       | istMagisch(zahl: Ganzzahl): Wahrheitswert                             |                       |
| 2       | flaeche(breite: Kommazahl, hoehe: Kommazahl): Kommazahl               |                       |
| 3       | begruesse(name: Zeichenkette): nichts                                 |                       |
| 4       | letztesZeichen(s: Zeichenkette): Zeichen                              |                       |
| 5       | zufallsReihung(laenge: Ganzzahl, max: Ganzzahl): Reihung von Ganzzahl |                       |
| 6       | startSignal(): nichts                                                 |                       |

|        |                                                                 |              |
|--------|-----------------------------------------------------------------|--------------|
| **b)** | Gib zu jedem Java-Methodenkopf die Signatur in Abi-Notation an. | **\[3 BE\]** |

| **Nr.** | **Java-Methodenkopf**                                           | **Abi-Signatur** |
|---------|-----------------------------------------------------------------|------------------|
| 7       | public static int anzahlZiffern(int n)                          |                  |
| 8       | public static String verbinde(String a, String b, char trenner) |                  |
| 9       | public static void leere(int\[\] regal)                         |                  |
| 10      | public static boolean enthaeltZeichen(String s, char c)         |                  |
| 11      | public static double\[\] halbiert(int\[\] werte)                |                  |

**Aufgabe 2: Vom Auftrag zum Methodenkopf** **PAPIER** ★★ **+5 XP**

Im Abitur steht oft nur ein Text – die Signatur musst du dir selbst zusammensetzen. Gib zu jeder Beschreibung die Abi-Signatur **und** den Java-Methodenkopf an. Wähle sinnvolle Parameternamen.

| **Nr.** | **Beschreibung**                                                                                                                         | **Abi-Signatur / Java-Methodenkopf** |
|---------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| 1       | Die Methode **anzahlUnter** erhält eine Reihung von Ganzzahlen und eine Grenze und liefert, wie viele Werte kleiner als die Grenze sind. |                                      |
| 2       | Die Methode **istVolljaehrig** prüft für ein Alter, ob es mindestens 18 ist.                                                             |                                      |
| 3       | Die Methode **ausgeben** gibt alle Werte einer Reihung von Zeichenketten zeilenweise auf der Konsole aus.                                |                                      |
| 4       | Die Methode **mittelwert** berechnet den Durchschnitt der Werte einer Reihung von Ganzzahlen.                                            |                                      |
| 5       | Die Methode **haeufigstesZeichen** liefert das Zeichen, das in einer Zeichenkette am häufigsten vorkommt.                                |                                      |
| 6       | Die Methode **ohneDuplikate** liefert eine neue Reihung, die jeden Wert einer gegebenen Reihung von Ganzzahlen nur einmal enthält.       |                                      |

**Bewertung: \[6 BE\]**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 3: Aufrufen – Parameter und Argumente</strong></p>
<p>Eine Methode wird erst durch einen <strong>Aufruf</strong> wirksam. Beim Aufruf übergibst du <strong>Argumente</strong>; sie werden der Reihe nach in die <strong>Parameter</strong> kopiert.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>String a = wiederhole("Ha", 3); // Rückgabe speichern: "HaHaHa"</p>
<p>println(wiederhole("ab", 2) + "!"); // ausgeben: abab!</p>
<p>if (wiederhole("x", n).length() &gt; 5) { … } // in einer Bedingung verwenden</p>
<p>String b = wiederhole(wiederhole("x", 2), 3); // als Argument: "xxxxxx"</p>
<p>wiederhole("Ha", 3); // erlaubt – aber die Rückgabe geht verloren!</p></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 47%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Begriff</strong></th>
<th><strong>Wo?</strong></th>
<th><strong>Beispiel</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Parameter</strong></td>
<td>im Methodenkopf: Variable mit Typ, ein Platzhalter</td>
<td>String text, int anzahl</td>
</tr>
<tr class="even">
<td><strong>Argument</strong></td>
<td>beim Aufruf: konkreter Wert oder Ausdruck</td>
<td>"Ha", 3, n + 1, wiederhole("x", 2)</td>
</tr>
</tbody>
</table>
<ul>
<li><p>Anzahl, Reihenfolge und Typen der Argumente müssen zu den Parametern passen. Eine Ganzzahl darf an einen Kommazahl-Parameter übergeben werden (wird umgewandelt), eine Kommazahl an einen Ganzzahl-Parameter <strong>nicht</strong>.</p></li>
<li><p>Der <strong>Rückgabetyp</strong> bestimmt, wo der Aufruf stehen darf: double d = heilwert(4); geht (Ganzzahl → Kommazahl), int x = spruchtext("Eis", 1); nicht.</p></li>
<li><p>Aufruf <strong>aus derselben Klasse</strong>: nur der Name, z. B. max2(a, b). Aufruf <strong>aus dem Hauptprogramm</strong> oder einer anderen Klasse: mit Klassennamen, z. B. Zauber.heilwert(3).</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Aufgabe 3: Passt der Zauber?** **PAPIER** ★★ **+5 XP**

Die Klasse Zauber enthält (wie im Gerüst) diese drei Methoden:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int heilwert(int stufe) // Stufe * 15</p>
<p>public static boolean istStaerker(int a, int b) // a &gt; b</p>
<p>public static String spruchtext(String name, int stufe) // z. B. "Feuerball (Stufe 3)"</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                                                                 |              |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Entscheide für jede Anweisung im Hauptprogramm, ob der Compiler sie akzeptiert. Gib bei akzeptierten Anweisungen den Wert bzw. die Ausgabe an, sonst den Grund. | **\[4 BE\]** |

|     | **Anweisung**                                            | **ok?** | **Wert / Ausgabe bzw. Grund** |
|-----|----------------------------------------------------------|---------|-------------------------------|
| A   | int h = Zauber.heilwert(2) + Zauber.heilwert(1);         |         |                               |
| B   | String t = Zauber.spruchtext(3, "Blitz");                |         |                               |
| C   | boolean b = Zauber.istStaerker(Zauber.heilwert(2), 25);  |         |                               |
| D   | int x = Zauber.spruchtext("Eis", 1);                     |         |                               |
| E   | println(Zauber.spruchtext("Licht", Zauber.heilwert(1))); |         |                               |
| F   | double d = Zauber.heilwert(4);                           |         |                               |
| G   | int y = Zauber.heilwert(2.5);                            |         |                               |
| H   | Zauber.istStaerker(3);                                   |         |                               |

|        |                                                                         |              |
|--------|-------------------------------------------------------------------------|--------------|
| **b)** | Benenne für Anweisung C die Parameter und die Argumente beider Aufrufe. | **\[2 BE\]** |

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
<td><p><strong>Infoteil 4: return – Rückgabepfade und void</strong></p>
<ul>
<li><p>return wert; liefert den Wert an die Aufrufstelle und <strong>beendet die Methode sofort</strong>. Anweisungen direkt dahinter erreicht Java nie (Compilerfehler „unreachable statement“).</p></li>
<li><p>Hat die Methode einen Rückgabetyp, muss <strong>jeder mögliche Ablauf</strong> mit einem return enden. Der Compiler prüft das, ohne die Bedingungen zu verstehen – sonst meldet er „missing return statement“.</p></li>
<li><p>Eine void-Methode liefert <strong>nichts</strong>. Sie bewirkt etwas (Ausgabe, Änderung einer Reihung). Mit return; (ohne Wert) darf sie vorzeitig enden.</p></li>
<li><p>Im Struktogramm: „gib … zurück“ – auch dort beendet es die Operation.</p></li>
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
<td><table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Akzeptiert:</strong> Das letzte return fängt alle übrigen Fälle.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int vorzeichen(int n) {</p>
<p>if (n &gt; 0) {</p>
<p>return 1;</p>
<p>} else if (n &lt; 0) {</p>
<p>return -1;</p>
<p>}</p>
<p>return 0;</p>
<p>}</p></td>
</tr>
</tbody>
</table></td>
<td><p><strong>Abgelehnt</strong> („missing return statement“) – obwohl inhaltlich jeder Fall abgedeckt ist:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int vorzeichen(int n) {</p>
<p>if (n &gt; 0) {</p>
<p>return 1;</p>
<p>} else if (n &lt; 0) {</p>
<p>return -1;</p>
<p>} else if (n == 0) {</p>
<p>return 0;</p>
<p>}</p>
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

**Aufgabe 4: Der Compiler-Detektiv** **PAPIER** ★★ **+5 XP**

Fünf Lehrlinge haben Zauberformeln abgegeben.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>// M1</p>
<p>public static int klassifiziere(int n) {</p>
<p>if (n &gt; 0) { return 1; }</p>
<p>if (n &lt; 0) { return -1; }</p>
<p>return 0;</p>
<p>}</p>
<p>// M2</p>
<p>public static String bewerte(int p) {</p>
<p>if (p &gt;= 10) { return "gut"; } else if (p &gt;= 5) { return "ok"; }</p>
<p>}</p>
<p>// M3</p>
<p>public static int ersteGerade(int[] r) {</p>
<p>for (int x : r) {</p>
<p>if (x % 2 == 0) { return x; }</p>
<p>}</p>
<p>return -1;</p>
<p>}</p>
<p>// M4</p>
<p>public static boolean pruefe(int n) {</p>
<p>return n &gt; 5;</p>
<p>println("geprüft");</p>
<p>}</p>
<p>// M5</p>
<p>public static void melde(int n) {</p>
<p>if (n &lt; 0) { return; }</p>
<p>println("Wert: " + n);</p>
<p>}</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                                            |              |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Entscheide, welche Methoden der Compiler akzeptiert. Gib bei abgelehnten Methoden den Grund an, bei akzeptierten das Ergebnis des Aufrufs. | **\[5 BE\]** |

|     | **akzeptiert?** | **Grund bzw. Ergebnis für den Aufruf** |
|-----|-----------------|----------------------------------------|
| M1  |                 | klassifiziere(-7):                     |
| M2  |                 |                                        |
| M3  |                 | ersteGerade({3, 7, 4, 8}):             |
| M4  |                 |                                        |
| M5  |                 | melde(-3):                             |

|        |                                             |              |
|--------|---------------------------------------------|--------------|
| **b)** | Stelle M1 als Struktogramm nach EH § 5 dar. | **\[2 BE\]** |

<img src="media/a20dbaa7a2a8c601a370f61b461e5647fba5eb49.png" title="grid_17_5.png" style="width:6.69792in;height:1.96875in" alt="grid_17_5.png" />

|        |                                                                            |              |
|--------|----------------------------------------------------------------------------|--------------|
| **c)** | Korrigiere M2 so, dass sie für alle Punktzahlen unter 5 "schwach" liefert. | **\[1 BE\]** |

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
<td><p><strong>Infoteil 5: Lokale Variablen und Gültigkeit</strong></p>
<ul>
<li><p>Variablen, die in einer Methode deklariert werden, und die <strong>Parameter</strong> sind <strong>lokal</strong>: Sie entstehen beim Aufruf und verschwinden beim Ende der Methode. Von außen sieht man sie nicht.</p></li>
<li><p>Ein Parameter ist eine lokale Variable, die beim Aufruf mit dem <strong>Wert des Arguments</strong> vorbelegt wird.</p></li>
<li><p>Gleicher Name heißt <strong>nicht</strong> gleiche Variable: Ein kraft im Hauptprogramm und ein Parameter kraft sind zwei verschiedene Kästchen.</p></li>
<li><p>Eine Variable gilt nur in dem <strong>Block</strong> { … }, in dem sie deklariert ist – die Zählvariable i einer for-Schleife also nur in der Schleife.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Aufgabe 5: Wer sieht wen?** **PAPIER** ★★ **+5 XP**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static int zauber(int kraft) {</p>
<p>2 int bonus = 5;</p>
<p>3 kraft = kraft + bonus;</p>
<p>4 return kraft * 2;</p>
<p>5 }</p>
<p>6 // Hauptprogramm</p>
<p>7 int kraft = 10;</p>
<p>8 int bonus = 1;</p>
<p>9 int ergebnis = zauber(kraft);</p>
<p>10 println(kraft + " " + bonus + " " + ergebnis);</p></td>
</tr>
</tbody>
</table>

|        |                                                                                            |              |
|--------|--------------------------------------------------------------------------------------------|--------------|
| **a)** | Gib die Ausgabe an und begründe, warum sich kraft und bonus im Hauptprogramm nicht ändern. | **\[3 BE\]** |

|     |
|-----|
|     |
|     |
|     |

Ein Lehrling hat diese Methode geschrieben und im Hauptprogramm println(summe); ergänzt:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static int summeBis(int n) {</p>
<p>2 int summe = 0;</p>
<p>3 for (int i = 1; i &lt;= n; i++) {</p>
<p>4 int quadrat = i * i;</p>
<p>5 summe = summe + quadrat;</p>
<p>6 }</p>
<p>7 println(i);</p>
<p>8 println(quadrat);</p>
<p>9 return summe;</p>
<p>10 }</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                                                   |              |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Der Compiler meldet drei Fehler „cannot find symbol“. Gib die drei Stellen an (zwei in der Methode, eine im Hauptprogramm) und erläutere jeweils. | **\[3 BE\]** |

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
<td><p><strong>Infoteil 6: Methode ruft Methode – das Aufrufprotokoll</strong></p>
<p>Methoden dürfen andere Methoden aufrufen. Die aufrufende Methode <strong>wartet</strong>, bis die aufgerufene ihr Ergebnis liefert, und rechnet dann weiter. So zerlegt man Probleme in kleine, einzeln prüfbare Teile.</p></td>
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
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int quadrat(int x) {</p>
<p>return x * x;</p>
<p>}</p>
<p>public static int summeDerQuadrate(int a, int b) {</p>
<p>int summe = 0;</p>
<p>for (int i = a; i &lt;= b; i++) {</p>
<p>summe = summe + quadrat(i);</p>
<p>}</p>
<p>return summe;</p>
<p>}</p></td>
</tr>
</tbody>
</table>
<p><img src="media/b14e7e13051e517d7565aa64dabcc13d05c3a8f7.png" title="s4_sdq.png" style="width:3.73958in;height:1.13542in" alt="s4_sdq.png" /></p></td>
</tr>
</tbody>
</table>

**Aufrufprotokoll** für summeDerQuadrate(2, 4) – eine Zeile pro Aufruf der Hilfsmethode:

| **i**            | **Aufruf** | **Rückgabe** | **summe**     |
|------------------|------------|--------------|---------------|
| vor der Schleife | –          | –            | 0             |
| 2                | quadrat(2) | 4            | 4             |
| 3                | quadrat(3) | 9            | 13            |
| 4                | quadrat(4) | 16           | 29            |
| Ende             |            |              | gib 29 zurück |

**Aufgabe 6: Die Runen der Zauberschule** **PAPIER** ★★ **+5 XP**

Auf den Türen der Zauberschule stehen Runen. Ihr Wert wird mit zwei Methoden berechnet:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static int runenwert(char c) {</p>
<p>2 if (c == 'X') {</p>
<p>3 return 10;</p>
<p>4 }</p>
<p>5 if (c == 'V') {</p>
<p>6 return 5;</p>
<p>7 }</p>
<p>8 if (c == 'I') {</p>
<p>9 return 1;</p>
<p>10 }</p>
<p>11 return 0;</p>
<p>12 }</p>
<p>13</p>
<p>14 public static int runenSumme(String s) {</p>
<p>15 int summe = 0;</p>
<p>16 for (int i = 0; i &lt; s.length(); i++) {</p>
<p>17 summe = summe + runenwert(s.charAt(i));</p>
<p>18 }</p>
<p>19 return summe;</p>
<p>20 }</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                                                        |              |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Erstelle ein Aufrufprotokoll für runenSumme("XVIIa"): erste Zeile vor der Schleife, dann eine Zeile pro Aufruf von runenwert. Gib den Rückgabewert an. | **\[3 BE\]** |

| **i**            | **Aufruf von runenwert** | **Rückgabe** | **summe** |
|------------------|--------------------------|--------------|-----------|
| vor der Schleife |                          |              |           |
|                  |                          |              |           |
|                  |                          |              |           |
|                  |                          |              |           |
|                  |                          |              |           |
|                  |                          |              |           |

Rückgabewert: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

|        |                                                                                                                              |              |
|--------|------------------------------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Gib an, wie oft runenwert bei der Anweisung int z = runenSumme("XXX") + runenSumme(""); aufgerufen wird, und den Wert von z. | **\[2 BE\]** |

|     |
|-----|
|     |

|        |                                                                                                                                                                                                                 |              |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **c)** | Gegeben ist public static int verdopple(int x) { return x \* 2; }. Gib für int e = verdopple(3) + verdopple(verdopple(1)); die **Reihenfolge** aller Aufrufe mit Argument und Rückgabe sowie den Wert von e an. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

|        |                                                                                              |              |
|--------|----------------------------------------------------------------------------------------------|--------------|
| **d)** | Nenne zwei Vorteile davon, den Wert einer einzelnen Rune in eine eigene Methode auszulagern. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

**Aufgabe 7: Level 0.4 – Die Zauberschule** **PAPIER → IDE** ★ – ★★★ **bis +60 XP**

In der Klasse **Zauber** sind nur die Köpfe der Stufe Basis vorgegeben. Für Erweiterung und Experte steht im Gerüst **nur die Abi-Signatur** – den Java-Kopf schreibst du selbst. Damit das Programm trotzdem kompiliert, sind die passenden Tests auskommentiert. Du schaltest sie frei, sobald deine Köpfe stehen.

|        |                                                                    |              |
|--------|--------------------------------------------------------------------|--------------|
| **a)** | **Erst Papier:** Schreibe zu jeder Signatur den Java-Methodenkopf. | **\[3 BE\]** |

| **Stufe** | **Abi-Signatur (aus dem Gerüst)**                                                      | **Java-Methodenkopf** |
|-----------|----------------------------------------------------------------------------------------|-----------------------|
| ★★        | manaKosten(stufe: Ganzzahl, verstaerkt: Wahrheitswert): Ganzzahl                       |                       |
| ★★        | kannZaubern(mana: Ganzzahl, stufe: Ganzzahl, verstaerkt: Wahrheitswert): Wahrheitswert |                       |
| ★★        | max3(a: Ganzzahl, b: Ganzzahl, c: Ganzzahl): Ganzzahl                                  |                       |
| ★★★       | runden(wert: Kommazahl): Ganzzahl                                                      |                       |
| ★★★       | wuerfelImBereich(von: Ganzzahl, bis: Ganzzahl): Ganzzahl                               |                       |
| ★★★       | zauberkette(stufe: Ganzzahl): Zeichenkette                                             |                       |

|        |                                                                                                                                                                                                   |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **b)** | **Basis in der IDE:** Implementiere heilwert, istStaerker, spruchtext und die Hilfsmethode max2 (Köpfe vorgegeben). Starte die Testklasse L04ZauberTest: Alle Tests mit basis\_ müssen grün sein. |

|        |                                                                                                                                                                                                                                                                                  |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **c)** | **Erweiterung:** Tippe deine Köpfe aus a) ab und schreibe die Rümpfe. kannZaubern muss manaKosten **aufrufen**, max3 muss max2 **aufrufen**. Dann schaltest du frei – in **zwei** Blöcken (in L04ZauberTest und im Hauptprogramm). Lösche jeweils genau die beiden Markerzeilen: |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>/* LEVEL-0.4-START Erweiterung &lt;- diese ganze Zeile löschen</p>
<p>@Test</p>
<p>public void erweiterung_manaKosten() {</p>
<p>...</p>
<p>}</p>
<p>...</p>
<p>LEVEL-0.4-ENDE Erweiterung */ &lt;- diese ganze Zeile löschen</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                                                                       |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **d)** | **Experte:** genauso mit den Markern LEVEL-0.4-START Experte und LEVEL-0.4-ENDE Experte. Runden und Zufallszahl kennst du aus AB 2, Infoteil 3 – Math.round ist tabu. |

**Checkliste zum Freischalten**

☐ Alle drei Methoden der Stufe haben einen Kopf (Name, Parametertypen, Rückgabetyp wie in der Signatur).

☐ Beide Blöcke der Stufe freigeschaltet: in L04ZauberTest **und** im Hauptprogramm – je zwei Markerzeilen gelöscht, sonst nichts.

☐ Meldet der Compiler „Methode nicht gefunden“ o. Ä.: Kopf mit der Signatur vergleichen – **niemals** den Test ändern.

☐ Code-Review in der Gilde: Ruft kannZaubern wirklich manaKosten auf, max3 wirklich max2? (Das kann kein Test prüfen.)

| **Stufe**      | **Methoden in Zauber**                                                       | **Tests beginnen mit** | **XP**  |
|----------------|------------------------------------------------------------------------------|------------------------|---------|
| ★ Basis        | heilwert, istStaerker, spruchtext, max2 (Köpfe vorgegeben)                   | basis\_                | **+10** |
| ★★ Erweiterung | manaKosten, kannZaubern, max3 (Köpfe selbst schreiben, freischalten)         | erweiterung\_          | **+20** |
| ★★★ Experte    | runden, wuerfelImBereich, zauberkette (Köpfe selbst schreiben, freischalten) | experte\_              | **+30** |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Für Schnelle (Teil 1): Zauberformeln, die Zauberformeln rufen</strong></p>
<ul>
<li><p><strong>Echte römische Zahlen:</strong> Erweitere die Runen aus Aufgabe 6 um L (50), C (100), D (500), M (1000) und um die Subtraktionsregel: Steht ein kleinerer Wert vor einem größeren, wird er abgezogen („XIV“ = 14, „MCMXCIV“ = 1994).</p></li>
<li><p><strong>kgV:</strong> kgV(a: Ganzzahl, b: Ganzzahl): Ganzzahl mit Werkstatt.ggT – es gilt kgV(a, b) = a / ggT(a, b) * b.</p></li>
<li><p><strong>Kalender der Akademie:</strong> istSchaltjahr(jahr: Ganzzahl): Wahrheitswert (durch 4 teilbar, aber nicht durch 100 – außer durch 400) und tageImMonat(monat: Ganzzahl, jahr: Ganzzahl): Ganzzahl, die istSchaltjahr aufruft.</p></li>
</ul>
<p>Side-Quest: <strong>+15 bis +40 XP</strong> je nach Umfang.</p></td>
</tr>
</tbody>
</table>

**Teil 2 – Zaubern mit Reihungen: Wert und Referenz (DS 5)**

Bisher hatten deine Zauberformeln einfache Zutaten: Zahlen, Zeichen, Zeichenketten. Jetzt bekommen sie ganze **Reihungen** – und liefern Reihungen zurück. Dabei passiert etwas Überraschendes: Manche Änderungen in der Methode sind danach im Hauptprogramm sichtbar, andere nicht.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 7: Wertübergabe – aber was ist der Wert?</strong></p>
<p>Java übergibt beim Aufruf immer eine <strong>Kopie des Werts</strong> der Argumentvariablen. Entscheidend ist, <strong>was</strong> in der Variablen steht:</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Fall 1: Ganzzahl-Parameter</strong></p>
<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static void verdoppleZahl(int n) {</p>
<p>n = n * 2;</p>
<p>}</p>
<p>// Hauptprogramm</p>
<p>int x = 5;</p>
<p>verdoppleZahl(x);</p>
<p>println(x); // 5</p></td>
</tr>
</tbody>
</table></td>
<td><p><img src="media/3c20bf2677aef82d7578bdc0714b757b7106869f.png" title="p4_wert.png" style="width:2.98958in;height:1.3125in" alt="p4_wert.png" /></p>
<p><strong>Keine Wirkung nach außen:</strong> n ist eine Kopie der Zahl 5. n wird 10, x bleibt 5.</p></td>
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
<td><p><strong>Fall 2: Reihungs-Parameter, Inhalt ändern</strong></p>
<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static void fuelleNull(int[] r) {</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>r[i] = 0;</p>
<p>}</p>
<p>}</p>
<p>// Hauptprogramm</p>
<p>int[] t = {4, 8, 6};</p>
<p>fuelleNull(t);</p>
<p>println(t[0]); // 0</p></td>
</tr>
</tbody>
</table></td>
<td><p><img src="media/eefa5e1de46e5c4703f91f18721394518e6074a8.png" title="p4_ref.png" style="width:2.98958in;height:1.41667in" alt="p4_ref.png" /></p>
<p><strong>Wirkung nach außen:</strong> r ist eine Kopie der <strong>Referenz</strong>. Beide Pfeile zeigen auf dieselbe Reihung – was über r geändert wird, sieht auch t.</p></td>
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
<td><p><strong>Fall 3: Reihungs-Parameter neu belegen</strong></p>
<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static void ersetze(int[] r) {</p>
<p>r = new int[r.length];</p>
<p>}</p>
<p>// Hauptprogramm</p>
<p>int[] t = {4, 8, 6};</p>
<p>ersetze(t);</p>
<p>println(t[0]); // 4</p></td>
</tr>
</tbody>
</table></td>
<td><p><img src="media/a012c299cd45eb70417174e857a35b24434d491b.png" title="p4_neu.png" style="width:2.98958in;height:1.41667in" alt="p4_neu.png" /></p>
<p><strong>Keine Wirkung nach außen:</strong> Nur der lokale Pfeil r wird auf eine neue Reihung umgelenkt. t zeigt weiter auf die alte.</p></td>
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
<td><p><strong>Merke: Wert und Referenz</strong></p>
<ul>
<li><p>Einen Parameter neu zu belegen (n = …, r = new …) wirkt <strong>nie</strong> nach außen.</p></li>
<li><p>Den <strong>Inhalt</strong> einer übergebenen Reihung zu ändern (r[i] = …) wirkt <strong>immer</strong> nach außen.</p></li>
<li><p>Soll eine Methode „eine neue Reihung liefern“, muss sie mit new eine anlegen und zurückgeben – sonst verändert sie das Original.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Aufgabe 8: Original oder Kopie?** **PAPIER** ★★ **+5 XP**

Vier Zauberformeln und ein Hauptprogramm. Überlege zuerst ohne Gerät!

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static void tausche(int a, int b) {</p>
<p>2 int h = a;</p>
<p>3 a = b;</p>
<p>4 b = h;</p>
<p>5 }</p>
<p>6 public static void tauscheInReihung(int[] r, int i, int j) {</p>
<p>7 int h = r[i];</p>
<p>8 r[i] = r[j];</p>
<p>9 r[j] = h;</p>
<p>10 }</p>
<p>11 public static int[] mitNull(int[] r) {</p>
<p>12 r[0] = 0;</p>
<p>13 return r;</p>
<p>14 }</p>
<p>15 public static void neuBelegen(int[] r) {</p>
<p>16 r = new int[3];</p>
<p>17 r[1] = 1;</p>
<p>18 }</p>
<p>19 // Hauptprogramm</p>
<p>20 int x = 1;</p>
<p>21 int y = 2;</p>
<p>22 int[] z = {3, 4, 5};</p>
<p>23 tausche(x, y);</p>
<p>24 tauscheInReihung(z, 0, 2);</p>
<p>25 int[] w = mitNull(z);</p>
<p>26 neuBelegen(w);</p>
<p>27 w[2] = 9;</p>
<p>28 println(x + " " + y);</p>
<p>29 println(z[0] + " " + z[1] + " " + z[2]);</p>
<p>30 println(w[0] + " " + w[1] + " " + w[2]);</p>
<p>31 println(z == w);</p></td>
</tr>
</tbody>
</table>

|        |                                |              |
|--------|--------------------------------|--------------|
| **a)** | Gib die vier Ausgabezeilen an. | **\[4 BE\]** |

| **Ausgabe 1** | **Ausgabe 2** | **Ausgabe 3** | **Ausgabe 4** |
|---------------|---------------|---------------|---------------|
|               |               |               |               |

|        |                                                                                                             |              |
|--------|-------------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Zeichne das Speicherbild (1) direkt nach Zeile 25 und (2) während neuBelegen kurz vor dem Ende der Methode. | **\[3 BE\]** |

<img src="media/7e19c3e3ed8ca9cbdd84b5f72c30f298eeca92a5.png" title="grid_17_6.png" style="width:6.69792in;height:2.36458in" alt="grid_17_6.png" />

|        |                                                                                      |              |
|--------|--------------------------------------------------------------------------------------|--------------|
| **c)** | Begründe für jede der vier Methoden, ob ihre Änderung im Hauptprogramm sichtbar ist. | **\[4 BE\]** |

|     |
|-----|
|     |
|     |
|     |
|     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 8: In der Reihung arbeiten oder neue Reihung liefern?</strong></p>
<p>Abituraufgaben sagen genau, was gewünscht ist. Achte auf die Formulierung – sie entscheidet über den Rückgabetyp:</p>
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 39%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><strong>in-place: die Reihung verändern</strong></th>
<th><strong>neue Reihung liefern</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>typische Formulierung</td>
<td>„… verändert r“, „setzt alle …“, „sortiert r“</td>
<td>„… liefert eine neue Reihung …“, „r bleibt unverändert“</td>
</tr>
<tr class="even">
<td>Rückgabetyp</td>
<td>nichts (void)</td>
<td>Reihung von … (int[])</td>
</tr>
<tr class="odd">
<td>Muster</td>
<td>r[i] = … in einer Zählschleife</td>
<td>int[] neu = new int[…]; füllen, return neu;</td>
</tr>
<tr class="even">
<td>Beispiel</td>
<td>halbiereAlle({9, 4, 7}) → r wird {4, 2, 3}</td>
<td>halbiert({9, 4, 7}) liefert {4, 2, 3}, r bleibt {9, 4, 7}</td>
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
<td><p>public static void halbiereAlle(int[] r) {</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>r[i] = r[i] / 2;</p>
<p>}</p>
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
<td><p>public static int[] halbiert(int[] r) {</p>
<p>int[] neu = new int[r.length];</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>neu[i] = r[i] / 2;</p>
<p>}</p>
<p>return neu;</p>
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

**Aufgabe 9: In der Reihung oder neu?** **PAPIER** ★★ **+5 XP**

|        |                                                                                                                               |              |
|--------|-------------------------------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Gib zu jeder Beschreibung die Abi-Signatur an und kreuze an, ob die Methode in-place arbeitet oder eine neue Reihung liefert. | **\[4 BE\]** |

| **Nr.** | **Beschreibung**                                                                                           | **Abi-Signatur** | **in-place / neu** |
|---------|------------------------------------------------------------------------------------------------------------|------------------|--------------------|
| 1       | **sortiere** ordnet die Werte der Reihung r aufsteigend.                                                   |                  | ☐ in-place ☐ neu   |
| 2       | **gespiegelt** liefert eine Reihung mit den Werten von r in umgekehrter Reihenfolge; r bleibt unverändert. |                  | ☐ in-place ☐ neu   |
| 3       | **nullStattNegativ** setzt alle negativen Werte in r auf 0.                                                |                  | ☐ in-place ☐ neu   |
| 4       | **positionenVon** liefert alle Indizes, an denen x in r vorkommt.                                          |                  | ☐ in-place ☐ neu   |

|        |                                                                                                                                                                                                                                                      |              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Implementiere nullStattNegativ aus a) und die Methode begrenzt(r: Reihung von Ganzzahl, max: Ganzzahl): Reihung von Ganzzahl. Sie liefert eine neue Reihung, in der jeder Wert, der größer als max ist, durch max ersetzt ist; r bleibt unverändert. | **\[4 BE\]** |

<img src="media/5d5c9121bf8d67eb31ea7e0bd3355c363ba88d86.png" title="grid_17_9.png" style="width:6.69792in;height:3.54167in" alt="grid_17_9.png" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 9: Hilfsmethoden – große Zauber aus kleinen</strong></p>
<p>Eine <strong>Hilfsmethode</strong> löst ein Teilproblem, das sonst die Hauptmethode unübersichtlich machen würde. Im Abitur steht oft dabei: „Die Methode … darf verwendet werden.“ – dann <strong>sollst</strong> du sie aufrufen.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static boolean istVokal(char c) {</p>
<p>return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'</p>
<p>|| c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';</p>
<p>}</p>
<p>public static int anzahlVokale(String s) {</p>
<p>int anzahl = 0;</p>
<p>for (int i = 0; i &lt; s.length(); i++) {</p>
<p>if (istVokal(s.charAt(i))) { // Teilproblem ausgelagert</p>
<p>anzahl++;</p>
<p>}</p>
<p>}</p>
<p>return anzahl;</p>
<p>}</p></td>
</tr>
</tbody>
</table>
<ul>
<li><p><strong>Zerlegen:</strong> Welches Teilproblem kommt mehrfach vor oder lässt sich in einem Satz beschreiben? → eigene Methode mit eigener Signatur.</p></li>
<li><p><strong>Vorteile:</strong> kürzerer, lesbarer Code; jede Methode einzeln testbar; Fehler nur an einer Stelle zu korrigieren; Wiederverwendung.</p></li>
<li><p><strong>Standardbausteine als Methoden:</strong> Summe, Zählen, Maximum mit Index, lineare Suche, neue Reihung füllen – in Welt 2 werden sie zum Werkzeugkasten.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Aufgabe 10: Das vokalreichste Zauberwort** **PAPIER** ★★★ **+5 XP**

**Auftrag:** Die Methode bestesWort(woerter: Reihung von Zeichenkette): Zeichenkette liefert das Wort mit den meisten Vokalen. Bei Gleichstand wird das erste dieser Wörter geliefert, für eine leere Reihung die leere Zeichenkette "". Die Methode anzahlVokale aus Infoteil 9 darf verwendet werden.

|        |                                   |              |
|--------|-----------------------------------|--------------|
| **a)** | Implementiere bestesWort in Java. | **\[4 BE\]** |

<img src="media/e4f8ffd0755f42868bd938f3fd23b0a1a8b4b6ae.png" title="grid_17_7.png" style="width:6.69792in;height:2.76042in" alt="grid_17_7.png" />

|        |                                                                                        |              |
|--------|----------------------------------------------------------------------------------------|--------------|
| **b)** | Gib an, was bestesWort für {"Eis", "Feuer", "Erde"} und für {"Wind", "Blitz"} liefert. | **\[1 BE\]** |

|     |
|-----|
|     |

|        |                                                                                           |              |
|--------|-------------------------------------------------------------------------------------------|--------------|
| **c)** | Gib an, wie oft istVokal beim Aufruf anzahlVokale("Feuer") aufgerufen wird, und begründe. | **\[1 BE\]** |

|     |
|-----|
|     |

**Aufgabe 11: Level 0.5 – Die Zauberschule, Teil II** **IDE** ★ – ★★★ **bis +60 XP**

|        |                                                                                    |
|--------|------------------------------------------------------------------------------------|
| **a)** | Arbeite in der Klasse **ZauberII** (Köpfe vorgegeben), Testklasse L05ZauberIITest. |

<table>
<colgroup>
<col style="width: 15%" />
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
<td><p>fuelle(r: Reihung von Ganzzahl, wert: Ganzzahl): nichts</p>
<p>erhoeheAlle(r: Reihung von Ganzzahl, bonus: Ganzzahl): nichts</p>
<p>erhoehteKopie(r: Reihung von Ganzzahl, bonus: Ganzzahl): Reihung von Ganzzahl</p></td>
<td>basis_</td>
<td><strong>+10</strong></td>
</tr>
<tr class="even">
<td>★★ Erweiterung</td>
<td><p>istImBereich(x: Ganzzahl, von: Ganzzahl, bis: Ganzzahl): Wahrheitswert</p>
<p>zaehleImBereich(r: Reihung von Ganzzahl, von: Ganzzahl, bis: Ganzzahl): Ganzzahl</p>
<p>indexDesMinimums(r: Reihung von Ganzzahl): Ganzzahl</p>
<p>tauscheErstesUndLetztes(r: Reihung von Ganzzahl): nichts</p></td>
<td>erweiterung_</td>
<td><strong>+20</strong></td>
</tr>
<tr class="odd">
<td>★★★ Experte</td>
<td><p>zweitgroesster(r: Reihung von Ganzzahl): Ganzzahl</p>
<p>verschmelze(a: Reihung von Ganzzahl, b: Reihung von Ganzzahl): Reihung von Ganzzahl</p></td>
<td>experte_</td>
<td><strong>+30</strong></td>
</tr>
</tbody>
</table>

- Bei erhoehteKopie prüfen die Tests **beides**: das Ergebnis **und** dass r unverändert ist.

- zaehleImBereich soll die Hilfsmethode istImBereich aufrufen (Code-Review in der Gilde).

- verschmelze arbeitet nach dem Reißverschluss-Prinzip: immer das kleinere der beiden vorderen Elemente nehmen, am Ende den Rest anhängen. Das ist der Kern von Mergesort (Welt 3).

|        |                                                                                                                                                                                                                                                         |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **b)** | **Vorhersage ohne Gerät:** Das Hauptprogramm ruft mit staerken = {12, 3, 25, 3, 18} nacheinander zaehleImBereich(staerken, 10, 20), indexDesMinimums(staerken) und zweitgroesster(staerken) auf. Notiere die drei Ausgaben, starte dann und vergleiche. |

|     |
|-----|
|     |

**Aufgabe 12: Bug-Hunt in der Zauberschule** **PAPIER** ★★ **+5 XP**

In jeder Methode steckt **genau ein** Fehler.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>// A: soll die größere der beiden Zahlen liefern</p>
<p>public static void max(int a, int b) {</p>
<p>if (a &gt; b) {</p>
<p>return a;</p>
<p>}</p>
<p>return b;</p>
<p>}</p>
<p>// B: soll eine neue Reihung ohne das erste Element liefern (r ist nicht leer)</p>
<p>public static int[] ohneErstes(int[] r) {</p>
<p>int[] neu = new int[r.length - 1];</p>
<p>for (int i = 0; i &lt; neu.length; i++) {</p>
<p>neu[i] = r[i];</p>
<p>}</p>
<p>return neu;</p>
<p>}</p>
<p>// C: soll zählen, wie viele Werte größer als grenze sind</p>
<p>public static int zaehleUeber(int[] r, int grenze) {</p>
<p>int anzahl = 0;</p>
<p>grenze = 0;</p>
<p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>if (r[i] &gt; grenze) {</p>
<p>anzahl++;</p>
<p>}</p>
<p>}</p>
<p>return anzahl;</p>
<p>}</p>
<p>// D: soll prüfen, ob das Gold für anzahl Tränke zum Preis preis reicht</p>
<p>public static int gesamtpreis(int preis, int anzahl) {</p>
<p>return preis * anzahl;</p>
<p>}</p>
<p>public static boolean kannKaufen(int gold, int preis, int anzahl) {</p>
<p>return gesamtpreis(anzahl, gold) &lt;= gold;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

|        |                                                                          |              |
|--------|--------------------------------------------------------------------------|--------------|
| **a)** | Beschreibe für jede Methode den Fehler und gib die korrigierte Zeile an. | **\[4 BE\]** |

| **Methode** | **Fehler** | **korrigierte Zeile** |
|-------------|------------|-----------------------|
| A           |            |                       |
| B           |            |                       |
| C           |            |                       |
| D           |            |                       |

|        |                                                                                                                                     |              |
|--------|-------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **b)** | Gib für B, C und D je einen Aufruf mit dem falschen und dem richtigen Ergebnis an. Welcher Fehler wird schon vom Compiler gemeldet? | **\[3 BE\]** |

|     |
|-----|
|     |
|     |
|     |
|     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Für Schnelle (Teil 2): Meisterzauber</strong></p>
<ul>
<li><p><strong>Rotation:</strong> rotiereLinks(r: Reihung von Ganzzahl, k: Ganzzahl): nichts schiebt alle Werte k Stellen nach links (vorne Herausfallende kommen hinten wieder herein): {1, 2, 3, 4, 5} mit k = 2 wird {3, 4, 5, 1, 2}. Zerlege: Schreibe zuerst rotiereEinmal(r).</p></li>
<li><p><strong>Anagramm:</strong> istAnagramm(s: Zeichenkette, t: Zeichenkette): Wahrheitswert – gleiche Buchstaben in anderer Reihenfolge („lager“ und „regal“). Nutze Vorrat.zaehleZeichen aus Level 0.3.</p></li>
<li><p><strong>Spur des Reißverschlusses:</strong> Verfolge verschmelze({1, 4, 9}, {2, 3, 10}) in einer Tracetabelle mit den Spalten i, j, k und neu. Wann endet die erste Schleife – und wer liefert den Rest?</p></li>
</ul>
<p>Side-Quest: <strong>+15 bis +40 XP</strong> je nach Umfang.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Abi-Check für Methoden – vor jeder Abgabe</strong></p>
<p>☐ Kopf exakt nach Signatur: Name, Reihenfolge und Typen der Parameter, Rückgabetyp („nichts“ = void).</p>
<p>☐ Jeder mögliche Ablauf endet mit einem return passenden Typs; nichts steht hinter einem return.</p>
<p>☐ Parameter werden benutzt, nicht mit festen Werten überschrieben.</p>
<p>☐ „neue Reihung“ verlangt? → new und das Original nur lesen. „verändert r“ verlangt? → r[i] = …, kein new.</p>
<p>☐ Darf eine Hilfsmethode verwendet werden, rufst du sie auf – mit Argumenten in der richtigen Reihenfolge.</p></td>
</tr>
</tbody>
</table>
