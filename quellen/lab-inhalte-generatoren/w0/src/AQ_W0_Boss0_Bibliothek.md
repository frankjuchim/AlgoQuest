<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>BOSS-KAMPF 0 · Welt 0 · DS 7 · Bearbeitungszeit 60 min · Hilfsmittel: Werkzeugkarten</strong></p>
<p><strong>W0·Boss – Aufnahmeprüfung: Die Bibliothek der Akademie</strong></p>
<p>Erreichbar: 24 BE → <strong>48 XP (2 XP je BE)</strong> · Papier-Compiler zu e): <strong>+30 XP, +10 XP beim ersten Versuch</strong></p></td>
</tr>
</tbody>
</table>

Bevor euer Studio Helden schmieden darf, wartet die Aufnahmeprüfung der Akademie der Baumeister. Die Bibliothekarin verwaltet die Ausleihzahlen der Zauberbücher in Reihungen – und braucht dringend eigene Methoden. Alle Operationen sind Klassenoperationen der Klasse **Bibliothek**. Zeig, dass du Signaturen lesen, Methodenaufrufe verfolgen und eigene Methoden von Hand schreiben kannst!

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Hinweise zur Bearbeitung</strong></p>
<ul>
<li><p>Bearbeite alle Teilaufgaben <strong>ohne Gerät</strong> auf dem Antwortbogen am Ende dieses Hefts. Erlaubt sind nur deine Werkzeugkarten.</p></li>
<li><p>Implementierungen schreibst du in <strong>Java</strong>, Struktogramme nach den Abi-Konventionen (Kopf mit Signatur, ←, „gib … zurück“).</p></li>
<li><p>Zeitbudget wie im Abitur: ca. 2,5 Minuten pro BE. Die BE stehen rechts neben jeder Teilaufgabe.</p></li>
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
<td><p><strong>Papier-Compiler</strong></p>
<p>Deine Lösung zu <strong>Aufgabe e)</strong> tippst du direkt nach dem Boss-Kampf <strong>unverändert</strong> in der Online-IDE ab und startest die Tests im Testrunner. Alle Tests grün: +30 XP, beim ersten Versuch +10 XP und das Badge <strong>Papier-Compiler</strong>. Hast du in e) und f) alle Leer- und Index-Abfragen und jeden Rückgabepfad richtig, gibt es das Badge <strong>Fehlerjäger</strong>.</p></td>
</tr>
</tbody>
</table>

**Aufgaben**

<table>
<colgroup>
<col style="width: 91%" />
<col style="width: 8%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>a)</strong> Abbildung 2 enthält die Signaturen der Operationen der Klasse Bibliothek. In Java werden alle Operationen als Klassenoperationen (public static) umgesetzt.</p>
<blockquote>
<p>Geben Sie zu den Signaturen der Operationen <strong>durchschnitt</strong> und <strong>neueAuflage</strong> jeweils den Java-Methodenkopf an. Geben Sie zum Java-Methodenkopf public static void markiere(String[] titel, int index, char zeichen) die Signatur in der Notation aus Abbildung 2 an.</p>
<p>Im Hauptprogramm steht die Anweisung int s = sterneSumme(werte, 2, 6);. Die Variable werte verweist auf eine Reihung mit der Belegung von ausleihen aus Abbildung 1. Benennen Sie für diesen Aufruf die Parameter und die Argumente und erläutern Sie den Unterschied.</p>
<p>Erläutern Sie, warum der Compiler die Anweisung int d = durchschnitt(werte); ablehnt, die Anweisung double s = sterneSumme(werte, 0, 3); dagegen akzeptiert.</p>
</blockquote></td>
<td><strong>[4 BE]</strong></td>
</tr>
<tr class="even">
<td><p><strong>b)</strong> Die Operationen <strong>sterne</strong> und <strong>sterneSumme</strong> sind in Abbildung 3 als Struktogramme dargestellt.</p>
<blockquote>
<p>Dokumentieren Sie im Antwortbogen die Verarbeitung beim Aufruf sterneSumme(ausleihen, 2, 6) mit der Belegung aus Abbildung 1. Ein Eintrag erfolgt jeweils an der grau markierten Stelle. Notieren Sie den Aufruf von sterne mit seinem Argument, den Wert der lokalen Variablen s der Operation sterne (–, falls s nicht belegt wird), den Rückgabewert von sterne und den Wert von summe. Geben Sie den Rückgabewert von sterneSumme an.</p>
<p>Geben Sie alle Ausleihzahlen n ≥ 0 an, für die sterne den Wert 5 liefert, und begründen Sie Ihre Angabe.</p>
<p>Erläutern Sie, was beim Aufruf sterneSumme(ausleihen, 5, 8) geschieht.</p>
</blockquote></td>
<td><strong>[4 BE]</strong></td>
</tr>
<tr class="odd">
<td><p><strong>c)</strong> Die Operation <strong>eintragen</strong> soll anzahl weitere Ausleihen für das Buch mit dem angegebenen Index vermerken. Die Operation <strong>jahresabschluss</strong> soll am Jahresende alle Ausleihzahlen auf 0 setzen. Abbildung 4 zeigt beide Operationen und ein Hauptprogramm.</p>
<blockquote>
<p>Geben Sie die drei Ausgaben des Hauptprogramms an und begründen Sie diese mithilfe der Begriffe Wertübergabe und Referenz.</p>
<p>Beurteilen Sie die Implementierung der Operation jahresabschluss und geben Sie eine korrigierte Implementierung an.</p>
</blockquote></td>
<td><strong>[3 BE]</strong></td>
</tr>
<tr class="even">
<td><p><strong>d)</strong> Die Operation <strong>indexMeistgeliehen</strong> liefert den Index des am häufigsten ausgeliehenen Buches. Haben mehrere Bücher die höchste Ausleihzahl, wird der kleinste dieser Indizes geliefert; für eine leere Reihung wird −1 geliefert. Für die Belegung aus Abbildung 1 wird 3 geliefert.</p>
<blockquote>
<p>Entwickeln Sie ein Struktogramm für die Operation indexMeistgeliehen.</p>
</blockquote></td>
<td><strong>[4 BE]</strong></td>
</tr>
<tr class="odd">
<td><p><strong>e)</strong> Für eine Neuauflage sollen die beliebten Bücher ermittelt werden. Die Operation <strong>neueAuflage</strong> liefert eine neue Reihung mit den Titeln aller Bücher, die mindestens grenze-mal ausgeliehen wurden, in der Reihenfolge der Reihung titel. Die Länge der gelieferten Reihung entspricht genau der Anzahl dieser Bücher; gibt es kein solches Buch, wird eine leere Reihung (Länge 0) geliefert. Die Reihungen titel und ausleihen sind gleich lang (auch die Länge 0 ist möglich) und bleiben unverändert. Die Operation anzahlMindestens (Abbildung 2) darf verwendet werden.</p>
<blockquote>
<p>Beispiel: neueAuflage(titel, ausleihen, 9) liefert mit der Belegung aus Abbildung 1 eine Reihung der Länge 4 mit den Titeln Feuerkunde, Sternkarten, Zahlenmagie und Nebelpfade.</p>
<p>Implementieren Sie die Operation neueAuflage in Java.</p>
</blockquote></td>
<td><strong>[5 BE]</strong></td>
</tr>
<tr class="even">
<td><p><strong>f)</strong> Die Operation <strong>durchschnitt</strong> soll die durchschnittliche Ausleihzahl als Kommazahl liefern, für eine leere Reihung 0.0. Die Implementierung in Abbildung 5 wird vom Compiler abgelehnt; insgesamt enthält sie drei Fehler.</p>
<blockquote>
<p>Identifizieren Sie die drei Fehler und erläutern Sie jeweils deren Auswirkung – bei den beiden Fehlern, die der Compiler nicht meldet, anhand der Belegung aus Abbildung 1. Geben Sie eine korrigierte Implementierung an.</p>
</blockquote></td>
<td><strong>[4 BE]</strong></td>
</tr>
</tbody>
</table>

**Summe: 24 BE**

**Material**

*zu allen Aufgabenteilen*

| **Index** | **0**      | **1**     | **2**      | **3**       | **4**        | **5**        | **6**       | **7**      |
|-----------|------------|-----------|------------|-------------|--------------|--------------|-------------|------------|
| titel     | Feuerkunde | Trankbuch | Runenlehre | Sternkarten | Kräuterfibel | Drachenrecht | Zahlenmagie | Nebelpfade |
| ausleihen | 12         | 0         | 7          | 25          | 3            | 0            | 18          | 9          |

*Abbildung 1: Belegung der Reihungen titel (Reihung von Zeichenkette) und ausleihen (Reihung von Ganzzahl). Das Buch mit dem Index i hat den Titel titel\[i\] und wurde ausleihen\[i\]-mal ausgeliehen.*

| **Signatur**                                                                                                              | **Beschreibung**                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| sterne(n: Ganzzahl): Ganzzahl                                                                                             | liefert die Sternebewertung (0 bis 5) zu einer Ausleihzahl n ≥ 0 (Abbildung 3)                      |
| sterneSumme(ausleihen: Reihung von Ganzzahl, start: Ganzzahl, ende: Ganzzahl): Ganzzahl                                   | liefert die Summe der Sterne der Bücher mit den Indizes start bis ende (Abbildung 3)                |
| anzahlMindestens(ausleihen: Reihung von Ganzzahl, grenze: Ganzzahl): Ganzzahl                                             | liefert die Anzahl der Bücher, die mindestens grenze-mal ausgeliehen wurden (bereits implementiert) |
| eintragen(ausleihen: Reihung von Ganzzahl, index: Ganzzahl, anzahl: Ganzzahl): nichts                                     | Aufgabenteil c), Abbildung 4                                                                        |
| jahresabschluss(ausleihen: Reihung von Ganzzahl): nichts                                                                  | Aufgabenteil c), Abbildung 4                                                                        |
| indexMeistgeliehen(ausleihen: Reihung von Ganzzahl): Ganzzahl                                                             | Aufgabenteil d)                                                                                     |
| neueAuflage(titel: Reihung von Zeichenkette, ausleihen: Reihung von Ganzzahl, grenze: Ganzzahl): Reihung von Zeichenkette | Aufgabenteil e)                                                                                     |
| durchschnitt(ausleihen: Reihung von Ganzzahl): Kommazahl                                                                  | Aufgabenteil f), Abbildung 5                                                                        |

*Abbildung 2: Übersicht über die Klassenoperationen der Klasse Bibliothek*

*zu Aufgabenteil b)*

<img src="media/9355a9fd5dbec53fe507c3be17a4667da9e7331b.png" style="width:3.19792in;height:2.27083in" />

<img src="media/4b7912999b48156b6e6733fbdfcc6d37fe4c90c8.png" style="width:5.16667in;height:1.51042in" />

*Abbildung 3: Struktogramme der Operationen sterne und sterneSumme. Hinweis: Die Division von Ganzzahlen ist als Division ohne Rest zu verstehen.*

*zu Aufgabenteil c)*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static void eintragen(int[] ausleihen, int index, int anzahl) {</p>
<p>ausleihen[index] = ausleihen[index] + anzahl;</p>
<p>anzahl = 0;</p>
<p>}</p>
<p>public static void jahresabschluss(int[] ausleihen) {</p>
<p>ausleihen = new int[ausleihen.length];</p>
<p>}</p>
<p>// Hauptprogramm</p>
<p>int[] a = {12, 0, 7};</p>
<p>int n = 4;</p>
<p>eintragen(a, 2, n);</p>
<p>println(a[2] + " " + n);</p>
<p>jahresabschluss(a);</p>
<p>println(a[0]);</p>
<p>int[] b = a;</p>
<p>b[0] = 0;</p>
<p>println(a[0]);</p></td>
</tr>
</tbody>
</table>

*Abbildung 4: Operationen eintragen und jahresabschluss mit Hauptprogramm (Online-IDE: println ohne System.out)*

*zu Aufgabenteil f)*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>public static double durchschnitt(int[] ausleihen) {</p>
<p>if (ausleihen.length &gt; 0) {</p>
<p>int summe = 0;</p>
<p>for (int i = 1; i &lt; ausleihen.length; i++) {</p>
<p>summe = summe + ausleihen[i];</p>
<p>}</p>
<p>return summe / ausleihen.length;</p>
<p>}</p>
<p>}</p></td>
</tr>
</tbody>
</table>

*Abbildung 5: fehlerhafte Implementierung der Operation durchschnitt*

**Antwortbogen**

**a)** Methodenköpfe, Signatur, Parameter und Argumente, Compiler **\[4 BE\]**

Methodenkopf durchschnitt:

|     |
|-----|
|     |

Methodenkopf neueAuflage:

|     |
|-----|
|     |
|     |

Signatur markiere:

|     |
|-----|
|     |

Parameter, Argumente, Unterschied · Compiler:

|     |
|-----|
|     |
|     |
|     |
|     |
|     |
|     |

**b)** Tracetabelle zu sterneSumme(ausleihen, 2, 6) · Analyse · Laufzeitfehler **\[4 BE\]**

| **i**            | **Aufruf von sterne** | **s (in sterne)** | **Rückgabe von sterne** | **summe** |
|------------------|-----------------------|-------------------|-------------------------|-----------|
| vor der Schleife | –                     | –                 | –                       | 0         |
|                  |                       |                   |                         |           |
|                  |                       |                   |                         |           |
|                  |                       |                   |                         |           |
|                  |                       |                   |                         |           |
|                  |                       |                   |                         |           |
|                  |                       |                   |                         |           |

Rückgabewert von sterneSumme(ausleihen, 2, 6): \_\_\_\_\_\_\_\_

|     |
|-----|
|     |
|     |
|     |
|     |
|     |

**c)** Ausgaben, Begründung, Beurteilung und Korrektur von jahresabschluss **\[3 BE\]**

Ausgabe 1: \_\_\_\_\_\_\_\_\_\_\_\_\_\_ Ausgabe 2: \_\_\_\_\_\_\_\_\_\_\_\_\_\_ Ausgabe 3: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

|     |
|-----|
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |

**d)** Struktogramm der Operation indexMeistgeliehen **\[4 BE\]**

|                                                                          |
|--------------------------------------------------------------------------|
| *Zeichenfläche für das Struktogramm (Kopf mit Signatur nicht vergessen)* |

**e)** Implementierung von neueAuflage – Papier-Compiler: sauber und lesbar schreiben! **\[5 BE\]**

|     |
|-----|
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |

**f)** Fehler, Auswirkungen und korrigierte Implementierung von durchschnitt **\[4 BE\]**

|     |
|-----|
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |

**Auswertung (Peer-Korrektur nach Kernpunkten)**

| **Teilaufgabe** | **a)** | **b)** | **c)** | **d)** | **e)** | **f)** | **Summe** | **XP** |
|-----------------|--------|--------|--------|--------|--------|--------|-----------|--------|
| max. BE         | 4      | 4      | 3      | 4      | 5      | 4      | 24        | 48     |
| erreicht        |        |        |        |        |        |        |           |        |

Korrigiert von Gilde: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Papier-Compiler e): ☐ grün beim 1. Versuch ☐ grün nach Korrektur ☐ nicht grün
