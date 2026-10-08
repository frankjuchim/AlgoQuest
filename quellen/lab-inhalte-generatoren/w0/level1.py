# Level 0.1 – Das Portal (DS 1): Notation fuers Abitur, Tracen, Struktogramm lesen
from lib import *

LEVEL1 = {
    "id": "W0-L1", "nr": "0.1", "titel": "Das Portal: Notation fürs Abitur", "ds": [1],
    "ab": "AB 1 „Das Portal“, Teil B (Notations-Referenz) und Aufgaben 4–7",
    "ide": "AQ_W0_L0_Diagnose_Geruest.txt – Level 0 „Diagnose“ (Klasse Diagnose; Testklassen DiagnoseBasisTest, DiagnoseErweiterungTest, DiagnoseExperteTest)",
    "intro": [
        txt("Im Abitur gibt es keinen Compiler: Signaturen, Struktogramme und Tracetabellen schreibst du **von Hand**. "
            "Das Portal prüft, ob du die Notation der Ergänzenden Hinweise (EH 2025) sicher liest."),
        hin("**Merke:** Signatur `name(p: Typ): Rückgabetyp` · Typnamen Ganzzahl, Kommazahl, Wahrheitswert, Zeichen, "
            "Zeichenkette, nichts, Reihung von … · Struktogramm: Zuweisung mit ←, Vergleich mit =, „gib … zurück“ beendet die Methode · "
            "Tracetabelle: eine Spalte je Variable, neue Zeile bei jeder Änderung."),
    ],
    "aufgaben": [],
}

# ---------------------------------------------------------------- 01
def c01(t):
    m = {"int": "Ganzzahl", "double": "Kommazahl", "boolean": "Wahrheitswert", "char": "Zeichen",
         "String": "Zeichenkette", "int[]": "Reihung von Ganzzahl", "void": "nichts", "String[]": "Reihung von Zeichenkette"}
    el = {e["id"]: e["md"].strip("`") for e in t["interaktion"]["elemente"]}
    ka = {k["id"]: k["md"] for k in t["interaktion"]["kategorien"]}
    for e, k in t["loesung"].items():
        assert m[el[e]] == ka[k], (el[e], ka[k])
    # Typen in Java gueltig?
    ok, err = jcompile("static void f() { int a = 1; double b = 1.5; boolean c = true; char d = 'x'; String e = \"x\"; int[] g = {1}; String[] h = {\"x\"}; }")
    assert ok, err

T("W0-L1-01", "Typnamen-Übersetzer", 1, "Methodenkopf und Signatur", ["P3"],
  [txt("Ordne jedem Java-Typ den **Typnamen aus dem Abitur** zu (EH 2025).")],
  match([("e1", "`int`"), ("e2", "`double`"), ("e3", "`boolean`"), ("e4", "`char`"), ("e5", "`String`"),
         ("e6", "`int[]`"), ("e7", "`void`"), ("e8", "`String[]`")],
        [("k1", "Ganzzahl"), ("k2", "Kommazahl"), ("k3", "Wahrheitswert"), ("k4", "Zeichen"), ("k5", "Zeichenkette"),
         ("k6", "Reihung von Ganzzahl"), ("k7", "nichts"), ("k8", "Reihung von Zeichenkette")]),
  {"e1": "k1", "e2": "k2", "e3": "k3", "e4": "k4", "e5": "k5", "e6": "k6", "e7": "k7", "e8": "k8"},
  [txt("Die Abi-Typnamen sind deutsch und sprachunabhängig. `void` heißt **nichts** (keine Rückgabe), "
       "eine Reihung heißt immer **Reihung von …** – nie „Array“. `char` (ein Zeichen, einfache Anführungszeichen) und "
       "`String` (Zeichenkette, doppelte Anführungszeichen) sind verschiedene Typen."),
   hin("Falle **P3** (Signatur verfehlt): Wer die Typnamen verwechselt, schreibt einen falschen Methodenkopf.")],
  ["Ein Zeichen steht in einfachen, eine Zeichenkette in doppelten Anführungszeichen."], c01)

# ---------------------------------------------------------------- 02
def c02(t):
    o, _ = jrun("", '''
        String s = "Zauberer";
        out("g1", s.length()); out("g2", s.charAt(3)); out("g3", s.substring(2, 5));
        out("g4", s.contains("ber")); out("g5", (int) s.charAt(0));
        int c1 = "Zauberer".compareTo("Zauberin"); int c2 = "zauber".compareTo("Zauber"); int c3 = "Elf".compareTo("Elfe");
        out("g6", c1 < 0 ? "negativ" : c1 == 0 ? "0" : "positiv");
        out("g7", c2 < 0 ? "negativ" : c2 == 0 ? "0" : "positiv");
        out("g8", c3 < 0 ? "negativ" : c3 == 0 ? "0" : "positiv");
    ''')
    for g, v in o.items(): expect(t, g, v)

NPZ = ["negativ", "0", "positiv"]
T("W0-L1-02", "Die Inschrift am Portal", 1, "Datentypen und Ausdrücke", ["P5"],
  [txt("Am Portal steht `String s = \"Zauberer\";`. Gib den Wert jedes Ausdrucks an. "
       "Zeichen und Zeichenketten schreibst du **ohne** Anführungszeichen, Wahrheitswerte als `true`/`false`."),
   tab(["Ausdruck", "Wert"], [
       ["`s.length()`", "[[g1]]"], ["`s.charAt(3)`", "[[g2]]"], ["`s.substring(2, 5)`", "[[g3]]"],
       ["`s.contains(\"ber\")`", "[[g4]]"], ["`(int) s.charAt(0)`", "[[g5]]"],
       ["`\"Zauberer\".compareTo(\"Zauberin\")`", "[[g6]]"], ["`\"zauber\".compareTo(\"Zauber\")`", "[[g7]]"],
       ["`\"Elf\".compareTo(\"Elfe\")`", "[[g8]]"]]),
   hin("ASCII-Werte: 'A' = 65, 'Z' = 90, 'a' = 97, 'z' = 122.")],
  gaps({"g1": fz(), "g2": ft(4), "g3": ft(8), "g4": fa(WF), "g5": fz(), "g6": fa(NPZ), "g7": fa(NPZ), "g8": fa(NPZ)}),
  {"g1": ["8"], "g2": ["b", "'b'"], "g3": ["ube", "\"ube\""], "g4": ["true"], "g5": ["90"],
   "g6": ["negativ"], "g7": ["positiv"], "g8": ["negativ"]},
  [txt("- `length()` zählt die Zeichen: Z-a-u-b-e-r-e-r = 8.\n- Der Index beginnt bei 0: Index 3 ist 'b'.\n"
       "- `substring(2, 5)` liefert die Zeichen mit Index 2, 3, 4 (das Ende ist **ausschließlich**): \"ube\".\n"
       "- `contains(\"ber\")` ist wahr, „ber“ steht ab Index 3.\n- `(int) 'Z'` liefert den ASCII-Wert 90.\n"
       "- `compareTo` vergleicht Zeichen für Zeichen: Bei Index 6 steht 'e' (101) gegen 'i' (105) → negativ. "
       "'z' (122) kommt nach 'Z' (90) → positiv. „Elf“ ist ein echter Anfang von „Elfe“ und damit kürzer → negativ."),
   hin("Alle diese Operationen sind im Abitur **erlaubt**. Falle **P5**: Zeichenketten vergleichst du mit `equals` bzw. `compareTo`, nie mit `==`.")],
  ["substring(a, b): a einschließlich, b ausschließlich."], c02)

# ---------------------------------------------------------------- 03
def c03(t):
    # erlaubte Operationen kompilieren alle; Liste gegen EH-Liste
    erlaubt = {"a", "b", "c", "d", "e", "f"}
    assert set(t["loesung"]["richtig"]) == erlaubt
    ok, err = jcompile("static void f(String s, String u) { int a = s.length(); char b = s.charAt(0); String c = s.substring(0, 1); boolean d = s.equals(u); boolean e = s.contains(u); int f = s.compareTo(u); }")
    assert ok, err

T("W0-L1-03", "Erlaubt oder verboten?", 1, "Datentypen und Ausdrücke", ["P5"],
  [txt("Die Liste der Zeichenketten-Operationen im Abitur ist **abschließend**. Wähle **alle** Operationen, die du verwenden darfst.")],
  choice([("a", "`s.length()`"), ("b", "`s.charAt(i)`"), ("c", "`s.substring(a, b)`"), ("d", "`s.equals(t)`"),
          ("e", "`s.contains(t)`"), ("f", "`s.compareTo(t)`"), ("g", "`s.toUpperCase()`"), ("h", "`s.indexOf(t)`"),
          ("i", "`s.split(\" \")`"), ("j", "`s.trim()`")], mehrfach=True),
  {"richtig": ["a", "b", "c", "d", "e", "f"]},
  [txt("Erlaubt sind (EH 2025): Länge, Zeichen an Position, Teilzeichenkette, Verketten mit `+`, Gleichheit (`equals`), "
       "enthält Teilzeichenkette (`contains`), lexikographischer Vergleich (`compareTo`) und ASCII-Wert ↔ Zeichen per Cast. "
       "`toUpperCase`, `indexOf`, `split`, `trim` usw. sind **nicht** erlaubt – du baust sie mit Schleife und `charAt` selbst nach."),
   hin("Falle **P5**: nicht erlaubte String-Operationen kosten im Abitur BE – auch wenn die Online-IDE sie ausführt.")],
  ["Es sind genau sechs."], c03)

# ---------------------------------------------------------------- 04
RAETSEL = sg("raetsel(r: Reihung von Ganzzahl): Ganzzahl", [
    A("z ← 0"),
    Z("i von 1 bis Länge von r − 1", [W("r[i] < r[i − 1]", [A("z ← z + 1")])]),
    G("z")])

def c04(t):
    o, lines_ = jrun('''
        static int raetsel(int[] r) {
            int z = 0;
            for (int i = 1; i <= r.length - 1; i++) {
                boolean b = r[i] < r[i - 1];
                if (b) { z = z + 1; }
                System.out.println("row=" + i + ";" + (b ? "w" : "f") + ";" + z);
            }
            return z;
        }''', 'out("ret", raetsel(new int[]{6, 2, 8, 5, 5, 1}));')
    rows = [l[4:].split(";") for l in lines_ if l.startswith("row=")]
    for k, (i, b, z) in enumerate(rows):
        expect(t, f"b{k+1}", b, 0); expect(t, f"z{k+1}", z, 0)
    expect(t, "ret", o["ret"], 0)

T("W0-L1-04", "Das Rätsel am Portaltor", 2, "Struktogramm lesen", ["P8"],
  [txt("In das Portaltor ist dieses Struktogramm eingeritzt."), RAETSEL,
   txt("**a)** Vervollständige die Tracetabelle für den Aufruf mit `r = {6, 2, 8, 5, 5, 1}` (eine Zeile pro Durchlauf; "
       "w/f = Wert der Bedingung, z = Wert **nach** dem Durchlauf)."),
   tab(["i", "r[i − 1]", "r[i]", "r[i] < r[i − 1]", "z"], [
       ["vor der Schleife", "–", "–", "–", "0"],
       ["1", "6", "2", "[[b1]]", "[[z1]]"], ["2", "2", "8", "[[b2]]", "[[z2]]"], ["3", "8", "5", "[[b3]]", "[[z3]]"],
       ["4", "5", "5", "[[b4]]", "[[z4]]"], ["5", "5", "1", "[[b5]]", "[[z5]]"]]),
   txt("Rückgabewert: [[ret]]"),
   txt("**b)** Beschreibe, was `raetsel` allgemein berechnet.")],
  [gaps({**{f"b{k}": fa(WFS) for k in range(1, 6)}, **{f"z{k}": fz() for k in range(1, 6)}, "ret": fz()}),
   choice([("a", "die Anzahl der Stellen, an denen ein Wert kleiner ist als sein Vorgänger"),
           ("b", "die Anzahl der Werte, die kleiner sind als `r[0]`"),
           ("c", "den Index des kleinsten Werts"),
           ("d", "die Anzahl der verschiedenen Werte in `r`")])],
  [{"b1": ["w"], "z1": ["1"], "b2": ["f"], "z2": ["1"], "b3": ["w"], "z3": ["2"], "b4": ["f"], "z4": ["2"],
    "b5": ["w"], "z5": ["3"], "ret": ["3"]},
   {"richtig": ["a"]}],
  [txt("Die Zählschleife beginnt bei **1**, weil jedes Element mit seinem Vorgänger `r[i − 1]` verglichen wird. "
       "Bei 5 < 5 ist die Bedingung **falsch** (gleich ist nicht kleiner). Gezählt werden die Abstiege 6→2, 8→5 und 5→1: Rückgabe 3."),
   hin("Falle **P8**: Trage in jede Zeile den Wert **nach** dem Durchlauf ein und vergiss den Rückgabewert nicht.")],
  ["Vergleiche jeweils die beiden Nachbarn in der Zeile."], c04)

# ---------------------------------------------------------------- 05
AUSDAUER = '''public static int ausdauer(int[] etappe, int kraft) {
    int i = 0;
    while (i < etappe.length && kraft >= etappe[i]) {
        kraft = kraft - etappe[i];
        i++;
    }
    return i;
}'''

def c05(t):
    o, lines_ = jrun(AUSDAUER.replace("    return i;", "    return i;").replace(
        "    while (i < etappe.length && kraft >= etappe[i]) {",
        '    System.out.println("row=" + i + ";" + kraft + ";" + ((i < etappe.length && kraft >= etappe[i]) ? "w" : "f"));\n'
        "    while (i < etappe.length && kraft >= etappe[i]) {").replace(
        "        i++;\n",
        '        i++;\n        System.out.println("row=" + i + ";" + kraft + ";" + ((i < etappe.length && kraft >= etappe[i]) ? "w" : "f"));\n'),
        'out("ret", ausdauer(new int[]{4, 3, 6, 2}, 12)); out("r20", ausdauer(new int[]{4, 3, 6, 2}, 20)); out("r0", ausdauer(new int[]{}, 5));')
    rows = [l[4:].split(";") for l in lines_ if l.startswith("row=")]
    rows = rows[:3]  # erster Aufruf
    for k, (i, kr, b) in enumerate(rows):
        expect(t, f"i{k}", i); expect(t, f"k{k}", kr); expect(t, f"b{k}", b)
    for g in ("ret", "r20", "r0"): expect(t, g, o[g])

T("W0-L1-05", "Die Ausdauer der Heldin", 2, "Tracetabelle", ["P8", "P1"],
  [txt("Eine Heldin läuft Etappen ab, solange ihre Kraft reicht."), code(AUSDAUER),
   txt("**a)** Vervollständige die Tracetabelle für `ausdauer({4, 3, 6, 2}, 12)`. Die Spalte „Bedingung“ enthält den Wert der "
       "Schleifenbedingung mit den Werten **dieser** Zeile (w/f)."),
   tab(["Zeitpunkt", "i", "kraft", "Bedingung"], [
       ["vor der Schleife", "[[i0]]", "[[k0]]", "[[b0]]"],
       ["nach Durchlauf 1", "[[i1]]", "[[k1]]", "[[b1]]"],
       ["nach Durchlauf 2", "[[i2]]", "[[k2]]", "[[b2]]"]]),
   txt("Rückgabewert: [[ret]]"),
   txt("**b)** Gib die Rückgabewerte an: `ausdauer({4, 3, 6, 2}, 20)` liefert [[r20]], `ausdauer({}, 5)` liefert [[r0]].")],
  gaps({"i0": fz(), "k0": fz(), "b0": fa(WFS), "i1": fz(), "k1": fz(), "b1": fa(WFS), "i2": fz(), "k2": fz(), "b2": fa(WFS),
        "ret": fz(), "r20": fz(), "r0": fz()}),
  {"i0": ["0"], "k0": ["12"], "b0": ["w"], "i1": ["1"], "k1": ["8"], "b1": ["w"], "i2": ["2"], "k2": ["5"], "b2": ["f"],
   "ret": ["2"], "r20": ["4"], "r0": ["0"]},
  [txt("Nach zwei Etappen ist die Kraft 5 < 6 – die Bedingung wird falsch, Rückgabe 2. Mit Kraft 20 reicht es für alle vier "
       "Etappen (4 + 3 + 6 + 2 = 15): Dann ist `i = 4` und schon `i < etappe.length` ist falsch."),
   hin("`&&` wertet von links aus und hört auf, sobald das Ergebnis feststeht. Darum wird `etappe[4]` **nie** gelesen – "
       "die Indexprüfung steht absichtlich zuerst (Falle **P1**). Bei der leeren Reihung läuft die Schleife gar nicht: Rückgabe 0.")],
  ["Prüfe in jeder Zeile beide Teilbedingungen."], c05)

# ---------------------------------------------------------------- 06
O6 = [("p1", "public static int zaehleGroesser(int[] r, int x) {"),
      ("p2", "    int anzahl = 0;"),
      ("p3", "    for (int w : r) {"),
      ("p4", "        if (w > x) {"),
      ("p5", "            anzahl = anzahl + 1;"),
      ("p6", "        } // Ende if"),
      ("p7", "    } // Ende for"),
      ("p8", "    return anzahl;"),
      ("p9", "} // Ende Methode"),
      ("d1", "public static void zaehleGroesser(int[] r, int x) {"),
      ("d2", "        if (w >= x) {"),
      ("d3", "    int anzahl ← 0;"),
      ("d4", "    for (int w = 0; w <= r.length; w++) {")]

def c06(t):
    for seq in t["loesung"]["reihenfolgen"]:
        src = assemble_order(t, seq)
        o, _ = jrun(src, 'out("a", zaehleGroesser(new int[]{4, 9, 2, 7, 7}, 6)); out("b", zaehleGroesser(new int[]{}, 0)); out("c", zaehleGroesser(new int[]{6, 6}, 6));')
        assert o == {"a": "3", "b": "0", "c": "0"}, o
    # Distraktoren fuehren zu Fehlern
    ok, _ = jcompile(assemble_order(t, ["p1", "d3", "p3", "p4", "p5", "p6", "p7", "p8", "p9"])); assert not ok
    ok, _ = jcompile(assemble_order(t, ["d1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9"])); assert not ok

T("W0-L1-06", "Code-Puzzle: Vom Bauplan zum Code", 2, "Code ↔ Struktogramm", ["P9", "P3"],
  [txt("Setze die Java-Methode zum Struktogramm aus den Teilen zusammen. Nicht alle Teile werden gebraucht."),
   sg("zaehleGroesser(r: Reihung von Ganzzahl, x: Ganzzahl): Ganzzahl", [
       A("anzahl ← 0"), Z("jedes w in r", [W("w > x", [A("anzahl ← anzahl + 1")])]), G("anzahl")])],
  order(O6),
  {"reihenfolgen": [["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9"]]},
  [txt("„für jedes w in r“ wird zur for-each-Schleife `for (int w : r)`. Der Rückgabetyp Ganzzahl wird `int` (nicht `void`), "
       "die Bedingung heißt **echt größer** (`>`). Die Rückgabe steht **nach** der Schleife."),
   hin("Falle **P9**: Der Pfeil ← gehört ins Struktogramm, in Java steht `=`. Falle **P3**: `void` passt nicht zur Signatur mit Rückgabetyp Ganzzahl.")],
  ["Beginne mit dem Kopf: Der Rückgabetyp steht in Java vorn."], c06)

# ---------------------------------------------------------------- 07
PAL = '''public static boolean istPalindrom(String s) {
    for (int i = 0; i < s.length() / 2; i++) {
        if (s.charAt(i) != s.charAt(s.length() - i)) {
            return false;
        }
    }
    return true;
}'''
PAL_FIX = "if (s.charAt(i) != s.charAt([[g1]])) {"

def c07(t):
    o, _ = jrun(PAL, '''
        try { out("otto", istPalindrom("otto")); } catch (StringIndexOutOfBoundsException e) { out("otto", "StringIndexOutOfBoundsException"); }
        out("leer", istPalindrom(""));''')
    expect(t, "g2", o["otto"], 1)
    lines_src = PAL.split("\n")
    assert lines_src[t["loesung"][0]["zeilen"][0] - 1].strip().startswith("if (s.charAt(i) != s.charAt(s.length() - i))")
    for var in t["loesung"][1]["g1"]:
        fixed = PAL.replace("s.charAt(s.length() - i)", f"s.charAt({var})")
        o, _ = jrun(fixed, 'out("r", "" + istPalindrom("otto") + istPalindrom("anna") + istPalindrom("abc") + istPalindrom("") + istPalindrom("x") + istPalindrom("abca") + istPalindrom("radar"));')
        assert o["r"] == "truetruefalsetruetruefalsetrue", (var, o)

T("W0-L1-07", "Bug-Hunt: Der Spiegel am Portal", 3, "Fehler im Java-Code", ["P1", "P6"],
  [txt("Die Methode soll `true` liefern, wenn `s` vorwärts und rückwärts gleich gelesen wird (exakter Zeichenvergleich). "
       "Sie enthält **genau einen** Fehler."), code(PAL),
   txt("**a)** Wähle die fehlerhafte Zeile."),
   txt("**b)** Korrigiere die Zeile (nur den Index, in Java-Schreibweise):"), code(PAL_FIX, nummern=False),
   txt("Was passiert beim Aufruf `istPalindrom(\"otto\")` **mit** dem Fehler? [[g2]]")],
  [lines(1, 1), gaps({"g1": ft(18), "g2": fa(["liefert true", "liefert false", "StringIndexOutOfBoundsException"])})],
  [{"zeilen": [3]},
   {"g1": ["s.length() - 1 - i", "s.length() - i - 1", "s.length() - (i + 1)", "(s.length() - 1) - i"],
    "g2": ["StringIndexOutOfBoundsException"]}],
  [txt("Das Gegenstück zu Index `i` ist `s.length() - 1 - i`: Für i = 0 ist es das **letzte** Zeichen mit Index "
       "`s.length() - 1`. Mit `s.length() - i` wird schon im ersten Durchlauf Index 4 von „otto“ gelesen – den gibt es nicht."),
   hin("Falle **P6** (Off-by-one) führt hier zu Falle **P1** (Laufzeitfehler). Prüfe immer den ersten und den letzten Durchlauf.")],
  ["Welchen Index hat das letzte Zeichen einer Zeichenkette der Länge 4?"], c07)

# ---------------------------------------------------------------- 08
PUNKTE_J = '''public static int punkte(int[] wuerfe) {
    int p = 0;
    for (int w : wuerfe) {
        if (w % 2 == 0) {
            p = p + w;
        } else {
            p = p - 1;
        }
    }
    return p;
}'''

def c08(t):
    o, _ = jrun(PUNKTE_J, 'out("w", punkte(new int[]{4, 3, 6, 1, 5}));')
    expect(t, "w", o["w"], 1)

T("W0-L1-08", "Bauplan aus Code", 3, "Code ↔ Struktogramm", ["P9"],
  [txt("Übersetze die Methode in ein Struktogramm nach EH § 5, indem du die Lücken füllst."), code(PUNKTE_J),
   sg("[[k]]", [
       A("p ← 0"),
       Z("jedes [[v]] in wuerfe", [W("[[b]]", [A("[[d]]")], [A("p ← p − 1")])]),
       G("[[r]]")]),
   txt("**b)** Gib den Rückgabewert für die Würfe `{4, 3, 6, 1, 5}` an: [[w]]")],
  [gaps({"k": fa(["punkte(wuerfe: Reihung von Ganzzahl): Ganzzahl", "int punkte(int[] wuerfe)",
                  "punkte(wuerfe: Ganzzahl): Reihung von Ganzzahl", "punkte(Reihung von Ganzzahl): Ganzzahl"]),
         "v": ft(4),
         "b": fa(["w % 2 = 0", "w % 2 == 0", "w % 2 ← 0", "w / 2 = 0"]),
         "d": fa(["p ← p + w", "p = p + w", "p + w", "gib p + w zurück"]),
         "r": ft(6)}),
   gaps({"w": fz()})],
  [{"k": ["punkte(wuerfe: Reihung von Ganzzahl): Ganzzahl"], "v": ["w"], "b": ["w % 2 = 0"], "d": ["p ← p + w"], "r": ["p"]},
   {"w": ["7"]}],
  [txt("Der Kopf enthält die **Signatur** (Name, Parameter mit Typ, Rückgabetyp). Im Struktogramm wird mit `=` verglichen "
       "und mit `←` zugewiesen; „gib p zurück“ steht nach der Schleife. Wert: 4 − 1 + 6 − 1 − 1 = 7."),
   hin("Falle **P9**: Java-Syntax (`==`, `=` als Zuweisung, `int[]`) hat im Struktogramm nichts zu suchen.")],
  ["Struktogramm: = vergleicht, ← weist zu."], c08)

LEVEL1["aufgaben"] = [k for k in ORDER if k.startswith("W0-L1-")]
