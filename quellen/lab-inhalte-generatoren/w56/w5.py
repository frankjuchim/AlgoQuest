# Welt 5 "Der Wald" – Algo Quest Lab: Level 5.1–5.6 + Boss-Pool
# Alle Loesungen werden hier berechnet (Python-Baummodell) und per Java (javac 21 + NI-Stub) gegengeprueft.
import sys, json
sys.path.insert(0, "/tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad/algolab/w56")
from common import *

J5 = Java("w5")
chk = []   # (beschreibung, python_wert, java_key) -> spaeter verglichen

def jt(key, ausdruck):
    """Zeile fuer run(): Ergebnis ausgeben"""
    return '        K.out("%s", %s);' % (key, ausdruck)

# ======================================================================= Testbaeume
BSP = "8(3(1,6(4,7)),10(-,14(13,-)))"            # beispielBST (Baumschule)
ZB = "5(9(2,7),4(-,9(1,-)))"                     # zahlenbaum (Baumschule)
ENT = "1(-,2(-,3(-,4(-,5))))"                    # entartet (Baumschule)
MQ = "Kann es fliegen?(Speit es Feuer?(Drache,Greif),Lebt es im Wasser?(Kraken,Troll))"  # monsterquiz
ITEM = "50(30(20(10,-),40(35,45)),70(60(-,65),80(75,-)))"   # Item-Datenbank (AB 2)

# Grundcheck der Baumschule gegen die Spec
assert wl(vals(nodes_pre(parse(BSP)))) == "8 3 1 6 4 7 10 14 13 "
assert wl(vals(nodes_level(parse(ZB)))) == "5 9 4 2 7 9 1 "

# Traversierungen aller verwendeten Baeume in Java (Vergleich mit Python)
TRAV = {}
def trav(name, s, text=False):
    TRAV[name] = s
    bau = "K.baueS" if text else "K.baue"
    return "\n".join([
        jt("trav.%s.pre" % name, 'K.pre(%s("%s"))' % (bau, s)),
        jt("trav.%s.in" % name, 'K.in(%s("%s"))' % (bau, s)),
        jt("trav.%s.post" % name, 'K.post(%s("%s"))' % (bau, s)),
        jt("trav.%s.level" % name, 'K.level(%s("%s"))' % (bau, s)),
        jt("trav.%s.k" % name, 'K.k(%s("%s"))' % (bau, s))])

# ----------------------------------------------------------------------- gemeinsame Java-Methoden
BAUM_METHODEN = r'''
    public static int anzahlKnoten(BinTree b) {
        if (b.isEmpty()) { return 0; }
        return 1 + anzahlKnoten(b.getLeft()) + anzahlKnoten(b.getRight());
    }
    public static int anzahlBlaetter(BinTree b) {
        if (b.isEmpty()) { return 0; }
        if (b.isLeaf()) { return 1; }
        return anzahlBlaetter(b.getLeft()) + anzahlBlaetter(b.getRight());
    }
    public static int hoehe(BinTree b) {
        if (b.isEmpty()) { return 0; }
        int l = hoehe(b.getLeft()); int r = hoehe(b.getRight());
        if (l > r) { return 1 + l; }
        return 1 + r;
    }
    public static int summe(BinTree b) {
        if (b.isEmpty()) { return 0; }
        return (Integer) b.getItem() + summe(b.getLeft()) + summe(b.getRight());
    }
    public static int maximum(BinTree b) {
        if (b.isEmpty()) { return -1; }
        int max = (Integer) b.getItem();
        int l = maximum(b.getLeft()); int r = maximum(b.getRight());
        if (l > max) { max = l; }
        if (r > max) { max = r; }
        return max;
    }
    public static int zahl(String s) {
        int z = 0;
        for (int i = 0; i < s.length(); i++) { z = z * 10 + ((int) s.charAt(i) - (int) '0'); }
        return z;
    }
    public static int berechne(BinTree t) {
        String w = (String) t.getItem();
        if (t.isLeaf()) { return zahl(w); }
        int l = berechne(t.getLeft()); int r = berechne(t.getRight());
        if (w.equals("+")) { return l + r; }
        if (w.equals("−") || w.equals("-")) { return l - r; }
        if (w.equals("*")) { return l * r; }
        return l / r;
    }
    public static int ebeneVon(BinTree b, Object x, int e) {
        if (b.isEmpty()) { return -1; }
        if (b.getItem().equals(x)) { return e; }
        int l = ebeneVon(b.getLeft(), x, e + 1);
        if (l >= 0) { return l; }
        return ebeneVon(b.getRight(), x, e + 1);
    }
    public static int anzahlInnere(BinTree b) {
        if (b.isEmpty() || b.isLeaf()) { return 0; }
        return 1 + anzahlInnere(b.getLeft()) + anzahlInnere(b.getRight());
    }
    public static boolean istBST(BinTree b, int min, int max) {
        if (b.isEmpty()) { return true; }
        int wert = (Integer) b.getItem();
        if (wert <= min) { return false; }
        if (max != -1 && wert >= max) { return false; }
        return istBST(b.getLeft(), min, wert) && istBST(b.getRight(), wert, max);
    }
    public static boolean nurKinder(BinTree b) {
        if (b.isEmpty()) { return true; }
        int w = (Integer) b.getItem();
        if (!b.getLeft().isEmpty() && (Integer) b.getLeft().getItem() >= w) { return false; }
        if (!b.getRight().isEmpty() && (Integer) b.getRight().getItem() <= w) { return false; }
        return nurKinder(b.getLeft()) && nurKinder(b.getRight());
    }
    public static boolean suche(BinTree b, int x) {
        if (b.isEmpty()) { return false; }
        int wert = (Integer) b.getItem();
        if (x == wert) { return true; }
        if (x < wert) { return suche(b.getLeft(), x); }
        return suche(b.getRight(), x);
    }
    public static int vergleiche(BinTree b, int x) {
        if (b.isEmpty()) { return 0; }
        int wert = (Integer) b.getItem();
        if (x == wert) { return 1; }
        if (x < wert) { return 1 + vergleiche(b.getLeft(), x); }
        return 1 + vergleiche(b.getRight(), x);
    }
    public static void einfuegen(BinTree b, int x) {
        if (b.isEmpty()) { b.setItem(x); return; }
        int wert = (Integer) b.getItem();
        if (x < wert) { einfuegen(b.getLeft(), x); }
        else if (x > wert) { einfuegen(b.getRight(), x); }
    }
    public static BinTree baueAus(int[] r) {
        BinTree b = new BinTree();
        for (int i = 0; i < r.length; i++) { einfuegen(b, r[i]); }
        return b;
    }
    public static int minimumBST(BinTree b) { if (b.getLeft().isEmpty()) { return (Integer) b.getItem(); } return minimumBST(b.getLeft()); }
    public static int maximumBST(BinTree b) { if (b.getRight().isEmpty()) { return (Integer) b.getItem(); } return maximumBST(b.getRight()); }
    public static void loesche(BinTree b, int x, boolean nachfolger) {
        if (b.isEmpty()) { return; }
        int wert = (Integer) b.getItem();
        if (x < wert) { loesche(b.getLeft(), x, nachfolger); }
        else if (x > wert) { loesche(b.getRight(), x, nachfolger); }
        else if (b.isLeaf()) { b.setEmpty(); }
        else if (b.getLeft().isEmpty()) { BinTree k = b.getRight(); b.setItem(k.getItem()); b.setLeft(k.getLeft()); b.setRight(k.getRight()); }
        else if (b.getRight().isEmpty()) { BinTree k = b.getLeft(); b.setItem(k.getItem()); b.setLeft(k.getLeft()); b.setRight(k.getRight()); }
        else if (nachfolger) { int nf = minimumBST(b.getRight()); b.setItem(nf); loesche(b.getRight(), nf, nachfolger); }
        else { int vg = maximumBST(b.getLeft()); b.setItem(vg); loesche(b.getLeft(), vg, nachfolger); }
    }
    public static BinTree ausgeglichenAus(int[] r, int lo, int hi) {
        if (lo > hi) { return new BinTree(); }
        int mitte = (lo + hi) / 2;
        BinTree b = new BinTree(r[mitte]);
        b.setLeft(ausgeglichenAus(r, lo, mitte - 1));
        b.setRight(ausgeglichenAus(r, mitte + 1, hi));
        return b;
    }
    public static String raten(BinTree b, String antworten) {
        if (b.isLeaf()) { return (String) b.getItem(); }
        if (antworten.length() == 0) { return "?"; }
        String rest = antworten.substring(1, antworten.length());
        if (antworten.charAt(0) == 'j') { return raten(b.getLeft(), rest); }
        return raten(b.getRight(), rest);
    }
    public static void lernen(BinTree b, String antworten, String neu, String frage, boolean jaFuerNeu) {
        if (b.isLeaf()) {
            String alt = (String) b.getItem();
            b.setItem(frage);
            if (jaFuerNeu) { b.setLeft(new BinTree(neu)); b.setRight(new BinTree(alt)); }
            else { b.setLeft(new BinTree(alt)); b.setRight(new BinTree(neu)); }
            return;
        }
        String rest = antworten.substring(1, antworten.length());
        if (antworten.charAt(0) == 'j') { lernen(b.getLeft(), rest, neu, frage, jaFuerNeu); }
        else { lernen(b.getRight(), rest, neu, frage, jaFuerNeu); }
    }
'''
J5.add("BM", BAUM_METHODEN, "        K.out(\"BM.ok\", \"1\");")

# ======================================================================= Level 5.1 – Daten
Q = "K(E(A,G(-,H)),T(R(P,-),W))"
N1 = "6(2(7,4(-,1)),9(-,3(5,8)))"
CODE_L104 = '''BinTree w = new BinTree(4);
w.setLeft(new BinTree(8));
w.setRight(new BinTree(1));
w.getRight().getLeft().setItem(6);
BinTree h = w.getLeft();
h.getRight().setItem(3);
h.getRight().setLeft(new BinTree(5));
w.getRight().setRight(new BinTree(2));
h = new BinTree(9);
h.setLeft(new BinTree(7));'''
L105_AUSDR = [("a", "w.getLeft().isLeaf()"), ("b", "h.isLeaf()"), ("c", "(Integer) w.getRight().getItem() + 5"),
              ("d", "w.getLeft().getLeft().isEmpty()"), ("e", "w.getLeft().getLeft().getItem()"),
              ("f", "w.getRight().getRight().isLeaf()")]
run = "\n".join("        " + l for l in CODE_L104.splitlines()) + "\n" + jt("W5-L1-04.w", "K.k(w)") + "\n" + jt("W5-L1-04.h", "K.k(h)")
for k, a in L105_AUSDR:
    run += '\n        try { K.out("W5-L1-05.%s", %s); } catch (IllegalStateException e) { K.out("W5-L1-05.%s", "Laufzeitfehler"); }' % (k, a, k)
J5.add("L104", "", run)

PRE106 = "E U L A R T S".split(); IN106 = "U A L E T R S".split()
TERM107 = "+(*(+(6,2),5),/(12,4))"
TERM108 = "−(*(+(1,3),5),/(8,2))"
J5.add("L1T", "", "\n".join([trav("Q", Q, True), trav("N1", N1), trav("T107", TERM107, True), trav("T108", TERM108, True),
       jt("W5-L1-07.wert", 'BM.berechne(K.baueS("%s"))' % TERM107), jt("W5-L1-08.wert", 'BM.berechne(K.baueS("%s"))' % TERM108),
       jt("W5-L1-01.knoten", 'BM.anzahlKnoten(K.baueS("%s"))' % Q), jt("W5-L1-01.blaetter", 'BM.anzahlBlaetter(K.baueS("%s"))' % Q),
       jt("W5-L1-01.innere", 'BM.anzahlInnere(K.baueS("%s"))' % Q), jt("W5-L1-01.hoehe", 'BM.hoehe(K.baueS("%s"))' % Q),
       jt("W5-L1-01.ebeneH", 'BM.ebeneVon(K.baueS("%s"), "H", 0)' % Q), jt("W5-L1-01.hoeheE", 'BM.hoehe(K.baueS("%s").getLeft())' % Q),
       ]))

# ======================================================================= Level 5.2 – Daten
G = "6(9(2,-),4(7(1,5),8))"
J5.add("L201", "", "\n".join([jt("W5-L2-01." + k, 'BM.%s(K.baue("%s"))' % (m, G)) for k, m in
       [("knoten", "anzahlKnoten"), ("blaetter", "anzahlBlaetter"), ("hoehe", "hoehe"), ("summe", "summe"), ("maximum", "maximum")]]))

# 5.2-02 Rekursionstabelle hoehe (instrumentiert)
T202 = "9(4(-,6),12)"
HOEHE_CODE = '''public static int hoehe(BinTree b) {
    if (b.isEmpty()) {
        return 0;
    }
    int l = hoehe(b.getLeft());
    int r = hoehe(b.getRight());
    if (l > r) {
        return 1 + l;
    }
    return 1 + r;
}'''
J5.add("L202", r'''
    static java.util.ArrayList<String[]> zeilen = new java.util.ArrayList<String[]>();
    static int hoehe(BinTree b, int t) {
        String[] z = new String[5]; zeilen.add(z);
        z[0] = "" + t; z[1] = b.isEmpty() ? "leer" : "" + b.getItem();
        if (b.isEmpty()) { z[2] = "–"; z[3] = "–"; z[4] = "0"; return 0; }
        int l = hoehe(b.getLeft(), t + 1); int r = hoehe(b.getRight(), t + 1);
        z[2] = "" + l; z[3] = "" + r;
        int erg = (l > r) ? 1 + l : 1 + r; z[4] = "" + erg; return erg;
    }''', '''        hoehe(K.baue("%s"), 0);
        String s = ""; for (String[] z : zeilen) s += String.join("|", z) + ";";
        K.out("W5-L2-02.tab", s);''' % T202)

# 5.2-03 Bug: isLeaf vor isEmpty
BLATT_BUG = '''public static int anzahlBlaetter(BinTree b) {
    if (b.isLeaf()) {
        return 1;
    }
    if (b.isEmpty()) {
        return 0;
    }
    return anzahlBlaetter(b.getLeft()) + anzahlBlaetter(b.getRight());
}'''
BLATT_OK = '''public static int anzahlBlaetter(BinTree b) {
    if (b.isEmpty()) {
        return 0;
    }
    if (b.isLeaf()) {
        return 1;
    }
    return anzahlBlaetter(b.getLeft()) + anzahlBlaetter(b.getRight());
}'''
J5.add("L203bug", BLATT_BUG, '''        try { anzahlBlaetter(K.baue("%s")); K.out("W5-L2-03.bug", "kein Fehler"); }
        catch (IllegalStateException e) { K.out("W5-L2-03.bug", K.zeile(e, "L203bug", 2)); }
        try { K.out("W5-L2-03.bspbug", anzahlBlaetter(K.baue("%s"))); } catch (IllegalStateException e) { K.out("W5-L2-03.bspbug", "Laufzeitfehler"); }''' % (ZB, "7(3,9)"))
J5.add("L203ok", BLATT_OK, jt("W5-L2-03.ok", 'anzahlBlaetter(K.baue("%s"))' % ZB) + "\n" + jt("W5-L2-03.okleer", "anzahlBlaetter(new BinTree())"))

# 5.2-04 Cast fehlt (Kompilierfehler)
SUMME_BUG = '''public static int summe(BinTree b) {
    if (b.isEmpty()) {
        return 0;
    }
    int w = b.getItem();
    return w + summe(b.getLeft()) + summe(b.getRight());
}'''
J5.expect_compile_error("W5-L2-04.zeile", "L204bug", SUMME_BUG)
J5.add("L204ok", SUMME_BUG.replace("int w = b.getItem();", "int w = (Integer) b.getItem();"),
       jt("W5-L2-04.summe", 'summe(K.baue("%s"))' % ZB))

# 5.2-05 Code-Puzzle maximum
T205 = {
    "t1": "public static int maximum(BinTree b) {",
    "t2": "if (b.isEmpty()) {\n    return -1;\n}",
    "t3": "int max = (Integer) b.getItem();",
    "t4": "int l = maximum(b.getLeft());",
    "t5": "int r = maximum(b.getRight());",
    "t6": "if (l > max) {\n    max = l;\n}",
    "t7": "if (r > max) {\n    max = r;\n}",
    "t8": "return max;\n}",
    "d1": "int max = b.getItem();",
    "d2": "if (b.isEmpty()) {\n    return 0;\n}",
    "d3": "maximum(b.getLeft());",
}
TEST_MAX = '''            if (maximum(K.baue("%s")) != 9) throw new RuntimeException("zb");
            if (maximum(K.baue("%s")) != 14) throw new RuntimeException("bsp");
            if (maximum(new BinTree()) != -1) throw new RuntimeException("leer");
            if (maximum(K.baue("3(12(-,40),7)")) != 40) throw new RuntimeException("tief");
            if (maximum(K.baue("50(2,1)")) != 50) throw new RuntimeException("wurzel");
            if (maximum(K.baue("0")) != 0) throw new RuntimeException("null");''' % (ZB, BSP)
OC205 = OrderCheck(J5, "W5-L2-05", T205, ["t1", "t2"], ["t3", "t4", "t5", "t6", "t7"], ["t8"], TEST_MAX, "O205")
# Distraktoren muessen scheitern: d2 statt t2 (leerer Baum liefert 0)
OC205d = OrderCheck(J5, "W5-L2-05d", T205, ["t1", "d2", "t3", "t4", "t5", "t6", "t7"], [], ["t8"], TEST_MAX, "O205d")

# 5.2-06 Struktogramm geheim = Knoten mit genau einem Kind
GEHEIM = r'''
    public static int geheim(BinTree b) {
        if (b.isEmpty()) { return 0; }
        int anzahl = geheim(b.getLeft()) + geheim(b.getRight());
        if (b.getLeft().isEmpty() && !b.getRight().isEmpty()) { anzahl = anzahl + 1; }
        if (!b.getLeft().isEmpty() && b.getRight().isEmpty()) { anzahl = anzahl + 1; }
        return anzahl;
    }'''
J5.add("L206", GEHEIM, "\n".join([jt("W5-L2-06.zb", 'geheim(K.baue("%s"))' % ZB), jt("W5-L2-06.ent", 'geheim(K.baue("%s"))' % ENT),
                                   jt("W5-L2-06.g", 'geheim(K.baue("%s"))' % G), jt("W5-L2-06.bsp", 'geheim(K.baue("%s"))' % BSP)]))

# 5.2-07 Lueckencode anzahlGroesser
LUECKE207 = '''public static int anzahlGroesser(BinTree b, int grenze) {
    if ([[g1]]) {
        return [[g2]];
    }
    int anzahl = anzahlGroesser(b.getLeft(), grenze) + [[g3]];
    if ([[g4]] > grenze) {
        anzahl = anzahl + 1;
    }
    return anzahl;
}'''
L207 = {"g1": ["b.isEmpty()"], "g2": ["0"], "g3": ["anzahlGroesser(b.getRight(),grenze)"],
        "g4": ["(Integer)b.getItem()", "((Integer)b.getItem())", "(int)b.getItem()"]}
for i, v4 in enumerate(L207["g4"]):
    code = LUECKE207.replace("[[g1]]", L207["g1"][0]).replace("[[g2]]", L207["g2"][0]).replace("[[g3]]", "anzahlGroesser(b.getRight(), grenze)").replace("[[g4]]", v4)
    J5.add("L207_%d" % i, code, "\n".join([jt("W5-L2-07.v%d.zb4" % i, 'anzahlGroesser(K.baue("%s"), 4)' % ZB),
                                            jt("W5-L2-07.v%d.bsp7" % i, 'anzahlGroesser(K.baue("%s"), 7)' % BSP),
                                            jt("W5-L2-07.v%d.leer" % i, "anzahlGroesser(new BinTree(), 3)")]))

# 5.2-08 Rekursionstabelle enthaelt mit ||
T208 = "3(8(1,6),5(-,6))"
ENTHAELT_CODE = '''public static boolean enthaelt(BinTree b, int x) {
    if (b.isEmpty()) {
        return false;
    }
    int wert = (Integer) b.getItem();
    if (wert == x) {
        return true;
    }
    return enthaelt(b.getLeft(), x) || enthaelt(b.getRight(), x);
}'''
J5.add("L208", r'''
    static java.util.ArrayList<String[]> zeilen = new java.util.ArrayList<String[]>();
    static boolean enthaelt(BinTree b, int x, int t) {
        String[] z = new String[3]; zeilen.add(z);
        z[0] = "" + t; z[1] = b.isEmpty() ? "leer" : "" + b.getItem();
        boolean e;
        if (b.isEmpty()) { e = false; }
        else if ((Integer) b.getItem() == x) { e = true; }
        else { e = enthaelt(b.getLeft(), x, t + 1) || enthaelt(b.getRight(), x, t + 1); }
        z[2] = e ? "true" : "false"; return e;
    }''', '''        enthaelt(K.baue("%s"), 6, 0);
        String s = ""; for (String[] z : zeilen) s += String.join("|", z) + ";";
        K.out("W5-L2-08.tab", s);''' % T208)
J5.add("L208b", ENTHAELT_CODE, jt("W5-L2-08.check", 'enthaelt(K.baue("%s"), 6)' % T208))

# ======================================================================= Level 5.3 – Daten
RATEN301 = ["nj", "jn", "j", "nnjn", ""]
J5.add("L301", "", "\n".join([jt("W5-L3-01.%d" % i, 'BM.raten(K.baueS("%s"), "%s")' % (MQ, a)) for i, a in enumerate(RATEN301)]))
LERN302 = [("jj", "Phönix", "Ist es ein Vogel?", True), ("nn", "Zyklop", "Ist es behaart?", False)]
run = '        BinTree b = K.baueS("%s");\n' % MQ
for a, n, f, j in LERN302:
    run += '        BM.lernen(b, "%s", "%s", "%s", %s);\n' % (a, n, f, "true" if j else "false")
run += jt("W5-L3-02.baum", "K.k(b)") + "\n" + jt("W5-L3-02.monster", "BM.anzahlBlaetter(b)") + "\n" + jt("W5-L3-02.fragen", "BM.anzahlInnere(b)")
run += "\n" + jt("W5-L3-02.r_jj", 'BM.raten(b, "jj")') + "\n" + jt("W5-L3-02.r_nnn", 'BM.raten(b, "nnn")')
J5.add("L302", "", run)
# 5.3-03: 7 lernen-Aufrufe ab einem Blatt
J5.add("L303", "", '''        BinTree b = new BinTree("Schleim");
        String[] wege = {"", "j", "n", "jj", "nn", "jn", "jjj"};
        for (int i = 0; i < wege.length; i++) { BM.lernen(b, wege[i], "M" + i, "F" + i, i % 2 == 0); }
''' + jt("W5-L3-03.monster", "BM.anzahlBlaetter(b)") + "\n" + jt("W5-L3-03.fragen", "BM.anzahlInnere(b)") + "\n" + jt("W5-L3-03.knoten", "BM.anzahlKnoten(b)"))
T304 = "5(8(1,-),3(7(-,2),9))"
T305 = "4(7(2,-),6(1,3(8,-)))"
LEVEL_CODE = '''public static String levelorder(BinTree b) {
    String text = "";
    Queue q = new Queue();
    if (!b.isEmpty()) {
        q.enqueue(b);
    }
    while (!q.isEmpty()) {
        BinTree k = (BinTree) q.dequeue();
        text = text + k.getItem() + " ";
        if (!k.getLeft().isEmpty()) {
            q.enqueue(k.getLeft());
        }
        if (!k.getRight().isEmpty()) {
            q.enqueue(k.getRight());
        }
    }
    return text;
}'''
LEVEL_TRACE = r'''
    static String inhalt(Queue q) {
        Queue h = new Queue(); String s = "";
        while (!q.isEmpty()) { BinTree k = (BinTree) q.dequeue(); s += (s.length() > 0 ? ", " : "") + k.getItem(); h.enqueue(k); }
        while (!h.isEmpty()) q.enqueue(h.dequeue());
        return s.length() == 0 ? "–" : s;
    }
    static String trace(BinTree b) {
        String log = ""; String text = ""; Queue q = new Queue();
        if (!b.isEmpty()) q.enqueue(b);
        log += "Start|–|" + inhalt(q) + ";";
        int d = 0;
        while (!q.isEmpty()) {
            BinTree k = (BinTree) q.dequeue(); text = text + k.getItem() + " ";
            if (!k.getLeft().isEmpty()) q.enqueue(k.getLeft());
            if (!k.getRight().isEmpty()) q.enqueue(k.getRight());
            d++; log += d + "|" + k.getItem() + "|" + inhalt(q) + ";";
        }
        return log;
    }'''
J5.add("L305", LEVEL_CODE + LEVEL_TRACE, jt("W5-L3-05.tab", 'trace(K.baue("%s"))' % T305) + "\n" + jt("W5-L3-05.text", 'levelorder(K.baue("%s"))' % T305)
       + "\n" + jt("W5-B-10.tab", 'trace(K.baue("%s"))' % "2(9(4,7),5(-,3))"))
J5.add("L3T", "", "\n".join([trav("T304", T304), trav("T305", T305)]))
# 5.3-06 Bug: leere Teilbaeume eingereiht
LEVEL_BUG = '''public static String levelorder(BinTree b) {
    String text = "";
    Queue q = new Queue();
    q.enqueue(b);
    while (!q.isEmpty()) {
        BinTree k = (BinTree) q.dequeue();
        text = text + k.getItem() + " ";
        q.enqueue(k.getLeft());
        q.enqueue(k.getRight());
    }
    return text;
}'''
J5.add("L306bug", LEVEL_BUG, '''        try { levelorder(K.baue("%s")); K.out("W5-L3-06.bug", "kein Fehler"); }
        catch (IllegalStateException e) { K.out("W5-L3-06.bug", K.zeile(e, "L306bug", 2)); }''' % ZB)
# Korrekturvarianten
FIX_A = LEVEL_BUG.replace('''        BinTree k = (BinTree) q.dequeue();
        text = text + k.getItem() + " ";
        q.enqueue(k.getLeft());
        q.enqueue(k.getRight());''', '''        BinTree k = (BinTree) q.dequeue();
        if (!k.isEmpty()) {
            text = text + k.getItem() + " ";
            q.enqueue(k.getLeft());
            q.enqueue(k.getRight());
        }''')
FIX_B = LEVEL_BUG.replace('''        q.enqueue(k.getLeft());
        q.enqueue(k.getRight());''', '''        if (!k.getLeft().isEmpty()) {
            q.enqueue(k.getLeft());
        }
        if (!k.getRight().isEmpty()) {
            q.enqueue(k.getRight());
        }''')
FIX_C = LEVEL_BUG.replace("    while (!q.isEmpty()) {", "    while (!q.isEmpty() && !((BinTree) q.head()).isEmpty()) {")
for n, code in [("a", FIX_A), ("b", FIX_B), ("c", FIX_C)]:
    J5.add("L306fix" + n, code, '''        String r1, r2;
        try { r1 = levelorder(K.baue("%s")); } catch (IllegalStateException e) { r1 = "Laufzeitfehler"; }
        try { r2 = levelorder(new BinTree()); } catch (IllegalStateException e) { r2 = "Laufzeitfehler"; }
        K.out("W5-L3-06.fix%s", r1 + "#" + r2);''' % (ZB, n))
# 5.3-07 Stapel statt Schlange
T307 = "8(3(1,6),10(-,14))"
STAPEL_CODE = '''public static String raetsel(BinTree b) {
    String text = "";
    Stack s = new Stack();
    if (!b.isEmpty()) {
        s.push(b);
    }
    while (!s.isEmpty()) {
        BinTree k = (BinTree) s.pop();
        text = text + k.getItem() + " ";
        if (!k.getLeft().isEmpty()) {
            s.push(k.getLeft());
        }
        if (!k.getRight().isEmpty()) {
            s.push(k.getRight());
        }
    }
    return text;
}'''
J5.add("L307", STAPEL_CODE, jt("W5-L3-07.text", 'raetsel(K.baue("%s"))' % T307))

# ======================================================================= Level 5.4 – Daten
TB_SEQ = [41, 20, 65, 11, 29, 50, 91, 32, 72, 99]
TB = ks(bst_from(TB_SEQ))
INS402 = [55, 30]
SEQ403 = [15, 9, 23, 4, 12, 30, 19, 11, 27]
X404 = [32, 50, 95, 5]
MAXBUG = '''public static int maximum(BinTree b) {
    if (b.isEmpty()) {
        return -1;
    }
    if (b.isLeaf()) {
        return (Integer) b.getItem();
    }
    return maximum(b.getRight());
}'''
T408 = "20(10,40(30,-))"
run = '        int[] seq = {%s};\n        BinTree tb = BM.baueAus(seq);\n' % ", ".join(map(str, TB_SEQ)) + jt("W5-L4.tb", "K.k(tb)") + "\n"
run += '        BinTree b2 = BM.baueAus(seq); BM.einfuegen(b2, 55); BM.einfuegen(b2, 30);\n' + jt("W5-L4-02.baum", "K.k(b2)") + "\n"
run += '        int[] s3 = {%s};\n' % ", ".join(map(str, SEQ403)) + jt("W5-L4-03.baum", "K.k(BM.baueAus(s3))") + "\n"
for x in X404:
    run += jt("W5-L4-04.v%d" % x, "BM.vergleiche(tb, %d)" % x) + "\n" + jt("W5-L4-04.s%d" % x, "BM.suche(tb, %d)" % x) + "\n"
for x, nf, key in [(50, True, "W5-L4-05.a"), (29, True, "W5-L4-05.b"), (65, True, "W5-L4-06"), (41, False, "W5-L4-07")]:
    run += '        { BinTree t = BM.baueAus(seq); BM.loesche(t, %d, %s); K.out("%s", K.k(t)); K.out("%s.inorder", K.in(t)); }\n' % (x, "true" if nf else "false", key, key)
run += jt("W5-L4-06.nf", "BM.minimumBST(tb.getRight().getRight())") + "\n" + jt("W5-L4-07.vg", "BM.maximumBST(tb.getLeft())")
J5.add("L4", "", run)
J5.add("L408", MAXBUG, jt("W5-L4-08.tb", 'maximum(BM.baueAus(new int[]{%s}))' % ", ".join(map(str, TB_SEQ))) + "\n" +
       jt("W5-L4-08.t", 'maximum(K.baue("%s"))' % T408) + "\n" +
       '        K.out("W5-L4-08.fix", maximumFix(K.baue("%s")) + "," + maximumFix(BM.baueAus(new int[]{%s})) + "," + maximumFix(new BinTree()));' % (T408, ", ".join(map(str, TB_SEQ))),
       extra=MAXBUG.replace("maximum(", "maximumFix(").replace("b.isLeaf()", "b.getRight().isEmpty()"))

# ======================================================================= Level 5.5 – Daten
ORD501 = {"a": [1, 2, 3, 4, 5, 6, 7], "b": [4, 2, 6, 1, 3, 5, 7], "c": [7, 1, 6, 2, 5, 3, 4], "d": [4, 1, 2, 3, 7, 6, 5], "e": [7, 6, 5, 4, 3, 2, 1]}
J5.add("L501", "", "\n".join(['        K.out("W5-L5-01.%s", BM.hoehe(BM.baueAus(new int[]{%s})));' % (k, ", ".join(map(str, v))) for k, v in ORD501.items()]))
N502 = [31, 100, 2000, 4096, 500000]
R504 = [3, 8, 12, 17, 21, 26, 30, 34, 39, 45]
R505 = [5, 9, 14, 22, 31]
AUSG_CODE = '''public static BinTree ausgeglichenAus(int[] r, int lo, int hi) {
    if (lo > hi) {
        return new BinTree();
    }
    int mitte = (lo + hi) / 2;
    BinTree b = new BinTree(r[mitte]);
    b.setLeft(ausgeglichenAus(r, lo, mitte - 1));
    b.setRight(ausgeglichenAus(r, mitte + 1, hi));
    return b;
}'''
J5.add("L505", AUSG_CODE + r'''
    static String log = "";
    static BinTree aus(int[] r, int lo, int hi, int t) {
        if (lo > hi) { log += t + "|" + lo + "|" + hi + "|–|leer;"; return new BinTree(); }
        int mitte = (lo + hi) / 2; log += t + "|" + lo + "|" + hi + "|" + mitte + "|" + r[mitte] + ";";
        BinTree b = new BinTree(r[mitte]); b.setLeft(aus(r, lo, mitte - 1, t + 1)); b.setRight(aus(r, mitte + 1, hi, t + 1)); return b;
    }''', '''        int[] r4 = {%s};
        K.out("W5-L5-04.baum", K.k(ausgeglichenAus(r4, 0, r4.length - 1)));
        int[] r5 = {%s};
        K.out("W5-L5-05.baum", K.k(ausgeglichenAus(r5, 0, r5.length - 1)));
        aus(r5, 0, r5.length - 1, 0); K.out("W5-L5-05.tab", log);
        for (int n : new int[]{%s}) { if (n <= 5000) { int[] s = new int[n]; for (int i = 0; i < n; i++) s[i] = i;
            BinTree a = ausgeglichenAus(s, 0, n - 1); K.out("W5-L5-02.min" + n, BM.hoehe(a)); K.out("W5-L5-02.bst" + n, BM.istBST(a, -1, -1)); } }''' % (
    ", ".join(map(str, R504)), ", ".join(map(str, R505)), ", ".join(map(str, N502))))
BST506 = {"A": "30(15(8,22),45(38,60))", "B": "30(15(8,35),45(38,60))", "C": "30(15(8,22),45(28,60))", "D": "30(15(-,22),45(-,60(52,70)))"}
J5.add("L506", "", "\n".join(['        K.out("W5-L5-06.%s", BM.istBST(K.baue("%s"), -1, -1) + "," + BM.nurKinder(K.baue("%s")));' % (k, v, v) for k, v in BST506.items()]))
F507 = "40(20(10,30(-,45)),60(50,70))"
J5.add("L507", "", '''        BinTree f = K.baue("%s");
        K.out("W5-L5-07.nur", BM.nurKinder(f)); K.out("W5-L5-07.ist", BM.istBST(f, -1, -1)); K.out("W5-L5-07.suche45", BM.suche(f, 45));
        K.out("W5-L5-07.suche10", BM.suche(f, 10)); K.out("W5-L5-07.in", K.in(f));''' % F507)
T508 = {
    "t1": "public static boolean istBST(BinTree b, int min, int max) {",
    "t2": "if (b.isEmpty()) {\n    return true;\n}",
    "t3": "int wert = (Integer) b.getItem();",
    "t4": "if (wert <= min) {\n    return false;\n}",
    "t5": "if (max != -1 && wert >= max) {\n    return false;\n}",
    "t6": "return istBST(b.getLeft(), min, wert) && istBST(b.getRight(), wert, max);\n}",
    "d1": "if (wert >= max) {\n    return false;\n}",
    "d2": "return istBST(b.getLeft(), min, max) && istBST(b.getRight(), min, max);\n}",
    "d3": "return istBST(b.getLeft(), wert, max) && istBST(b.getRight(), min, wert);\n}",
}
TEST_BST = "\n".join(['            if (istBST(K.baue("%s"), -1, -1) != %s) throw new RuntimeException("%s");' % (s, "true" if e else "false", s)
                      for s, e in [(BSP, True), (ZB, False), (F507, False), (BST506["B"], False), (BST506["C"], False), (BST506["D"], True),
                                   ("8(3(1,9),10)", False), ("8(3,10(5,14))", False), ("5(5,-)", False), ("0(-,1)", True), (ENT, True)]] +
                     ['            if (!istBST(new BinTree(), -1, -1)) throw new RuntimeException("leer");'])
OC508 = OrderCheck(J5, "W5-L5-08", T508, ["t1", "t2", "t3"], ["t4", "t5"], ["t6"], TEST_BST, "O508")
OC508d = [OrderCheck(J5, "W5-L5-08d%d" % i, T508, ["t1", "t2", "t3"] + mid, [], [last], TEST_BST, "O508d%d" % i)
          for i, (mid, last) in enumerate([(["t4", "d1"], "t6"), (["t4", "t5"], "d2"), (["t4", "t5"], "d3")])]

# ======================================================================= Level 5.6 – Daten (Transfer)
HEAP602 = {"A": "90(60(30,50),80(70,-))", "B": "90(60(30,50),80(-,70))", "C": "90(60(30,65),80(70,-))", "D": "85(85(40,20),60)"}
HEAP603 = "90(70(40,65),80(55,-))"
HEAP_INS = [85, 95]
HUFF = "•(•(E,L),•(F,•(B,N)))"
HUFF_WORT_DEC = "LEBEN"; HUFF_WORT_ENC = "NEBEL"
RUNE = "T(A(L*(-,U*),O(R*(F*,-),-)),-)"
PRUEFE = '''public static boolean pruefe(BinTree b) {
    if (b.isEmpty()) {
        return true;
    }
    int w = (Integer) b.getItem();
    if (!b.getLeft().isEmpty() && (Integer) b.getLeft().getItem() > w) {
        return false;
    }
    if (!b.getRight().isEmpty() && (Integer) b.getRight().getItem() > w) {
        return false;
    }
    return pruefe(b.getLeft()) && pruefe(b.getRight());
}'''
J5.add("L607", PRUEFE, "\n".join([jt("W5-L6-07.%s" % k, 'pruefe(K.baue("%s"))' % HEAP602[k]) for k in "ABC"]))

# ======================================================================= Boss – Daten
B01 = "3(7(5,-),1(8(2,9),4))"
B02 = "12(4(9,-),7(3(-,6),1))"
B03_SEQ = [47, 23, 71, 12, 35, 60, 88, 29, 40, 66]; B03 = ks(bst_from(B03_SEQ)); B03_X = 40
B04 = "7(3(1,-),9(8,12(10,-)))"
B06_SEQ = [33, 18, 50, 9, 27, 41, 62, 21, 45]
B07 = B03; B07_X = 23
B08 = "5(2(-,8),6)"
EINF_BUG = '''public static void einfuegen(BinTree b, int x) {
    if (b.isEmpty()) {
        b = new BinTree(x);
        return;
    }
    int wert = (Integer) b.getItem();
    if (x < wert) {
        einfuegen(b.getLeft(), x);
    } else if (x > wert) {
        einfuegen(b.getRight(), x);
    }
}'''
B10 = "2(9(4,7),5(-,3))"
B11 = '''public static boolean suche(BinTree b, int x) {
    if ([[g1]]) {
        return false;
    }
    int wert = [[g2]];
    if (x == wert) {
        return true;
    }
    if (x < wert) {
        return [[g3]];
    }
    return [[g4]];
}'''
B11_L = {"g1": ["b.isEmpty()"], "g2": ["(Integer)b.getItem()", "((Integer)b.getItem())", "(int)b.getItem()"],
         "g3": ["suche(b.getLeft(),x)"], "g4": ["suche(b.getRight(),x)"]}
B12 = "A(B(-,D),C(E(F,G),-))"
T513 = {
    "t1": "public static int anzahlAufEbene(BinTree b, int ebene) {",
    "t2": "if (b.isEmpty()) {\n    return 0;\n}",
    "t3": "if (ebene == 0) {\n    return 1;\n}",
    "t4": "return anzahlAufEbene(b.getLeft(), ebene - 1)\n     + anzahlAufEbene(b.getRight(), ebene - 1);\n}",
    "d1": "return anzahlAufEbene(b.getLeft(), ebene)\n     + anzahlAufEbene(b.getRight(), ebene);\n}",
    "d2": "if (b.isLeaf()) {\n    return 1;\n}",
    "d3": "if (ebene == 0) {\n    return 0;\n}",
}
TEST_EBENE = "\n".join(['            if (anzahlAufEbene(K.baue("%s"), %d) != %d) throw new RuntimeException("%s/%d");' % (ZB, e, w, ZB, e)
                        for e, w in [(0, 1), (1, 2), (2, 3), (3, 1), (4, 0)]] +
                       ['            if (anzahlAufEbene(K.baue("%s"), %d) != %d) throw new RuntimeException("bsp%d");' % (BSP, e, w, e) for e, w in [(0, 1), (2, 3), (3, 3)]] +
                       ['            if (anzahlAufEbene(new BinTree(), 0) != 0) throw new RuntimeException("leer");'])
OC513 = OrderCheck(J5, "W5-B-13", T513, ["t1"], ["t2", "t3"], ["t4"], TEST_EBENE, "OB13")
OC513d = [OrderCheck(J5, "W5-B-13d%d" % i, T513, ["t1"] + mid, [], [last], TEST_EBENE, "OB13d%d" % i)
          for i, (mid, last) in enumerate([(["t2", "t3"], "d1"), (["t2", "d2"], "t4"), (["t2", "d3"], "t4")])]
B14 = "50(30(20,60),70(55,80))"
B15 = "*(−(9,4),+(/(8,2),3))"
run = "\n".join([trav("B01", B01), trav("B02", B02), trav("B12", B12, True), trav("B15", B15, True),
                 jt("W5-B-15.wert", 'BM.berechne(K.baueS("%s"))' % B15),
                 jt("W5-B-03.tb", "K.k(BM.baueAus(new int[]{%s}))" % ", ".join(map(str, B03_SEQ))),
                 jt("W5-B-03.v", "BM.vergleiche(BM.baueAus(new int[]{%s}), %d)" % (", ".join(map(str, B03_SEQ)), B03_X)),
                 jt("W5-B-06.baum", "K.k(BM.baueAus(new int[]{%s}))" % ", ".join(map(str, B06_SEQ))),
                 '        { BinTree t = BM.baueAus(new int[]{%s}); BM.loesche(t, %d, true); K.out("W5-B-07.baum", K.k(t)); K.out("W5-B-07.nf", BM.minimumBST(BM.baueAus(new int[]{%s}).getLeft().getRight())); }' % (
                     ", ".join(map(str, B03_SEQ)), B07_X, ", ".join(map(str, B03_SEQ))),
                 jt("W5-B-04.knoten", 'BM.anzahlKnoten(K.baue("%s"))' % B04), jt("W5-B-04.blaetter", 'BM.anzahlBlaetter(K.baue("%s"))' % B04),
                 jt("W5-B-04.hoehe", 'BM.hoehe(K.baue("%s"))' % B04), jt("W5-B-04.ebene10", 'BM.ebeneVon(K.baue("%s"), 10, 0)' % B04),
                 '        { BinTree f = K.baue("%s"); K.out("W5-B-14.nur", BM.nurKinder(f)); K.out("W5-B-14.ist", BM.istBST(f, -1, -1)); K.out("W5-B-14.s60", BM.suche(f, 60)); K.out("W5-B-14.s55", BM.suche(f, 55)); }' % B14,
                 ])
J5.add("BT", "", run)
J5.add("B08", r'''
    static String log = "";
    static int blaetter(BinTree b, int t) {
        int idx = log.length(); String kn = b.isEmpty() ? "leer" : "" + b.getItem();
        java.util.ArrayList<String> dummy = null;
        int e;
        String eigen = t + "|" + kn + "|";
        log += eigen + "#;";
        if (b.isEmpty()) { e = 0; }
        else if (b.isLeaf()) { e = 1; }
        else { e = blaetter(b.getLeft(), t + 1) + blaetter(b.getRight(), t + 1); }
        int p = log.indexOf(eigen + "#;", idx);
        log = log.substring(0, p) + eigen + e + ";" + log.substring(p + eigen.length() + 2);
        return e;
    }''', '        blaetter(K.baue("%s"), 0); K.out("W5-B-08.tab", log);' % B08)
J5.add("B09bug", EINF_BUG, '''        BinTree t = BM.baueAus(new int[]{%s}); einfuegen(t, 44); K.out("W5-B-09.nach", K.k(t));
        BinTree l = new BinTree(); einfuegen(l, 7); K.out("W5-B-09.leer", l.isEmpty());''' % ", ".join(map(str, B03_SEQ)))
J5.add("B09fix", EINF_BUG.replace("b = new BinTree(x);", "b.setItem(x);"), '''        BinTree t = BM.baueAus(new int[]{%s}); einfuegen(t, 44); K.out("W5-B-09.fix", K.k(t));''' % ", ".join(map(str, B03_SEQ)))
for i, v2 in enumerate(B11_L["g2"]):
    code = B11.replace("[[g1]]", "b.isEmpty()").replace("[[g2]]", v2).replace("[[g3]]", "suche(b.getLeft(), x)").replace("[[g4]]", "suche(b.getRight(), x)")
    J5.add("B11_%d" % i, code, '''        BinTree t = BM.baueAus(new int[]{%s}); String s = "";
        for (int x = 0; x <= 100; x++) { if (suche(t, x) != BM.suche(t, x)) s += x + " "; }
        K.out("W5-B-11.v%d", s.length() == 0 ? "OK" : s);
        K.out("W5-B-11.nurEinWeg%d", suche(K.baue("8(3,10(5,-))"), 5));''' % (", ".join(map(str, B03_SEQ)), i, i))

# #######################################################################################
#  Java ausfuehren
# #######################################################################################
J = J5.run()
def jv(k):
    assert k in J, "Java-Schluessel fehlt: " + k
    return J[k]
def same(py, key):
    """Python-Ergebnis muss mit Java uebereinstimmen"""
    assert str(py) == jv(key), "Abweichung %s: Python %r, Java %r" % (key, py, jv(key))
    chk.append(key)
    return py

# Traversierungen Python vs. Java
for name, s in TRAV.items():
    t = parse(s)
    same(wl(vals(nodes_pre(t))), "trav.%s.pre" % name); same(wl(vals(nodes_in(t))), "trav.%s.in" % name)
    same(wl(vals(nodes_post(t))), "trav.%s.post" % name); same(wl(vals(nodes_level(t))), "trav.%s.level" % name)
    same(ks(t), "trav.%s.k" % name)

# ---------------------------------------------------------------- Helfer fuer Gap-Tabellen
LEER = ["leer", "–", "-", "leerer Baum", "leererBaum"]
def zell_feld(art, wert):
    """art: 'zahl' | 'knoten' | 'tf' | 'wf' | 'text'  -> (feld, akzeptiert)"""
    if art == "zahl": return Z(4), [str(wert)]
    if art == "knoten":
        if wert in ("leer", "–"): return TX("text", 6), LEER
        return TX("text", 6), [str(wert)]
    if art == "tf": return AW(["true", "false"]), [str(wert)]
    if art == "wf": return AW(WF), [str(wert)]
    if art == "text": return TX("text", 10), ([str(wert)] if not isinstance(wert, list) else wert)
    if art == "liste":
        if wert == "–": return TX("text", 12), LEER
        return TX("text", 12), [wert, wert.replace(", ", ","), wert.replace(", ", " ")]
    raise ValueError(art)

def gap_tab(kopf, rows, spalten, praefix, fest=()):
    """rows: Loesungszeilen (Strings); spalten: {spaltenindex: art}; fest: Zeilenindizes ohne Luecken."""
    zeilen, felder, loes = [], {}, {}
    for i, row in enumerate(rows):
        z = []
        for c, wert in enumerate(row):
            if c in spalten and i not in fest and not (wert == "–" and spalten[c] in ("zahl", "tf", "wf")):
                fid = "%s%d%s" % (praefix, i + 1, "abcdefgh"[c])
                f, acc = zell_feld(spalten[c], wert)
                felder[fid] = f; loes[fid] = acc
                z.append("[[%s]]" % fid)
            else:
                z.append(wert)
        zeilen.append(z)
    return TAB(kopf, zeilen), felder, loes

def klick(ids_paths):
    return {"folge": ids_paths}

LEVELS, AUFG = [], []
def level(id, nr, titel, ds, ab, ide, intro, tasks):
    LEVELS.append({"id": id, "nr": nr, "titel": titel, "ds": ds, "ab": ab, "ide": ide, "intro": intro,
                   "aufgaben": [t["id"] for t in tasks]})
    AUFG.extend(tasks)

PRUEF_HINWEIS = "Klammerform: `wert(links,rechts)`, `-` = leerer Teilbaum, ein Blatt schreibt man nur als `wert`."

# #######################################################################################
#  LEVEL 5.1
# #######################################################################################
tq = parse(Q); tn1 = parse(N1)
L1 = []
L1.append(task("W5-L1-01", "Begriffe an der Eulen-Eiche", 1, "Bäume", [],
    [T("Die Eulen des Waldes wohnen in diesem Binärbaum. Beantworte die Fragen mit den Begriffen aus dem Merkkasten des Levels."), BAUM(Q),
     T("- Wurzel: [[w]]\n- Anzahl der Blätter: [[b]]\n- Anzahl der inneren Knoten: [[i]]\n- Höhe des Baums: [[h]]\n- Ebene des Knotens H: [[e]]\n- Höhe des Teilbaums mit der Wurzel E: [[he]]")],
    gaps({"w": TX("text", 3), "b": Z(), "i": Z(), "h": Z(), "e": Z(), "he": Z()}),
    {"w": ["K"], "b": [jv("W5-L1-01.blaetter")], "i": [jv("W5-L1-01.innere")], "h": [jv("W5-L1-01.hoehe")],
     "e": [jv("W5-L1-01.ebeneH")], "he": [jv("W5-L1-01.hoeheE")]},
    [T("Blätter (beide Teilbäume leer): %s – also %s. Innere Knoten (mindestens ein Kind): K, E, G, T, R – also %s. "
       "Der längste Weg K → E → G → H bzw. K → T → R → P hat 4 Knoten, die Höhe ist **%s** (leerer Baum 0, Blatt 1). "
       "H liegt auf **Ebene %s** (Wurzel = Ebene 0). Der Teilbaum E(A,G(-,H)) hat die Höhe %s." % (
           ", ".join(blaetter(tq)), jv("W5-L1-01.blaetter"), jv("W5-L1-01.innere"), same(hoehe(tq), "W5-L1-01.hoehe"),
           jv("W5-L1-01.ebeneH"), jv("W5-L1-01.hoeheE"))),
     H("Achtung: G ist **kein** Blatt – G hat das rechte Kind H. Ein Knoten mit nur einem Kind ist ein innerer Knoten.")],
    ["Höhe = Anzahl der Ebenen. Zähle die Knoten auf dem längsten Weg von der Wurzel nach unten."]))

pre1 = nodes_pre(tn1)
L1.append(task("W5-L1-02", "Preorder – Wurzel zuerst", 1, "Bäume", [],
    [T("Klicke die Knoten in **Preorder**-Reihenfolge an (Wurzel – links – rechts, rekursiv für jeden Teilbaum).")],
    tree_klick(N1), klick(paths(pre1)),
    [T("Preorder: **%s**. Erst die Wurzel 6, dann der ganze linke Teilbaum (2, 7, 4, 1), danach der rechte (9, 3, 5, 8)." % " ".join(vals(pre1))),
     H("Tipp „Rundgang“: Umrunde den Baum links an der Wurzel beginnend – notiere jeden Knoten, wenn du **links** an ihm vorbeikommst.")]))

in1 = nodes_in(tn1)
L1.append(task("W5-L1-03", "Inorder – links, Wurzel, rechts", 1, "Bäume", [],
    [T("Klicke die Knoten in **Inorder**-Reihenfolge an (links – Wurzel – rechts).")],
    tree_klick(N1), klick(paths(in1)),
    [T("Inorder: **%s**. Der linke Teilbaum von 6 liefert 7 2 4 1 (bei 4 ist links leer, also zuerst 4, dann 1). "
       "Bei 9 ist der linke Teilbaum leer – deshalb folgt die 9 direkt auf die 6." % " ".join(vals(in1)))],
    ["Ein leerer linker Teilbaum liefert nichts – dann kommt sofort der Knoten selbst."]))

L1.append(task("W5-L1-04", "Vom Code zum Baum", 2, "Bäume", ["P1"],
    [T("Die Anweisungen werden nacheinander ausgeführt. Baue den Baum **w** nach Zeile 10 auf. Nicht jeder Wert in der Auswahl wird gebraucht."),
     C(CODE_L104)],
    tree_bauen("-", [4, 8, 1, 6, 3, 5, 2, 9, 7]), {"baum": same(norm("4(8(-,3(5,-)),1(6,2))"), "W5-L1-04.w")},
    [T("Ergebnis: `%s`." % jv("W5-L1-04.w")),
     T("- Zeile 4: `w.getRight().getLeft()` ist ein **leerer** Teilbaum (nicht null) – `setItem(6)` macht ihn zum Blatt.\n"
       "- Zeile 5: `h` ist eine **Referenz** auf den linken Teilbaum von w. Zeilen 6 und 7 verändern deshalb w.\n"
       "- Zeile 9: `h = new BinTree(9)` lässt h auf ein **neues** Objekt zeigen. Zeilen 9 und 10 ändern w nicht mehr – 9 und 7 gehören nicht in den Baum."),
     H("P1 im Blick: `getRight()` auf einem leeren Baum wäre ein Laufzeitfehler – `setItem` auf einem leeren Baum ist dagegen erlaubt.")],
    ["Zeichne nach jeder Zeile mit. Welche Zeilen ändern wirklich w – und ab wann zeigt h auf etwas anderes?"]))

L105_LOES = {k: jv("W5-L1-05.%s" % k) for k, a in L105_AUSDR}
L1.append(task("W5-L1-05", "Was liefert der Ausdruck?", 2, "Bäume", ["P1", "P4"],
    [T("Nach Zeile 10 des Codes werden die Ausdrücke ausgewertet. Gib den Wert an – oder „Laufzeitfehler“."), C(CODE_L104),
     TAB(["Ausdruck", "Wert"], [["`%s`" % a, "[[%s]]" % k] for k, a in L105_AUSDR])],
    gaps({k: (Z() if k == "c" else AW(TFL)) for k, a in L105_AUSDR}),
    {k: [v] for k, v in L105_LOES.items()},
    [T("w = `%s`, h = `%s`." % (jv("W5-L1-04.w"), jv("W5-L1-04.h"))),
     T("- a) 8 hat das rechte Kind 3 → **false**.\n- b) h ist der neue Baum 9 mit dem linken Kind 7 → **false**.\n"
       "- c) `(Integer)` castet den Inhalt 1, dann + 5 → **6** (P4: ohne Cast kein Rechnen mit Object).\n"
       "- d) links von 8 ist ein leerer Baum → **true**.\n- e) `getItem()` auf dem leeren Baum → **Laufzeitfehler** (P1, IllegalStateException).\n"
       "- f) 2 hat zwei leere Teilbäume → **true**.")],
    ["Ein nicht leerer Baum hat immer zwei Teilbäume – notfalls leere, nie null."]))

t106 = from_pre_in(PRE106, IN106)
L1.append(task("W5-L1-06", "Rekonstruktion aus Pre- und Inorder", 3, "Bäume", [],
    [T("Von einem Baum kennt man nur zwei Traversierungen:\n\n- Preorder: `%s`\n- Inorder: `%s`\n\nBaue den Baum auf." % (" ".join(PRE106), " ".join(IN106)))],
    tree_bauen("-", PRE106), {"baum": ks(t106)},
    [T("Die Preorder beginnt mit der Wurzel **E**. In der Inorder steht links von E der linke Teilbaum (U A L), rechts davon der rechte (T R S)."),
     T("Links: Preorder U L A → Wurzel U; in der Inorder steht vor U nichts, also ist links von U leer und rechts liegt (A L) mit der Wurzel L und dem linken Kind A. "
       "Rechts: Wurzel R mit T links und S rechts."),
     BAUM(ks(t106)),
     T("Ergebnis `%s`. Kontrolle Postorder: %s." % (ks(t106), " ".join(vals(nodes_post(t106)))))],
    ["Erstes Element der Preorder = Wurzel. Teile die Inorder an der Wurzel – links davon liegt der linke Teilbaum.",
     "Wende dasselbe Verfahren rekursiv auf die beiden Teilbäume an."]))
assert wl(vals(nodes_pre(t106))) == wl(PRE106) and wl(vals(nodes_in(t106))) == wl(IN106)

L1.append(task("W5-L1-07", "Ein Termbaum für den Zaubertrank", 2, "Bäume", [],
    [T("Der Alchemist braucht den Termbaum (Inhaltstyp Zeichenkette) zum Term\n\n`(6 + 2) * 5 + 12 / 4`\n\n"
       "Es gilt Punkt vor Strich, `/` rechnet ganzzahlig. Baue den Termbaum und gib seinen Wert an: [[wert]]")],
    [tree_bauen("-", ["+", "+", "*", "/", "6", "2", "5", "12", "4"]), gaps({"wert": Z()})],
    [{"baum": norm(TERM107)}, {"wert": [same(43, "W5-L1-07.wert")]}],
    [T("Die **Wurzel** ist das Rechenzeichen, das zuletzt ausgewertet wird – das zweite `+` (Punkt vor Strich). "
       "Links steht `(6 + 2) * 5`, rechts `12 / 4`."), BAUM(TERM107),
     T("Wert: (6 + 2) · 5 + 12 / 4 = 40 + 3 = **43**. Kontrolle Postorder: %s – das ist die Postfix-Schreibweise." % jv("trav.T107.post").strip())],
    ["Welches Rechenzeichen wird zuletzt ausgeführt? Das ist die Wurzel."]))

post108 = nodes_post(parse(TERM108))
L1.append(task("W5-L1-08", "Postorder = Postfix", 2, "Bäume", [],
    [T("Klicke die Knoten des Termbaums in **Postorder** an (links – rechts – Wurzel). So entsteht die Postfix-Schreibweise aus Welt 4.")],
    tree_klick(TERM108), klick(paths(post108)),
    [T("Postorder: **%s**. Jedes Rechenzeichen steht hinter seinen beiden Operanden – genau so rechnet der Postfix-Rechner mit einem Stapel. "
       "Wert des Terms: (1 + 3) · 5 − 8 / 2 = **%s**." % (" ".join(vals(post108)), same(16, "W5-L1-08.wert")))]))

level("W5-L1", "5.1", "Wegweiser im Wald – Binärbäume und Traversierungen", [31], "AB 1 Binärbäume, Teil 1 (DS 31)",
      "AQ_W5_L5_Wald_Geruest.txt – Level 5.1 (Klasse Baum, Testklasse L51BaumTest)",
      [T("Ein **Binärbaum** ist leer oder besteht aus einer Wurzel mit Inhalt und zwei Teilbäumen. "
         "**Höhe**: leerer Baum 0, Blatt 1, sonst 1 + größere Höhe der Teilbäume. **Ebene**: Wurzel = Ebene 0."),
       H("**Traversierungen:** Preorder = Wurzel, links, rechts · Inorder = links, Wurzel, rechts · Postorder = links, rechts, Wurzel. "
         "`BinTree` ist nicht generisch: `int x = (Integer) b.getItem();`")], L1)

# #######################################################################################
#  LEVEL 5.2
# #######################################################################################
tg = parse(G)
L2 = []
L2.append(task("W5-L2-01", "Vier Fragen an einen Baum", 1, "Bäume", [],
    [T("Die Methoden aus Level 5.1 und 5.2 werden mit dem Baum b aufgerufen. Gib die Rückgaben an."), BAUM(G),
     TAB(["Aufruf", "Rückgabe"], [["`anzahlKnoten(b)`", "[[k]]"], ["`anzahlBlaetter(b)`", "[[bl]]"], ["`hoehe(b)`", "[[h]]"],
                                  ["`summe(b)`", "[[s]]"], ["`maximum(b)`", "[[m]]"]])],
    gaps({"k": Z(), "bl": Z(), "h": Z(), "s": Z(), "m": Z()}),
    {"k": [same(anzahl(tg), "W5-L2-01.knoten")], "bl": [same(len(blaetter(tg)), "W5-L2-01.blaetter")], "h": [same(hoehe(tg), "W5-L2-01.hoehe")],
     "s": [same(sum(int(v) for v in vals(nodes_pre(tg))), "W5-L2-01.summe")], "m": [same(max(int(v) for v in vals(nodes_pre(tg))), "W5-L2-01.maximum")]},
    [T("Knoten: %s. Blätter: %s (%d Stück). Höhe: %d (Weg 6 → 4 → 7 → 1). Summe: %s. Maximum: %s (die 9 ist ein innerer Knoten – das Maximum muss kein Blatt sein)." % (
        jv("W5-L2-01.knoten"), ", ".join(blaetter(tg)), len(blaetter(tg)), hoehe(tg), jv("W5-L2-01.summe"), jv("W5-L2-01.maximum")))]))

rows = [z.split("|") for z in jv("W5-L2-02.tab").strip(";").split(";")]
blk, fel, loe = gap_tab(["Rekursionstiefe", "Aufruf", "l", "r", "Rückgabe"],
                        [[r[0], "hoehe(%s)" % r[1], r[2], r[3], r[4]] for r in rows], {0: "zahl", 2: "zahl", 3: "zahl", 4: "zahl"}, "z", fest=(0,))
blk["zeilen"][0] = [rows[0][0], "hoehe(9)", "[[z1c]]", "[[z1d]]", "[[z1e]]"]
fel.update({"z1c": Z(4), "z1d": Z(4), "z1e": Z(4)}); loe.update({"z1c": [rows[0][2]], "z1d": [rows[0][3]], "z1e": [rows[0][4]]})
L2.append(task("W5-L2-02", "Wie hoch reicht der Ast?", 2, "Rekursionstabelle", ["P7", "P8"],
    [T("Dokumentiere den Aufruf `hoehe(t)` für den Baum t in der Rekursionstabelle. Die Aufrufe stehen in der Reihenfolge, in der sie **beginnen**; "
       "`hoehe(leer)` ist ein Aufruf mit leerem Teilbaum. Der Erstaufruf hat die Rekursionstiefe 0."), BAUM(T202), C(HOEHE_CODE), blk],
    gaps(fel), loe,
    [T("Jeder der 4 Knoten löst einen Aufruf aus, dazu kommt je ein Aufruf für die 5 leeren Teilbäume: 2 · 4 + 1 = **9 Aufrufe**. "
       "Die Rückgaben entstehen von innen nach außen: Blätter liefern 1 + 0 = 1, der Knoten 4 liefert 1 + max(0, 1) = 2, die Wurzel 1 + max(2, 1) = **3**."),
     H("P7/P8: Erstaufruf = Tiefe 0, leere Teilbäume mitzählen, Rückgabe eines Blatts ist 1 (nicht 0).")],
    ["Arbeite wie der Rechner: Erst wird der komplette linke Teilbaum abgearbeitet, dann der rechte."]))

L2.append(task("W5-L2-03", "Der Ast bricht", 2, "Fehler im Java-Code", ["P1", "P7"],
    [T("`anzahlBlaetter` soll die Anzahl der Blätter liefern (leerer Baum: 0). Beim Aufruf mit dem zahlenbaum stürzt die Methode ab."), BAUM(ZB), C(BLATT_BUG),
     T("Teil 1: Markiere die Zeile, in der der Laufzeitfehler auftritt. Teil 2: Wähle die passende Korrektur.")],
    [lines(2, 1), choice([("a", "Die Abfragen tauschen: zuerst `if (b.isEmpty())` mit `return 0;`, danach `if (b.isLeaf())` mit `return 1;`."),
                          ("b", "Zeile 2 ersetzen durch `if (b != null)`."),
                          ("c", "Zeile 8 ersetzen durch `return 1 + anzahlBlaetter(b.getLeft()) + anzahlBlaetter(b.getRight());`"),
                          ("d", "Die Abfrage in Zeilen 5–7 löschen, weil sie nie erreicht wird.")])],
    [{"zeilen": [int(jv("W5-L2-03.bug"))]}, {"richtig": ["a"]}],
    [T("Der Knoten 4 hat einen **leeren** linken Teilbaum. Der rekursive Aufruf für diesen leeren Baum führt Zeile 2 aus: `isLeaf()` auf einem leeren Baum "
       "→ IllegalStateException. Die Prüfung `isEmpty()` in Zeile 5 kommt zu spät."),
     T("Korrigiert liefert die Methode %s für den zahlenbaum und %s für den leeren Baum. `b != null` hilft nicht – ein leerer Teilbaum ist nie null." % (
         jv("W5-L2-03.ok"), jv("W5-L2-03.okleer"))),
     H("P1 + P7: Der Basisfall `if (b.isEmpty())` gehört **ganz nach oben**. Fies: Für Bäume, in denen jeder innere Knoten zwei Kinder hat (z. B. `7(3,9)`), "
       "läuft die fehlerhafte Methode fehlerfrei (Ergebnis %s) – ein Test nur mit solchen Bäumen findet den Fehler nicht." % jv("W5-L2-03.bspbug"))]))

L2.append(task("W5-L2-04", "Der Compiler meckert", 1, "Fehler im Java-Code", ["P4"],
    [T("`summe` soll die Summe aller Werte eines BinTree vom Inhaltstyp Ganzzahl liefern. Der Compiler meldet einen Fehler."), C(SUMME_BUG),
     T("Teil 1: Markiere die fehlerhafte Zeile. Teil 2: Korrigiere sie: `int w = [[k]] b.getItem();`")],
    [lines(1, 1), gaps({"k": TX("code", 10)})],
    [{"zeilen": [int(jv("W5-L2-04.zeile"))]}, {"k": ["(Integer)"]}],
    [T("Zeile %s: `getItem()` liefert `Object` – das passt nicht ohne Cast in eine int-Variable (javac: „%s“)." % (jv("W5-L2-04.zeile"), jv("W5-L2-04.zeile.msg"))),
     T("Richtig: `int w = (Integer) b.getItem();` Danach liefert `summe(zahlenbaum)` den Wert %s." % jv("W5-L2-04.summe")),
     H("P4 – Typen und Casts: Bei den Klassen der Bibliothek „Niedersachsen“ (Stack, Queue, DynArray, BinTree) wird **jeder** Inhalt gecastet.")]))

v205 = OC205.gueltig(J)
assert ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8"] in v205 and not OC205d.gueltig(J)
L2.append(task("W5-L2-05", "Puzzle: Das Maximum im Geäst", 2, "Methode implementieren", ["P4", "P7"],
    [T("Setze die Methode `maximum(b: BinTree vom Inhaltstyp Ganzzahl): Ganzzahl` zusammen. Sie liefert den größten Wert, beim leeren Baum −1 "
       "(alle Werte sind ≥ 0, der Baum ist **kein** Suchbaum). Drei Teile sind Fallen und gehören nicht hinein.")],
    order([(k, T205[k]) for k in ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "d1", "d2", "d3"]]),
    {"reihenfolgen": v205},
    [C("\n".join(T205[k] for k in ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8"])),
     T("Der Basisfall steht zuerst – sonst würde `getItem()` auf dem leeren Baum abstürzen. Die Reihenfolge der Zeilen mit `max`, `l` und `r` ist teilweise frei "
       "(alle %d gültigen Reihenfolgen wurden per Testlauf geprüft)." % len(v205)),
     T("Fallen: `int max = b.getItem();` ohne Cast (P4); `return 0;` im Basisfall verletzt die Vorgabe −1; `maximum(b.getLeft());` verwirft das Ergebnis des rekursiven Aufrufs (P7).")]))

STR206 = STR("geheim(b: BinTree vom Inhaltstyp Ganzzahl): Ganzzahl", [
    {"wenn": "b.isEmpty()", "dann": [{"gib": "0"}], "sonst": []},
    {"anw": "anzahl ← geheim(b.getLeft()) + geheim(b.getRight())"},
    {"wenn": "b.getLeft().isEmpty() und nicht b.getRight().isEmpty()", "dann": [{"anw": "anzahl ← anzahl + 1"}], "sonst": []},
    {"wenn": "nicht b.getLeft().isEmpty() und b.getRight().isEmpty()", "dann": [{"anw": "anzahl ← anzahl + 1"}], "sonst": []},
    {"gib": "anzahl"}])
L2.append(task("W5-L2-06", "Das geheime Struktogramm", 2, "Struktogramm lesen", ["P10"],
    [STR206, T("Gib die Rückgaben an: `geheim(zahlenbaum)` = [[a]], `geheim(entartet())` = [[b]], `geheim(t)` = [[c]] für den Baum t:"), BAUM(G),
     T("Wähle danach die Beschreibung, die genau erläutert, was `geheim` berechnet.")],
    [gaps({"a": Z(), "b": Z(), "c": Z()}),
     choice([("a", "Die Anzahl der Knoten mit **genau einem** Kind – jeder Knoten wird geprüft, die Ergebnisse der Teilbäume werden addiert."),
             ("b", "Die Anzahl der Blätter."), ("c", "Die Anzahl der inneren Knoten."),
             ("d", "Die Anzahl der leeren Teilbäume.")])],
    [{"a": [jv("W5-L2-06.zb")], "b": [jv("W5-L2-06.ent")], "c": [jv("W5-L2-06.g")]}, {"richtig": ["a"]}],
    [T("Die beiden Verzweigungen sind zusammen genau dann wahr, wenn ein Teilbaum leer ist und der andere nicht – der Knoten hat genau ein Kind."),
     T("zahlenbaum `%s`: Knoten 4 (nur rechts) und die untere 9 (nur links) → **%s**. entartet(): 1, 2, 3, 4 haben je nur ein rechtes Kind → **%s**. "
       "t: nur 9 → **%s**." % (ZB, jv("W5-L2-06.zb"), jv("W5-L2-06.ent"), jv("W5-L2-06.g"))),
     H("P10: „erläutern“ heißt nicht nur nennen („zählt Knoten“), sondern sagen, **welche** Knoten und **warum** – mit Bezug zu den Bedingungen.")]))

loes207 = {k: v for k, v in L207.items()}
for i in range(3):
    assert jv("W5-L2-07.v%d.zb4" % i) == "4" and jv("W5-L2-07.v%d.bsp7" % i) == "4" and jv("W5-L2-07.v%d.leer" % i) == "0"
L2.append(task("W5-L2-07", "Lückencode: Wer ist größer?", 2, "Lückencode", ["P4", "P7"],
    [T("`anzahlGroesser(b, grenze)` liefert, wie viele Werte im Baum größer als `grenze` sind (beliebiger Baum, kein Suchbaum). "
       "Beispiel: zahlenbaum, grenze 4 → 4 (5, 9, 7, 9). Ergänze die Lücken."), C(LUECKE207)],
    gaps({"g1": TX("code", 14), "g2": TX("code", 4), "g3": TX("code", 30), "g4": TX("code", 20)}), loes207,
    [C(LUECKE207.replace("[[g1]]", "b.isEmpty()").replace("[[g2]]", "0").replace("[[g3]]", "anzahlGroesser(b.getRight(), grenze)").replace("[[g4]]", "(Integer) b.getItem()")),
     T("Bauplan: Basisfall leer → 0 · beide Teilbäume rekursiv, Ergebnisse **verwenden** (P7) · Wurzel auswerten mit Cast (P4) · verknüpfen. "
       "Mit der Musterlösung: zahlenbaum/4 → %s, beispielBST/7 → %s, leerer Baum → %s." % (jv("W5-L2-07.v0.zb4"), jv("W5-L2-07.v0.bsp7"), jv("W5-L2-07.v0.leer")))]))

rows = [z.split("|") for z in jv("W5-L2-08.tab").strip(";").split(";")]
blk, fel, loe = gap_tab(["Rekursionstiefe", "Knoten (Wert oder leer)", "Rückgabe"], rows, {0: "zahl", 1: "knoten", 2: "tf"}, "z")
blk["zeilen"][0][0] = "0"; blk["zeilen"][0][1] = "3"; del fel["z1a"], fel["z1b"], loe["z1a"], loe["z1b"]
L2.append(task("W5-L2-08", "Kurzschluss im Unterholz", 3, "Rekursionstabelle", ["P7", "P8"],
    [T("Dokumentiere den Aufruf `enthaelt(t, 6)` in der Rekursionstabelle (Aufrufe in der Reihenfolge ihres Beginns, leere Teilbäume als „leer“). "
       "Beachte: `||` wertet den rechten Aufruf nur aus, wenn der linke `false` geliefert hat."), BAUM(T208), C(ENTHAELT_CODE), blk,
     T("Wie viele Aufrufe gibt es insgesamt? [[n]]")],
    gaps(dict(fel, n=Z())), dict(loe, n=[str(len(rows))]),
    [T("Die Suche geht zuerst in den linken Teilbaum (8). Dort findet sie bei 1 nichts (zwei Aufrufe mit leeren Teilbäumen), dann die 6 rechts von 8. "
       "`enthaelt(8)` liefert true – damit steht das Ergebnis von `||` in der Wurzel fest: Der rechte Teilbaum mit der 5 (und der zweiten 6) wird **nie** untersucht."),
     T("%d Aufrufe, größte Rekursionstiefe 3, Rückgabe **true**." % len(rows)),
     H("P7/P8: Tiefe des Erstaufrufs 0; Kurzschlussauswertung von `||` und `&&` beachten – nicht jeder Teilbaum wird besucht.")]))
assert jv("W5-L2-08.check") == "true"

level("W5-L2", "5.2", "Rekursion im Geäst – rekursive Baumalgorithmen", [32], "AB 1 Binärbäume, Teil 2 (DS 32)",
      "AQ_W5_L5_Wald_Geruest.txt – Level 5.2 (Klasse Rekursiv, Testklasse L52RekursivTest)",
      [T("**Bauplan rekursiver Baummethoden:** 1. Basisfall `if (b.isEmpty())` – ganz oben. 2. Wurzel auswerten (Cast!). "
         "3. Teilbäume rekursiv. 4. Ergebnisse verknüpfen."),
       H("Rekursionstabelle: Erstaufruf = Tiefe 0, Aufrufe in der Reihenfolge ihres Beginns, leere Teilbäume mitzählen. "
         "Ein Baum mit n Knoten erzeugt bei einem vollständigen Durchlauf 2n + 1 Aufrufe.")], L2)

# #######################################################################################
#  LEVEL 5.3 (Kuer)
# #######################################################################################
def raten_py(t, a):
    while not (t.l is None and t.r is None):
        if not a: return "?"
        t = t.l if a[0] == "j" else t.r; a = a[1:]
    return t.v
L3 = []
MON_OPT = ["Drache", "Greif", "Kraken", "Troll", "?"]
L3.append(task("W5-L3-01", "Der Akinator rät", 1, "Bäume", [],
    [T("Der Akinator geht von der Wurzel aus je Antwort einen Schritt: `'j'` → links, sonst rechts – bis zu einem Blatt. "
       "Überzählige Antworten werden ignoriert; reichen die Antworten nicht bis zu einem Blatt, liefert `raten` `\"?\"`."), BAUM(MQ),
     TAB(["antworten", "raten(antworten)"], [['`"%s"`' % a, "[[r%d]]" % i] for i, a in enumerate(RATEN301)])],
    gaps({"r%d" % i: AW(MON_OPT) for i in range(len(RATEN301))}),
    {"r%d" % i: [same(raten_py(parse(MQ), a), "W5-L3-01.%d" % i)] for i, a in enumerate(RATEN301)},
    [T("- `\"nj\"`: nein (kann nicht fliegen) → ja (lebt im Wasser) → **Kraken**\n- `\"jn\"`: → **Greif**\n"
       "- `\"j\"`: endet bei der Frage „Speit es Feuer?“ → **?**\n- `\"nnjn\"`: nach zwei Schritten ist das Blatt **Troll** erreicht, der Rest wird ignoriert.\n"
       "- `\"\"`: keine Antwort, die Wurzel ist eine Frage → **?**")]))

t302 = jv("W5-L3-02.baum")
L3.append(task("W5-L3-02", "Der Akinator lernt dazu", 2, "Bäume", [],
    [T("`lernen(antworten, neu, frage, jaFuerNeu)`: Das über `antworten` erreichte Blatt (Monster alt) wird zum Frageknoten `frage`. "
       "Seine Kinder sind `neu` und `alt` – `neu` links, wenn `jaFuerNeu` wahr ist, sonst rechts."),
     C('lernen("jj", "Phönix", "Ist es ein Vogel?", true);\nlernen("nn", "Zyklop", "Ist es behaart?", false);', nummern=False),
     T("Verändere den Startbaum so, wie er nach beiden Aufrufen aussieht.")],
    tree_bauen(MQ, ["Ist es ein Vogel?", "Phönix", "Ist es behaart?", "Zyklop", "Drache", "Troll"]),
    {"baum": norm(t302)},
    [BAUM(t302),
     T("1. `\"jj\"` führt zum Blatt Drache. Es wird zur Frage „Ist es ein Vogel?“; Phönix (ja) links, Drache rechts.\n"
       "2. `\"nn\"` führt zu Troll. `jaFuerNeu` ist **false**: Troll (alt) kommt nach links, Zyklop nach rechts – ein behaartes Monster wäre also der Troll."),
     T("Danach: %s Monster, %s Fragen; `raten(\"nnn\")` liefert %s." % (jv("W5-L3-02.monster"), jv("W5-L3-02.fragen"), jv("W5-L3-02.r_nnn")))],
    ["Bei jaFuerNeu = false steht das neue Monster auf der Nein-Seite (rechts)."]))

L3.append(task("W5-L3-03", "Monster zählen", 1, "Bäume", [],
    [T("Ein Akinator startet mit **einem** Monster (ein Blatt) und lernt danach 7-mal mit `lernen` dazu.\n\n"
       "- Anzahl der Monster (Blätter): [[m]]\n- Anzahl der Fragen (innere Knoten): [[f]]\n- Anzahl aller Knoten: [[k]]\n\n"
       "Ein anderer Akinator kennt 20 Monster. Wie viele Fragen enthält sein Baum? [[f20]]")],
    gaps({"m": Z(), "f": Z(), "k": Z(), "f20": Z()}),
    {"m": [jv("W5-L3-03.monster")], "f": [jv("W5-L3-03.fragen")], "k": [jv("W5-L3-03.knoten")], "f20": ["19"]},
    [T("Jeder `lernen`-Aufruf macht aus einem Blatt eine Frage und hängt zwei Blätter an: Fragen + 1, Monster − 1 + 2 = Monster + 1. "
       "Am Anfang gilt Monster = 1, Fragen = 0 – also immer **Monster = Fragen + 1**."),
     T("Nach 7 Aufrufen: 8 Monster, 7 Fragen, 15 Knoten (per Java nachgebaut). 20 Monster → **19 Fragen**.")]))

lv304 = nodes_level(parse(T304))
L3.append(task("W5-L3-04", "Ebene für Ebene", 1, "Bäume", [],
    [T("Klicke die Knoten in **Levelorder** an: Ebene für Ebene, jede Ebene von links nach rechts.")],
    tree_klick(T304), klick(paths(lv304)),
    [T("Levelorder: **%s**. Ebene 0: 5 · Ebene 1: 8, 3 · Ebene 2: 1, 7, 9 · Ebene 3: 2." % " ".join(vals(lv304))),
     H("Nicht mit der Preorder verwechseln (%s) – die geht erst ganz in die Tiefe." % jv("trav.T304.pre").strip())]))

rows = [z.split("|") for z in jv("W5-L3-05.tab").strip(";").split(";")]
blk, fel, loe = gap_tab(["Durchlauf", "entnommen", "Schlange (vorne → hinten)"], rows, {1: "zahl", 2: "liste"}, "z", fest=(0,))
L3.append(task("W5-L3-05", "Die Wanderschlange", 2, "Tracetabelle", ["P8"],
    [T("`levelorder` benutzt eine Schlange vom Inhaltstyp BinTree. Notiere nach jedem Durchlauf den entnommenen Knoten und den Inhalt der Schlange "
       "(vorne zuerst, jeden Teilbaum durch seinen Wurzelwert, mit Komma getrennt; leere Schlange: –)."), BAUM(T305), C(LEVEL_CODE), blk],
    gaps(fel), loe,
    [T("Ausgabe: `\"%s\"`. In der Schlange stehen Teilbäume – wer entnommen wird, stellt seine (nicht leeren) Kinder hinten an. "
       "Höchstens %d Teilbäume stehen gleichzeitig in der Schlange." % (jv("W5-L3-05.text"), max(len(r[2].split(", ")) for r in rows if r[2] != "–"))),
     H("P8: Jeder Durchlauf bekommt eine Zeile, auch der letzte mit leerer Schlange.")]))

L3.append(task("W5-L3-06", "Die Schlange verschluckt sich", 2, "Fehler im Java-Code", ["P1"],
    [T("Diese Fassung von `levelorder` stürzt schon beim zahlenbaum ab."), C(LEVEL_BUG),
     T("Teil 1: Markiere die Zeile, in der der Laufzeitfehler auftritt. Teil 2: Welche Korrekturen machen die Methode richtig – auch für den leeren Baum?")],
    [lines(1, 1), choice([("a", "Die Zeilen 7 bis 9 in `if (!k.isEmpty()) { … }` einschließen."),
                          ("b", "Nur die Zeilen 8 und 9 jeweils mit `if (!k.getLeft().isEmpty())` bzw. `if (!k.getRight().isEmpty())` absichern."),
                          ("c", "Die Schleifenbedingung zu `while (!q.isEmpty() && !((BinTree) q.head()).isEmpty())` ändern.")], mehrfach=True)],
    [{"zeilen": [int(jv("W5-L3-06.bug"))]}, {"richtig": ["a"]}],
    [T("Zeile %s: Ein Blatt reiht seine beiden **leeren** Teilbäume ein. Werden sie entnommen, ruft Zeile 7 `getItem()` auf einem leeren Baum auf → IllegalStateException (P1)." % jv("W5-L3-06.bug")),
     T("- a) richtig: liefert `\"%s\"`, für den leeren Baum `\"\"`.\n"
       "- b) reicht **nicht**: Für den leeren Gesamtbaum wird Zeile 4 trotzdem ausgeführt und Zeile 7 stürzt ab (Testlauf: %s).\n"
       "- c) falsch: Die Schleife bricht beim ersten leeren Teilbaum ab – Ausgabe nur `\"%s\"`." % (
           jv("W5-L3-06.fixa").split("#")[0], jv("W5-L3-06.fixb").split("#")[1], jv("W5-L3-06.fixc").split("#")[0])),
     H("Musterlösung (siehe Level-Code): nur **nicht leere** Bäume einreihen – auch die Wurzel.")]))
assert jv("W5-L3-06.fixa").split("#") == ["5 9 4 2 7 9 1 ", ""] and jv("W5-L3-06.fixb").endswith("#Laufzeitfehler")

# Stapel-Variante: Python-Simulation
def stapel_py(t):
    out, s = [], ([("", t)] if t else [])
    while s:
        p, n = s.pop(); out.append((p, n))
        if n.l: s.append((p + "L", n.l))
        if n.r: s.append((p + "R", n.r))
    return out
st307 = stapel_py(parse(T307))
same(wl(vals(st307)), "W5-L3-07.text")
L3.append(task("W5-L3-07", "Stapel statt Schlange", 3, "ADT-Befehlsfolgen", ["P8"],
    [T("In `raetsel` wurde die Schlange der Levelorder durch einen **Stapel** ersetzt. Klicke die Knoten in der Reihenfolge an, in der `raetsel(t)` sie an `text` anhängt."),
     C(STAPEL_CODE)],
    tree_klick(T307), klick(paths(st307)),
    [T("Ausgabe: `\"%s\"`. Der Stapel gibt den zuletzt eingelegten Teilbaum zuerst heraus: Nach der 8 liegen 3 (unten) und 10 (oben) im Stapel – "
       "also geht es mit dem **rechten** Teilbaum weiter, und zwar gleich in die Tiefe." % jv("W5-L3-07.text")),
     T("Das ist eine Tiefensuche: Preorder, aber rechts vor links. Würde man erst rechts und dann links einlegen, entstünde genau die Preorder `%s`." % wl(vals(nodes_pre(parse(T307)))).strip())]))

L3.append(task("W5-L3-08", "Der klügste Akinator", 3, "Effizienz", ["P10"],
    [T("Ein Akinator kennt **16** Monster. Jedes Monster muss erraten werden können.\n\n"
       "- Wie viele Fragen braucht er für das am schwersten zu erratende Monster **mindestens** (bestmöglicher Baum)? [[min]]\n"
       "- Wie viele Fragen sind es dort **höchstens** (ungünstigster Baum)? [[max]]\n"
       "- Mindestanzahl Fragen bis zum schwersten Monster bei **1000** Monstern: [[m1000]]"),
     T("Wähle die Begründung für den ersten Wert.")],
    [gaps({"min": Z(), "max": Z(), "m1000": Z()}),
     choice([("a", "Jede Frage kann die Kandidaten höchstens halbieren; im ausgeglichenen Baum liegen alle 16 = 2⁴ Monster auf Ebene 4, also reichen 4 Fragen."),
             ("b", "Weil es 16 Monster gibt, braucht man 16 Fragen."),
             ("c", "Der Baum hat 15 Fragen, also braucht jedes Monster 15 Fragen."),
             ("d", "Ein Akinator stellt immer genau so viele Fragen, wie der Baum hoch ist.")])],
    [{"min": ["4"], "max": ["15"], "m1000": ["10"]}, {"richtig": ["a"]}],
    [T("Ausgeglichen: Mit k Fragen erreicht man höchstens 2^k Blätter. 2⁴ = 16 → **4 Fragen**. "
       "Bei einer Kette schließt jede Frage nur ein Monster aus: 16 − 1 = **15 Fragen**. 1000 Monster: 2⁹ = 512 < 1000 ≤ 1024 = 2¹⁰ → **10 Fragen**."),
     H("P10 „begründen“: Der Verweis auf das Halbieren der Kandidaten (Verdopplung → eine Frage mehr) ist die Begründung – die bloße Zahl reicht nicht.")]))
# Pruefung der Min-/Max-Werte (volle Binaerbaeume mit n Blaettern)
import math
assert math.ceil(math.log2(16)) == 4 and math.ceil(math.log2(1000)) == 10

level("W5-L3", "5.3", "Kür: Der Akinator lernt – Entscheidungsbaum und Level-Order", [33], "AB 1 Binärbäume, Teil 3 (DS 33, Kür)",
      "AQ_W5_L5_Wald_Geruest.txt – Level 5.3 (Klasse Akinator, Testklasse L53AkinatorTest); Baumzeichner Aufgabe 3",
      [T("Im **Entscheidungsbaum** sind innere Knoten Ja/Nein-Fragen und Blätter Monster: ja → links, nein → rechts. "
         "Beim Lernen wird ein Blatt zur Frage – deshalb gilt immer Monster = Fragen + 1."),
       H("**Levelorder** (Ebene für Ebene) braucht eine **Schlange vom Inhaltstyp BinTree**: entnehmen, ausgeben, nicht leere Kinder hinten anstellen. "
         "Cast: `BinTree k = (BinTree) q.dequeue();`")], L3)

# #######################################################################################
#  LEVEL 5.4
# #######################################################################################
ttb = parse(TB); same(TB, "W5-L4.tb")
L4 = []
p401, f401 = bst_path(ttb, 70)
L4.append(task("W5-L4-01", "Der Weg zur Truhe 70", 1, "Sortieren und Suchen", [],
    [T("In diesem binären Suchbaum liegen die Truhennummern des Waldlagers. Klicke alle Knoten an, die `suche(b, 70)` **untersucht** (mit 70 vergleicht) – in der richtigen Reihenfolge.")],
    tree_klick(TB), klick(p401),
    [T("Suchweg: %s → leer. 70 > 41 → rechts; 70 > 65 → rechts; 70 < 91 → links; 70 < 72 → links: leerer Teilbaum, `suche` liefert **false**. "
       "Es werden %d Knoten untersucht – der Rest des Baums wird nie betreten." % (", ".join(node_at(ttb, p).v for p in p401), len(p401)))]))
assert not f401

t402 = copy(ttb)
for x in INS402: bst_insert(t402, x)
L4.append(task("W5-L4-02", "Neue Truhen einsortieren", 1, "Bäume", [],
    [T("Füge nacheinander **55** und **30** in den Suchbaum ein (Duplikate werden ignoriert, kleinere Werte links, größere rechts).")],
    tree_bauen(TB, INS402), {"baum": same(ks(t402), "W5-L4-02.baum")},
    [BAUM(ks(t402)),
     T("55: 41 → 65 → 50 → rechts von 50 ist leer → neues Blatt. 30: 41 → 20 → 29 → 32 → links von 32 ist leer → neues Blatt. "
       "Eingefügt wird immer an der Stelle, an der die Suche im Leeren endet.")]))

t403 = bst_from(SEQ403)
L4.append(task("W5-L4-03", "Ein Suchbaum wächst", 2, "Bäume", [],
    [T("Die Werte werden in dieser Reihenfolge in einen **leeren** binären Suchbaum eingefügt:\n\n`%s`\n\nBaue den entstehenden Baum." % ", ".join(map(str, SEQ403)))],
    tree_bauen("-", SEQ403), {"baum": same(ks(t403), "W5-L4-03.baum")},
    [BAUM(ks(t403)),
     T("Der erste Wert (15) wird Wurzel. Jeder weitere Wert sucht seinen Platz von der Wurzel aus. Höhe %d, Inorder zur Kontrolle: %s (aufsteigend sortiert)." % (
         hoehe(t403), " ".join(vals(nodes_in(t403)))))]))

L4.append(task("W5-L4-04", "Suchen mit Zählwerk", 1, "Sortieren und Suchen", [],
    [T("`vergleiche(b, x)` zählt die untersuchten (nicht leeren) Knoten bei der Suche nach x. Ergänze für den Suchbaum die Tabelle."), BAUM(TB),
     TAB(["x", "vergleiche(b, x)", "suche(b, x)"], [[str(x), "[[v%d]]" % x, "[[s%d]]" % x] for x in X404])],
    gaps(dict({"v%d" % x: Z() for x in X404}, **{"s%d" % x: AW(["true", "false"]) for x in X404})),
    dict({"v%d" % x: [same(len(bst_path(ttb, x)[0]), "W5-L4-04.v%d" % x)] for x in X404},
         **{"s%d" % x: [same(str(bst_path(ttb, x)[1]).lower(), "W5-L4-04.s%d" % x)] for x in X404}),
    [T("\n".join("- x = %d: %s%s → %d Knoten" % (x, ", ".join(node_at(ttb, p).v for p in bst_path(ttb, x)[0]), "" if bst_path(ttb, x)[1] else " → leer",
                                              len(bst_path(ttb, x)[0])) for x in X404)),
     T("Höchstens so viele Knoten wie der Baum hoch ist (%d) – egal ob x vorkommt oder nicht." % hoehe(ttb))]))

t405a = bst_delete(copy(ttb), 50); t405b = bst_delete(copy(ttb), 29)
L4.append(task("W5-L4-05", "Löschen: Blatt und ein Kind", 2, "Bäume", [],
    [T("Lösche jeweils aus dem **ursprünglichen** Baum. Teil 1: Lösche **50**. Teil 2: Lösche **29**."), BAUM(TB)],
    [tree_bauen(TB), tree_bauen(TB)],
    [{"baum": same(ks(t405a), "W5-L4-05.a")}, {"baum": same(ks(t405b), "W5-L4-05.b")}],
    [T("Teil 1: 50 ist ein **Blatt** (Fall 1) – es wird einfach entfernt."), BAUM(ks(t405a)),
     T("Teil 2: 29 hat **genau ein Kind** (32, Fall 2) – das Kind rückt mit seinem ganzen Teilbaum an die Stelle von 29."), BAUM(ks(t405b)),
     T("Probe: Die Inorder ist jeweils die alte Inorder ohne den gelöschten Wert.")]))

nf406 = int(node_at(ttb, "RR").v); m = node_at(ttb, "RR")
while m.l: m = m.l
nf406 = same(int(m.v), "W5-L4-06.nf")
t406 = bst_delete(copy(ttb), 65)
L4.append(task("W5-L4-06", "Löschen mit Nachfolger", 2, "Bäume", [],
    [T("Lösche **65** (zwei Kinder) mit dem **Nachfolger** – dem kleinsten Wert im rechten Teilbaum. Der Nachfolger von 65 ist [[nf]]. Baue den Baum danach."), BAUM(TB)],
    [gaps({"nf": Z()}), tree_bauen(TB)],
    [{"nf": [str(nf406)]}, {"baum": same(ks(t406), "W5-L4-06")}],
    [T("Nachfolger: einmal rechts (91), dann immer links → **%d**. 72 ersetzt 65 und wird an seiner alten Stelle entfernt (dort ist es ein Blatt, Fall 1)." % nf406),
     BAUM(ks(t406)), T("Inorder-Probe: %s – die alte Inorder ohne 65." % " ".join(vals(nodes_in(t406))))],
    ["Der Nachfolger hat nie ein linkes Kind – deshalb ist sein Entfernen immer Fall 1 oder 2."]))

m = ttb.l
while m.r: m = m.r
vg407 = same(int(m.v), "W5-L4-07.vg")
t407 = bst_delete(copy(ttb), 41, "vorgaenger")
L4.append(task("W5-L4-07", "Die Wurzel fällt", 3, "Bäume", [],
    [T("Lösche die Wurzel **41** – diesmal mit dem **Vorgänger** (größter Wert im linken Teilbaum). Der Vorgänger ist [[vg]]."), BAUM(TB)],
    [gaps({"vg": Z()}), tree_bauen(TB)],
    [{"vg": [str(vg407)]}, {"baum": same(ks(t407), "W5-L4-07")}],
    [T("Vorgänger: einmal links (20), dann immer rechts → 29 → **32**. 32 wird neue Wurzel; an seiner alten Stelle war 32 ein Blatt (Fall 1)."),
     BAUM(ks(t407)),
     T("Inorder-Probe: %s. Mit dem Nachfolger (50) entstünde ein anderer, ebenfalls richtiger Suchbaum – im Abitur immer angeben, welche Variante du wählst." %
       " ".join(vals(nodes_in(t407))))]))

assert jv("W5-L4-08.tb") == "99" and jv("W5-L4-08.t") == "-1" and jv("W5-L4-08.fix") == "40,99,-1"
L4.append(task("W5-L4-08", "Das falsche Maximum", 2, "Fehler im Java-Code", ["P7"],
    [T("`maximum` soll den größten Wert eines Suchbaums liefern (leerer Baum: −1). Für das Waldlager stimmt das Ergebnis, aber für den Baum t nicht."),
     BAUM(T408), C(MAXBUG),
     T("`maximum(t)` liefert [[r]]. Markiere die fehlerhafte Zeile und korrigiere sie: `if ([[k]]) {`")],
    [gaps({"r": Z(), "k": TX("code", 26)}), lines(2, 1)],
    [{"r": ["-1"], "k": ["b.getRight().isEmpty()"]}, {"zeilen": [5]}],
    [T("Das Maximum steht ganz rechts – aber es muss **kein Blatt** sein. Bei t hat 40 nur ein linkes Kind: 40 ist kein Blatt, die Methode geht nach rechts in den leeren Baum und liefert −1."),
     T("Richtig ist der Basisfall „rechter Teilbaum leer“: `if (b.getRight().isEmpty())`. Dann liefert die Methode 40 für t, 99 für das Waldlager und −1 für den leeren Baum."),
     H("P7 – falscher Basisfall: Tests nur mit Bäumen, in denen das Maximum zufällig ein Blatt ist, finden den Fehler nicht.")]))

level("W5-L4", "5.4", "Die Item-Datenbank – binäre Suchbäume", [34], "AB 2 Suchbäume, Teil 1 (DS 34)",
      "AQ_W5_L5_Wald_Geruest.txt – Level 5.4 Basis/Erweiterung (Klasse Suchbaum, Testklasse L54SuchbaumTest); Baumzeichner Aufgaben 4–8",
      [T("**Binärer Suchbaum:** Für **jeden** Knoten sind alle Werte im linken Teilbaum kleiner, alle im rechten größer. Suchen und Einfügen gehen nur **einen** Weg nach unten."),
       H("**Löschen:** Blatt → entfernen · ein Kind → Kind rückt nach · zwei Kinder → Wert durch den Nachfolger (kleinster im rechten Teilbaum) "
         "oder Vorgänger (größter im linken) ersetzen. Probe: Inorder ohne den gelöschten Wert.")], L4)

# #######################################################################################
#  LEVEL 5.5
# #######################################################################################
L5 = []
h501 = {k: same(hoehe(bst_from(v)), "W5-L5-01.%s" % k) for k, v in ORD501.items()}
L5.append(task("W5-L5-01", "Wäscheleine erkennen", 1, "Bäume", [],
    [T("Die Werte 1 bis 7 werden in einen leeren Suchbaum eingefügt. Bei welchen Reihenfolgen entsteht ein **entarteter** Baum (Höhe 7)?")],
    choice([(k, "`" + ", ".join(map(str, v)) + "`") for k, v in ORD501.items()], mehrfach=True),
    {"richtig": [k for k in ORD501 if h501[k] == 7]},
    [T("\n".join("- `%s` → Höhe %d" % (", ".join(map(str, v)), h501[k]) for k, v in ORD501.items())),
     T("Entartet heißt: jeder innere Knoten hat nur ein Kind. Das passiert nicht nur bei sortierten Folgen – auch beim Zickzack 7, 1, 6, 2, … ist jeder neue Wert "
       "größer bzw. kleiner als alle restlichen, sodass immer nur ein Kind entsteht.")]))

def minh(n): return math.ceil(math.log2(n + 1))
for n in N502:
    if n <= 5000: same(minh(n), "W5-L5-02.min%d" % n)
L5.append(task("W5-L5-02", "Krumm oder buschig?", 2, "Effizienz", ["P10"],
    [T("Ergänze die Höhe des Suchbaums, wenn die n Werte **sortiert** eingefügt werden, und die **kleinstmögliche** Höhe (ausgeglichener Baum)."),
     TAB(["n"] + [str(n) for n in N502], [["Höhe sortiert eingefügt"] + ["[[s%d]]" % i for i in range(len(N502))],
                                          ["kleinstmögliche Höhe"] + ["[[m%d]]" % i for i in range(len(N502))]])],
    gaps(dict({"s%d" % i: Z(8) for i in range(len(N502))}, **{"m%d" % i: Z(4) for i in range(len(N502))})),
    dict({"s%d" % i: [str(n)] for i, n in enumerate(N502)}, **{"m%d" % i: [str(minh(n))] for i, n in enumerate(N502)}),
    [T("Sortiert eingefügt entsteht eine Kette: Höhe = n. Kleinstmögliche Höhe = kleinstes k mit 2^k − 1 ≥ n: " +
       ", ".join("n = %d → %d" % (n, minh(n)) for n in N502) + " (bis n = 4096 mit `ausgeglichenAus` in Java nachgebaut)."),
     T("Bei 500 000 Werten untersucht die Suche im ausgeglichenen Baum höchstens 19 Knoten, in der Kette bis zu 500 000."),
     H("4096 = 2¹² braucht schon 13 Ebenen: 12 volle Ebenen fassen nur 2¹² − 1 = 4095 Werte.")]))

L5.append(task("W5-L5-03", "Doppelt so viele Items", 1, "Effizienz", ["P10"],
    [T("Die Item-Datenbank ist ein **vollständiger** Suchbaum mit 1023 Items (10 volle Ebenen). Sie wächst auf 2047 Items und bleibt vollständig. "
       "Wie viele Knoten untersucht eine Suche jetzt **höchstens**?")],
    choice([("a", "11"), ("b", "20"), ("c", "1024"), ("d", "2047")]),
    {"richtig": ["a"]},
    [T("Eine Ebene mehr bietet Platz für 2¹⁰ = 1024 neue Knoten: 2¹¹ − 1 = 2047. Die Suche geht pro Ebene einen Knoten tiefer – **ein Vergleich mehr**, also höchstens 11."),
     H("Merke: Verdopplung der Anzahl → im ausgeglichenen Baum **ein** Vergleich mehr, im entarteten Baum doppelt so viele.")]))

t504 = ausgeglichen(R504)
L5.append(task("W5-L5-04", "Mitte nach oben", 2, "Bäume", [],
    [T("`ausgeglichenAus(r, 0, r.length − 1)` baut aus der sortierten Reihung einen möglichst niedrigen Suchbaum: Das Element in der Mitte `mitte = (lo + hi) / 2` "
       "wird Wurzel, aus den Hälften entstehen rekursiv die Teilbäume. Baue den Baum für"), REIH(R504), C(AUSG_CODE)],
    tree_bauen("-", R504), {"baum": same(ks(t504), "W5-L5-04.baum")},
    [BAUM(ks(t504)),
     T("lo = 0, hi = 9 → mitte = 4 → Wurzel **21** (ganzzahlige Division rundet ab: bei gerader Länge wird das linke der beiden mittleren Elemente Wurzel). "
       "Links entsteht aus 3, 8, 12, 17 der Teilbaum mit Wurzel 8, rechts aus 26 … 45 der mit Wurzel 34. Höhe %d = kleinstmöglich für 10 Werte." % hoehe(t504))]))

log505 = []; ausgeglichen(R505, log=log505)
rows = [z.split("|") for z in jv("W5-L5-05.tab").strip(";").split(";")]
assert [(int(a), int(b), int(c), (None if d == "–" else int(d))) for a, b, c, d, e in rows] == log505
blk, fel, loe = gap_tab(["Rekursionstiefe", "lo", "hi", "mitte", "liefert (Wurzelwert oder leer)"], rows,
                        {0: "zahl", 1: "zahl", 2: "zahl", 3: "zahl", 4: "knoten"}, "z", fest=(0,))
L5.append(task("W5-L5-05", "Rekursionstabelle: Mitte nach oben", 3, "Rekursionstabelle", ["P7", "P8"],
    [T("Dokumentiere den Aufruf `ausgeglichenAus(r, 0, 4)` mit"), REIH(R505), C(AUSG_CODE),
     T("Trage die Aufrufe in der Reihenfolge ihres Beginns ein. Bei leerem Bereich (lo > hi) bleibt mitte „–“ und der Aufruf liefert „leer“."), blk],
    gaps(fel), loe,
    [T("Es entsteht der Baum `%s`. %d Aufrufe = 2 · 5 + 1: Jeder der 5 Werte wird in genau einem Aufruf Wurzel, jeder dieser Aufrufe ruft zweimal auf." % (
        jv("W5-L5-05.baum"), len(rows))),
     T("Achtung bei lo = 0, hi = 1: mitte = 0, also bleibt links der leere Bereich (0, −1) und rechts (1, 1)."),
     H("P7: Erst wird der ganze linke Bereich abgearbeitet, dann der rechte – die Reihenfolge der Zeilen ist die Reihenfolge des Beginns.")]))

isb = {k: same("%s,%s" % (str(is_bst(parse(v))).lower(), str(nur_kinder(parse(v))).lower()), "W5-L5-06.%s" % k) for k, v in BST506.items()}
L5.append(task("W5-L5-06", "Echt oder gefälscht?", 2, "Bäume", [],
    [T("Welche der Bäume sind binäre Suchbäume?")] + sum([[T("**Baum %s**" % k), BAUM(v)] for k, v in BST506.items()], []),
    choice([(k, "Baum %s" % k) for k in BST506], mehrfach=True),
    {"richtig": [k for k in BST506 if isb[k].startswith("true")]},
    [T("- A: ja.\n- B: **nein** – 35 steht im linken Teilbaum der Wurzel 30, ist aber größer als 30 (zu ihrem Elternknoten 15 passt sie!).\n"
       "- C: **nein** – 28 steht im rechten Teilbaum der 30, ist aber kleiner.\n- D: ja – fehlende Kinder sind erlaubt."),
     H("Alle vier Bäume bestehen den Test „jeder Knoten passt zu seinen Kindern“. Entscheidend sind die Grenzen **aller Vorfahren** – oder: Die Inorder muss streng aufsteigend sein.")]))

L5.append(task("W5-L5-07", "Die isBST-Falle", 2, "Funktionsweise erläutern", ["P10"],
    [T("`nurKinder(b)` vergleicht jeden Knoten nur mit seinen Kindern, `istBST(b, -1, -1)` gibt jedem Teilbaum die Grenzen aller Vorfahren mit. Baum F:"),
     BAUM(F507),
     TAB(["Aufruf", "Rückgabe"], [["`nurKinder(F)`", "[[a]]"], ["`istBST(F, -1, -1)`", "[[b]]"], ["`suche(F, 45)`", "[[c]]"], ["`suche(F, 10)`", "[[d]]"]])],
    gaps({x: AW(["true", "false"]) for x in "abcd"}),
    {"a": [same("true", "W5-L5-07.nur")], "b": [same("false", "W5-L5-07.ist")], "c": [same("false", "W5-L5-07.suche45")], "d": [same("true", "W5-L5-07.suche10")]},
    [T("45 ist rechtes Kind von 30 – das passt. Aber 45 steht im **linken** Teilbaum der Wurzel 40 und ist größer als 40: F ist kein Suchbaum. "
       "Inorder: %s (45 vor 40)." % jv("W5-L5-07.in").strip()),
     T("Folge: `suche(F, 45)` geht 40 → rechts → 60 → links → 50 → links → leer und liefert **false**, obwohl 45 im Baum steht.")]))

v508 = OC508.gueltig(J)
assert v508 and all(not o.gueltig(J) for o in OC508d)
L5.append(task("W5-L5-08", "Puzzle: istBST mit Grenzen", 3, "Methode implementieren", ["P1", "P7"],
    [T("Setze `istBST(b: BinTree vom Inhaltstyp Ganzzahl, min: Ganzzahl, max: Ganzzahl): Wahrheitswert` zusammen. Alle Werte sind ≥ 0, "
       "−1 steht für „keine Grenze“; der Erstaufruf lautet `istBST(b, -1, -1)`. Drei Teile sind Fallen.")],
    order([(k, T508[k]) for k in ["t1", "t2", "t3", "t4", "t5", "t6", "d1", "d2", "d3"]]),
    {"reihenfolgen": v508},
    [C("\n".join(T508[k] for k in ["t1", "t2", "t3", "t4", "t5", "t6"])),
     T("Nach links wird der eigene Wert zur neuen **Obergrenze**, nach rechts zur neuen **Untergrenze** – so gelten die Grenzen aller Vorfahren. "
       "Getestet mit beispielBST, zahlenbaum, F, den Fallen `8(3(1,9),10)` und `8(3,10(5,14))`, Duplikat `5(5,-)` und dem leeren Baum."),
     T("Fallen: `if (wert >= max)` ohne `max != -1` lehnt jeden Baum ab (−1 als Obergrenze); Grenzen unverändert weitergeben oder vertauscht prüft nichts bzw. das Falsche.")]))

level("W5-L5", "5.5", "Krumm oder buschig? – ausgeglichen, entartet, isBST", [35], "AB 2 Suchbäume, Teil 2 (DS 35)",
      "AQ_W5_L5_Wald_Geruest.txt – Level 5.4 Experte (Klasse Suchbaum: istBST, ausgeglichenAus, nachfolger)",
      [T("Die Suche untersucht höchstens so viele Knoten, wie der Baum **hoch** ist. Entartet (Kette): Höhe n. Ausgeglichen: Höhe ≈ log₂(n)."),
       H("**Verdopplung → ein Vergleich mehr** (ausgeglichen). isBST-Falle: Nicht nur die Kinder prüfen – die Grenzen aller Vorfahren gelten!")], L5)

# #######################################################################################
#  LEVEL 5.6 (Transfer)
# #######################################################################################
def heap_ok(t):
    # Max-Heap: Ordnung + vollstaendig (links aufgefuellt)
    def ordnung(n):
        if n is None: return True
        for c in (n.l, n.r):
            if c is not None and int(c.v) > int(n.v): return False
        return ordnung(n.l) and ordnung(n.r)
    lv = nodes_level(t); pos = []
    for p, n in lv:
        idx = 1
        for c in p: idx = 2 * idx + (1 if c == "R" else 0)
        pos.append(idx)
    vollst = sorted(pos) == list(range(1, len(pos) + 1))
    return ordnung(t) and vollst, ordnung(t)
def heap_arr(t):
    lv = nodes_level(t); arr = {}
    for p, n in lv:
        idx = 1
        for c in p: idx = 2 * idx + (1 if c == "R" else 0)
        arr[idx] = int(n.v)
    return [arr[i] for i in range(1, len(arr) + 1)]
def arr_tree(a, i=1):
    if i > len(a): return None
    return N(str(a[i - 1]), arr_tree(a, 2 * i), arr_tree(a, 2 * i + 1))
def heap_insert(a, x):
    a = a + [x]; i = len(a)
    while i > 1 and a[i // 2 - 1] < a[i - 1]:
        a[i // 2 - 1], a[i - 1] = a[i - 1], a[i // 2 - 1]; i //= 2
    return a

L6 = []
L6.append(task("W5-L6-01", "Welche Baumart, welche Regel?", 1, "Bäume", [],
    [T("Ordne jeder Baumart ihre **Invariante** (die Regel, die immer gilt) zu.")],
    match([("e1", "Termbaum"), ("e2", "Akinator-Entscheidungsbaum"), ("e3", "binärer Suchbaum"), ("e4", "Max-Heap"), ("e5", "Huffman-Baum")],
          [("k1", "Blätter sind Zahlen, innere Knoten Rechenzeichen mit genau zwei Teilbäumen"),
           ("k2", "Blätter sind Antworten, innere Knoten Ja/Nein-Fragen; Anzahl Blätter = Anzahl Fragen + 1"),
           ("k3", "für jeden Knoten: links alle kleiner, rechts alle größer"),
           ("k4", "jeder Knoten ist mindestens so groß wie seine Kinder; alle Ebenen voll, die letzte von links aufgefüllt"),
           ("k5", "Zeichen stehen nur in Blättern; der Weg (0 = links, 1 = rechts) ergibt den Code")]),
    {"e1": "k1", "e2": "k2", "e3": "k3", "e4": "k4", "e5": "k5"},
    [T("Bei einer unbekannten Baumart ist die Invariante der Schlüssel: Aus ihr folgen Such- und Prüfverfahren und fast alle Begründungen."),
     H("Fünf-Schritte-Strategie: Definition lesen – Beispiel von Hand – Invariante formulieren – auf BinTree abbilden – implementieren.")]))

hok = {k: heap_ok(parse(v)) for k, v in HEAP602.items()}
L6.append(task("W5-L6-02", "Max-Heap erkennen", 1, "Bäume", [],
    [H("**Material – Max-Heap:** Ein Binärbaum ist ein Max-Heap, wenn (1) jeder Knoten **mindestens so groß** ist wie seine Kinder und "
       "(2) alle Ebenen vollständig gefüllt sind, nur die letzte darf rechts Lücken haben (sie wird **von links** aufgefüllt)."),
     T("Welche Bäume sind Max-Heaps?")] + sum([[T("**Baum %s**" % k), BAUM(v)] for k, v in HEAP602.items()], []),
    choice([(k, "Baum %s" % k) for k in HEAP602], mehrfach=True),
    {"richtig": [k for k in HEAP602 if hok[k][0]]},
    [T("- A: ja.\n- B: **nein** – die Ordnung stimmt, aber die letzte Ebene ist nicht von links aufgefüllt (links von 80 fehlt ein Knoten, rechts steht 70).\n"
       "- C: **nein** – 65 ist größer als sein Elternknoten 60.\n- D: ja – gleiche Werte sind erlaubt („mindestens so groß“)."),
     H("Unterschied zum Suchbaum: Im Heap gibt es **keine** Ordnung zwischen linkem und rechtem Kind – das Maximum steht immer in der Wurzel.")]))

a603 = heap_arr(parse(HEAP603)); a1 = heap_insert(a603, HEAP_INS[0]); a2 = heap_insert(a1, HEAP_INS[1])
t603 = arr_tree(a2); assert heap_ok(t603)[0]
L6.append(task("W5-L6-03", "Ein Heap wächst", 2, "Bäume", [],
    [H("**Material – Einfügen in einen Max-Heap:** Der neue Wert kommt an die nächste freie Stelle der untersten Ebene (von links). "
       "Solange er größer ist als sein Elternknoten, tauscht er mit ihm den Platz (er „steigt auf“)."),
     T("Füge nacheinander **%d** und **%d** ein und baue den Heap danach." % tuple(HEAP_INS)), BAUM(HEAP603)],
    tree_bauen(HEAP603, HEAP_INS), {"baum": ks(t603)},
    [T("85 kommt rechts unter 80, ist größer und tauscht mit 80; 85 < 90 → fertig: `%s`." % ks(arr_tree(a1))),
     T("95 kommt links unter 40 (neue Ebene) und steigt auf: tauscht mit 40, dann mit 70, dann mit 90 – 95 ist die neue Wurzel."),
     BAUM(ks(t603)),
     T("Als Reihung (Ebene für Ebene): %s. Der aufsteigende Wert geht nur einen Weg nach oben – höchstens so viele Tausche, wie der Heap hoch ist." % a2)],
    ["Erst die Form (nächste freie Stelle), dann die Ordnung (aufsteigen) herstellen."]))

htree = parse(HUFF)
codes = {n.v: p.replace("L", "0").replace("R", "1") for p, n in nodes_pre(htree) if n.l is None and n.r is None}
bits_dec = "".join(codes[c] for c in HUFF_WORT_DEC); bits_enc = "".join(codes[c] for c in HUFF_WORT_ENC)
def decode(bits):
    out, n = "", htree
    for b in bits:
        n = n.l if b == "0" else n.r
        if n.l is None and n.r is None: out += n.v; n = htree
    return out
assert decode(bits_dec) == HUFF_WORT_DEC and decode(bits_enc) == HUFF_WORT_ENC
L6.append(task("W5-L6-04", "Die Huffman-Botschaft", 2, "Bäume", [],
    [H("**Material – Huffman-Baum:** Die Zeichen stehen nur in den Blättern (innere Knoten: •). Der Code eines Zeichens ist der Weg von der Wurzel: "
       "0 = links, 1 = rechts. Zum Dekodieren läuft man von der Wurzel los; erreicht man ein Blatt, ist ein Zeichen fertig und es geht wieder an der Wurzel weiter."),
     BAUM(HUFF), T("Dekodiere die Bitfolge `%s`: [[w]]" % bits_dec)],
    gaps({"w": TX("text", 10)}), {"w": [HUFF_WORT_DEC]},
    [T("Codes: " + ", ".join("%s = %s" % (k, v) for k, v in sorted(codes.items(), key=lambda x: (len(x[1]), x[1]))) + "."),
     T("%s → %s → **%s**." % (bits_dec, " | ".join(codes[c] for c in HUFF_WORT_DEC), HUFF_WORT_DEC))]))

L6.append(task("W5-L6-05", "Kodieren und begründen", 2, "Funktionsweise erläutern", ["P10"],
    [T("Kodiere mit dem Huffman-Baum das Wort **%s** (Bits ohne Leerzeichen): [[b]]" % HUFF_WORT_ENC), BAUM(HUFF),
     T("Warum kann man die Bitfolge ohne Trennzeichen eindeutig dekodieren? Wähle die Begründung.")],
    [gaps({"b": TX("code", 18)}),
     choice([("a", "Weil alle Zeichen in Blättern stehen, ist kein Code Anfang eines anderen Codes (präfixfrei): Sobald ein Blatt erreicht ist, ist das Zeichen eindeutig zu Ende."),
             ("b", "Weil alle Codes gleich lang sind."),
             ("c", "Weil häufige Zeichen kurze Codes haben."),
             ("d", "Weil der Huffman-Baum ein Suchbaum ist.")])],
    [{"b": [bits_enc]}, {"richtig": ["a"]}],
    [T("%s → %s = `%s`." % (HUFF_WORT_ENC, " | ".join(codes[c] for c in HUFF_WORT_ENC), bits_enc)),
     T("Die Codes sind verschieden lang (E = 00, B = 110) – eindeutig wird es durch die **Präfixfreiheit**: Ein Code endet an einem Blatt, unter einem Blatt geht kein Weg weiter. "
       "Dass häufige Zeichen kurze Codes bekommen, macht den Code kurz, aber nicht eindeutig."),
     H("P10 „begründen“: auf die Invariante (Zeichen nur in Blättern) zurückführen, nicht nur behaupten.")]))

def rune_words(t, praefix=""):
    if t is None: return []
    v = t.v.rstrip("*"); w = praefix + v
    out = [w] if t.v.endswith("*") else []
    return out + rune_words(t.l, w) + rune_words(t.r, praefix)
W606 = rune_words(parse(RUNE))
OPT606 = ["TAL", "TAU", "TOR", "TORF", "TA", "TO", "TALU", "TOF"]
L6.append(task("W5-L6-06", "Der Runenbaum des Försters", 2, "Bäume", [],
    [H("**Material – Präfixbaum als Binärbaum:** Jeder Knoten enthält einen Buchstaben, `*` markiert ein Wortende. "
       "**Links** (K) beginnt das erste Kind (der nächste Buchstabe des Worts), **rechts** (G) das nächste Geschwister (ein anderer Buchstabe an derselben Stelle). "
       "Der Binärbaum beginnt mit dem ersten Buchstaben."),
     BAUM(RUNE), T("Welche Wörter sind gespeichert?")],
    choice([(w.lower(), w) for w in OPT606], mehrfach=True),
    {"richtig": [w.lower() for w in OPT606 if w in W606]},
    [T("Gespeichert: **%s**. T → A → L* ergibt TAL; U* ist Geschwister von L, also TAU. O ist Geschwister von A: T → O → R* = TOR, darunter F* = TORF." % ", ".join(W606)),
     T("TA und TO sind nur Wortanfänge (A und O nicht markiert). TALU gibt es nicht: U ist **Geschwister** von L, nicht Kind – ein Schritt nach rechts verlängert das Wort nicht."),
     H("Typischer Fehler: `getRight()` als „rechtes Kind“ lesen. In dieser Darstellung bedeutet rechts „nächstes Geschwister“.")]))

L6.append(task("W5-L6-07", "Reicht der Blick auf die Kinder?", 3, "Funktionsweise erläutern", ["P10"],
    [T("`pruefe` vergleicht jeden Knoten nur mit seinen Kindern."), C(PRUEFE),
     T("Gib die Rückgaben für die Bäume A, B und C aus der Aufgabe „Max-Heap erkennen“ an: A [[a]], B [[b]], C [[c]]"),
     BAUM(HEAP602["A"]), BAUM(HEAP602["B"]), BAUM(HEAP602["C"]),
     T("Welche Aussagen sind richtig?")],
    [gaps({x: AW(["true", "false"]) for x in "abc"}),
     choice([("a", "Für die **Ordnung** eines Max-Heaps reicht der Vergleich mit den Kindern: Ist jeder Knoten ≥ seinen Kindern, ist er wegen der Transitivität ≥ allen Nachfahren."),
             ("b", "`pruefe` erkennt keinen Verstoß gegen die **Form** (letzte Ebene von links aufgefüllt) – deshalb liefert es für B true."),
             ("c", "Beim binären Suchbaum reicht der Vergleich mit den Kindern genauso."),
             ("d", "`pruefe` stürzt bei Blättern ab, weil `getLeft()` leer ist.")], mehrfach=True)],
    [{"a": [same("true", "W5-L6-07.A")], "b": [same("true", "W5-L6-07.B")], "c": [same("false", "W5-L6-07.C")]}, {"richtig": ["a", "b"]}],
    [T("A: true, B: true (Form wird nicht geprüft), C: false (65 > 60)."),
     T("Heap-Ordnung ist **transitiv**: Knoten ≥ Kind ≥ Enkel … Beim Suchbaum genügt das nicht – dort muss ein Enkel auch zur Grenze des Großelternknotens passen (isBST-Falle). "
       "Abstürze gibt es nicht: Vor `getItem()` der Kinder wird `isEmpty()` geprüft."),
     H("P10: Bei „beurteilen/begründen“ die Eigenschaft der Struktur (hier Transitivität) nennen und mit dem Gegenbeispiel Suchbaum abgrenzen.")]))

level("W5-L6", "5.6", "Fremde Bäume – Transfer auf unbekannte Baumarten", [35, 36], "AB 3 Transfer: Unbekannte Bäume erschließen (Vorbereitung Boss 5)",
      "AQ_W5_AB3_Runenbuch_Testumgebung.txt – Papier-Compiler (Klasse Runenbaum, RunenbuchTest)",
      [T("Im Abitur steht oft eine **unbekannte Baumart** im Material (B-Baum 2024, Huffman 2025, Heap 2026). Niemand erwartet, dass du sie kennst – du erschließt sie."),
       H("**Fünf Schritte:** Definition lesen · Beispiel von Hand · Invariante formulieren · auf BinTree abbilden (was heißt links/rechts?) · implementieren (Basisfall leer zuerst).")], L6)

# #######################################################################################
#  BOSS-POOL Welt 5
# #######################################################################################
B = []
tb01 = parse(B01); in01 = nodes_in(tb01)
B.append(task("W5-B-01", "Inorder im Dickicht", 1, "Bäume", [],
    [T("Klicke die Knoten in **Inorder**-Reihenfolge an.")], tree_klick(B01), klick(paths(in01)),
    [T("Inorder (links – Wurzel – rechts): **%s**." % " ".join(vals(in01)))]))
lv02 = nodes_level(parse(B02))
B.append(task("W5-B-02", "Levelorder im Nebel", 1, "Bäume", [],
    [T("Klicke die Knoten in **Levelorder** an (Ebene für Ebene, jeweils von links nach rechts).")], tree_klick(B02), klick(paths(lv02)),
    [T("Levelorder: **%s**." % " ".join(vals(lv02)))]))
tb03 = parse(B03); same(B03, "W5-B-03.tb")
p03, f03 = bst_path(tb03, B03_X)
B.append(task("W5-B-03", "Suchweg zur 40", 1, "Sortieren und Suchen", [],
    [T("Klicke in der Reihenfolge der Suche alle Knoten an, die `suche(b, %d)` im Suchbaum untersucht." % B03_X)], tree_klick(B03), klick(p03),
    [T("Suchweg: %s – %d untersuchte Knoten (Java: `vergleiche` = %s)." % (", ".join(node_at(tb03, p).v for p in p03), len(p03), jv("W5-B-03.v")))]))
assert f03 and str(len(p03)) == jv("W5-B-03.v")
tb04 = parse(B04)
B.append(task("W5-B-04", "Vermessung eines Baums", 1, "Bäume", [],
    [BAUM(B04), T("Anzahl der Knoten: [[k]] · Anzahl der Blätter: [[b]] · Höhe: [[h]] · Ebene des Knotens 10: [[e]]")],
    gaps({"k": Z(), "b": Z(), "h": Z(), "e": Z()}),
    {"k": [same(anzahl(tb04), "W5-B-04.knoten")], "b": [same(len(blaetter(tb04)), "W5-B-04.blaetter")], "h": [same(hoehe(tb04), "W5-B-04.hoehe")],
     "e": [jv("W5-B-04.ebene10")]},
    [T("Blätter: %s. Höhe %d (leerer Baum 0, Blatt 1). Die 10 liegt auf Ebene %s (Wurzel = Ebene 0)." % (", ".join(blaetter(tb04)), hoehe(tb04), jv("W5-B-04.ebene10")))]))
B.append(task("W5-B-05", "Doppelt so groß", 1, "Effizienz", ["P10"],
    [T("Ein ausgeglichener (vollständiger) Suchbaum enthält 4095 Werte. Wie viele Knoten untersucht eine Suche höchstens?")],
    choice([("a", "12"), ("b", "13"), ("c", "2048"), ("d", "4095")]), {"richtig": ["a"]},
    [T("4095 = 2¹² − 1: 12 volle Ebenen → höchstens **12** untersuchte Knoten. Bei 8191 Werten wäre es einer mehr.")]))
t06 = bst_from(B06_SEQ)
B.append(task("W5-B-06", "Das Inventar wird sortiert", 2, "Bäume", [],
    [T("Füge in einen leeren Suchbaum nacheinander ein: `%s`." % ", ".join(map(str, B06_SEQ)))], tree_bauen("-", B06_SEQ),
    {"baum": same(ks(t06), "W5-B-06.baum")}, [BAUM(ks(t06)), T("Inorder zur Kontrolle: %s." % " ".join(vals(nodes_in(t06))))]))
t07 = bst_delete(copy(tb03), B07_X)
B.append(task("W5-B-07", "Löschen mit zwei Kindern", 2, "Bäume", [],
    [T("Lösche **%d** mit dem **Nachfolger** (kleinster Wert im rechten Teilbaum)." % B07_X), BAUM(B03)], tree_bauen(B03),
    {"baum": same(ks(t07), "W5-B-07.baum")},
    [T("23 hat zwei Kinder. Nachfolger: einmal rechts (35), dann immer links → **%s**. 29 ersetzt 23, das Blatt 29 wird entfernt." % jv("W5-B-07.nf")), BAUM(ks(t07))]))
rows = [z.split("|") for z in jv("W5-B-08.tab").strip(";").split(";")]
blk, fel, loe = gap_tab(["Rekursionstiefe", "Knoten (Wert oder leer)", "Rückgabe"], rows, {0: "zahl", 1: "knoten", 2: "zahl"}, "z")
BLATT_ANZ = BLATT_OK
B.append(task("W5-B-08", "Rekursionstabelle: Blätter zählen", 2, "Rekursionstabelle", ["P7", "P8"],
    [T("Dokumentiere `anzahlBlaetter(t)` (Aufrufe in der Reihenfolge ihres Beginns, Erstaufruf Tiefe 0)."), BAUM(B08), C(BLATT_ANZ), blk],
    gaps(fel), loe,
    [T("Bei Blättern endet die Rekursion ohne weitere Aufrufe (Zeile 5). Nur der leere linke Teilbaum von 2 wird aufgerufen. %d Aufrufe, Ergebnis %s." % (len(rows), rows[0][2]))]))
B.append(task("W5-B-09", "Das verschwundene Item", 2, "Fehler im Java-Code", [],
    [T("Nach `einfuegen(b, 44)` ist der Suchbaum unverändert, und ein leerer Baum bleibt nach `einfuegen(leer, 7)` leer."), C(EINF_BUG),
     T("Markiere die fehlerhafte Zeile und gib die richtige Anweisung an: [[k]]")],
    [lines(1, 1), gaps({"k": TX("code", 18)})],
    [{"zeilen": [3]}, {"k": ["b.setItem(x);"]}],
    [T("`b = new BinTree(x);` ändert nur die **lokale Parametervariable** b – das neue Blatt kennt niemand, der leere Teilbaum im Baum bleibt leer "
       "(Java-Test: Baum nach dem Aufruf `%s`, leerer Baum bleibt leer: %s)." % (jv("W5-B-09.nach"), jv("W5-B-09.leer"))),
     T("`b.setItem(x);` verändert das Objekt selbst: Der leere Teilbaum wird zum Blatt → `%s`." % jv("W5-B-09.fix"))]))
assert jv("W5-B-09.nach") == B03 and jv("W5-B-09.leer") == "true"
rows = [z.split("|") for z in jv("W5-B-10.tab").strip(";").split(";")]
blk, fel, loe = gap_tab(["Durchlauf", "entnommen", "Schlange (vorne → hinten)"], rows, {1: "zahl", 2: "liste"}, "z", fest=(0,))
B.append(task("W5-B-10", "Levelorder-Protokoll", 2, "Tracetabelle", ["P8"],
    [T("Führe `levelorder(t)` (Schlange vom Inhaltstyp BinTree, nur nicht leere Teilbäume werden eingereiht) aus. Schlange: vorne zuerst, Wurzelwerte mit Komma, leer: –."),
     BAUM(B10), blk],
    gaps(fel), loe, [T("Ausgabe: `\"%s\"`." % wl(vals(nodes_level(parse(B10)))))]))
for i in range(3): assert jv("W5-B-11.v%d" % i) == "OK" and jv("W5-B-11.nurEinWeg%d" % i) == "false"
B.append(task("W5-B-11", "Lückencode: Suche im Suchbaum", 2, "Lückencode", ["P4", "P7"],
    [T("Ergänze die rekursive Suche im binären Suchbaum. In jedem Schritt darf nur **ein** Teilbaum durchsucht werden."), C(B11)],
    gaps({"g1": TX("code", 14), "g2": TX("code", 20), "g3": TX("code", 22), "g4": TX("code", 22)}), B11_L,
    [T("Basisfall leer → false; Wert casten (P4); bei x < wert nur links, sonst nur rechts weitersuchen – und das Ergebnis **zurückgeben** (P7). "
       "Alle akzeptierten Varianten wurden für x = 0 … 100 gegen die Musterlösung getestet.")]))
t12 = parse(B12); post12 = vals(nodes_post(t12)); in12 = vals(nodes_in(t12))
assert ks(from_post_in(post12, in12)) == B12
B.append(task("W5-B-12", "Rekonstruktion aus Post- und Inorder", 3, "Bäume", [],
    [T("Postorder: `%s` · Inorder: `%s`. Baue den Baum." % (" ".join(post12), " ".join(in12)))], tree_bauen("-", sorted(in12)), {"baum": B12},
    [T("Das **letzte** Element der Postorder ist die Wurzel (A). In der Inorder liegt links davon B D, rechts F E G C."), BAUM(B12)]))
v13 = OC513.gueltig(J); assert v13 == [["t1", "t2", "t3", "t4"]] and all(not o.gueltig(J) for o in OC513d)
B.append(task("W5-B-13", "Puzzle: Knoten auf Ebene k", 3, "Methode implementieren", ["P7"],
    [T("Setze `anzahlAufEbene(b: BinTree, ebene: Ganzzahl): Ganzzahl` zusammen (Wurzel = Ebene 0). Drei Teile sind Fallen.")],
    order([(k, T513[k]) for k in ["t1", "t2", "t3", "t4", "d1", "d2", "d3"]]), {"reihenfolgen": v13},
    [C("\n".join(T513[k] for k in ["t1", "t2", "t3", "t4"])),
     T("Erst leer prüfen (sonst zählt ein leerer Baum auf Ebene 0 mit), dann Ebene 0 → 1, sonst in beiden Teilbäumen eine Ebene tiefer suchen (`ebene - 1`). "
       "`isLeaf` als Basisfall wäre falsch: Ein Blatt auf Ebene 2 darf bei Ebene 0 nicht gezählt werden.")]))
B.append(task("W5-B-14", "Gefälschter Suchbaum", 3, "Funktionsweise erläutern", ["P10"],
    [BAUM(B14), T("`nurKinder(b)` = [[a]] · `istBST(b, -1, -1)` = [[b]] · `suche(b, 60)` = [[c]] · Welcher Wert verletzt die Suchbaum-Ordnung? [[d]] "
                  "Gegenüber welchem Vorfahren? [[e]]")],
    gaps({"a": AW(["true", "false"]), "b": AW(["true", "false"]), "c": AW(["true", "false"]), "d": Z(), "e": Z()}),
    {"a": [same("true", "W5-B-14.nur")], "b": [same("false", "W5-B-14.ist")], "c": [same("false", "W5-B-14.s60")], "d": ["60"], "e": ["50"]},
    [T("60 ist rechtes Kind von 30 (passt), liegt aber im **linken** Teilbaum der Wurzel 50 – zu groß. `suche(b, 60)` geht deshalb nach rechts und findet 60 nie.")]))
tb15 = parse(B15); pre15 = nodes_pre(tb15)
B.append(task("W5-B-15", "Der Rechenbaum des Orakels", 3, "Bäume", [],
    [T("Gib den Wert des Termbaums an (`/` ganzzahlig): [[w]]. Klicke danach die Knoten in **Preorder** an.")],
    [gaps({"w": Z()}), tree_klick(B15)],
    [{"w": [same(35, "W5-B-15.wert")]}, klick(paths(pre15))],
    [T("(9 − 4) · (8 / 2 + 3) = 5 · 7 = **35**. Preorder (Präfix-Schreibweise): %s." % " ".join(vals(pre15)))]))

# #######################################################################################
#  Ausgabe
# #######################################################################################
welt5 = {"version": 2, "welt": 5, "titel": "Der Wald", "farbe": "#3B7A3B", "levels": LEVELS,
         "boss": {"id": "W5-BOSS", "titel": "Die drei Baumhüter – Online-Duell", "dauerMin": 25, "anzahl": 8,
                  "mix": {"1": 3, "2": 3, "3": 2}, "pool": [t["id"] for t in B]},
         "aufgaben": AUFG + B}

ZUSATZ = {
 "W5-L3-07": "P8: Beim Protokollieren genau der Datenstruktur folgen – ein Stapel arbeitet nach LIFO; nicht aus Gewohnheit die Levelorder hinschreiben.",
 "W5-L5-02": "P10: „abschätzen“ heißt Zahl **und** Begründung – k volle Ebenen fassen 2^k − 1 Knoten.",
 "W5-L5-03": "P10: Im Abitur zählt die Begründung über die Ebenen, nicht die bloße Zahl.",
 "W5-L5-05": "P8: Jede Zeile vollständig – auch die Aufrufe mit leerem Bereich bekommen eine Zeile.",
 "W5-L5-07": "P10: Wer erläutern soll, warum F kein Suchbaum ist, nennt das verletzende Paar (45 im linken Teilbaum der 40) – nicht nur „die Ordnung ist verletzt“.",
 "W5-L5-08": "P1: Der Basisfall `isEmpty` steht vor `getItem`. P7: Beide rekursiven Ergebnisse werden mit && verknüpft und zurückgegeben.",
 "W5-B-05": "P10: Begründung über die Ebenen: k volle Ebenen = 2^k − 1 Knoten.",
 "W5-B-08": "P7: Erstaufruf Tiefe 0. P8: Auch der Aufruf mit dem leeren Teilbaum bekommt eine Zeile.",
 "W5-B-10": "P8: Jeder Durchlauf eine Zeile, auch der letzte mit leerer Schlange.",
 "W5-B-13": "P7: Falscher Basisfall (Blatt statt leer, 0 statt 1) oder fehlendes `ebene - 1` liefert falsche Zählungen.",
 "W5-B-14": "P10: Beim Begründen das verletzende Paar aus Knoten und Vorfahre nennen.",
}
for a in AUFG + B:
    if a["id"] in ZUSATZ: a["erklaerung"].append(H(ZUSATZ[a["id"]]))
str_loesungen(welt5["aufgaben"])
os.makedirs(SCRATCH + "/algolab/content", exist_ok=True)
json.dump(welt5, open(SCRATCH + "/algolab/content/welt5.json", "w"), ensure_ascii=False, indent=1)
print("welt5.json:", len(LEVELS), "Level,", len(AUFG), "Level-Aufgaben,", len(B), "Boss-Aufgaben,", len(chk), "Python/Java-Abgleiche")
