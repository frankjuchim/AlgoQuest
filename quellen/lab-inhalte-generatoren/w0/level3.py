# Level 0.3 – Die Vorratskammer (DS 3): Reihungen, Referenz/Kopie, neue Reihung, Zeichenketten
from lib import *

LEVEL3 = {
    "id": "W0-L3", "nr": "0.3", "titel": "Die Vorratskammer: Reihungen und Zeichenketten", "ds": [3],
    "ab": "AB 3 „Die Vorratskammer“ (Infoteile 1–5, Aufgaben 0–7)",
    "ide": "AQ_W0_Akademie_Geruest.txt – Level 0.3 (Klasse Vorrat, Testklasse L03VorratTest)",
    "intro": [
        txt("Eine **Reihung** ist ein Regal mit nummerierten Fächern: ein Name, viele Werte, Index von 0 bis Länge − 1."),
        hin("**Merke:** `r.length` (ohne Klammern), aber `s.length()` · letztes Element `r[r.length - 1]` · ungültiger Index → "
            "ArrayIndexOutOfBoundsException · `int[] b = a;` kopiert nur den **Pfeil** (Referenz) · neue Reihung: `new`, "
            "Werte einzeln übertragen, zurückgeben · for-each liefert nur Kopien der Werte."),
    ],
    "aufgaben": [],
}

# ---------------------------------------------------------------- 01
def c01(t):
    o, _ = jrun("", '''
        int[] r = {6, 0, 9, 2, 4}; String s = "Kristall";
        out("g1", r.length); out("g2", r[r.length - 1]); out("g3", r[r[3]]); out("g4", r[1] + r[4]);
        try { out("g5", r[5]); } catch (ArrayIndexOutOfBoundsException e) { out("g5", "ArrayIndexOutOfBoundsException"); }
        out("g6", s.length()); out("g7", s.charAt(3)); out("g8", s.substring(2, 6)); out("g9", (int) s.charAt(1));''')
    for g, v in o.items(): expect(t, g, v)

T("W0-L3-01", "Blitz-Kata: Fach für Fach", 1, "Datentypen und Ausdrücke", ["P1"],
  [txt("Gegeben sind `int[] r = {6, 0, 9, 2, 4};` und `String s = \"Kristall\";`. Gib den Wert jedes Ausdrucks an "
       "(Zeichen und Zeichenketten ohne Anführungszeichen)."),
   rei([6, 0, 9, 2, 4]),
   tab(["Ausdruck", "Wert"], [["`r.length`", "[[g1]]"], ["`r[r.length - 1]`", "[[g2]]"], ["`r[r[3]]`", "[[g3]]"],
                              ["`r[1] + r[4]`", "[[g4]]"], ["`r[5]`", "[[g5]]"], ["`s.length()`", "[[g6]]"],
                              ["`s.charAt(3)`", "[[g7]]"], ["`s.substring(2, 6)`", "[[g8]]"], ["`(int) s.charAt(1)`", "[[g9]]"]]),
   hin("'a' hat den ASCII-Wert 97, die folgenden Kleinbuchstaben zählen weiter: 'b' = 98, …")],
  gaps({"g1": fz(), "g2": fz(), "g3": fz(), "g4": fz(),
        "g5": fa(["0", "4", "null", "ArrayIndexOutOfBoundsException"]), "g6": fz(), "g7": ft(4), "g8": ft(8), "g9": fz()}),
  {"g1": ["5"], "g2": ["4"], "g3": ["9"], "g4": ["4"], "g5": ["ArrayIndexOutOfBoundsException"], "g6": ["8"],
   "g7": ["s", "'s'"], "g8": ["ista", "\"ista\""], "g9": ["114"]},
  [txt("- Die Länge ist 5, das letzte Element hat den Index 4 und den Wert 4.\n- `r[r[3]]` = `r[2]` = 9 (erst den inneren Index auswerten).\n"
       "- `r[5]` gibt es nicht – Indizes laufen nur von 0 bis 4 → ArrayIndexOutOfBoundsException.\n"
       "- „Kristall“ hat 8 Zeichen, Index 3 ist 's', `substring(2, 6)` liefert die Indizes 2 bis 5: \"ista\".\n"
       "- 'r' ist der 18. Buchstabe: 97 + 17 = 114."),
   hin("Falle **P1**: Laufzeitfehler durch einen Index außerhalb von 0 … Länge − 1.")],
  ["Bei verschachtelten Indizes zuerst den inneren Ausdruck auswerten."], c01)

# ---------------------------------------------------------------- 02
ITEMS2 = [("e1", "die Summe aller Vorräte bilden", "beide"), ("e2", "jeden Vorrat halbieren", "for"),
          ("e3", "den Index des ersten leeren Fachs liefern", "for"), ("e4", "prüfen, ob ein Fach mehr als 100 enthält", "beide"),
          ("e5", "zählen, wie oft zwei Nachbarfächer gleich viel enthalten", "for"), ("e6", "den größten Vorrat bestimmen", "beide"),
          ("e7", "die Vorräte von hinten nach vorn ausgeben", "for")]

def c02(t):
    # Beleg: for-each kann nicht veraendern; beide Varianten fuer "beide"-Aufgaben liefern dasselbe
    o, _ = jrun("", '''
        int[] r = {4, 8, 6};
        for (int x : r) { x = x / 2; }  out("each", arr(r));
        for (int i = 0; i < r.length; i++) { r[i] = r[i] / 2; } out("for", arr(r));''')
    assert o == {"each": "4,8,6", "for": "2,4,3"}, o
    for k, _m, sol in ITEMS2: assert t["loesung"][k] == sol

T("W0-L3-02", "for oder for-each?", 1, "Funktionsweise erläutern", [],
  [txt("Für jede Aufgabe auf der Reihung `vorrat` soll eine Schleife geschrieben werden. Ordne zu: Geht es **nur mit der Zählschleife** "
       "(Index nötig) oder sind **beide** Schleifen möglich?")],
  match([(k, m) for k, m, _s in ITEMS2], [("for", "nur Zählschleife mit Index"), ("beide", "Zählschleife oder for-each")]),
  {k: s for k, _m, s in ITEMS2},
  [txt("for-each liefert in jedem Durchlauf nur eine **Kopie** des Werts – ohne Index. Das reicht zum Lesen (Summe, Maximum, "
       "Suche nach einem Wert). Sobald du **verändern** (`r[i] = …`), eine **Position** liefern, mit **Nachbarn** vergleichen oder "
       "**rückwärts** laufen willst, brauchst du die Zählschleife.")],
  ["Frage dich: Brauche ich den Index i?"], c02)

# ---------------------------------------------------------------- 03
LOOP3 = '''int[] r = {5, 8, 1, 9, 3, 7, 2};
for (int i = r.length - 2; i >= 0; i = i - 3) {
    println(r[i]);
}'''

def c03(t):
    o, ls = jrun("", LOOP3.replace("println(r[i]);", 'System.out.println("idx=" + i);'))
    folge = [int(l[4:]) for l in ls if l.startswith("idx=")]
    assert folge == t["loesung"]["folge"], folge

T("W0-L3-03", "Der Sprung durchs Regal", 1, "Tracetabelle", ["P6"],
  [code(LOOP3),
   txt("Klicke die Fächer in der Reihenfolge an, in der ihr Wert ausgegeben wird.")],
  arr([5, 8, 1, 9, 3, 7, 2], "klick"),
  {"folge": [5, 2]},
  [txt("Die Länge ist 7, also startet i bei 7 − 2 = 5. Danach i = 2, dann i = −1 – die Bedingung `i >= 0` ist falsch. "
       "Ausgegeben werden r[5] = 7 und r[2] = 1."),
   hin("Falle **P6**: Startwert und Abbruchbedingung genau ausrechnen, nicht schätzen.")],
  ["Berechne zuerst den Startwert r.length − 2."], c03)

# ---------------------------------------------------------------- 04
REF4 = '''int[] a = {3, 5, 7};
int[] b = a;
int[] c = new int[3];
for (int i = 0; i < a.length; i++) {
    c[i] = a[i];
}
b[0] = 30;
c[1] = 50;
b = c;
b[2] = 70;'''

def c04(t):
    o, _ = jrun("", REF4 + '''
        for (int i = 0; i < 3; i++) { out("a" + i, a[i]); out("b" + i, b[i]); out("c" + i, c[i]); }
        out("ab", a == b); out("bc", b == c);''')
    for g, v in o.items():
        i = 1 if g in ("ab", "bc") else 0
        expect(t, g, v, i)

T("W0-L3-04", "Zwei Schilder, ein Regal", 2, "Objektkarten und Referenzen", ["P2"],
  [txt("Überlege ohne Gerät: Was steht nach dem letzten Befehl in den Reihungen, auf die `a`, `b` und `c` verweisen?"),
   code(REF4),
   tab(["Variable", "Index 0", "Index 1", "Index 2"], [["a", "[[a0]]", "[[a1]]", "[[a2]]"], ["b", "[[b0]]", "[[b1]]", "[[b2]]"],
                                                      ["c", "[[c0]]", "[[c1]]", "[[c2]]"]]),
   txt("Werte der Vergleiche: `a == b` → [[ab]] · `b == c` → [[bc]]")],
  [gaps({f"{v}{i}": fz() for v in "abc" for i in range(3)}), gaps({"ab": fa(WF), "bc": fa(WF)})],
  [{"a0": ["30"], "a1": ["5"], "a2": ["7"], "b0": ["3"], "b1": ["50"], "b2": ["70"], "c0": ["3"], "c1": ["50"], "c2": ["70"]},
   {"ab": ["false"], "bc": ["true"]}],
  [txt("`b = a` kopiert nur den Pfeil: `b[0] = 30` ändert die Reihung von `a`. `c` ist eine **echte Kopie** (new + Schleife) – "
       "`c[1] = 50` betrifft nur sie. Nach `b = c` zeigt `b` auf die Reihung von `c`, darum ändert `b[2] = 70` diese. "
       "`==` vergleicht bei Reihungen die **Pfeile**: a und b zeigen jetzt auf verschiedene Reihungen, b und c auf dieselbe."),
   hin("Wer im Abitur „die Reihung bleibt unverändert“ liest, braucht eine echte Kopie – eine zweite Variable reicht nicht (vgl. Falle **P2**).")],
  ["Zeichne nach jeder Zeile die Pfeile."], c04)

# ---------------------------------------------------------------- 05
O5 = [("p1", "public static int[] differenzen(int[] r) {"),
      ("p2", "    int[] d = new int[r.length - 1];"),
      ("p3", "    for (int i = 0; i < d.length; i++) {"),
      ("p4", "        d[i] = r[i + 1] - r[i];"),
      ("p5", "    } // Ende for"),
      ("p6", "    return d;"),
      ("p7", "} // Ende Methode"),
      ("d1", "    int[] d = r;"),
      ("d2", "    for (int i = 0; i < r.length; i++) {"),
      ("d3", "        d[i] = r[i] - r[i - 1];"),
      ("d4", "public static void differenzen(int[] r) {")]

def c05(t):
    for seq in t["loesung"]["reihenfolgen"]:
        o, _ = jrun(assemble_order(t, seq), '''int[] r = {3, 8, 6, 6, 10}; int[] d = differenzen(r);
            out("d", arr(d)); out("r", arr(r)); out("e", differenzen(new int[]{7}).length);''')
        assert o == {"d": "5,-2,0,4", "r": "3,8,6,6,10", "e": "0"}, o
    # Distraktor d2 fuehrt zum Laufzeitfehler
    src = assemble_order(t, ["p1", "p2", "d2", "p4", "p5", "p6", "p7"])
    o, _ = jrun(src, 'try { differenzen(new int[]{1, 2, 3}); out("x", "ok"); } catch (ArrayIndexOutOfBoundsException e) { out("x", "AIOOBE"); }')
    assert o["x"] == "AIOOBE"

T("W0-L3-05", "Code-Puzzle: Die Zuwachs-Liste", 2, "Methode implementieren", ["P1", "P2", "P6"],
  [txt("Die Methode `differenzen(r: Reihung von Ganzzahl): Reihung von Ganzzahl` liefert eine **neue** Reihung mit allen Differenzen "
       "benachbarter Werte (`r[i + 1] − r[i]`), z. B. `{5, −2, 0, 4}` für `{3, 8, 6, 6, 10}`. `r` enthält mindestens ein Element und bleibt "
       "unverändert. Setze die Methode zusammen – nicht alle Teile werden gebraucht.")],
  order(O5),
  {"reihenfolgen": [["p1", "p2", "p3", "p4", "p5", "p6", "p7"]]},
  [txt("Muster „neue Reihung liefern“: (1) mit `new` in passender Länge anlegen – hier eine weniger als `r`, (2) in der Schleife "
       "aus `r` lesen und in `d` schreiben, (3) `d` zurückgeben. Die Schleife läuft über `d.length`, damit `r[i + 1]` gültig bleibt."),
   hin("Fallen: **P2** `int[] d = r;` würde keine neue Reihung anlegen. **P6/P1** `i < r.length` greift im letzten Durchlauf auf "
       "`r[r.length]` zu – Absturz.")],
  ["Wie viele Differenzen hat eine Reihung mit 5 Werten?"], c05)

# ---------------------------------------------------------------- 06
UMDREHEN = '''public static void umdrehen(int[] r) {
    for (int i = 0; i < r.length / 2; i++) {
        tausche(r, i, r.length - 1 - i);
    }
}'''

def c06(t):
    o, ls = jrun('static void tausche(int[] r, int i, int j) { System.out.println("sw=" + i + "," + j); int h = r[i]; r[i] = r[j]; r[j] = h; }\n' + UMDREHEN,
                 'int[] r = {4, 9, 1, 7, 3, 8}; umdrehen(r); out("r", arr(r));')
    sw = [[int(x) for x in l[3:].split(",")] for l in ls if l.startswith("sw=")]
    assert sw == t["loesung"]["tausche"], sw
    assert o["r"] == "8,3,7,1,9,4"

T("W0-L3-06", "Die Inventur von hinten", 2, "Tracetabelle", ["P6"],
  [txt("Die Methode `umdrehen` kehrt die Reihenfolge **in der Reihung selbst** um. `tausche(r, i, j)` vertauscht `r[i]` und `r[j]`."),
   code(UMDREHEN),
   txt("Führe die Tausche aus, die der Aufruf mit `r = {4, 9, 1, 7, 3, 8}` bewirkt – in der richtigen Reihenfolge.")],
  arr([4, 9, 1, 7, 3, 8], "tausch"),
  {"tausche": [[0, 5], [1, 4], [2, 3]]},
  [txt("Die Schleife läuft nur bis zur **Mitte** (`r.length / 2` = 3 Durchläufe): i = 0 tauscht mit 5, i = 1 mit 4, i = 2 mit 3. "
       "Ergebnis: {8, 3, 7, 1, 9, 4}."),
   hin("Liefe die Schleife bis `r.length`, würde jedes Paar **zweimal** getauscht – die Reihung wäre wieder wie vorher (Falle **P6**).")],
  ["Das Gegenstück zu Index i ist r.length − 1 − i."], c06)

# ---------------------------------------------------------------- 07
DOPPEL = '''public static boolean hatDoppelbuchstaben(String s) {
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == s.charAt(i + 1)) {
            return true;
        }
    }
    return false;
}'''

def c07(t):
    o, _ = jrun(DOPPEL, '''
        try { out("g2", hatDoppelbuchstaben("Elfe")); } catch (StringIndexOutOfBoundsException e) { out("g2", "StringIndexOutOfBoundsException"); }
        out("troll", hatDoppelbuchstaben("Troll"));''')
    lf = lambda v: "liefert " + v if v in ("true", "false") else v
    expect(t, "g2", lf(o["g2"]), 1)
    expect(t, "g3", lf(o["troll"]), 1)
    assert DOPPEL.split("\n")[t["loesung"][0]["zeilen"][0] - 1].strip().startswith("for (int i = 0; i < s.length()")
    for var in t["loesung"][1]["g1"]:
        fixed = DOPPEL.replace("i < s.length();", f"i < {var};")
        o, _ = jrun(fixed, 'out("r", "" + hatDoppelbuchstaben("Elfe") + hatDoppelbuchstaben("Troll") + hatDoppelbuchstaben("") + hatDoppelbuchstaben("x") + hatDoppelbuchstaben("aa"));')
        assert o["r"] == "falsetruefalsefalsetrue", (var, o)

T("W0-L3-07", "Bug-Hunt: Doppelte Buchstaben", 3, "Fehler im Java-Code", ["P1", "P6"],
  [txt("Die Methode soll `true` liefern, wenn in `s` zwei **gleiche Zeichen direkt nebeneinander** stehen (z. B. „Troll“). "
       "Sie enthält **genau einen** Fehler."), code(DOPPEL),
   txt("**a)** Wähle die fehlerhafte Zeile."),
   txt("**b)** Korrigiere die Schleifenbedingung: `for (int i = 0; i < [[g1]]; i++)`"),
   txt("Was passiert **mit** dem Fehler beim Aufruf `hatDoppelbuchstaben(\"Elfe\")`? [[g2]] · und bei `hatDoppelbuchstaben(\"Troll\")`? [[g3]]")],
  [lines(1, 1), gaps({"g1": ft(14), "g2": fa(["liefert true", "liefert false", "StringIndexOutOfBoundsException"]),
                      "g3": fa(["liefert true", "liefert false", "StringIndexOutOfBoundsException"])})],
  [{"zeilen": [2]}, {"g1": ["s.length() - 1", "(s.length() - 1)"], "g2": ["StringIndexOutOfBoundsException"], "g3": ["liefert true"]}],
  [txt("Im letzten Durchlauf ist `i = s.length() - 1`, dann liest `s.charAt(i + 1)` hinter dem Ende. Bei „Troll“ fällt das nicht auf: "
       "Das Paar „ll“ wird gefunden, bevor das Ende erreicht ist – darum ist der Fehler tückisch. Bei „Elfe“ läuft die Schleife bis zum Ende und stürzt ab."),
   hin("Falle **P1/P6**: Wer `i + 1` liest, muss die Grenze um 1 verkleinern. Teste immer auch einen Fall **ohne** Treffer.")],
  ["Welcher Index wird im letzten Durchlauf mit charAt(i + 1) gelesen?"], c07)

# ---------------------------------------------------------------- 08
OHNE = '''public static String ohneLeerzeichen(String s) {
    String e = [[g1]];
    for (int i = 0; i < [[g2]]; i++) {
        char c = [[g3]];
        if (c [[g4]] ' ') {
            e = [[g5]];
        }
    }
    return e;
}'''

def c08(t):
    L = t["loesung"]
    base = {g: L[g][0] for g in ("g1", "g2", "g3", "g4", "g5")}
    tests = 'out("r", ohneLeerzeichen("Kraut der Weisen") + "|" + ohneLeerzeichen("") + "|" + ohneLeerzeichen("  a b ") + "|");'
    for g in base:
        for v in L[g]:
            m = dict(base); m[g] = v
            o, _ = jrun(fill(OHNE, m), tests)
            assert o["r"] == "KrautderWeisen||ab|", (g, v, o)
    # Gegenprobe: equals statt != kompiliert nicht
    ok, _ = jcompile(fill(OHNE, {**base, "g4": ".equals"}))
    assert not ok

T("W0-L3-08", "Lückencode: Etiketten ohne Lücken", 3, "Lückencode", ["P5", "P4"],
  [txt("Die Methode `ohneLeerzeichen(s: Zeichenkette): Zeichenkette` liefert `s` ohne alle Leerzeichen, z. B. \"KrautderWeisen\" für "
       "\"Kraut der Weisen\". Verwende nur erlaubte Zeichenketten-Operationen. Fülle die Lücken (Java-Code)."),
   code(OHNE)],
  gaps({"g1": ft(6), "g2": ft(12), "g3": ft(12), "g4": fa(["==", "!=", ".equals", "="]), "g5": ft(12)}),
  {"g1": ["\"\""], "g2": ["s.length()"], "g3": ["s.charAt(i)"], "g4": ["!="], "g5": ["e + c", "e + s.charAt(i)", "e + \"\" + c"]},
  [txt("Das Ergebnis wird Zeichen für Zeichen mit `+` aufgebaut – Startwert ist die leere Zeichenkette `\"\"`. "
       "Ein **Zeichen** (`char`, einfache Anführungszeichen) vergleichst du mit `==` bzw. `!=`; `equals` gibt es nur für Zeichenketten."),
   hin("Falle **P5**: `replace` oder `split` wären bequemer, sind im Abitur aber verboten. Falle **P4**: `' '` (Zeichen) und `\" \"` (Zeichenkette) "
       "sind verschiedene Typen.")],
  ["Die Schleife besucht jedes Zeichen genau einmal."], c08)

LEVEL3["aufgaben"] = [k for k in ORDER if k.startswith("W0-L3-")]
