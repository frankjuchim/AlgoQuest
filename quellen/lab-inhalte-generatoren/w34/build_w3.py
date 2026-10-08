# Baut content/welt3.json – alle Loesungen aus Java-Laeufen (w3_java/w3b_java)
import json
from lib import *
from w3b_java import *   # registriert alle Snippets in J, C

V = J.run()
def v(k):
    assert k in V, "fehlt: " + k
    return V[k]
assert not any(k.endswith(".FEHLER") for k in V), [k for k in V if k.endswith(".FEHLER")]

A = []      # alle Aufgaben
def add(a): A.append(a); return a["id"]

TIEFE_FN = "Der Erstaufruf hat die Rekursionstiefe 0, jeder Selbstaufruf erhöht die Tiefe um 1."

def ras(lst):
    return [list(z) for z in lst]

# =====================================================================
# Level 3.1 – Spiegelsaal: Basisfall und Rekursionstabelle (DS 18)
# =====================================================================
L1 = []
t = rows(V, "L1_01.t")
L1.append(add(aufgabe("W3-L1-01", "Das Echo im Spiegelsaal", 1, "Rekursionstabelle", ["P7"],
    [text("Im Spiegelsaal ruft der Held und hört ein seltsames Echo. Die Methode `ruf` erzeugt es:"),
     code(C["L1_01"]),
     text("Gib den Rückgabewert von `ruf(5)` an (ohne Anführungszeichen) und wie viele Aufrufe von `ruf` dabei insgesamt entstehen (Erstaufruf mitgezählt).\n\n`ruf(5)` liefert [[g1]] · Anzahl der Aufrufe: [[g2]] · größte Rekursionstiefe: [[g3]]")],
    gaps({"g1": txt("code", 8), "g2": zahl(), "g3": zahl()}),
    {"g1": strvar(v("L1_01.r")), "g2": [str(len(t))], "g3": [str(max(x[0] for x in t))]},
    ["Schreibe die Aufrufe untereinander: ruf(5) → ruf(3) → … bis zum Basisfall. Die Rückgaben setzt du danach von unten nach oben zusammen.",
     "Achtung: Die Zahl wird HINTER das Ergebnis des Selbstaufrufs gehängt."],
    [text("Abstieg: ruf(5) → ruf(3) → ruf(1) → ruf(−1). Bei n = −1 greift der Basisfall `n <= 0` und liefert \"*\". "
          "Aufstieg: ruf(1) = \"*\" + 1 = \"*1\", ruf(3) = \"*13\", ruf(5) = \"%s\". Das sind %d Aufrufe, die größte Rekursionstiefe ist %d (Erstaufruf = Tiefe 0). "
          "Weil n in Zweierschritten kleiner wird, hätte ein Basisfall `n == 0` die ungerade 5 übersprungen – hier ist `n <= 0` richtig gewählt (Falle P7)." % (v("L1_01.r"), len(t), max(x[0] for x in t)))])))

t = rows(V, "L1_02.t")
zeilen = []
F = {}; L = {}
for i, (tf, call, ret) in enumerate(t):
    n = call[call.index("(") + 1:-1]
    tcell = "0" if i == 0 else "[[t%d]]" % i
    if i: F["t%d" % i] = zahl(); L["t%d" % i] = [str(tf)]
    F["r%d" % i] = zahl(); L["r%d" % i] = [ret]
    zeilen.append([tcell, call, n, "[[r%d]]" % i])
L1.append(add(aufgabe("W3-L1-02", "Punkte im Gewölbe – Rekursionstabelle", 1, "Rekursionstabelle", ["P7", "P8"],
    [text("Vervollständige die Rekursionstabelle für den Aufruf `punkte(3)`. " + TIEFE_FN),
     code(C["L1_02"]),
     tabelle(["Rekursionstiefe", "Aufruf", "n", "Rückgabe"], zeilen)],
    gaps(F), L,
    ["Fülle zuerst die Tiefen von oben nach unten (Abstieg), dann die Rückgaben von unten nach oben (Aufstieg).",
     "punkte(0) ist der Basisfall. Danach gilt jeweils: Rückgabe = 3 · (Rückgabe der Zeile darunter) − 1."],
    [text("Abstieg: punkte(3) → punkte(2) → punkte(1) → punkte(0); die Tiefen sind 0, 1, 2, 3. Aufstieg: punkte(0) = 2, punkte(1) = 3 · 2 − 1 = 5, "
          "punkte(2) = 3 · 5 − 1 = 14, punkte(3) = 3 · 14 − 1 = 41. Typischer Fehler (P8): Rückgaben schon beim Abstieg eintragen – sie stehen erst fest, wenn der Aufruf darunter fertig ist.")])))

L1.append(add(aufgabe("W3-L1-03", "Rückwärts aus dem Nebel", 1, "Rekursionstabelle", ["P7"],
    [text("Die Methode gibt nur aus (`print` ohne Zeilenumbruch) – sie liefert nichts zurück."),
     code(C["L1_03"]),
     text("Welche Ausgabe erzeugt der Aufruf `rueckwaerts(\"NEBEL\")`?")],
    choice([("a", "`NEBEL`"), ("b", "`LEBEN`"), ("c", "`N`"), ("d", "`NEBELLEBEN`")]),
    {"richtig": ["b"] if v("L1_03.aus") == "LEBEN" else []},
    ["Die Ausgabe steht HINTER dem Selbstaufruf. Wann wird also das erste Zeichen ausgegeben?"],
    [text("Jeder Aufruf ruft zuerst `rueckwaerts` für den Rest auf und gibt sein erstes Zeichen erst danach aus – auf dem Rückweg. "
          "Der Aufruf mit \"L\" (der letzte vor dem Basisfall \"\") wird zuerst fertig, der Erstaufruf mit \"NEBEL\" zuletzt. "
          "Deshalb erscheinen die Zeichen in umgekehrter Reihenfolge: %s. Stünde `print` vor dem Selbstaufruf, käme NEBEL heraus." % v("L1_03.aus"))])))

t = rows(V, "L1_04.t")
zeilen = []; F = {}; L = {}
for i, (tf, call, ret) in enumerate(t):
    n, k = call[call.index("(") + 1:-1].split(", ")
    if i == 0:
        zeilen.append(["0", call, n, k, "[[r0]]"])
    else:
        zeilen.append([str(tf), "halbiere([[n%d]], [[k%d]])" % (i, i), "", "", "[[r%d]]" % i])
        F["n%d" % i] = zahl(); F["k%d" % i] = zahl(); L["n%d" % i] = [n]; L["k%d" % i] = [k]
    F["r%d" % i] = zahl(); L["r%d" % i] = [ret]
for z in zeilen[1:]:
    pass
# Spalten n und k in Folgezeilen aus dem Aufruf lesbar -> Spalten weglassen
zeilen = [[z[0], z[1], z[4]] for z in zeilen]
L1.append(add(aufgabe("W3-L1-04", "Halbieren bis zum Grund", 2, "Rekursionstabelle", ["P8"],
    [text("Dokumentiere den Aufruf `halbiere(45, 0)` in der Rekursionstabelle. Beachte: `/` ist bei Ganzzahlen die ganzzahlige Division."),
     code(C["L1_04"]),
     tabelle(["Rekursionstiefe", "Aufruf", "Rückgabe"], zeilen),
     text("Was berechnet `halbiere(n, 0)` für n ≥ 1? [[w]]")],
    gaps(dict(F, w=auswahl(["die Hälfte von n", "wie oft man n ganzzahlig halbieren kann, bis höchstens 1 übrig ist", "n geteilt durch k", "die Anzahl der Ziffern von n"]))),
    dict(L, w=["wie oft man n ganzzahlig halbieren kann, bis höchstens 1 übrig ist"]),
    ["Rechne 45 / 2 = 22 (ganzzahlig), 22 / 2 = 11, …",
     "Schau auf die Spalte Rückgabe: Nach dem Selbstaufruf wird nicht mehr gerechnet."],
    [text("Die Aufrufe: " + " → ".join(x[1] for x in t) + ". Im Basisfall (n = 1) wird k = %s geliefert. "
          "Weil nach dem Selbstaufruf nichts mehr gerechnet wird (Endrekursion), steht in JEDER Zeile dieselbe Rückgabe %s – sie wird nur durchgereicht. "
          "k zählt die Halbierungen: halbiere(n, 0) ist die abgerundete Zweierlogarithmus-Zahl ⌊log₂ n⌋ (z. B. 32 → 5, 64 → 6)." % (t[-1][2], t[0][2]))])))
assert v("L1_04.h32") == "5" and v("L1_04.h64") == "6"

code5 = C["L1_05"]
L1.append(add(aufgabe("W3-L1-05", "Bug-Hunt: Der übersprungene Grund", 2, "Fehler im Java-Code", ["P7"],
    [text("Die Methode soll die Summe der geraden Zahlen 2 + 4 + … + n liefern (n gerade, n ≥ 0). Der Aufruf `geradeSumme(4)` bricht aber mit einem Laufzeitfehler ab."),
     code(code5),
     text("**Teil 1:** Markiere die fehlerhafte Zeile.\n\n**Teil 2:** Gib die korrigierte Bedingung der if-Anweisung an: `if ([[g1]])`"),
     text("**Teil 3:** Mit welchem Fehler bricht die ursprüngliche Fassung bei `geradeSumme(4)` ab?")],
    [lines(1, 1), gaps({"g1": txt("code", 12)}),
     choice([("a", "`StackOverflowError`"), ("b", "`ArithmeticException`"), ("c", "`ArrayIndexOutOfBoundsException`"), ("d", "Kein Fehler – sie liefert 4.")])],
    [{"zeilen": [3]}, {"g1": ["n==0", "n<=0", "n<1", "n<2", "n<=1", "0==n"]},
     {"richtig": ["a"] if v("L1_05.r") == "StackOverflowError" else []}],
    ["Verfolge geradeSumme(4) → geradeSumme(2) → … Wird n jemals 1?"],
    [text("Weil n in Zweierschritten kleiner wird (4, 2, 0, −2, …), wird n nie 1 – der Basisfall wird übersprungen, es kommen immer neue Rahmen auf den Aufrufstapel: "
          "**StackOverflowError** (Falle P7: Basisfall falsch). Richtig ist `n == 0` (oder robuster `n <= 0`); dann liefert geradeSumme(4) = 4 + 2 + 0 = %s und geradeSumme(10) = %s. "
          "Merke: Der Basisfall muss den kleinsten erlaubten Fall abdecken, und jeder Selbstaufruf muss ihn tatsächlich erreichen." % (v("L1_05k0.r4"), v("L1_05k0.r10")))])))
for i in range(5):
    assert v("L1_05k%d.r4" % i) == "6" and v("L1_05k%d.r0" % i) == "0"

L1.append(add(aufgabe("W3-L1-06", "Bug-Hunt: Das vergessene Ergebnis", 3, "Fehler im Java-Code", ["P7"],
    [text("Die Methode soll zählen, wie oft die Ziffer 7 in n vorkommt (n ≥ 0)."),
     code(C["L1_06"]),
     text("**Teil 1:** `siebener(7077)` liefert [[g1]], richtig wäre [[g2]].\n\n**Teil 2:** Markiere im Code die **zwei** Zeilen, die geändert werden müssen."),
     text("**Teil 3:** Korrigiere die beiden Zeilen: Zeile 8: `return [[g3]];` · Zeile 10: `return [[g4]];`")],
    [gaps({"g1": zahl(), "g2": zahl(), "g3": txt(), "g4": txt()}), lines(1, 2)],
    [{"g1": [v("L1_06.r")], "g2": [v("L1_06k.r")], "g3": ["1+rest", "rest+1"], "g4": ["rest"]}, {"zeilen": [8, 10]}],
    ["In Zeile 6 wird `rest` zwar berechnet – wird es danach auch verwendet?",
     "Das Ergebnis des Erstaufrufs hängt hier nur von der letzten Ziffer ab."],
    [text("Der Selbstaufruf in Zeile 6 wird ausgeführt, aber sein Ergebnis `rest` wird nie verwendet (Falle P7: Ergebnis des rekursiven Aufrufs nicht verwendet). "
          "Deshalb entscheidet nur die letzte Ziffer: 7077 endet auf 7 → %s. Korrekt: Zeile 8 `return 1 + rest;`, Zeile 10 `return rest;` – dann liefert siebener(7077) = %s und siebener(7770) = %s." %
          (v("L1_06.r"), v("L1_06k.r"), v("L1_06k.r2")))])))

t = rows(V, "L1_07.t")
L1.append(add(aufgabe("W3-L1-07", "Vom Code zum Struktogramm", 2, "Code ↔ Struktogramm", ["P9"],
    [text("Die Methode zählt die geraden Werte ab Position i:"),
     code(C["L1_07"]),
     text("Vervollständige das Struktogramm nach EH § 5. Ein Selbstaufruf ist im Struktogramm eine ganz normale Anweisung."),
     struk("anzahlGerade(r: Reihung von Ganzzahl, i: Ganzzahl): Ganzzahl", [
         {"wenn": "i = Länge von r", "dann": [{"gib": "0"}], "sonst": [
             {"anw": "rest ← [[g1]]"},
             {"wenn": "r[i] mod 2 = 0", "dann": [{"gib": "[[g2]]"}], "sonst": [{"gib": "rest"}]}]}]),
     text("Für `r = {4, 7, 2, 6}` liefert `anzahlGerade(r, 0)` den Wert [[g3]]; dabei gibt es [[g4]] Aufrufe.")],
    gaps({"g1": txt("code", 22), "g2": txt(), "g3": zahl(), "g4": zahl()}),
    {"g1": ["anzahlGerade(r,i+1)"], "g2": ["rest+1", "1+rest"], "g3": [v("L1_07.r")], "g4": [str(len(t))]},
    ["Im Struktogramm steht statt `int rest = …;` eine Zuweisung mit ←.", "Aufrufe: i = 0, 1, 2, 3 und der Basisfall i = 4."],
    [text("Der Selbstaufruf wird zur Anweisung „rest ← anzahlGerade(r, i + 1)“, die Rückgabe zu „gib rest + 1 zurück“ – keine Java-Syntax wie `int`, `;` oder `==` im Struktogramm (Falle P9). "
          "Für {4, 7, 2, 6} gibt es %d Aufrufe (i = 0 bis 4, der Basisfall i = Länge zählt mit); gerade sind 4, 2 und 6 → %s." % (len(t), v("L1_07.r")))])))

t = rows(V, "L1_08.t")
zeilen = []; F = {}; L = {}
for i, (tf, call, ret) in enumerate(t):
    zeilen.append([str(tf), call, "[[r%d]]" % i])
    F["r%d" % i] = txt("code", 8); L["r%d" % i] = strvar(ret)
L1.append(add(aufgabe("W3-L1-08", "Der Verdichtungszauber", 3, "Rekursionstabelle", ["P8"],
    [text("Ein Zauberspruch wird „verdichtet“:"),
     code(C["L1_08"]),
     text("Vervollständige die Spalte Rückgabe für den Aufruf `verdichte(\"baaum\")` (Zeichenketten ohne Anführungszeichen). "
          "Hinweis: `s.charAt(0) + verdichte(…)` hängt ein Zeichen vor eine Zeichenkette."),
     tabelle(["Rekursionstiefe", "Aufruf", "Rückgabe"], zeilen),
     text("Was bewirkt `verdichte`? [[w]]")],
    gaps(dict(F, w=auswahl(["entfernt alle doppelten Zeichen im ganzen Wort", "entfernt direkt aufeinanderfolgende Wiederholungen eines Zeichens", "dreht das Wort um", "entfernt alle Vokale"]))),
    dict(L, w=["entfernt direkt aufeinanderfolgende Wiederholungen eines Zeichens"]),
    ["Beginne unten: verdichte(\"m\") ist der Basisfall.", "In Zeile 1 sind die ersten beiden Zeichen gleich – das erste wird dann einfach weggelassen."],
    [text("Aufstieg: \"m\" (Basisfall) → \"um\" (u ≠ m, also \"u\" + \"m\") → \"aum\" → in Zeile 1 sind beide ersten Zeichen \"a\": das erste entfällt, Rückgabe \"aum\" → Zeile 0: \"b\" + \"aum\" = \"%s\". "
          "verdichte entfernt direkt aufeinanderfolgende Wiederholungen (aus \"zzauberrr\" wird \"%s\"); nicht benachbarte gleiche Zeichen bleiben. Jede Zeile bekommt ihre Rückgabe erst beim Aufstieg (P8)." % (v("L1_08.r"), v("L1_08.r2")))])))

# =====================================================================
# Level 3.2 – Hydra: Aufrufbaum und Aufrufe zählen (DS 18)
# =====================================================================
L2 = []
t = rows(V, "L2_01.t")
# Aufrufbaum splitter(4) als Klammerbaum + Pfade
def sbaum(n):
    if n < 2: return ("s%d" % n, None, None)
    return ("s%d" % n, sbaum(n - 1), sbaum(n - 2))
def kl(b):
    if b[1] is None: return b[0]
    return "%s(%s,%s)" % (b[0], kl(b[1]), kl(b[2]))
def pre(b, p=""):
    if b is None: return []
    return [(p, b[0])] + pre(b[1], p + "L") + pre(b[2], p + "R")
def post(b, p=""):
    if b is None: return []
    return post(b[1], p + "L") + post(b[2], p + "R") + [(p, b[0])]
SB = sbaum(4)
assert [x[1] for x in pre(SB)] == [x[1] for x in t]
L2.append(add(aufgabe("W3-L2-01", "Die Kristallspalterin", 1, "Rekursionstabelle", ["P7"],
    [text("Ein Kristall zerspringt im Labyrinth immer wieder:"),
     code(C["L2_01"]),
     text("Gib für den Aufruf `splitter(4)` an:\n\n- Rückgabewert: [[g1]]\n- Anzahl aller Aufrufe (Erstaufruf mitgezählt): [[g2]]\n- größte Rekursionstiefe: [[g3]]\n- wie oft `splitter(2)` aufgerufen wird: [[g4]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": zahl(), "g4": zahl()}),
    {"g1": [v("L2_01.r")], "g2": [str(len(t))], "g3": [str(max(x[0] for x in t))], "g4": [str(sum(1 for x in t if x[1] == "s2"))]},
    ["Zeichne den Aufrufbaum: Jeder Aufruf mit n ≥ 2 hat zwei Kinder (n − 1 links, n − 2 rechts).", "Die Wurzel hat die Tiefe 0."],
    [text("Der Aufrufbaum hat %d Knoten (Aufrufe), die Blätter splitter(1) und splitter(0) liefern je 1. splitter(4) = splitter(3) + splitter(2) = 3 + 2 = %s. "
          "Der tiefste Ast ist s4 → s3 → s2 → s1 mit Tiefe 3. splitter(2) wird zweimal berechnet – gleiche Teilprobleme werden mehrfach gelöst, das macht Baumrekursion teuer." % (len(t), v("L2_01.r")))])))

L2.append(add(aufgabe("W3-L2-02", "Der Aufrufbaum: Wer beginnt wann?", 1, "Rekursionstabelle", [],
    [text("Der Baum zeigt alle Aufrufe von `splitter(4)` aus der vorigen Aufgabe: `s3` steht für den Aufruf `splitter(3)`, linkes Kind = `splitter(n − 1)`, rechtes Kind = `splitter(n − 2)`."),
     code(C["L2_01"]),
     text("Klicke die Aufrufe in der Reihenfolge an, in der sie **beginnen** (so stehen sie auch untereinander in der Rekursionstabelle).")],
    {"kind": "tree", "modus": "klick", "baum": kl(SB)},
    {"folge": [p for p, _ in pre(SB)]},
    ["Java wertet `splitter(n - 1) + splitter(n - 2)` von links nach rechts aus – der linke Teilbaum wird vollständig bearbeitet, bevor der rechte beginnt."],
    [text("Abgearbeitet wird von links nach rechts in die Tiefe: s4, s3, s2, s1, s0, dann das rechte Kind von s3 (s1), danach erst der rechte Teilbaum s2 mit s1 und s0. "
          "Zu jedem Zeitpunkt liegt nur ein Ast des Baums auf dem Aufrufstapel. Genau diese Reihenfolge haben die Zeilen einer Rekursionstabelle.")])))

L2.append(add(aufgabe("W3-L2-03", "Der Aufrufbaum: Wer endet wann?", 2, "Rekursionstabelle", ["P8"],
    [text("Gleicher Aufrufbaum von `splitter(4)` wie zuvor. Klicke die Aufrufe jetzt in der Reihenfolge an, in der sie **enden**, also ihren Wert zurückgeben."),
     code(C["L2_01"])],
    {"kind": "tree", "modus": "klick", "baum": kl(SB)},
    {"folge": [p for p, _ in post(SB)]},
    ["Ein Aufruf endet erst, wenn alle seine Kinder geendet haben.", "Der Erstaufruf endet als letzter."],
    [text("Ein Aufruf kann seinen Wert erst liefern, wenn beide Selbstaufrufe fertig sind. Deshalb enden zuerst die Blätter ganz links (s1, s0), dann s2, dann s1 rechts davon, dann s3 usw.; "
          "der Erstaufruf s4 endet zuletzt. Darum füllt man die Spalte Rückgabe einer Rekursionstabelle beim Aufstieg (P8).")])))

def a2(k, n): return int(v("L2_04.%s%d" % (k, n)))
assert a2("a", 20) == 21 and a2("e", 20) == 11 and a2("b", 20) == 5 and a2("c", 20) > 20000 and a2("d", 20) > 2000000
L2.append(add(aufgabe("W3-L2-04", "Wie schnell wächst die Hydra?", 1, "Effizienz", [],
    [text("Ordne jedem Rekursionsschritt zu, wie die **Anzahl der Aufrufe** mit n wächst (Basisfall jeweils bei kleinem n, z. B. n ≤ 0 bzw. n ≤ 1).")],
    match([("e1", "`return a(n - 1) + 1;`"), ("e2", "`return b(n / 2) + 1;`"), ("e3", "`return c(n - 1) + c(n - 2);`"),
           ("e4", "`return d(n - 1) + d(n - 1);`"), ("e5", "`return e(n - 2) + 1;`")],
          [("lin", "linear: etwa n bzw. n/2 Aufrufe"), ("log", "logarithmisch: etwa log₂ n Aufrufe"), ("exp", "exponentiell: Verdopplung (o. ä.) je Schritt")]),
    {"e1": "lin", "e2": "log", "e3": "exp", "e4": "exp", "e5": "lin"},
    ["Wie viele Selbstaufrufe stehen im Rekursionsschritt – einer oder zwei?", "Wird n um einen festen Betrag kleiner oder halbiert?"],
    [text("Gemessen für n = 20: a %d, b %d, c %d, d %d, e %d Aufrufe. Ein einzelner Selbstaufruf mit n − 1 oder n − 2 ergibt eine Kette → linear; mit n / 2 halbiert sich das Problem → logarithmisch. "
          "Zwei Selbstaufrufe bilden einen Aufrufbaum: c wächst wie die Fibonacci-Zahlen (≈ 1,6-fach je Schritt), d verdoppelt sich je Schritt (2^(n+1) − 1) – exponentiell." %
          (a2("a", 20), a2("b", 20), a2("c", 20), a2("d", 20), a2("e", 20)))])))

teile = [
    {"id": "t1", "code": "public static int produktAb(int[] r, int i) {"},
    {"id": "t2", "code": "    if (i == r.length) {"},
    {"id": "t3", "code": "        return 1;"},
    {"id": "t4", "code": "    }"},
    {"id": "t5", "code": "    return r[i] * produktAb(r, i + 1);"},
    {"id": "t6", "code": "}"},
    {"id": "d1", "code": "        return 0;"},
    {"id": "d2", "code": "    return r[i] * produktAb(r, i);"},
    {"id": "d3", "code": "    if (i == r.length - 1) {"},
]
assert "\n".join(x["code"] for x in teile[:6]) == C["L2_05"]
L2.append(add(aufgabe("W3-L2-05", "Schleifen-Bann: Produkt ohne Schleife", 2, "Methode implementieren", ["P7"],
    [text("Im Labyrinth funktionieren keine Schleifen. Die Methode `produktAb(r, i)` soll das Produkt r[i] · r[i + 1] · … · r[length − 1] **rekursiv** liefern; für i = Länge (nichts mehr übrig) ist das Produkt 1. "
          "Aufgerufen wird sie mit `produktAb(r, 0)`. Bringe die passenden Zeilen in die richtige Reihenfolge – drei Zeilen gehören nicht hinein."),
     code('''public static int produkt(int[] r) {
    int p = 1;
    for (int i = 0; i < r.length; i++) {
        p = p * r[i];
    }
    return p;
}''')],
    order(teile), {"reihenfolgen": [["t1", "t2", "t3", "t4", "t5", "t6"]]},
    ["Die Zählvariable i der Schleife wird zum Parameter. Der Startwert p = 1 wird zum Basisfall.", "Jeder Selbstaufruf muss dem Basisfall näherkommen."],
    [text("Basisfall i == r.length → 1 (das neutrale Element der Multiplikation, wie der Startwert p = 1; mit 0 wäre jedes Produkt 0). Rekursionsschritt: r[i] mal das Produkt ab i + 1. "
          "`produktAb(r, i)` ohne + 1 käme dem Basisfall nie näher (StackOverflowError, P7). Mit `i == r.length - 1` als Basisfall würde der letzte Wert nicht mehr multipliziert, und bei einer leeren Reihung käme es zu einem Indexfehler. "
          "Für {3, 5, 2, 4} liefert die Methode %s, für eine leere Reihung %s." % (v("L2_05.r"), v("L2_05.leer")))])))

an = [int(v("L2_06.a%d" % n)) for n in range(8)]
assert all(an[n] == 1 + an[n - 1] + (an[n - 2] if n >= 2 else 1) + (an[n - 3] if n >= 3 else 1) for n in range(1, 8))
L2.append(add(aufgabe("W3-L2-06", "Zählen ohne Zeichnen", 2, "Effizienz", [],
    [code(C["L2_06"]),
     text("A(n) sei die Anzahl **aller** Aufrufe von `dreier`, die der Aufruf `dreier(n)` auslöst (Erstaufruf mitgezählt). Für n ≤ 0 ist A(n) = 1. "
          "Bestimme die fehlenden Werte, ohne den ganzen Aufrufbaum zu zeichnen."),
     tabelle(["n", "0", "1", "2", "3", "4", "5"], [["A(n)", "1", str(an[1]), str(an[2]), "[[g3]]", "[[g4]]", "[[g5]]"]])],
    gaps({"g3": zahl(), "g4": zahl(), "g5": zahl()}),
    {"g3": [str(an[3])], "g4": [str(an[4])], "g5": [str(an[5])]},
    ["Ein Aufruf verursacht sich selbst plus alle Aufrufe seiner drei Teilbäume: A(n) = 1 + A(n − 1) + A(n − 2) + A(n − 3).",
     "Für negative Werte gilt ebenfalls A = 1 (sofortiger Basisfall)."],
    [text("A(1) = 1 + A(0) + A(−1) + A(−2) = 4, A(2) = 1 + 4 + 1 + 1 = 7, A(3) = 1 + 7 + 4 + 1 = %d, A(4) = 1 + %d + 7 + 4 = %d, A(5) = 1 + %d + %d + 7 = %d. "
          "Gemessen bis n = 7: %s. Die Zahl der Aufrufe wächst exponentiell (fast Verdopplung je Schritt)." %
          (an[3], an[3], an[4], an[4], an[3], an[5], ", ".join(map(str, an))))])))

L2.append(add(aufgabe("W3-L2-07", "Bug-Hunt: Der falsche Zähler", 3, "Fehler im Java-Code", ["P7"],
    [text("Ein Mitschüler will zählen, wie oft `splitter` aufgerufen wird:"),
     code(C["L2_07"]),
     text("Nach `aufrufe = 0;` und `splitter(6)` gilt:\n\n- Rückgabe von `splitter(6)`: [[g1]]\n- Wert von `aufrufe`: [[g2]]\n- tatsächliche Anzahl aller Aufrufe von `splitter`: [[g3]]\n\n"
          "Damit wirklich jeder Aufruf gezählt wird, muss `aufrufe++;` [[g4]].")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": zahl(), "g4": auswahl(["die erste Anweisung der Methode sein (vor dem Basisfall)", "hinter dem Selbstaufruf stehen", "im Basisfall vor return stehen", "entfallen – der Zähler stimmt schon"])}),
    {"g1": [v("L2_07.r")], "g2": [v("L2_07.auf")], "g3": [v("L2_07.alle")], "g4": ["die erste Anweisung der Methode sein (vor dem Basisfall)"]},
    ["Welche Aufrufe erreichen die Zeile `aufrufe++;` gar nicht?", "Im Aufrufbaum: Blätter vs. innere Knoten."],
    [text("Der Zähler steht hinter dem Basisfall: Aufrufe mit n < 2 (die Blätter des Aufrufbaums) kehren vorher zurück und werden nicht gezählt. "
          "Gezählt werden nur die %s inneren Knoten; insgesamt gibt es %s Aufrufe (Blätter = Rückgabe %s, innere Knoten = %s, zusammen %s). "
          "`aufrufe++;` gehört als erste Anweisung an den Anfang – so zählt auch Level 3.1 (fibonacci mit Zähler aufrufe)." %
          (v("L2_07.auf"), v("L2_07.alle"), v("L2_07.r"), v("L2_07.auf"), v("L2_07.alle")))])))

# =====================================================================
# Level 3.3 – Der Wachturm: 2D-Reihung und Flood-Fill (DS 19)
# =====================================================================
L3 = []
RA = ras(KARTE_A)
L3.append(add(aufgabe("W3-L3-01", "Koordinaten im Wachturm", 1, "Datentypen und Ausdrücke", ["P6"],
    [text("Die Karte des Wachturms ist in `char[][] feld` gespeichert, Zugriff immer `feld[Zeile][Spalte]` ('#' Wand, '.' frei)."),
     raster(RA),
     text("- `feld.length` = [[g1]]\n- `feld[0].length` = [[g2]]\n- `feld[3][4]` = [[g3]]\n- `feld[4][2]` = [[g4]]\n- `feld[1][6]` = [[g5]]\n- `feld[5][1]` = [[g6]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": auswahl(["#", ".", "Laufzeitfehler"]), "g4": auswahl(["#", ".", "Laufzeitfehler"]),
          "g5": auswahl(["#", ".", "Laufzeitfehler"]), "g6": auswahl(["#", ".", "Laufzeitfehler"])}),
    {"g1": [v("L3_01.len")], "g2": [v("L3_01.len0")], "g3": [v("L3_01.f3_4")], "g4": [v("L3_01.f4_2")], "g5": [v("L3_01.f1_6")], "g6": [v("L3_01.f5_1")]},
    ["feld.length zählt die Zeilen, feld[0].length die Spalten.", "Gültige Indizes laufen von 0 bis Länge − 1."],
    [text("Die Karte hat %s Zeilen und %s Spalten. feld[3][4] ist Zeile 3, Spalte 4 → '%s'; feld[4][2] → '%s'. "
          "Spalte 6 und Zeile 5 gibt es nicht (Indizes 0 bis 5 bzw. 0 bis 4) → ArrayIndexOutOfBoundsException (P6: Off-by-one, P1: Laufzeitfehler)." %
          (v("L3_01.len"), v("L3_01.len0"), v("L3_01.f3_4"), v("L3_01.f4_2")))])))

L3.append(add(aufgabe("W3-L3-02", "Begehbare Nachbarn", 1, "Datentypen und Ausdrücke", ["P1"],
    [text("Gleiche Karte. Gib an, wie viele **begehbare** Nachbarn ('.') die Felder in der 4er-Nachbarschaft (oben, rechts, unten, links) haben. Nachbarn außerhalb der Karte zählen nicht."),
     raster(RA),
     text("(0|2): [[g1]] · (2|5): [[g2]] · (3|3): [[g3]] · (1|1): [[g4]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": zahl(), "g4": zahl()}),
    {"g1": [v("L3_01.nb0_2")], "g2": [v("L3_01.nb2_5")], "g3": [v("L3_01.nb3_3")], "g4": [v("L3_01.nb1_1")]},
    ["(z|s) bedeutet Zeile z, Spalte s. Oben ist (z − 1|s), rechts (z|s + 1)."],
    [text("(0|2): oben außerhalb, rechts '#', unten (1|2) '.', links '#' → %s. (2|5): oben '#', rechts außerhalb, unten (3|5) '.', links (2|4) '.' → %s. "
          "(3|3): oben '#', rechts '#', unten '#', links (3|2) '.' → %s. (1|1): oben '#', rechts '.', unten '.', links '#' → %s. "
          "Am Rand fehlen Nachbarn – im Programm verhindert `istImFeld` vor dem Zugriff den Absturz (P1)." %
          (v("L3_01.nb0_2"), v("L3_01.nb2_5"), v("L3_01.nb3_3"), v("L3_01.nb1_1")))])))

acht = [[int(x) for x in p.split(",")] for p in v("L3_01.acht33").strip(";").split(";")]
L3.append(add(aufgabe("W3-L3-03", "Acht Richtungen", 1, "Datentypen und Ausdrücke", [],
    [text("Markiere alle **begehbaren** Felder ('.') in der **8er-Nachbarschaft** des Feldes (3|3) – also auch diagonal.")],
    grid(RA), {"zellen": acht, "reihenfolge": False},
    ["Die 8 Nachbarn von (3|3) liegen in den Zeilen 2 bis 4 und den Spalten 2 bis 4 (ohne (3|3) selbst)."],
    [text("Von den acht Nachbarn sind %d begehbar: %s. In der 4er-Nachbarschaft wäre es nur (3|2) – diagonale Felder zählen dort nicht." %
          (len(acht), ", ".join("(%d|%d)" % (a, b) for a, b in acht)))])))

L3.append(add(aufgabe("W3-L3-04", "Lückencode: Zählen in einer Zeile", 2, "Lückencode", ["P6"],
    [text("Die Methode der Klasse Karte soll zählen, wie oft das Zeichen c in Zeile z vorkommt (0 ≤ z < Anzahl der Zeilen)."),
     code(C["L3_04"].replace("s < feld[z].length", "s < [[g1]]").replace("if (feld[z][s] == c)", "if ([[g2]] == c)")),
     text("Für den Wachturm liefert `anzahlInZeile(4, '.')` den Wert [[g3]].")],
    gaps({"g1": txt("code", 14), "g2": txt("code", 12), "g3": zahl()}),
    {"g1": ["feld[z].length", "feld[0].length"], "g2": ["feld[z][s]"], "g3": [v("L3_04.z4")]},
    ["Die Zeile z bleibt fest, nur die Spalte s läuft.", "Zeichen vergleicht man mit ==."],
    [text("Grenze ist die Spaltenzahl `feld[z].length` (bei rechteckigen Karten gleich `feld[0].length`) mit `<` – mit `<=` käme ein Indexfehler (P6). "
          "Verglichen wird `feld[z][s] == c` (Zeichen sind ein einfacher Typ, hier ist == richtig). Zeile 4 des Wachturms enthält %s Punkte." % v("L3_04.z4"))])))

RB = ras(KARTE_B)
folge = [[int(a) for a in x.split("@")[0].split(",")] for x in v("L3_05.folge").strip(";").split(";")]
tiefen = {tuple(int(a) for a in x.split("@")[0].split(",")): int(x.split("@")[1]) for x in v("L3_05.folge").strip(";").split(";")}
FACKEL_S = struk("fackel(z: Ganzzahl, s: Ganzzahl): nichts", [
    {"wenn": "istImFeld(z, s) und feld[z][s] = '.'", "dann": [
        {"anw": "feld[z][s] ← '+'"}, {"aufruf": "fackel(z − 1, s)"}, {"aufruf": "fackel(z, s + 1)"},
        {"aufruf": "fackel(z + 1, s)"}, {"aufruf": "fackel(z, s − 1)"}], "sonst": []}])
L3.append(add(aufgabe("W3-L3-05", "Nebel lüften: die Reihenfolge", 2, "Rekursionstabelle", [],
    [text("Die Fackel lüftet den Nebel mit dem rekursiven Flood-Fill (Nachbarn in der Reihenfolge oben, rechts, unten, links):"),
     FACKEL_S,
     text("Es wird `fackel(0, 0)` auf der Karte unten aufgerufen. Klicke die Felder in der Reihenfolge an, in der sie zu '+' werden.")],
    grid(RB), {"zellen": folge, "reihenfolge": True},
    ["Erst markieren, dann weitergehen: (0|0) wird zuerst markiert, danach wird OBEN versucht (außerhalb), dann RECHTS …",
     "Ein Aufruf geht sofort in die Tiefe – die anderen Nachbarn kommen erst nach der Rückkehr dran."],
    [text("Reihenfolge: " + ", ".join("(%d|%d)" % (a, b) for a, b in folge) + ". Vom Start geht es zunächst den Gang hinunter und rechts herum bis (0|4); "
          "erst auf dem Rückweg kommen (0|2) und der rechte untere Bereich dran. Die Felder (3|0), (4|0) und (4|1) bleiben im Nebel: Sie sind nur über Wände bzw. diagonal mit dem Rest verbunden. "
          "Die Menge der gelüfteten Felder hängt nicht von der Nachbarreihenfolge ab – die Nummerierung schon.")])))

m = int(v("L3_05.m"))
L3.append(add(aufgabe("W3-L3-06", "Wie viele Fackeln brennen?", 2, "Effizienz", [],
    [text("Weiter mit `fackel(0, 0)` auf derselben Karte (Struktogramm wie zuvor)."),
     FACKEL_S, raster(RB),
     text("- Anzahl der markierten Felder m: [[g1]]\n- Anzahl **aller** Aufrufe von `fackel` (auch die, die sofort enden): [[g2]]\n"
          "- Rekursionstiefe des Aufrufs, der das Feld (4|3) markiert: [[g3]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": zahl()}),
    {"g1": [str(m)], "g2": [v("L3_05.aufrufe")], "g3": [str(tiefen[(4, 3)])]},
    ["Nur ein markierender Aufruf löst weitere Aufrufe aus – genau vier.", "Zur Tiefe: Zähle die Felder auf dem Weg vom Start bis (4|3), auf dem die Rekursion dorthin gelangt."],
    [text("Es werden m = %d Felder markiert. Jeder markierende Aufruf ruft genau vier weitere auf, alle anderen enden sofort: 1 + 4 · %d = %s Aufrufe. "
          "(4|3) wird auf dem Weg (0|0) → (1|0) → (1|1) → (2|1) → (2|2) → (2|3) → (3|3) → (3|4) → (4|4) → (4|3) erreicht – Tiefe %d (Erstaufruf = 0). "
          "Die größte Tiefe eines markierenden Aufrufs ist %s." % (m, m, v("L3_05.aufrufe"), tiefen[(4, 3)], v("L3_05.maxT")))])))
assert int(v("L3_05.aufrufe")) == 1 + 4 * m

L3.append(add(aufgabe("W3-L3-07", "Bug-Hunt: Die falsche Reihenfolge", 3, "Fehler im Java-Code", ["P1"],
    [text("Die Klasse Karte besitzt `istImFeld(z, s)`. Diese Fassung von `fackel` stürzt auf Karten ohne Randmauer ab:"),
     code(C["L3_07"].split("\n", 1)[1]),
     text("**Teil 1:** Markiere die fehlerhafte Zeile.\n\n**Teil 2:** Mit welchem Laufzeitfehler bricht `fackel(0, 0)` auf der Karte aus der vorigen Aufgabe ab? [[g1]]\n\n"
          "**Teil 3:** Gib die korrigierte Bedingung an: `if ([[g2]])`")],
    [lines(1, 1), gaps({"g1": auswahl(["ArrayIndexOutOfBoundsException", "StackOverflowError", "NullPointerException", "kein Fehler"]), "g2": txt("code", 30)})],
    [{"zeilen": [2]}, {"g1": [v("L3_07.r")], "g2": ["!istImFeld(z,s)||feld[z][s]!='.'", "!(istImFeld(z,s)&&feld[z][s]=='.')"]}],
    ["`||` wertet von links nach rechts aus und bricht beim ersten `true` ab (Kurzschluss).", "Was passiert bei fackel(−1, 0) im ersten Teil der Bedingung?"],
    [text("Der Kurzschluss schützt nur, wenn die Randprüfung LINKS steht: Bei `fackel(-1, 0)` wird zuerst `feld[-1][0]` ausgewertet → **%s**, bevor `istImFeld` überhaupt geprüft wird. "
          "Korrekt: `!istImFeld(z, s) || feld[z][s] != '.'` – liegt das Feld außerhalb, ist die Bedingung schon wahr und der Zugriff wird nie ausgeführt (P1: Laufzeitfehler nicht ausgeschlossen). "
          "Mit der Korrektur lüftet die Methode dieselben Felder wie zuvor." % v("L3_07.r"))])))
assert v("L3_07k0.karte") == v("L3_05.karte") == v("L3_07k1.karte")

t = rows(V, "L3_08.t")
zeilen = []; F = {}; L = {}
for i, (tf, call, ret) in enumerate(t):
    c, zei = call.split("#")
    if i == 0:
        zeilen.append(["0", c, zei, "[[r0]]"])
    else:
        zeilen.append(["[[t%d]]" % i, c, "[[c%d]]" % i, "[[r%d]]" % i])
        F["t%d" % i] = zahl(); L["t%d" % i] = [str(tf)]
        F["c%d" % i] = auswahl(["'.'", "'#'", "außerhalb"]); L["c%d" % i] = [zei]
    F["r%d" % i] = zahl(); L["r%d" % i] = [ret]
L3.append(add(aufgabe("W3-L3-08", "Der Lichtstrahl", 3, "Rekursionstabelle", ["P8"],
    [text("Ein Lichtstrahl fällt diagonal nach rechts unten durch den Raum, bis er auf eine Wand trifft oder die Karte verlässt:"),
     struk("strahl(z: Ganzzahl, s: Ganzzahl): Ganzzahl", [
         {"wenn": "nicht istImFeld(z, s) oder feld[z][s] = '#'", "dann": [{"gib": "0"}], "sonst": [{"gib": "1 + strahl(z + 1, s + 1)"}]}]),
     raster(RB),
     text("Dokumentiere den Aufruf `strahl(0, 0)` für die Karte. " + TIEFE_FN),
     tabelle(["Rekursionstiefe", "Aufruf", "Zeichen auf dem Feld", "Rückgabe"], zeilen)],
    gaps(F), L,
    ["Jeder Selbstaufruf geht eine Zeile nach unten UND eine Spalte nach rechts.", "Der letzte Aufruf liegt außerhalb der Karte – auch er ist eine Zeile der Tabelle."],
    [text("Der Strahl läuft über (0|0), (1|1), (2|2), (3|3), (4|4) – alle frei – und dann nach (5|5) außerhalb: Basisfall, Rückgabe 0. "
          "Beim Aufstieg kommt je Feld 1 dazu: 1, 2, 3, 4, %s. Auch der Aufruf außerhalb gehört in die Tabelle (P8: jede Zeile, auch der Basisfall). "
          "strahl endet immer, weil jeder Schritt z und s erhöht und die Karte endlich ist." % v("L3_08.r"))])))

# =====================================================================
# Level 3.4 – Kür: Der Ariadnefaden – Backtracking (DS 20)
# =====================================================================
L4 = []
FW_CODE = C["L4_K"].split("\n", 2)[2]   # ohne istImFeld/schritte-Deklaration
L4.append(add(aufgabe("W3-L4-01", "Der Ariadnefaden", 1, "Funktionsweise erläutern", [],
    [text("Backtracking im Labyrinth: `findeWeg(z, s)` markiert ein betretenes Feld vorläufig mit '*', probiert die Nachbarn (oben, rechts, unten, links) und nimmt den Schritt zurück ('x'), wenn keiner zum Ziel führt."),
     text("Welche Aussagen sind richtig? (Mehrere Antworten möglich.)")],
    choice([("a", "Der Aufrufstapel enthält zu jedem Zeitpunkt genau die Felder des aktuellen Weges von S bis zum aktuellen Feld."),
            ("b", "Backtracking findet immer den kürzesten Weg."),
            ("c", "Wegen `||` werden nach dem ersten erfolgreichen Nachbarn keine weiteren Nachbarn mehr versucht."),
            ("d", "Ein mit 'x' markiertes Feld wird kein zweites Mal betreten."),
            ("e", "Ohne die Markierung '*' vor den Selbstaufrufen könnten sich zwei Nachbarfelder endlos gegenseitig aufrufen.")], True),
    {"richtig": ["a", "c", "d", "e"]},
    ["Denke an Theseus: Er wickelt den Faden auf dem Rückweg wieder auf."],
    [text("a, c, d und e sind richtig. b ist falsch: Backtracking liefert den ERSTEN gefundenen Weg – welcher das ist, hängt von der Reihenfolge der Richtungen ab (siehe Aufgabe „Der Umweg“). "
          "'x' und '*' sind keine '.'-Felder mehr und gelten deshalb als nicht begehbar – so endet die Suche immer.")])))

L4.append(add(aufgabe("W3-L4-02", "Wer macht was im findeWeg?", 1, "Funktionsweise erläutern", [],
    [text("Ordne jeder Anweisung aus `findeWeg` ihre Aufgabe zu."), code(FW_CODE)],
    match([("e1", "`schritte++;`"), ("e2", "`feld[z][s] = '*';`"), ("e3", "`feld[z][s] = 'x';`"), ("e4", "`findeWeg(z - 1, s) || findeWeg(z, s + 1) || …`"), ("e5", "`if (alt == 'Z') { return true; }`")],
          [("k1", "zählt jeden Aufruf, auch auf Wänden und außerhalb"), ("k2", "Feld vorläufig auf den Weg setzen (Faden abwickeln)"),
           ("k3", "Schritt zurücknehmen: Sackgasse markieren"), ("k4", "Nachbarn nacheinander probieren, beim ersten Erfolg abbrechen"), ("k5", "Basisfall: Ziel erreicht")]),
    {"e1": "k1", "e2": "k2", "e3": "k3", "e4": "k4", "e5": "k5"},
    ["Basisfälle stehen vor dem Markieren, das Zurücknehmen ganz am Ende."],
    [text("schritte++ steht als erste Anweisung und zählt deshalb jeden Aufruf. '*' setzt das Feld vorläufig auf den Weg, bevor die Nachbarn probiert werden; "
          "'x' nimmt den Schritt zurück, wenn kein Nachbar zum Ziel führt. Die Oder-Verknüpfung wird von links nach rechts ausgewertet und bricht beim ersten true ab. Das Ziel ist ein Basisfall.")])))

KR = ras(KRYPTA)
def btp(x):
    tf, rest = x.split("|", 1); rest, ok = rest.rsplit("|", 1); return tf, rest, ok
bt = [btp(V["L4_K.b%d" % i]) for i in range(int(v("L4_K.bn")))]
betreten = []
for tf, rest, ok in bt:
    rich, weg = rest.split("#", 1)
    if not weg.endswith("#Z"):
        letzte = weg.split(")(")[-1].strip("()")
        betreten.append([int(x) for x in letzte.split("|")])
L4.append(add(aufgabe("W3-L4-03", "Spur in der Krypta", 2, "Rekursionstabelle", [],
    [text("In der Krypta (ohne Randmauer) wird `findeWeg(1, 0)` aufgerufen (S auf (1|0), Z auf (1|4)); Nachbarn: oben, rechts, unten, links."),
     code(FW_CODE),
     text("Klicke die Felder in der Reihenfolge an, in der sie **betreten** werden (also von '.' oder 'S' zu '*' werden) – beginnend mit S, ohne Z.")],
    grid(KR), {"zellen": betreten, "reihenfolge": True},
    ["Von S aus wird zuerst OBEN versucht.", "Führt ein Weg in eine Sackgasse, geht es auf dem Rückweg beim letzten Feld mit noch nicht probierten Nachbarn weiter."],
    [text("Reihenfolge: " + ", ".join("(%d|%d)" % (a, b) for a, b in betreten) + ". Zuerst führt „oben“ in die Sackgasse (0|0), (0|1); sie wird zurückgenommen. "
          "Dann geht es von S nach unten und die untere Zeile entlang; von (1|3) aus wird zuerst oben (0|3) betreten – wieder eine Sackgasse – und danach rechts das Ziel erreicht.")])))

karte_end = v("L4_K.karte").split("/")
sterne = [[z, s] for z in range(len(karte_end)) for s in range(len(karte_end[0])) if karte_end[z][s] == "*"]
kreuze = [[z, s] for z in range(len(karte_end)) for s in range(len(karte_end[0])) if karte_end[z][s] == "x"]
L4.append(add(aufgabe("W3-L4-04", "Die Krypta nach der Suche", 2, "Rekursionstabelle", [],
    [text("Gleicher Aufruf `findeWeg(1, 0)` in der Krypta. Wie sieht die Karte nach dem Ende des Erstaufrufs aus? (S und Z bleiben sichtbar.)"),
     text("**Teil 1:** Markiere alle Felder, die am Ende '*' sind (der gefundene Weg ohne S und Z).\n\n**Teil 2:** Markiere alle Felder, die am Ende 'x' sind (Sackgassen).")],
    [grid(KR), grid(KR)],
    [{"zellen": sterne, "reihenfolge": False}, {"zellen": kreuze, "reihenfolge": False}],
    ["Ein Feld bleibt '*', wenn von ihm aus das Ziel erreicht wurde. Felder, die betreten und wieder zurückgenommen wurden, werden 'x'.",
     "Nie betretene Felder bleiben '.'."],
    [text("Endkarte (Zeilen von oben): " + " / ".join(karte_end) + ". Weg: S → " + " → ".join("(%d|%d)" % (a, b) for a, b in sterne) + " → Z. "
          "Sackgassen 'x': " + ", ".join("(%d|%d)" % (a, b) for a, b in kreuze) + ". Das Feld (2|4) wird nie betreten und bleibt '.', weil von (2|3) aus zuerst „oben“ erfolgreich war.")])))

L4.append(add(aufgabe("W3-L4-05", "Schritte zählen", 2, "Effizienz", [],
    [text("Weiter mit `findeWeg(1, 0)` in der Krypta (Startwert `schritte = 0`)."), raster(KR),
     text("- Rückgabe des Erstaufrufs: [[g1]]\n- Wert von `schritte` am Ende (alle Aufrufe, auch auf Wänden, besuchten Feldern und außerhalb): [[g2]]\n"
          "- Anzahl der Aufrufe, die ein Feld betreten: [[g3]]")],
    gaps({"g1": auswahl(["true", "false"]), "g2": zahl(), "g3": zahl()}),
    {"g1": [v("L4_K.ok")], "g2": [v("L4_K.schritte")], "g3": [str(len(betreten))]},
    ["Jeder betretende Aufruf ruft bis zu vier Nachbarn auf – aber nach dem ersten Erfolg keine weiteren mehr.",
     "Zähle für jedes betretene Feld, wie viele Nachbarn tatsächlich aufgerufen werden (Abbruch bei true)."],
    [text("findeWeg liefert true. Betreten werden %d Felder. Gezählt werden aber alle Aufrufe: Sackgassen-Felder rufen alle vier Nachbarn auf, Felder auf dem Weg nur bis zum ersten Erfolg; "
          "dazu kommen der Erstaufruf und die Aufrufe auf Wände, besuchte Felder, außerhalb und auf Z. Zusammen: schritte = %s." % (len(betreten), v("L4_K.schritte")))])))

zeilen = []; F = {}; L = {}
gi = 0
for i, (tf, rest, ok) in enumerate(bt):
    rich, weg = rest.split("#", 1)
    weg = weg.replace("#Z", "")
    if i in (0,):
        zeilen.append([tf, "– (Aufruf)", weg]); continue
    if i % 3 == 1:
        zeilen.append(["[[t%d]]" % i, rich, weg]); F["t%d" % i] = zahl(); L["t%d" % i] = [tf]
    elif i % 3 == 2:
        zeilen.append([tf, "[[r%d]]" % i, weg]); F["r%d" % i] = auswahl(["oben", "rechts", "unten", "links"]); L["r%d" % i] = [rich]
    else:
        zeilen.append(["[[t%d]]" % i, "[[r%d]]" % i, weg]); F["t%d" % i] = zahl(); L["t%d" % i] = [tf]
        F["r%d" % i] = auswahl(["oben", "rechts", "unten", "links"]); L["r%d" % i] = [rich]
L4.append(add(aufgabe("W3-L4-06", "Abi-Format: Der Weg mit Rekursionstiefe", 3, "Rekursionstabelle", ["P8"],
    [text("Die Tabelle hat das Format aus dem Abitur 2024: eine Zeile für jeden Aufruf, der ein Feld betritt oder das Ziel erreicht. „Richtung“ ist der Schritt vom aufrufenden Feld aus, „Weg“ die Folge der Felder von S bis zum betretenen Feld. "
          "Aufruf: `findeWeg(1, 0)` in der Krypta. " + TIEFE_FN),
     raster(KR),
     tabelle(["Rekursionstiefe", "Richtung", "Weg"], zeilen)],
    gaps(F), L,
    ["Geschwisteraufrufe (verschiedene Nachbarn desselben Feldes) haben dieselbe Rekursionstiefe.", "Die Tiefe ist die Anzahl der Felder im Weg minus 1."],
    [text("Nach der Sackgasse oben (Tiefe 1 und 2) geht es von S aus mit „unten“ wieder in Tiefe 1 weiter – Geschwister haben dieselbe Tiefe. "
          "Die beiden letzten Zeilen (oben in die Sackgasse (0|3), dann rechts zum Ziel) haben ebenfalls dieselbe Tiefe 6. Typischer Fehler (P8): Die Tiefe wird einfach fortlaufend hochgezählt.")])))

UM = ras(UMWEG)
L4.append(add(aufgabe("W3-L4-07", "Der Umweg", 3, "Funktionsweise erläutern", ["P10"],
    [text("Auf dieser kleinen Karte (S auf (1|0), Z auf (1|3)) wird `findeWeg(1, 0)` aufgerufen (Reihenfolge oben, rechts, unten, links)."),
     raster(UM),
     text("- Anzahl der Schritte des gefundenen Weges (Anzahl der Felder nach S bis einschließlich Z): [[g1]]\n- Länge eines kürzesten Weges von S nach Z: [[g2]]\n- Wert von `schritte` am Ende: [[g3]]\n\n"
          "Welche Aussage passt? [[g4]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": zahl(),
          "g4": auswahl(["Backtracking liefert irgendeinen Weg – welchen, hängt von der Reihenfolge der Richtungen ab.",
                         "Backtracking liefert immer den kürzesten Weg.", "Backtracking findet hier keinen Weg."])}),
    {"g1": [str(int(v("L4_U.bn")) - 1)], "g2": ["3"], "g3": [v("L4_U.schritte")],
     "g4": ["Backtracking liefert irgendeinen Weg – welchen, hängt von der Reihenfolge der Richtungen ab."]},
    ["Von S aus wird zuerst OBEN versucht – und von dort aus geht es erfolgreich weiter."],
    [text("findeWeg geht zuerst nach oben und läuft über (0|0), (0|1), (0|2), (0|3) nach unten zu Z: %d Schritte, obwohl der direkte Weg (1|1), (1|2), Z nur 3 Schritte hat. "
          "Die Suche bricht beim ersten Erfolg ab und vergleicht keine Alternativen (schritte = %s). Einen kürzesten Weg findet erst die Breitensuche mit einer Schlange (Welt 4, DS 29). "
          "Begründen heißt im Abitur: Gegenbeispiel angeben und am Ablauf erklären (P10)." % (int(v("L4_U.bn")) - 1, v("L4_U.schritte")))])))

# =====================================================================
# Level 3.5 – Schatzkammer: Teile und herrsche, Mergesort (DS 21)
# =====================================================================
L5 = []
SCH = [3, 8, 12, 17, 23, 31, 36, 42, 50, 57, 64, 71]
t57 = rows(V, "L5_01.t57")
L5.append(add(aufgabe("W3-L5-01", "Das Orakel: binäre Suche rekursiv", 1, "Sortieren und Suchen", [],
    [text("Die Truhen sind aufsteigend nach Gold sortiert. `binaerRek(r, 57, 0, 11)` sucht den Wert 57:"), code(BINAER.strip("\n")),
     text("Klicke nacheinander die Positionen `mid` an, die die Aufrufe untersuchen.")],
    {"kind": "array", "modus": "klick", "start": SCH}, {"folge": [int(x[1].split(",")[2]) for x in t57]},
    ["mid = (lo + hi) / 2 ganzzahlig, zu Beginn lo = 0, hi = 11.", "Ist r[mid] < x, geht es rechts mit lo = mid + 1 weiter."],
    [text("Aufrufe: " + " → ".join("(lo %s, hi %s, mid %s: %s)" % tuple(x[1].split(",")) for x in t57) + ". Gefunden an Index %s nach %d Aufrufen. "
          "Jeder Aufruf halbiert den Suchbereich mindestens – deshalb reichen etwa log₂ n Aufrufe." % (v("L5_01.r57"), len(t57)))])))

t20 = rows(V, "L5_01.t20")
zeilen = []; F = {}; L = {}
for i, (tf, c, ret) in enumerate(t20):
    lo, hi, mid, rm = c.split(",")
    if i == 0:
        zeilen.append(["0", lo, hi, mid, rm, "[[ret0]]"]); F["ret0"] = zahl(); L["ret0"] = [ret]; continue
    zeilen.append([str(tf), "[[lo%d]]" % i, "[[hi%d]]" % i, "[[mid%d]]" % i if mid != "-" else "–", rm if rm != "-" else "–", ret])
    for nm, val in (("lo", lo), ("hi", hi)):
        F["%s%d" % (nm, i)] = zahl(); L["%s%d" % (nm, i)] = [val]
    if mid != "-":
        F["mid%d" % i] = zahl(); L["mid%d" % i] = [mid]
L5.append(add(aufgabe("W3-L5-02", "Die vergebliche Suche", 2, "Rekursionstabelle", ["P8"],
    [text("Gleiche Truhen, jetzt wird der Wert 20 gesucht: `binaerRek(r, 20, 0, 11)`. Vervollständige die Tabelle. " + TIEFE_FN),
     reihung(SCH),
     tabelle(["Tiefe", "lo", "hi", "mid", "r[mid]", "Rückgabe"], zeilen)],
    gaps(F), L,
    ["Ist r[mid] > x, geht es links mit hi = mid − 1 weiter.", "Der letzte Aufruf hat einen leeren Bereich (lo > hi)."],
    [text("Die Suche halbiert: (0, 11) → (0, 4) → (3, 4) → (4, 4) → (4, 3). Im letzten Aufruf ist lo > hi: Basisfall „Bereich leer“ → −1. "
          "Weil das Ergebnis nur durchgereicht wird (Endrekursion), steht in jeder Zeile −1. Auch der Aufruf mit leerem Bereich ist eine Zeile der Tabelle (P8).")])))

L5.append(add(aufgabe("W3-L5-03", "Teilen, herrschen, zusammenführen", 1, "Funktionsweise erläutern", ["P10"],
    [text("Ordne die Bestandteile von `mergeSort` den Schritten von Teile und herrsche zu."), code("public static int[] mergeSort" + C["L5_05"].split("public static int[] mergeSort")[1])],
    match([("e1", "`if (r.length <= 1) { return teilstueck(r, 0, r.length); }`"), ("e2", "`int mitte = r.length / 2;` und die Aufrufe von `teilstueck`"),
           ("e3", "`mergeSort(teilstueck(…))` für beide Hälften"), ("e4", "`return verschmelze(links, rechts);`")],
          [("k1", "Basisfall"), ("k2", "Teilen"), ("k3", "Herrschen (rekursiv lösen)"), ("k4", "Zusammenführen")]),
    {"e1": "k1", "e2": "k2", "e3": "k3", "e4": "k4"},
    ["Bei Mergesort steckt die eigentliche Arbeit im Zusammenführen."],
    [text("Teilen: in der Mitte halbieren (teilstueck kopiert die Hälften). Herrschen: beide Hälften mit demselben Verfahren sortieren. Zusammenführen: verschmelze. "
          "Basisfall: höchstens ein Element ist schon sortiert. Wer im Abitur „Teile und herrsche erläutern“ soll, nennt alle drei Schritte UND den Basisfall am Beispiel (P10).")])))

t = rows(V, "L5_04.t")
zeilen = []; F = {}; L = {}
for i, (tf, c, ret) in enumerate(t):
    von, bis = c.split(",")
    if i in (0, 3):
        zeilen.append([str(tf), "maximumTH(r, %s, %s)" % (von, bis), "[[r%d]]" % i]); F["r%d" % i] = zahl(); L["r%d" % i] = [ret]
    else:
        zeilen.append(["[[t%d]]" % i, "maximumTH(r, [[v%d]], [[b%d]])" % (i, i), "[[r%d]]" % i])
        for nm, val in (("t", str(tf)), ("v", von), ("b", bis), ("r", ret)):
            F["%s%d" % (nm, i)] = zahl(); L["%s%d" % (nm, i)] = [val]
L5.append(add(aufgabe("W3-L5-04", "Die wertvollste Truhe", 2, "Rekursionstabelle", ["P8"],
    [text("Dokumentiere `maximumTH(r, 0, 4)` für `r = {4, 9, 2, 7, 5}`: eine Zeile pro Aufruf in der Reihenfolge ihres Beginns. " + TIEFE_FN),
     code(MAXTH.strip("\n")),
     tabelle(["Tiefe", "Aufruf", "Rückgabe"], zeilen)],
    gaps(F), L,
    ["Linke Hälfte: von … mitte, rechte Hälfte: mitte + 1 … bis. Bei ungerader Länge ist die linke Hälfte größer.", "Insgesamt gibt es 2n − 1 Aufrufe."],
    [text("Teilungsbaum: (0,4) → (0,2) und (3,4); (0,2) → (0,1) und (2,2); (0,1) → (0,0) und (1,1); (3,4) → (3,3) und (4,4). "
          "Das sind 2 · 5 − 1 = 9 Aufrufe; die Blätter liefern ihren Wert, beim Aufstieg gewinnt jeweils der größere. Ergebnis %s. Geschwister haben dieselbe Tiefe (P8)." % v("L5_04.r"))])))

vs = [V["L5_05.v%d" % i].split("|") for i in range(int(v("L5_05.nv")))]
zeilen = []; F = {}; L = {}
for i, (ab, e) in enumerate(vs):
    zeilen.append([str(i + 1), ab.replace("}+{", "} und {"), "[[e%d]]" % i]); F["e%d" % i] = txt("code", 20); L["e%d" % i] = listvar(e.split(", "))
L5.append(add(aufgabe("W3-L5-05", "Truhen verschmelzen", 2, "Sortieren und Suchen", [],
    [text("`mergeSort` sortiert `r = {14, 6, 11, 3, 9, 2, 7}` (Code aus Level 3.3: mitte = Länge / 2, links = r[0 … mitte − 1], rechts = r[mitte … Länge − 1]). "
          "Die Tabelle zeigt alle Aufrufe von `verschmelze` in der Reihenfolge, in der sie stattfinden. Gib jeweils das Ergebnis an (Werte mit Komma getrennt)."),
     tabelle(["Nr.", "verschmelze", "Ergebnis"], zeilen)],
    gaps(F), L,
    ["Zuerst wird die linke Hälfte {14, 6, 11} vollständig sortiert, dann die rechte {3, 9, 2, 7}.", "{14, 6, 11} teilt sich in {14} und {6, 11}."],
    [text("Teilung: {14, 6, 11} | {3, 9, 2, 7}; links weiter {14} | {6, 11}, rechts {3, 9} | {2, 7}. Die Verschmelzungen laufen von unten nach oben, zuerst komplett links: "
          + "; ".join("%s → %s" % (ab.replace("}+{", "} + {"), "{" + e + "}") for ab, e in vs) + ".")])))

L5.append(add(aufgabe("W3-L5-06", "Aufrufe der Schatzkammer zählen", 1, "Effizienz", [],
    [text("Weiter mit `mergeSort(r)` für `r = {14, 6, 11, 3, 9, 2, 7}` (n = 7)."),
     text("- Anzahl der Aufrufe von `mergeSort`: [[g1]]\n- Anzahl der Aufrufe von `verschmelze`: [[g2]]\n- größte Rekursionstiefe von `mergeSort`: [[g3]]\n- Anzahl der Vergleiche `a[i] <= b[j]` insgesamt: [[g4]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": zahl(), "g4": zahl()}),
    {"g1": [v("L5_05.nm")], "g2": [v("L5_05.nv")], "g3": [v("L5_05.maxT")], "g4": [v("L5_06.vgl")]},
    ["Jedes Element wird genau einmal zu einem Blatt (Basisfall).", "verschmelze wird von jedem Aufruf aufgerufen, der kein Basisfall ist."],
    [text("mergeSort: 2n − 1 = %s Aufrufe (7 Blätter + 6 innere Aufrufe); verschmelze: n − 1 = %s. Größte Tiefe %s (z. B. {14, 6, 11} → {6, 11} → {6}). "
          "Vergleiche: 1 + 2 + 1 + 1 + 3 + 5 = %s – etwa n · log₂ n, auch im schlechtesten Fall." % (v("L5_05.nm"), v("L5_05.nv"), v("L5_05.maxT"), v("L5_06.vgl")))])))
assert int(v("L5_05.nm")) == 13 and int(v("L5_05.nv")) == 6 and v("L5_06.vgl") == "13"

teile = [{"id": "t%d" % (i + 1), "code": z} for i, z in enumerate(C["L5_07"].split("\n"))]
teile += [{"id": "d1", "code": "    int mitte = (von + bis + 1) / 2;"}, {"id": "d2", "code": "    int rechts = anzahlTH(r, x, mitte, bis);"}, {"id": "d3", "code": "    if (von > bis) {"}]
assert len(teile) == 13
L5.append(add(aufgabe("W3-L5-07", "Puzzle: Zählen nach Teile und herrsche", 3, "Methode implementieren", ["P7"],
    [text("`anzahlTH(r, x, von, bis)` soll zählen, wie oft x im Bereich r[von] … r[bis] vorkommt (von ≤ bis) – nach Teile und herrsche: ein Element direkt prüfen, sonst in der Mitte teilen, beide Hälften rekursiv zählen und die Ergebnisse addieren. "
          "Bringe die Zeilen in die richtige Reihenfolge. Drei Zeilen gehören nicht hinein.")],
    order(teile), {"reihenfolgen": [["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "t10"], ["t1", "t2", "t3", "t4", "t5", "t6", "t8", "t7", "t9", "t10"]]},
    ["Der Basisfall „ein Element“ ist von == bis.", "mitte gehört zur LINKEN Hälfte: von … mitte und mitte + 1 … bis."],
    [text("Lösung: Basisfall von == bis (ein Element: 1 oder 0), dann mitte = (von + bis) / 2, linke Hälfte von … mitte, rechte Hälfte mitte + 1 … bis, Summe zurückgeben. "
          "Mit (von + bis + 1) / 2 oder mit der rechten Hälfte ab mitte wäre bei zwei Elementen eine Hälfte so groß wie das Ganze → %s (P7). "
          "Für {5, 3, 5, 5, 8, 1, 5} und x = 5 liefert die Methode %s." % (v("L5_07f.r"), v("L5_07.r")))])))

le = v("L5_08.le").split(", "); lt = v("L5_08.lt").split(", ")
BUCH = {"1": "a", "2": "b", "3": "c", "4": "d", "0": "a"}
def paar(code_):
    wert, idx = int(code_) // 10, int(code_) % 10
    return "(%d, %s)" % (wert, "abcde"[idx])
le_p = [paar(x) for x in le]; lt_p = [paar(x) for x in lt]
L5.append(add(aufgabe("W3-L5-08", "Stabil oder nicht?", 3, "Sortieren und Suchen", [],
    [text("Fünf Truhen (Goldwert, Kennbuchstabe) werden mit Mergesort nach dem Goldwert sortiert: (5, a), (2, b), (5, c), (2, d), (1, e). "
          "Gib die Buchstaben in der Reihenfolge des Ergebnisses an (ohne Leerzeichen, z. B. `abcde`)."),
     text("- verschmelze vergleicht mit `a[i] <= b[j]`: [[g1]]\n- verschmelze vergleicht mit `a[i] < b[j]`: [[g2]]\n\nWelche Fassung ist **stabil**? [[g3]]")],
    gaps({"g1": txt("code", 8), "g2": txt("code", 8), "g3": auswahl(["die Fassung mit <=", "die Fassung mit <", "beide", "keine"])}),
    {"g1": ["".join(p[-2] for p in le_p)], "g2": ["".join(p[-2] for p in lt_p)], "g3": ["die Fassung mit <="]},
    ["Teilung wie immer: mitte = 5 / 2 = 2 → {(5,a), (2,b)} | {(5,c), (2,d), (1,e)}.", "Bei Gleichstand nimmt <= das Element der LINKEN Hälfte."],
    [text("Mit <=: %s – gleiche Goldwerte behalten ihre ursprüngliche Reihenfolge (b vor d, a vor c): stabil. Mit <: %s – bei Gleichstand wird das Element der rechten Hälfte zuerst genommen, die Reihenfolge kippt. "
          "Stabil heißt: Elemente mit gleichem Schlüssel behalten ihre Reihenfolge." % (", ".join(le_p), ", ".join(lt_p)))])))

# =====================================================================
# Level 3.6 – Der Torwächter: Quicksort und unbekannte Verfahren (DS 22)
# =====================================================================
L6 = []
def zerlege_py(r, lo, hi):
    r = list(r); tau = []
    piv = r[lo]; g = lo
    for i in range(lo + 1, hi + 1):
        if r[i] < piv:
            g += 1
            if g != i: tau.append([g, i])
            r[g], r[i] = r[i], r[g]
    if g != lo: tau.append([lo, g])
    r[lo], r[g] = r[g], r[lo]
    return r, g, tau
R6 = [5, 8, 2, 9, 1, 7, 3, 6]
rr, gg, tau = zerlege_py(R6, 0, 7)
assert ", ".join(map(str, rr)) == v("L6_01.nach") and str(gg) == v("L6_01.p")
ZERLEGE = QS.split("public static int zerlege")[1]
ZERLEGE = "public static int zerlege" + ZERLEGE.rstrip("\n")
L6.append(add(aufgabe("W3-L6-01", "Der Torwächter zerlegt die Schar", 2, "Sortieren und Suchen", [],
    [text("Führe `zerlege(r, 0, 7)` aus (Pivot = r[lo], kleinere Werte nach vorn). Klicke jeweils die zwei Positionen an, die getauscht werden – in der Reihenfolge des Programms. "
          "**Tausche, bei denen beide Positionen gleich sind (grenze = i), lässt du weg.**"),
     code(ZERLEGE)],
    {"kind": "array", "modus": "tausch", "start": R6, "fertigKnopf": True}, {"tausche": tau},
    ["Pivot ist 5. Für i = 1, 2, …, 7: Ist r[i] < 5, wird grenze erhöht und r[grenze] mit r[i] getauscht.", "Zum Schluss wird das Pivot mit r[grenze] getauscht."],
    [text("Tausche: " + ", ".join("r[%d] ↔ r[%d]" % (a, b) for a, b in tau) + ". Ergebnis {%s}, Rückgabe %s: Links vom Pivot 5 stehen nur kleinere, rechts nur größere Werte. "
          "Verglichen wird 7-mal (i = 1 bis 7)." % (v("L6_01.nach"), v("L6_01.p")))])))

L6.append(add(aufgabe("W3-L6-02", "Was garantiert zerlege?", 1, "Sortieren und Suchen", [],
    [text("Nach `p = zerlege(r, lo, hi)` (Pivot links, Code wie im Level) gilt sicher … (Mehrere Antworten möglich.)")],
    choice([("a", "Das Pivot steht an Position p an seiner endgültigen Stelle."), ("b", "Alle Werte links von p sind kleiner als das Pivot."),
            ("c", "Alle Werte rechts von p sind größer oder gleich dem Pivot."), ("d", "Der Bereich lo … p − 1 ist bereits sortiert."),
            ("e", "p ist immer die Mitte (lo + hi) / 2.")], True),
    {"richtig": ["a", "b", "c"]},
    ["Nach dem Zerlegen werden die beiden Teile ja noch rekursiv sortiert …"],
    [text("Richtig sind a, b, c. Die Teile links und rechts sind nur „vorsortiert“ (getrennt nach kleiner/größer), aber nicht sortiert – deshalb folgen die Selbstaufrufe quickSort(r, lo, p − 1) und quickSort(r, p + 1, hi). "
          "Wo das Pivot landet, hängt von den Werten ab: Ist das Pivot das Minimum, ist p = lo – das ist der schlechteste Fall.")])))

zl = [V["L6_01.z%d" % i].split("|") for i in range(int(v("L6_01.nz")))]
zeilen = []; F = {}; L = {}
for i, (tf, lo, hi, p, nach, vg) in enumerate(zl):
    if i == 0:
        zeilen.append([tf, lo, hi, p, nach, vg]); continue
    zeilen.append(["[[t%d]]" % i, lo, hi, "[[p%d]]" % i, "[[n%d]]" % i, "[[v%d]]" % i])
    F["t%d" % i] = zahl(); L["t%d" % i] = [tf]; F["p%d" % i] = zahl(); L["p%d" % i] = [p]
    F["n%d" % i] = txt("code", 22); L["n%d" % i] = listvar(nach.split(", ")); F["v%d" % i] = zahl(); L["v%d" % i] = [vg]
gesamt = sum(int(x[5]) for x in zl)
L6.append(add(aufgabe("W3-L6-03", "Quicksort vollständig", 2, "Rekursionstabelle", ["P8"],
    [text("Dokumentiere `quickSort(r, 0, 7)` für `r = {5, 8, 2, 9, 1, 7, 3, 6}`: eine Zeile für jeden Aufruf, in dem zerlegt wird (lo < hi), mit der ganzen Reihung nach `zerlege` (Werte mit Komma). " + TIEFE_FN),
     code(QS.split("public static int zerlege")[0].strip("\n")),
     tabelle(["Tiefe", "lo", "hi", "p", "Reihung nach zerlege", "Vergleiche"], zeilen),
     text("Vergleiche insgesamt: [[g]] · Aufrufe von quickSort insgesamt (auch die mit lo ≥ hi): [[q]]")],
    gaps(dict(F, g=zahl(), q=zahl())), dict(L, g=[str(gesamt)], q=[v("L6_01.nq")]),
    ["Nach der ersten Zeile wird zuerst der LINKE Teil 0 … 2 vollständig bearbeitet.", "zerlege(r, lo, hi) vergleicht hi − lo Mal."],
    [text("Ablauf: " + "; ".join("Tiefe %s: (%s, %s) → p = %s, {%s}" % (x[0], x[1], x[2], x[3], x[4]) for x in zl) + ". "
          "Die zwei Aufrufe der Tiefe 1 sind Geschwister. Vergleiche: %s; quickSort wird %s-mal aufgerufen (%d zerlegende + %d sofort endende)." %
          (gesamt, v("L6_01.nq"), len(zl), int(v("L6_01.nq")) - len(zl)))])))

L6.append(add(aufgabe("W3-L6-04", "Der schlechteste Tag des Torwächters", 1, "Effizienz", [],
    [text("Quicksort (Pivot links) sortiert die bereits sortierte Reihung `{1, 2, 3, 4, 5, 6}` mit `quickSort(r, 0, 5)`."),
     text("- Vergleiche insgesamt: [[g1]]\n- Anzahl der Aufrufe, in denen zerlegt wird: [[g2]]\n- größte Rekursionstiefe, in der noch zerlegt wird: [[g3]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": zahl()}),
    {"g1": [v("L6_01.wv")], "g2": [v("L6_01.wn")], "g3": [v("L6_01.wt")]},
    ["Bei sortierter Eingabe ist das linke Pivot immer das Minimum: p = lo, der linke Teil ist leer.", "5 + 4 + 3 + …"],
    [text("Jede Zerlegung trennt nur das Pivot ab: Bereiche der Länge 6, 5, 4, 3, 2 mit 5 + 4 + 3 + 2 + 1 = %s Vergleichen = n(n − 1)/2. "
          "Zerlegt wird %s-mal, in den Tiefen 0 bis %s. Gegenmittel: Pivot aus der Mitte oder „Median aus drei“ wählen." % (v("L6_01.wv"), v("L6_01.wn"), v("L6_01.wt")))])))

R5 = [6, 2, 9, 4, 7, 1]
def sortbis_py(r):
    r = list(r); tau = []
    for ende in range(len(r) - 1, 0, -1):
        m = 0
        for i in range(1, ende + 1):
            if r[i] > r[m]: m = i
        if m != ende: tau.append([m, ende])
        r[m], r[ende] = r[ende], r[m]
    return r, tau
r5, tau5 = sortbis_py(R5)
assert ", ".join(map(str, r5)) == v("L6_05.r")
L6.append(add(aufgabe("W3-L6-05", "Der Turmwächter sortiert", 2, "Sortieren und Suchen", [],
    [text("Ein unbekanntes rekursives Verfahren:"), code(C["L6_05"]),
     text("Führe `sortiereBis(r, 5)` aus. Klicke die getauschten Positionen in der Reihenfolge des Programms an. **Tausche mit m = ende (Wert bleibt stehen) lässt du weg.**")],
    {"kind": "array", "modus": "tausch", "start": R5, "fertigKnopf": True}, {"tausche": tau5},
    ["Jeder Aufruf sucht die Position m des größten Wertes in r[0] … r[ende] und tauscht ihn ans Ende.", "Danach geht es mit ende − 1 weiter."],
    [text("Tausche: " + ", ".join("r[%d] ↔ r[%d]" % (a, b) for a, b in tau5) + ". Jeder Aufruf bringt das Maximum des noch unsortierten Bereichs an Position ende – das ist ein **rekursiver Selectionsort** (Maximum-Variante). "
          "Basisfall: ende ≤ 0 (ein Element ist sortiert). Es gibt %s Aufrufe; die Schleife ist hier erlaubt, die Wiederholung über die Bereiche erledigt die Rekursion." % v("L6_05.aufrufe"))])))

tp = rows(V, "L6_06.t")
zeilen = []; F = {}; L = {}
for i, (tf, c, ret) in enumerate(tp):
    n, bel = c.split("#")
    if i == 0:
        zeilen.append(["0", "pfannkuchen(r, %s)" % n, bel]); continue
    zeilen.append(["[[t%d]]" % i, "pfannkuchen(r, %s)" % n, "[[b%d]]" % i])
    F["t%d" % i] = zahl(); L["t%d" % i] = [str(tf)]; F["b%d" % i] = txt("code", 14); L["b%d" % i] = listvar(bel.split(", "))
L6.append(add(aufgabe("W3-L6-06", "Transfer: Die Pfannkuchen-Golems", 3, "Rekursionstabelle", ["P8", "P10"],
    [text("Die Golems stapeln Pfannkuchen nach Größe. Sie dürfen nur einen oberen Teil des Stapels umdrehen (`wende(r, bis)` kehrt r[0] … r[bis] um)."),
     code(C["L6_06"]),
     text("Dokumentiere `pfannkuchen(r, 4)` für `r = {3, 1, 4, 2}`: Notiere zu jedem Aufruf die Belegung der Reihung **zum Zeitpunkt des Aufrufs** (Werte mit Komma). " + TIEFE_FN),
     tabelle(["Tiefe", "Aufruf", "Belegung beim Aufruf"], zeilen),
     text("Anzahl der Aufrufe von `wende` insgesamt: [[w]] · Was bewirkt das Paar `wende(r, m); wende(r, n - 1);`? [[g]]")],
    gaps(dict(F, w=zahl(), g=auswahl(["Es bringt den größten der ersten n Werte an Position n − 1.", "Es dreht die ganze Reihung um.", "Es tauscht r[m] und r[n − 1], alle anderen bleiben stehen.", "Es sortiert die ersten n Werte."]))),
    dict(L, w=[v("L6_06.wende")], g=["Es bringt den größten der ersten n Werte an Position n − 1."]),
    ["Erster Aufruf: Das Maximum 4 steht an m = 2. wende(r, 2) bringt es nach vorn, wende(r, 3) dann ans Ende.", "Die Belegung notierst du VOR den Änderungen des jeweiligen Aufrufs."],
    [text("Zeile 0: {3, 1, 4, 2}. Mit m = 2: wende(r, 2) → {4, 1, 3, 2}, wende(r, 3) → {2, 3, 1, 4}: Das Maximum liegt hinten. Zeile 1 beginnt mit {2, 3, 1, 4}, … "
          "Jeder Aufruf mit n ≥ 2 wendet zweimal: 2 · (n − 1) = %s Wendungen. Das Verfahren sortiert korrekt (alle Permutationen bis n = 6 geprüft) – es ist ein Selectionsort, der statt Tauschen nur „Umdrehen von oben“ benutzt. "
          "Belegung zum Zeitpunkt des Aufrufs heißt: vor den eigenen Änderungen (P8)." % v("L6_06.wende"))])))
assert v("L6_06.korrekt") == "true"

L6.append(add(aufgabe("W3-L6-07", "Der große Sortiervergleich", 1, "Effizienz", [],
    [text("Ordne jedem Sortierverfahren (aufsteigend, Zählweise aus Welt 2 und Welt 3) seine Eigenschaften zu.")],
    match([("e1", "Mergesort"), ("e2", "Quicksort (Pivot links)"), ("e3", "Insertionsort"), ("e4", "Selectionsort")],
          [("k1", "stabil, immer etwa n · log₂ n Vergleiche, braucht zusätzliche Reihungen"),
           ("k2", "nicht stabil, im Mittel etwa n · log₂ n, bei sortierter Eingabe n(n − 1)/2 Vergleiche"),
           ("k3", "stabil, bei sortierter Eingabe nur n − 1 Vergleiche"),
           ("k4", "nicht stabil, immer n(n − 1)/2 Vergleiche")]),
    {"e1": "k1", "e2": "k2", "e3": "k3", "e4": "k4"},
    ["Welches Verfahren ist unempfindlich gegen die Eingabe? Welches profitiert von vorsortierten Daten?"],
    [text("Mergesort teilt immer in der Mitte (≈ log₂ n Ebenen, je ≈ n Vergleiche) und ist mit <= stabil. Quicksort ist im Mittel schnell, mit Pivot links bei sortierter Eingabe aber quadratisch und nicht stabil. "
          "Insertionsort braucht bei sortierter Eingabe nur n − 1 Vergleiche. Selectionsort vergleicht immer n(n − 1)/2-mal und springt beim Tauschen über gleiche Werte.")])))

so = [v("L6_08.t%d" % i) for i in range(6)]
QSB = QS_BUG.split("public static int zerlege")[0].strip("\n")
opts = [("a", "{1, 2, 3}"), ("b", "{3, 1, 2}"), ("c", "{3, 2, 1}"), ("d", "{2, 1}"), ("e", "{2, 3, 1}")]
richtig = [o[0] for i, o in enumerate(opts) if so[i] == "SO"]
L6.append(add(aufgabe("W3-L6-08", "Bug-Hunt: Der Torwächter dreht sich im Kreis", 3, "Fehler im Java-Code", ["P7"],
    [text("Ein Mitschüler hat quickSort abgetippt (zerlege ist korrekt):"), code(QSB),
     text("**Teil 1:** Markiere die fehlerhafte Zeile.\n\n**Teil 2:** Korrigiere sie: `quickSort(r, [[g1]], hi);`"),
     text("**Teil 3:** Bei welchen Eingaben bricht `quickSort(r, 0, r.length - 1)` mit `StackOverflowError` ab? (Mehrere Antworten möglich.)")],
    [lines(1, 1), gaps({"g1": txt()}), choice(opts, True)],
    [{"zeilen": [5]}, {"g1": ["p+1"]}, {"richtig": richtig}],
    ["Was passiert, wenn das Pivot das Minimum ist (p = lo)?", "Ist der Bereich p … hi dann kleiner als lo … hi?"],
    [text("Der rechte Teil muss bei p + 1 beginnen – das Pivot steht schon richtig. Mit `quickSort(r, p, hi)` ist der Bereich nicht kleiner, wenn p = lo gilt (Pivot ist das Minimum): "
          "Dann wird derselbe Bereich mit derselben Belegung erneut zerlegt – endlos → StackOverflowError (P7: Rekursionsschritt verkleinert nicht). "
          "Betroffen sind alle Eingaben, bei denen irgendwann ein Bereich mit dem Minimum vorn zerlegt wird: hier %s. {3, 1, 2} und {2, 1} laufen zufällig durch." %
          ", ".join(o[1] for o in opts if o[0] in richtig))])))

# =====================================================================
# BOSS – Das Echo der Schlucht
# =====================================================================
B = []
t = rows(V, "B01.t")
zeilen = []; F = {}; L = {}
for i, (tf, c, ret) in enumerate(t):
    n = c[c.index("(") + 1:-1]
    zeilen.append(["0" if i == 0 else "[[t%d]]" % i, c, n, "[[r%d]]" % i])
    if i: F["t%d" % i] = zahl(); L["t%d" % i] = [str(tf)]
    F["r%d" % i] = zahl(); L["r%d" % i] = [ret]
B.append(add(aufgabe("W3-B-01", "Widerhall in der Schlucht", 1, "Rekursionstabelle", ["P8"],
    [text("Dokumentiere den Aufruf `widerhall(10)` in der Rekursionstabelle. " + TIEFE_FN), code(C["B01"]),
     tabelle(["Rekursionstiefe", "Aufruf", "n", "Rückgabe"], zeilen)],
    gaps(F), L, ["Basisfall: n < 3."],
    [text("Abstieg 10 → 7 → 4 → 1 (Basisfall, liefert 1). Aufstieg: 1 + 4 = 5, 5 + 7 = 12, 12 + 10 = %s." % v("B01.r"))])))

B.append(add(aufgabe("W3-B-02", "Das Echo antwortet", 1, "Rekursionstabelle", [],
    [code(C["B02"]), text("Gib die Rückgabe von `ruf(\"HALLO\")` an (ohne Anführungszeichen): [[g1]] · Anzahl der Aufrufe von `ruf` dabei: [[g2]]")],
    gaps({"g1": txt("code", 8), "g2": zahl()}), {"g1": strvar(v("B02.r")), "g2": [v("B02.n")]},
    ["Jeder Aufruf setzt das letzte Zeichen vor und das erste Zeichen hinter das Ergebnis für die Mitte."],
    [text("ruf(\"HALLO\") = 'O' + ruf(\"ALL\") + 'H'; ruf(\"ALL\") = 'L' + ruf(\"L\") + 'A' = \"LLA\". Ergebnis \"%s\" mit %s Aufrufen – die Methode kehrt die Zeichenkette um." % (v("B02.r"), v("B02.n")))])))

B.append(add(aufgabe("W3-B-03", "Stufen ohne Ende", 1, "Fehler im Java-Code", ["P7"],
    [code(C["B03"]), text("`stufen(6)` liefert 3. Was geschieht beim Aufruf `stufen(5)`?")],
    choice([("a", "Er liefert 2."), ("b", "Er liefert 3."), ("c", "Abbruch mit StackOverflowError, weil der Basisfall übersprungen wird."), ("d", "Abbruch mit ArithmeticException.")]),
    {"richtig": ["c"] if v("B03.r5") == "StackOverflowError" else []},
    ["Verfolge n: 5, 3, 1, …"],
    [text("n durchläuft 5, 3, 1, −1, −3, … und wird nie 0 – der Basisfall wird übersprungen, der Aufrufstapel läuft über (P7). Abhilfe: `n <= 0` als Basisfall.")])))

SCHL = ras(SCHLUCHT)
B.append(add(aufgabe("W3-B-04", "Die Karte der Schlucht", 1, "Datentypen und Ausdrücke", ["P6"],
    [text("Die Schlucht ist als `char[][] feld` gespeichert ([Zeile][Spalte], '#' Fels, '.' frei)."), raster(SCHL),
     text("- `feld.length` = [[g1]] · `feld[0].length` = [[g2]]\n- `feld[2][3]` = [[g3]]\n- Anzahl der freien Nachbarn (4er-Nachbarschaft, nur innerhalb der Karte) von (1|3): [[g4]] und von (3|0): [[g5]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": auswahl(["#", ".", "Laufzeitfehler"]), "g4": zahl(), "g5": zahl()}),
    {"g1": [v("B04.len")], "g2": [v("B04.len0")], "g3": [v("B04.f23")], "g4": [v("B04.nb13")], "g5": [v("B04.nb30")]},
    ["feld.length = Zeilen, feld[0].length = Spalten."],
    [text("%s Zeilen, %s Spalten; feld[2][3] = '%s'. (1|3): oben (0|3) '#', rechts (1|4) '.', unten (2|3) '.', links (1|2) '#' → %s. (3|0): oben (2|0) '.', rechts (3|1) '.', unten außerhalb, links außerhalb → %s." %
          (v("B04.len"), v("B04.len0"), v("B04.f23"), v("B04.nb13"), v("B04.nb30")))])))

t = rows(V, "B05.t")
B.append(add(aufgabe("W3-B-05", "Tiefenmessung", 1, "Sortieren und Suchen", [],
    [text("Die Messpunkte sind aufsteigend nach Tiefe sortiert. Gesucht wird 14 mit `binaerRek(r, 14, 0, 8)` (mid = (lo + hi) / 2). Klicke die untersuchten Positionen mid der Reihe nach an.")],
    {"kind": "array", "modus": "klick", "start": [2, 5, 9, 14, 20, 27, 33, 41, 48]}, {"folge": [int(x[1].split(",")[2]) for x in t]},
    ["Erster Aufruf: lo = 0, hi = 8."],
    [text("mid-Folge: " + ", ".join(x[1].split(",")[2] for x in t) + " – gefunden an Index %s." % v("B05.r"))])))

B.append(add(aufgabe("W3-B-06", "Zerlegt am Abgrund", 2, "Sortieren und Suchen", [],
    [text("Gib die Belegung von `r = {7, 3, 9, 1, 8, 5}` nach `zerlege(r, 0, 5)` an (Pivot links, Code aus Level 3.6) und die Rückgabe."),
     text("Belegung (Werte mit Komma): [[g1]] · Rückgabe: [[g2]] · Anzahl der Vergleiche r[i] < pivot: [[g3]]")],
    gaps({"g1": txt("code", 20), "g2": zahl(), "g3": zahl()}),
    {"g1": listvar(v("B06.nach").split(", ")), "g2": [v("B06.p")], "g3": ["5"]},
    ["Pivot 7: kleinere Werte werden nacheinander hinter die Grenze getauscht."],
    [text("Ablauf: 3 < 7 (Grenze 1, Selbsttausch), 9 nein, 1 < 7 (Grenze 2: tausche r[2], r[3] → 7, 3, 1, 9, 8, 5), 8 nein, 5 < 7 (Grenze 3: tausche r[3], r[5] → 7, 3, 1, 5, 8, 9), "
          "Schlusstausch r[0] ↔ r[3]: {%s}, Rückgabe %s, 5 Vergleiche." % (v("B06.nach"), v("B06.p")))])))

PI = ras(PILZE)
kend = v("B07.karte").split("/")
ernte = [[z, s] for z in range(len(PILZE)) for s in range(len(PILZE[0])) if PILZE[z][s] == "P" and kend[z][s] == "-"]
B.append(add(aufgabe("W3-B-07", "Die Pilzkolonie", 2, "Rekursionstabelle", [],
    [text("Leuchtpilze 'P', die oben, rechts, unten oder links aneinandergrenzen, bilden eine Kolonie. Die Methode erntet die ganze Kolonie:"), code(C["B07"].split("\n", 1)[1]),
     text("Markiere alle Felder, die nach `ernte(2, 2)` geerntet ('-') sind.")],
    grid(PI), {"zellen": ernte, "reihenfolge": False},
    ["Diagonal benachbarte Pilze gehören NICHT zur Kolonie."],
    [text("Geerntet werden %s Pilze: %s. (0|2) und (1|4) berühren die Kolonie nur diagonal und bleiben stehen." % (v("B07.r"), ", ".join("(%d|%d)" % (a, b) for a, b in ernte)))])))
assert int(v("B07.r")) == len(ernte)

B.append(add(aufgabe("W3-B-08", "Funkenflug", 2, "Effizienz", [],
    [code(C["B08"]), text("- `funken(3)` liefert [[g1]] und löst [[g2]] Aufrufe aus (Erstaufruf mitgezählt).\n- Für `funken(4)` sind es [[g3]] Aufrufe.\n- Wird n um 1 größer, dann [[g4]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": zahl(), "g4": auswahl(["verdoppelt sich die Anzahl der Aufrufe ungefähr.", "kommt ein Aufruf dazu.", "kommen zwei Aufrufe dazu.", "bleibt die Anzahl gleich."])}),
    {"g1": [v("B08.v3")], "g2": [v("B08.a3")], "g3": [v("B08.a4")], "g4": ["verdoppelt sich die Anzahl der Aufrufe ungefähr."]},
    ["A(n) = 1 + 2 · A(n − 1), A(0) = 1."],
    [text("A(0) = 1, A(1) = 3, A(2) = 7, A(3) = %s, A(4) = %s: A(n) = 2^(n+1) − 1. Je Schritt verdoppelt sich die Zahl – funken(20) braucht schon %s Aufrufe. Eine Variable `int h = funken(n - 1); return h + h;` käme mit n + 1 Aufrufen aus." %
          (v("B08.a3"), v("B08.a4"), v("B08.a20")))])))

SU = C["B09"]
B.append(add(aufgabe("W3-B-09", "Die Suche, die nicht endet", 2, "Fehler im Java-Code", ["P7"],
    [text("Die rekursive Suche in r = {4, 10, 15, 22, 30, 37} liefert für 22 und 37 die richtigen Indizes, `suche(r, 3, 0, 5)` bricht aber mit StackOverflowError ab."), code(SU),
     text("**Teil 1:** Markiere die fehlerhafte Zeile.\n\n**Teil 2:** Korrigiere: `return suche(r, x, lo, [[g1]]);`")],
    [lines(1, 1), gaps({"g1": txt()})],
    [{"zeilen": [12]}, {"g1": ["mid-1"]}],
    ["Verfolge suche(r, 3, 0, 0): Wird der Bereich kleiner?"],
    [text("Bei suche(r, 3, 0, 0) ist mid = 0 und r[0] = 4 > 3 → suche(r, 3, 0, 0) mit demselben Bereich: endlos (P7). mid wurde schon geprüft und gehört nicht mehr in den Bereich: hi = mid − 1. "
          "Korrigiert liefert die Suche für 3 und 12 den Wert −1 (geprüft: %s, %s)." % (v("B09k.r3"), v("B09k.r12")))])))
assert v("B09.r3") == "SO" and v("B09.r22") == "3"

vs = [V["B10.v%d" % i].split("|") for i in range(int(v("B10.nv")))]
zeilen = []; F = {}; L = {}
for i, (ab, e) in enumerate(vs):
    zeilen.append([str(i + 1), ab.replace("}+{", "} und {"), "[[e%d]]" % i]); F["e%d" % i] = txt("code", 16); L["e%d" % i] = listvar(e.split(", "))
B.append(add(aufgabe("W3-B-10", "Echos verschmelzen", 2, "Sortieren und Suchen", [],
    [text("mergeSort (mitte = Länge / 2) sortiert `{9, 4, 7, 1, 6}`. Gib die Ergebnisse der verschmelze-Aufrufe in ihrer Reihenfolge an (Werte mit Komma)."),
     tabelle(["Nr.", "verschmelze", "Ergebnis"], zeilen)],
    gaps(F), L, ["Erst wird {9, 4} vollständig sortiert, dann {7, 1, 6}."],
    [text("; ".join("%s → {%s}" % (ab.replace("}+{", "} + {"), e) for ab, e in vs) + ".")])))

teile = [{"id": "t%d" % (i + 1), "code": z} for i, z in enumerate(C["B11"].split("\n"))]
teile += [{"id": "d1", "code": "    if (feld[z][s] == '#' || s < 0) {"}, {"id": "d2", "code": "    return gangLinks(z, s - 1);"}, {"id": "d3", "code": "    return 1 + gangLinks(z, s);"}]
B.append(add(aufgabe("W3-B-11", "Puzzle: Der Gang nach links", 2, "Methode implementieren", ["P1", "P7"],
    [text("`gangLinks(z, s)` (Klasse Karte, Attribut `feld`) soll zählen, wie viele freie Felder man ab (z|s) einschließlich nach links geht, bis eine Wand '#' oder der linke Rand kommt (z ist gültig). "
          "Bringe die Zeilen in die richtige Reihenfolge; drei Zeilen gehören nicht hinein.")],
    order(teile), {"reihenfolgen": [["t1", "t2", "t3", "t4", "t5", "t6"]]},
    ["Die Randprüfung muss VOR dem Feldzugriff stehen (Kurzschluss)."],
    [text("Die Bedingung `s < 0 || feld[z][s] == '#'` prüft zuerst den Rand; umgekehrt käme es bei s = −1 zur %s (P1). Rekursionsschritt: 1 + gangLinks(z, s − 1). Für die Schlucht liefert gangLinks(3, 3) den Wert %s." %
          (v("B11f.r"), v("B11.r33")))])))

GR = ras(GROTTE)
bt = [btp(V["B12.b%d" % i]) for i in range(int(v("B12.bn")))]
betreten = []
for tf, rest, ok in bt:
    rich, weg = rest.split("#", 1)
    if not weg.endswith("#Z"):
        betreten.append([int(x) for x in weg.split(")(")[-1].strip("()").split("|")])
B.append(add(aufgabe("W3-B-12", "Durch die Grotte", 3, "Rekursionstabelle", [],
    [text("In der Grotte wird `findeWeg(0, 0)` aufgerufen (Backtracking wie in Level 3.4; Nachbarn oben, rechts, unten, links). Klicke die Felder in der Reihenfolge an, in der sie betreten werden – mit S, ohne Z.")],
    grid(GR), {"zellen": betreten, "reihenfolge": True},
    ["Von S aus ist oben außerhalb – also zuerst rechts."],
    [text("Reihenfolge: " + ", ".join("(%d|%d)" % (a, b) for a, b in betreten) + ". Der Weg nach rechts endet in einer Sackgasse ((0|1), (0|2), (1|2) werden 'x'), dann führt „unten“ zum Ziel. Endkarte: " + " / ".join(v("B12.karte").split("/")) + ".")])))

e = [v("B13.e%d" % i) for i in range(int(v("B13.ne")))]
zeilen = [["0", "echoSort(r, 4)", e[0].split("#")[1]]] + [["%d" % i, "echoSort(r, %s)" % e[i].split("#")[0], "[[b%d]]" % i] for i in range(1, len(e))]
F = {"b%d" % i: txt("code", 14) for i in range(1, len(e))}; L = {"b%d" % i: listvar(e[i].split("#")[1].split(", ")) for i in range(1, len(e))}
B.append(add(aufgabe("W3-B-13", "Das unbekannte Echo-Verfahren", 3, "Rekursionstabelle", ["P8"],
    [code(C["B13"]), text("Dokumentiere die Aufrufe von `echoSort` für `echoSort(r, 4)` mit `r = {4, 2, 5, 1}`: Belegung zum Zeitpunkt des Aufrufs (Werte mit Komma)."),
     tabelle(["Tiefe", "Aufruf", "Belegung beim Aufruf"], zeilen),
     text("Anzahl der Vergleiche `r[i] > r[i + 1]` insgesamt: [[v]]")],
    gaps(dict(F, v=zahl())), dict(L, v=[v("B13.vgl")]),
    ["welle ist ein rekursiver Durchlauf von Bubblesort: Der größte Wert wandert nach hinten.", "welle(r, 0) läuft immer bis zum Ende der Reihung – unabhängig von n."],
    [text("Belegungen: " + " | ".join(x.split("#")[1] for x in e) + ". welle wandert wie ein Bubblesort-Durchlauf. Da welle immer bis r.length − 1 läuft, gibt es bei 3 Durchläufen 3 · 3 = %s Vergleiche – auch dort, wo hinten schon sortiert ist. "
          "Verbesserung: welle nur bis n − 1 laufen lassen." % v("B13.vgl"))])))

B.append(add(aufgabe("W3-B-14", "Der leiseste Ton", 3, "Struktogramm lesen", ["P9"],
    [text("Die Operation liefert die Position des kleinsten Wertes in r[von] … r[bis] nach Teile und herrsche (bei Gleichstand die linke):"),
     struk("posMin(r: Reihung von Ganzzahl, von: Ganzzahl, bis: Ganzzahl): Ganzzahl", [
         {"wenn": "von = bis", "dann": [{"gib": "von"}], "sonst": [
             {"anw": "mitte ← (von + bis) / 2"}, {"anw": "l ← [[g1]]"}, {"anw": "re ← posMin(r, mitte + 1, bis)"},
             {"wenn": "[[g2]]", "dann": [{"gib": "l"}], "sonst": [{"gib": "re"}]}]}]),
     text("Für `r = {8, 3, 6, 3, 9, 4}` liefert `posMin(r, 0, 5)` den Wert [[g3]] mit [[g4]] Aufrufen.")],
    gaps({"g1": txt("code", 20), "g2": txt("code", 16), "g3": zahl(), "g4": zahl()}),
    {"g1": ["posMin(r,von,mitte)"], "g2": ["r[l]<=r[re]", "r[l]≤r[re]", "r[re]>=r[l]", "r[re]≥r[l]"], "g3": [v("B14.r")], "g4": [v("B14.n")]},
    ["Die linke Hälfte ist von … mitte.", "Bei Gleichstand soll l gewinnen."],
    [text("l ← posMin(r, von, mitte); die Bedingung r[l] ≤ r[re] sorgt dafür, dass bei Gleichstand (3 an Index 1 und 3) die linke Position gewinnt → %s. 2n − 1 = %s Aufrufe." % (v("B14.r"), v("B14.n")))])))

B.append(add(aufgabe("W3-B-15", "Quicksort auf dem Prüfstand", 3, "Effizienz", [],
    [text("Quicksort mit Pivot links bekommt bereits sortierte Reihungen. Gib die Anzahl der Vergleiche r[i] < pivot an: n = 10: [[g1]] · n = 20: [[g2]]\n\n"
          "Wie verändert sich die Anzahl, wenn sich n verdoppelt? [[g3]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": auswahl(["etwa vervierfacht", "etwa verdoppelt", "um 1 größer", "gleich"])}),
    {"g1": [v("B15.v10")], "g2": [v("B15.v20")], "g3": ["etwa vervierfacht"]},
    ["Bei sortierter Eingabe ist der linke Teil immer leer: (n − 1) + (n − 2) + … + 1."],
    [text("n(n − 1)/2: 45 für n = 10, 190 für n = 20, %s für n = 40 – quadratisches Wachstum, bei Verdopplung etwa der Faktor 4. Mergesort bliebe bei etwa n · log₂ n." % v("B15.v40"))])))

assert v("B15.v10") == "45" and v("B15.v20") == "190"

# =====================================================================
LEVELS = [
    ("W3-L1", "3.1", "Spiegelsaal: Basisfall und Rekursionstabelle", [18], "AB 1 Rekursion – Infoteile 1–3, Aufgaben 0–4",
     "AQ_W3_L3_Labyrinth_Geruest.txt – Level 3.1 (Klasse Rekursion, Basis: fakultaet, summeBis, potenz)",
     [hinweis("**Merke:** Jede Rekursion braucht einen **Basisfall** (Antwort steht sofort fest) und einen **Rekursionsschritt**, der dem Basisfall näherkommt. "
              "Rekursionstabelle: eine Zeile pro Aufruf in der Reihenfolge des Beginns, **Erstaufruf = Tiefe 0**, Rückgaben beim Aufstieg von unten nach oben."),
      text("Im Spiegelsaal übst du, rekursive Methoden Schritt für Schritt zu verfolgen und Basisfall-Fehler zu finden.")], L1),
    ("W3-L2", "3.2", "Hydra: Aufrufbaum und Aufrufe zählen", [18], "AB 1 Rekursion – Infoteile 4–5, Aufgaben 5–6",
     "AQ_W3_L3_Labyrinth_Geruest.txt – Level 3.1 (Klasse Rekursion, Erweiterung/Experte: summeAb, fibonacci mit Zähler aufrufe)",
     [hinweis("**Merke:** Ruft sich eine Methode zweimal auf, entsteht ein **Aufrufbaum**. Abgearbeitet wird von links nach rechts in die Tiefe. "
              "Anzahl der Aufrufe: A(n) = 1 + Aufrufe der Teilbäume – Baumrekursion wächst oft exponentiell."),
      text("Die Hydra lässt für jeden Kopf zwei neue wachsen – zähle mit, bevor sie dich überrollt.")], L2),
    ("W3-L3", "3.3", "Wachturm: 2D-Reihung und Flood-Fill", [19], "AB 2 Dungeon-Karte – Teil 1 (Aufgaben 1–5)",
     "AQ_W3_L3_Labyrinth_Geruest.txt – Level 3.2 (Klasse Karte, Basis und Erweiterung: istImFeld, lueften)",
     [hinweis("**Merke:** `feld[z][s]` – immer [Zeile][Spalte]. `feld.length` = Zeilen, `feld[0].length` = Spalten. "
              "Vor jedem Zugriff Rand prüfen – die Prüfung steht **links** vom Zugriff. Flood-Fill: erst markieren, dann die Nachbarn (oben, rechts, unten, links)."),
      text("Im Wachturm liegt Nebel. Lies die Karte sicher aus und lüfte den Nebel Feld für Feld.")], L3),
    ("W3-L4", "3.4", "Kür: Ariadnefaden – Backtracking", [20], "AB 2 Dungeon-Karte – Teil 2 (Aufgaben 7–9)",
     "AQ_W3_L3_Labyrinth_Geruest.txt – Level 3.2 Experte (findeWeg) · AQ_W3_DungeonRennen_Geruest.txt (Dungeon-Rennen)",
     [hinweis("**Merke:** Backtracking = ausprobieren und Schritt zurücknehmen. Feld vorläufig '*', Nachbarn probieren, beim ersten Erfolg abbrechen (`||`), sonst 'x'. "
              "Der Aufrufstapel ist der Ariadnefaden – Geschwisteraufrufe haben dieselbe Tiefe."),
      text("Kür-Level: Folge dem Faden durch die Krypta – und finde heraus, warum Backtracking nicht immer den kürzesten Weg nimmt.")], L4),
    ("W3-L5", "3.5", "Schatzkammer: Teile und herrsche", [21], "AB 3 Teile und herrsche – Teil 1 (Aufgaben 0–4)",
     "AQ_W3_L3_Labyrinth_Geruest.txt – Level 3.3 (Klasse TeileUndHerrsche, Basis und Erweiterung: binaerRek, maximumTH, mergeSort)",
     [hinweis("**Merke:** Teile und herrsche = **Teilen** (meist in der Mitte), **Herrschen** (Teile rekursiv lösen, Basisfall direkt) und **Zusammenführen**. "
              "Grenzen: von … mitte und mitte + 1 … bis, mitte = (von + bis) / 2."),
      text("Die Zwerge teilen den Schatz – und sortieren ihn mit Mergesort.")], L5),
    ("W3-L6", "3.6", "Torwächter: Quicksort und unbekannte Verfahren", [22], "AB 3 Teile und herrsche – Teil 2 (Aufgaben 5–8)",
     "AQ_W3_L3_Labyrinth_Geruest.txt – Level 3.3 Experte (zerlege, quickSort mit Zähler vergleiche)",
     [hinweis("**Merke:** Quicksort steckt die Arbeit ins **Zerlegen** (Pivot links, kleinere nach vorn), Mergesort ins **Zusammenführen**. "
              "Schlechtester Fall bei Pivot links: sortierte Eingabe, n(n − 1)/2 Vergleiche. Bei unbekannten Verfahren: Belegung **zum Zeitpunkt des Aufrufs** notieren."),
      text("Der Torwächter zerlegt jede Schar – und unbekannte Golems sortieren auf ihre eigene Art.")], L6),
]

welt = {"version": 2, "welt": 3, "titel": "Das Labyrinth", "farbe": "#7030A0", "levels": [],
        "boss": {"id": "W3-BOSS", "titel": "Das Echo der Schlucht", "dauerMin": 25, "anzahl": 8, "mix": {"1": 3, "2": 3, "3": 2}, "pool": B},
        "aufgaben": A}
for lid, nr, titel, ds, ab, ide, intro, auf in LEVELS:
    welt["levels"].append({"id": lid, "nr": nr, "titel": titel, "ds": ds, "ab": ab, "ide": ide, "intro": intro, "aufgaben": auf})

os.makedirs(SCRATCH + "/algolab/content", exist_ok=True)
json.dump(welt, open(SCRATCH + "/algolab/content/welt3.json", "w"), ensure_ascii=False, indent=1)
print("welt3.json:", len(A), "Aufgaben")
