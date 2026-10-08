# Level 0.4 – Die Zauberschule I (DS 4): Methoden bauen und aufrufen, Signatur <-> Kopf, return, Aufrufprotokoll
from lib import *

LEVEL4 = {
    "id": "W0-L4", "nr": "0.4", "titel": "Die Zauberschule: Eigene Methoden", "ds": [4],
    "ab": "AB 4 „Die Zauberschule“, Teil 1 (Infoteile 1–6, Aufgaben 0–7)",
    "ide": "AQ_W0_Akademie_Geruest.txt – Level 0.4 (Klasse Zauber, Testklasse L04ZauberTest; Köpfe für Erweiterung/Experte selbst schreiben)",
    "intro": [
        txt("Jede Zauberformel hat einen **Namen**, braucht **Zutaten** (Parameter) und hat eine **Wirkung** (Rückgabewert). "
            "Im Abitur ist jede Implementierung eine Methode mit vorgegebener Signatur."),
        hin("**Merke:** `name(a: Ganzzahl, s: Zeichenkette): Wahrheitswert` ⟷ `public static boolean name(int a, String s)` · "
            "Rückgabetyp wandert nach vorn, „nichts“ wird `void` · jeder Parameter mit eigenem Typ · `return` beendet die Methode, "
            "**jeder** Ablauf braucht ein `return` · Argumente werden der Reihe nach in die Parameter kopiert."),
    ],
    "aufgaben": [],
}

# ---------------------------------------------------------------- 01
KOPF1 = "public static String runenName(int nr, boolean gross, char trenner)"
ABI_T = ["Ganzzahl", "Kommazahl", "Wahrheitswert", "Zeichen", "Zeichenkette", "nichts"]

def c01(t):
    ok, err = jcompile(KOPF1 + ' { return ""; }', 'String x = runenName(3, true, \'-\');'); assert ok, err
    ok, _ = jcompile(KOPF1 + ' { return ""; }', 'String x = runenName(3, true, "-");'); assert not ok   # 3. Parameter ist char

T("W0-L4-01", "Den Kopf zerlegen", 1, "Methodenkopf und Signatur", ["P3"],
  [txt("Gegeben ist der Methodenkopf"), code(KOPF1, nummern=False),
   tab(["Name", "Rückgabetyp (Abi)", "Anzahl Parameter", "Typ des 3. Parameters (Abi)"], [["[[g1]]", "[[g2]]", "[[g3]]", "[[g4]]"]])],
  gaps({"g1": ft(12), "g2": fa(ABI_T), "g3": fz(), "g4": fa(ABI_T)}),
  {"g1": ["runenName"], "g2": ["Zeichenkette"], "g3": ["3"], "g4": ["Zeichen"]},
  [txt("Vor dem Namen steht der Rückgabetyp `String` = Zeichenkette. In den Klammern stehen drei Parameter, jeder mit Typ und Name; "
       "der dritte ist `char trenner` = Zeichen. Signatur: `runenName(nr: Ganzzahl, gross: Wahrheitswert, trenner: Zeichen): Zeichenkette`.")],
  ["Der Rückgabetyp steht in Java direkt vor dem Namen."], c01)

# ---------------------------------------------------------------- 02
SIG2A = "zaehleUeber(r: Reihung von Kommazahl, grenze: Kommazahl): Ganzzahl"
OPT2A = [("a", "public static int zaehleUeber(double[] r, double grenze)"),
         ("b", "public static int zaehleUeber(double[] r, grenze)"),
         ("c", "public static zaehleUeber(double[] r, double grenze): int"),
         ("d", "public static double zaehleUeber(double[] r, double grenze)"),
         ("e", "public static int zaehleUeber(double grenze, double[] r)")]
SIG2B = "public static void markiere(String[] namen, int pos, char z)"
OPT2B = [("a", "markiere(namen: Reihung von Zeichenkette, pos: Ganzzahl, z: Zeichen): nichts"),
         ("b", "markiere(namen: Zeichenkette, pos: Ganzzahl, z: Zeichen): nichts"),
         ("c", "markiere(namen: Reihung von Zeichenkette, pos: Ganzzahl, z: Zeichen)"),
         ("d", "void markiere(namen: Reihung von Zeichenkette, pos: Ganzzahl, z: Zeichen)"),
         ("e", "markiere(namen: Reihung von Zeichenkette, pos: Ganzzahl, z: Zeichenkette): nichts")]

def c02(t):
    res = {}
    for k, kopf in OPT2A:
        ok, _ = jcompile(kopf + " { return 0; }", "double[] r = {1.5}; int n = zaehleUeber(r, 1.0);")
        res[k] = ok
    assert [k for k, v in res.items() if v] == t["loesung"][0]["richtig"], res
    ok, err = jcompile(SIG2B + " { }", 'String[] n = {"a"}; markiere(n, 0, \'x\');'); assert ok, err

T("W0-L4-02", "Das Übersetzungsbüro", 1, "Methodenkopf und Signatur", ["P3"],
  [txt(f"**a)** Welcher Java-Methodenkopf passt zur Signatur `{SIG2A}`?")] +
  [txt(f"**b)** Welche Signatur in Abi-Notation passt zum Kopf `{SIG2B}`?")],
  [choice([(k, f"`{v}`") for k, v in OPT2A]), choice([(k, f"`{v}`") for k, v in OPT2B])],
  [{"richtig": ["a"]}, {"richtig": ["a"]}],
  [txt("Übersetzungsregeln: Rückgabetyp nach vorn (Abi: hinten nach dem Doppelpunkt), jeder Parameter „Typ Name“ ohne Doppelpunkt, "
       "Reihenfolge der Parameter bleibt, `void` = nichts. Die Abi-Signatur nennt **immer** den Rückgabetyp – auch „nichts“."),
   hin("Falle **P3**: Vertauschte Parameter, fehlende Typen oder ein falscher Rückgabetyp kosten im Abitur BE.")],
  ["Prüfe Rückgabetyp, Parameterreihenfolge und jeden Parametertyp einzeln."], c02)

# ---------------------------------------------------------------- 03
HEADS3 = [("e1", "public static void leere(int[] r)", "k1"),
          ("e2", "public static int[] leere(int r)", "k2"),
          ("e3", "public static boolean leere(String r)", "k3"),
          ("e4", "public static char leere(String[] r)", "k4"),
          ("e5", "public static double leere(int r, double s)", "k5")]
SIGS3 = [("k1", "leere(r: Reihung von Ganzzahl): nichts"), ("k2", "leere(r: Ganzzahl): Reihung von Ganzzahl"),
         ("k3", "leere(r: Zeichenkette): Wahrheitswert"), ("k4", "leere(r: Reihung von Zeichenkette): Zeichen"),
         ("k5", "leere(r: Ganzzahl, s: Kommazahl): Kommazahl"), ("k6", "leere(r: Kommazahl, s: Ganzzahl): Kommazahl")]

def c03(t):
    J = {"Ganzzahl": "int", "Kommazahl": "double", "Wahrheitswert": "boolean", "Zeichen": "char", "Zeichenkette": "String", "nichts": "void"}
    def tj(x): return J[x[len("Reihung von "):]] + "[]" if x.startswith("Reihung von ") else J[x]
    def sig2head(s):
        name, rest = s.split("(", 1); params, ret = rest.rsplit("): ", 1)
        ps = ", ".join(f"{tj(p.split(': ')[1])} {p.split(': ')[0]}" for p in params.split(", "))
        return f"public static {tj(ret)} {name}({ps})"
    sigs = dict(SIGS3)
    for e, h, k in HEADS3:
        assert sig2head(sigs[t["loesung"][e]]) == h, (h, sig2head(sigs[t["loesung"][e]]))

T("W0-L4-03", "Fünf Köpfe, ein Name", 1, "Methodenkopf und Signatur", ["P3"],
  [txt("Alle fünf Methoden heißen `leere`. Ordne jedem Java-Methodenkopf die passende Abi-Signatur zu. Eine Signatur bleibt übrig.")],
  match([(e, f"`{h}`") for e, h, _k in HEADS3], [(k, f"`{s}`") for k, s in SIGS3]),
  {e: k for e, _h, k in HEADS3},
  [txt("Lies **beide** Seiten vollständig: Rückgabetyp, Anzahl, Reihenfolge und Typen der Parameter. `int[]` ist eine Reihung von Ganzzahl, "
       "`String[]` eine Reihung von Zeichenkette. Die Signatur `leere(r: Kommazahl, s: Ganzzahl): Kommazahl` hat die Parametertypen in "
       "umgekehrter Reihenfolge – sie passt zu keinem Kopf.")],
  ["Beginne mit dem Rückgabetyp – er unterscheidet die meisten Köpfe."], c03)

# ---------------------------------------------------------------- 04
ALCH = '''public static int preis(int menge) {           // menge * 4
    return menge * 4;
}
public static boolean reicht(int gold, int kosten) {
    return gold >= kosten;
}
public static String etikett(String name, int menge) {
    return name + " x" + menge;
}'''
ST4 = [("A", "int p = Alchemie.preis(3) + Alchemie.preis(2);", "ok"),
       ("B", "String e = Alchemie.etikett(2, \"Salbe\");", "fehler"),
       ("C", "boolean b = Alchemie.reicht(Alchemie.preis(5), 20);", "ok"),
       ("D", "int z = Alchemie.etikett(\"Salbe\", 1);", "fehler"),
       ("E", "double d = Alchemie.preis(7);", "ok"),
       ("F", "int y = Alchemie.preis(1.5);", "fehler"),
       ("G", "Alchemie.reicht(10);", "fehler"),
       ("H", "println(Alchemie.etikett(\"Elixier\", Alchemie.preis(2)));", "ok")]

def c04(t):
    extra = "class Alchemie {\n" + ALCH.replace("public static", "    public static") + "\n}"
    for k, s, sol in ST4:
        ok, _ = jcompile("", s, extra)
        assert ok == (t["loesung"][0][k] == "ok"), (k, ok)
    o, ls = jrun("", 'int p = Alchemie.preis(3) + Alchemie.preis(2); out("pa", p); boolean b = Alchemie.reicht(Alchemie.preis(5), 20); out("pc", b);'
                 'double d = Alchemie.preis(7); out("pe", d); out("ph", Alchemie.etikett("Elixier", Alchemie.preis(2)));', extra)
    for g, v in o.items(): expect(t, g, v, 1)

T("W0-L4-04", "Passt die Zutat?", 2, "Methodenkopf und Signatur", ["P3", "P4"],
  [txt("Die Klasse `Alchemie` enthält drei Klassenoperationen:"), code(ALCH),
   txt("**a)** Entscheide für jede Anweisung im Hauptprogramm, ob der Compiler sie akzeptiert."),
   txt("**b)** Gib die Werte bzw. die Ausgabe der akzeptierten Anweisungen an (Zeichenketten ohne Anführungszeichen): "
       "p in A: [[pa]] · b in C: [[pc]] · d in E: [[pe]] · Ausgabe von H: [[ph]]")],
  [match([(k, f"**{k}** `{s}`") for k, s, _x in ST4], [("ok", "akzeptiert"), ("fehler", "Compilerfehler")]),
   gaps({"pa": fz(), "pc": fa(WF), "pe": fz(), "ph": ft(14)})],
  [{k: x for k, _s, x in ST4}, {"pa": ["20"], "pc": ["true"], "pe": ["28.0"], "ph": ["Elixier x8", "\"Elixier x8\""]}],
  [txt("- B: Argumente in falscher Reihenfolge (Ganzzahl an Zeichenkette-Parameter).\n- D: Rückgabe Zeichenkette passt nicht in `int`.\n"
       "- F: Eine Kommazahl darf nicht an einen Ganzzahl-Parameter übergeben werden (umgekehrt schon).\n- G: Es fehlt ein Argument.\n"
       "- E: Ganzzahl → Kommazahl ist erlaubt, d = 28.0.\n- C: `preis(5)` = 20, und 20 ≥ 20 ist wahr.\n"
       "- H: `preis(2)` = 8 ist Argument von `etikett` → \"Elixier x8\"."),
   hin("Falle **P3/P4**: Anzahl, Reihenfolge und Typen der Argumente müssen zu den Parametern passen.")],
  ["Prüfe jeden Aufruf: Anzahl der Argumente, Typen in der richtigen Reihenfolge, passt der Rückgabetyp zur Variablen?"], c04)

# ---------------------------------------------------------------- 05
M5 = [("M1", '''public static int vorzeichen(int n) {
    if (n >= 0) {
        return 1;
    } else {
        return -1;
    }
}''', "ok"),
      ("M2", '''public static String note(int p) {
    if (p >= 50) {
        return "bestanden";
    } else if (p < 50) {
        return "durchgefallen";
    }
}''', "missing"),
      ("M3", '''public static int erstesNegatives(int[] r) {
    for (int x : r) {
        if (x < 0) {
            return x;
        }
    }
}''', "missing"),
      ("M4", '''public static boolean gross(int n) {
    return n > 100;
    n = 0;
}''', "unreach"),
      ("M5", '''public static void zeige(int n) {
    if (n == 0) {
        return;
    }
    println(n);
}''', "ok")]

def c05(t):
    for k, src, sol in M5:
        ok, err = jcompile(src)
        got = "ok" if ok else ("missing" if "missing return" in err else "unreach" if "unreachable" in err else "?")
        assert got == t["loesung"][k] == sol, (k, got, err)

T("W0-L4-05", "Der Compiler-Detektiv", 2, "Fehler im Java-Code", ["P3"],
  [txt("Fünf Lehrlinge haben Zauberformeln abgegeben. Ordne jeder Methode die Reaktion des Compilers zu.")] +
  [x for k, src, _s in M5 for x in (txt(f"**{k}**"), code(src))],
  match([(k, f"Methode **{k}**") for k, _s, _x in M5],
        [("ok", "wird akzeptiert"), ("missing", "Fehler: missing return statement"), ("unreach", "Fehler: unreachable statement")]),
  {k: s for k, _src, s in M5},
  [txt("Der Compiler prüft, ob **jeder** mögliche Ablauf mit `return` endet – **ohne** die Bedingungen zu verstehen. "
       "Bei M2 sieht er nach dem `else if` keinen Zweig für den Rest, bei M3 fehlt die Rückgabe, wenn die Schleife ohne Treffer endet. "
       "Bei M4 steht eine Anweisung hinter `return` – sie kann nie erreicht werden. M1 hat ein `else`, M5 ist `void` und darf mit `return;` vorzeitig enden."),
   hin("Falle **P3**: Rückgabe fehlt auf einem Pfad. Abhilfe: ein abschließendes `return` nach der Verzweigung bzw. nach der Schleife.")],
  ["Was liefert die Methode, wenn die Schleife ohne Treffer endet?"], c05)

# ---------------------------------------------------------------- 06
MAX = '''public static int max2(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}
public static int maxAlle(int[] r) {      // r ist nicht leer
    int m = r[0];
    for (int i = 1; i < r.length; i++) {
        m = max2(m, r[i]);
    }
    return m;
}'''

def c06(t):
    inst = MAX.replace("        m = max2(m, r[i]);", '        int alt = m;\n        m = max2(m, r[i]);\n        System.out.println("row=" + i + ";max2(" + alt + "," + r[i] + ");" + m);')
    o, ls = jrun(inst, 'out("ret", maxAlle(new int[]{7, 12, 4, 15}));')
    rows = [l[4:].split(";") for l in ls if l.startswith("row=")]
    for k, (i, auf, m) in enumerate(rows):
        expect(t, f"a{k+1}", auf); expect(t, f"r{k+1}", m); expect(t, f"m{k+1}", m)
    expect(t, "ret", o["ret"])

T("W0-L4-06", "Das Aufrufprotokoll des Maximums", 2, "Tracetabelle", ["P8"],
  [txt("`maxAlle` ruft die Hilfsmethode `max2` auf."), code(MAX),
   txt("Erstelle das Aufrufprotokoll für `maxAlle({7, 12, 4, 15})`: eine Zeile pro Aufruf von `max2`. "
       "Den Aufruf schreibst du wie in Java mit den **Werten** der Argumente, z. B. `max2(1, 2)`."),
   tab(["i", "Aufruf von max2", "Rückgabe", "m"], [["vor der Schleife", "–", "–", "7"]] +
       [[str(k), f"[[a{k}]]", f"[[r{k}]]", f"[[m{k}]]"] for k in range(1, 4)]),
   txt("Rückgabewert von `maxAlle`: [[ret]]")],
  gaps({**{f"a{k}": ft(12) for k in range(1, 4)}, **{f"{c}{k}": fz() for c in "rm" for k in range(1, 4)}, "ret": fz()}),
  {"a1": ["max2(7, 12)"], "r1": ["12"], "m1": ["12"], "a2": ["max2(12, 4)"], "r2": ["12"], "m2": ["12"],
   "a3": ["max2(12, 15)"], "r3": ["15"], "m3": ["15"], "ret": ["15"]},
  [txt("Beim Aufruf werden die **aktuellen Werte** von `m` und `r[i]` in die Parameter `a` und `b` kopiert. `maxAlle` wartet, bis `max2` "
       "liefert, und speichert die Rückgabe in `m`. Drei Aufrufe für vier Elemente, weil die Schleife bei Index 1 beginnt."),
   hin("Falle **P8**: Im Aufrufprotokoll stehen die Argumente als Werte, nicht als Variablennamen.")],
  ["Im ersten Durchlauf ist m = 7 und r[1] = 12."], c06)

# ---------------------------------------------------------------- 07
TICKET = '''public static int ticketPreis(int alter, boolean mitglied) {
    int preis = 12;
    if (alter < 18) {
        preis = 6;
    }
    if (mitglied) {
        preis = preis - 2;
    }
    return preis;
}'''

def c07(t):
    o, _ = jrun(TICKET, 'out("p1", ticketPreis(15, true)); out("p2", ticketPreis(30, false)); out("p3", ticketPreis(18, true));')
    for g, v in o.items(): expect(t, g, v, 1)

T("W0-L4-07", "Der Eintritt zur Turmbibliothek", 3, "Code ↔ Struktogramm", ["P9", "P3"],
  [txt("**a)** Vervollständige das Struktogramm zur Methode nach EH § 5."), code(TICKET),
   sg("[[k]]", [A("preis ← 12"), W("[[b1]]", [A("[[a1]]")]), W("mitglied", [A("[[a2]]")]), G("[[r]]")]),
   txt("**b)** Gib die Rückgabewerte an: `ticketPreis(15, true)` → [[p1]] · `ticketPreis(30, false)` → [[p2]] · `ticketPreis(18, true)` → [[p3]]")],
  [gaps({"k": fa(["ticketPreis(alter: Ganzzahl, mitglied: Wahrheitswert): Ganzzahl",
                  "ticketPreis(alter: Ganzzahl, mitglied: Wahrheitswert)",
                  "int ticketPreis(int alter, boolean mitglied)",
                  "ticketPreis(mitglied: Wahrheitswert, alter: Ganzzahl): Ganzzahl"]),
         "b1": fa(["alter < 18", "alter ≤ 18", "alter > 18", "alter < 18 und mitglied"]),
         "a1": fa(["preis ← 6", "preis = 6", "gib 6 zurück", "preis == 6"]),
         "a2": fa(["preis ← preis − 2", "preis − 2", "preis = preis − 2", "gib preis − 2 zurück"]),
         "r": ft(8)}),
   gaps({"p1": fz(), "p2": fz(), "p3": fz()})],
  [{"k": ["ticketPreis(alter: Ganzzahl, mitglied: Wahrheitswert): Ganzzahl"], "b1": ["alter < 18"], "a1": ["preis ← 6"],
    "a2": ["preis ← preis − 2"], "r": ["preis"]},
   {"p1": ["4"], "p2": ["12"], "p3": ["10"]}],
  [txt("Der Kopf enthält die vollständige Signatur mit Rückgabetyp. Zwei **unabhängige** Verzweigungen ohne Falsch-Zweig, "
       "Zuweisungen mit ←. `gib … zurück` steht am Ende. 15 Jahre und Mitglied: 6 − 2 = 4; mit 18 gilt der volle Preis: 12 − 2 = 10."),
   hin("Falle **P9**: Im Struktogramm keine Java-Syntax. Ein `return` mitten in der ersten Verzweigung würde die Mitglieder-Ermäßigung überspringen.")],
  ["Die zweite Verzweigung wird immer geprüft – egal, wie die erste ausgeht."], c07)

# ---------------------------------------------------------------- 08
O8 = [("p1", "public static int anzahlZauberzahlen(int von, int bis) {"),
      ("p2", "    int anzahl = 0;"),
      ("p3", "    for (int z = von; z <= bis; z++) {"),
      ("p4", "        if (istZauberzahl(z)) {"),
      ("p5", "            anzahl++;"),
      ("p6", "        } // Ende if"),
      ("p7", "    } // Ende for"),
      ("p8", "    return anzahl;"),
      ("p9", "} // Ende Methode"),
      ("d1", "    for (int z = von; z < bis; z++) {"),
      ("d2", "        if (istZauberzahl(z) == \"true\") {"),
      ("d3", "        istZauberzahl(z);"),
      ("d4", "public static void anzahlZauberzahlen(int von, int bis) {")]
ISTZ = "static boolean istZauberzahl(int n) { return n % 7 == 0 || n % 10 == 7; }"

def c08(t):
    for seq in t["loesung"]["reihenfolgen"]:
        o, _ = jrun(ISTZ + "\n" + assemble_order(t, seq),
                    'out("a", anzahlZauberzahlen(1, 30)); out("b", anzahlZauberzahlen(14, 14)); out("c", anzahlZauberzahlen(5, 3)); out("d", anzahlZauberzahlen(20, 27));')
        assert o == {"a": "6", "b": "1", "c": "0", "d": "2"}, o
    src = assemble_order(t, ["p1", "p2", "d1", "p4", "p5", "p6", "p7", "p8", "p9"])
    o, _ = jrun(ISTZ + "\n" + src, 'out("d", anzahlZauberzahlen(20, 27));')
    assert o["d"] == "1"          # Off-by-one-Distraktor liefert falsches Ergebnis
    ok, _ = jcompile(ISTZ + "\n" + assemble_order(t, ["p1", "p2", "p3", "d2", "p5", "p6", "p7", "p8", "p9"])); assert not ok

T("W0-L4-08", "Code-Puzzle: Die Zauberzahlen", 3, "Methode implementieren", ["P6", "P3"],
  [txt("Die Methode `anzahlZauberzahlen(von: Ganzzahl, bis: Ganzzahl): Ganzzahl` liefert, wie viele der Zahlen von `von` bis `bis` "
       "(**beide einschließlich**) Zauberzahlen sind. Die Methode `istZauberzahl(n: Ganzzahl): Wahrheitswert` ist bereits implementiert "
       "und **soll verwendet werden**. Ist `von > bis`, wird 0 geliefert. Setze die Methode zusammen – nicht alle Teile werden gebraucht.")],
  order(O8),
  {"reihenfolgen": [["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9"]]},
  [txt("Der Zähler wird vor der Schleife mit 0 belegt; die Schleife läuft von `von` **bis einschließlich** `bis` (`<=`). "
       "Die Hilfsmethode liefert einen Wahrheitswert – den kannst du direkt als Bedingung verwenden. Die Rückgabe steht nach der Schleife. "
       "Für `von > bis` läuft die Schleife nie: Rückgabe 0."),
   hin("Fallen: **P6** `z < bis` lässt die letzte Zahl aus. `istZauberzahl(z) == \"true\"` vergleicht einen Wahrheitswert mit einer "
       "Zeichenkette (Compilerfehler). Ein Aufruf ohne Verwendung der Rückgabe (`istZauberzahl(z);`) bewirkt nichts.")],
  ["„einschließlich“ bedeutet <=."], c08)

LEVEL4["aufgaben"] = [k for k in ORDER if k.startswith("W0-L4-")]
