# Level 0.5 – Die Zauberschule II (DS 5): Reihungen als Parameter/Rueckgabe, Wert vs. Referenz, Hilfsmethoden
from lib import *

LEVEL5 = {
    "id": "W0-L5", "nr": "0.5", "titel": "Zauberschule II: Wert und Referenz", "ds": [5],
    "ab": "AB 4 „Die Zauberschule“, Teil 2 (Infoteile 7–9, Aufgaben 8–12)",
    "ide": "AQ_W0_Akademie_Geruest.txt – Level 0.5 (Klasse ZauberII, Testklasse L05ZauberIITest)",
    "intro": [
        txt("Jetzt bekommen Zauberformeln ganze Reihungen als Zutat – und manche Änderungen sind danach im Hauptprogramm sichtbar, andere nicht."),
        hin("**Merke:** Java übergibt immer eine **Kopie des Werts** der Argumentvariablen. Bei Ganzzahlen ist das die Zahl, bei Reihungen der "
            "**Pfeil** (Referenz). Einen Parameter neu belegen (`n = …`, `r = new …`) wirkt nie nach außen; den **Inhalt** einer übergebenen "
            "Reihung ändern (`r[i] = …`) wirkt immer nach außen. „liefert eine neue Reihung“ → `new` und zurückgeben; „verändert r“ → `void`."),
    ],
    "aufgaben": [],
}

# ---------------------------------------------------------------- 01
P1 = '''public static void verdreifache(int n) {
    n = n * 3;
}
public static void verdreifacheAlle(int[] r) {
    for (int i = 0; i < r.length; i++) {
        r[i] = r[i] * 3;
    }
}
// Hauptprogramm
int x = 4;
int[] t = {1, 2};
verdreifache(x);
verdreifacheAlle(t);
println(x + " " + t[0] + " " + t[1]);'''

def c01(t):
    meth, main = P1.split("// Hauptprogramm\n")
    o, ls = jrun(meth, main)
    x, a, b = ls[0].split()
    expect(t, "g1", x); expect(t, "g2", a); expect(t, "g3", b)

T("W0-L5-01", "Zahl oder Pfeil?", 1, "Objektkarten und Referenzen", [],
  [code(P1), txt("Die Ausgabe lautet: [[g1]] [[g2]] [[g3]]")],
  gaps({"g1": fz(), "g2": fz(), "g3": fz()}),
  {"g1": ["4"], "g2": ["3"], "g3": ["6"]},
  [txt("`verdreifache` bekommt eine **Kopie der Zahl** 4 – `n` wird 12, `x` bleibt 4. `verdreifacheAlle` bekommt eine Kopie des "
       "**Pfeils**: `r` und `t` zeigen auf dieselbe Reihung, also ist die Änderung über `r` auch in `t` sichtbar: {3, 6}.")],
  ["Was genau steht in der Variablen t – die Werte oder ein Verweis?"], c01)

# ---------------------------------------------------------------- 02
ITEMS2 = [("e1", "**begrenze** setzt jeden Wert in r, der größer als 100 ist, auf 100.", "inplace"),
          ("e2", "**quadriert** liefert eine Reihung mit den Quadraten der Werte von r; r bleibt unverändert.", "neu"),
          ("e3", "**mische** vertauscht die Elemente von r zufällig.", "inplace"),
          ("e4", "**nurPositive** liefert eine Reihung, die genau die positiven Werte von r enthält.", "neu"),
          ("e5", "**verschiebeLinks** rückt alle Werte von r einen Index nach links; der erste Wert wandert ans Ende.", "inplace"),
          ("e6", "**teilreihung** liefert die Elemente von r von Index a bis Index b.", "neu")]

def c02(t):
    # Beleg: Reihung mit anderer Laenge kann nur als neue Reihung entstehen -> Rueckgabetyp noetig
    ok, _ = jcompile("static void nurPositive(int[] r) { int[] neu = new int[1]; r = neu; }",
                     "int[] a = {-1, 2}; nurPositive(a);")
    assert ok
    o, _ = jrun("static void nurPositive(int[] r) { int[] neu = {2}; r = neu; }", 'int[] a = {-1, 2}; nurPositive(a); out("len", a.length);')
    assert o["len"] == "2"     # die Aenderung kommt nicht an -> void ist hier unmoeglich
    for k, _m, s in ITEMS2: assert t["loesung"][k] == s

T("W0-L5-02", "In der Reihung oder neu?", 1, "Methodenkopf und Signatur", ["P2", "P3"],
  [txt("Ordne jede Beschreibung zu: Arbeitet die Methode **in der Reihung** (Rückgabetyp nichts) oder liefert sie eine **neue Reihung** "
       "(Rückgabetyp Reihung von Ganzzahl)?")],
  match([(k, m) for k, m, _s in ITEMS2],
        [("inplace", "verändert r – Rückgabetyp nichts (`void`)"), ("neu", "liefert neue Reihung – Rückgabetyp Reihung von Ganzzahl (`int[]`)")]),
  {k: s for k, _m, s in ITEMS2},
  [txt("Formulierungen wie „setzt“, „vertauscht“, „rückt“ beschreiben eine Änderung **in** r → `void`, Muster `r[i] = …`. "
       "„liefert eine Reihung“ verlangt `new` und `return`. Hat das Ergebnis eine **andere Länge** (nurPositive, teilreihung), "
       "geht es ohnehin nur mit einer neuen Reihung."),
   hin("Falle **P2/P3**: Falscher Rückgabetyp oder das Original verändert, obwohl „r bleibt unverändert“ gefordert ist.")],
  ["Achte auf die Verben im Text: „setzt“ oder „liefert“?"], c02)

# ---------------------------------------------------------------- 03
ROT = '''public static void rotiereRechts(int[] r) {
    for (int i = r.length - 1; i >= 1; i--) {
        tausche(r, i, i - 1);
    }
}'''

def c03(t):
    o, ls = jrun('static void tausche(int[] r, int i, int j) { System.out.println("sw=" + i + "," + j); int h = r[i]; r[i] = r[j]; r[j] = h; }\n' + ROT,
                 'int[] r = {8, 5, 2, 9}; rotiereRechts(r); out("r", arr(r));')
    sw = [[int(x) for x in l[3:].split(",")] for l in ls if l.startswith("sw=")]
    assert sw == t["loesung"]["tausche"], sw
    assert o["r"] == "9,8,5,2"

T("W0-L5-03", "Der Ringzauber", 1, "Tracetabelle", ["P6"],
  [txt("`rotiereRechts` verschiebt alle Werte um einen Platz nach rechts; der letzte Wert wandert nach vorn. "
       "`tausche(r, i, j)` vertauscht `r[i]` und `r[j]`."), code(ROT),
   txt("Führe die Tausche des Aufrufs mit `r = {8, 5, 2, 9}` in der richtigen Reihenfolge aus.")],
  arr([8, 5, 2, 9], "tausch"),
  {"tausche": [[3, 2], [2, 1], [1, 0]]},
  [txt("Die Schleife läuft **rückwärts** von 3 bis 1: (3, 2), (2, 1), (1, 0). Die 9 „wandert“ dabei Schritt für Schritt nach vorn: "
       "{8, 5, 9, 2} → {8, 9, 5, 2} → {9, 8, 5, 2}. Die Methode ist `void` – sie verändert die übergebene Reihung selbst."),
   hin("Falle **P6**: Die Schleife endet bei i = 1, sonst würde `r[-1]` gelesen.")],
  ["Beginne mit i = r.length − 1 = 3."], c03)

# ---------------------------------------------------------------- 04
P4 = '''public static void plusEins(int[] r) {
    for (int i = 0; i < r.length; i++) {
        r[i] = r[i] + 1;
    }
}
public static int[] plusEinsKopie(int[] r) {
    int[] n = new int[r.length];
    for (int i = 0; i < r.length; i++) {
        n[i] = r[i] + 1;
    }
    return n;
}
public static void ersetze(int[] r) {
    r = new int[3];
    r[0] = 9;
}
public static int[] ersteNull(int[] r) {
    r[0] = 0;
    return r;
}
// Hauptprogramm
int[] a = {5, 6, 7};
plusEins(a);
int[] b = plusEinsKopie(a);
ersetze(b);
int[] c = ersteNull(b);
c[2] = 1;
println(a[0] + " " + a[1] + " " + a[2]);
println(b[0] + " " + b[1] + " " + b[2]);
println(b == c);
println(a == b);'''

def c04(t):
    meth, main = P4.split("// Hauptprogramm\n")
    o, ls = jrun(meth, main)
    a = ls[0].split(); b = ls[1].split()
    for i in range(3): expect(t, f"a{i}", a[i], 0); expect(t, f"b{i}", b[i], 0)
    expect(t, "bc", ls[2], 1); expect(t, "ab", ls[3], 1)

T("W0-L5-04", "Original oder Kopie?", 2, "Objektkarten und Referenzen", ["P2"],
  [txt("Vier Zauberformeln und ein Hauptprogramm. Überlege ohne Gerät!"), code(P4),
   txt("Ausgabe 1: [[a0]] [[a1]] [[a2]] · Ausgabe 2: [[b0]] [[b1]] [[b2]]"),
   txt("Ausgabe 3: [[bc]] · Ausgabe 4: [[ab]]")],
  [gaps({f"{v}{i}": fz() for v in "ab" for i in range(3)}), gaps({"bc": fa(WF), "ab": fa(WF)})],
  [{"a0": ["6"], "a1": ["7"], "a2": ["8"], "b0": ["0"], "b1": ["8"], "b2": ["1"]}, {"bc": ["true"], "ab": ["false"]}],
  [txt("- `plusEins(a)` ändert den Inhalt von `a` → {6, 7, 8}.\n- `plusEinsKopie(a)` legt mit `new` eine **neue** Reihung an → b = {7, 8, 9}, a bleibt.\n"
       "- `ersetze(b)` lenkt nur den lokalen Pfeil `r` um – `b` merkt nichts.\n"
       "- `ersteNull(b)` ändert `b[0]` und gibt **denselben Pfeil** zurück: c und b zeigen auf dieselbe Reihung. Darum ändert `c[2] = 1` auch b → {0, 8, 1}.\n"
       "- `b == c` ist true (gleicher Pfeil), `a == b` false."),
   hin("Falle **P2**: `ersteNull` liefert keine neue Reihung, sondern verändert das Original. Das passiert immer, wenn kein `new` vorkommt.")],
  ["Zeichne für jede Reihung ein Kästchen und für jede Variable einen Pfeil."], c04)

# ---------------------------------------------------------------- 05
ABR = '''public static int[] abgerundet(int[] r) {
    int[] erg = r;
    for (int i = 0; i < r.length; i++) {
        erg[i] = r[i] / 10 * 10;
    }
    return erg;
}'''
ABR_MAIN = 'int[] p = {47, 5, 120}; int[] q = abgerundet(p); out("g2", p[0]); out("g3", q[0]);'

def c05(t):
    o, _ = jrun(ABR, ABR_MAIN)
    expect(t, "g2", o["g2"], 1); expect(t, "g3", o["g3"], 1)
    assert ABR.split("\n")[t["loesung"][0]["zeilen"][0] - 1].strip() == "int[] erg = r;"
    for v in t["loesung"][1]["g1"]:
        o, _ = jrun(ABR.replace("int[] erg = r;", f"int[] erg = {v};"), 'int[] p = {47, 5, 120}; int[] q = abgerundet(p); out("p", arr(p)); out("q", arr(q));')
        assert o == {"p": "47,5,120", "q": "40,0,120"}, o

T("W0-L5-05", "Bug-Hunt: Das abgerundete Lager", 2, "Fehler im Java-Code", ["P2"],
  [txt("`abgerundet(r: Reihung von Ganzzahl): Reihung von Ganzzahl` soll eine **neue** Reihung liefern, in der jeder Wert auf volle Zehner "
       "abgerundet ist (47 → 40). `r` soll unverändert bleiben. Die Methode enthält **genau einen** Fehler."), code(ABR),
   txt("**a)** Wähle die fehlerhafte Zeile."),
   txt("**b)** Korrigiere: `int[] erg = [[g1]];`"),
   txt("Mit dem Fehler gibt `int[] p = {47, 5, 120}; int[] q = abgerundet(p); println(p[0] + \" \" + q[0]);` diese Werte aus: "
       "`p[0]` = [[g2]], `q[0]` = [[g3]]")],
  [lines(1, 1), gaps({"g1": ft(16), "g2": fz(), "g3": fz()})],
  [{"zeilen": [2]}, {"g1": ["new int[r.length]"], "g2": ["40"], "g3": ["40"]}],
  [txt("`int[] erg = r;` legt **keine** neue Reihung an – `erg` und `r` zeigen auf dieselbe. Darum wird das Original überschrieben: "
       "p[0] und q[0] sind beide 40. Richtig ist `new int[r.length]`; dann bleibt p = {47, 5, 120} und q = {40, 0, 120}."),
   hin("Falle **P2**: „liefert eine neue Reihung“ ohne `new` in der Methode – das Original wird zerstört.")],
  ["Wie viele Reihungen gibt es nach Zeile 2?"], c05)

# ---------------------------------------------------------------- 06
WEG = '''public static int abstand(int a, int b) {
    if (a > b) {
        return a - b;
    }
    return b - a;
}
public static int gesamtweg(int[] orte) {
    int weg = 0;
    for (int i = 1; i < orte.length; i++) {
        weg = weg + abstand(orte[i - 1], orte[i]);
    }
    return weg;
}'''

def c06(t):
    inst = WEG.replace("        weg = weg + abstand(orte[i - 1], orte[i]);",
                       "        int rv = abstand(orte[i - 1], orte[i]);\n        weg = weg + rv;\n        System.out.println(\"row=\" + rv + \";\" + weg);")
    o, ls = jrun(inst, 'out("ret", gesamtweg(new int[]{3, 8, 2, 2, 10}));')
    rows = [l[4:].split(";") for l in ls if l.startswith("row=")]
    for k, (rv, w) in enumerate(rows):
        expect(t, f"r{k+1}", rv, 0); expect(t, f"w{k+1}", w, 0)
    expect(t, "ret", o["ret"], 0)
    # Anzahl Aufrufe fuer Laenge n
    o, _ = jrun("static int cnt = 0;\n" + WEG.replace("    if (a > b) {", "    cnt++;\n    if (a > b) {"),
                'boolean ok = true; for (int n = 1; n <= 6; n++) { cnt = 0; gesamtweg(new int[n]); if (cnt != n - 1) ok = false; } out("ok", ok); cnt = 0; gesamtweg(new int[0]); out("leer", cnt);')
    assert o == {"ok": "true", "leer": "0"}, o
    assert t["loesung"][1]["richtig"] == ["b"]

T("W0-L5-06", "Der Weg des Boten", 2, "Tracetabelle", ["P8"],
  [txt("Ein Bote läuft der Reihe nach zu den Orten (Positionen auf einer Straße). `gesamtweg` nutzt die Hilfsmethode `abstand`."), code(WEG),
   txt("**a)** Vervollständige das Aufrufprotokoll für `gesamtweg({3, 8, 2, 2, 10})`."),
   tab(["i", "Aufruf", "Rückgabe", "weg"], [["vor der Schleife", "–", "–", "0"],
       ["1", "abstand(3, 8)", "[[r1]]", "[[w1]]"], ["2", "abstand(8, 2)", "[[r2]]", "[[w2]]"],
       ["3", "abstand(2, 2)", "[[r3]]", "[[w3]]"], ["4", "abstand(2, 10)", "[[r4]]", "[[w4]]"]]),
   txt("Rückgabewert: [[ret]]"),
   txt("**b)** Wie oft wird `abstand` bei einer Reihung der Länge n ≥ 1 aufgerufen?")],
  [gaps({**{f"{c}{k}": fz() for c in "rw" for k in range(1, 5)}, "ret": fz()}),
   choice([("a", "n-mal"), ("b", "(n − 1)-mal"), ("c", "(n + 1)-mal"), ("d", "2 · n-mal")])],
  [{"r1": ["5"], "w1": ["5"], "r2": ["6"], "w2": ["11"], "r3": ["0"], "w3": ["11"], "r4": ["8"], "w4": ["19"], "ret": ["19"]},
   {"richtig": ["b"]}],
  [txt("`abstand` liefert immer den **Betrag** der Differenz. Summe: 5 + 6 + 0 + 8 = 19. Die Schleife beginnt bei 1, weil jeweils der "
       "Vorgänger `orte[i - 1]` gebraucht wird – bei n Orten gibt es n − 1 Wegstücke und damit n − 1 Aufrufe."),
   hin("Falle **P8**: Auch Durchläufe, in denen sich `weg` nicht ändert (Rückgabe 0), gehören ins Protokoll.")],
  ["abstand(8, 2): Welcher Zweig wird ausgeführt?"], c06)

# ---------------------------------------------------------------- 07
BONUS = '''public static int[] mitBonus(int[] r, int bonus, int grenze) {
    int[] neu = [[g1]];
    for (int i = 0; i < [[g2]]; i++) {
        if (r[i] < grenze) {
            neu[i] = [[g3]];
        } else {
            neu[i] = [[g4]];
        }
    }
    return [[g5]];
}'''

def c07(t):
    L = t["loesung"]
    base = {g: L[g][0] for g in L}
    main = 'int[] r = {12, 30, 7, 25}; int[] n = mitBonus(r, 5, 25); out("n", arr(n)); out("r", arr(r)); out("e", mitBonus(new int[0], 1, 1).length);'
    for g in base:
        for v in L[g]:
            m = dict(base); m[g] = v
            o, _ = jrun(fill(BONUS, m), main)
            assert o == {"n": "17,30,12,25", "r": "12,30,7,25", "e": "0"}, (g, v, o)

T("W0-L5-07", "Lückencode: Der Bonuszauber", 3, "Lückencode", ["P2", "P6"],
  [txt("`mitBonus(r: Reihung von Ganzzahl, bonus: Ganzzahl, grenze: Ganzzahl): Reihung von Ganzzahl` liefert eine **neue** Reihung: "
       "Werte unter `grenze` werden um `bonus` erhöht, alle anderen übernommen. Beispiel: `mitBonus({12, 30, 7, 25}, 5, 25)` liefert "
       "`{17, 30, 12, 25}`. `r` bleibt unverändert. Fülle die Lücken (Java-Code)."),
   code(BONUS)],
  gaps({"g1": ft(16), "g2": ft(10), "g3": ft(12), "g4": ft(8), "g5": ft(6)}),
  {"g1": ["new int[r.length]"], "g2": ["r.length", "neu.length"], "g3": ["r[i] + bonus", "bonus + r[i]"], "g4": ["r[i]"], "g5": ["neu"]},
  [txt("Die neue Reihung bekommt dieselbe Länge wie `r`. In der Schleife wird nur **gelesen** aus `r` und **geschrieben** in `neu` – "
       "auch die unveränderten Werte müssen übertragen werden, sonst stünde dort 0. Am Ende wird `neu` zurückgegeben."),
   hin("Falle **P2**: `neu[i] = …` statt `r[i] = …` – sonst wäre das Original verändert. Falle **P6**: Grenze `< r.length`, nicht `<=`.")],
  ["Vergiss den else-Zweig nicht: Was steht sonst in neu[i]?"], c07)

# ---------------------------------------------------------------- 08
O8 = [("h1", "public static void tausche(int[] r, int i, int j) {"),
      ("h2", "    int h = r[i];"),
      ("h3", "    r[i] = r[j];"),
      ("h4", "    r[j] = h;"),
      ("h5", "} // Ende tausche"),
      ("m1", "public static void tauscheNachbarn(int[] r) {"),
      ("m2", "    for (int i = 0; i + 1 < r.length; i = i + 2) {"),
      ("m3", "        tausche(r, i, i + 1);"),
      ("m4", "    } // Ende for"),
      ("m5", "} // Ende tauscheNachbarn"),
      ("d1", "public static void tausche(int a, int b) {"),
      ("d2", "        tausche(r[i], r[i + 1]);"),
      ("d3", "    for (int i = 0; i < r.length; i = i + 2) {"),
      ("d4", "    return r;")]

def c08(t):
    H = ["h1", "h2", "h3", "h4", "h5"]; M = ["m1", "m2", "m3", "m4", "m5"]
    assert t["loesung"]["reihenfolgen"] == [H + M, M + H]
    for seq in t["loesung"]["reihenfolgen"]:
        o, _ = jrun(assemble_order(t, seq), '''int[] a = {1, 2, 3, 4, 5}; tauscheNachbarn(a); out("a", arr(a));
            int[] b = {7, 8}; tauscheNachbarn(b); out("b", arr(b)); int[] c = {}; tauscheNachbarn(c); out("c", c.length);''')
        assert o == {"a": "2,1,4,3,5", "b": "8,7", "c": "0"}, o
    src = assemble_order(t, H + ["m1", "d3", "m3", "m4", "m5"])
    o, _ = jrun(src, 'try { tauscheNachbarn(new int[]{1, 2, 3}); out("x", "ok"); } catch (ArrayIndexOutOfBoundsException e) { out("x", "AIOOBE"); }')
    assert o["x"] == "AIOOBE"
    # Distraktor d1/d2: Wertuebergabe -> keine Wirkung
    o, _ = jrun("public static void tausche(int a, int b) { int h = a; a = b; b = h; }\npublic static void tauscheNachbarn(int[] r) { for (int i = 0; i + 1 < r.length; i = i + 2) { tausche(r[i], r[i + 1]); } }",
                'int[] a = {1, 2}; tauscheNachbarn(a); out("a", arr(a));')
    assert o["a"] == "1,2"

T("W0-L5-08", "Code-Puzzle: Der Paartanz", 3, "Methode implementieren", ["P1", "P6"],
  [txt("`tauscheNachbarn(r: Reihung von Ganzzahl): nichts` vertauscht in `r` jeweils die Paare an den Indizes 0/1, 2/3, 4/5, … "
       "Bei ungerader Länge bleibt das letzte Element stehen: `{1, 2, 3, 4, 5}` wird `{2, 1, 4, 3, 5}`. Schreibe dazu eine Hilfsmethode "
       "`tausche(r: Reihung von Ganzzahl, i: Ganzzahl, j: Ganzzahl): nichts` und verwende sie. Setze **beide** Methoden zusammen "
       "(Reihenfolge der Methoden beliebig) – nicht alle Teile werden gebraucht.")],
  order(O8),
  {"reihenfolgen": [["h1", "h2", "h3", "h4", "h5", "m1", "m2", "m3", "m4", "m5"], ["m1", "m2", "m3", "m4", "m5", "h1", "h2", "h3", "h4", "h5"]]},
  [txt("Die Hilfsmethode bekommt die **Reihung** und zwei Indizes – nur so wirkt der Tausch nach außen (Referenz). Mit "
       "`tausche(int a, int b)` würden nur Kopien der Zahlen vertauscht (Wertübergabe), die Reihung bliebe gleich. "
       "Die Bedingung `i + 1 < r.length` stellt sicher, dass es zu jedem i einen Partner gibt; `i = i + 2` springt zum nächsten Paar. "
       "Beide Methoden sind `void` – kein `return r`."),
   hin("Fallen **P1/P6**: Mit `i < r.length` würde bei ungerader Länge `r[r.length]` gelesen – Absturz.")],
  ["Welche Parameter braucht tausche, damit die Änderung im Original ankommt?"], c08)

LEVEL5["aufgaben"] = [k for k in ORDER if k.startswith("W0-L5-")]
