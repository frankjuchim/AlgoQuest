# Boss 0 – Aufnahmepruefung: Die Bibliothek der Akademie (Pool, 15 eigene Aufgaben)
from lib import *

KONTEXT = "Die Bibliothekarin der Akademie verwaltet die Ausleihzahlen der Zauberbücher in Reihungen. Alle Operationen sind Klassenoperationen (`public static`)."

# ================================================================ Stufe 1
EXPR1 = [("e1", "(double) 17 / 4"), ("e2", "17 / 4 * 2.0"), ("e3", "\"S\" + 2 * 3"), ("e4", "9 % 4 + 9 / 4")]

def b01(t):
    o, _ = jrun("", "".join(f'out("t{k[1:]}", typ({e})); out("w{k[1:]}", {e});' for k, e in EXPR1))
    for g, v in o.items(): expect(t, g, v)

T("W0-B-01", "Die Rechentafel am Eingang", 1, "Datentypen und Ausdrücke", ["P4"],
  [txt("Geben Sie zu jedem Ausdruck den Typ und den Wert an (Zeichenketten ohne Anführungszeichen)."),
   tab(["Ausdruck", "Typ", "Wert"], [[f"`{e}`", f"[[t{k[1:]}]]", f"[[w{k[1:]}]]"] for k, e in EXPR1])],
  gaps({**{f"t{i}": fa(TYPEN) for i in range(1, 5)}, "w1": fz(), "w2": fz(), "w3": ft(6), "w4": fz()}),
  {"t1": ["double"], "w1": ["4.25"], "t2": ["double"], "w2": ["8.0"], "t3": ["String"], "w3": ["S6", "\"S6\""], "t4": ["int"], "w4": ["3"]},
  [txt("(double) 17 / 4: erst umwandeln, dann teilen → 4.25. 17 / 4 ist ganzzahlig 4, mal 2.0 → 8.0. Punkt vor Strich: 2 * 3 = 6, dann "
       "\"S\" + 6 → \"S6\". 9 % 4 = 1 und 9 / 4 = 2 → 3."), hin("Falle **P4**: ganzzahlige Division und Typ des Ergebnisses.")],
  check=b01)

OPT2 = [("a", "public static double mahngebuehr(int tage, boolean vip)"), ("b", "public static double mahngebuehr(int tage, vip)"),
        ("c", "public static int mahngebuehr(int tage, boolean vip)"), ("d", "public static double mahngebuehr(boolean vip, int tage)"),
        ("e", "public static void mahngebuehr(int tage, boolean vip): double")]

def b02(t):
    good = []
    for k, h in OPT2:
        ok, _ = jcompile(h + " { return 1.5; }", "double g = mahngebuehr(3, true);")
        if ok: good.append(k)
    assert good == t["loesung"]["richtig"], good

T("W0-B-02", "Die Mahngebühr", 1, "Methodenkopf und Signatur", ["P3"],
  [txt("Die Operation `mahngebuehr(tage: Ganzzahl, vip: Wahrheitswert): Kommazahl` berechnet die Gebühr für eine verspätete Rückgabe. "
       "Welcher Java-Methodenkopf ist korrekt?")],
  choice([(k, f"`{h}`") for k, h in OPT2]),
  {"richtig": ["a"]},
  [txt("Rückgabetyp Kommazahl → `double` vor dem Namen; Parameter in derselben Reihenfolge, jeder mit Typ: `int tage, boolean vip`."),
   hin("Falle **P3**: Signatur verfehlt (Typ fehlt, Reihenfolge vertauscht, falscher Rückgabetyp).")],
  check=b02)

H3 = [("h1", "public static int[] ausleihenVon(String[] titel, String autor)", "s1"),
      ("h2", "public static void sortiere(String[] titel)", "s2"),
      ("h3", "public static char kennung(String titel, int nr)", "s3")]
S3 = [("s1", "ausleihenVon(titel: Reihung von Zeichenkette, autor: Zeichenkette): Reihung von Ganzzahl"),
      ("s2", "sortiere(titel: Reihung von Zeichenkette): nichts"),
      ("s3", "kennung(titel: Zeichenkette, nr: Ganzzahl): Zeichen"),
      ("s4", "kennung(titel: Zeichenkette, nr: Ganzzahl): Zeichenkette")]

def b03(t):
    J = {"Ganzzahl": "int", "Zeichen": "char", "Zeichenkette": "String", "nichts": "void"}
    def tj(x): return J[x[len("Reihung von "):]] + "[]" if x.startswith("Reihung von ") else J[x]
    sigs = dict(S3)
    for h, kopf, _s in H3:
        name, rest = sigs[t["loesung"][h]].split("(", 1); params, ret = rest.rsplit("): ", 1)
        ps = ", ".join(f"{tj(p.split(': ')[1])} {p.split(': ')[0]}" for p in params.split(", "))
        assert f"public static {tj(ret)} {name}({ps})" == kopf

T("W0-B-03", "Der Katalog der Operationen", 1, "Methodenkopf und Signatur", ["P3"],
  [txt("Ordnen Sie jedem Java-Methodenkopf die Signatur in Abi-Notation zu. Eine Signatur bleibt übrig.")],
  match([(h, f"`{k}`") for h, k, _s in H3], [(s, f"`{v}`") for s, v in S3]),
  {h: s for h, _k, s in H3},
  [txt("`int[]` → Reihung von Ganzzahl, `String[]` → Reihung von Zeichenkette, `void` → nichts, `char` → Zeichen. "
       "Die übrige Signatur hat den Rückgabetyp Zeichenkette – dazu gibt es keinen Kopf.")],
  check=b03)

LEIHEN = '''public static void leihen(int[] bestand, int i, int anzahl) {
    bestand[i] = bestand[i] - anzahl;
    anzahl = 0;
}
// Hauptprogramm
int[] b = {5, 2, 8};
int n = 3;
leihen(b, 2, n);
println(b[2] + " " + n);'''

def b04(t):
    meth, main = LEIHEN.split("// Hauptprogramm\n")
    o, ls = jrun(meth, main)
    x, y = ls[0].split(); expect(t, "g1", x); expect(t, "g2", y)

T("W0-B-04", "Die Ausleihe", 1, "Objektkarten und Referenzen", [],
  [txt(KONTEXT), code(LEIHEN), txt("Geben Sie die Ausgabe an: [[g1]] [[g2]]")],
  gaps({"g1": fz(), "g2": fz()}),
  {"g1": ["5"], "g2": ["3"]},
  [txt("`bestand` erhält eine Kopie der **Referenz** – die Änderung an `bestand[2]` (8 − 3 = 5) ist in `b` sichtbar. `anzahl` erhält eine "
       "Kopie der **Zahl** 3; `anzahl = 0` ändert nur die lokale Kopie, `n` bleibt 3.")],
  check=b04)

LETZT = '''public static int letzterIndex(int[] r, int x) {
    int i = r.length - 1;
    while (i >= 0 && r[i] != x) {
        i--;
    }
    return i;
}'''

def b05(t):
    o, ls = jrun(LETZT.replace("while (i >= 0 && r[i] != x) {", 'while (i >= 0 && lies(r, i) != x) {') +
                 '\nstatic int lies(int[] r, int i) { System.out.println("idx=" + i); return r[i]; }',
                 'out("ret", letzterIndex(new int[]{4, 7, 3, 7, 1}, 3));')
    assert [int(l[4:]) for l in ls if l.startswith("idx=")] == t["loesung"]["folge"]
    assert o["ret"] == "2"

T("W0-B-05", "Die Suche im Regal", 1, "Sortieren und Suchen", ["P1"],
  [code(LETZT), txt("Klicken Sie die Indizes in der Reihenfolge an, in der `r[i]` beim Aufruf `letzterIndex({4, 7, 3, 7, 1}, 3)` gelesen wird.")],
  arr([4, 7, 3, 7, 1], "klick"),
  {"folge": [4, 3, 2]},
  [txt("Die Suche beginnt hinten bei Index 4 (Wert 1), dann Index 3 (Wert 7), dann Index 2 (Wert 3) – Treffer, die Schleife endet. Rückgabe 2. "
       "Dank `i >= 0 &&` wird bei fehlendem Wert nie `r[-1]` gelesen (Falle **P1**).")],
  check=b05)

# ================================================================ Stufe 2
GEB = '''public static int gebuehr(int tage) {
    if (tage <= 7) {
        return 0;
    }
    return (tage - 7) / 3 + 1;
}
public static int gesamt(int[] tage) {
    int s = 0;
    for (int t : tage) {
        s = s + gebuehr(t);
    }
    return s;
}'''

def b06(t):
    inst = GEB.replace("        s = s + gebuehr(t);", '        int rv = gebuehr(t);\n        s = s + rv;\n        System.out.println("row=" + rv + ";" + s);')
    o, ls = jrun(inst, 'out("ret", gesamt(new int[]{5, 10, 7, 15}));')
    rows = [l[4:].split(";") for l in ls if l.startswith("row=")]
    for k, (rv, s) in enumerate(rows):
        expect(t, f"r{k+1}", rv); expect(t, f"s{k+1}", s)
    expect(t, "ret", o["ret"])

T("W0-B-06", "Mahngebühren protokollieren", 2, "Tracetabelle", ["P8", "P4"],
  [txt(KONTEXT + " Die Gebühr hängt von den Tagen der Ausleihe ab."), code(GEB),
   txt("Dokumentieren Sie den Aufruf `gesamt({5, 10, 7, 15})` (Werte am Ende jedes Durchlaufs) und geben Sie den Rückgabewert an."),
   tab(["t", "Aufruf", "Rückgabe von gebuehr", "s"], [["vor der Schleife", "–", "–", "0"],
       ["5", "gebuehr(5)", "[[r1]]", "[[s1]]"], ["10", "gebuehr(10)", "[[r2]]", "[[s2]]"],
       ["7", "gebuehr(7)", "[[r3]]", "[[s3]]"], ["15", "gebuehr(15)", "[[r4]]", "[[s4]]"]]),
   txt("Rückgabewert: [[ret]]")],
  gaps({**{f"{c}{k}": fz() for c in "rs" for k in range(1, 5)}, "ret": fz()}),
  {"r1": ["0"], "s1": ["0"], "r2": ["2"], "s2": ["2"], "r3": ["0"], "s3": ["2"], "r4": ["3"], "s4": ["5"], "ret": ["5"]},
  [txt("Bis 7 Tage ist die Ausleihe gebührenfrei (auch genau 7). gebuehr(10) = 3 / 3 + 1 = 2, gebuehr(15) = 8 / 3 + 1 = 2 + 1 = 3 "
       "(ganzzahlige Division). Summe 0 + 2 + 0 + 3 = 5."), hin("Fallen **P8** (vollständige Tabelle) und **P4** (8 / 3 = 2).")],
  check=b06)

ERST = '''public static int erstesNull(int[] r) {
    int i = 0;
    while (r[i] != 0 && i < r.length) {
        i++;
    }
    if (i == r.length) {
        return -1;
    }
    return i;
}'''
OPT7 = ["i < r.length && r[i] != 0", "r[i] != 0 || i < r.length", "i <= r.length && r[i] != 0", "r[i] == 0 && i < r.length"]

def b07(t):
    o, _ = jrun(ERST, '''out("g2", erstesNull(new int[]{4, 0, 2}));
        try { out("g3", erstesNull(new int[]{4, 2})); } catch (ArrayIndexOutOfBoundsException e) { out("g3", "ArrayIndexOutOfBoundsException"); }''')
    expect(t, "g2", o["g2"], 1); expect(t, "g3", o["g3"], 1)
    good = []
    for opt in OPT7:
        src = ERST.replace("r[i] != 0 && i < r.length", opt)
        o, _ = jrun(src, '''String s = ""; int[][] f = {{4, 0, 2}, {4, 2}, {}, {0}, {3, 3, 0}};
            for (int[] r : f) { try { s += erstesNull(r) + ","; } catch (ArrayIndexOutOfBoundsException e) { s += "X,"; } } out("s", s);''')
        if o["s"] == "1,-1,-1,0,2,": good.append(opt)
    assert good == t["loesung"][1]["g1"], good

T("W0-B-07", "Das erste unberührte Buch", 2, "Fehler im Java-Code", ["P1"],
  [txt("*Die Operation `erstesNull(r: Reihung von Ganzzahl): Ganzzahl` liefert den Index des ersten Buchs, das nie ausgeliehen wurde (Wert 0), "
       "sonst −1.* Die Implementierung enthält **einen** Fehler."), code(ERST),
   txt("**a)** Markieren Sie die fehlerhafte Zeile."),
   txt("**b)** Korrigierte Bedingung: [[g1]] · `erstesNull({4, 0, 2})` liefert (auch mit Fehler) [[g2]] · `erstesNull({4, 2})` mit Fehler: [[g3]]")],
  [lines(1, 1), gaps({"g1": fa(OPT7), "g2": fz(), "g3": fa(["liefert -1", "liefert 2", "ArrayIndexOutOfBoundsException"])})],
  [{"zeilen": [3]}, {"g1": ["i < r.length && r[i] != 0"], "g2": ["1"], "g3": ["ArrayIndexOutOfBoundsException"]}],
  [txt("`&&` wertet von links aus. Steht `r[i] != 0` vorn, wird bei i == r.length zuerst `r[i]` gelesen – Absturz, wenn keine 0 vorkommt. "
       "Erst die Indexprüfung, dann der Zugriff. Kommt eine 0 vor, fällt der Fehler nicht auf."), hin("Falle **P1**: Laufzeitfehler nicht ausgeschlossen.")],
  check=b07)

OPT8 = [("a", "double d = schnitt(new int[3]);", True), ("b", "int s = schnitt(werte);", False), ("c", "int[] t = top(werte, 2);", True),
        ("d", "top(werte);", False), ("e", "int[] u = top(2, werte);", False), ("f", "schnitt(werte);", True), ("g", "double e = top(werte, 1);", False)]
M8 = '''public static double schnitt(int[] r)          // Durchschnitt
public static int[] top(int[] r, int k)          // die k größten Werte'''

def b08(t):
    meth = "static double schnitt(int[] r) { return 0.0; }\nstatic int[] top(int[] r, int k) { return new int[k]; }"
    good = []
    for k, s, _x in OPT8:
        ok, _ = jcompile(meth, "int[] werte = {12, 0, 7};\n" + s)
        if ok: good.append(k)
    assert good == t["loesung"]["richtig"], good

T("W0-B-08", "Was akzeptiert der Compiler?", 2, "Methodenkopf und Signatur", ["P3", "P4"],
  [txt("Gegeben sind die Methodenköpfe zweier Operationen der Bibliothek und im Hauptprogramm `int[] werte = {12, 0, 7};`."),
   code(M8, nummern=False), txt("Welche Anweisungen akzeptiert der Compiler? Wählen Sie **alle** passenden.")],
  choice([(k, f"`{s}`") for k, s, _x in OPT8], mehrfach=True),
  {"richtig": ["a", "c", "f"]},
  [txt("a) Eine neu erzeugte Reihung ist ein gültiges Argument. b) Eine Kommazahl passt nicht in `int`. c) passt. d) Es fehlt ein Argument. "
       "e) Argumente vertauscht. f) Erlaubt – die Rückgabe geht allerdings verloren. g) Eine Reihung ist keine Kommazahl."),
   hin("Falle **P3/P4**: Anzahl, Reihenfolge und Typen der Argumente sowie der Rückgabetyp müssen passen.")],
  check=b08)

REF9 = '''int[] a = {1, 2, 3};
int[] b = a;
int[] c = verdoppelt(a);    // liefert eine NEUE Reihung mit den doppelten Werten
b[1] = 20;
c[2] = 30;
a = c;'''

def b09(t):
    meth = "static int[] verdoppelt(int[] r) { int[] n = new int[r.length]; for (int i = 0; i < r.length; i++) n[i] = 2 * r[i]; return n; }"
    o, _ = jrun(meth, REF9 + '\nout("a1", a[1]); out("a2", a[2]); out("b0", b[0]); out("b1", b[1]); out("c0", c[0]); out("ac", a == c); out("bc", b == c);')
    for g, v in o.items(): expect(t, g, v)

T("W0-B-09", "Drei Verweise, zwei Regale", 2, "Objektkarten und Referenzen", ["P2"],
  [code(REF9), txt("Geben Sie nach der letzten Zeile an: `a[1]` = [[a1]] · `a[2]` = [[a2]] · `b[0]` = [[b0]] · `b[1]` = [[b1]] · `c[0]` = [[c0]] · "
                   "`a == c` → [[ac]] · `b == c` → [[bc]]")],
  gaps({"a1": fz(), "a2": fz(), "b0": fz(), "b1": fz(), "c0": fz(), "ac": fa(WF), "bc": fa(WF)}),
  {"a1": ["4"], "a2": ["30"], "b0": ["1"], "b1": ["20"], "c0": ["2"], "ac": ["true"], "bc": ["false"]},
  [txt("`b = a`: ein Regal {1, 2, 3}, zwei Pfeile. `verdoppelt` legt ein **zweites** Regal {2, 4, 6} an. `b[1] = 20` ändert das erste Regal, "
       "`c[2] = 30` das zweite. `a = c` lenkt `a` auf das zweite Regal um: a = c = {2, 4, 30}, b = {1, 20, 3}.")],
  check=b09)

JAHRE = '''public static int jahre(int bestand, int ziel) {
    int j = 0;
    while (bestand < ziel) {
        bestand = bestand * 2;
        j++;
    }
    return j;
}'''

def b10(t):
    o, _ = jrun(JAHRE, 'out("w", jahre(3, 20)); out("w2", jahre(25, 20));')
    expect(t, "w", o["w"], 1); expect(t, "w2", o["w2"], 1)

T("W0-B-10", "Der Bestand wächst", 2, "Code ↔ Struktogramm", ["P9"],
  [txt("Die Bibliothek verdoppelt jedes Jahr ihren Bestand an Zauberbüchern."), code(JAHRE),
   txt("**a)** Vervollständigen Sie das Struktogramm nach EH § 5."),
   sg("jahre(bestand: Ganzzahl, ziel: Ganzzahl): Ganzzahl", [A("j ← 0"), SOL("[[g1]]", [A("[[g2]]"), A("j ← j + 1")]), G("[[g3]]")]),
   txt("**b)** `jahre(3, 20)` liefert [[w]], `jahre(25, 20)` liefert [[w2]].")],
  [gaps({"g1": fa(["bestand < ziel", "bestand ≥ ziel", "bestand = ziel", "j < ziel"]),
         "g2": fa(["bestand ← bestand * 2", "bestand = bestand * 2", "bestand * 2", "gib bestand * 2 zurück"]), "g3": ft(4)}),
   gaps({"w": fz(), "w2": fz()})],
  [{"g1": ["bestand < ziel"], "g2": ["bestand ← bestand * 2"], "g3": ["j"]}, {"w": ["3"], "w2": ["0"]}],
  [txt("Die while-Schleife wird zur kopfgesteuerten Solange-Schleife mit **derselben** Bedingung (solange, nicht bis). Zuweisung mit ←. "
       "3 → 6 → 12 → 24: nach 3 Jahren ist das Ziel erreicht. Ist der Bestand schon groß genug, läuft die Schleife nie: 0."),
   hin("Falle **P9**: keine Java-Syntax im Struktogramm.")],
  check=b10)

O11 = [("p1", "public static int summeBereich(int[] r, int von, int bis) {"), ("p2", "    int summe = 0;"),
       ("p3", "    for (int i = von; i <= bis; i++) {"), ("p4", "        summe = summe + r[i];"), ("p5", "    } // Ende for"),
       ("p6", "    return summe;"), ("p7", "} // Ende Methode"),
       ("d1", "    for (int i = 0; i < r.length; i++) {"), ("d2", "    von = 0;"), ("d3", "    for (int i = von; i < bis; i++) {"),
       ("d4", "        return summe + r[i];")]

def b11(t):
    tests = 'int[] r = {12, 0, 7, 25, 3}; out("a", summeBereich(r, 1, 3)); out("b", summeBereich(r, 2, 2)); out("c", summeBereich(r, 3, 1)); out("d", summeBereich(r, 0, 4));'
    want = {"a": "32", "b": "7", "c": "0", "d": "47"}
    for seq in t["loesung"]["reihenfolgen"]:
        o, _ = jrun(assemble_order(t, seq), tests); assert o == want, o
    for bad in (["p1", "p2", "d1", "p4", "p5", "p6", "p7"], ["p1", "p2", "d3", "p4", "p5", "p6", "p7"], ["p1", "p2", "d2", "p3", "p4", "p5", "p6", "p7"]):
        o, _ = jrun(assemble_order(t, bad), tests); assert o != want, bad

T("W0-B-11", "Ausleihen im Regalabschnitt", 2, "Methode implementieren", ["P6", "P3"],
  [txt("*Die Operation `summeBereich(r: Reihung von Ganzzahl, von: Ganzzahl, bis: Ganzzahl): Ganzzahl` liefert die Summe der Werte mit den "
       "Indizes von `von` bis `bis` (beide einschließlich). Es gilt 0 ≤ von und bis < Länge von r; ist von > bis, wird 0 geliefert.* "
       "Setzen Sie die Methode zusammen – nicht alle Teile werden gebraucht.")],
  order(O11),
  {"reihenfolgen": [["p1", "p2", "p3", "p4", "p5", "p6", "p7"]]},
  [txt("Die Schleife beginnt beim Parameter `von` und läuft **einschließlich** bis `bis`. Die Parameter werden gelesen, nicht überschrieben (F5). "
       "Für von > bis läuft die Schleife nicht → 0."), hin("Fallen **P6** (`<` statt `<=`) und **P3** (Rückgabe in der Schleife).")],
  check=b11)

# ================================================================ Stufe 3
ZAEHL12 = '''public static int[] ueberGrenze(int[] r, int grenze) {
    int anzahl = 0;
    for (int x : r) {
        if (x > grenze) {
            anzahl++;
        }
    }
    // ... hier geht es weiter'''
O12 = [("p1", "    int[] erg = new int[anzahl];"), ("p2", "    int k = 0;"), ("p3", "    for (int i = 0; i < r.length; i++) {"),
       ("p4", "        if (r[i] > grenze) {"), ("p5", "            erg[k] = r[i];"), ("p6", "            k++;"),
       ("p7", "        } // Ende if"), ("p8", "    } // Ende for"), ("p9", "    return erg;"), ("p10", "} // Ende Methode"),
       ("d1", "            erg[i] = r[i];"), ("d2", "    int[] erg = new int[r.length];"), ("d3", "    return r;")]

def b12(t):
    head = ZAEHL12.replace("    // ... hier geht es weiter", "")
    tests = 'int[] r = {12, 0, 7, 25, 3}; out("a", arr(ueberGrenze(r, 5))); out("r", arr(r)); out("b", ueberGrenze(r, 30).length); out("c", ueberGrenze(new int[0], 1).length);'
    want = {"a": "12,7,25", "r": "12,0,7,25,3", "b": "0", "c": "0"}
    for seq in t["loesung"]["reihenfolgen"]:
        o, _ = jrun(head + "\n" + assemble_order(t, seq), tests); assert o == want, o
    for bad in (["p1", "p2", "p3", "p4", "d1", "p6", "p7", "p8", "p9", "p10"], ["d2", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10"]):
        try:
            o, _ = jrun(head + "\n" + assemble_order(t, bad), tests); assert o != want, bad
        except AssertionError as e:
            if "Laufzeitfehler" not in str(e): raise

T("W0-B-12", "Die Liste für die Neuauflage", 3, "Methode implementieren", ["P1", "P2"],
  [txt("*Die Operation `ueberGrenze(r: Reihung von Ganzzahl, grenze: Ganzzahl): Reihung von Ganzzahl` liefert eine neue Reihung mit allen "
       "Werten von r, die echt größer als grenze sind, in der ursprünglichen Reihenfolge. Die Länge entspricht genau der Anzahl dieser Werte; "
       "r bleibt unverändert.* Der erste Teil (Zählen) ist fertig:"), code(ZAEHL12),
   txt("Setzen Sie den Rest der Methode zusammen – nicht alle Teile werden gebraucht.")],
  order(O12),
  {"reihenfolgen": [["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10"], ["p2", "p1", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10"]]},
  [txt("Zweiphasiges Muster: erst zählen, dann eine Reihung **genau dieser Länge** anlegen und mit einem **eigenen Schreibindex** `k` füllen. "
       "`erg[i]` würde über das Ende von `erg` hinausschreiben (Laufzeitfehler) bzw. Lücken lassen; `new int[r.length]` hätte die falsche Länge."),
   hin("Fallen **P1** (Index außerhalb von erg) und **P2** (Original nicht verändern, `return r` ist keine neue Reihung).")],
  check=b12)

IMAX = '''public static int indexMaximum(int[] r) {
    int pos = 0;
    for (int i = 1; i < r.length; i++) {
        if (r[i] >= r[pos]) {
            pos = i;
        }
    }
    return pos;
}'''

def b13(t):
    o, _ = jrun(IMAX, 'out("g2", indexMaximum(new int[]{3, 9, 2, 9})); out("leer", indexMaximum(new int[0]));')
    expect(t, "g2", o["g2"], 1); assert o["leer"] == "0"
    fixed = IMAX.replace(">=", t["loesung"][1]["g1"][0])
    o, _ = jrun(fixed, 'out("g3", indexMaximum(new int[]{3, 9, 2, 9}));')
    expect(t, "g3", o["g3"], 1)
    assert t["loesung"][0]["zeilen"] == [4] and t["loesung"][2]["richtig"] == ["b"]

T("W0-B-13", "Das meistgeliehene Buch", 3, "Fehler im Java-Code", ["P1", "P3"],
  [txt("*Die Operation `indexMaximum(r: Reihung von Ganzzahl): Ganzzahl` liefert den Index des am häufigsten ausgeliehenen Buchs; bei Gleichstand "
       "den **kleinsten** dieser Indizes, für eine leere Reihung −1.*"), code(IMAX),
   txt("**a)** Markieren Sie die Zeile, die bei Gleichstand ein falsches Ergebnis verursacht."),
   txt("**b)** Korrigierter Operator: `r[i]` [[g1]] `r[pos]` · `indexMaximum({3, 9, 2, 9})` liefert fehlerhaft [[g2]], korrigiert [[g3]]"),
   txt("**c)** Was gilt für die leere Reihung?")],
  [lines(1, 1), gaps({"g1": fa([">", ">=", "<", "<="]), "g2": fz(), "g3": fz()}),
   choice([("a", "Die Methode stürzt mit einer ArrayIndexOutOfBoundsException ab."),
           ("b", "Die Methode liefert 0 statt −1 – es fehlt eine Abfrage `if (r.length == 0) { return -1; }` vor der Schleife."),
           ("c", "Die Methode liefert korrekt −1."),
           ("d", "Der Compiler meldet „missing return statement“.")])],
  [{"zeilen": [4]}, {"g1": [">"], "g2": ["3"], "g3": ["1"]}, {"richtig": ["b"]}],
  [txt("Mit `>=` übernimmt jeder **gleich große** spätere Wert die Position – geliefert wird der letzte Index des Maximums (3 statt 1). "
       "Für die leere Reihung läuft die Schleife nicht; es wird nichts gelesen, aber `pos = 0` zurückgegeben – ein Index, den es gar nicht gibt. "
       "Die Leer-Abfrage gehört an den Anfang."),
   hin("Fallen **P1** (Leer-Abfrage) und **P3** (Rückgabe entspricht nicht der Vorgabe).")],
  check=b13)

NEST = '''for (int z = 1; z <= 3; z++) {
    String zeile = "";
    for (int s = z; s <= 4; s++) {
        zeile = zeile + (s * z);
    }
    println(zeile);
}'''

def b14(t):
    o, ls = jrun("static int cnt = 0;", NEST.replace("zeile = zeile + (s * z);", "zeile = zeile + (s * z); cnt++;") + '\nout("n", cnt);')
    for k in range(3): expect(t, f"z{k+1}", ls[k])
    expect(t, "n", o["n"])

T("W0-B-14", "Das Sternenregister", 3, "Tracetabelle", ["P8"],
  [txt("Die Bibliothekarin druckt ein Register (Online-IDE: `println` ohne `System.out`)."), code(NEST),
   txt("Geben Sie die drei Ausgabezeilen an (ohne Anführungszeichen):"),
   tab(["Zeile", "Ausgabe"], [["1", "[[z1]]"], ["2", "[[z2]]"], ["3", "[[z3]]"]]),
   txt("Wie oft wird die Anweisung `zeile = zeile + (s * z);` insgesamt ausgeführt? [[n]]")],
  gaps({"z1": ft(8), "z2": ft(8), "z3": ft(8), "n": fz()}),
  {"z1": ["1234", "\"1234\""], "z2": ["468", "\"468\""], "z3": ["912", "\"912\""], "n": ["9"]},
  [txt("Die innere Schleife beginnt bei `s = z`. z = 1: 1, 2, 3, 4 → \"1234\". z = 2: s = 2, 3, 4 → 4, 6, 8 → \"468\". "
       "z = 3: s = 3, 4 → 9, 12 → \"912\". Die Zahlen werden an die Zeichenkette **angehängt**, nicht addiert. 4 + 3 + 2 = 9 Ausführungen."),
   hin("Falle **P8**: Bei geschachtelten Schleifen jede innere Runde einzeln verfolgen.")],
  check=b14)

ABST = '''public static boolean istAbsteigend(int[] r) {
    for (int i = [[g1]]; i < r.length; i++) {
        if (r[i] [[g2]] r[i - 1]) {
            return [[g3]];
        }
    }
    return [[g4]];
}'''

def b15(t):
    L = t["loesung"][0]
    src = fill(ABST, {g: L[g][0] for g in L})
    inst = src.replace("        if (r[i]", "        cnt++;\n        if (r[i]")
    o, _ = jrun("static int cnt = 0;\n" + inst, '''out("a", "" + istAbsteigend(new int[]{9, 7, 7, 2}) + istAbsteigend(new int[]{}) + istAbsteigend(new int[]{5}) + istAbsteigend(new int[]{3, 4}));
        cnt = 0; out("w", istAbsteigend(new int[]{9, 7, 7, 8, 2})); out("n", cnt);''')
    assert o["a"] == "truetruetruefalse", o
    expect(t, "w", o["w"], 1); expect(t, "n", o["n"], 1)

T("W0-B-15", "Die Rangfolge der Regale", 3, "Lückencode", ["P1", "P6", "P3"],
  [txt("*Die Operation `istAbsteigend(r: Reihung von Ganzzahl): Wahrheitswert` liefert wahr, wenn jedes Element ab dem zweiten **kleiner oder gleich** "
       "seinem Vorgänger ist. Für Reihungen mit weniger als zwei Elementen liefert sie wahr.* Füllen Sie die Lücken."),
   code(ABST),
   txt("Für `{9, 7, 7, 8, 2}` liefert die Methode [[w]]; dabei wird die Bedingung der if-Anweisung [[n]]-mal ausgewertet.")],
  [gaps({"g1": fz(), "g2": fa([">", ">=", "<", "<="]), "g3": fa(WF), "g4": fa(WF)}), gaps({"w": fa(WF), "n": fz()})],
  [{"g1": ["1"], "g2": [">"], "g3": ["false"], "g4": ["true"]}, {"w": ["false"], "n": ["3"]}],
  [txt("Start bei 1, damit `r[i - 1]` existiert (P1/P6). Gesucht ist ein **Gegenbeispiel**: ein Element, das größer als sein Vorgänger ist → sofort "
       "`false`. Erst nach der Schleife steht fest, dass es keins gibt → `true` (P3: Rückgabe in jedem Pfad). Bei {9, 7, 7, 8, 2} wird beim dritten "
       "Vergleich (8 > 7) abgebrochen."),
   hin("Gleichheit (7, 7) ist erlaubt – darum `>` und nicht `>=`.")],
  check=b15)

BOSS = {"id": "W0-BOSS", "titel": "Aufnahmeprüfung: Die Bibliothek der Akademie", "dauerMin": 25, "anzahl": 8,
        "mix": {"1": 3, "2": 3, "3": 2}, "pool": [k for k in ORDER if k.startswith("W0-B-")]}
for k in BOSS["pool"]:
    TASKS[k]["tipps"] = []
