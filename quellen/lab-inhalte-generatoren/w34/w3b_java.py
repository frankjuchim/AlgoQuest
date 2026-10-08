# Welt 3 – Boss-Pool-Snippets (ergaenzt w3_java.J)
from w3_java import *

def q(lst): return ", ".join('"%s"' % z for z in lst)

reg("B01", '''
public static int widerhall(int n) {
    if (n < 3) {
        return n;
    }
    return widerhall(n - 3) + n;
}
''', 'out(K+"r", widerhall(10)); Log.dump(K+"t");', [wrap1("widerhall", "int n", '"widerhall(" + n + ")"', "n")])

reg("B02", '''
public static String ruf(String s) {
    if (s.length() <= 1) {
        return s;
    }
    return s.charAt(s.length() - 1) + ruf(s.substring(1, s.length() - 1)) + s.charAt(0);
}
''', 'out(K+"r", ruf("HALLO")); out(K+"n", Log.rows.size()); Log.reset(); out(K+"r2", ruf("ECHO")); out(K+"n2", Log.rows.size()); Log.reset();',
    [wrap1("ruf", "String s", '"ruf(" + s + ")"', "s", "String")])

reg("B03", '''
public static int stufen(int n) {
    if (n == 0) {
        return 0;
    }
    return 1 + stufen(n - 2);
}
''', 'out(K+"r6", stufen(6)); try { out(K+"r5", stufen(5)); } catch (StackOverflowError e) { out(K+"r5", "StackOverflowError"); }')

SCHLUCHT = ["#..#.", "..#..", ".##.#", "....#"]
reg("B04", ISTIMFELD + '''
boolean istBegehbar(int z, int s) { return istImFeld(z, s) && feld[z][s] == '.'; }
int nachbarn(int z, int s) { int a = 0; if (istBegehbar(z - 1, s)) a++; if (istBegehbar(z, s + 1)) a++; if (istBegehbar(z + 1, s)) a++; if (istBegehbar(z, s - 1)) a++; return a; }
''', 'T_B04 k = new T_B04(new String[]{%s}); out(K+"len", k.feld.length); out(K+"len0", k.feld[0].length); out(K+"f23", k.feld[2][3]); out(K+"f32", k.feld[3][2]);'
     'out(K+"nb01", k.nachbarn(0, 1)); out(K+"nb13", k.nachbarn(1, 3)); out(K+"nb30", k.nachbarn(3, 0));' % q(SCHLUCHT), extra=KARTE_EXTRA % "B04")

reg("B05", BINAER, 'int[] r = {2, 5, 9, 14, 20, 27, 33, 41, 48}; out(K+"r", binaerRek(r, 14, 0, 8)); Log.dump(K+"t");',
    [wrap1("binaerRek", "int[] r, int x, int lo, int hi", 'lo + "," + hi + "," + (lo <= hi ? (lo + hi) / 2 + "," + r[(lo + hi) / 2] : "-,-")', "r, x, lo, hi")])

reg("B06", QS, 'int[] r = {7, 3, 9, 1, 8, 5}; int p = zerlege(r, 0, 5); out(K+"p", p); out(K+"nach", arr(r));')

PILZE = ["P.P#.", "PP.#P", "#PPP.", "..#PP"]
reg("B07", ISTIMFELD + '''
public int ernte(int z, int s) {
    if (!istImFeld(z, s) || feld[z][s] != 'P') {
        return 0;
    }
    feld[z][s] = '-';
    return 1 + ernte(z - 1, s) + ernte(z, s + 1) + ernte(z + 1, s) + ernte(z, s - 1);
}
''', 'T_B07 k = new T_B07(new String[]{%s}); out(K+"r", k.ernte(2, 2)); out(K+"karte", k.text());' % q(PILZE), extra=KARTE_EXTRA % "B07")

reg("B08", '''
public static int funken(int n) {
    if (n <= 0) {
        return 1;
    }
    return funken(n - 1) + funken(n - 1);
}
''', 'for (int n = 0; n <= 20; n++) { out(K+"v"+n, funken(n)); out(K+"a"+n, Log.rows.size()); Log.reset(); }',
    [wrap1("funken", "int n", '"" + n', "n")])

SUCHE = '''
public static int suche(int[] r, int x, int lo, int hi) {
    if (lo > hi) {
        return -1;
    }
    int mid = (lo + hi) / 2;
    if (r[mid] == x) {
        return mid;
    }
    if (r[mid] < x) {
        return suche(r, x, mid + 1, hi);
    }
    return suche(r, x, lo, mid);
}
'''
reg("B09", SUCHE, '''int[] r = {4, 10, 15, 22, 30, 37};
for (int x : new int[]{22, 37, 10, 3, 4, 15, 30, 40}) { try { out(K+"r"+x, suche(r, x, 0, 5)); } catch (StackOverflowError e) { out(K+"r"+x, "SO"); } }''')
reg("B09k", SUCHE.replace("return suche(r, x, lo, mid);", "return suche(r, x, lo, mid - 1);"),
    'int[] r = {4, 10, 15, 22, 30, 37}; for (int x : new int[]{3, 4, 10, 15, 22, 30, 37, 40, 12}) out(K+"r"+x, suche(r, x, 0, 5));')

reg("B10", MERGE, '''int[] r = {9, 4, 7, 1, 6}; out(K+"r", arr(mergeSort(r)));
int i = 0; for (String[] x : Log.rows) { if (x[1].startsWith("V")) { out(K+"v"+i, x[1].substring(1) + "|" + x[2]); i++; } } out(K+"nv", i); Log.reset();''',
    [("verschmelze", 'public static int[] verschmelze(int[] a, int[] b) { int i__ = Log.enter("V{" + arr(a) + "}+{" + arr(b) + "}"); int[] e__ = verschmelze__(a, b); Log.leave(i__, arr(e__)); return e__; }')])

GANG = '''
public int gangLinks(int z, int s) {
    if (s < 0 || feld[z][s] == '#') {
        return 0;
    }
    return 1 + gangLinks(z, s - 1);
}
'''
reg("B11", GANG, 'T_B11 k = new T_B11(new String[]{%s}); out(K+"r33", k.gangLinks(3, 3)); out(K+"r14", k.gangLinks(1, 4)); out(K+"r02", k.gangLinks(0, 2));' % q(SCHLUCHT),
    extra=KARTE_EXTRA % "B11")
reg("B11f", GANG.replace("s < 0 || feld[z][s] == '#'", "feld[z][s] == '#' || s < 0"),
    'T_B11f k = new T_B11f(new String[]{%s}); try { out(K+"r", k.gangLinks(3, 3)); } catch (Throwable t) { out(K+"r", ex(t)); }' % q(SCHLUCHT),
    extra=KARTE_EXTRA % "B11f")

GROTTE = ["S..#", ".#.#", "..##", "#..Z"]
reg("B12", ISTIMFELD + "int schritte = 0;\n" + FINDEWEG, '''T_B12 k = new T_B12(new String[]{%s}); boolean ok = k.findeWeg(0, 0); out(K+"ok", ok); out(K+"karte", k.text()); out(K+"schritte", k.schritte);
int i = 0; for (String[] r : Log.rows) { if (!r[1].equals("")) { out(K+"b"+i, r[0] + "|" + r[1] + "|" + r[2]); i++; } } out(K+"bn", i); Log.reset();''' % q(GROTTE),
    [FW_WRAP], extra=KARTE_EXTRA % "B12")

reg("B13", '''
public static void welle(int[] r, int i) {
    if (i >= r.length - 1) {
        return;
    }
    if (r[i] > r[i + 1]) {
        int h = r[i];
        r[i] = r[i + 1];
        r[i + 1] = h;
    }
    welle(r, i + 1);
}

public static void echoSort(int[] r, int n) {
    if (n <= 1) {
        return;
    }
    welle(r, 0);
    echoSort(r, n - 1);
}
''', '''int[] r = {4, 2, 5, 1}; echoSort(r, 4); out(K+"r", arr(r)); for (String[] x : Log.rows) out(K+"e"+x[0], x[1]); out(K+"ne", Log.rows.size()); out(K+"welle", wz); out(K+"vgl", vgl); Log.reset();''',
    [("echoSort", 'public static void echoSort(int[] r, int n) { int i__ = Log.enter(n + "#" + arr(r)); echoSort__(r, n); Log.leave(i__, "-"); }'),
     ("welle", 'static int vgl = 0; static int wz = 0; public static void welle(int[] r, int i) { wz++; if (i < r.length - 1) vgl++; welle__(r, i); }')])

reg("B14", '''
public static int posMin(int[] r, int von, int bis) {
    if (von == bis) {
        return von;
    }
    int mitte = (von + bis) / 2;
    int l = posMin(r, von, mitte);
    int re = posMin(r, mitte + 1, bis);
    if (r[l] <= r[re]) {
        return l;
    }
    return re;
}
''', 'int[] r = {8, 3, 6, 3, 9, 4}; out(K+"r", posMin(r, 0, 5)); out(K+"n", Log.rows.size()); int mt = 0; for (String[] x : Log.rows) mt = Math.max(mt, Integer.parseInt(x[0])); out(K+"mt", mt); Log.reset();',
    [wrap1("posMin", "int[] r, int von, int bis", 'von + "," + bis', "r, von, bis")])

reg("B15", QS, '''for (int n : new int[]{10, 20, 40}) { int[] r = new int[n]; for (int i = 0; i < n; i++) r[i] = i; zl.clear(); quickSort(r, 0, n - 1); int v = 0; for (String z : zl) v += Integer.parseInt(z.split("\\\\|")[5]); out(K+"v"+n, v); Log.reset(); }''', QS_WRAP)

if __name__ == "__main__":
    V = J.run()
    for k in sorted(V):
        if k.startswith("B"):
            print(k, "=", V[k])

reg("TXT_PRODUKT", '''
public static int produkt(int[] r) {
    int p = 1;
    for (int i = 0; i < r.length; i++) {
        p = p * r[i];
    }
    return p;
}
''', 'int[] r = {3, 5, 2, 4}; out(K+"r", produkt(r));')
