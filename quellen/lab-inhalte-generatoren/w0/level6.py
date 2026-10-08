# Level 0.6 – Die Methoden-Werkstatt (DS 6): Rezept, Fehlergalerie F1–F10, Abi-Check, Papier-Compiler 0
from lib import *

LEVEL6 = {
    "id": "W0-L6", "nr": "0.6", "titel": "Die Methoden-Werkstatt: Fehlergalerie und Abi-Check", "ds": [6],
    "ab": "AB 5 „Die Methoden-Werkstatt“ (Rezept, Fehlergalerie F1–F10, Aufgaben 1–5)",
    "ide": "AQ_W0_Akademie_Geruest.txt – Papier-Compiler 0 (Klasse Werkstattpruefung, Testklasse PapierCompiler0Test)",
    "intro": [
        txt("Im Abitur steht nur ein Aufgabentext: „Implementieren Sie die Methode …“. Kein Compiler meldet das fehlende `return`, kein Test "
            "die vergessene leere Reihung. Das Rezept: **Lesen und markieren → Signatur → Randfälle → Idee/Struktogramm → Java → Abi-Check → Papier-Compiler.**"),
        hin("**Abi-Check:** Kopf wie gefordert · Rückgabe in jedem Pfad · Leer-Abfrage vor `r[0]` / `charAt(0)` · Grenzen 0 bis length − 1 · "
            "Original unverändert, wenn gefordert · Kommazahl ohne ganzzahlige Division · nur erlaubte String-Operationen, `equals`."),
    ],
    "aufgaben": [],
}

FEHLER = [("F1", "F1 fehlender Rückgabepfad"), ("F2", "F2 Off-by-one"), ("F3", "F3 = statt =="), ("F4", "F4 ganzzahlige Division"),
          ("F5", "F5 Parameter überschrieben"), ("F6", "F6 Rückgabe in der Schleife zu früh"), ("F7", "F7 Reihung verändert statt Kopie"),
          ("F8", "F8 == statt equals"), ("F9", "F9 Leer-Abfrage vergessen"), ("F10", "F10 falscher Startwert bei Maximum/Minimum")]

# ---------------------------------------------------------------- 01
S1 = [("s1", "`for (int i = 0; i <= r.length; i++) { s = s + r[i]; }` – Summe aller Werte", "F2"),
      ("s2", "`if (titel == \"Runenlehre\") { … }` – Titel prüfen", "F8"),
      ("s3", "`double quote = treffer / versuche;` – Anteil (treffer, versuche sind Ganzzahlen)", "F4"),
      ("s4", "`for (int x : r) { if (x > 0) { return true; } else { return false; } }` – Gibt es irgendeinen positiven Wert?", "F6"),
      ("s5", "`int groesstes = 0; for (int x : r) { if (x > groesstes) { groesstes = x; } }` – Maximum (r nicht leer)", "F10"),
      ("s6", "`int[] sicher = r; sicher[0] = -1;` – r soll unverändert bleiben", "F7"),
      ("s7", "`return s.charAt(s.length() - 1);` – letztes Zeichen; s darf leer sein", "F9"),
      ("s8", "`public static int summeAb(int[] r, int k) { k = 2; …` – Summe ab Index k", "F5")]

def c01(t):
    o, _ = jrun('''
        static int s1(int[] r) { int s = 0; for (int i = 0; i <= r.length; i++) { s = s + r[i]; } return s; }
        static boolean s4(int[] r) { for (int x : r) { if (x > 0) { return true; } else { return false; } } return false; }
        static int s5(int[] r) { int groesstes = 0; for (int x : r) { if (x > groesstes) { groesstes = x; } } return groesstes; }
        static char s7(String s) { return s.charAt(s.length() - 1); }
        static int s8(int[] r, int k) { k = 2; int s = 0; for (int i = k; i < r.length; i++) s += r[i]; return s; }''', '''
        try { s1(new int[]{1, 2}); out("s1", "ok"); } catch (ArrayIndexOutOfBoundsException e) { out("s1", "AIOOBE"); }
        String titel = new String("Runenlehre"); out("s2", titel == "Runenlehre");
        int treffer = 3, versuche = 4; double quote = treffer / versuche; out("s3", quote);
        out("s4", s4(new int[]{-1, 5}));
        out("s5", s5(new int[]{-4, -2, -9}));
        int[] r = {7, 8}; int[] sicher = r; sicher[0] = -1; out("s6", r[0]);
        try { s7(""); out("s7", "ok"); } catch (StringIndexOutOfBoundsException e) { out("s7", "SIOOBE"); }
        out("s8", s8(new int[]{1, 2, 3, 4}, 0));''')
    assert o == {"s1": "AIOOBE", "s2": "false", "s3": "0.0", "s4": "false", "s5": "0", "s6": "-1", "s7": "SIOOBE", "s8": "7"}, o
    for k, _m, f in S1: assert t["loesung"][k] == f

T("W0-L6-01", "Fehler-Bingo", 1, "Fehler im Java-Code", ["P1", "P4", "P5", "P6"],
  [txt("Jeder Schnipsel enthält **genau einen** Fehler aus der Fehlergalerie. Ordne die Fehlernummer zu (nicht alle Nummern kommen vor).")],
  match([(k, m) for k, m, _f in S1], FEHLER),
  {k: f for k, _m, f in S1},
  [txt("- `<=` mit `length` greift auf `r[r.length]` zu (F2).\n- Zeichenketten mit `equals` vergleichen (F8).\n- 3 / 4 ergibt 0 (F4).\n"
       "- Ein `return` in **beiden** Zweigen beendet die Schleife nach dem ersten Element (F6).\n- Startwert 0 ist falsch, wenn alle Werte negativ sind (F10).\n"
       "- `sicher = r` kopiert nur die Referenz (F7).\n- `s.length() - 1` ist −1 bei der leeren Zeichenkette (F9).\n- `k = 2` überschreibt den Parameter (F5)."),
   hin("Die Fehler entsprechen den Fallen **P1** (Laufzeitfehler), **P4** (Division), **P5** (equals) und **P6** (Off-by-one).")],
  ["Lies die Absicht in jeder Zeile genau – sie verrät, was schiefgeht."], c01)

# ---------------------------------------------------------------- 02
ANTEIL = '''static double anteilGerade(int[] r) {
    if (r.length == 0) { return 0.0; }
    int a = 0;
    for (int x : r) { if (x % 2 == 0) { a++; } }
    return (double) a / r.length;
}'''
FAELLE2 = [("g1", "{4, 7, 2, 9}"), ("g2", "{ }"), ("g3", "{3}"), ("g4", "{-2, 6}"), ("g5", "{-3, 6, 8, 10, 1}")]

def c02(t):
    main = "".join(f'out("{g}", anteilGerade(new int[]{v.replace(" ", "") if v == "{ }" else v}));' for g, v in FAELLE2)
    o, _ = jrun(ANTEIL, main)
    for g, v in o.items(): expect(t, g, v)

T("W0-L6-02", "Rezept Schritt 3: Randfälle", 1, "Methode implementieren", ["P4"],
  [txt("Aufgabe: *Implementieren Sie die Methode `anteilGerade(r: Reihung von Ganzzahl): Kommazahl`. Sie liefert den Anteil der geraden "
       "Werte in r als Kommazahl zwischen 0.0 und 1.0. Für eine leere Reihung liefert sie 0.0.*"),
   txt("Bevor du programmierst, legst du die Testtabelle an. Gib die erwarteten Ergebnisse an (Kommazahl mit Punkt)."),
   tab(["r", "erwartet"], [[f"`{v}`", f"[[{g}]]"] for g, v in FAELLE2])],
  gaps({g: fz() for g, _v in FAELLE2}),
  {"g1": ["0.5"], "g2": ["0.0"], "g3": ["0.0"], "g4": ["1.0"], "g5": ["0.6"]},
  [txt("Gerade heißt `x % 2 == 0` – das gilt auch für −2 (−2 % 2 = 0), aber nicht für −3 (−3 % 2 = −1). "
       "In {−3, 6, 8, 10, 1} sind 3 von 5 Werten gerade: 0.6. Die leere Reihung ist ein **Randfall**, der laut Text 0.0 liefert – "
       "ohne Abfrage würde 0 / 0 gerechnet."),
   hin("Falle **P4**: Der Anteil muss als Kommazahl berechnet werden – `a / r.length` mit zwei Ganzzahlen liefert fast immer 0.")],
  ["Anteil = Anzahl der geraden Werte / Anzahl aller Werte."], c02)

# ---------------------------------------------------------------- 03
FORM3 = [("e1", "„… die **echt größer** als grenze sind“", "gt"), ("e2", "„… die **mindestens** grenze betragen“", "ge"),
         ("e3", "„… die **höchstens** grenze betragen“", "le"), ("e4", "„… die **kleiner** als grenze sind“", "lt"),
         ("e5", "„… liefert eine **neue** Reihung …; r bleibt unverändert“", "neu"), ("e6", "„… **setzt** alle negativen Werte in r auf 0“", "void"),
         ("e7", "„Der Durchschnitt ist **als Kommazahl** zu berechnen.“", "cast")]
KAT3 = [("gt", "`x > grenze`"), ("ge", "`x >= grenze`"), ("le", "`x <= grenze`"), ("lt", "`x < grenze`"),
        ("neu", "`new` anlegen, füllen, zurückgeben"), ("void", "Rückgabetyp `void`, `r[i] = …`"), ("cast", "`(double)` **vor** der Division")]

def c03(t):
    o, _ = jrun("", 'int g = 5; int[] r = {4, 5, 6}; int gt=0, ge=0, le=0, lt=0; for (int x : r) { if (x > g) gt++; if (x >= g) ge++; if (x <= g) le++; if (x < g) lt++; }'
                    'out("gt", gt); out("ge", ge); out("le", le); out("lt", lt); out("cast", (double) 7 / 2); out("nocast", (double) (7 / 2));')
    assert o == {"gt": "1", "ge": "2", "le": "2", "lt": "1", "cast": "3.5", "nocast": "3.0"}, o
    for k, _m, s in FORM3: assert t["loesung"][k] == s

T("W0-L6-03", "Rezept Schritt 1: Lesen und markieren", 1, "Methode implementieren", ["P6", "P2", "P4"],
  [txt("Jede Formulierung im Aufgabentext hat eine Folge für deinen Code. Ordne zu.")],
  match([(k, m) for k, m, _s in FORM3], KAT3),
  {k: s for k, _m, s in FORM3},
  [txt("„echt größer“ → `>`, „mindestens“ → `>=`, „höchstens“ → `<=`, „kleiner“ → `<`. „neue Reihung“ verlangt `new` – das Original wird nur gelesen. "
       "„setzt … in r“ verändert die übergebene Reihung, eine Rückgabe ist nicht nötig. „als Kommazahl“: Cast vor der Division, "
       "sonst ganzzahlige Division (7 / 2 → 3)."),
   hin("Falle **P6**: Wer „mindestens“ mit `>` umsetzt, verliert genau den Grenzfall. Darum gehört der Gleichheitsfall in die Testtabelle.")],
  ["Markiere im Text alle Vergleichswörter."], c03)

# ---------------------------------------------------------------- 04
GLEICH = '''public static int anzahlGleich(String[] woerter, String wort) {
    int anzahl = 0;
    for (int i = 1; i < woerter.length; i++) {
        if (woerter[i] == wort) {
            anzahl++;
        }
    }
}'''

def c04(t):
    ok, err = jcompile(GLEICH); assert not ok and "missing return" in err
    fixed1 = GLEICH.replace("        }\n    }\n}", "        }\n    }\n    return anzahl;\n}")
    o, _ = jrun(fixed1, 'String[] w = {new String("Eis"), new String("Eis"), "Feuer"}; out("a", anzahlGleich(w, "Eis"));')
    assert o["a"] == "0"   # == und Start bei 1 -> falsch (richtig waere 2)
    fixed = fixed1.replace("int i = 1", "int i = 0").replace("woerter[i] == wort", "woerter[i].equals(wort)")
    o, _ = jrun(fixed, 'String[] w = {new String("Eis"), new String("Eis"), "Feuer"}; out("a", anzahlGleich(w, "Eis")); out("b", anzahlGleich(new String[0], "x"));')
    assert o == {"a": "2", "b": "0"}
    assert sorted(t["loesung"]["richtig"]) == ["a", "b", "c"]

T("W0-L6-04", "Abi-Check: Was fehlt hier?", 2, "Fehler im Java-Code", ["P3", "P5", "P6"],
  [txt("Auftrag: *`anzahlGleich(woerter: Reihung von Zeichenkette, wort: Zeichenkette): Ganzzahl` liefert, wie oft `wort` in `woerter` vorkommt.* "
       "Ein Lehrling gibt diese Lösung ab:"), code(GLEICH),
   txt("Welche Punkte des Abi-Checks verletzt die Lösung? Wähle **alle** passenden.")],
  choice([("a", "Rückgabe fehlt auf einem Pfad (F1)"), ("b", "Schleifengrenzen falsch – ein Element wird ausgelassen (F2)"),
          ("c", "Zeichenketten mit `==` statt `equals` verglichen (F8)"), ("d", "ganzzahlige Division (F4)"),
          ("e", "Parameter überschrieben (F5)"), ("f", "Leer-Abfrage vor dem Zugriff vergessen (F9)"),
          ("g", "Kopf passt nicht zur Signatur")], mehrfach=True),
  {"richtig": ["a", "b", "c"]},
  [txt("Nach der Schleife fehlt `return anzahl;` – der Compiler meldet „missing return statement“. Die Schleife beginnt bei 1, `woerter[0]` wird "
       "nie geprüft. `==` vergleicht bei Zeichenketten Referenzen. Eine Leer-Abfrage ist **nicht** nötig: Für die leere Reihung läuft die "
       "Schleife nicht – es wird nie auf ein Element zugegriffen. Kopf und Signatur passen."),
   hin("Fallen **P3** (Rückgabe fehlt), **P6** (Startindex), **P5** (equals).")],
  ["Gehe den Abi-Check Punkt für Punkt durch."], c04)

# ---------------------------------------------------------------- 05
ANSTIEG = '''public static int laengsterAnstieg(int[] r) {
    if (r.length == 0) {
        return 0;
    }
    int beste = 1;
    int aktuell = 1;
    for (int i = 1; i < r.length; i++) {
        if (r[i] > r[i - 1]) {
            aktuell++;
            if (aktuell > beste) {
                beste = aktuell;
            }
        } else {
            aktuell = 1;
        }
    }
    return beste;
}'''
R5 = [2, 5, 7, 3, 4, 6, 9, 1]

def c05(t):
    inst = ANSTIEG.replace("        if (r[i] > r[i - 1]) {", "        boolean b = r[i] > r[i - 1];\n        if (b) {").replace(
        "            aktuell = 1;\n        }\n", '            aktuell = 1;\n        }\n        System.out.println("row=" + i + ";" + (b ? "w" : "f") + ";" + aktuell + ";" + beste);\n')
    o, ls = jrun(inst, 'out("ret", laengsterAnstieg(new int[]{2, 5, 7, 3, 4, 6, 9, 1})); out("leer", laengsterAnstieg(new int[0])); out("ab", laengsterAnstieg(new int[]{9, 7, 5}));')
    rows = [l[4:].split(";") for l in ls if l.startswith("row=")]
    for i, b, a, be in rows[2:7]:
        expect(t, f"b{i}", b, 0); expect(t, f"a{i}", a, 0); expect(t, f"m{i}", be, 0)
    assert rows[0][1:] == ["w", "2", "2"] and rows[1][1:] == ["w", "3", "3"]
    expect(t, "ret", o["ret"], 0); expect(t, "x", o["ab"], 1)

T("W0-L6-05", "Die längste Treppe", 2, "Tracetabelle", ["P8"],
  [txt("`laengsterAnstieg` liefert die Länge der längsten Folge direkt aufeinanderfolgender, **echt steigender** Werte."), code(ANSTIEG),
   txt("**a)** Vervollständige die Tracetabelle für `r = {2, 5, 7, 3, 4, 6, 9, 1}` (Werte am Ende jedes Durchlaufs)."),
   tab(["i", "r[i] > r[i − 1]", "aktuell", "beste"], [["vor der Schleife", "–", "1", "1"], ["1", "w", "2", "2"], ["2", "w", "3", "3"]] +
       [[str(i), f"[[b{i}]]", f"[[a{i}]]", f"[[m{i}]]"] for i in range(3, 8)]),
   txt("Rückgabewert: [[ret]]"),
   txt("**b)** Was liefert `laengsterAnstieg({9, 7, 5})`? [[x]]")],
  [gaps({**{f"b{i}": fa(WFS) for i in range(3, 8)}, **{f"{c}{i}": fz() for c in "am" for i in range(3, 8)}, "ret": fz()}),
   gaps({"x": fz()})],
  [{"b3": ["f"], "a3": ["1"], "m3": ["3"], "b4": ["w"], "a4": ["2"], "m4": ["3"], "b5": ["w"], "a5": ["3"], "m5": ["3"],
    "b6": ["w"], "a6": ["4"], "m6": ["4"], "b7": ["f"], "a7": ["1"], "m7": ["4"], "ret": ["4"]},
   {"x": ["1"]}],
  [txt("`aktuell` zählt die laufende Treppe und fällt bei einem Abstieg auf 1 zurück; `beste` merkt sich den Rekord **sofort** (Baustein Maximum). "
       "Die Treppe 3, 4, 6, 9 hat Länge 4. Bei {9, 7, 5} gibt es keinen Anstieg – jedes einzelne Element ist eine Treppe der Länge 1."),
   hin("Falle **P8**: In der Spalte „beste“ steht auch dann ein Wert, wenn er sich nicht ändert – sonst ist die Zeile unvollständig.")],
  ["Bei einem Abstieg wird aktuell auf 1 gesetzt, beste bleibt."], c05)

# ---------------------------------------------------------------- 06
PROZ = '''public static double prozentBestanden(int[] punkte, int grenze) {
    if (punkte.length == 0) {
        return 0.0;
    }
    int anzahl = 0;
    for (int p : punkte) {
        if (p > grenze) {
            anzahl++;
        }
    }
    return anzahl / punkte.length * 100;
}'''
OPT6 = ["(double) (anzahl / punkte.length) * 100", "(double) anzahl / punkte.length * 100",
        "anzahl / punkte.length * 100.0", "(int) (100.0 * anzahl / punkte.length)"]

def c06(t):
    o, _ = jrun(PROZ, 'out("g3", prozentBestanden(new int[]{50, 40, 70, 30}, 40));')
    expect(t, "g3", o["g3"], 1)
    L = t["loesung"]
    assert L[0]["zeilen"] == [7, 11]
    ok_opts = []
    for opt in OPT6:
        src = PROZ.replace("p > grenze", "p " + L[1]["g1"][0] + " grenze").replace("return anzahl / punkte.length * 100;", f"return {opt};")
        o, _ = jrun(src, 'out("a", prozentBestanden(new int[]{50, 40, 70, 30}, 40)); out("b", prozentBestanden(new int[]{1, 2, 3}, 2)); out("c", prozentBestanden(new int[0], 1));')
        if o["a"] == "75.0" and abs(float(o["b"]) - 200 / 3) < 1e-9 and o["c"] == "0.0": ok_opts.append(opt)
        if opt == L[1]["g2"][0]: expect(t, "g4", o["a"], 1)
    assert ok_opts == L[1]["g2"], ok_opts

T("W0-L6-06", "Bug-Hunt: Die Prüfungsstatistik", 2, "Fehler im Java-Code", ["P4", "P6"],
  [txt("*`prozentBestanden(punkte: Reihung von Ganzzahl, grenze: Ganzzahl): Kommazahl` liefert, wie viel Prozent der Werte **mindestens** "
       "`grenze` betragen, als Kommazahl; für eine leere Reihung 0.0.* Die Implementierung enthält **zwei** Fehler."), code(PROZ),
   txt("**a)** Wähle die beiden fehlerhaften Zeilen."),
   txt("**b)** Korrektur: Bedingung `p` [[g1]] `grenze` · Rückgabe `return` [[g2]] `;`"),
   txt("Für `prozentBestanden({50, 40, 70, 30}, 40)` liefert die fehlerhafte Fassung [[g3]], die korrigierte [[g4]].")],
  [lines(1, 2), gaps({"g1": fa([">", ">=", "<", "=="]), "g2": fa(OPT6), "g3": fz(), "g4": fz()})],
  [{"zeilen": [7, 11]}, {"g1": [">="], "g2": ["(double) anzahl / punkte.length * 100"], "g3": ["0.0"], "g4": ["75.0"]}],
  [txt("„mindestens“ heißt `>=` – mit `>` fehlt die 40. In Zeile 11 teilen zwei Ganzzahlen: 2 / 4 = 0, mal 100 bleibt 0 (dann 0.0). "
       "Der Cast muss **vor** der Division stehen: `(double) anzahl / punkte.length * 100` = 3 / 4 · 100 = 75.0. "
       "`(double) (anzahl / punkte.length)` castet zu spät; `* 100.0` am Ende kommt nach der ganzzahligen Division; der `(int)`-Cast schneidet Nachkommastellen ab."),
   hin("Fallen **P6** (Grenzfall „mindestens“) und **P4** (ganzzahlige Division).")],
  ["Rechne die fehlerhafte Zeile 11 mit anzahl = 2 und Länge 4 von links nach rechts aus."], c06)

# ---------------------------------------------------------------- 07
O7 = [("p1", "public static int ersterUeber(int[] r, int grenze) {"),
      ("p2", "    for (int i = 0; i < r.length; i++) {"),
      ("p3", "        if (r[i] > grenze) {"),
      ("p4", "            return i;"),
      ("p5", "        } // Ende if"),
      ("p6", "    } // Ende for"),
      ("p7", "    return -1;"),
      ("p8", "} // Ende Methode"),
      ("d1", "        } else { return -1; }"),
      ("d2", "    for (int i = 1; i < r.length; i++) {"),
      ("d3", "        if (r[i] >= grenze) {"),
      ("d4", "            return r[i];")]

def c07(t):
    tests = 'out("a", ersterUeber(new int[]{3, 9, 4, 12}, 5)); out("b", ersterUeber(new int[]{8, 1}, 5)); out("c", ersterUeber(new int[]{1, 5}, 5)); out("d", ersterUeber(new int[0], 0));'
    want = {"a": "1", "b": "0", "c": "-1", "d": "-1"}
    for seq in t["loesung"]["reihenfolgen"]:
        o, _ = jrun(assemble_order(t, seq), tests); assert o == want, o
    for bad in (["p1", "p2", "p3", "p4", "d1", "p6", "p7", "p8"], ["p1", "d2", "p3", "p4", "p5", "p6", "p7", "p8"],
                ["p1", "p2", "d3", "p4", "p5", "p6", "p7", "p8"], ["p1", "p2", "p3", "d4", "p5", "p6", "p7", "p8"]):
        o, _ = jrun(assemble_order(t, bad), tests); assert o != want, bad

T("W0-L6-07", "Code-Puzzle: Der erste Riese", 3, "Methode implementieren", ["P3", "P6"],
  [txt("*Implementieren Sie die Methode `ersterUeber(r: Reihung von Ganzzahl, grenze: Ganzzahl): Ganzzahl`. Sie liefert den **Index** des ersten "
       "Werts in r, der echt größer als grenze ist. Gibt es keinen solchen Wert (auch bei leerer Reihung), liefert sie −1.* "
       "Setze die Methode zusammen – nicht alle Teile werden gebraucht.")],
  order(O7),
  {"reihenfolgen": [["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]]},
  [txt("Lineare Suche: Beim ersten Treffer sofort den **Index** `i` zurückgeben. Erst **nach** der Schleife steht fest, dass es keinen Treffer gibt → `return -1`. "
       "Die leere Reihung braucht keine Sonderbehandlung – die Schleife läuft dann nicht."),
   hin("Fehlergalerie: `else { return -1; }` in der Schleife ist F6 (prüft nur r[0]); Start bei 1 ist F2; `>=` verfehlt „echt größer“; "
       "`return r[i]` liefert den Wert statt des Index (Falle **P3**).")],
  ["Wo steht fest, dass es keinen Treffer gibt?"], c07)

# ---------------------------------------------------------------- 08
def c08(t):
    korr = 'static int indexKleinster(int[] r) { if (r.length == 0) return -1; int pos = 0; for (int i = 1; i <= r.length - 1; i++) { if (r[i] < r[pos]) pos = i; } return pos; }'
    o, _ = jrun(korr, 'out("g3", indexKleinster(new int[]{5, 3, 8, 3, 1, 4})); out("g4", indexKleinster(new int[]{6, 2, 9, 2})); out("e", indexKleinster(new int[0]));')
    expect(t, "g3", o["g3"], 1); expect(t, "g4", o["g4"], 1); assert o["e"] == "-1"
    fehler = 'static int indexKleinster(int[] r) { if (r.length == 0) return -1; int pos = 0; for (int i = 1; i <= r.length; i++) { if (r[i] < pos) pos = i; } return pos; }'
    o, _ = jrun(fehler, 'try { out("x", indexKleinster(new int[]{5, 3})); } catch (ArrayIndexOutOfBoundsException e) { out("x", "AIOOBE"); }')
    assert o["x"] == "AIOOBE"
    assert t["loesung"][0]["richtig"] == ["c", "d"]

T("W0-L6-08", "Der kaputte Bauplan", 3, "Fehler im Struktogramm", ["P1", "P6", "P9"],
  [txt("*`indexKleinster(r: Reihung von Ganzzahl): Ganzzahl` liefert den Index des kleinsten Werts in r (bei mehreren den kleinsten Index), "
       "für eine leere Reihung −1.* Im Struktogramm stecken **zwei** Fehler."),
   sg("indexKleinster(r: Reihung von Ganzzahl): Ganzzahl", [
       W("Länge von r = 0", [G("−1")]),
       A("pos ← 0"),
       Z("i von 1 bis Länge von r", [W("r[i] < pos", [A("pos ← i")])]),
       G("pos")]),
   txt("**a)** Welche Stellen sind fehlerhaft?"),
   txt("**b)** Korrigiere: Schleifenkopf [[g1]] · Bedingung [[g2]]"),
   txt("Die korrigierte Methode liefert für `{5, 3, 8, 3, 1, 4}` den Wert [[g3]] und für `{6, 2, 9, 2}` den Wert [[g4]].")],
  [choice([("a", "die Abfrage „Länge von r = 0“ mit „gib −1 zurück“"), ("b", "der Startwert „pos ← 0“"),
           ("c", "der Schleifenkopf „für i von 1 bis Länge von r“"), ("d", "die Bedingung „r[i] < pos“"), ("e", "„gib pos zurück“")], mehrfach=True),
   gaps({"g1": fa(["für i von 1 bis Länge von r − 1", "für i von 0 bis Länge von r", "für i von 2 bis Länge von r"]),
         "g2": fa(["r[i] < r[pos]", "r[i] < r[i − 1]", "i < pos", "r[pos] < r[i]"]), "g3": fz(), "g4": fz()})],
  [{"richtig": ["c", "d"]}, {"g1": ["für i von 1 bis Länge von r − 1"], "g2": ["r[i] < r[pos]"], "g3": ["4"], "g4": ["1"]}],
  [txt("„bis“ ist im Struktogramm **einschließlich** – „bis Länge von r“ greift im letzten Durchlauf hinter das Ende (Laufzeitfehler). "
       "`pos` ist ein **Index**; verglichen werden muss der Wert an dieser Stelle: `r[i] < r[pos]`. Der Startwert pos ← 0 ist richtig, "
       "weil nach der Leer-Abfrage r[0] existiert. Mit `<` (nicht `≤`) bleibt bei Gleichstand der kleinere Index: {6, 2, 9, 2} → 1."),
   hin("Fallen **P6/P1**: Zählschleife bis Länge − 1. **P9**: Struktogramm nach EH § 5 – Index und Wert sauber unterscheiden.")],
  ["„für i von a bis b“ schließt b mit ein."], c08)

LEVEL6["aufgaben"] = [k for k in ORDER if k.startswith("W0-L6-")]
