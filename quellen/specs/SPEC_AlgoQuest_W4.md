# SPEC – Algo Quest, Welt 4 „Der Hafen“ (Stapel, Schlange, dynamische Reihung)

Grundkonventionen (LIES ZUERST VOLLSTÄNDIG): …/scratchpad/SPEC_AlgoQuest_W0_W1.md; ergänzend SPEC_AlgoQuest_W3.md
(Arbeitsweise, Generatoren, Rekursionstiefe Erstaufruf = 0) und SPEC_AlgoQuest_W0_Akademie.md (DS-Zählung).
Scratchpad = /tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad
Vorbilder: /mnt/user-data/outputs/AlgoQuest/Welt0 … Welt3, Werkzeuge, WebApp. Generatoren der Welt 3 wiederverwenden
(…/scratchpad/w3_code, w3_ab, w3_pptx, w3_boss) – in eigenen Unterordner …/scratchpad/w4_<name>/ kopieren.
Ausgabe: /mnt/user-data/outputs/AlgoQuest/Welt4/ (Kata/Lehrerhinweise in Werkzeuge/). Andere Welten NICHT verändern.

## 0. VERIFIZIERT: Niedersachsen-Bibliothek der Online-IDE (API-Doku online-ide.de, Stand 10/2026)
Aktivieren: Workspace rechtsklicken → „Einstellungen“ → Häkchen „Niedersachsen“. Dann sind java.util Stack, Queue, Deque,
LinkedList, ArrayList, Vector AUSGEBLENDET. Die Klassen sind NICHT generisch, Inhalt ist Object:
  class Stack  : Stack(); boolean isEmpty(); Object top(); void push(Object pContent); Object pop()
                 top/pop auf leerem Stapel → IllegalStateException; push(null) → IllegalArgumentException
  class Queue  : Queue(); boolean isEmpty(); Object head(); void enqueue(Object neu); Object dequeue()
                 head/dequeue auf leerer Schlange → IllegalStateException
  class DynArray implements Iterable<Object>: DynArray(); boolean isEmpty(); Object getItem(int index);
                 void append(Object x); void insertAt(int index, Object x); void setItem(int index, Object x);
                 void delete(int index); int getLength(); (for-each möglich: for (Object o : d))
                 append(null) → IllegalArgumentException; ungültiger Index → IndexOutOfBoundsException;
                 insertAt(getLength(), x) hängt an.
  class BinTree: BinTree(); BinTree(Object o); boolean isEmpty(); Object getItem(); void setItem(Object o);
                 boolean isLeaf(); BinTree getLeft(); BinTree getRight(); void setLeft(BinTree b); void setRight(BinTree b);
                 void setEmpty()   (Zugriffe auf leeren Baum → IllegalStateException)
FOLGEN für allen Code: KEINE Generics (`Stack s = new Stack();`), Rückgaben casten:
  Kiste k = (Kiste) s.pop();   int x = (Integer) q.dequeue();   char c = (Character) s.pop();
  Zahlen werden automatisch geboxt (s.push(5)). Vergleich von Inhalten: Objekte über Getter, Zeichenketten mit equals.
  → im Gerüst/LSG und auf ABs einen Infokasten „Casten bei Abitur-Klassen“; „vor Einsatz prüfen“: (Integer)-Cast + Unboxing,
    (Character)-Cast, for-each über DynArray in der echten IDE.
Für die Java-21-Verifikation im Harness: exakte Nachbauten dieser vier Klassen (Object-basiert, gleiche Exceptions) als Stubs.
Notation in Signaturen/Struktogrammen (EH §5): „Stapel vom Inhaltstyp Kiste“, „Schlange vom Inhaltstyp Ganzzahl“,
„dynamische Reihung vom Inhaltstyp Kiste“. Laufzeitfehler MÜSSEN durch explizite Abfragen ausgeschlossen werden (EH §4) –
das ist in Welt 4 das zentrale Abi-Check-Thema („Leer? Index?“).

## 1. Didaktischer Ort
Welt 4 – Der Hafen (W8–10, 7 DS). Ziel: Die drei linearen ADTs exakt nach §4 nutzen, ohne Laufzeitfehler. Spielmodule:
Undo/Redo (Stapel), Zugreihenfolge/Initiative (Schlange), Ladeliste/Inventar (DynArray). Hafen-Story: Kisten werden gestapelt,
Schiffe warten in der Schlange, die Ladeliste ist eine dynamische Reihung.
| DS | Wo | Inhalt | Level | Abi-Bezug |
| 24 | 8 | ADT-Begriff (Schnittstelle vs. Implementierung), Stack/Queue nach §4, Bibliothek aktivieren, Casten, Befehlsfolgen und Mischaufgaben tracen (Zustand skizzieren), Checkliste „Leer? Index?“ | L4.1 | 22N-B a, 24H-B e |
| 25 (K) | 9 | Spielmodule Undo/Redo-Stapel und Initiative-Schlange; Eignung einer Struktur beurteilen | L4.2 | 24N-B b, 26H-B f |
| 26 | 9 | Muster „unverändert lassen“: Hilfsstapel, Schlange über Hilfsschlange bzw. rotieren; Umkehren; Durchschnitt/Maximum über Schlange | L4.3 | 23H-C c, 25H-B b, 25N-B l, 26H-B e |
| 27 | 9 | DynArray nach §4: sortiert einfügen, Einfügesortierung, Minimum suchen und entfernen, Duplikate | L4.4 | 24H-B g, 25N-A l, 26H-B b |
| 28 | 10 | Umformen zwischen ADTs; Klammerprüfung, Postfix-Rechner mit Stapel | L4.5 | 22N-A c/d, 23H-B c, 25N-B b/c |
| 29 (K) | 10 | Iterativer Flood-Fill mit Schlange vs. Stapel (gleiche Anzahl, andere Reihenfolge); Aufwand Queue vs. DynArray; Expertenpfad: eigener Stapel mit Knotenklasse | L4.6 | 22H-B b, 22H-C d, 22N-C c |
| 30 | 10 | Boss 4 | – | 25N-B b–d, l |

## 2. Online-IDE – EXAKTE API (static-Methoden; alle Materialien identisch!)
Dateien Welt4/AQ_W4_L4_Hafen_Geruest.txt + _LSG.txt. Testklassen L41StapelSchlangeTest, L42SpielmoduleTest, L43UnveraendertTest,
L44LadelisteTest, L45UmformenTest, L46ExpertenpfadTest; Präfixe basis_/erweiterung_/experte_. Leer-Abfragen sind Pflicht
(Tests prüfen leere Strukturen). „unverändert“ heißt: gleiche Elemente (dieselben Objekte) in gleicher Reihenfolge.

class Kiste – - name: Zeichenkette; - gewicht: Ganzzahl; + c Kiste(name, gewicht); + getName(); + getGewicht();
              + beschreibung(): Zeichenkette → name + " (" + gewicht + " kg)"      (VORGEGEBEN)

class Hafen (L4.1, DS 24)
  Basis:       stapleAuf(werte: Reihung von Ganzzahl): Stapel     → push in Reihenfolge, letzter Wert oben
               obersterWert(s: Stapel vom Inhaltstyp Ganzzahl): Ganzzahl → −1 bei leerem Stapel (top, nicht pop)
               leeren(s: Stapel): Ganzzahl                         → entnimmt alles, gibt Anzahl zurück
  Erweiterung: warteschlange(namen: Reihung von Zeichenkette): Schlange → enqueue in Reihenfolge
               naechster(q: Schlange vom Inhaltstyp Zeichenkette): Zeichenkette → dequeue; "" bei leerer Schlange
               alleAbfertigen(q): Zeichenkette                     → alle entnehmen, mit ", " verbunden ("A, B, C"); leer → ""
  Experte:     umkehren(q: Schlange): nichts                       → Reihenfolge umkehren mithilfe eines Stapels
               stapelUmdrehen(s: Stapel): Stapel                   → NEUER Stapel mit umgekehrter Reihenfolge; s ist danach leer

class Zugbuch (L4.2, DS 25 Kür) – Undo/Redo, Objekt-Klasse:
  - erledigt: Stapel; - rueckgaengig: Stapel   + c Zugbuch()
  + zug(z: Zeichenkette): nichts          → push auf erledigt; leert den Redo-Stapel
  + rueckgaengig(): Zeichenkette          → letzter Zug von erledigt nach rueckgaengig, Rückgabe des Zugs; "" wenn nichts da
  + wiederholen(): Zeichenkette           → zurück nach erledigt; "" wenn nichts da
  + anzahlZuege(): Ganzzahl               → Anzahl in erledigt (erledigt bleibt unverändert)
class Initiative (L4.2) – Rundenreihenfolge:
  - reihe: Schlange   + c Initiative()
  + beitreten(name: Zeichenkette): nichts
  + amZug(): Zeichenkette                → vorderster wird entnommen, hinten wieder angestellt, Rückgabe sein Name; "" wenn leer
  + ausscheiden(name: Zeichenkette): Wahrheitswert → entfernt erstes Vorkommen, Reihenfolge der übrigen bleibt; false wenn nicht da

class Unveraendert (L4.3, DS 26) – ALLE Methoden lassen die übergebenen Strukturen unverändert!
  Basis:       zaehle(s: Stapel): Ganzzahl                       (Hilfsstapel)
               summe(q: Schlange vom Inhaltstyp Ganzzahl): Ganzzahl (Hilfsschlange)
  Erweiterung: enthaelt(s: Stapel vom Inhaltstyp Kiste, name: Zeichenkette): Wahrheitswert
               durchschnittsGewicht(q: Schlange vom Inhaltstyp Kiste): Kommazahl  → 0.0 bei leerer Schlange
               schwerste(s: Stapel vom Inhaltstyp Kiste): Kiste    → null bei leerem Stapel; bei Gleichstand die oberste
  Experte:     unterste(s: Stapel vom Inhaltstyp Kiste): Kiste     → null bei leerem Stapel
               entferneAlle(q: Schlange vom Inhaltstyp Kiste, name: Zeichenkette): Ganzzahl → AUSNAHME: verändert q –
                                                                   entfernt alle Kisten mit name, Reihenfolge der übrigen bleibt; Anzahl

class Ladeliste (L4.4, DS 27) – auf DynArray vom Inhaltstyp Kiste:
  Basis:       gesamtGewicht(d): Ganzzahl;  indexVon(d, name: Zeichenkette): Ganzzahl (erstes, sonst −1);
               leichteste(d): Kiste (null bei leer, erste bei Gleichstand)
  Erweiterung: einfuegenSortiert(d, k: Kiste): nichts               → d aufsteigend nach Gewicht; k hinter gleich schwere
               entferneLeichteste(d): Kiste                        → entfernt und liefert die leichteste (erste bei Gleichstand); null bei leer
               entferneDuplikate(d): nichts                        → gleicher Name: erstes Vorkommen bleibt, Reihenfolge bleibt
  Experte:     einfuegesortierung(d): nichts                        → aufsteigend nach Gewicht, stabil, nur mit getItem/setItem/insertAt/delete
               abspalten(d, grenze: Ganzzahl): DynArray             → neue Reihung mit allen Kisten gewicht > grenze (Reihenfolge
                                                                   bleibt), diese werden aus d entfernt

class Umformen (L4.5, DS 28)
  Basis:       schlangeZuDynArray(q: Schlange): DynArray            → q bleibt unverändert, Reihenfolge = Schlangenreihenfolge
               dynArrayZuStapel(d: DynArray): Stapel                → Element 0 zuerst gepusht (letztes oben)
  Erweiterung: klammernOk(s: Zeichenkette): Wahrheitswert          → '(' '[' '{' mit Stapel; andere Zeichen ignorieren
  Experte:     postfix(ausdruck: Zeichenkette): Ganzzahl            → einstellige Operanden, Operatoren + - * ohne Leerzeichen,
                                                                   z. B. "34+2*" = 14; Ausdruck gültig vorausgesetzt
               nachGewicht(q: Schlange vom Inhaltstyp Kiste, grenze: Ganzzahl): DynArray → Kisten <= grenze in neuer DynArray
                                                                   (Reihenfolge), q bleibt unverändert

class Expertenpfad (L4.6, DS 29 Kür)
  fluteIterativ(karte: Reihung von Reihung von Zeichen, z: Ganzzahl, s: Ganzzahl, mitSchlange: Wahrheitswert): Ganzzahl
     → wie lueften aus Welt 3 ('.'/'S'/'Z' begehbar, '.' → '+'), aber iterativ mit Schlange (true) oder Stapel (false) von
       Positionen (Positionen als Reihung {z, s} oder Ganzzahl z * 1000 + s – festlegen und dokumentieren); Rückgabe Anzahl
       markierter '.'-Felder; Ergebnis-Karte gleich, Reihenfolge verschieden (Test prüft beides gegen festgelegte Werte)
  class Knoten (- inhalt: Object, - naechster: Knoten, c Knoten(inhalt, naechster), Getter/Setter) und
  class MeinStapel (isEmpty, push, top, pop – gleiches Verhalten wie Stack inkl. IllegalStateException bei leer); Tests
  vergleichen MeinStapel mit Stack in zufälligen Befehlsfolgen (fester Seed, eigener LCG).

## 3. Grafik/Spiel
Optional, nur wenn Zeit: Welt4/AQ_W4_Hafen_Visual_Geruest.txt – Visualisierung von Stapel und Schlange (Kisten als Rechtecke),
Befehle per Tastatur oder Hauptprogramm, nach jedem Befehl neu gezeichnet. Nicht Pflicht.

## 4. Boss 4 (DS 30) – neuer Kontext (Transfer), z. B. „Die Fähre von Nebelhafen“ oder „Postkutschenstation“
≈ 24 BE, 60 min, AFB ≈ 30/53/17 %. Teilaufgaben-Typen: Befehlsfolge auf Stapel/Schlange ausführen und Zustände angeben (Mischaufgabe);
Eignung Stapel vs. Schlange vs. DynArray beurteilen; Methode implementieren, die einen Stapel/eine Schlange auswertet und UNVERÄNDERT
zurücklässt (mit Leerabfragen; Papier-Compiler); Struktogramm entwickeln zu DynArray (sortiert einfügen oder Minimum entfernen);
gegebenen Algorithmus mit Schlange tracen und Funktionsweise erläutern; Fehler finden (pop/top ohne Leerabfrage, Struktur nicht
wiederhergestellt, Index-Fehler bei delete in Vorwärtsschleife). Material mit Klassenkarten (EH §6) und Hinweis auf die
ADT-Schnittstellen (Hilfsmittel EH).

## 5. Kata-Karten Welt 4
Werkzeuge/kata_w4.json ("welt": 4, ids W4-01…, 12–14 Karten, bisherige Kategorien) + Werkzeuge/AQ_Kata-Karten_W4.docx.
Themen: Befehlsfolgen Stack/Queue/DynArray (Zustand), Mischaufgabe stapel.push(schlange.dequeue()), Leer-Abfrage vergessen,
Hilfsstapel-Muster, Rotieren, Umkehren, delete in Vorwärtsschleife (Index-Fehler), sortiert einfügen in DynArray, Klammerprüfung-Trace,
Postfix-Trace, Eignung beurteilen, Casten (Object → Kiste/Integer), Methodenkopf mit ADT-Typen.

## 6. Dateinamen Welt 4
Welt4/AQ_W4_Hafen.pptx
Welt4/AQ_W4_AB1_Stapel_und_Schlange.docx + AQ_W4_AB1_LSG.docx                 (DS 24–25: L4.1, L4.2)
Welt4/AQ_W4_AB2_Unveraendert_und_DynArray.docx + AQ_W4_AB2_LSG.docx           (DS 26–27: L4.3, L4.4)
Welt4/AQ_W4_AB3_Umformen_und_Anwendungen.docx + AQ_W4_AB3_LSG.docx            (DS 28–29: L4.5, L4.6)
Welt4/AQ_W4_L4_Hafen_Geruest.txt + _LSG.txt
Welt4/AQ_W4_Boss4_<Kontext>.docx + Welt4/AQ_W4_Boss4_Erwartungshorizont.docx
Werkzeuge/kata_w4.json · Werkzeuge/AQ_Kata-Karten_W4.docx · Werkzeuge/AQ_W4_Lehrerhinweise.docx (DS 24–30)
