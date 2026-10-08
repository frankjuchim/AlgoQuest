# Level 0.2 – Die Werkstatt (DS 2): Datentypen, Operatoren, Zufall/Runden, Verzweigung, Schleifen
from lib import *

LEVEL2 = {
    "id": "W0-L2", "nr": "0.2", "titel": "Die Werkstatt: Datentypen und Kontrollstrukturen", "ds": [2],
    "ab": "AB 2 „Die Werkstatt“ (Infoteile 1–4, Aufgaben 0–8)",
    "ide": "AQ_W0_Akademie_Geruest.txt – Level 0.2 (Klasse Werkstatt, Testklasse L02WerkstattTest)",
    "intro": [
        txt("In der Werkstatt wird gerechnet, gewogen und gezählt – und zwar **genau**: In Java ist `7 / 2` nicht 3.5 und `-7 % 2` nicht 1."),
        hin("**Merke:** `/` mit zwei Ganzzahlen rechnet **ganzzahlig** · `%` liefert den Rest (Vorzeichen der linken Zahl) · "
            "`(int)` schneidet ab · `(double) a / b` teilt als Kommazahl, `(double) (a / b)` nicht · "
            "Zufallszahl von `von` bis `bis`: `(int) (Math.random() * (bis - von + 1)) + von` · Runden (x ≥ 0): `(int) (x + 0.5)` – "
            "`Math.round` ist in der Akademie tabu."),
    ],
    "aufgaben": [],
}

# ---------------------------------------------------------------- 01
def c01(t):
    o, _ = jrun("", 'out("g1", 29 / 6); out("g2", 29 % 6); out("g3", 6 % 29); out("g4", -11 / 4); out("g5", -11 % 4); out("g6", 12 - 5 * 3 % 4);')
    for g, v in o.items(): expect(t, g, v)

T("W0-L2-01", "Blitz-Kata: Was rechnet Java?", 1, "Datentypen und Ausdrücke", ["P4"],
  [txt("Gib den Wert jedes Ausdrucks an (alle Zahlen sind Ganzzahlen)."),
   tab(["Ausdruck", "`29 / 6`", "`29 % 6`", "`6 % 29`", "`-11 / 4`", "`-11 % 4`", "`12 - 5 * 3 % 4`"],
       [["Wert", "[[g1]]", "[[g2]]", "[[g3]]", "[[g4]]", "[[g5]]", "[[g6]]"]])],
  gaps({f"g{i}": fz() for i in range(1, 7)}),
  {"g1": ["4"], "g2": ["5"], "g3": ["6"], "g4": ["-2"], "g5": ["-3"], "g6": ["9"]},
  [txt("- `29 / 6` = 4 (Rest fällt weg), `29 % 6` = 5.\n- `6 % 29` = 6: 29 passt 0-mal in 6, Rest 6.\n"
       "- `-11 / 4` = −2: Java schneidet zur 0 hin ab (nicht −3).\n- `-11 % 4` = −3: Der Rest hat das Vorzeichen der **linken** Zahl.\n"
       "- `*`, `/`, `%` haben gleichen Rang und werden von links ausgewertet: 5 * 3 = 15, 15 % 4 = 3, 12 − 3 = 9."),
   hin("Falle **P4** (ganzzahlige Division): Mit zwei Ganzzahlen ist `/` immer ganzzahlig.")],
  ["Bei negativen Zahlen: erst wie bei positiven rechnen, dann das Vorzeichen der linken Zahl übernehmen."], c01)

# ---------------------------------------------------------------- 02
EXPR2 = [("e1", "(double) 11 / 4"), ("e2", "(double) (11 / 4)"), ("e3", "(int) 8.99"), ("e4", "1 / 4 * 8.0"),
         ("e5", "3 + 4 + \"x\""), ("e6", "\"x\" + 3 + 4"), ("e7", "'a' + 1"), ("e8", "!(4 > 2) && 3 == 3")]

def c02(t):
    main = "".join(f'out("t{k[1:]}", typ({e})); out("w{k[1:]}", {e});\n' for k, e in EXPR2)
    o, _ = jrun("", main)
    for g, v in o.items(): expect(t, g, v)

T("W0-L2-02", "Der Typ-Detektiv", 2, "Datentypen und Ausdrücke", ["P4"],
  [txt("Gib zu jedem Ausdruck den **Typ** und den **Wert** an. Zeichenketten schreibst du ohne Anführungszeichen, "
       "Wahrheitswerte als `true`/`false`."),
   tab(["Ausdruck", "Typ", "Wert"], [[f"`{e}`", f"[[t{k[1:]}]]", f"[[w{k[1:]}]]"] for k, e in EXPR2]),
   hin("'a' hat den ASCII-Wert 97.")],
  gaps({**{f"t{i}": fa(TYPEN) for i in range(1, 9)},
        "w1": fz(), "w2": fz(), "w3": fz(), "w4": fz(), "w5": ft(6), "w6": ft(6), "w7": fz(), "w8": fa(WF)}),
  {"t1": ["double"], "w1": ["2.75"], "t2": ["double"], "w2": ["2.0"], "t3": ["int"], "w3": ["8"],
   "t4": ["double"], "w4": ["0.0"], "t5": ["String"], "w5": ["7x", "\"7x\""], "t6": ["String"], "w6": ["x34", "\"x34\""],
   "t7": ["int"], "w7": ["98"], "t8": ["boolean"], "w8": ["false"]},
  [txt("- `(double) 11 / 4`: erst umwandeln, dann teilen → 2.75. `(double) (11 / 4)`: erst ganzzahlig teilen (2), dann umwandeln → 2.0.\n"
       "- `(int) 8.99` schneidet ab → 8.\n- `1 / 4 * 8.0`: Von links: `1 / 4` ist ganzzahlig 0, dann 0 * 8.0 = 0.0.\n"
       "- `+` arbeitet von links: 3 + 4 = 7, dann \"7\" + \"x\" → \"7x\". Bei `\"x\" + 3 + 4` ist sofort eine Zeichenkette beteiligt → \"x34\".\n"
       "- `'a' + 1`: Ein Zeichen wird beim Rechnen zur Zahl (97) → 98 vom Typ int.\n- `!(4 > 2)` ist false, also ist die Und-Verknüpfung false."),
   hin("Falle **P4**: Typen und Casts. Die Klammer entscheidet, **wann** umgewandelt wird.")],
  ["Werte Ausdrücke streng von links nach rechts aus und achte auf den Typ jedes Zwischenergebnisses."], c02)

# ---------------------------------------------------------------- 03
ST3 = [("s1", "int a = 5.0;"), ("s2", "double d = 5;"), ("s3", "char c = \"y\";"), ("s4", "String s = 'y';"),
       ("s5", "boolean b = 1;"), ("s6", "int n = (int) 5.5;"), ("s7", "double q = 9 / 2;"), ("s8", "int m = 9 / 2.0;"),
       ("s9", "String t = 3 + \"\";"), ("s10", "boolean g = 2 < 4 < 6;")]

def c03(t):
    for sid, s in ST3:
        ok, _ = jcompile("", s)
        assert (t["loesung"][0][sid] == "ok") == ok, (sid, s, ok)
    o, _ = jrun("", 'double q = 9 / 2; out("q", q);')
    expect(t, "q", o["q"], 1)

T("W0-L2-03", "Kompiliert das?", 1, "Datentypen und Ausdrücke", ["P4"],
  [txt("Ein Lehrling hat zehn Anweisungen in die Werkstatt-Datei getippt. Ordne jede Anweisung zu."),
   txt("Welchen Wert speichert `q` in `double q = 9 / 2;`? [[q]]")],
  [match([(k, f"`{s}`") for k, s in ST3], [("ok", "kompiliert"), ("fehler", "Compilerfehler")]),
   gaps({"q": fz()})],
  [{"s1": "fehler", "s2": "ok", "s3": "fehler", "s4": "fehler", "s5": "fehler", "s6": "ok", "s7": "ok",
    "s8": "fehler", "s9": "ok", "s10": "fehler"},
   {"q": ["4.0"]}],
  [txt("- Eine Ganzzahl passt automatisch in eine Kommazahl (`double d = 5` speichert 5.0), umgekehrt braucht man einen Cast.\n"
       "- `\"y\"` ist eine Zeichenkette, `'y'` ein Zeichen – die Typen sind nicht austauschbar.\n"
       "- `boolean` kennt nur `true`/`false`, keine 0/1.\n- `9 / 2` wird **ganzzahlig** gerechnet (4) und erst dann zu 4.0.\n"
       "- `3 + \"\"` ist eine Zeichenkette \"3\".\n- `2 < 4 < 6` vergleicht zuerst zu `true`, dann `true < 6` – das geht nicht. Richtig: `2 < 4 && 4 < 6`."),
   hin("Falle **P4**: Zeichen vs. Zeichenkette und ganzzahlige Division.")],
  ["Frage dich bei jeder Zeile: Welchen Typ hat die rechte Seite?"], c03)

# ---------------------------------------------------------------- 04
RND = [("r1", "(int) (Math.random() * 8)"), ("r2", "(int) (Math.random() * 8) + 3"),
       ("r3", "(int) Math.random() * 8 + 3"), ("r4", "(int) (Math.random() * 9) - 4")]
RND_OPT = [("a", "(int) (Math.random() * 8) + 5"), ("b", "(int) (Math.random() * 12) + 5"),
           ("c", "(int) (Math.random() * 7) + 5"), ("d", "(int) Math.random() * 8 + 5")]

def c04(t):
    # Math.random() durch kleinsten und groessten moeglichen Wert ersetzen
    main = ""
    for k, e in RND + RND_OPT:
        lo, hi = e.replace("Math.random()", "0.0"), e.replace("Math.random()", "Math.nextDown(1.0)")
        main += f'out("{k}min", {lo}); out("{k}max", {hi});\n'
    o, _ = jrun("", main)
    for k, _e in RND:
        expect(t, k + "min", o[k + "min"], 0); expect(t, k + "max", o[k + "max"], 0)
    good = [k for k, _e in RND_OPT if o[k + "min"] == "5" and o[k + "max"] == "12"]
    assert good == t["loesung"][1]["richtig"], good

T("W0-L2-04", "Die Würfel der Werkstatt", 2, "Datentypen und Ausdrücke", ["P4"],
  [txt("`Math.random()` liefert eine Kommazahl z mit 0 ≤ z < 1. Gib für jeden Ausdruck den kleinsten und den größten möglichen Wert an."),
   tab(["Ausdruck", "kleinster Wert", "größter Wert"], [[f"`{e}`", f"[[{k}min]]", f"[[{k}max]]"] for k, e in RND]),
   txt("**b)** Welcher Ausdruck liefert eine ganzzahlige Zufallszahl von **5 bis 12** (beide möglich, alle gleich wahrscheinlich)?")],
  [gaps({f"{k}{s}": fz() for k, _e in RND for s in ("min", "max")}),
   choice([(k, f"`{e}`") for k, e in RND_OPT])],
  [{"r1min": ["0"], "r1max": ["7"], "r2min": ["3"], "r2max": ["10"], "r3min": ["3"], "r3max": ["3"],
    "r4min": ["-4"], "r4max": ["4"]},
   {"richtig": ["a"]}],
  [txt("`Math.random() * 8` liegt in 0 ≤ … < 8, der Cast macht daraus 0 bis 7. `+ 3` verschiebt auf 3 bis 10. "
       "Bei `(int) Math.random() * 8 + 3` wirkt der Cast nur auf `Math.random()` – das ist immer 0, also immer 3. "
       "`* 9` liefert 9 Werte (0 bis 8), `- 4` verschiebt auf −4 bis 4."),
   txt("Von 5 bis 12 gibt es 12 − 5 + 1 = **8** Werte, also `* 8` und `+ 5`."),
   hin("Falle **P4**: Die Klammer muss um das ganze Produkt, sonst wirkt der Cast zu früh.")],
  ["Anzahl der möglichen Werte = bis − von + 1."], c04)

# ---------------------------------------------------------------- 05
ZEIT = '''int sek = 4000;
int std = sek / 3600;
sek = sek % 3600;
int min = sek / 60;
sek = sek % 60;'''
SCHNITT = '''int summe = 47;
double schnitt = summe / 6;
double schnitt2 = (double) summe / 6;
int gerundet = (int) (schnitt2 + 0.5);
int abgeschnitten = (int) schnitt2;'''

def c05(t):
    lns = ZEIT.split("\n")
    main = ""
    names = ["sek", "std", "sek", "min", "sek"]
    for i, l in enumerate(lns):
        main += l + f'\nout("z{i+1}", {names[i]});\n'
    main += SCHNITT + '\nout("s1", schnitt); out("s3", gerundet); out("s4", abgeschnitten);'
    o, _ = jrun("", main)
    for g, v in o.items(): expect(t, g, v)

T("W0-L2-05", "Die Sanduhr des Alchemisten", 1, "Tracetabelle", ["P8", "P4"],
  [txt("**a)** Der Alchemist rechnet Sekunden in Stunden und Minuten um. Trage in jede Zeile nur den **neuen** Wert ein."),
   code(ZEIT),
   tab(["Zeile", "sek", "std", "min"], [["1", "[[z1]]", "", ""], ["2", "", "[[z2]]", ""], ["3", "[[z3]]", "", ""],
                                        ["4", "", "", "[[z4]]"], ["5", "[[z5]]", "", ""]]),
   txt("**b)** Er berechnet den Durchschnittspreis von sechs Tränken. Gib die Werte an."), code(SCHNITT),
   tab(["Variable", "Wert"], [["schnitt", "[[s1]]"], ["gerundet", "[[s3]]"], ["abgeschnitten", "[[s4]]"]])],
  gaps({"z1": fz(), "z2": fz(), "z3": fz(), "z4": fz(), "z5": fz(), "s1": fz(), "s3": fz(), "s4": fz()}),
  {"z1": ["4000"], "z2": ["1"], "z3": ["400"], "z4": ["6"], "z5": ["40"], "s1": ["7.0"], "s3": ["8"], "s4": ["7"]},
  [txt("4000 / 3600 = 1 Stunde, Rest 400 Sekunden; 400 / 60 = 6 Minuten, Rest 40 Sekunden."),
   txt("`summe / 6` wird ganzzahlig gerechnet (7) und dann zu 7.0. Erst `(double) summe / 6` ergibt 7.833…; "
       "+ 0.5 = 8.333… → `(int)` liefert 8 (kaufmännisch gerundet), ohne + 0.5 wird auf 7 abgeschnitten."),
   hin("Falle **P8**: Eine Zeile pro Anweisung, nur der geänderte Wert. Falle **P4**: ganzzahlige Division vor der Umwandlung.")],
  ["`/` liefert die ganzen Stunden, `%` den Rest."], c05)

# ---------------------------------------------------------------- 06
WETTER = '''public static String wetter(int t) {
    String w = "eisig";
    if (t > 25) {
        w = "heiß";
    }
    if (t > 15) {
        w = "warm";
    }
    if (t > 5) {
        w = "kühl";
    }
    return w;
}'''
WETTER_OPT = ["eisig", "kühl", "warm", "heiß"]

def c06(t):
    calls = {"g1": 30, "g2": 20, "g3": 10, "g4": 0}
    o, _ = jrun(WETTER, "".join(f'out("{g}", wetter({v}));' for g, v in calls.items()))
    for g, v in o.items(): expect(t, g, v, 0)
    soll = 'static String soll(int t) { if (t > 25) return "heiß"; if (t > 15) return "warm"; if (t > 5) return "kühl"; return "eisig"; }'
    var = {
        "a": WETTER.replace("    if (t > 15)", "    else if (t > 15)").replace("    if (t > 5)", "    else if (t > 5)").replace("}\n    else", "} else"),
        "b": 'public static String wetter(int t) { String w = "eisig"; if (t > 5) { w = "kühl"; } if (t > 15) { w = "warm"; } if (t > 25) { w = "heiß"; } return w; }',
        "c": WETTER.replace("> 25", ">= 25").replace("> 15", ">= 15").replace("> 5", ">= 5"),
    }
    korrekt = []
    for k, src in var.items():
        o, _ = jrun(src + "\n" + soll, 'boolean ok = true; for (int t = -10; t <= 40; t++) { if (!wetter(t).equals(soll(t))) ok = false; } out("ok", ok);')
        if o["ok"] == "true": korrekt.append(k)
    ok, _ = jcompile(WETTER.replace('String w = "eisig";', 'String w;'))   # d: ohne Startwert -> Compilerfehler
    assert not ok
    assert korrekt == t["loesung"][1]["richtig"], korrekt

T("W0-L2-06", "Die Wetterfahne – die Reihenfolge zählt", 2, "Fehler im Java-Code", [],
  [txt("Die Wetterfahne der Akademie soll anzeigen: über 25 Grad „heiß“, über 15 „warm“, über 5 „kühl“, sonst „eisig“."),
   code(WETTER),
   txt("**a)** Gib die Rückgabewerte an: `wetter(30)` [[g1]] · `wetter(20)` [[g2]] · `wetter(10)` [[g3]] · `wetter(0)` [[g4]]"),
   txt("**b)** Welche Änderungen machen die Methode korrekt? Wähle **alle** passenden.")],
  [gaps({g: fa(WETTER_OPT) for g in ("g1", "g2", "g3", "g4")}),
   choice([("a", "Reihenfolge beibehalten, aber das zweite und dritte `if` durch `else if` ersetzen."),
           ("b", "Die drei `if`-Anweisungen in umgekehrter Reihenfolge schreiben: erst `t > 5`, dann `t > 15`, dann `t > 25`."),
           ("c", "Überall `>` durch `>=` ersetzen."),
           ("d", "Die Startbelegung `\"eisig\"` weglassen (`String w;`).")], mehrfach=True)],
  [{"g1": ["kühl"], "g2": ["kühl"], "g3": ["kühl"], "g4": ["eisig"]}, {"richtig": ["a", "b"]}],
  [txt("Die drei `if` sind **unabhängig**: Bei 30 Grad sind alle drei Bedingungen wahr, die letzte Zuweisung „kühl“ gewinnt. "
       "Mit `else if` wird nur der **erste** zutreffende Zweig ausgeführt – dann stimmt die absteigende Reihenfolge. "
       "Bei unabhängigen `if` muss die strengste Bedingung zuletzt stehen. `>=` ändert nur die Grenzen, und ohne Startwert "
       "meldet der Compiler „variable w might not have been initialized“."),
   hin("Im Struktogramm wird eine else-if-Kette zur **geschachtelten** Verzweigung im Falsch-Zweig.")],
  ["Spiele wetter(30) Zeile für Zeile durch: Welche Zuweisung passiert zuletzt?"], c06)

# ---------------------------------------------------------------- 07
RUECK = '''public static int rueckwaerts(int n) {
    int r = 0;
    while (n > 0) {
        r = r * 10 + n % 10;
        n = n / 10;
    }
    return r;
}'''

def c07(t):
    inst = RUECK.replace("        n = n / 10;\n", '        int z = n % 10;\n        n = n / 10;\n        System.out.println("row=" + z + ";" + r + ";" + n);\n')
    o, ls = jrun(inst, 'out("ret", rueckwaerts(4705)); out("r1200", rueckwaerts(1200)); out("r0", rueckwaerts(0));')
    rows = [l[4:].split(";") for l in ls if l.startswith("row=")][:4]
    for k, (z, r, n) in enumerate(rows):
        expect(t, f"z{k+1}", z, 0); expect(t, f"r{k+1}", r, 0); expect(t, f"n{k+1}", n, 0)
    expect(t, "ret", o["ret"], 0); expect(t, "a", o["r1200"], 1); expect(t, "b", o["r0"], 1)

T("W0-L2-07", "Der Spiegelzauber der Zahlen", 3, "Tracetabelle", ["P8"],
  [code(RUECK),
   txt("**a)** Vervollständige die Tracetabelle für `rueckwaerts(4705)`: eine Zeile vor der Schleife, dann eine Zeile am **Ende** jedes Durchlaufs. "
       "Die Spalte `n % 10` enthält die Ziffer, die im Durchlauf verwendet wird."),
   tab(["Durchlauf", "n % 10", "r", "n"], [["vor der Schleife", "–", "0", "4705"]] +
       [[str(k), f"[[z{k}]]", f"[[r{k}]]", f"[[n{k}]]"] for k in range(1, 5)]),
   txt("Rückgabewert: [[ret]]"),
   txt("**b)** Gib die Rückgabewerte an: `rueckwaerts(1200)` liefert [[a]], `rueckwaerts(0)` liefert [[b]].")],
  [gaps({**{f"{c}{k}": fz() for c in "zrn" for k in range(1, 5)}, "ret": fz()}), gaps({"a": fz(), "b": fz()})],
  [{"z1": ["5"], "r1": ["5"], "n1": ["470"], "z2": ["0"], "r2": ["50"], "n2": ["47"], "z3": ["7"], "r3": ["507"], "n3": ["4"],
    "z4": ["4"], "r4": ["5074"], "n4": ["0"], "ret": ["5074"]},
   {"a": ["21"], "b": ["0"]}],
  [txt("`n % 10` liefert die letzte Ziffer, `r * 10 + …` hängt sie hinten an `r` an, `n / 10` streicht sie aus `n`. "
       "So entsteht die Zahl rückwärts: 5074. Bei 1200 ergibt sich 0021 – führende Nullen gibt es bei Zahlen nicht, also 21. "
       "Bei n = 0 läuft die Schleife gar nicht."),
   hin("Falle **P8**: Die Zeile „vor der Schleife“ und der Rückgabewert gehören zur vollständigen Tracetabelle.")],
  ["`4705 % 10` = 5 und `4705 / 10` = 470."], c07)

# ---------------------------------------------------------------- 08
PRIM = '''public static boolean istPrimzahl(int n) {
    if (n < 2) {
        return false;
    }
    for (int t = 2; t * t < n; t++) {
        if (n % t == 0) {
            return false;
        }
    }
    return true;
}'''

def c08(t):
    istp = 'static boolean istP(int n) { if (n < 2) return false; for (int t = 2; t < n; t++) if (n % t == 0) return false; return true; }'
    o, _ = jrun(PRIM + "\n" + istp, 'int k = 2; while (istPrimzahl(k) == istP(k)) k++; out("g2", k);')
    expect(t, "g2", o["g2"], 1)
    assert PRIM.split("\n")[t["loesung"][0]["zeilen"][0] - 1].strip().startswith("for (int t = 2; t * t < n")
    fixed = PRIM.replace("t * t < n", "t * t " + t["loesung"][1]["g1"][0] + " n")
    o, _ = jrun(fixed + "\n" + istp, 'boolean ok = true; for (int n = -5; n < 2000; n++) if (istPrimzahl(n) != istP(n)) ok = false; out("ok", ok);')
    assert o["ok"] == "true"

T("W0-L2-08", "Bug-Hunt: Der Primzahl-Prüfer", 3, "Fehler im Java-Code", ["P6"],
  [txt("Die Methode soll prüfen, ob `n` eine Primzahl ist. Sie enthält **genau einen** Fehler."), code(PRIM),
   txt("**a)** Wähle die fehlerhafte Zeile."),
   txt("**b)** Korrigiere den Vergleichsoperator: `t * t` [[g1]] `n`. Gib die **kleinste** Zahl n an, für die die fehlerhafte "
       "Methode ein falsches Ergebnis liefert: [[g2]]")],
  [lines(1, 1), gaps({"g1": fa(["<", "<=", ">", ">=", "=="]), "g2": fz()})],
  [{"zeilen": [5]}, {"g1": ["<="], "g2": ["4"]}],
  [txt("Ein Teiler t mit t · t = n muss noch geprüft werden: Bei n = 4 (und 9, 25, 49 …) ist der einzige kleine Teiler genau die Wurzel. "
       "Mit `<` läuft die Schleife für n = 4 gar nicht (2 · 2 < 4 ist falsch) und die Methode liefert `true`."),
   hin("Falle **P6** (Off-by-one): `<` oder `<=`? Teste die Grenze mit einem Wert, bei dem Gleichheit eintritt.")],
  ["Probiere Quadratzahlen aus."], c08)

LEVEL2["aufgaben"] = [k for k in ORDER if k.startswith("W0-L2-")]
