# SPEC – Algo Quest, Welt 5 „Der Wald“ (Binärbäume, binäre Suchbäume, Transfer)

Grundkonventionen (LIES ZUERST VOLLSTÄNDIG): …/scratchpad/SPEC_AlgoQuest_W0_W1.md; ergänzend SPEC_AlgoQuest_W4.md §0 (VERIFIZIERTE,
NICHT generische Object-API der Niedersachsen-Bibliothek inkl. BinTree – exakt so verwenden, mit Casts) und SPEC_AlgoQuest_W3.md
(Rekursionstiefe: Erstaufruf = Tiefe 0; rekursive Struktogramme nach EH §5).
Scratchpad = /tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad
Vorbilder: /mnt/user-data/outputs/AlgoQuest/Welt0 … Welt4, Werkzeuge, WebApp. Generatoren der Welt 4 wiederverwenden (…/scratchpad/
w4_code inkl. harness/NI.java, w4_ab, w4_pptx, w4_boss) – in eigenen Unterordner …/scratchpad/w5_<name>/ kopieren.
Ausgabe: /mnt/user-data/outputs/AlgoQuest/Welt5/ (Kata/Lehrerhinweise in Werkzeuge/). Andere Welten NICHT verändern.

## 0. BinTree der Online-IDE (verifiziert, Bibliothek „Niedersachsen“)
BinTree(); BinTree(Object o); boolean isEmpty(); Object getItem(); void setItem(Object o); boolean isLeaf();
BinTree getLeft(); BinTree getRight(); void setLeft(BinTree b); void setRight(BinTree b); void setEmpty().
Ein nicht-leerer Baum hat IMMER zwei Teilbäume (ggf. leere Bäume, nie null). getItem/getLeft/getRight/setLeft/setRight auf
leerem Baum → IllegalStateException; setItem(null), setLeft(null) → IllegalArgumentException. setItem auf leerem Baum macht
ihn zum Blatt (mit zwei leeren Teilbäumen). Rekursions-Basisfall daher immer: if (b.isEmpty()).
Casten: int x = (Integer) b.getItem(); String s = (String) b.getItem();
KEINE Knotenklasse, keine hasLeft/hasRight/deleteLeft (alte EWH-Schnittstelle bis 2025!).

Begriffe (überall gleich): Wurzel, Knoten, Blatt, innerer Knoten, Teilbaum, Ebene (Wurzel = Ebene 0), Höhe:
hoehe(leerer Baum) = 0, Blatt = 1, sonst 1 + max(hoehe links, hoehe rechts) (= Anzahl der Ebenen; Abi 2024 A „Tiefe“ als Anzahl
abgefragter Merkmale entspricht dieser Höhe). Traversierungs-Ausgabe als Zeichenkette: jedes Element gefolgt von EINEM Leerzeichen,
z. B. "8 3 1 6 " (rekursiv leicht: item + " " + pre(links) + pre(rechts)); leerer Baum → "".

## 1. Didaktischer Ort
Welt 5 – Der Wald (W11–12, 6 DS). Ziel: BinTree rekursiv nutzen, BST beherrschen, unbekannte Bäume erschließen.
Spielmodule: Akinator-Monsterquiz (Entscheidungsbaum, der lernt), Item-Datenbank (BST nach Item-Nummer).
| DS | Wo | Inhalt | Level | Abi-Bezug |
| 31 | 11 | Baumbegriffe; BinTree nach §4; Bäume von Hand aufbauen (Code ↔ Bild); pre-/in-/postorder; Termbaum | L5.1 | 22N-A a, 25N-A g, 26H-A h |
| 32 | 11 | Rekursive Baumalgorithmen: Knoten, Blätter, Höhe, Summe, Maximum, Sammeln in DynArray, Filtern; rekursives Struktogramm | L5.2 | 23N-A b, 24H-A h/i, 26H-A d |
| 33 (K) | 11 | Entscheidungsbaum als Akinator-Spiel (Baum lernt); Level-Order mit Schlange | L5.3 | 23N-A d, 24H-A g/j, 25N-A e |
| 34 | 12 | BST: Ordnung, Suchen und Einfügen (rekursiv und iterativ), Löschen GRAFISCH in drei Fällen (Blatt, ein Kind, zwei Kinder: Nachfolger = kleinster im rechten Teilbaum oder Vorgänger) | L5.4 | 22H-A a, 23H-A a, 24N-A g–i |
| 35 | 12 | Ausgeglichen vs. entartet; Verdopplung → ein Vergleich mehr; Baum aus sortierter Reihung (Mitte als Wurzel); isBST begründen | L5.4 Experte | 22H-B e, 23H-A d, 24N-A j |
| 36 | 12 | Boss 5 (Transfer-Stationen Max-Heap, Huffman-Baum, B-Baum) | – | 24N-A k/m, 25H-A, 26H-A |

## 2. Online-IDE – EXAKTE API (static-Methoden; alle Materialien identisch!)
Dateien Welt5/AQ_W5_L5_Wald_Geruest.txt + _LSG.txt. Testklassen L51BaumTest, L52RekursivTest, L53AkinatorTest, L54SuchbaumTest;
Präfixe basis_/erweiterung_/experte_. Alle Baum-Methoden REKURSIV (außer wo „iterativ“ steht). Werte in Zahl-Bäumen: Ganzzahlen >= 0.
Hilfsklasse Baumschule (VORGEGEBEN): fertige Testbäume (z. B. Beispielbaum, entarteter Baum, Termbaum "(3+4)*(5-2)", leerer Baum,
einzelnes Blatt) – im LSG-Kopf als ASCII-Bild dokumentieren, damit AB/Kata/Boss sie übernehmen.

class Baum (L5.1, DS 31)
  Basis:       anzahlKnoten(b: BinTree): Ganzzahl
               preorder(b): Zeichenkette;  inorder(b): Zeichenkette;  postorder(b): Zeichenkette   (Format siehe §0)
  Erweiterung: hoehe(b): Ganzzahl;  anzahlBlaetter(b): Ganzzahl;  summe(b: BinTree vom Inhaltstyp Ganzzahl): Ganzzahl
  Experte:     berechne(t: BinTree vom Inhaltstyp Zeichenkette): Ganzzahl → Termbaum: Blätter Ganzzahl-Zeichenketten ("3",
               "12"), innere Knoten "+", "-", "*", "/" (ganzzahlig); Umwandlung Zeichenkette→Ganzzahl selbst per charAt
               (Hilfsmethode zahl(s) ohne Integer.parseInt – EH §1: nur erlaubte String-Operationen!)
               spiegeln(b): nichts → links/rechts in jedem Knoten tauschen (setLeft/setRight)

class Rekursiv (L5.2, DS 32)
  Basis:       enthaelt(b, x: Ganzzahl): Wahrheitswert   (beliebiger Baum, kein BST)
               maximum(b): Ganzzahl                       → −1 bei leerem Baum
               anzahlGroesser(b, grenze: Ganzzahl): Ganzzahl
  Erweiterung: sammleInorder(b): DynArray                → neue DynArray mit allen Werten in Inorder-Reihenfolge
               blaetter(b): DynArray                      → Blattwerte von links nach rechts
               anzahlAufEbene(b, ebene: Ganzzahl): Ganzzahl → Wurzel = Ebene 0
  Experte:     pfadZu(b, x: Ganzzahl): Zeichenkette       → Weg von der Wurzel als Folge von 'L'/'R' zum ERSTEN Vorkommen in Preorder;
                                                           Wurzel → ""; nicht vorhanden → "-"
               istGleich(a: BinTree, b: BinTree): Wahrheitswert → gleiche Struktur und gleiche Werte

class Akinator (L5.3, DS 33 Kür) – Objekt-Klasse: Entscheidungsbaum mit Zeichenketten; innere Knoten = Ja/Nein-Fragen,
  Blätter = Monsternamen; ja → linker Teilbaum, nein → rechter Teilbaum.
  - baum: BinTree   + c Akinator(start: Zeichenkette)   → Baum mit einem Blatt (Monstername)
  + getBaum(): BinTree
  + raten(antworten: Zeichenkette): Zeichenkette → geht von der Wurzel gemäß 'j'/'n' (je Zeichen ein Schritt) bis zu einem Blatt;
                                                    liefert dessen Namen; zu wenige Antworten → "?" ; überzählige werden ignoriert
  + lernen(antworten: Zeichenkette, neu: Zeichenkette, frage: Zeichenkette, jaFuerNeu: Wahrheitswert): nichts
        → das über antworten erreichte Blatt (Name alt) wird zum Frageknoten frage; Kinder: neu und alt (neu links, wenn jaFuerNeu)
  + anzahlMonster(): Ganzzahl (Blätter);  + anzahlFragen(): Ganzzahl (innere Knoten)
  + static levelorder(b: BinTree): Zeichenkette → ebenenweise mit Schlange (Queue von BinTree), Format wie §0

class Suchbaum (L5.4, DS 34–35) – BST mit Ganzzahlen: links < Wurzel < rechts, Duplikate werden ignoriert
  Basis:       suche(b, x: Ganzzahl): Wahrheitswert       → rekursiv, nur EIN Teilbaum je Schritt
               minimum(b): Ganzzahl                       → −1 bei leerem Baum (immer links)
               einfuegen(b, x: Ganzzahl): nichts          → rekursiv; leerer Baum: setItem(x); Duplikat: nichts tun
  Erweiterung: sucheIterativ(b, x): Wahrheitswert         → mit Schleife
               vergleiche(b, x: Ganzzahl): Ganzzahl       → Anzahl der untersuchten (nicht-leeren) Knoten bis gefunden bzw. bis leer
               baueAus(r: Reihung von Ganzzahl): BinTree  → neuer BST, Werte in Reihenfolge eingefügt
  Experte:     istBST(b): Wahrheitswert                   → mit Grenzen (Hilfsmethode istBST(b, min, max)), nicht nur Kinder prüfen!
               ausgeglichenAus(sortiert: Reihung von Ganzzahl): BinTree → Mitte als Wurzel: mitte = (lo + hi) / 2, rekursiv
               nachfolger(b, x: Ganzzahl): Ganzzahl       → kleinster Wert > x im BST, −1 wenn keiner (Vorbereitung Löschen)

## 3. Grafik-Gerüst „Baumzeichner“ (Pflicht, Sichtprüfung in der IDE)
Welt5/AQ_W5_Baumzeichner_Geruest.txt + _LSG.txt: zeichnet einen BinTree in der World (Kreise + Linien + Text, Ebenen untereinander,
x-Position nach Inorder-Index oder Halbierungsverfahren), Hervorheben von Knoten (Farbe) mit SystemTools.setSpeed für
Traversierungs-Animation (pre/in/post/level), BST-Einfüge-Animation (Suchweg einfärben), Item-Datenbank-Demo. Grafik-API nur wie in
den bisherigen Grafik-Gerüsten (Welt 2/3) bzw. per learnj-Doku bestätigt (Circle, Line, Text, Rectangle, setFillColor,
setBorderColor, destroy). Schüler-TODOs: z. B. Hervorheben in Preorder selbst schreiben, Suchweg einfärben.

## 4. Boss 5 (DS 36) – Transfer-Stationen
„Die drei Baumhüter“ (oder ähnlich): drei Stationen mit je ≈ 12 BE und eigenem Material zu einer UNBEKANNTEN Baumart; die Prüflinge
bearbeiten 2 von 3 Stationen in 60 min (24 BE). Station A Max-Heap (Ordnung erkennen, Heap angeben, sink/Einfügen von Hand, Vergleich
mit BST, rekursives Struktogramm isMaxHeap – angelehnt an Abi 2026 A, aber eigene Daten), Station B Huffman-Baum (Baum nach Verfahren
aufbauen, codieren/decodieren, Präfixfreiheit begründen, decodiere implementieren – Abi 2025 A, eigene Daten), Station C B-Baum
(Ordnungsprinzip beschreiben, Einfügen mit Split angeben, Suchaufwand abschätzen – Abi 2024 N-A k/m, eigene Daten). Materialien
enthalten alle nötigen Definitionen. Mindestens eine Implementierung auf BinTree (Papier-Compiler, Testklasse im EH-Anhang).
AFB je Station ≈ 30/53/17 %.

## 5. Kata-Karten Welt 5
Werkzeuge/kata_w5.json ("welt": 5, ids W5-01…, 12–14 Karten) + Werkzeuge/AQ_Kata-Karten_W5.docx. Themen: Baum aus Code zeichnen,
Traversierungen angeben, Baum aus pre+inorder rekonstruieren, Termbaum ↔ Term, Höhe/Blätter rekursiv (Rekursionstabelle), Basisfall
isEmpty vergessen → Exception, BST einfügen/zeichnen, BST suchen (Vergleiche), Löschen (drei Fälle, grafisch), entartet vs. ausgeglichen
(Verdopplung), isBST-Falle (nur Kinder prüfen), Level-Order-Trace mit Schlange, Methodenkopf mit BinTree-Typen, Casten.

## 6. Dateinamen Welt 5
Welt5/AQ_W5_Wald.pptx
Welt5/AQ_W5_AB1_Binaerbaeume.docx + AQ_W5_AB1_LSG.docx            (DS 31–33: L5.1–L5.3)
Welt5/AQ_W5_AB2_Suchbaeume.docx + AQ_W5_AB2_LSG.docx              (DS 34–35: L5.4)
Welt5/AQ_W5_AB3_Transfer_unbekannte_Baeume.docx + AQ_W5_AB3_LSG.docx (Vorbereitung DS 36: Strategie „unbekannte Struktur erschließen“
     an einer vierten Baumart, z. B. Trie/Präfixbaum oder Entscheidungsbaum mit Gewichten – NICHT Heap/Huffman/B-Baum)
Welt5/AQ_W5_L5_Wald_Geruest.txt + _LSG.txt · Welt5/AQ_W5_Baumzeichner_Geruest.txt + _LSG.txt
Welt5/AQ_W5_Boss5_<Kontext>.docx + Welt5/AQ_W5_Boss5_Erwartungshorizont.docx
Werkzeuge/kata_w5.json · Werkzeuge/AQ_Kata-Karten_W5.docx · Werkzeuge/AQ_W5_Lehrerhinweise.docx (DS 31–36)

## 7. Baumschule – VERBINDLICHE Testbäume (alle Materialien verwenden GENAU diese Bäume und Werte)
Klasse Baumschule (vorgegeben im Gerüst, static-Methoden, liefern jeweils einen NEUEN Baum):
beispielBST(): BinTree  – BST durch Einfügen von 8, 3, 10, 1, 6, 14, 4, 7, 13
            8
          /   \
         3     10
        / \      \
       1   6      14
          / \    /
         4   7  13
   pre "8 3 1 6 4 7 10 14 13 " · in "1 3 4 6 7 8 10 13 14 " · post "1 4 7 6 3 13 14 10 8 " · level "8 3 10 1 6 14 4 7 13 "
   Knoten 9, Höhe 4, Blätter 4 (1 4 7 13), Summe 66, Minimum 1, Maximum 14.
   vergleiche(…, 7) = 4 (8,3,6,7); vergleiche(…, 5) = 4 (8,3,6,4 → leer); nachfolger(…, 8) = 10; nachfolger(…, 7) = 8; nachfolger(…, 14) = −1.
zahlenbaum(): BinTree  – KEIN BST, Duplikat 9
            5
          /   \
         9     4
        / \     \
       2   7     9
                /
               1
   pre "5 9 2 7 4 9 1 " · in "2 9 7 5 4 1 9 " · post "2 7 9 1 9 4 5 " · level "5 9 4 2 7 9 1 "
   Knoten 7, Höhe 4, Blätter 3 (2 7 1), Summe 37, Maximum 9, anzahlGroesser(…, 4) = 4 (5 9 7 9);
   anzahlAufEbene 0→1, 1→2, 2→3, 3→1, 4→0; pfadZu 5→"", 9→"L", 7→"LR", 1→"RRL", 8→"-".
entartet(): BinTree  – BST durch Einfügen von 1, 2, 3, 4, 5 (rechte Kette), Höhe 5.
termbaum(): BinTree  – "(3+4)*(5-2)": Wurzel "*", links "+" (3, 4), rechts "-" (5, 2)
   pre "* + 3 4 - 5 2 " · in "3 + 4 * 5 - 2 " · post "3 4 + 5 2 - * " · Wert 21.
monsterquiz(): BinTree  – Akinator-Startbaum (ja = links, nein = rechts)
   "Kann es fliegen?"  → j: "Speit es Feuer?" (j: "Drache", n: "Greif")
                       → n: "Lebt es im Wasser?" (j: "Kraken", n: "Troll")
   raten "jj" Drache, "jn" Greif, "nj" Kraken, "nn" Troll, "j" → "?", "nnj" → Troll. 4 Monster, 3 Fragen.
leer(): BinTree – leerer Baum;  blatt(x: Ganzzahl): BinTree – einzelnes Blatt.
Zusätzlich Konstruktor Akinator(start) wie §2 (ein Blatt); Akinator mit monsterquiz-Baum über Hilfskonstruktor NICHT nötig –
Tests bauen per lernen() auf oder setzen den Baum über einen zweiten Konstruktor Akinator(b: BinTree) (vorgegeben im Gerüst).
