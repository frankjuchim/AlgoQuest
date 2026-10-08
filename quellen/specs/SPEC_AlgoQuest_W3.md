# SPEC – Algo Quest, Welt 3 „Das Labyrinth“ (Rekursion, 2D-Reihungen, Teile und herrsche)

Grundkonventionen (LIES ZUERST VOLLSTÄNDIG): …/scratchpad/SPEC_AlgoQuest_W0_W1.md (Didaktik, XP, EH-2025-Notation,
Gestaltung, Online-IDE/JUnit-Dialekt, Kommentarstil); ergänzend SPEC_AlgoQuest_W2.md und SPEC_AlgoQuest_W0_Akademie.md
(neue DS-Zählung: Welt 3 = DS 18–23, Wochen 6–8; Kür-DS 20).
Scratchpad = /tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad
Fertige Materialien als Vorbild: /mnt/user-data/outputs/AlgoQuest/Welt0, Welt1, Welt2, Werkzeuge, WebApp.
Generatoren (in eigenen Unterordner …/scratchpad/w3_<name>/ kopieren): w0a_ab, w2_ab (ABs; ab/render.py = Struktogramm-
Renderer nach EH §5 – für REKURSIVE Struktogramme ggf. erweitern: Aufruf als normale Anweisung „x ← name(n − 1)“),
w0a_pptx/w2_pptx (Folien, aq_common.js), w0a_boss/w2_boss (Boss/Kata/Lehrerhinweise, verify-Skripte), w0a_code/w2_code
(Java-Harness, Mutationstests). Andere Welten NICHT verändern.
Ausgabe: /mnt/user-data/outputs/AlgoQuest/Welt3/ (Kata/Lehrerhinweise in Werkzeuge/).

## 1. Didaktischer Ort
Welt 3 – Das Labyrinth (W6–8, 6 DS). Ziel: Rekursion tracen, entwerfen und unbekannte rekursive Verfahren analysieren.
Spielmodul: Dungeon-Karte als 2D-Reihung, Nebel lüften (Flood-Fill), Wegsuche (Backtracking), Deko-Fraktale.
| DS | Wo | Inhalt | Material | Abi-Bezug |
| 18 | 6 | Basisfall und Rekursionsschritt, Aufrufstapel, Rekursionstabelle mit Spalte „Rekursionstiefe“, Anzahl Aufrufe bestimmen (Fibonacci), Rekursion vs. Schleife; Turtle-Fraktale | AB1, L3.1, Fraktale-Gerüst | Rekursion 19/22 Aufgaben |
| 19 | 7 | 2D-Reihung als Dungeon-Karte [Zeile][Spalte] (EH §3): Durchlauf, Nachbarschaft (4er/8er), Randfälle; rekursiver Flood-Fill „Nebel lüften“ | AB2, L3.2, Dungeon-Gerüst | 22H-C, 22N-C |
| 20 (K) | 7 | Backtracking: Wegsuche im Labyrinth, Schritt zurücknehmen erläutern; Dungeon-Rennen (Wettbewerb) | AB2 Teil 2, L3.2 Experte, Dungeon-Rennen | 24N-B h/i |
| 21 | 7 | Teile und herrsche: Prinzip, binäre Suche rekursiv, Maximum per T&H, Mergesort; Teilungs- und Verschmelzungsbaum von Hand | AB3, L3.3 | 23N-C e, 24H-A d, 26H-B g |
| 22 | 8 | Quicksort (Pivot links, kleinere nach vorn); Transfer: unbekannte rekursive Sortierungen analysieren (Stooge-Sort, rekursiver Selectionsort) | AB3 Teil 2, L3.3 Experte | 24H-A e/f, 24H-B h/i, 23H-B c |
| 23 | 8 | Boss 3 | Boss 3 + EH | 26H-B g–i |

## 2. Online-IDE – EXAKTE API (alle Materialien identisch!)
Datei Welt3/AQ_W3_L3_Labyrinth_Geruest.txt + _LSG.txt. Testklassen L31RekursionTest, L32KarteTest, L33TeileHerrscheTest,
Präfixe basis_/erweiterung_/experte_ (10/20/30 XP). ALLE Methoden mit „rek“ im Auftrag MÜSSEN rekursiv sein (keine Schleife) –
Hinweis im Gerüst; Tests können das nicht erzwingen → „Code-Review“-Hinweis in LSG.

class Rekursion (L3.1, DS 18) – alle static, REKURSIV ohne Schleifen:
  Basis:       fakultaet(n: Ganzzahl): Ganzzahl            → n >= 0, fakultaet(0) = 1
               summeBis(n: Ganzzahl): Ganzzahl             → 0 + 1 + … + n, n >= 0
               potenz(basis: Ganzzahl, exponent: Ganzzahl): Ganzzahl → exponent >= 0
  Erweiterung: anzahlZiffern(n: Ganzzahl): Ganzzahl        → n >= 0; anzahlZiffern(0) = 1
               istPalindrom(s: Zeichenkette): Wahrheitswert → rekursiv mit charAt/length/substring; "" und 1 Zeichen → true
               summeAb(r: Reihung von Ganzzahl, i: Ganzzahl): Ganzzahl → Summe r[i] … r[length−1]; i == length → 0
  Experte:     maximumAb(r: Reihung von Ganzzahl, i: Ganzzahl): Ganzzahl → größter Wert ab Index i (0 <= i < length)
               dual(n: Ganzzahl): Zeichenkette             → Dualdarstellung, n >= 0, dual(0) = "0", dual(6) = "110"
               fibonacci(n: Ganzzahl): Ganzzahl            → fib(0) = 0, fib(1) = 1, baumrekursiv (zwei Aufrufe!);
               + static aufrufe: Ganzzahl (öffentlich)     → jeder Aufruf von fibonacci erhöht aufrufe um 1
                                                             (Test: aufrufe = 0; fibonacci(5) → 5, aufrufe == 15)

class Karte (L3.2, DS 19–20) – Dungeon-Karte als 2D-Reihung von Zeichen [Zeile][Spalte]
  Zeichen: '#' Wand, '.' frei (vernebelt), 'S' Start, 'Z' Ziel, '+' gelüftet/besucht, '*' Weg, 'x' Sackgasse.
  - feld: Reihung von Reihung von Zeichen
  + c Karte(zeilen: Reihung von Zeichenkette)   → VORGEGEBEN: feld[z][s] = zeilen[z].charAt(s); alle Zeilen gleich lang
  + getZeilen(): Ganzzahl; + getSpalten(): Ganzzahl; + getFeld(z, s): Zeichen; + setFeld(z, s, c): nichts; + alsText(): Zeichenkette
    (VORGEGEBEN; alsText = Zeilen mit "\n" getrennt, ohne abschließendes "\n")
  Basis:       istImFeld(z: Ganzzahl, s: Ganzzahl): Wahrheitswert
               istBegehbar(z, s): Wahrheitswert          → im Feld UND Zeichen ist '.', 'S' oder 'Z'
               anzahlWaende(): Ganzzahl                  → Anzahl '#'
  Erweiterung: anzahlBegehbareNachbarn(z, s): Ganzzahl   → 4er-Nachbarschaft (oben, rechts, unten, links), Rand beachten
               lueften(z: Ganzzahl, s: Ganzzahl): nichts → REKURSIVER Flood-Fill: ist (z, s) begehbar ('.', 'S' oder 'Z')?
                                                           dann wird ein '.' zu '+' (S und Z bleiben S und Z, gelten aber als
                                                           besucht – Achtung Endlosrekursion: S/Z vorübergehend markieren
                                                           oder eigene Besucht-Logik; Ergebnis: alle von (z, s) aus
                                                           erreichbaren '.' sind '+', S/Z unverändert sichtbar) und die vier
                                                           Nachbarn werden gelüftet (Reihenfolge oben, rechts, unten, links)
               anzahlGelueftet(): Ganzzahl                → Anzahl '+'
  Experte:     findeWeg(z: Ganzzahl, s: Ganzzahl): Wahrheitswert → BACKTRACKING von (z, s) zum Ziel 'Z' (4er-Nachbarschaft,
                                                           Reihenfolge oben, rechts, unten, links): true, wenn Z erreichbar.
                                                           Danach: Felder des gefundenen Wegs (ohne S und Z) = '*', besuchte
                                                           Sackgassen-Felder = 'x', nie besuchte bleiben '.'.
                                                           Wird Z nicht gefunden → false, alle besuchten '.' sind 'x'.
               + schritte: Ganzzahl (öffentlich, Instanzattribut) → Anzahl der Aufrufe von findeWeg (für Rekursionstiefe/Rennen);
                                                           wird NICHT automatisch zurückgesetzt (Test setzt schritte = 0).
  Testkarten (für Gerüst, AB, Kata, Boss gemeinsam nutzbar) legt der Code-Agent fest und dokumentiert sie im LSG-Kopf.

class TeileUndHerrsche (L3.3, DS 21–22) – static
  Basis:       binaerRek(r: Reihung von Ganzzahl, x: Ganzzahl, lo: Ganzzahl, hi: Ganzzahl): Ganzzahl → r aufsteigend, Index
                                                           oder −1; mid = (lo + hi) / 2; lo > hi → −1
               binaer(r, x): Ganzzahl                     → ruft binaerRek(r, x, 0, r.length − 1)
  Erweiterung: maximumTH(r, von: Ganzzahl, bis: Ganzzahl): Ganzzahl → Teile und herrsche: von == bis → r[von]; sonst Mitte
                                                           teilen, beide Hälften rekursiv, größeren Wert zurück (von <= bis)
               mergeSort(r: Reihung von Ganzzahl): Reihung von Ganzzahl → NEUE aufsteigend sortierte Reihung; Länge <= 1 → Kopie;
                                                           teilt in links = r[0 … mitte−1], rechts = r[mitte … ende] mit
                                                           mitte = länge / 2; nutzt teilstueck und verschmelze
               teilstueck(r, von: Ganzzahl, bis: Ganzzahl): Reihung von Ganzzahl → Kopie r[von] … r[bis − 1] (bis exklusiv)
               verschmelze(a, b): Reihung von Ganzzahl    → beide aufsteigend → neue aufsteigende Reihung
  Experte:     quickSort(r: Reihung von Ganzzahl): nichts → in-place, ruft quickSort(r, 0, r.length − 1)
               quickSort(r, lo, hi): nichts               → lo < hi: p ← zerlege(r, lo, hi); quickSort(r, lo, p − 1); quickSort(r, p + 1, hi)
               zerlege(r, lo, hi): Ganzzahl               → Pivot = r[lo] (links); grenze ← lo; für i von lo+1 bis hi:
                                                           falls r[i] < pivot: grenze ← grenze + 1; tausche r[grenze], r[i];
                                                           danach tausche r[lo], r[grenze]; gib grenze zurück
               + static vergleiche: Ganzzahl              → zählt die Vergleiche r[i] < pivot in zerlege

## 3. Grafik-Gerüste (nicht per JUnit, Sichtprüfung in der IDE)
a) Welt3/AQ_W3_Fraktale_Geruest.txt + _LSG.txt – Neufassung des Lehrer-Gerüsts „10_Rekursive_Grafik.txt“ + „10_RekursionGrafik_LSG.txt“
   (Projects-Tool project_read) im Algo-Quest-Stil („Deko für den Dungeon“: Fraktal-Baum, Koch-Kurve/-Schneeflocke,
   Sierpinski-Dreieck, optional H-Baum). Bekannten Fehler beheben: Drehwinkel und Startdrehung von Sierpinski in Gerüst und
   LSG identisch und korrekt. Nur Turtle-API, die im Original verwendet wird (forward, turn, penUp/penDown, ggf. setBorderColor).
   Zusätzlich Aufrufzähler je Fraktal (Ausgabe „Aufrufe: …“), damit die Aufrufzahl in Abhängigkeit der Tiefe bestimmt werden kann.
b) Welt3/AQ_W3_DungeonRennen_Geruest.txt + _LSG.txt – Visualisierung: Karte als Rechtecke in der World (Wand dunkel, frei grau,
   gelüftet hell, Weg gold, Sackgasse rot), Animation über SystemTools.setSpeed. Modus 1 „Nebel lüften“ (Flood-Fill animiert),
   Modus 2 „Dungeon-Rennen“: Schüler schreiben MeinSolver.suche(z, s): Wahrheitswert mit freier Strategie, dürfen NUR die Rennen-API
   nutzen: Rennen.istBegehbar(z, s), Rennen.istZiel(z, s), Rennen.betrete(z, s) (zählt einen Schritt, markiert), Rennen.verlasse(z, s)
   (Sackgasse markieren, zählt NICHT), Rennen.zeilen()/spalten(). Kein direkter Zugriff auf die Karte (private). Drei feste Rennkarten
   (klein, mittel, groß mit mehreren Wegen/Sackgassen) + Kontrollkarte; Rennen.starten() führt alle aus, prüft, ob das Ziel tatsächlich
   über benachbarte betretene Felder erreicht wurde, und gibt aus: "RENNEN-ERGEBNIS: Schritte = …, gueltig = ja/nein" (weniger ist besser;
   Eintrag in der WebApp unter „Wettbewerbe“, Badge Rekursions-Magier/ XP-Bonus). LSG: Standard-Backtracking (oben, rechts, unten, links)
   + eine bessere Strategie (z. B. Richtung Ziel zuerst – Manhattan-Heuristik) + Tabelle der Referenz-Schritte je Karte (durch Ausführen ermittelt).

## 4. Boss 3 (DS 23) – NEUER Kontext (Transfer), z. B. „Die Kristallhöhle“ oder „Das Echo der Schlucht“
≈ 24 BE, 60 min, AFB ≈ 30/53/17 %. Teilaufgaben-Typen: Rekursionsverlauf einer gegebenen rekursiven Methode als Rekursionstabelle mit
Spalte „Rekursionstiefe“ dokumentieren; Anzahl rekursiver Aufrufe bestimmen und Verhalten bei Vergrößerung abschätzen; Prinzip der Rekursion
bzw. Teile und herrsche erläutern (Basisfall, Abbruch); rekursives Struktogramm nach EH §5 entwickeln (z. B. auf 2D-Karte oder Teilreihung);
Fehler in einem rekursiven Struktogramm finden und korrigieren (Format 26H-B i); unbekanntes rekursives Verfahren (z. B. Stooge-Sort-artig)
analysieren. Papier-Compiler: eine rekursive Implementierung wird danach abgetippt und getestet (Testklasse im EH-Anhang).

## 5. Kata-Karten Welt 3
Werkzeuge/kata_w3.json (Schema wie bisher, "welt": 3, ids "W3-01" …, 12–14 Karten; Kategorien aus der bisherigen Liste inkl.
"Methodenkopf und Signatur") + Werkzeuge/AQ_Kata-Karten_W3.docx. Themen: Rekursionstabelle mit Tiefe, Aufrufe zählen, Basisfall fehlt
(Endlosrekursion/StackOverflow), Rekursion ↔ Schleife, 2D-Reihung Index/Rand, Nachbarn zählen, Flood-Fill-Reihenfolge, Backtracking-Trace,
Mergesort-Teilungsbaum, Quicksort-Zerlegung (Zustand nach zerlege), binäre Suche rekursiv, fehlerhaftes rekursives Struktogramm,
unbekanntes rekursives Verfahren erklären.

## 6. Dateinamen Welt 3
Welt3/AQ_W3_Labyrinth.pptx
Welt3/AQ_W3_AB1_Rekursion.docx + AQ_W3_AB1_LSG.docx                          (DS 18)
Welt3/AQ_W3_AB2_Dungeon-Karte_Flood-Fill_Backtracking.docx + AQ_W3_AB2_LSG.docx (DS 19–20)
Welt3/AQ_W3_AB3_Teile_und_herrsche.docx + AQ_W3_AB3_LSG.docx                 (DS 21–22)
Welt3/AQ_W3_L3_Labyrinth_Geruest.txt + _LSG.txt
Welt3/AQ_W3_Fraktale_Geruest.txt + _LSG.txt
Welt3/AQ_W3_DungeonRennen_Geruest.txt + _LSG.txt
Welt3/AQ_W3_Boss3_<Kontext>.docx + Welt3/AQ_W3_Boss3_Erwartungshorizont.docx
Werkzeuge/kata_w3.json · Werkzeuge/AQ_Kata-Karten_W3.docx · Werkzeuge/AQ_W3_Lehrerhinweise.docx (DS 18–23)
