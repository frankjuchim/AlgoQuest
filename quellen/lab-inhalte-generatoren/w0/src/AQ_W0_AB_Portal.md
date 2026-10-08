<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>WELT 0 · DOPPELSTUNDE 1 · KICK-OFF · TEIL B: NOTATIONS-REFERENZ FÜR DS 2</strong></p>
<p><strong>W0·1 – Das Portal: Start ins Dungeon und Notation fürs Abitur</strong></p>
<p>Level 0 „Diagnose“: bis zu <strong>+60 XP</strong> · Papier-Aufgaben: je <strong>+5 XP</strong> · Datei: AQ_W0_L0_Diagnose_Geruest.txt</p></td>
</tr>
</tbody>
</table>

Willkommen im Game-Studio! In den nächsten 14 Wochen baut euer Kurs ein Dungeon-Spiel – und dabei genau die Algorithmen und Datenstrukturen, die im Abitur drankommen: Suchen und Sortieren, Rekursion, Stapel, Schlangen und Bäume. Sieben Welten liegen vor euch, am Ende jeder Welt wartet ein Boss-Kampf.

Doch bevor euer Studio Helden schmieden darf, durchläuft es die **Akademie der Baumeister** – und zuerst steht ihr vor ihrem **Portal**. Es lässt nur Gilden durch, die ihr Werkzeug beherrschen: die **Online-IDE** zum Programmieren und Testen – und **Papier und Stift**. Denn im Abitur gibt es keinen Compiler. Java-Methoden, Struktogramme und Tracetabellen schreibst du dort von Hand. Darum trainieren wir beides vom ersten Tag an.

**Teil A – Start: Gilde, Werkzeug, Diagnose**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil: So funktioniert Algo Quest</strong></p>
<ul>
<li><p>Ihr arbeitet in <strong>Gilden</strong> mit 3–4 Personen. Die Gilde bleibt für die ganze Einheit gleich.</p></li>
<li><p>Für erledigte Aufgaben gibt es <strong>XP</strong> (Erfahrungspunkte). Mit genug XP steigst du im <strong>Rang</strong> auf: Novize → Lehrling → Geselle → Meister → Großmeister („abiturbereit“).</p></li>
<li><p><strong>XP zählen nicht für die Note.</strong> Öffentlich ist nur die Gilden-Rangliste. Deine eigenen XP siehst nur du.</p></li>
<li><p>Jede Aufgabe ist gekennzeichnet: [IDE] = am Gerät, [PAPIER] = ohne Gerät, nur mit Stift. Die Sterne zeigen die Stufe: ★ Basis, ★★ Erweiterung, ★★★ Experte.</p></li>
<li><p>Jede Doppelstunde hat denselben Rhythmus: 10 min Papier-Kata (ohne Gerät) · 15 min Input · 50 min Level in der Online-IDE · 15 min Sicherung.</p></li>
</ul></td>
</tr>
</tbody>
</table>

| **Wofür?**                                                          | **XP**                       | **Wofür?**                                       | **XP**      |
|---------------------------------------------------------------------|------------------------------|--------------------------------------------------|-------------|
| IDE-Level Basis / Erweiterung / Experte                             | **10 / 20 / 30**             | Boss-Kampf (Test am Ende einer Welt)             | **2 je BE** |
| Papier-Kata korrekt gelöst                                          | **5**                        | Side-Quest (Zusatzauftrag)                       | **15–40**   |
| Papier-Compiler: Handschrift unverändert abgetippt, alle Tests grün | **30** (+10 beim 1. Versuch) | Mentor: jemandem etwas erklärt (nicht vorgesagt) | **10**      |
|                                                                     |                              | Bug-Bounty: Fehler im Material gefunden          | **15**      |

**Aufgabe 1: Die Gilde wird gegründet** **PAPIER** ★

|        |                                                                                                                                                                       |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **a)** | Setzt euch in eurer Gilde zusammen (Einteilung durch die Lehrkraft). Einigt euch auf einen **Gildennamen** – passend zum Dungeon, ohne Klarnamen, ohne Beleidigungen. |

|        |                                                                                                                                                                                       |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **b)** | Jede Person wählt ein **Pseudonym** (Spielername). Es darf keinen Rückschluss auf deinen echten Namen zulassen. Gebt Gildenname und Pseudonyme auf einem Zettel bei der Lehrkraft ab. |

|        |                                                                                                                         |
|--------|-------------------------------------------------------------------------------------------------------------------------|
| **c)** | Lest die Gilden-Regeln im Kasten. Formuliert gemeinsam **eine zusätzliche Regel** für eure Gilde und notiert sie unten. |

|                         |     |
|-------------------------|-----|
| **Gildenname:**         |     |
| **Mein Pseudonym:**     |     |
| **Unsere Zusatzregel:** |     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Gilden-Regeln</strong></p>
<p><strong>1.</strong> Ihr helft euch gegenseitig – aber jede Person schreibt <strong>ihren eigenen</strong> Code und <strong>ihre eigenen</strong> Papier-Lösungen.</p>
<p><strong>2.</strong> Wer erklärt statt vorsagt, bekommt Mentor-XP.</p>
<p><strong>3.</strong> Tests in der IDE werden nie verändert. Wer glaubt, dass ein Test falsch ist, meldet ihn (Bug-Bounty).</p>
<p><strong>4.</strong> XP zählen nicht für die Note. Fair spielen lohnt sich trotzdem: Die Gilden-Rangliste hängt am Beamer.</p>
<p><strong>5.</strong> Pseudonym und PIN gehören nur dir. Die PIN schreibst du nirgends auf dieses Blatt.</p></td>
</tr>
</tbody>
</table>

**Aufgabe 2: Das Portal öffnet sich** **IDE** ★

|        |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **a)** | **Login in die Algo-Quest-WebApp.** Von der Lehrkraft bekommst du einen Zugangszettel mit **Kurscode** und **PIN**. Öffne die Adresse der WebApp: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ und melde dich mit Kurscode, deinem Pseudonym und deiner PIN an. Unter „Mein Stand“ siehst du deine XP und deinen Rang, unter „Gilde“ eure Gildensumme. Die XP bucht die Lehrkraft – zeig ihr deine grünen Tests. |

|        |                                                                                                                                                                                                                                                                                           |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **b)** | **Online-IDE einrichten.** Öffne online-ide.de und melde dich mit deinen Zugangsdaten an. Lege einen neuen Workspace **AlgoQuest_W0** an (oder öffne den Workspace, den die Lehrkraft verteilt hat). Erstelle darin eine Datei und füge den Inhalt von AQ_W0_L0_Diagnose_Geruest.txt ein. |

|        |                                                                                                                                                                                                                                                                                |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **c)** | **Testrunner ausprobieren.** Öffne den Reiter **„Testrunner“** und starte die Testklasse DiagnoseBasisTest mit dem grünen Dreieckspfeil. Notiere: Wie viele Tests sind rot, wie viele schon grün? Warum sind manche Tests schon grün, obwohl du noch nichts programmiert hast? |

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
<td><p><strong>Ausblick: Bibliothek „niedersachsen“</strong></p>
<p>Ab Welt 4 brauchst du die Klassen Stack, Queue, DynArray und BinTree aus dem Abitur. Sie stecken in der Bibliothek <strong>„niedersachsen“</strong>, die man pro Workspace einschaltet (Rechtsklick auf den Workspace → Einstellungen). <strong>Jetzt noch nicht nötig.</strong></p>
<p><strong>Vermerk: Lehrkraft prüft den Menüpfad vor dem Einsatz.</strong></p></td>
</tr>
</tbody>
</table>

**Aufgabe 3: Level 0 – Die Diagnose** **IDE** ★ – ★★★ **bis +60 XP**

Das Portal prüft, was du aus der Einführungsphase noch kannst: Reihungen, Schleifen, Verzweigungen und Zeichenketten. Keine Panik – das ist eine Diagnose, keine Klassenarbeit. Jeder grüne Test zeigt dir, was schon sitzt. Du arbeitest nur in der Klasse Diagnose im Abschnitt „DEIN TEIL“.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 55%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Stufe</strong></th>
<th><strong>Testklasse</strong></th>
<th><strong>Methoden (Signatur wie im Abitur)</strong></th>
<th><strong>XP</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>★ Basis</td>
<td>DiagnoseBasisTest</td>
<td><p>summe(r: Reihung von Ganzzahl): Ganzzahl</p>
<p>maximum(r: Reihung von Ganzzahl): Ganzzahl (r ist nicht leer)</p>
<p>zaehle(r: Reihung von Ganzzahl, x: Ganzzahl): Ganzzahl</p></td>
<td><strong>+10</strong></td>
</tr>
<tr class="even">
<td>★★ Erweiterung</td>
<td>DiagnoseErweiterungTest</td>
<td><p>indexVon(r: Reihung von Ganzzahl, x: Ganzzahl): Ganzzahl (erstes Vorkommen, sonst −1)</p>
<p>istAufsteigendSortiert(r: Reihung von Ganzzahl): Wahrheitswert</p>
<p>durchschnitt(r: Reihung von Ganzzahl): Kommazahl (leere Reihung → 0.0)</p></td>
<td><strong>+20</strong></td>
</tr>
<tr class="odd">
<td>★★★ Experte</td>
<td>DiagnoseExperteTest</td>
<td><p>anzahlVokale(s: Zeichenkette): Ganzzahl (a, e, i, o, u – klein und groß)</p>
<p>istPalindrom(s: Zeichenkette): Wahrheitswert (exakter Zeichenvergleich)</p></td>
<td><strong>+30</strong></td>
</tr>
</tbody>
</table>

|        |                                                                                                                 |
|--------|-----------------------------------------------------------------------------------------------------------------|
| **a)** | Arbeite die Stufen der Reihe nach ab. Eine Stufe ist geschafft, wenn **alle** Tests ihrer Testklasse grün sind. |

|        |                                                                                                                                                                                                                        |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **b)** | Lies bei roten Tests die Meldung – sie verrät dir, welcher Fall noch nicht klappt. Trage zwei Fehler, die du gemacht hast, in dein **Fehlerlogbuch** ein (Tabelle unten; im Heft auf den letzten Seiten weiterführen). |

|        |                                                                                                                                                                                         |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **c)** | Halte dich an die Spielregeln des Abiturs: Zeichenketten nur mit den erlaubten Operationen bearbeiten (Teil B) – also **kein** toLowerCase. Reihungen laufen von Index 0 bis Länge − 1. |

**Tipp:** Mit dem grünen Startknopf läuft das Hauptprogramm ganz unten in der Datei. Dort kannst du deine Methoden mit eigenen Werten ausprobieren.

**Mein Fehlerlogbuch**

| **Nr.** | **Was war falsch?** | **Warum? (Ursache)** | **So vermeide ich es** |
|---------|---------------------|----------------------|------------------------|
| 1       |                     |                      |                        |
| 2       |                     |                      |                        |
| 3       |                     |                      |                        |

**Teil B – Notation fürs Abitur (Referenz für DS 2)**

Im Abitur gibt es keinen Compiler und keinen Testrunner. Wer die Notation aus den Ergänzenden Hinweisen (EH 2025) sicher beherrscht, verschenkt keine BE. Die folgenden Infoteile gibt es auch als laminierte Werkzeugkarten.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 1: Signaturen und Typnamen</strong></p>
<p>Methoden werden im Abitur sprachunabhängig angegeben: <strong>name(parameter: Typ, …): Rückgabetyp</strong></p>
<p>Beispiel: zaehle(r: Reihung von Ganzzahl, x: Ganzzahl): Ganzzahl ⟷ public static int zaehle(int[] r, int x)</p>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 34%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Typname im Abitur</strong></th>
<th><strong>Java</strong></th>
<th><strong>Typname im Abitur</strong></th>
<th><strong>Java</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Ganzzahl</td>
<td>int</td>
<td>nichts (keine Rückgabe)</td>
<td>void</td>
</tr>
<tr class="even">
<td>Kommazahl</td>
<td>double</td>
<td>Reihung von Ganzzahl</td>
<td>int[]</td>
</tr>
<tr class="odd">
<td>Wahrheitswert</td>
<td>boolean</td>
<td>Reihung von Gegenstand</td>
<td>Gegenstand[]</td>
</tr>
<tr class="even">
<td>Zeichen</td>
<td>char</td>
<td>Klassenname, z. B. Held</td>
<td>Held</td>
</tr>
<tr class="odd">
<td>Zeichenkette</td>
<td>String</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<ul>
<li><p>Es heißt immer <strong>Reihung</strong>, nie „Array“. Der Index beginnt bei 0 und endet bei Länge − 1. Bei 2D-Reihungen: r[zeile][spalte].</p></li>
<li><p>Die Länge einer Reihung auslesen (r.length) ist erlaubt, die for-each-Schleife auch.</p></li>
<li><p>/ rechnet bei Ganzzahlen ganzzahlig: 7 / 2 = 3. % liefert den Rest: 7 % 2 = 1.</p></li>
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
<td><p><strong>Infoteil 2: Struktogramm-Elemente (EH § 5)</strong></p>
<p>Struktogramme sind sprachunabhängig. Zuweisungen schreibst du mit <strong>←</strong>, Vergleiche mit =, ≠, &lt;, ≤, &gt;, ≥. Bedingungen verknüpfst du mit <strong>und</strong>, <strong>oder</strong>, <strong>nicht</strong>.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 39%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Element</strong></th>
<th><strong>Struktogramm-Notation</strong></th>
<th><strong>Java</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Kopf</strong> mit Signatur</td>
<td><img src="media/18752e28a612f41320e8554f23ba013824e0171b.png" title="el_kopf.png" style="width:2.32292in;height:0.5in" alt="el_kopf.png" /></td>
<td><p>public static int summe(int[] r) {</p>
<p>...</p>
<p>}</p></td>
</tr>
<tr class="even">
<td><strong>Zuweisung</strong></td>
<td><img src="media/8af05c85f02275b68a93941065196cabdf3f14fb.png" title="el_zuweisung.png" style="width:2.32292in;height:0.26042in" alt="el_zuweisung.png" /></td>
<td>anzahl = anzahl + 1;</td>
</tr>
<tr class="odd">
<td><strong>Objekt erzeugen</strong> (ruft den Konstruktor auf)</td>
<td><img src="media/6b989ffeb0978e24f721b31f144d65668582ade1.png" title="el_erzeuge.png" style="width:2.32292in;height:0.26042in" alt="el_erzeuge.png" /></td>
<td>Held h = new Held("Aria");</td>
</tr>
<tr class="even">
<td><strong>Methodenaufruf</strong></td>
<td><img src="media/a159ca82a8465726336de4307ce8e22f61c73071.png" title="el_aufruf.png" style="width:2.32292in;height:0.26042in" alt="el_aufruf.png" /></td>
<td>h.nimmSchaden(30);</td>
</tr>
<tr class="odd">
<td><strong>Rückgabe</strong> – beendet die Methode sofort</td>
<td><img src="media/67c261a0579cbb08dbdb20fccf4512ba2d9855d5.png" title="el_rueckgabe.png" style="width:2.32292in;height:0.26042in" alt="el_rueckgabe.png" /></td>
<td>return summe;</td>
</tr>
<tr class="even">
<td><strong>Verzweigung</strong> (Dreieck-Kopf mit Bedingung, links wahr, rechts falsch)</td>
<td><img src="media/692b15fb6aa33e3934d4a93abdea4b23c7a12ae1.png" title="el_verzweigung.png" style="width:2.32292in;height:0.71875in" alt="el_verzweigung.png" /></td>
<td><p>if (r[i] &gt; max) {</p>
<p>max = r[i];</p>
<p>}</p></td>
</tr>
<tr class="odd">
<td><strong>Solange-Schleife</strong> (kopfgesteuert)</td>
<td><img src="media/b2f5ebd18493ccd81cd131ef394bcc51c6830753.png" title="el_solange.png" style="width:2.32292in;height:0.47917in" alt="el_solange.png" /></td>
<td><p>while (summe &lt; ziel) {</p>
<p>...</p>
<p>}</p></td>
</tr>
<tr class="even">
<td><strong>Zählschleife</strong> – „bis“ ist einschließlich!</td>
<td><img src="media/68e457059d90e09693222669962af2122454c671.png" title="el_zaehl.png" style="width:2.32292in;height:0.47917in" alt="el_zaehl.png" /></td>
<td><p>for (int i = 0; i &lt; r.length; i++) {</p>
<p>...</p>
<p>}</p></td>
</tr>
<tr class="odd">
<td><strong>Für-jedes-Schleife</strong></td>
<td><img src="media/844810adca02b298cde95209068382430c9983f7.png" title="el_foreach.png" style="width:2.32292in;height:0.47917in" alt="el_foreach.png" /></td>
<td><p>for (int x : r) {</p>
<p>...</p>
<p>}</p></td>
</tr>
<tr class="even">
<td><strong>Kommentar</strong></td>
<td><img src="media/f6d511713d9903ff11bb142b2d80965e5cf80124.png" title="el_kommentar.png" style="width:2.32292in;height:0.26042in" alt="el_kommentar.png" /></td>
<td>hilf = r[i]; // Wert retten</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Infoteil 3: Die Tracetabelle</strong></p>
<ul>
<li><p>Eine <strong>Spalte je Variable</strong> – bei Bedarf zusätzlich eine Spalte für die Bedingung (w/f) und für Rückgabe oder Ausgabe.</p></li>
<li><p>Eine <strong>neue Zeile</strong>, sobald sich ein Wert ändert. Unveränderte Werte darfst du weglassen.</p></li>
<li><p>Gibt die Aufgabe die Spalten vor, hältst du dich genau daran.</p></li>
</ul>
<p><strong>Beispiel:</strong> Aufruf summe(r) mit r = {4, 7, 1}</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
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
<p>}</p>
<p>return summe;</p></td>
</tr>
</tbody>
</table></td>
<td><table>
<colgroup>
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Schritt</strong></th>
<th><strong>i</strong></th>
<th><strong>i &lt; 3</strong></th>
<th><strong>r[i]</strong></th>
<th><strong>summe</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>0</td>
</tr>
<tr class="even">
<td>2</td>
<td>0</td>
<td>w</td>
<td>4</td>
<td>4</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>w</td>
<td>7</td>
<td>11</td>
</tr>
<tr class="even">
<td>4</td>
<td>2</td>
<td>w</td>
<td>1</td>
<td>12</td>
</tr>
<tr class="odd">
<td>5</td>
<td>3</td>
<td>f</td>
<td></td>
<td>Rückgabe 12</td>
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
<td><p><strong>Infoteil 4: Erlaubte Zeichenketten-Operationen (abschließend!)</strong></p>
<p>Im Abitur darfst du <strong>nur</strong> diese Operationen verwenden. Beispiele mit s = "Drache":</p>
<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 25%" />
<col style="width: 29%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th><strong>Java</strong></th>
<th><strong>Beispiel</strong></th>
<th><strong>Ergebnis</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Länge</td>
<td>s.length()</td>
<td>s.length()</td>
<td>6</td>
</tr>
<tr class="even">
<td>Zeichen an Position</td>
<td>s.charAt(i)</td>
<td>s.charAt(0)</td>
<td>'D'</td>
</tr>
<tr class="odd">
<td>Teilzeichenkette (von a einschließlich bis b ausschließlich)</td>
<td>s.substring(a, b)</td>
<td>s.substring(1, 4)</td>
<td>"rac"</td>
</tr>
<tr class="even">
<td>Verketten</td>
<td>s + t</td>
<td>s + "nei"</td>
<td>"Drachenei"</td>
</tr>
<tr class="odd">
<td>Gleichheit</td>
<td>s.equals(t)</td>
<td>s.equals("Drache")</td>
<td>true</td>
</tr>
<tr class="even">
<td>enthält Teilzeichenkette</td>
<td>s.contains(t)</td>
<td>s.contains("ach")</td>
<td>true</td>
</tr>
<tr class="odd">
<td>lexikographischer Vergleich</td>
<td>s.compareTo(t)</td>
<td>s.compareTo("Elfe")</td>
<td>negative Zahl (D vor E)</td>
</tr>
<tr class="even">
<td>ASCII-Wert ↔︎ Zeichen</td>
<td>(int) c / (char) n</td>
<td>(int) 'A' / (char) 97</td>
<td>65 / 'a'</td>
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
<td><p><strong>Achtung Abi:</strong></p>
<ul>
<li><p><strong>Nicht</strong> verwenden: toLowerCase, toUpperCase, split, indexOf, trim, replace usw.</p></li>
<li><p>Zeichenketten <strong>immer</strong> mit equals vergleichen, nie mit ==. Die Online-IDE vergleicht mit == zwar den Inhalt – echtes Java und das Abitur aber nicht!</p></li>
<li><p>Einzelne Zeichen (char) vergleichst du dagegen mit ==, z. B. s.charAt(i) == 'a'.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Aufgabe 4: Das Rätsel am Portaltor** **PAPIER** ★ **+5 XP**

In das Portaltor ist ein Struktogramm eingeritzt. Wer seinen Zweck errät, darf passieren.

<img src="media/64029024e4c3285c11a0ac6c2bc6b416a5059e3c.png" title="w0_geheim.png" style="width:3.79167in;height:1.85417in" alt="w0_geheim.png" />

*Abbildung 1: Das Struktogramm am Portaltor*

|        |                                                                                                       |              |
|--------|-------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Gib den Rückgabewert für den Aufruf mit r = {7, 3, 9, 3, 5} an. Notiere dazu die Werte von i und pos. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

|        |                                                                                             |              |
|--------|---------------------------------------------------------------------------------------------|--------------|
| **b)** | Beschreibe, was die Methode allgemein berechnet. Schlage einen passenden Methodennamen vor. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

|        |                                                                                       |              |
|--------|---------------------------------------------------------------------------------------|--------------|
| **c)** | Erläutere, was bei einer leeren Reihung passiert. Formuliere eine Vorbedingung für r. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

|        |                                                                                                                     |              |
|--------|---------------------------------------------------------------------------------------------------------------------|--------------|
| **d)** | Im Struktogramm wird \< durch ≤ ersetzt. Gib an, wie sich das Ergebnis für die Reihung aus a) ändert, und begründe. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

**Aufgabe 5: Die Spur der Schatztruhen** **PAPIER** ★★ **+5 XP**

Eine Heldin öffnet Schatztruhen der Reihe nach, bis sie genug Gold gesammelt hat.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 public static int schatzSuche(int[] truhe, int ziel) {</p>
<p>2 int summe = 0;</p>
<p>3 int i = 0;</p>
<p>4 while (i &lt; truhe.length &amp;&amp; summe &lt; ziel) {</p>
<p>5 summe = summe + truhe[i];</p>
<p>6 i++;</p>
<p>7 }</p>
<p>8 return i;</p>
<p>9 }</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                         |              |
|--------|---------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Erstelle eine Tracetabelle für den Aufruf schatzSuche({5, 8, 2, 9, 4}, 15) und gib den Rückgabewert an. | **\[4 BE\]** |

| **Schritt** | **i** | **summe** | **i \< truhe.length** | **summe \< ziel** | **Bedingung (w/f)** |
|-------------|-------|-----------|-----------------------|-------------------|---------------------|
|             |       |           |                       |                   |                     |
|             |       |           |                       |                   |                     |
|             |       |           |                       |                   |                     |
|             |       |           |                       |                   |                     |
|             |       |           |                       |                   |                     |
|             |       |           |                       |                   |                     |

Rückgabewert: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

|        |                                                                 |              |
|--------|-----------------------------------------------------------------|--------------|
| **b)** | Beschreibe in einem Satz, was die Methode allgemein zurückgibt. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

|        |                                                                                                                                                   |              |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **c)** | Gib einen Aufruf an, bei dem die Methode truhe.length zurückgibt. Begründe, warum es trotzdem nicht zu einem Zugriff außerhalb der Reihung kommt. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

**Aufgabe 6: Vom Code zum Bauplan** **PAPIER** ★★ **+5 XP**

Im Würfelspiel des Dungeons zählt eine 6 als Volltreffer (10 Punkte), eine 1 als Patzer (−5 Punkte). Alle anderen Würfe zählen ihre Augenzahl.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static int wertung(int[] wuerfe) {</p>
<p>int punkte = 0;</p>
<p>for (int w : wuerfe) {</p>
<p>if (w == 6) {</p>
<p>punkte = punkte + 10;</p>
<p>} else {</p>
<p>if (w == 1) {</p>
<p>punkte = punkte - 5;</p>
<p>} else {</p>
<p>punkte = punkte + w;</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>return punkte;</p>
<p>}</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                            |              |
|--------|------------------------------------------------------------------------------------------------------------|--------------|
| **a)** | Stelle die Methode als Struktogramm nach EH § 5 dar – mit Kopfzeile, Für-jedes-Schleife und Verzweigungen. | **\[5 BE\]** |

<img src="media/5d5c9121bf8d67eb31ea7e0bd3355c363ba88d86.png" title="grid_17_9.png" style="width:6.69792in;height:3.54167in" alt="grid_17_9.png" />

|        |                                                                          |              |
|--------|--------------------------------------------------------------------------|--------------|
| **b)** | Gib den Rückgabewert für die Würfe {6, 1, 3} und für {2, 6, 6, 1, 5} an. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |

**Aufgabe 7: Bug-Hunt im Bauplan** **PAPIER** ★★ **+5 XP**

Die Methode soll den Index des **letzten** Vorkommens von x in r liefern, sonst −1. Im Struktogramm steckt **genau ein** Fehler.

<img src="media/800160df881d97532bf076445056c9cde5f0ee25.png" title="w0_bug.png" style="width:4.17708in;height:1.85417in" alt="w0_bug.png" />

*Abbildung 2: Struktogramm mit Fehler*

|        |                                                                                           |              |
|--------|-------------------------------------------------------------------------------------------|--------------|
| **a)** | Finde den Fehler. Beschreibe, was beim Ausführen mit r = {4, 2, 4, 1} und x = 9 passiert. | **\[2 BE\]** |

|     |
|-----|
|     |
|     |
|     |

|        |                                |              |
|--------|--------------------------------|--------------|
| **b)** | Gib die korrigierte Stelle an. | **\[1 BE\]** |

|     |
|-----|
|     |

|        |                                                                                                                                                                                                                        |              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **c)** | Eine Mitschülerin schlägt vor: „Lauf die Reihung von hinten nach vorne durch und gib beim ersten Treffer sofort i zurück.“ Stelle diese Variante als Struktogramm dar (mit Solange-Schleife). Erläutere einen Vorteil. | **\[4 BE\]** |

<img src="media/e4f8ffd0755f42868bd938f3fd23b0a1a8b4b6ae.png" title="grid_17_7.png" style="width:6.69792in;height:2.76042in" alt="grid_17_7.png" />

|     |
|-----|
|     |
|     |

**Aufgabe 8: Der Debugger als Trace-Maschine** **IDE** ★★ **+15 XP Side-Quest**

Die Online-IDE kann ein Programm Schritt für Schritt ausführen. So prüfst du deine Tracetabelle aus Aufgabe 5 – und siehst, was im Rechner wirklich passiert.

|        |                                                                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **a)** | Lege eine neue Datei an. Schreibe eine Klasse Spur mit der Methode schatzSuche (als public static) aus Aufgabe 5. Rufe sie im Hauptprogramm auf: |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>int[] truhe = {5, 8, 2, 9, 4};</p>
<p>println(Spur.schatzSuche(truhe, 15));</p></td>
</tr>
</tbody>
</table>

|        |                                                                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **b)** | Setze einen **Haltepunkt** (Breakpoint): Klicke links neben die Zeilennummer der Zeile summe = summe + truhe\[i\];. Starte das Programm. Es hält an dieser Zeile an. |

|        |                                                                                                                                                                                                                                                         |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **c)** | Gehe mit dem Knopf für den **Einzelschritt** weiter. Beobachte in der **Variablenansicht** die Werte von i und summe. Vergleiche bei jedem Halt mit deiner Tracetabelle aus Aufgabe 5 und markiere Abweichungen farbig. Wo lagst du falsch – und warum? |

|     |
|-----|
|     |
|     |

|        |                                                                                                                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **d)** | Baue absichtlich einen Fehler ein: Ändere die Bedingung zu i \<= truhe.length und rufe die Methode mit ziel = 100 auf. Bei welchem Wert von i bricht das Programm ab? Notiere die Fehlermeldung. |

|     |
|-----|
|     |
|     |

**Hinweis:** Wie Haltepunkt, Einzelschritt und Variablenansicht genau bedient werden, zeigt dir die Lehrkraft am Beamer.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Für Schnelle</strong></p>
<ul>
<li><p><strong>Architekten-Probe:</strong> Zeichne ein Struktogramm zu deiner Methode istPalindrom aus Level 0 (erst, wenn die Stufe Experte grün ist). Prüfe es mit der Werkzeugkarte „Struktogramm“.</p></li>
<li><p><strong>Rätselschmiede:</strong> Erfinde selbst ein Struktogramm-Rätsel wie in Aufgabe 4 für eine andere Gilde (Lösung auf die Rückseite). Ist es fehlerfrei und lösbar, gibt es Mentor-XP.</p></li>
<li><p><strong>Trace-Detektiv:</strong> Fünf fehlerfreie Tracetabellen in Folge bringen das Badge „Trace-Detektiv“. Aufgabe 5 ist die erste!</p></li>
</ul></td>
</tr>
</tbody>
</table>
