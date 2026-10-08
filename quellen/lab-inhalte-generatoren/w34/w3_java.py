# Welt 3 – alle Java-Snippets (woertlich wie in den Aufgaben) + Probes
from lib import *

J = JavaProg("W3Check")
C = {}  # angezeigter Code je Schluessel

def reg(key, code, probe, wrap=None, extra=""):
    C[key] = code.strip("\n")
    J.add(key, code.strip("\n"), probe, wrap, extra)

def wrap1(meth, sig, args_fmt, call, rtype="int"):
    """Standard-Wrapper fuer statische Methoden: protokolliert Tiefe, Aufruf, Rueckgabe."""
    if rtype == "void":
        return (meth, "public static void %s(%s) { int i__ = Log.enter(%s); %s__(%s); Log.leave(i__, \"-\"); }" % (meth, sig, args_fmt, meth, call))
    return (meth, "public static %s %s(%s) { int i__ = Log.enter(%s); %s r__ = %s__(%s); Log.leave(i__, r__); return r__; }" % (rtype, meth, sig, args_fmt, rtype, meth, call))

KARTE_EXTRA = r'''
char[][] feld;
T_%s(String[] z) { feld = new char[z.length][z[0].length()]; for (int a = 0; a < z.length; a++) for (int b = 0; b < z[0].length(); b++) feld[a][b] = z[a].charAt(b); }
String text() { StringBuilder sb = new StringBuilder(); for (int a = 0; a < feld.length; a++) { if (a > 0) sb.append("/"); sb.append(new String(feld[a])); } return sb.toString(); }
'''
ISTIMFELD = "boolean istImFeld(int z, int s) { return z >= 0 && z < feld.length && s >= 0 && s < feld[0].length; }\n"

# ======================= Level 1 =======================
reg("L1_01", '''
public static String ruf(int n) {
    if (n <= 0) {
        return "*";
    }
    return ruf(n - 2) + n;
}
''', 'out(K+"r", ruf(5)); Log.dump(K+"t"); out(K+"r7", ruf(7)); Log.dump(K+"t7");',
    [wrap1("ruf", "int n", '"ruf(" + n + ")"', "n", "String")])

reg("L1_02", '''
public static int punkte(int n) {
    if (n == 0) {
        return 2;
    }
    return 3 * punkte(n - 1) - 1;
}
''', 'out(K+"r", punkte(3)); Log.dump(K+"t");', [wrap1("punkte", "int n", '"punkte(" + n + ")"', "n")])

reg("L1_03", '''
public static void rueckwaerts(String s) {
    if (s.length() > 0) {
        rueckwaerts(s.substring(1));
        print(s.charAt(0));
    }
}
''', 'out(K+"aus", capture(() -> rueckwaerts("NEBEL")));')

reg("L1_04", '''
public static int halbiere(int n, int k) {
    if (n <= 1) {
        return k;
    }
    return halbiere(n / 2, k + 1);
}
''', 'out(K+"r", halbiere(45, 0)); Log.dump(K+"t"); for (int n = 1; n <= 70; n++) out(K+"h"+n, halbiere(n, 0)); Log.reset();',
    [wrap1("halbiere", "int n, int k", '"halbiere(" + n + ", " + k + ")"', "n, k")])

L1_05 = '''
// soll 2 + 4 + ... + n liefern (n gerade, n >= 0)
public static int geradeSumme(int n) {
    if (n == 1) {
        return 0;
    }
    return n + geradeSumme(n - 2);
}
'''
reg("L1_05", L1_05, 'try { out(K+"r", geradeSumme(4)); } catch (StackOverflowError e) { out(K+"r", "StackOverflowError"); }')
for i, cond in enumerate(["n == 0", "n <= 0", "n < 1", "n < 2", "n <= 1"]):
    reg("L1_05k%d" % i, L1_05.replace("n == 1", cond), 'out(K+"r4", geradeSumme(4)); out(K+"r0", geradeSumme(0)); out(K+"r10", geradeSumme(10));')

L1_06 = '''
// soll zaehlen, wie oft die Ziffer 7 in n vorkommt (n >= 0)
public static int siebener(int n) {
    if (n == 0) {
        return 0;
    }
    int rest = siebener(n / 10);
    if (n % 10 == 7) {
        return 1;
    }
    return 0;
}
'''
reg("L1_06", L1_06, 'out(K+"r", siebener(7077)); out(K+"r2", siebener(7770));')
reg("L1_06k", L1_06.replace("        return 1;", "        return 1 + rest;").replace("    return 0;\n}", "    return rest;\n}"),
    'out(K+"r", siebener(7077)); out(K+"r2", siebener(7770)); out(K+"r0", siebener(0));')

reg("L1_07", '''
public static int anzahlGerade(int[] r, int i) {
    if (i == r.length) {
        return 0;
    }
    int rest = anzahlGerade(r, i + 1);
    if (r[i] % 2 == 0) {
        return rest + 1;
    }
    return rest;
}
''', 'int[] r = {4, 7, 2, 6}; out(K+"r", anzahlGerade(r, 0)); Log.dump(K+"t"); int[] e = {}; out(K+"leer", anzahlGerade(e, 0)); Log.reset();',
    [wrap1("anzahlGerade", "int[] r, int i", '"anzahlGerade(r, " + i + ")"', "r, i")])

reg("L1_08", '''
public static String verdichte(String s) {
    if (s.length() <= 1) {
        return s;
    }
    if (s.charAt(0) == s.charAt(1)) {
        return verdichte(s.substring(1));
    }
    return s.charAt(0) + verdichte(s.substring(1));
}
''', 'out(K+"r", verdichte("baaum")); Log.dump(K+"t"); out(K+"r2", verdichte("zzauberrr")); Log.reset();',
    [wrap1("verdichte", "String s", '"verdichte(\\"" + s + "\\")"', "s", "String")])

# ======================= Level 2 =======================
SPLITTER = '''
public static int splitter(int n) {
    if (n < 2) {
        return 1;
    }
    return splitter(n - 1) + splitter(n - 2);
}
'''
reg("L2_01", SPLITTER, 'out(K+"r", splitter(4)); Log.dump(K+"t"); for (int n = 0; n <= 20; n++) { out(K+"v"+n, splitter(n)); out(K+"a"+n, Log.rows.size()); Log.reset(); }',
    [wrap1("splitter", "int n", '"s" + n', "n")])

reg("L2_06", '''
public static int dreier(int n) {
    if (n <= 0) {
        return 1;
    }
    return dreier(n - 1) + dreier(n - 2) + dreier(n - 3);
}
''', 'for (int n = 0; n <= 7; n++) { out(K+"v"+n, dreier(n)); out(K+"a"+n, Log.rows.size()); Log.reset(); }',
    [wrap1("dreier", "int n", '"d" + n', "n")])

reg("L2_05", '''
public static int produktAb(int[] r, int i) {
    if (i == r.length) {
        return 1;
    }
    return r[i] * produktAb(r, i + 1);
}
''', 'int[] r = {3, 5, 2, 4}; out(K+"r", produktAb(r, 0)); int[] e = {}; out(K+"leer", produktAb(e, 0));')

reg("L2_07", '''
public static int aufrufe = 0;

public static int splitter(int n) {
    if (n < 2) {
        return 1;
    }
    aufrufe++;
    return splitter(n - 1) + splitter(n - 2);
}
''', 'aufrufe = 0; out(K+"r", splitter(6)); out(K+"auf", aufrufe); out(K+"alle", Log.rows.size()); Log.reset();',
    [wrap1("splitter", "int n", '"s" + n', "n")])

# Wachstum der Aufrufzahlen (Match-Aufgabe): Zaehler je Muster
reg("L2_04", '''
public static int z = 0;
public static int a(int n) { z++; if (n <= 0) { return 0; } return a(n - 1) + 1; }
public static int b(int n) { z++; if (n <= 1) { return 0; } return b(n / 2) + 1; }
public static int c(int n) { z++; if (n <= 1) { return 1; } return c(n - 1) + c(n - 2); }
public static int d(int n) { z++; if (n <= 0) { return 1; } return d(n - 1) + d(n - 1); }
public static int e(int n) { z++; if (n <= 0) { return 0; } return e(n - 2) + 1; }
''', '''for (int n : new int[]{10, 20}) {
 z = 0; a(n); out(K+"a"+n, z); z = 0; b(n); out(K+"b"+n, z); z = 0; c(n); out(K+"c"+n, z); z = 0; d(n); out(K+"d"+n, z); z = 0; e(n); out(K+"e"+n, z); }''')

# ======================= Level 3: Karte =======================
KARTE_A = ["##.#..", "#..#.#", "..##..", ".#..#.", "...#.."]
KARTE_B = [".#...", "..#.#", "#...#", ".#...", "..#.."]

reg("L3_01", ISTIMFELD + '''
boolean istBegehbar(int z, int s) { if (!istImFeld(z, s)) { return false; } char c = feld[z][s]; return c == '.' || c == 'S' || c == 'Z'; }
int anzahlBegehbareNachbarn(int z, int s) { int a = 0; if (istBegehbar(z - 1, s)) a++; if (istBegehbar(z, s + 1)) a++; if (istBegehbar(z + 1, s)) a++; if (istBegehbar(z, s - 1)) a++; return a; }
''', '''T_L3_01 k = new T_L3_01(new String[]{%s});
out(K+"len", k.feld.length); out(K+"len0", k.feld[0].length);
int[][] q = {{3,4},{4,2},{2,0},{1,6},{5,1},{0,2}};
for (int[] p : q) { String v; try { v = "" + k.feld[p[0]][p[1]]; } catch (ArrayIndexOutOfBoundsException e) { v = "Laufzeitfehler"; } out(K+"f"+p[0]+"_"+p[1], v); }
int[][] nb = {{0,2},{2,5},{3,3},{1,1}};
for (int[] p : nb) out(K+"nb"+p[0]+"_"+p[1], k.anzahlBegehbareNachbarn(p[0], p[1]));
StringBuilder acht = new StringBuilder();
for (int dz = -1; dz <= 1; dz++) for (int ds = -1; ds <= 1; ds++) { if (dz == 0 && ds == 0) continue; if (k.istBegehbar(3 + dz, 3 + ds)) acht.append((3+dz) + "," + (3+ds) + ";"); }
out(K+"acht33", acht);''' % ", ".join('"%s"' % z for z in KARTE_A), extra=KARTE_EXTRA % "L3_01")

reg("L3_04", '''
public int anzahlInZeile(int z, char c) {
    int anzahl = 0;
    for (int s = 0; s < feld[z].length; s++) {
        if (feld[z][s] == c) {
            anzahl++;
        }
    }
    return anzahl;
}
''', '''T_L3_04 k = new T_L3_04(new String[]{%s}); for (int z = 0; z < 5; z++) out(K+"z"+z, k.anzahlInZeile(z, '.'));''' % ", ".join('"%s"' % z for z in KARTE_A),
    extra=KARTE_EXTRA % "L3_04")

FACKEL = '''
public void fackel(int z, int s) {
    if (!istImFeld(z, s) || feld[z][s] != '.') {
        return;
    }
    feld[z][s] = '+';
    fackel(z - 1, s);
    fackel(z, s + 1);
    fackel(z + 1, s);
    fackel(z, s - 1);
}
'''
reg("L3_05", ISTIMFELD + FACKEL, '''T_L3_05 k = new T_L3_05(new String[]{%s}); k.fackel(0, 0); out(K+"karte", k.text());
StringBuilder sb = new StringBuilder(); int maxT = 0, maxAll = 0, m = 0;
for (String[] r : Log.rows) { maxAll = Math.max(maxAll, Integer.parseInt(r[0])); if (r[2].equals("M")) { m++; sb.append(r[1] + "@" + r[0] + ";"); maxT = Math.max(maxT, Integer.parseInt(r[0])); } }
out(K+"folge", sb); out(K+"m", m); out(K+"aufrufe", Log.rows.size()); out(K+"maxT", maxT); out(K+"maxAll", maxAll); Log.reset();''' % ", ".join('"%s"' % z for z in KARTE_B),
    [("fackel", 'public void fackel(int z, int s) { boolean mark = istImFeld(z, s) && feld[z][s] == \'.\'; int i__ = Log.enter(z + "," + s); fackel__(z, s); Log.leave(i__, mark ? "M" : "-"); }')],
    extra=KARTE_EXTRA % "L3_05")

FACKEL_BUG = '''
public void fackel(int z, int s) {
    if (feld[z][s] != '.' || !istImFeld(z, s)) {
        return;
    }
    feld[z][s] = '+';
    fackel(z - 1, s);
    fackel(z, s + 1);
    fackel(z + 1, s);
    fackel(z, s - 1);
}
'''
reg("L3_07", ISTIMFELD + FACKEL_BUG, '''T_L3_07 k = new T_L3_07(new String[]{%s}); try { k.fackel(0, 0); out(K+"r", "ok"); } catch (Throwable t) { out(K+"r", ex(t)); }''' % ", ".join('"%s"' % z for z in KARTE_B),
    extra=KARTE_EXTRA % "L3_07")
for i, cond in enumerate(["!istImFeld(z, s) || feld[z][s] != '.'", "!(istImFeld(z, s) && feld[z][s] == '.')"]):
    reg("L3_07k%d" % i, ISTIMFELD + FACKEL_BUG.replace("feld[z][s] != '.' || !istImFeld(z, s)", cond),
        '''T_L3_07k%d k = new T_L3_07k%d(new String[]{%s}); k.fackel(0, 0); out(K+"karte", k.text());''' % (i, i, ", ".join('"%s"' % z for z in KARTE_B)),
        extra=KARTE_EXTRA % ("L3_07k%d" % i))

reg("L3_08", ISTIMFELD + '''
public int strahl(int z, int s) {
    if (!istImFeld(z, s) || feld[z][s] == '#') {
        return 0;
    }
    return 1 + strahl(z + 1, s + 1);
}
''', '''T_L3_08 k = new T_L3_08(new String[]{%s}); out(K+"r", k.strahl(0, 0)); Log.dump(K+"t"); out(K+"r01", k.strahl(0, 2)); Log.reset();''' % ", ".join('"%s"' % z for z in KARTE_B),
    [("strahl", 'public int strahl(int z, int s) { String c = istImFeld(z, s) ? "\'" + feld[z][s] + "\'" : "außerhalb"; int i__ = Log.enter("strahl(" + z + ", " + s + ")#" + c); int r__ = strahl__(z, s); Log.leave(i__, r__); return r__; }')],
    extra=KARTE_EXTRA % "L3_08")

# ======================= Level 4: Backtracking =======================
FINDEWEG = '''
public boolean findeWeg(int z, int s) {
    schritte++;
    if (!istImFeld(z, s)) {
        return false;
    }
    char alt = feld[z][s];
    if (alt == 'Z') {
        return true;
    }
    if (alt != '.' && alt != 'S') {
        return false;
    }
    feld[z][s] = '*';
    if (findeWeg(z - 1, s) || findeWeg(z, s + 1) || findeWeg(z + 1, s) || findeWeg(z, s - 1)) {
        if (alt == 'S') {
            feld[z][s] = 'S';
        }
        return true;
    }
    feld[z][s] = 'x';
    if (alt == 'S') {
        feld[z][s] = 'S';
    }
    return false;
}
'''
FW_WRAP = ('findeWeg', '''
java.util.ArrayList<String> pfad = new java.util.ArrayList<>();
public boolean findeWeg(int z, int s) {
    boolean betritt = istImFeld(z, s) && (feld[z][s] == '.' || feld[z][s] == 'S' || feld[z][s] == 'Z');
    String richtung = "-";
    if (!pfad.isEmpty()) { String[] p = pfad.get(pfad.size() - 1).split("\\\\|"); int pz = Integer.parseInt(p[0].substring(1)), ps = Integer.parseInt(p[1].substring(0, p[1].length() - 1));
        richtung = z < pz ? "oben" : z > pz ? "unten" : s > ps ? "rechts" : "links"; }
    pfad.add("(" + z + "|" + s + ")");
    int i__ = Log.enter(betritt ? (richtung + "#" + String.join("", pfad) + (istImFeld(z, s) && feld[z][s] == 'Z' ? "#Z" : "")) : "");
    boolean r__ = findeWeg__(z, s);
    Log.leave(i__, r__);
    pfad.remove(pfad.size() - 1);
    return r__;
}''')
KRYPTA = ["..#.#", "S##.Z", "....."]
UMWEG = ["....", "S..Z"]
for key, karte, st in [("L4_K", KRYPTA, (1, 0)), ("L4_U", UMWEG, (1, 0))]:
    reg(key, ISTIMFELD + "int schritte = 0;\n" + FINDEWEG, '''T_%s k = new T_%s(new String[]{%s}); boolean ok = k.findeWeg(%d, %d); out(K+"ok", ok); out(K+"karte", k.text()); out(K+"schritte", k.schritte);
int i = 0; for (String[] r : Log.rows) { if (!r[1].equals("")) { out(K+"b"+i, r[0] + "|" + r[1] + "|" + r[2]); i++; } } out(K+"bn", i); Log.reset();''' % (key, key, ", ".join('"%s"' % z for z in karte), st[0], st[1]),
        [FW_WRAP], extra=KARTE_EXTRA % key)

# ======================= Level 5: Teile und herrsche =======================
BINAER = '''
public static int binaerRek(int[] r, int x, int lo, int hi) {
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
}
'''
SCHATZ = "{3, 8, 12, 17, 23, 31, 36, 42, 50, 57, 64, 71}"
reg("L5_01", BINAER, 'int[] r = %s; out(K+"r57", binaerRek(r, 57, 0, 11)); Log.dump(K+"t57"); out(K+"r20", binaerRek(r, 20, 0, 11)); Log.dump(K+"t20");' % SCHATZ,
    [wrap1("binaerRek", "int[] r, int x, int lo, int hi", 'lo + "," + hi + "," + (lo <= hi ? (lo + hi) / 2 + "," + r[(lo + hi) / 2] : "-,-")', "r, x, lo, hi")])

MAXTH = '''
public static int maximumTH(int[] r, int von, int bis) {
    if (von == bis) {
        return r[von];
    }
    int mitte = (von + bis) / 2;
    int links = maximumTH(r, von, mitte);
    int rechts = maximumTH(r, mitte + 1, bis);
    if (links > rechts) {
        return links;
    }
    return rechts;
}
'''
reg("L5_04", MAXTH, 'int[] r = {4, 9, 2, 7, 5}; out(K+"r", maximumTH(r, 0, 4)); Log.dump(K+"t");',
    [wrap1("maximumTH", "int[] r, int von, int bis", 'von + "," + bis', "r, von, bis")])

MERGE = '''
public static int[] teilstueck(int[] r, int von, int bis) {
    int[] t = new int[bis - von];
    for (int i = 0; i < t.length; i++) {
        t[i] = r[von + i];
    }
    return t;
}

public static int[] verschmelze(int[] a, int[] b) {
    int[] erg = new int[a.length + b.length];
    int i = 0;
    int j = 0;
    int k = 0;
    while (i < a.length && j < b.length) {
        if (a[i] <= b[j]) {
            erg[k] = a[i];
            i++;
        } else {
            erg[k] = b[j];
            j++;
        }
        k++;
    }
    while (i < a.length) {
        erg[k] = a[i];
        i++;
        k++;
    }
    while (j < b.length) {
        erg[k] = b[j];
        j++;
        k++;
    }
    return erg;
}

public static int[] mergeSort(int[] r) {
    if (r.length <= 1) {
        return teilstueck(r, 0, r.length);
    }
    int mitte = r.length / 2;
    int[] links = mergeSort(teilstueck(r, 0, mitte));
    int[] rechts = mergeSort(teilstueck(r, mitte, r.length));
    return verschmelze(links, rechts);
}
'''
reg("L5_05", MERGE, '''int[] r = {14, 6, 11, 3, 9, 2, 7}; out(K+"r", arr(mergeSort(r)));
int nm = 0, maxT = 0; for (String[] x : Log.rows) { if (x[1].startsWith("M")) { nm++; maxT = Math.max(maxT, Integer.parseInt(x[0])); } }
out(K+"nm", nm); out(K+"maxT", maxT);
int i = 0; for (String[] x : Log.rows) { if (x[1].startsWith("V")) { out(K+"v"+i, x[1].substring(1) + "|" + x[2]); i++; } } out(K+"nv", i); Log.reset();''',
    [("mergeSort", 'public static int[] mergeSort(int[] r) { int i__ = Log.enter("M" + arr(r)); int[] e__ = mergeSort__(r); Log.leave(i__, arr(e__)); return e__; }'),
     ("verschmelze", 'public static int[] verschmelze(int[] a, int[] b) { int i__ = Log.enter("V{" + arr(a) + "}+{" + arr(b) + "}"); int[] e__ = verschmelze__(a, b); Log.leave(i__, arr(e__)); return e__; }')])

reg("L5_07", '''
public static int anzahlTH(int[] r, int x, int von, int bis) {
    if (von == bis) {
        if (r[von] == x) { return 1; }
        return 0;
    }
    int mitte = (von + bis) / 2;
    int links = anzahlTH(r, x, von, mitte);
    int rechts = anzahlTH(r, x, mitte + 1, bis);
    return links + rechts;
}
''', 'int[] r = {5, 3, 5, 5, 8, 1, 5}; out(K+"r", anzahlTH(r, 5, 0, 6)); out(K+"r0", anzahlTH(r, 4, 0, 6));')
reg("L5_07f", '''
public static int anzahlTH(int[] r, int x, int von, int bis) {
    if (von == bis) {
        if (r[von] == x) { return 1; }
        return 0;
    }
    int mitte = (von + bis + 1) / 2;
    int links = anzahlTH(r, x, von, mitte);
    int rechts = anzahlTH(r, x, mitte + 1, bis);
    return links + rechts;
}
''', 'int[] r = {5, 3}; try { out(K+"r", anzahlTH(r, 5, 0, 1)); } catch (StackOverflowError e) { out(K+"r", "StackOverflowError"); }')

# Stabilitaet: mergeSort auf Paaren (Schluessel*10 + Index), Vergleich nur nach Schluessel, <= bzw. <
STAB = '''
static boolean strikt = false;
static int[] vs(int[] a, int[] b) { int[] e = new int[a.length + b.length]; int i = 0, j = 0, k = 0;
  while (i < a.length && j < b.length) { boolean links = strikt ? a[i] / 10 < b[j] / 10 : a[i] / 10 <= b[j] / 10; if (links) { e[k] = a[i]; i++; } else { e[k] = b[j]; j++; } k++; }
  while (i < a.length) { e[k++] = a[i++]; } while (j < b.length) { e[k++] = b[j++]; } return e; }
static int[] ts(int[] r, int v, int b) { int[] t = new int[b - v]; for (int i = 0; i < t.length; i++) t[i] = r[v + i]; return t; }
static int[] ms(int[] r) { if (r.length <= 1) return ts(r, 0, r.length); int m = r.length / 2; return vs(ms(ts(r, 0, m)), ms(ts(r, m, r.length))); }
'''
reg("L5_08", STAB, 'int[] r = {50, 21, 52, 23, 14}; strikt = false; out(K+"le", arr(ms(r))); strikt = true; out(K+"lt", arr(ms(r)));')

# Vergleiche in verschmelze (Zaehlkopie)
reg("L5_06", STAB.replace("static boolean strikt = false;", "static boolean strikt = false; static int vgl = 0;").replace("boolean links =", "vgl++; boolean links ="),
    'int[] r = {140, 60, 110, 30, 90, 20, 70}; vgl = 0; ms(r); out(K+"vgl", vgl);')

# ======================= Level 6: Quicksort & Co. =======================
QS = '''
public static void quickSort(int[] r, int lo, int hi) {
    if (lo < hi) {
        int p = zerlege(r, lo, hi);
        quickSort(r, lo, p - 1);
        quickSort(r, p + 1, hi);
    }
}

public static int zerlege(int[] r, int lo, int hi) {
    int pivot = r[lo];
    int grenze = lo;
    for (int i = lo + 1; i <= hi; i++) {
        if (r[i] < pivot) {
            grenze++;
            int h = r[grenze];
            r[grenze] = r[i];
            r[i] = h;
        }
    }
    int hilf = r[lo];
    r[lo] = r[grenze];
    r[grenze] = hilf;
    return grenze;
}
'''
QS_WRAP = [("quickSort", 'public static void quickSort(int[] r, int lo, int hi) { int i__ = Log.enter("Q" + lo + "," + hi); quickSort__(r, lo, hi); Log.leave(i__, "-"); }'),
           ("zerlege", 'static java.util.ArrayList<String> zl = new java.util.ArrayList<>(); public static int zerlege(int[] r, int lo, int hi) { int t = Log.tiefe - 1; int p = zerlege__(r, lo, hi); zl.add(t + "|" + lo + "|" + hi + "|" + p + "|" + arr(r) + "|" + (hi - lo)); return p; }')]
reg("L6_01", QS, '''int[] r = {5, 8, 2, 9, 1, 7, 3, 6}; int p = zerlege(r, 0, 7); out(K+"p", p); out(K+"nach", arr(r)); zl.clear();
int[] q = {5, 8, 2, 9, 1, 7, 3, 6}; quickSort(q, 0, 7); out(K+"sort", arr(q)); for (int i = 0; i < zl.size(); i++) out(K+"z"+i, zl.get(i)); out(K+"nz", zl.size()); out(K+"nq", Log.rows.size()); Log.reset(); zl.clear();
int[] s = {1, 2, 3, 4, 5, 6}; quickSort(s, 0, 5); int v = 0, mt = 0; for (String z : zl) { String[] f = z.split("\\\\|"); v += Integer.parseInt(f[5]); mt = Math.max(mt, Integer.parseInt(f[0])); } out(K+"wv", v); out(K+"wt", mt); out(K+"wn", zl.size()); out(K+"wq", Log.rows.size()); Log.reset(); zl.clear();''',
    QS_WRAP)

QS_BUG = QS.replace("quickSort(r, p + 1, hi);", "quickSort(r, p, hi);")
reg("L6_08", QS_BUG, '''int[][] tests = {{1, 2, 3}, {3, 1, 2}, {3, 2, 1}, {2, 1}, {2, 3, 1}, {4, 1, 3, 2}};
for (int t = 0; t < tests.length; t++) { try { quickSort(tests[t], 0, tests[t].length - 1); out(K+"t"+t, "ok:" + arr(tests[t])); } catch (StackOverflowError e) { out(K+"t"+t, "SO"); } }''')

reg("L6_05", '''
public static void sortiereBis(int[] r, int ende) {
    if (ende <= 0) {
        return;
    }
    int m = 0;
    for (int i = 1; i <= ende; i++) {
        if (r[i] > r[m]) {
            m = i;
        }
    }
    int h = r[m];
    r[m] = r[ende];
    r[ende] = h;
    sortiereBis(r, ende - 1);
}
''', 'int[] r = {6, 2, 9, 4, 7, 1}; sortiereBis(r, 5); out(K+"r", arr(r)); out(K+"aufrufe", Log.rows.size()); Log.reset();',
    [wrap1("sortiereBis", "int[] r, int ende", '"" + ende', "r, ende", "void")])

PFANNE = '''
public static void wende(int[] r, int bis) {
    int li = 0;
    int re = bis;
    while (li < re) {
        int h = r[li];
        r[li] = r[re];
        r[re] = h;
        li++;
        re--;
    }
}

public static void pfannkuchen(int[] r, int n) {
    if (n <= 1) {
        return;
    }
    int m = 0;
    for (int i = 1; i < n; i++) {
        if (r[i] > r[m]) {
            m = i;
        }
    }
    wende(r, m);
    wende(r, n - 1);
    pfannkuchen(r, n - 1);
}
'''
reg("L6_06", PFANNE, '''int[] r = {3, 1, 4, 2}; pfannkuchen(r, 4); out(K+"r", arr(r)); Log.dump(K+"t"); out(K+"wende", wz); wz = 0;
boolean alle = true; for (int n = 1; n <= 6; n++) { int[] p = new int[n]; for (int i = 0; i < n; i++) p[i] = i; do { int[] q = p.clone(); pfannkuchen(q, n); Log.reset(); for (int i = 0; i < n; i++) if (q[i] != i) alle = false; } while (nextPerm(p)); } out(K+"korrekt", alle);
for (int n = 1; n <= 10; n++) { int[] q = new int[n]; for (int i = 0; i < n; i++) q[i] = (7 * i) % n; wz = 0; pfannkuchen(q, n); out(K+"a"+n, Log.rows.size()); out(K+"w"+n, wz); Log.reset(); }''',
    [("pfannkuchen", 'public static void pfannkuchen(int[] r, int n) { int i__ = Log.enter(n + "#" + arr(r)); pfannkuchen__(r, n); Log.leave(i__, arr(r)); }'),
     ("wende", 'static int wz = 0; public static void wende(int[] r, int bis) { wz++; wende__(r, bis); }')],
    extra='static boolean nextPerm(int[] a) { int i = a.length - 2; while (i >= 0 && a[i] >= a[i + 1]) i--; if (i < 0) return false; int j = a.length - 1; while (a[j] <= a[i]) j--; int h = a[i]; a[i] = a[j]; a[j] = h; for (int l = i + 1, r = a.length - 1; l < r; l++, r--) { h = a[l]; a[l] = a[r]; a[r] = h; } return true; }')

if __name__ == "__main__":
    V = J.run()
    for k in sorted(V):
        print(k, "=", V[k])
