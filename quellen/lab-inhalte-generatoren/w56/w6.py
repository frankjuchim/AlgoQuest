# Welt 6 "Der Endgegner" – Algo Quest Lab: Fallenjagd P1–P10, Abi-Mix, Boss "Generalprobe online"
# Eigene Kontexte (Schatzkammer/Truhen, Drachenhort, Level-Editor) – NICHT Paketstation/Ladepark/Kletterhalle.
import sys, json, math
sys.path.insert(0, "/tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad/algolab/w56")
from common import *

J6 = Java("w6")
def jt(key, ausdruck): return '        K.out("%s", %s);' % (key, ausdruck)

KLASSEN = r'''
package aq;
class Truhe {
    private String name; private int gold;
    public Truhe(String name, int gold) { this.name = name; this.gold = gold; }
    public String getName() { return name; }
    public int getGold() { return gold; }
    public String toString() { return name + ":" + gold; }
}
class Held {
    private String name; private int leben; private int maxLeben; private int staerke; private int gold;
    public Held(String name) { this.name = name; maxLeben = 100; leben = 100; staerke = 10; gold = 0; }
    public String getName() { return name; }
    public int getLeben() { return leben; }
    public void nimmSchaden(int schaden) { leben = leben - schaden; if (leben < 0) { leben = 0; } }
    public void heilen(int punkte) { leben = leben + punkte; if (leben > maxLeben) { leben = maxLeben; } }
}
class Typ {
    static String t(int x) { return "int"; } static String t(double x) { return "double"; } static String t(String x) { return "String"; }
    static String t(char x) { return "char"; } static String t(boolean x) { return "boolean"; }
    static String stapel(Stack s) { Stack h = new Stack(); String r = ""; while (!s.isEmpty()) h.push(s.pop());
        while (!h.isEmpty()) { Object o = h.pop(); r += (r.length() > 0 ? "," : "") + o; s.push(o); } return r; }
    static String schlange(Queue q) { Queue h = new Queue(); String r = ""; while (!q.isEmpty()) { Object o = q.dequeue(); r += (r.length() > 0 ? "," : "") + o; h.enqueue(o); }
        while (!h.isEmpty()) q.enqueue(h.dequeue()); return r; }
    static String dyn(DynArray d) { String r = ""; for (int i = 0; i < d.getLength(); i++) r += (i > 0 ? "," : "") + d.getItem(i); return r; }
}
'''
J6.add_raw("Klassen", KLASSEN)

# ======================================================================= 6.1 Fallenjagd I
C101 = '''// liefert das Gold der obersten Truhe; -1, wenn der Stapel leer ist
public static int obersteTruhe(Stack s) {
    Truhe t = (Truhe) s.top();
    if (s.isEmpty()) {
        return -1;
    }
    return t.getGold();
}'''
J6.add("F101", C101, '''        try { obersteTruhe(new Stack()); K.out("W6-L1-01.z", "kein Fehler"); } catch (IllegalStateException e) { K.out("W6-L1-01.z", K.zeile(e, "F101", 2)); }
        Stack s = new Stack(); s.push(new Truhe("Kupfer", 12)); s.push(new Truhe("Silber", 30)); K.out("W6-L1-01.voll", obersteTruhe(s));''')
J6.add("F101fix", C101.replace("    Truhe t = (Truhe) s.top();\n    if (s.isEmpty()) {\n        return -1;\n    }\n",
                                "    if (s.isEmpty()) {\n        return -1;\n    }\n    Truhe t = (Truhe) s.top();\n"),
       '        K.out("W6-L1-01.fix", obersteTruhe(new Stack()));')

C102 = '''// Gold der Truhe an Position index; -1 bei ungueltigem Index
public static int goldAn(DynArray d, int index) {
    if (index < [[g1]] || index > [[g2]]) {
        return -1;
    }
    Truhe t = (Truhe) d.getItem(index);
    return t.getGold();
}'''
L102 = {"g1": ["0"], "g2": ["d.getLength()-1", "(d.getLength()-1)"]}
for i, g2 in enumerate(L102["g2"]):
    J6.add("F102_%d" % i, C102.replace("[[g1]]", "0").replace("[[g2]]", g2), '''        DynArray d = new DynArray(); d.append(new Truhe("A", 5)); d.append(new Truhe("B", 9)); d.append(new Truhe("C", 2));
        String r = ""; for (int k = -2; k <= 4; k++) r += goldAn(d, k) + " "; r += "|" + goldAn(new DynArray(), 0);
        K.out("W6-L1-02.v%d", r);''' % i)

C103 = '''// zaehlt die Edelsteine im Stapel s; s soll danach unveraendert sein
public static int zaehle(Stack s) {
    int anzahl = 0;
    Queue hilf = new Queue();
    while (!s.isEmpty()) {
        hilf.enqueue(s.pop());
        anzahl = anzahl + 1;
    }
    while (!hilf.isEmpty()) {
        s.push(hilf.dequeue());
    }
    return anzahl;
}'''
START103 = ["Rubin", "Saphir", "Gold", "Smaragd"]
J6.add("F103", C103, '''        Stack s = new Stack(); %s
        int n = zaehle(s); K.out("W6-L1-03.n", n); K.out("W6-L1-03.s", Typ.stapel(s));''' % " ".join('s.push("%s");' % x for x in START103))
J6.add("F103fix", C103.replace("Queue hilf = new Queue();", "Stack hilf = new Stack();").replace("hilf.enqueue(s.pop())", "hilf.push(s.pop())").replace("s.push(hilf.dequeue())", "s.push(hilf.pop())"),
       '''        Stack s = new Stack(); %s
        zaehle(s); K.out("W6-L1-03.fix", Typ.stapel(s));''' % " ".join('s.push("%s");' % x for x in START103))

SIG104 = [("anzahlReicher(truhen: Reihung von Truhe, grenze: Ganzzahl): Ganzzahl", "anzahlReicher", [("a1", "int"), ("a2", "Truhe[]"), ("a3", "int")], "truhen", "grenze"),
          ("istLeer(q: Schlange vom Inhaltstyp Ganzzahl): Wahrheitswert", "istLeer", [("b1", "boolean"), ("b2", "Queue")], "q", None),
          ("durchschnitt(r: Reihung von Ganzzahl): Kommazahl", "durchschnitt", [("c1", "double"), ("c2", "int[]")], "r", None),
          ("zeigen(t: Truhe): nichts", "zeigen", [("d1", "void"), ("d2", "Truhe")], "t", None)]
src = ""
for sig, name, fl, p1, p2 in SIG104:
    typen = [v for k, v in fl]
    ret = typen[0]
    params = "%s %s" % (typen[1], p1) + (", %s %s" % (typen[2], p2) if p2 else "")
    body = {"int": "return 0;", "boolean": "return true;", "double": "return 0.0;", "void": ""}[ret]
    src += "    public static %s %s(%s) { %s }\n" % (ret, name, params, body)
J6.add("F104", src, '        K.out("W6-L1-04.ok", "kompiliert");')

C105 = '''public static int indexVon(String[] namen, String gesucht) {
    for (int i = 0; i < namen.length; i++) {
        if (namen[i].equals(gesucht)) {
            return i;
        }
    }
}'''
J6.expect_compile_error("W6-L1-05.zeile", "F105", C105)
J6.add("F105fix", C105.replace("    }\n}", "    }\n    return -1;\n}"), '        K.out("W6-L1-05.fix", indexVon(new String[]{"Ork", "Elf"}, "Elf") + "," + indexVon(new String[]{"Ork"}, "Zwerg"));')

AUSDR106 = [("a", "7 / 2"), ("b", "7 / 2.0"), ("c", "(double) (7 / 2)"), ("d", '"Gold" + 1 + 2'), ("e", '1 + 2 + "Gold"'),
            ("f", "(int) 'A' + 2"), ("g", "(char) ('A' + 2)"), ("h", "17 % 5")]
J6.add("F106", "", "\n".join('        K.out("W6-L1-06.%s", (%s) + "|" + Typ.t(%s));' % (k, a, a) for k, a in AUSDR106))

C107 = '''// zaehlt, wie oft name in der Reihung namen vorkommt
public static int zaehle(String[] namen, String name) {
    int anzahl = 0;
    for (int i = 0; i < namen.length; i++) {
        if (namen[i] == name) {
            anzahl = anzahl + 1;
        }
    }
    return anzahl;
}'''
J6.add("F107", C107, '''        String[] n = {new String("Ork"), "Elf", new String("Ork")};
        K.out("W6-L1-07.bug", zaehle(n, new String("Ork")));''')
for i, v in enumerate(["namen[i].equals(name)", "name.equals(namen[i])"]):
    J6.add("F107fix%d" % i, C107.replace("namen[i] == name", v), '''        String[] n = {new String("Ork"), "Elf", new String("Ork")};
        K.out("W6-L1-07.fix%d", zaehle(n, new String("Ork")));''' % i)

# ======================================================================= 6.2 Fallenjagd II
C201 = '''// groesstes Gold in der Reihung r (r nicht leer)
public static int maximum(int[] r) {
    int max = r[0];
    for (int i = 1; i <= r.length; i++) {
        if (r[i] > max) {
            max = r[i];
        }
    }
    return max;
}'''
J6.add("F201", C201, '''        try { maximum(new int[]{4, 11, 7}); K.out("W6-L2-01.z", "kein Fehler"); } catch (ArrayIndexOutOfBoundsException e) { K.out("W6-L2-01.z", K.zeile(e, "F201", 2)); }''')
J6.add("F201fix", C201.replace("i <= r.length", "i < r.length"), '        K.out("W6-L2-01.fix", maximum(new int[]{4, 11, 7}) + "," + maximum(new int[]{20}));')

R202 = [3, 8, 12, 17, 21, 26, 33, 40, 47, 52, 58]; X202 = 50
C202 = '''public static int binaer(int[] r, int x) {
    int lo = 0;
    int hi = r.length - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (r[mid] == x) {
            return mid;
        }
        if (r[mid] < x) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return -1;
}'''
J6.add("F202", C202 + '''
    static String mids = "";
    static int binaerLog(int[] r, int x) { int lo = 0, hi = r.length - 1; while (lo <= hi) { int mid = (lo + hi) / 2; mids += mid + " ";
        if (r[mid] == x) return mid; if (r[mid] < x) lo = mid + 1; else hi = mid - 1; } return -1; }''',
       '''        int[] r = {%s}; K.out("W6-L2-02.erg", binaer(r, %d)); binaerLog(r, %d); K.out("W6-L2-02.mids", mids.trim());''' % (", ".join(map(str, R202)), X202, X202))

C203 = '''public static int zerlege(int n) {
    if (n < 3) {
        return n;
    }
    return zerlege(n / 3) + n % 3;
}'''
J6.add("F203", C203 + '''
    static String log = "";
    static int z(int n, int t) { String pre = t + "|" + n + "|"; int p = log.length(); log += pre + "#;";
        int e = (n < 3) ? n : z(n / 3, t + 1) + n % 3;
        int q = log.indexOf(pre + "#;", p); log = log.substring(0, q) + pre + e + ";" + log.substring(q + pre.length() + 2); return e; }''',
       '''        z(50, 0); K.out("W6-L2-03.tab", log); K.out("W6-L2-03.e500", zerlege(500)); log = ""; z(500, 0); K.out("W6-L2-03.tab500", log);''')

C204 = '''// zaehlt die geraden Werte in r ab Index i
public static int zaehleGerade(int[] r, int i) {
    if (i == r.length) {
        return 0;
    }
    int rest = zaehleGerade(r, i + 1);
    if (r[i] % 2 == 0) {
        return 1;
    }
    return 0;
}'''
J6.add("F204", C204, '        K.out("W6-L2-04.bug", zaehleGerade(new int[]{4, 7, 2, 8, 5}, 0));')
FIX204 = [("rest+1", "rest"), ("1+rest", "rest")]
for i, (a, b) in enumerate(FIX204):
    code = C204.replace("        return 1;", "        return %s;" % a).replace("    return 0;\n}", "    return %s;\n}" % b)
    J6.add("F204fix%d" % i, code, '        K.out("W6-L2-04.fix%d", zaehleGerade(new int[]{4, 7, 2, 8, 5}, 0) + "," + zaehleGerade(new int[]{}, 0));' % i)

R205 = [4, 9, 2, 9, 6]
C205 = '''int[] r = {%s};
int max = r[0];
int anzahl = 1;
for (int i = 1; i < r.length; i++) {
    if (r[i] > max) {
        max = r[i];
        anzahl = 1;
    } else if (r[i] == max) {
        anzahl = anzahl + 1;
    }
}''' % ", ".join(map(str, R205))
J6.add("F205", "", '''        int[] r = {%s}; int max = r[0]; int anzahl = 1; String log = "–|–|" + max + "|" + anzahl + ";"; int i;
        for (i = 1; i < r.length; i++) { if (r[i] > max) { max = r[i]; anzahl = 1; } else if (r[i] == max) { anzahl = anzahl + 1; }
            log += i + "|" + r[i] + "|" + max + "|" + anzahl + ";"; }
        log += i + "|–|" + max + "|" + anzahl + ";"; K.out("W6-L2-05.tab", log);''' % ", ".join(map(str, R205)))

C207 = '''public static int anzahlUeber(int[] r, int grenze) {
    int anzahl = 0;
    for (int i = 0; i < r.length; i++) {
        if (r[i] > grenze) {
            anzahl++;
        }
    }
    return anzahl;
}'''
J6.add("F207", C207, '        K.out("W6-L2-07.t", anzahlUeber(new int[]{3, 12, 8, 15}, 8));')

# ======================================================================= 6.3 Abi-Mix I
X301 = 14
AUSDR301 = [("a", "x % 4 == 2"), ("b", "x / 4 * 4"), ("c", "x > 10 && x % 2 == 1"), ("d", "!(x < 10) || x == 3"), ("e", "(double) x / 4")]
J6.add("F301", "", "        int x = %d;\n" % X301 + "\n".join('        K.out("W6-L3-01.%s", (%s) + "|" + Typ.t(%s));' % (k, a, a) for k, a in AUSDR301))
C302 = '''Held a = new Held("Aria");
Held b = new Held("Bo");
Held c = a;
c.nimmSchaden(30);
b = c;
b.heilen(10);
a = new Held("Aria");'''
J6.add("F302", "", "\n".join("        " + l for l in C302.splitlines()) + "\n" + "\n".join([
    jt("W6-L3-02.c", "c.getLeben()"), jt("W6-L3-02.a", "a.getLeben()"), jt("W6-L3-02.ac", "a == c"), jt("W6-L3-02.bc", "b == c"),
    jt("W6-L3-02.eq", "a.getName().equals(c.getName())")]))
START304 = [29, 14, 37, 8, 21]
START305 = [5, 2, 8, 1, 6]
SORT = r'''
    static String sel(int[] r) { String log = ""; int v = 0;
        for (int i = 0; i < r.length - 1; i++) { int m = i; for (int j = i + 1; j < r.length; j++) { v++; if (r[j] < r[m]) m = j; }
            if (m != i) { int h = r[i]; r[i] = r[m]; r[m] = h; log += "[" + i + "," + m + "]"; } }
        return log + "|" + v + "|" + java.util.Arrays.toString(r); }
    static String selTab(int[] r) { String log = ""; int v = 0;
        for (int i = 0; i < r.length - 1; i++) { int m = i; for (int j = i + 1; j < r.length; j++) { v++; if (r[j] < r[m]) m = j; }
            boolean t = m != i; if (t) { int h = r[i]; r[i] = r[m]; r[m] = h; }
            String s = ""; for (int k = 0; k < r.length; k++) s += (k > 0 ? ", " : "") + r[k];
            log += i + "|" + m + "|" + (t ? "ja" : "nein") + "|" + s + "|" + v + ";"; }
        return log; }
    static String ins(int[] r) { String log = "";
        for (int i = 1; i < r.length; i++) { int j = i; while (j > 0 && r[j - 1] > r[j]) { int h = r[j]; r[j] = r[j - 1]; r[j - 1] = h; log += "[" + (j - 1) + "," + j + "]"; j--; } }
        return log + "|" + java.util.Arrays.toString(r); }
    static int selVergl(int n) { int[] r = new int[n]; for (int i = 0; i < n; i++) r[i] = (i * 7919) % 1009; String s = sel(r); return Integer.parseInt(s.split("\\|")[1]); }
    static int binMax(int n) { int[] r = new int[n]; for (int i = 0; i < n; i++) r[i] = 2 * i; int best = 0;
        for (int x = -1; x <= 2 * n; x++) { int lo = 0, hi = n - 1, d = 0; while (lo <= hi) { d++; int mid = (lo + hi) / 2; if (r[mid] == x) break; if (r[mid] < x) lo = mid + 1; else hi = mid - 1; }
            if (d > best) best = d; } return best; }
    static String binTrace(int[] r, int x) { String log = ""; int lo = 0, hi = r.length - 1;
        while (lo <= hi) { int mid = (lo + hi) / 2; log += lo + "|" + hi + "|" + mid + "|" + r[mid] + ";"; if (r[mid] == x) return log + "=" + mid; if (r[mid] < x) lo = mid + 1; else hi = mid - 1; }
        return log + "=-1|" + lo + "|" + hi; }
'''
R307 = [6, 11, 17, 24, 30, 36, 45, 52, 60]; X307 = 52
J6.add("F30x", SORT, "\n".join([
    jt("W6-L3-04.sel", "sel(new int[]{%s})" % ", ".join(map(str, START304))),
    jt("W6-L3-05.ins", "ins(new int[]{%s})" % ", ".join(map(str, START305))),
    jt("W6-L3-06.v10", "selVergl(10)"), jt("W6-L3-06.v20", "selVergl(20)"), jt("W6-L3-06.b1000", "binMax(1000)"), jt("W6-L3-06.b2000", "binMax(2000)"),
    jt("W6-L3-07.tab", "binTrace(new int[]{%s}, %d)" % (", ".join(map(str, R307)), X307)),
    jt("W6-B-13.tab", "selTab(new int[]{7, 3, 9, 1, 5})"),
]))

# ======================================================================= 6.4 Abi-Mix II
R401 = [2, 5, 9, 13, 18, 24, 30, 37]; X401 = 10
C401 = '''public static int binaerRek(int[] r, int x, int lo, int hi) {
    if (lo > hi) {
        return -1;
    }
    int mid = (lo + hi) / 2;
    if (r[mid] == x) {
        return mid;
    }
    if (r[mid] < x) {
        return binaerRek(r, x, mid + 1, hi);
    }
    return binaerRek(r, x, lo, mid - 1);
}'''
J6.add("F401", C401 + '''
    static String log = "";
    static int b(int[] r, int x, int lo, int hi, int t) { String pre = t + "|" + lo + "|" + hi + "|" + (lo > hi ? "–" : "" + (lo + hi) / 2) + "|";
        int p = log.length(); log += pre + "#;"; int e;
        if (lo > hi) e = -1; else { int mid = (lo + hi) / 2; if (r[mid] == x) e = mid; else if (r[mid] < x) e = b(r, x, mid + 1, hi, t + 1); else e = b(r, x, lo, mid - 1, t + 1); }
        int q = log.indexOf(pre + "#;", p); log = log.substring(0, q) + pre + e + ";" + log.substring(q + pre.length() + 2); return e; }''',
       '        int[] r = {%s}; b(r, %d, 0, r.length - 1, 0); K.out("W6-L4-01.tab", log); K.out("W6-L4-01.erg", binaerRek(r, %d, 0, r.length - 1));' % (
           ", ".join(map(str, R401)), X401, X401))
C403 = '''s.push(q.dequeue());
q.enqueue(s.top());
s.push(q.dequeue());
q.enqueue(s.pop());
s.push(q.dequeue());
s.push(q.head());'''
START403 = [3, 7, 1, 9]
J6.add("F403", "", "        Stack s = new Stack(); Queue q = new Queue(); %s\n" % " ".join("q.enqueue(%d);" % x for x in START403) +
       "\n".join("        " + l for l in C403.splitlines()) + "\n" + jt("W6-L4-03.s", "Typ.stapel(s)") + "\n" + jt("W6-L4-03.q", "Typ.schlange(q)"))
C404 = '''DynArray d = new DynArray();
d.append("Axt");
d.append("Bogen");
d.insertAt(1, "Dolch");
d.append("Elixier");
d.delete(0);
d.setItem(1, "Fackel");
d.insertAt(3, "Gift");'''
J6.add("F404", "", "\n".join("        " + l for l in C404.splitlines()) + "\n" + jt("W6-L4-04.d", "Typ.dyn(d)"))
C405 = '''public static boolean suche(BinTree b, int x) {
    int wert = (Integer) b.getItem();
    if (x == wert) {
        return true;
    }
    if (x < wert) {
        return suche(b.getLeft(), x);
    }
    return suche(b.getRight(), x);
}'''
J6.add("F405", C405, '''        try { K.out("W6-L4-05.da", suche(K.baue("20(10,30)"), 30)); suche(K.baue("20(10,30)"), 25); K.out("W6-L4-05.z", "kein Fehler"); }
        catch (IllegalStateException e) { K.out("W6-L4-05.z", K.zeile(e, "F405", 2)); }''')
J6.add("F405fix", C405.replace("    int wert", "    if (b.isEmpty()) {\n        return false;\n    }\n    int wert"),
       '        K.out("W6-L4-05.fix", suche(K.baue("20(10,30)"), 25) + "," + suche(K.baue("20(10,30)"), 10) + "," + suche(new BinTree(), 1));')
START406 = [6, 9, 2, 7, 1, 8, 4]
J6.add("F406", r'''
    static String zerlege(int[] r, int lo, int hi) { String log = ""; int pivot = r[lo]; int grenze = lo;
        for (int i = lo + 1; i <= hi; i++) { if (r[i] < pivot) { grenze = grenze + 1; if (grenze == i) log += "!"; int h = r[grenze]; r[grenze] = r[i]; r[i] = h; log += "[" + grenze + "," + i + "]"; } }
        int h = r[lo]; r[lo] = r[grenze]; r[grenze] = h; log += "[" + lo + "," + grenze + "]"; return log + "|" + java.util.Arrays.toString(r) + "|" + grenze; }''',
       jt("W6-L4-06.z", "zerlege(new int[]{%s}, 0, %d)" % (", ".join(map(str, START406)), len(START406) - 1)))
C407 = '''public static int summe(Queue q) {
    int s = 0;
    Queue hilf = new Queue();
    while (!q.isEmpty()) {
        int x = (Integer) q.dequeue();
        s = s + x;
        hilf.enqueue(x);
    }
    while (!hilf.isEmpty()) {
        q.enqueue(hilf.dequeue());
    }
    return s;
}'''
J6.add("F407", C407, '        Queue q = new Queue(); q.enqueue(4); q.enqueue(9); q.enqueue(2); K.out("W6-L4-07.s", summe(q)); K.out("W6-L4-07.q", Typ.schlange(q));')

# ======================================================================= Boss
CB01 = '''// Name des naechsten Gegners in der Welle; "" wenn die Welle leer ist
public static String naechster(Queue welle) {
    String name = (String) welle.dequeue();
    if (welle.isEmpty()) {
        return "";
    }
    return name;
}'''
J6.add("FB01", CB01, '''        try { naechster(new Queue()); K.out("W6-B-01.z", "kein Fehler"); } catch (IllegalStateException e) { K.out("W6-B-01.z", K.zeile(e, "FB01", 2)); }
        Queue q = new Queue(); q.enqueue("Ork"); K.out("W6-B-01.eins", "[" + naechster(q) + "]");''')
AUSDRB02 = [("a", "11 / 4"), ("b", "11 % 4"), ("c", "11 / 4.0")]
J6.add("FB02", "", "\n".join('        K.out("W6-B-02.%s", (%s) + "|" + Typ.t(%s));' % (k, a, a) for k, a in AUSDRB02))
RB04 = [2, 6, 11, 15, 19, 24, 28, 35, 41]; XB04 = 6
J6.add("FB04", C202 + '''
    static String mids = "";
    static int binaerLog(int[] r, int x) { int lo = 0, hi = r.length - 1; while (lo <= hi) { int mid = (lo + hi) / 2; mids += mid + " ";
        if (r[mid] == x) return mid; if (r[mid] < x) lo = mid + 1; else hi = mid - 1; } return -1; }''',
       '        int[] r = {%s}; binaerLog(r, %d); K.out("W6-B-04.mids", mids.trim()); K.out("W6-B-04.erg", binaer(r, %d));' % (", ".join(map(str, RB04)), XB04, XB04))
SIGB05 = [("summeAb(b: BinTree vom Inhaltstyp Ganzzahl, grenze: Ganzzahl): Ganzzahl", [("a1", "int"), ("a2", "BinTree"), ("a3", "int")]),
          ("letzteTruhe(d: dynamische Reihung vom Inhaltstyp Truhe): Truhe", [("b1", "Truhe"), ("b2", "DynArray")])]
J6.add("FB05", "    public static int summeAb(BinTree b, int grenze) { return 0; }\n    public static Truhe letzteTruhe(DynArray d) { return null; }",
       '        K.out("W6-B-05.ok", "kompiliert");')
CB06 = '''// liefert das groesste Gold in q; q soll unveraendert bleiben
public static int maxGold(Queue q) {
    int max = -1;
    int n = 0;
    Queue hilf = new Queue();
    while (!q.isEmpty()) {
        int x = (Integer) q.dequeue();
        if (x > max) {
            max = x;
        }
        hilf.enqueue(x);
        n = n + 1;
    }
    for (int i = 0; i < n - 1; i++) {
        q.enqueue(hilf.dequeue());
    }
    return max;
}'''
STARTB06 = [12, 40, 7, 25]
J6.add("FB06", CB06, '        Queue q = new Queue(); %s K.out("W6-B-06.max", maxGold(q)); K.out("W6-B-06.q", Typ.schlange(q));' % " ".join("q.enqueue(%d);" % x for x in STARTB06))
CB07 = '''public static String runen(int n) {
    if (n <= 0) {
        return "";
    }
    if (n % 2 == 0) {
        return runen(n - 2) + "#";
    }
    return "*" + runen(n - 1);
}'''
J6.add("FB07", CB07 + '''
    static String log = "";
    static String m(int n, int t) { String pre = t + "|" + n + "|"; int p = log.length(); log += pre + "#;"; String e;
        if (n <= 0) e = ""; else if (n % 2 == 0) e = m(n - 2, t + 1) + "#"; else e = "*" + m(n - 1, t + 1);
        int q = log.indexOf(pre + "#;", p); log = log.substring(0, q) + pre + "\\"" + e + "\\";" + log.substring(q + pre.length() + 2); return e; }''',
       '        m(7, 0); K.out("W6-B-07.tab", log); K.out("W6-B-07.erg", runen(7));')
NB08 = 4073
J6.add("FB08", "", '''        int n = %d; int s = 0; int k = 0; String log = n + "|" + s + "|" + k + ";";
        while (n > 0) { s = s + n %% 10; n = n / 10; k = k + 1; log += n + "|" + s + "|" + k + ";"; }
        K.out("W6-B-08.tab", log);''' % NB08)
CB11 = '''// entfernt alle Truhen mit 0 Gold aus d
public static void entferneLeere(DynArray d) {
    for (int i = 0; i < d.getLength(); i++) {
        Truhe t = (Truhe) d.getItem(i);
        if (t.getGold() == 0) {
            d.delete(i);
        }
    }
}'''
STARTB11 = [("Eiche", 5), ("Buche", 0), ("Birke", 0), ("Linde", 8), ("Ulme", 0)]
J6.add("FB11", CB11, '        DynArray d = new DynArray(); %s entferneLeere(d); K.out("W6-B-11.d", Typ.dyn(d));' % " ".join('d.append(new Truhe("%s", %d));' % x for x in STARTB11))
TB12 = {
    "t1": "public static int zaehleAb(int[] r, int i, int x) {",
    "t2": "if (i == r.length) {\n    return 0;\n}",
    "t3": "int rest = zaehleAb(r, i + 1, x);",
    "t4": "if (r[i] == x) {\n    return rest + 1;\n}",
    "t5": "return rest;\n}",
    "d1": "if (i == r.length - 1) {\n    return 0;\n}",
    "d2": "zaehleAb(r, i + 1, x);",
    "d3": "if (r[i] == x) {\n    return 1;\n}",
}
TEST_B12 = '''            if (zaehleAb(new int[]{3, 5, 3, 3}, 0, 3) != 3) throw new RuntimeException("a");
            if (zaehleAb(new int[]{3, 5, 3, 3}, 0, 4) != 0) throw new RuntimeException("b");
            if (zaehleAb(new int[]{}, 0, 1) != 0) throw new RuntimeException("leer");
            if (zaehleAb(new int[]{1, 2, 1}, 1, 1) != 1) throw new RuntimeException("ab1");
            if (zaehleAb(new int[]{7}, 0, 7) != 1) throw new RuntimeException("eins");'''
OCB12 = OrderCheck(J6, "W6-B-12", TB12, ["t1"], ["t2", "t3", "t4"], ["t5"], TEST_B12, "OB12", signatur_vars=("r", "i", "x"))
OCB12d = [OrderCheck(J6, "W6-B-12d%d" % i, TB12, ["t1"] + mid, [], ["t5"], TEST_B12, "OB12d%d" % i, signatur_vars=("r", "i", "x"))
          for i, mid in enumerate([["d1", "t3", "t4"], ["t2", "t3", "d3"]])]
CB14 = '''public static int anzahl(Stack s) {
    int n = 0;
    Stack hilf = new Stack();
    while (!s.isEmpty()) {
        hilf.push(s.pop());
        n = n + 1;
    }
    while (!hilf.isEmpty()) {
        s.push(hilf.pop());
    }
    return n;
}'''
J6.add("FB14", CB14, '        Stack s = new Stack(); s.push("A"); s.push("B"); s.push("C"); K.out("W6-B-14.n", anzahl(s)); K.out("W6-B-14.s", Typ.stapel(s));')
CB15 = '''public static int zahl(String s) {
    int z = 0;
    for (int i = 0; i < s.length(); i++) {
        z = z * 10 + [[a]];
    }
    return z;
}'''
LB15 = ["(int)s.charAt(i)-(int)'0'", "s.charAt(i)-'0'", "(int)s.charAt(i)-48", "s.charAt(i)-48", "(int)s.charAt(i)-'0'", "(int)(s.charAt(i)-'0')"]
for i, v in enumerate(LB15):
    J6.add("FB15_%d" % i, CB15.replace("[[a]]", v), '        K.out("W6-B-15.v%d", zahl("907") + "," + zahl("0") + "," + zahl("12"));' % i)

# #######################################################################################
J = J6.run()
def jv(k):
    assert k in J, "Java-Schluessel fehlt: " + k
    return J[k]
LEVELS, AUFG = [], []
def level(id, nr, titel, ds, ab, ide, intro, tasks):
    LEVELS.append({"id": id, "nr": nr, "titel": titel, "ds": ds, "ab": ab, "ide": ide, "intro": intro, "aufgaben": [t["id"] for t in tasks]})
    AUFG.extend(tasks)
def tab_rows(key):
    return [z.split("|") for z in jv(key).strip(";").split(";")]
def gtab(kopf, rows, spalten, praefix, fest=()):
    """spalten: {index: 'zahl'|'text'|'liste'|'auswahl:a/b'}"""
    zeilen, felder, loes = [], {}, {}
    for i, row in enumerate(rows):
        z = []
        for c, w in enumerate(row):
            art = spalten.get(c)
            if art is None or i in fest or (w == "–" and art == "zahl"):
                z.append(w); continue
            fid = "%s%d%s" % (praefix, i + 1, "abcdefgh"[c]); z.append("[[%s]]" % fid)
            if art == "zahl": felder[fid] = Z(4); loes[fid] = [w]
            elif art == "text": felder[fid] = TX("text", 8); loes[fid] = [w] if w != "–" else ["–", "-"]
            elif art == "liste": felder[fid] = TX("text", 14); loes[fid] = [w, w.replace(", ", ","), w.replace(", ", " ")]
            elif art.startswith("auswahl:"): felder[fid] = AW(art[8:].split("/")); loes[fid] = [w]
        zeilen.append(z)
    return TAB(kopf, zeilen), felder, loes
def falle(*ps):
    namen = {"P1": "Laufzeitfehler nicht ausgeschlossen", "P2": "Struktur zerstört statt unverändert", "P3": "Signatur verfehlt",
             "P4": "Typen und Casts", "P5": "Zeichenketten mit == statt equals", "P6": "Off-by-one", "P7": "Rekursion",
             "P8": "Trace-/Dokumentationstabelle", "P9": "Struktogramm nicht nach EH §5", "P10": "Operator verfehlt"}
    return H("**Falle " + " + ".join("%s – %s" % (p, namen[p]) for p in ps) + "**")

# #######################################################################################
#  LEVEL 6.1 – Fallenjagd I (P1–P5)
# #######################################################################################
L1 = []
assert jv("W6-L1-01.z") == "3" and jv("W6-L1-01.fix") == "-1"
L1.append(task("W6-L1-01", "P1: Leerer Stapel, voller Absturz", 1, "Fehler im Java-Code", ["P1"],
    [falle("P1"), T("In der Schatzkammer liegen Truhen in einem Stapel vom Inhaltstyp Truhe. Die Methode stürzt ab, wenn der Stapel leer ist."), C(C101),
     T("Teil 1: Markiere die Zeile, in der der Laufzeitfehler auftritt. Teil 2: Wie behebst du ihn?")],
    [lines(2, 1), choice([("a", "Die Abfrage `if (s.isEmpty())` mit `return -1;` **vor** den Zugriff `s.top()` setzen."),
                          ("b", "`s.pop()` statt `s.top()` verwenden."), ("c", "`if (s == null)` abfragen."),
                          ("d", "Nichts – die Abfrage in Zeile 4 fängt den Fehler ab.")])],
    [{"zeilen": [3]}, {"richtig": ["a"]}],
    [T("Zeile 3: `top()` auf einem leeren Stapel → IllegalStateException. Die Abfrage in Zeile 4 kommt zu spät – der Absturz ist schon passiert. "
       "Korrigiert liefert die Methode für den leeren Stapel %s." % jv("W6-L1-01.fix")),
     H("P1: Erst fragen, dann zugreifen – `isEmpty()` vor `top`, `pop`, `head`, `dequeue`, `getItem`, `getLeft`. Ein leerer Stapel ist nicht `null`.")]))

for i in range(2): assert jv("W6-L1-02.v%d" % i) == "-1 -1 5 9 2 -1 -1 |-1"
L1.append(task("W6-L1-02", "P1: Indexgrenzen bewachen", 2, "Lückencode", ["P1", "P6"],
    [falle("P1", "P6"), T("Die Truhen liegen in einer dynamischen Reihung vom Inhaltstyp Truhe. Ergänze die Abfrage so, dass für **jeden** ungültigen Index −1 geliefert wird "
       "und kein Laufzeitfehler auftreten kann."), C(C102)],
    gaps({"g1": TX("code", 4), "g2": TX("code", 18)}), L102,
    [T("Gültig sind die Indizes 0 bis `d.getLength() - 1`. Mit `index > d.getLength()` bliebe `index == d.getLength()` erlaubt → IndexOutOfBoundsException (P6). "
       "Getestet mit den Indizes −2 … 4 und einer leeren Reihung: kein Laufzeitfehler."),
     H("Gleichwertig wäre `index >= d.getLength()` – hier ist der Vergleich mit `>` vorgegeben.")]))

L1.append(task("W6-L1-03", "P2: Die vertauschten Edelsteine", 2, "ADT-Befehlsfolgen", ["P2"],
    [falle("P2"), T("Der Stapel s enthält vor dem Aufruf (unten → oben): Rubin, Saphir, Gold, Smaragd. `zaehle(s)` soll s **unverändert** lassen."), ADT("stapel", START103), C(C103),
     T("Teil 1: Gib den Inhalt von s **nach** dem Aufruf an (unten → oben). Teil 2: Welche Änderung lässt s wirklich unverändert?")],
    [adtsim("stapel", START103),
     choice([("a", "Einen Hilfs**stapel** statt der Hilfsschlange verwenden (push/pop statt enqueue/dequeue)."),
             ("b", "Die zweite Schleife weglassen."), ("c", "Am Ende `s = hilf;` schreiben."),
             ("d", "In der ersten Schleife `s.top()` statt `s.pop()` verwenden.")])],
    [{"inhalt": jv("W6-L1-03.s").split(",")}, {"richtig": ["a"]}],
    [T("Die Schlange gibt die Edelsteine in der Reihenfolge zurück, in der sie vom Stapel kamen (Smaragd zuerst). Smaragd wird also zuerst wieder gepusht und liegt danach **unten**: "
       "s = %s (unten → oben) – umgekehrt!" % jv("W6-L1-03.s").replace(",", ", ")),
     T("Mit einem Hilfsstapel wird zweimal umgekehrt → Originalreihenfolge %s. `s = hilf;` ändert nur die lokale Variable (Referenz), "
       "`s.top()` in der Schleife wäre eine Endlosschleife." % jv("W6-L1-03.fix").replace(",", ", ")),
     H("P2: „unverändert“ = dieselben Elemente in derselben Reihenfolge. Stapel → Hilfsstapel, Schlange → Hilfsschlange.")]))

f104 = {}; l104 = {}
zeilen = []
for sig, name, fl, p1, p2 in SIG104:
    kopf = "public static [[%s]] %s([[%s]] %s" % (fl[0][0], name, fl[1][0], p1) + (", [[%s]] %s)" % (fl[2][0], p2) if p2 else ")")
    zeilen.append(["`%s`" % sig, kopf])
    for k, v in fl:
        f104[k] = TX("code", 9); l104[k] = [v]
assert jv("W6-L1-04.ok") == "kompiliert"
L1.append(task("W6-L1-04", "P3: Vom Kopf zum Methodenkopf", 1, "Methodenkopf und Signatur", ["P3"],
    [falle("P3"), T("Übersetze die Signaturen (EH-Notation) in Java-Methodenköpfe (alle `public static`).")] +
    [T("`%s`\n\n%s" % (z[0].strip("`"), z[1])) for z in zeilen],
    gaps(f104), l104,
    [T("Ganzzahl → `int`, Wahrheitswert → `boolean`, Kommazahl → `double`, nichts → `void`, Reihung von Truhe → `Truhe[]`, "
       "Schlange vom Inhaltstyp Ganzzahl → `Queue` (nicht generisch!). Alle vier Köpfe wurden mit javac übersetzt."),
     H("P3: Die Signatur ist Vertrag – falscher Rückgabetyp oder falscher Parametertyp kostet im Abitur Punkte, auch wenn der Rumpf stimmt.")]))

assert jv("W6-L1-05.zeile") == "7" and jv("W6-L1-05.fix") == "1,-1"
L1.append(task("W6-L1-05", "P3: Rückgabe vergessen", 2, "Fehler im Java-Code", ["P3"],
    [falle("P3"), T("`indexVon` soll den Index des ersten Vorkommens liefern, sonst −1. Der Compiler meldet einen Fehler."), C(C105),
     T("Teil 1: Markiere die Zeile, die der Compiler meldet. Teil 2: Welche Anweisung fehlt direkt davor? [[k]]")],
    [lines(2, 1), gaps({"k": TX("code", 12)})],
    [{"zeilen": [7]}, {"k": ["return -1;"]}],
    [T("javac meldet in Zeile 7: „%s“. Wird `gesucht` nicht gefunden, endet die Schleife ohne `return` – auf diesem Pfad fehlt die Rückgabe." % jv("W6-L1-05.zeile.msg")),
     T("Mit `return -1;` vor der letzten Klammer: `indexVon({\"Ork\", \"Elf\"}, \"Elf\")` = 1, nicht gefunden = −1."),
     H("P3: Rückgabe auf **jedem** Pfad – auch nach der Schleife.")]))

T106 = ["int", "double", "String", "char", "boolean"]
f106, l106, rows106 = {}, {}, []
for k, a in AUSDR106:
    w, t = jv("W6-L1-06.%s" % k).split("|")
    rows106.append(["`%s`" % a, "[[w%s]]" % k, "[[t%s]]" % k])
    f106["w" + k] = Z(5) if t in ("int", "double") else TX("exakt" if t == "char" else "text", 8)
    l106["w" + k] = [w]; f106["t" + k] = AW(T106); l106["t" + k] = [t]
L1.append(task("W6-L1-06", "P4: Typen und Werte", 3, "Datentypen und Ausdrücke", ["P4"],
    [falle("P4"), T("Gib Wert und Typ jedes Ausdrucks an (Kommazahlen mit Punkt oder Komma, Zeichenketten ohne Anführungszeichen)."),
     TAB(["Ausdruck", "Wert", "Typ"], rows106)],
    gaps(f106), l106,
    [T("\n".join("- `%s` → %s (%s)" % (a, *jv("W6-L1-06.%s" % k).split("|")) for k, a in AUSDR106)),
     T("Ganzzahlige Division schneidet ab (7 / 2 = 3); erst ein Kommazahl-Operand macht 3.5. `(double) (7 / 2)` castet zu spät → 3.0. "
       "Verkettung wird von links ausgewertet: \"Gold\" + 1 + 2 = \"Gold12\", aber 1 + 2 + \"Gold\" = \"3Gold\". `'A' + 2` ist int (67), erst `(char)` macht wieder ein Zeichen.")]))

assert jv("W6-L1-07.bug") == "0" and jv("W6-L1-07.fix0") == "2" and jv("W6-L1-07.fix1") == "2"
L1.append(task("W6-L1-07", "P5: Gleich ist nicht gleich", 1, "Fehler im Java-Code", ["P5"],
    [falle("P5"), T("`zaehle` liefert für die Reihung {\"Ork\", \"Elf\", \"Ork\"} und den Namen \"Ork\" manchmal 0 statt 2."), C(C107),
     T("Teil 1: Markiere die fehlerhafte Zeile. Teil 2: Korrigiere die Bedingung: `if ([[k]]) {`")],
    [lines(2, 1), gaps({"k": TX("code", 22)})],
    [{"zeilen": [5]}, {"k": ["namen[i].equals(name)", "name.equals(namen[i])"]}],
    [T("`==` vergleicht bei Objekten die **Referenzen**, nicht den Inhalt. Im Java-Test mit neu erzeugten Zeichenketten liefert die Methode %s statt 2; mit `equals` %s." % (
        jv("W6-L1-07.bug"), jv("W6-L1-07.fix0"))),
     H("P5: In der Online-IDE vergleicht `==` Zeichenketten zwar inhaltlich – im Abitur wird trotzdem `equals` verlangt.")]))

ERLAUBT = {"length()", "charAt(i)", "substring(a, b)", "equals(t)", "contains(t)", "compareTo(t)"}
OPT108 = ["length()", "charAt(i)", "substring(a, b)", "equals(t)", "contains(t)", "compareTo(t)", "toUpperCase()", "indexOf(c)", "split(\" \")", "trim()", "replace(a, b)"]
L1.append(task("W6-L1-08", "P5: Erlaubte Zeichenketten-Operationen", 1, "Datentypen und Ausdrücke", ["P5"],
    [falle("P5"), T("Welche Zeichenketten-Operationen sind laut Ergänzenden Hinweisen im Abitur erlaubt?")],
    choice([("o%d" % i, "`%s`" % o) for i, o in enumerate(OPT108)], mehrfach=True),
    {"richtig": ["o%d" % i for i, o in enumerate(OPT108) if o in ERLAUBT]},
    [T("Erlaubt (abschließende Liste): Länge, Zeichen an Position, Teilzeichenkette, Verketten, Gleichheit, enthält, lexikographischer Vergleich, ASCII-Wert ↔ Zeichen – "
       "in Java `length()`, `charAt(i)`, `substring(a, b)`, `+`, `equals`, `contains`, `compareTo`, `(int) c` / `(char) n`."),
     T("Nicht erlaubt: `toUpperCase`, `indexOf`, `split`, `trim`, `replace` (und auch `Integer.parseInt`) – wer sie benutzt, verliert Punkte, selbst wenn das Programm läuft.")]))

level("W6-L1", "6.1", "Fallenjagd I – P1 bis P5", [38], "AB 1 Korrektur und Fehlerjagd, Teil 4 (P1–P5)",
      "– (Papier-Training; Papier-Compiler: AQ_W6_Probeklausur_Papier-Compiler.txt)",
      [T("Die meisten Abiturpunkte gehen nicht durch fehlendes Wissen verloren, sondern durch **immer dieselben zehn Fehler**. Jede Aufgabe trainiert genau eine Falle."),
       H("P1 Laufzeitfehler nicht ausgeschlossen · P2 Struktur zerstört · P3 Signatur verfehlt · P4 Typen und Casts · P5 == statt equals / verbotene String-Operationen")], L1)

# #######################################################################################
#  LEVEL 6.2 – Fallenjagd II (P6–P10)
# #######################################################################################
L2 = []
assert jv("W6-L2-01.z") == "5" and jv("W6-L2-01.fix") == "11,20"
L2.append(task("W6-L2-01", "P6: Eins zu weit", 1, "Fehler im Java-Code", ["P6"],
    [falle("P6"), T("`maximum({4, 11, 7})` bricht mit einer ArrayIndexOutOfBoundsException ab."), C(C201),
     T("Teil 1: Markiere die Zeile, in der die **Ursache** steht. Teil 2: Korrigiere: `i [[op]] r.length`")],
    [lines(2, 1), gaps({"op": TX("code", 3)})],
    [{"zeilen": [4]}, {"op": ["<"]}],
    [T("Der Absturz passiert in Zeile %s (`r[i]` mit i = 3), die Ursache ist die Schleifenbedingung in Zeile 4: Der letzte gültige Index ist `r.length - 1`." % jv("W6-L2-01.z")),
     T("Mit `i < r.length`: maximum({4, 11, 7}) = 11, maximum({20}) = 20."),
     H("P6: Grenzen prüfen – `<` statt `<=`, Start bei 0 oder 1, `getLength() - 1`.")]))

assert jv("W6-L2-02.erg") == "-1"
L2.append(task("W6-L2-02", "P6: Die binäre Suche nach Truhe 50", 1, "Sortieren und Suchen", ["P6"],
    [falle("P6"), T("Klicke nacheinander die Indizes an, die `binaer(r, %d)` als `mid` untersucht." % X202), REIH(R202), C(C202)],
    array_klick(R202), {"folge": [int(x) for x in jv("W6-L2-02.mids").split()]},
    [T("lo = 0, hi = 10 → mid = 5 (26 < 50) → lo = 6; mid = 8 (47 < 50) → lo = 9; mid = 9 (52 > 50) → hi = 8; lo > hi → −1."),
     H("P6: `lo = mid + 1` bzw. `hi = mid - 1` – mit `lo = mid` entstünde bei lo = hi − 1 eine Endlosschleife.")]))

rows = tab_rows("W6-L2-03.tab")
blk, fel, loe = gtab(["Rekursionstiefe", "n", "Rückgabe"], rows, {0: "zahl", 1: "zahl", 2: "zahl"}, "z")
L2.append(task("W6-L2-03", "P7: Die Zerlegung der Zauberzahl", 3, "Rekursionstabelle", ["P7", "P8"],
    [falle("P7", "P8"), T("Dokumentiere `zerlege(50)` in der Rekursionstabelle. Der Erstaufruf hat die Rekursionstiefe 0."), C(C203), blk,
     T("Wie viele Aufrufe erzeugt `zerlege(500)`? [[a]] · Ergebnis von `zerlege(500)`: [[e]]")],
    gaps(dict(fel, a=Z(), e=Z())), dict(loe, a=[str(len(tab_rows("W6-L2-03.tab500")))], e=[jv("W6-L2-03.e500")]),
    [T("50 → 16 → 5 → 1 (ganzzahlige Division durch 3). Rückgaben von innen nach außen: 1, 1 + 5 % 3 = 3, 3 + 16 % 3 = 4, 4 + 50 % 3 = **6**."),
     T("zerlege bildet die Quersumme in der Dreierdarstellung (50 = 1212₃). 500 → 166 → 55 → 18 → 6 → 2: **%d Aufrufe**, Ergebnis %s." % (
         len(tab_rows("W6-L2-03.tab500")), jv("W6-L2-03.e500"))),
     H("P7: Erstaufruf = Tiefe 0. P8: Jede Zeile vollständig – auch die Rückgabe des Basisfalls.")]))

assert jv("W6-L2-04.bug") == "1" and jv("W6-L2-04.fix0") == "3,0"
L2.append(task("W6-L2-04", "P7: Das vergessene Ergebnis", 2, "Fehler im Java-Code", ["P7"],
    [falle("P7"), T("`zaehleGerade({4, 7, 2, 8, 5}, 0)` soll 3 liefern, liefert aber %s." % jv("W6-L2-04.bug")), C(C204),
     T("Teil 1: Markiere die **zwei** fehlerhaften Zeilen. Teil 2: Korrigiere: Zeile 8 `return [[a]];` und Zeile 10 `return [[b]];`")],
    [lines(2, 2), gaps({"a": TX("code", 10), "b": TX("code", 8)})],
    [{"zeilen": [8, 10]}, {"a": ["rest+1", "1+rest"], "b": ["rest"]}],
    [T("Das Ergebnis des rekursiven Aufrufs (`rest`) wird berechnet, aber nie verwendet – zurückgegeben wird nur, ob r[0] gerade ist."),
     T("Korrigiert: `return rest + 1;` bzw. `return rest;` → %s (leere Reihung: %s)." % tuple(jv("W6-L2-04.fix0").split(","))),
     H("P7: Rekursive Aufrufe liefern Teilergebnisse – sie müssen in die eigene Rückgabe eingehen.")]))

rows = tab_rows("W6-L2-05.tab")
rows = [["vor der Schleife"] + rows[0][1:]] + rows[1:-1] + [["Ende: " + rows[-1][0]] + rows[-1][1:]]
blk, fel, loe = gtab(["i", "r[i]", "max", "anzahl"], rows, {2: "zahl", 3: "zahl"}, "z", fest=(0,))
fel["ie"] = Z(4); loe["ie"] = [tab_rows("W6-L2-05.tab")[-1][0]]
blk["zeilen"][-1][0] = "Ende: i = [[ie]]"
for i in range(1, len(rows) - 1):
    fid = "z%db" % (i + 1); blk["zeilen"][i][1] = "[[%s]]" % fid; fel[fid] = Z(4); loe[fid] = [rows[i][1]]
L2.append(task("W6-L2-05", "P8: Das Protokoll des Schatzmeisters", 2, "Tracetabelle", ["P8"],
    [falle("P8"), T("Dokumentiere den Ablauf: eine Zeile vor der Schleife, eine Zeile je Schleifendurchlauf (Werte **am Ende** des Durchlaufs) und eine Zeile mit den Endwerten."),
     C(C205), blk],
    gaps(fel), loe,
    [T("max und anzahl werden nur geändert, wenn ein größerer bzw. gleich großer Wert kommt: Bei der zweiten 9 (i = 3) wird anzahl 2. "
       "Nach der Schleife ist i = %s – die Schleife bricht ab, weil i < r.length falsch ist. Ergebnis: max = 9, anzahl = 2." % loe["ie"][0]),
     H("P8: Vorgegebene Spalten vollständig, jede Wertänderung, und die **Endwerte** (auch der Zähler hat einen Endwert!).")]))

STR206 = STR("summeGerade(r: Reihung von Ganzzahl): Ganzzahl", [
    {"anw": "summe = 0"},
    {"zaehle": "für i von 0 bis r.length", "rumpf": [
        {"wenn": "r[i] % 2 == 0", "dann": [{"anw": "summe += r[i];"}], "sonst": []}]},
    {"anw": "return summe;"}])
OPT206 = [("a", "Zuweisung mit `=` statt `←`", True), ("b", "Zählschleife bis `r.length` statt bis `r.length − 1`", True),
          ("c", "Java-Operatoren in der Bedingung bzw. Anweisung (`%`, `==`, `+=`, `;`) statt `mod`, `=`, `←`", True),
          ("d", "`return summe;` statt „gib summe zurück“", True), ("e", "Die Verzweigung bräuchte einen Sonst-Zweig mit Inhalt", False),
          ("f", "Der Kopf dürfte keinen Rückgabetyp enthalten", False)]
txt206 = " ".join(s for b in [STR206] for s in [json.dumps(b, ensure_ascii=False)])
assert "summe = 0" in txt206 and "bis r.length\"" in txt206 and "%" in txt206 and "return summe;" in txt206
L2.append(task("W6-L2-06", "P9: Notations-Polizei", 1, "Fehler im Struktogramm", ["P9", "P6"],
    [falle("P9", "P6"), T("Inhaltlich soll das Struktogramm die Summe der geraden Werte liefern. Welche Mängel würden im Abitur Punkte kosten?"), STR206],
    choice([(i, m) for i, m, r in OPT206], mehrfach=True), {"richtig": [i for i, m, r in OPT206 if r]},
    [T("Richtig nach EH §5: „summe ← 0“, „für i von 0 bis r.length − 1“, Bedingung „r[i] mod 2 = 0“, „summe ← summe + r[i]“, „gib summe zurück“."),
     T("Ein leerer Sonst-Zweig ist erlaubt, und der Kopf enthält die vollständige Signatur mit Rückgabetyp.")]))

L207 = {"a": ["0"], "b": ["r.length − 1", "r.length - 1", "r.length−1", "r.length-1", "Länge(r) − 1", "Länge(r) - 1", "länge(r)-1", "länge(r)−1"],
        "c": ["anzahl + 1", "anzahl+1", "1 + anzahl"], "d": ["anzahl"]}
assert jv("W6-L2-07.t") == "2"
L2.append(task("W6-L2-07", "P9: Vom Code zum Struktogramm", 2, "Code ↔ Struktogramm", ["P9", "P6"],
    [falle("P9", "P6"), T("Übersetze die Methode in ein Struktogramm nach EH §5 – ergänze die Lücken (keine Java-Syntax!)."), C(C207),
     STR("anzahlUeber(r: Reihung von Ganzzahl, grenze: Ganzzahl): Ganzzahl", [
         {"anw": "anzahl ← [[a]]"},
         {"zaehle": "für i von 0 bis [[b]]", "rumpf": [{"wenn": "r[i] > grenze", "dann": [{"anw": "anzahl ← [[c]]"}], "sonst": []}]},
         {"gib": "[[d]]"}])],
    gaps({"a": TX("text", 4), "b": TX("text", 14), "c": TX("text", 12), "d": TX("text", 8)}), L207,
    [T("`i < r.length` heißt in der Zählschleife „für i von 0 bis r.length − 1“ (P6). `anzahl++` wird zu „anzahl ← anzahl + 1“, `return` zu „gib anzahl zurück“ (P9)."),
     H("Im Struktogramm keine `;`, kein `++`, kein `==` – Zuweisung immer mit ←.")]))

L2.append(task("W6-L2-08", "P10: Behaupten ist nicht begründen", 2, "Funktionsweise erläutern", ["P10"],
    [falle("P10"), T("Aufgabe im Abi-Stil: „**Begründen** Sie, dass für die Rückgängig-Funktion des Level-Editors ein Stapel geeignet ist.“ [2 BE] – Welche Antwort erhält die volle Punktzahl?")],
    choice([("a", "Ein Stapel arbeitet nach dem LIFO-Prinzip."),
            ("b", "Weil man beim Stapel nur oben etwas ablegen und wegnehmen kann, ist er besser als eine Schlange."),
            ("c", "Rückgängig gemacht wird immer die **zuletzt** ausgeführte Änderung. Jede Änderung wird mit push oben abgelegt; pop liefert genau die jüngste – nach dem LIFO-Prinzip. "
                  "Wiederholtes Rückgängigmachen geht so Schritt für Schritt in umgekehrter Reihenfolge zurück; beliebigen Zugriff wie bei einer dynamischen Reihung braucht man nicht."),
            ("d", "Stapel sind schneller als dynamische Reihungen.")]),
    {"richtig": ["c"]},
    [T("a) nennt nur das Prinzip – ohne Bezug zur Rückgängig-Funktion (0–1 BE). b) behauptet „besser“ ohne Grund. d) ist eine unbegründete (und so falsche) Behauptung."),
     T("c) verbindet Anforderung (die jüngste Änderung zuerst zurücknehmen) mit der Arbeitsweise (push/pop, LIFO) und grenzt ab – das ist **begründen**."),
     H("P10: „begründen“ = Aussage auf Eigenschaften der Struktur **und** auf den Kontext aus dem Material zurückführen.")]))

level("W6-L2", "6.2", "Fallenjagd II – P6 bis P10", [38], "AB 1 Korrektur und Fehlerjagd, Teil 4 (P6–P10)",
      "– (Papier-Training; Papier-Compiler: AQ_W6_Probeklausur_Papier-Compiler.txt)",
      [T("Zweite Runde der Fehlerjagd: Grenzen, Rekursion, Tabellen, Struktogramme und Operatoren."),
       H("P6 Off-by-one · P7 Rekursion (Basisfall, Ergebnis verwenden, Tiefe 0) · P8 Trace-/Rekursionstabelle vollständig · P9 Struktogramm nach EH §5 · P10 Operator verfehlt")], L2)

# #######################################################################################
#  LEVEL 6.3 – Abi-Mix I (Welt 0–2)
# #######################################################################################
L3 = []
f301, l301, r301 = {}, {}, []
for k, a in AUSDR301:
    w, t = jv("W6-L3-01.%s" % k).split("|")
    r301.append(["`%s`" % a, "[[%s]]" % k])
    f301[k] = AW(["true", "false"]) if t == "boolean" else Z(5)
    l301[k] = [w]
L3.append(task("W6-L3-01", "Welt 0: Ausdrücke am Portal", 1, "Datentypen und Ausdrücke", ["P4"],
    [falle("P4"), T("Es gilt `int x = %d;`. Gib den Wert jedes Ausdrucks an." % X301), TAB(["Ausdruck", "Wert"], r301)],
    gaps(f301), l301,
    [T("\n".join("- `%s` → %s" % (a, jv("W6-L3-01.%s" % k).split("|")[0]) for k, a in AUSDR301)),
     T("14 / 4 = 3 (ganzzahlig), · 4 = 12. Erst `(double) x` macht aus der Division eine Kommazahl-Division: 3.5.")]))

L3.append(task("W6-L3-02", "Welt 1: Zwei Namen, ein Held", 2, "Objektkarten und Referenzen", ["P5"],
    [falle("P5"), T("Held wie in der Heldenschmiede (`Held(name)` setzt leben = 100; `nimmSchaden` und `heilen` verändern leben). Nach dem Code:"), C(C302),
     TAB(["Frage", "Antwort"], [["Wie viele Held-Objekte wurden erzeugt?", "[[n]]"], ["`c.getLeben()`", "[[c]]"], ["`a.getLeben()`", "[[a]]"],
                                ["`a == c`", "[[ac]]"], ["`b == c`", "[[bc]]"], ["`a.getName().equals(c.getName())`", "[[eq]]"],
                                ["Auf welches Objekt zeigt keine Variable mehr? (Name)", "[[weg]]"]])],
    gaps({"n": Z(), "c": Z(), "a": Z(), "ac": AW(["true", "false"]), "bc": AW(["true", "false"]), "eq": AW(["true", "false"]), "weg": TX("text", 6)}),
    {"n": ["3"], "c": [jv("W6-L3-02.c")], "a": [jv("W6-L3-02.a")], "ac": [jv("W6-L3-02.ac")], "bc": [jv("W6-L3-02.bc")], "eq": [jv("W6-L3-02.eq")], "weg": ["Bo"]},
    [T("`new` wird dreimal ausgeführt → 3 Objekte. c zeigt auf die erste Aria (leben 100 − 30 + 10 = 80), ab Zeile 5 auch b. In Zeile 7 bekommt a ein **neues** Objekt (leben 100)."),
     T("`a == c` vergleicht Referenzen → false (zwei verschiedene Objekte), `b == c` → true. Die Namen sind inhaltlich gleich → `equals` liefert true. Das Objekt „Bo“ ist nicht mehr erreichbar."),
     H("P5: `==` prüft Identität (dasselbe Objekt), `equals` den Inhalt – deshalb Zeichenketten immer mit equals.")]))

L3.append(task("W6-L3-03", "Welt 1: Klassendiagramm lesen", 1, "Klassendiagramm", ["P10"],
    [falle("P10"), T("Ordne jedes Element eines Klassendiagramms nach EH §6 dem richtigen Fachbegriff zu."),
     KK("Held", ["- leben: Ganzzahl", "…"], ["+ c Held(name: Zeichenkette)", "+ getLeben(): Ganzzahl", "+ nimmSchaden(schaden: Ganzzahl): nichts"])],
    match([("e1", "`- leben: Ganzzahl`"), ("e2", "`+ c Held(name: Zeichenkette)`"), ("e3", "`+ getLeben(): Ganzzahl`"),
           ("e4", "`+ nimmSchaden(schaden: Ganzzahl): nichts`"), ("e5", "Linie mit hohler Dreiecksspitze von Waffe zu Gegenstand"),
           ("e6", "einfache, unbeschriftete Linie zwischen Held und Waffe")],
          [("k1", "privates Attribut"), ("k2", "Konstruktor"), ("k3", "Methode mit Rückgabe (Anfrage)"), ("k4", "Methode ohne Rückgabe (Auftrag)"),
           ("k5", "Vererbung"), ("k6", "Assoziation")]),
    {"e1": "k1", "e2": "k2", "e3": "k3", "e4": "k4", "e5": "k5", "e6": "k6"},
    [T("`-` = privat, `+` = öffentlich, `c` kennzeichnet den Konstruktor. „nichts“ als Rückgabetyp = Auftrag (void). Vererbung: hohle Dreiecksspitze zur Oberklasse; "
       "Assoziation: einfache Linie ohne Kardinalitäten."),
     H("P10: In Erläuterungen die Fachbegriffe verwenden (Attribut, Konstruktor, Sichtbarkeit, Vererbung) – nicht „das Ding mit dem c“.")]))

s304 = jv("W6-L3-04.sel").split("|")
tausch304 = [list(map(int, p.split(","))) for p in s304[0].strip("[]").split("][")]
L3.append(task("W6-L3-04", "Welt 2: Selectionsort in der Rangliste", 2, "Sortieren und Suchen", ["P6"],
    [falle("P6"), T("Sortiere **aufsteigend** mit Selectionsort: Für i von 0 bis n − 2 wird das Minimum von r[i] … r[n − 1] gesucht und mit r[i] getauscht – "
       "aber nur, wenn es nicht schon an Position i steht. Führe alle Tausche aus und klicke dann auf „fertig“.")],
    array_tausch(START304, fertigKnopf=True), {"tausche": tausch304},
    [T("i = 0: Minimum 8 (Index 3) → tausche 0 und 3. i = 1: Minimum 14 steht schon richtig → kein Tausch. i = 2: Minimum 21 (Index 4) → tausche 2 und 4. "
       "i = 3: 29 steht richtig. Ergebnis %s mit %s Vergleichen (= 5 · 4 / 2)." % (s304[2], s304[1])),
     H("P6: Die äußere Schleife läuft nur bis n − 2, die innere Suche beginnt bei i + 1.")]))

s305 = jv("W6-L3-05.ins").split("|")
tausch305 = [list(map(int, p.split(","))) for p in s305[0].strip("[]").split("][")]
L3.append(task("W6-L3-05", "Welt 2: Insertionsort mit Nachbartauschen", 2, "Sortieren und Suchen", ["P6"],
    [falle("P6"), T("Sortiere **aufsteigend** mit Insertionsort: Für i von 1 bis n − 1 wandert r[i] durch **Tausche benachbarter Elemente** nach links, "
       "solange sein linker Nachbar größer ist. Führe alle Tausche in der richtigen Reihenfolge aus.")],
    array_tausch(START305, fertigKnopf=True), {"tausche": tausch305},
    [T("i = 1: 2 < 5 → (0,1). i = 2: 8 bleibt. i = 3: 1 wandert dreimal: (2,3), (1,2), (0,1). i = 4: 6 < 8 → (3,4), dann 6 > 5 – Stopp. Ergebnis %s." % s305[1]),
     H("P6: Die Schleife beginnt bei i = 1 (ein einzelnes Element ist schon sortiert) und muss bei j = 0 stoppen.")]))

L3.append(task("W6-L3-06", "Welt 2: Verdopplung abschätzen", 2, "Effizienz", ["P10"],
    [falle("P10"), T("Selectionsort braucht bei n Werten n(n − 1)/2 Vergleiche. Die binäre Suche braucht höchstens ⌊log₂ n⌋ + 1 Schleifendurchläufe.\n\n"
       "- Vergleiche bei n = 10: [[v10]] · bei n = 20: [[v20]]\n- Durchläufe der binären Suche höchstens bei n = 1000: [[b1000]] · bei n = 2000: [[b2000]]"),
     T("Welche Abschätzung ist richtig begründet?")],
    [gaps({"v10": Z(), "v20": Z(), "b1000": Z(), "b2000": Z()}),
     choice([("a", "Verdoppelt sich n, vervierfacht sich ungefähr die Zahl der Vergleiche von Selectionsort (n² wächst mit 2² = 4), die binäre Suche braucht nur einen Durchlauf mehr, weil sich der Suchbereich je Durchlauf halbiert."),
             ("b", "Beide Verfahren brauchen bei doppeltem n doppelt so viele Schritte."),
             ("c", "Selectionsort braucht doppelt so viele, die binäre Suche gleich viele Schritte."),
             ("d", "Man kann das ohne O-Notation nicht abschätzen.")])],
    [{"v10": [jv("W6-L3-06.v10")], "v20": [jv("W6-L3-06.v20")], "b1000": [jv("W6-L3-06.b1000")], "b2000": [jv("W6-L3-06.b2000")]}, {"richtig": ["a"]}],
    [T("10 · 9 / 2 = 45, 20 · 19 / 2 = 190 ≈ 4 · 45. Binäre Suche: 2⁹ = 512 ≤ 1000 < 1024 → 10 Durchläufe, 2000 → 11 (per Java für alle Suchwerte nachgezählt)."),
     H("P10: Im Abitur wird Effizienz durch **Zählen** und **Verdopplung** beurteilt – mit Begründung, nicht als bloße Zahl.")]))

t307 = jv("W6-L3-07.tab").split("=")
rows = [r.split("|") for r in t307[0].strip(";").split(";")]
blk, fel, loe = gtab(["lo", "hi", "mid", "r[mid]"], rows, {0: "zahl", 1: "zahl", 2: "zahl", 3: "zahl"}, "z")
L3.append(task("W6-L3-07", "Welt 2: Trace der binären Suche", 3, "Tracetabelle", ["P8", "P6"],
    [falle("P8", "P6"), T("Dokumentiere `binaer(r, %d)`: eine Zeile je Schleifendurchlauf mit den Werten von lo, hi, mid und r[mid] **zu Beginn der Prüfung**. "
       "Gib danach die Rückgabe an: [[erg]]" % X307), REIH(R307), C(C202), blk],
    gaps(dict(fel, erg=Z())), dict(loe, erg=[t307[1]]),
    [T("; ".join("lo = %s, hi = %s → mid = %s (r[mid] = %s)" % tuple(r) for r in rows) + " → gefunden, Rückgabe **%s**. Bei r[mid] < x wird lo = mid + 1, sonst hi = mid − 1." % t307[1]),
     H("P8: mid ganzzahlig berechnen; jede Zeile vollständig ausfüllen.")]))

L3.append(task("W6-L3-08", "Welt 1: Klasse oder Objekt?", 1, "Klasse vs. Objekt", ["P10"],
    [falle("P10"), T("Welche Aussagen sind fachlich richtig?")],
    choice([("a", "Ein Objekt ist ein Exemplar einer Klasse mit eigenen Attributwerten."),
            ("b", "Der Konstruktor erzeugt ein Objekt und belegt seine Attribute mit Anfangswerten."),
            ("c", "Von einer Klasse kann es nur ein Objekt geben."),
            ("d", "Private Attribute sind nur innerhalb der Klasse zugreifbar; von außen greift man über öffentliche Methoden zu (Kapselung)."),
            ("e", "Zwei Variablen, die auf dasselbe Objekt zeigen, bedeuten zwei Objekte.")], mehrfach=True),
    {"richtig": ["a", "b", "d"]},
    [T("Eine Klasse ist der Bauplan, beliebig viele Objekte können nach ihr erzeugt werden. Zwei Referenzen auf dasselbe Objekt sind **ein** Objekt (siehe „Zwei Namen, ein Held“)."),
     H("P10: „erläutern“ heißt, diese Begriffe am Material zu zeigen – z. B. welcher Konstruktor welche Attribute setzt.")]))

level("W6-L3", "6.3", "Abi-Mix I – Welten 0 bis 2", [39], "AB 1 Korrektur und Fehlerjagd, Teil 5 (Abi-Fahrplan) · Kata W6-11/W6-12",
      "– (Wiederholung Welten 0–2)",
      [T("Abitur-Klassiker aus Portal, Heldenschmiede und Rangliste – jede Aufgabe mit der Falle, die dort typischerweise Punkte kostet."),
       H("Abi-Check: Signatur · Leer?/Index? · Cast · equals · return auf jedem Pfad · Struktur unverändert · Struktogramm ohne Java · Operator erfüllt")], L3)

# #######################################################################################
#  LEVEL 6.4 – Abi-Mix II (Welt 3–5)
# #######################################################################################
L4 = []
rows = tab_rows("W6-L4-01.tab")
blk, fel, loe = gtab(["Rekursionstiefe", "lo", "hi", "mid", "Rückgabe"], rows, {0: "zahl", 1: "zahl", 2: "zahl", 3: "zahl", 4: "zahl"}, "z", fest=(0,))
blk["zeilen"][0][4] = "[[r0]]"; fel["r0"] = Z(4); loe["r0"] = [rows[0][4]]
L4.append(task("W6-L4-01", "Welt 3: Rekursive binäre Suche", 2, "Rekursionstabelle", ["P7", "P8"],
    [falle("P7", "P8"), T("Dokumentiere `binaerRek(r, %d, 0, 7)` in der Rekursionstabelle (bei lo > hi bleibt mid „–“)." % X401), REIH(R401), C(C401), blk],
    gaps(fel), loe,
    [T("(0, 7, mid 3): 13 > 10 → links. (0, 2, mid 1): 5 < 10 → rechts. (2, 2, mid 2): 9 < 10 → rechts. (3, 2): lo > hi → −1. Die −1 wird unverändert nach außen gereicht."),
     H("P7: Erstaufruf Tiefe 0, auch der Basisfall-Aufruf bekommt eine Zeile.")]))

RAST402 = [[0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0]]
def flut(R, z, s):
    seen, st = set(), [(z, s)]
    while st:
        a, b = st.pop()
        if not (0 <= a < len(R) and 0 <= b < len(R[0])) or R[a][b] == 1 or (a, b) in seen: continue
        seen.add((a, b)); st += [(a - 1, b), (a, b + 1), (a + 1, b), (a, b - 1)]
    return sorted(seen)
F402 = flut(RAST402, 0, 0)
L4.append(task("W6-L4-02", "Welt 3: Nebel lüften", 1, "Funktionsweise erläutern", ["P1"],
    [falle("P1"), T("Die Dungeon-Karte ist eine 2D-Reihung [Zeile][Spalte]: 0 = frei, 1 = Wand. Der rekursive Flood-Fill startet bei [0][0] und lüftet alle freien Felder, "
       "die über die 4er-Nachbarschaft (oben, rechts, unten, links) erreichbar sind. Markiere alle gelüfteten Felder."), RAST(RAST402)],
    grid(RAST402), {"zellen": [list(c) for c in F402], "reihenfolge": False},
    [T("Erreichbar sind %d freie Felder – auch über den Umweg durch Zeile 0 bis in Spalte 5 und über [3][0] nach unten links. Nicht erreichbar: %s – "
       "die Wände [3][1] bis [3][5] und [4][2] schneiden sie ab, diagonal geht es nicht weiter." % (len(F402), ", ".join("[%d][%d]" % (z, s) for z in range(len(RAST402)) for s in range(len(RAST402[0]))
                                                                                    if RAST402[z][s] == 0 and (z, s) not in F402))),
     H("P1: Vor jedem Zugriff `karte[z][s]` prüfen, ob 0 ≤ z < Zeilenzahl und 0 ≤ s < Spaltenzahl – sonst stürzt der Flood-Fill am Rand ab.")]))

L4.append(task("W6-L4-03", "Welt 4: Stapel und Schlange im Wechsel", 2, "ADT-Befehlsfolgen", ["P8"],
    [falle("P8"), T("q ist eine Schlange vom Inhaltstyp Ganzzahl mit (vorn → hinten) 3, 7, 1, 9; s ist ein leerer Stapel. Danach wird ausgeführt:"),
     ADT("schlange", START403), C(C403),
     T("Teil 1: Inhalt von s (unten → oben). Teil 2: Inhalt von q (vorn → hinten).")],
    [adtsim("stapel", []), adtsim("schlange", START403)],
    [{"inhalt": jv("W6-L4-03.s").split(",")}, {"inhalt": jv("W6-L4-03.q").split(",")}],
    [T("1: s = 3; q = 7 1 9 · 2: q = 7 1 9 3 (top lässt die 3 im Stapel) · 3: s = 3 7; q = 1 9 3 · 4: q = 1 9 3 7; s = 3 · 5: s = 3 1; q = 9 3 7 · "
       "6: `head` entnimmt nicht → s = 3 1 9, q = 9 3 7."),
     H("P8: Nach jedem Befehl den Zustand notieren; `top`/`head` lesen nur, `pop`/`dequeue` entnehmen.")]))

L4.append(task("W6-L4-04", "Welt 4: Das Inventar als dynamische Reihung", 1, "ADT-Befehlsfolgen", ["P6"],
    [falle("P6"), T("Gib den Inhalt von d nach allen Befehlen an (Index 0 zuerst)."), C(C404)],
    adtsim("dynarray", []), {"inhalt": jv("W6-L4-04.d").split(",")},
    [T("Axt, Bogen → insertAt(1) schiebt Bogen nach rechts: Axt, Dolch, Bogen → + Elixier → delete(0): Dolch, Bogen, Elixier → setItem(1) ersetzt Bogen: "
       "Dolch, Fackel, Elixier → insertAt(3, …) mit 3 = getLength() hängt an: **%s**." % jv("W6-L4-04.d").replace(",", ", ")),
     H("P6: Nach insertAt und delete verschieben sich die Indizes der folgenden Elemente.")]))

assert jv("W6-L4-05.z") == "2" and jv("W6-L4-05.fix") == "false,true,false"
L4.append(task("W6-L4-05", "Welt 5: Suche ohne Boden", 2, "Fehler im Java-Code", ["P1", "P7"],
    [falle("P1", "P7"), T("Die Suche im binären Suchbaum funktioniert, solange x vorkommt. `suche(20(10,30), 25)` stürzt ab."), C(C405),
     T("Teil 1: Markiere die Zeile mit dem Laufzeitfehler. Teil 2: Ergänze den fehlenden Basisfall am Anfang der Methode: `if ([[a]]) { return [[b]]; }`")],
    [lines(2, 1), gaps({"a": TX("code", 14), "b": TX("code", 6)})],
    [{"zeilen": [2]}, {"a": ["b.isEmpty()"], "b": ["false"]}],
    [T("Bei 25 geht die Suche 20 → rechts → 30 → links in den **leeren** Teilbaum; dort ruft Zeile 2 `getItem()` auf → IllegalStateException."),
     T("Mit dem Basisfall `if (b.isEmpty()) { return false; }`: 25 → false, 10 → true, leerer Baum → false."),
     H("P1 + P7: Der Basisfall „leerer Baum“ steht in jeder rekursiven Baummethode ganz oben.")]))

z406 = jv("W6-L4-06.z").split("|"); assert "!" not in z406[0]
tausch406 = [list(map(int, p.split(","))) for p in z406[0].strip("[]").split("][")]
L4.append(task("W6-L4-06", "Welt 3: Quicksort zerlegt", 3, "Sortieren und Suchen", ["P6"],
    [falle("P6"), T("Führe `zerlege(r, 0, 6)` aus: Pivot = r[lo]; grenze ← lo; für i von lo + 1 bis hi: falls r[i] < pivot, dann grenze ← grenze + 1 und tausche r[grenze] und r[i]. "
       "Zum Schluss tausche r[lo] und r[grenze]. Führe genau diese Tausche aus.")],
    array_tausch(START406), {"tausche": tausch406},
    [T("Pivot 6. Kleinere Werte 2, 1, 4 wandern nacheinander an die Positionen 1, 2, 3: Tausche %s. Zum Schluss kommt das Pivot an Position grenze = %s: %s." % (
        ", ".join("(%d,%d)" % tuple(p) for p in tausch406[:-1]), z406[2], z406[1])),
     H("P6: Die Schleife beginnt bei lo + 1 und läuft **bis einschließlich** hi.")]))

assert jv("W6-L4-07.s") == "15" and jv("W6-L4-07.q") == "4,9,2"
L4.append(task("W6-L4-07", "Welt 4: Schlange unverändert – als Struktogramm", 2, "Code ↔ Struktogramm", ["P2", "P9"],
    [falle("P2", "P9"), T("Ergänze das Struktogramm zur Methode `summe`, die die Schlange q unverändert zurücklässt."), C(C407),
     STR("summe(q: Schlange vom Inhaltstyp Ganzzahl): Ganzzahl", [
         {"anw": "s ← 0"}, {"anw": "hilf ← erzeuge Schlange()"},
         {"solange": "nicht q.isEmpty()", "rumpf": [{"anw": "x ← q.dequeue()"}, {"anw": "s ← s + x"}, {"aufruf": "[[a]]"}]},
         {"solange": "[[b]]", "rumpf": [{"aufruf": "[[c]]"}]},
         {"gib": "s"}])],
    gaps({"a": TX("code", 16), "b": TX("code", 22), "c": TX("code", 24)}),
    {"a": ["hilf.enqueue(x)"], "b": ["nicht hilf.isEmpty()", "nicht(hilf.isEmpty())"], "c": ["q.enqueue(hilf.dequeue())"]},
    [T("Jedes entnommene Element kommt in die Hilfsschlange; danach wandert alles in derselben Reihenfolge zurück nach q (Java-Test: Summe 15, q danach 4, 9, 2)."),
     H("P9: „nicht“ statt `!`, kein Semikolon. P2: Ohne die zweite Schleife wäre q am Ende leer.")]))

L4.append(task("W6-L4-08", "Welten 4–5: Die richtige Struktur", 1, "Funktionsweise erläutern", ["P10"],
    [falle("P10"), T("Ordne jedem Spielmodul die **geeignetste** Datenstruktur zu.")],
    match([("e1", "Rückgängig-Funktion im Level-Editor"), ("e2", "Warteschlange am Händlerstand: Wer zuerst kommt, wird zuerst bedient"),
           ("e3", "Inventar, in dem man direkt auf den dritten Gegenstand zugreift"), ("e4", "Klammerprüfung eines Zauberspruchs"),
           ("e5", "Gegner ebenenweise durchlaufen (Levelorder)"), ("e6", "Items blitzschnell nach ihrer Nummer finden")],
          [("k1", "Stapel"), ("k2", "Schlange"), ("k3", "dynamische Reihung"), ("k4", "binärer Suchbaum")]),
    {"e1": "k1", "e2": "k2", "e3": "k3", "e4": "k1", "e5": "k2", "e6": "k4"},
    [T("LIFO (zuletzt hinein, zuerst heraus): Rückgängig, Klammerprüfung → Stapel. FIFO: Warteschlange, Levelorder → Schlange. "
       "Zugriff über den Index → dynamische Reihung. Suche nach Schlüssel mit wenigen Vergleichen → binärer Suchbaum (ausgeglichen)."),
     H("P10: Beim „beurteilen“ das Kriterium nennen (Zugriffsart, Reihenfolge, Aufwand) und auf das Spielmodul beziehen.")]))

level("W6-L4", "6.4", "Abi-Mix II – Welten 3 bis 5", [39, 40], "AB 1 Korrektur und Fehlerjagd, Teil 5 (Abi-Fahrplan) · Kata W6-13/W6-14",
      "– (Wiederholung Welten 3–5)",
      [T("Rekursion, 2D-Reihungen, Stapel/Schlange/DynArray und Bäume – die Klassiker der zweiten Hälfte, jeweils mit ihrer typischen Falle."),
       H("Zeitplan im Abitur: ≈ 2,5 Minuten je BE. Erst Methodenkopf, dann Leer-/Indexabfragen, dann der Rest.")], L4)

# #######################################################################################
#  BOSS-POOL Welt 6 – „Generalprobe online“
# #######################################################################################
B = []
assert jv("W6-B-01.z") == "3" and jv("W6-B-01.eins") == "[]"
B.append(task("W6-B-01", "P1: Die Gegnerwelle", 1, "Fehler im Java-Code", ["P1"],
    [T("Die Gegnerwelle ist eine Schlange vom Inhaltstyp Zeichenkette."), C(CB01), T("Markiere die Zeile, in der bei leerer Welle der Laufzeitfehler entsteht.")],
    lines(1, 1), {"zeilen": [3]},
    [T("`dequeue()` auf der leeren Schlange (Zeile 3) → IllegalStateException – die Abfrage danach kommt zu spät. Zusätzlich falsch: Bei genau einem Gegner liefert die Methode \"\" "
       "(Java-Test: %s), weil nach dem Entnehmen geprüft wird. Richtig: erst `if (welle.isEmpty()) return \"\";`, dann entnehmen (P1)." % jv("W6-B-01.eins"))]))
fb02, lb02, rb02 = {}, {}, []
for k, a in AUSDRB02:
    w, t = jv("W6-B-02.%s" % k).split("|"); rb02.append(["`%s`" % a, "[[w%s]]" % k, "[[t%s]]" % k])
    fb02["w" + k] = Z(5); lb02["w" + k] = [w]; fb02["t" + k] = AW(["int", "double", "String", "char", "boolean"]); lb02["t" + k] = [t]
B.append(task("W6-B-02", "P4: Rechnen im Drachenhort", 1, "Datentypen und Ausdrücke", ["P4"],
    [T("Gib Wert und Typ an."), TAB(["Ausdruck", "Wert", "Typ"], rb02)], gaps(fb02), lb02,
    [T("11 / 4 = 2 (ganzzahlig), 11 % 4 = 3 (Rest), 11 / 4.0 = 2.75 (Kommazahl, weil ein Operand double ist) – P4.")]))
B.append(task("W6-B-03", "P5: Wer heißt hier Smaug?", 1, "Fehler im Java-Code", ["P5"],
    [T("`name` und `gesucht` sind Zeichenketten. Welche Bedingungen prüfen im Sinne des Abiturs korrekt, ob beide **inhaltlich** gleich sind?")],
    choice([("a", "`name.equals(gesucht)`"), ("b", "`name == gesucht`"), ("c", "`gesucht.equals(name)`"), ("d", "`name.compareTo(gesucht) == 0`"),
            ("e", "`name.toUpperCase().equals(gesucht.toUpperCase())`")], mehrfach=True),
    {"richtig": ["a", "c", "d"]},
    [T("`equals` (in beide Richtungen) und `compareTo(…) == 0` vergleichen den Inhalt und sind erlaubte Operationen. `==` vergleicht Referenzen (P5), `toUpperCase` ist nicht erlaubt.")]))
L_b04 = [int(x) for x in jv("W6-B-04.mids").split()]
B.append(task("W6-B-04", "P6: Binäre Suche nach der 6", 1, "Sortieren und Suchen", ["P6"],
    [T("Klicke die Indizes an, die die binäre Suche (mid = (lo + hi) / 2, lo = mid + 1 bzw. hi = mid − 1) nach %d als mid untersucht." % XB04), REIH(RB04)],
    array_klick(RB04), {"folge": L_b04},
    [T("lo = 0, hi = 8 → mid 4 (19 > 6) → hi = 3 → mid 1 (6) gefunden. Index %s." % jv("W6-B-04.erg"))]))
fb05, lb05, inh05 = {}, {}, [T("Übersetze die Signaturen in Java-Methodenköpfe (`public static`).")]
for sig, fl in SIGB05:
    name = sig.split("(")[0]
    if len(fl) == 3: kopf = "public static [[%s]] %s([[%s]] b, [[%s]] grenze)" % (fl[0][0], name, fl[1][0], fl[2][0])
    else: kopf = "public static [[%s]] %s([[%s]] d)" % (fl[0][0], name, fl[1][0])
    inh05.append(T("`%s`\n\n%s" % (sig, kopf)))
    for k, v in fl: fb05[k] = TX("code", 9); lb05[k] = [v]
assert jv("W6-B-05.ok") == "kompiliert"
B.append(task("W6-B-05", "P3: Köpfe mit Bibliotheksklassen", 1, "Methodenkopf und Signatur", ["P3"], inh05, gaps(fb05), lb05,
    [T("BinTree vom Inhaltstyp Ganzzahl → `BinTree` (nicht generisch), dynamische Reihung → `DynArray`, Rückgabe Truhe → Klassenname `Truhe` (P3). Beide Köpfe mit javac geprüft.")]))
B.append(task("W6-B-06", "P2 + P6: Der verlorene Schatz", 2, "ADT-Befehlsfolgen", ["P2", "P6"],
    [T("q enthält (vorn → hinten) 12, 40, 7, 25. Gib den Inhalt von q nach `maxGold(q)` an."), ADT("schlange", STARTB06), C(CB06)],
    adtsim("schlange", STARTB06), {"inhalt": jv("W6-B-06.q").split(",")},
    [T("Die Rückgabe 40 stimmt, aber die zweite Schleife läuft nur n − 1 = 3-mal: q = %s – die 25 bleibt in der Hilfsschlange zurück (P6), die Struktur ist zerstört (P2)." % jv("W6-B-06.q").replace(",", ", "))]))
rows = tab_rows("W6-B-07.tab")
blk, fel, loe = gtab(["Rekursionstiefe", "n", "Rückgabe"], rows, {0: "zahl", 1: "zahl", 2: "text"}, "z")
for k in loe:
    if k.endswith("c"):
        v = loe[k][0].strip('"'); loe[k] = ['"%s"' % v] + ([v] if v else ["leer", "(leer)"])
        fel[k] = TX("code", 8)
B.append(task("W6-B-07", "P7: Die Runenkette", 2, "Rekursionstabelle", ["P7", "P8"],
    [T("Dokumentiere `runen(7)` (Rückgaben als Zeichenkette in Anführungszeichen; die leere Zeichenkette als `\"\"`)."), C(CB07), blk],
    gaps(fel), loe,
    [T("7 ist ungerade → \"*\" + runen(6); 6, 4, 2 sind gerade → runen(n − 2) + \"#\"; runen(0) = \"\". Auf dem Rückweg entsteht \"#\", \"##\", \"###\" und schließlich **\"*###\"**.")]))
rows = tab_rows("W6-B-08.tab")
rows = [["vor der Schleife"] + rows[0]] + [[str(i)] + r for i, r in enumerate(rows[1:], 1)]
blk, fel, loe = gtab(["Durchlauf", "n", "s", "k"], rows, {1: "zahl", 2: "zahl", 3: "zahl"}, "z", fest=(0,))
B.append(task("W6-B-08", "P8: Die Quersumme der Schatzkiste", 2, "Tracetabelle", ["P8"],
    [T("Dokumentiere den Ablauf für n = %d (Werte am Ende jedes Durchlaufs)." % NB08),
     C("int n = %d;\nint s = 0;\nint k = 0;\nwhile (n > 0) {\n    s = s + n %% 10;\n    n = n / 10;\n    k = k + 1;\n}" % NB08), blk],
    gaps(fel), loe,
    [T("Jeder Durchlauf trennt die letzte Ziffer ab: 3, 7, 0, 4 → s = 14, k = 4 Ziffern. Auch der Durchlauf mit der Ziffer 0 bekommt eine Zeile (P8).")]))
STRB09 = STR("zaehleLeer(d)", [{"anw": "anzahl := 0"}, {"anw": "i ← 0"},
    {"solange": "i < d.getLength()", "rumpf": [{"wenn": "d.getItem(i).getGold() = 0", "dann": [{"anw": "anzahl++"}], "sonst": []}, {"anw": "i ← i + 1"}]},
    {"gib": "anzahl"}])
B.append(task("W6-B-09", "P9: Struktogramm mit Java-Resten", 2, "Fehler im Struktogramm", ["P9", "P3"],
    [T("Das Struktogramm zählt die leeren Truhen einer dynamischen Reihung vom Inhaltstyp Truhe. Welche Notationsfehler nach EH §5 enthält es?"), STRB09],
    choice([("a", "Der Kopf enthält keine Parameter- und Rückgabetypen."), ("b", "`:=` statt `←` bei der Zuweisung"), ("c", "`anzahl++` ist Java-Syntax"),
            ("d", "Statt „solange“ müsste eine Zählschleife stehen."), ("e", "„gib anzahl zurück“ ist falsch notiert.")], mehrfach=True),
    {"richtig": ["a", "b", "c"]},
    [T("Richtig wäre der Kopf `zaehleLeer(d: dynamische Reihung vom Inhaltstyp Truhe): Ganzzahl`, „anzahl ← 0“ und „anzahl ← anzahl + 1“. "
       "Eine solange-Schleife mit eigenem Zähler ist erlaubt, „gib … zurück“ ist korrekt (P9, P3).")]))
B.append(task("W6-B-10", "P10: Erläutern statt nennen", 2, "Funktionsweise erläutern", ["P10"],
    [T("„**Erläutern** Sie, warum die Suche im binären Suchbaum in jedem Schritt nur einen Teilbaum betreten muss.“ [2 BE] – Welche Antwort erfüllt den Operator?")],
    choice([("a", "Weil der Baum sortiert ist."),
            ("b", "Für jeden Knoten sind alle Werte links kleiner und alle rechts größer. Ist x kleiner als der Wert des Knotens, kann x nur links liegen, sonst nur rechts – der andere Teilbaum "
                  "kann x nicht enthalten. Beispiel: Bei der Suche nach 25 in 20(10,30) wird der Teilbaum mit der 10 nie betreten."),
            ("c", "Weil die Suche rekursiv ist."), ("d", "Suchbäume sind effizient.")]),
    {"richtig": ["b"]},
    [T("Erläutern = nachvollziehbar machen: Ordnungsregel nennen, daraus folgern, warum der andere Teilbaum ausscheidet, mit Beispiel. a), c), d) sind bloße Nennungen (P10).")]))
B.append(task("W6-B-11", "P6: Löschen im Vorwärtslauf", 2, "ADT-Befehlsfolgen", ["P6"],
    [T("d enthält (Index 0 zuerst) die Truhen Eiche:5, Buche:0, Birke:0, Linde:8, Ulme:0 (Name:Gold). Gib den Inhalt von d nach `entferneLeere(d)` an (Schreibweise Name:Gold)."),
     ADT("dynarray", ["%s:%d" % x for x in STARTB11]), C(CB11)],
    adtsim("dynarray", ["%s:%d" % x for x in STARTB11]), {"inhalt": jv("W6-B-11.d").split(",")},
    [T("Nach `delete(1)` rückt Birke auf Index 1 nach – i wird aber auf 2 erhöht, Birke wird übersprungen. Ergebnis: %s. "
       "Abhilfe: rückwärts laufen oder i nur erhöhen, wenn nichts gelöscht wurde (P6)." % jv("W6-B-11.d").replace(",", ", "))]))
vb12 = OCB12.gueltig(J); assert vb12 == [["t1", "t2", "t3", "t4", "t5"]] and all(not o.gueltig(J) for o in OCB12d)
B.append(task("W6-B-12", "P7: Puzzle – rekursiv zählen", 3, "Methode implementieren", ["P7", "P6"],
    [T("Setze `zaehleAb(r: Reihung von Ganzzahl, i: Ganzzahl, x: Ganzzahl): Ganzzahl` zusammen: Wie oft kommt x in r[i] … r[r.length − 1] vor? Rekursiv, ohne Schleife. Drei Teile sind Fallen.")],
    order([(k, TB12[k]) for k in ["t1", "t2", "t3", "t4", "t5", "d1", "d2", "d3"]]), {"reihenfolgen": vb12},
    [C("\n".join(TB12[k] for k in ["t1", "t2", "t3", "t4", "t5"])),
     T("Basisfall `i == r.length` (nicht `r.length - 1`, sonst fehlt das letzte Element – P6). Das Ergebnis des rekursiven Aufrufs wird gespeichert und verwendet (P7); "
       "`return 1;` würde alle weiteren Treffer verwerfen.")]))
rows = tab_rows("W6-B-13.tab")
blk, fel, loe = gtab(["i", "Index des Minimums", "Tausch?", "Reihung danach", "Vergleiche bisher"], rows, {1: "zahl", 2: "auswahl:ja/nein", 3: "liste", 4: "zahl"}, "z")
B.append(task("W6-B-13", "P8: Selectionsort mit Zählwerk", 3, "Tracetabelle", ["P8", "P6"],
    [T("r = {7, 3, 9, 1, 5} wird aufsteigend mit Selectionsort sortiert (Minimum suchen, mit r[i] tauschen, nur wenn nötig; jeder Vergleich r[j] < r[min] zählt). "
       "Fülle je Durchlauf der äußeren Schleife eine Zeile aus (Reihung mit Komma getrennt)."), blk],
    gaps(fel), loe,
    [T("Die innere Suche vergleicht in Durchlauf i genau n − 1 − i Paare: 4 + 3 + 2 + 1 = 10 = 5 · 4 / 2. Getauscht wird nur bei i = 0 und i = 2.")]))
assert jv("W6-B-14.s") == "A,B,C"
B.append(task("W6-B-14", "P2 + P9: Den Stapel heil lassen", 3, "Code ↔ Struktogramm", ["P2", "P9"],
    [T("Ergänze das Struktogramm zur Methode `anzahl`, die einen Stapel zählt und ihn **unverändert** zurücklässt."), C(CB14),
     STR("anzahl(s: Stapel): Ganzzahl", [{"anw": "n ← 0"}, {"anw": "hilf ← erzeuge Stapel()"},
         {"solange": "nicht s.isEmpty()", "rumpf": [{"aufruf": "[[a]]"}, {"anw": "n ← [[b]]"}]},
         {"solange": "[[c]]", "rumpf": [{"aufruf": "[[d]]"}]}, {"gib": "n"}])],
    gaps({"a": TX("code", 18), "b": TX("code", 8), "c": TX("code", 22), "d": TX("code", 18)}),
    {"a": ["hilf.push(s.pop())"], "b": ["n+1", "1+n"], "c": ["nicht hilf.isEmpty()", "nicht(hilf.isEmpty())"], "d": ["s.push(hilf.pop())"]},
    [T("Zweimal Umstapeln stellt die ursprüngliche Reihenfolge wieder her (Java-Test: A, B, C bleibt A, B, C). Notation: ←, „nicht“, keine Semikolons (P9); ohne zweite Schleife wäre s leer (P2).")]))
for i in range(len(LB15)): assert jv("W6-B-15.v%d" % i) == "907,0,12"
B.append(task("W6-B-15", "P4 + P5: Zahlen lesen ohne parseInt", 3, "Lückencode", ["P4", "P5"],
    [T("`zahl(\"907\")` soll 907 liefern – nur mit erlaubten Zeichenketten-Operationen (kein `Integer.parseInt`). Ergänze den Ausdruck."), C(CB15),
     T("Warum darfst du im Abitur nicht `Integer.parseInt(s)` schreiben?")],
    [gaps({"a": TX("code", 26)}),
     choice([("a", "Die Umwandlung gehört nicht zu den in den Ergänzenden Hinweisen erlaubten Zeichenketten-Operationen."),
             ("b", "parseInt gibt es in Java nicht."), ("c", "parseInt liefert eine Kommazahl."), ("d", "parseInt ist zu langsam.")])],
    [{"a": LB15}, {"richtig": ["a"]}],
    [T("Ziffernwert = ASCII-Wert des Zeichens minus ASCII-Wert von '0' (48): `(int) s.charAt(i) - (int) '0'`. Jede Stelle verschiebt die bisherige Zahl um eine Zehnerstelle (z · 10). "
       "Alle akzeptierten Schreibweisen liefern im Test 907, 0 und 12 (P4: char ↔ int)."),
     T("Erlaubt sind nur length, charAt, substring, +, equals, contains, compareTo und (int)/(char) – P5.")]))

welt6 = {"version": 2, "welt": 6, "titel": "Der Endgegner", "farbe": "#7A1F2B", "levels": LEVELS,
         "boss": {"id": "W6-BOSS", "titel": "Generalprobe online", "dauerMin": 30, "anzahl": 8, "mix": {"1": 3, "2": 3, "3": 2},
                  "pool": [t["id"] for t in B]},
         "aufgaben": AUFG + B}

ZUSATZ = {
 "W6-B-04": "P6: `lo = mid + 1` bzw. `hi = mid - 1` – sonst Endlosschleife oder übersprungene Werte.",
 "W6-B-07": "P7: Erstaufruf Tiefe 0, Rückgaben entstehen von innen nach außen. P8: Auch der Basisfall mit \"\" bekommt eine Zeile.",
 "W6-B-13": "P8: Je Durchlauf alle Spalten ausfüllen, auch wenn nicht getauscht wird. P6: Die innere Suche beginnt bei i + 1, die äußere endet bei n − 2.",
}
for a in AUFG + B:
    if a["id"] in ZUSATZ: a["erklaerung"].append(H(ZUSATZ[a["id"]]))
str_loesungen(welt6["aufgaben"])
json.dump(welt6, open(SCRATCH + "/algolab/content/welt6.json", "w"), ensure_ascii=False, indent=1)
print("welt6.json:", len(LEVELS), "Level,", len(AUFG), "Level-Aufgaben,", len(B), "Boss-Aufgaben")
