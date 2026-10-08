# Baut content/welt4.json – Loesungen aus Java-Laeufen (NI-Stub) und ADT-Simulation
import json
from lib import *
from w4b_java import *

V = J.run()
def v(k):
    assert k in V, "fehlt: " + k
    return V[k]
assert not any(k.endswith(".FEHLER") for k in V), [k for k in V if k.endswith(".FEHLER")]

A = []
def add(a): A.append(a); return a["id"]

def L_(s): return [] if s in ("-", "") else s.split(", ")          # Java-Ausgabe -> Liste (Stapel: unten->oben)
def oben(s): return list(reversed(L_(s)))
def ras(lst): return [list(z) for z in lst]                            # Stapel oben -> unten
def nur_namen(s): return [x.rsplit(" ", 1)[0] for x in L_(s)]        # "Tee 4" -> "Tee"

# ---------- kleine ADT-Simulation (Gegenprobe zu Java) ----------
class SimStack:
    def __init__(self, init=()): self.a = list(init)
    def push(self, x): self.a.append(x)
    def pop(self):
        if not self.a: raise RuntimeError("leer")
        return self.a.pop()
    def top(self):
        if not self.a: raise RuntimeError("leer")
        return self.a[-1]
class SimQueue:
    def __init__(self, init=()): self.a = list(init)
    def enqueue(self, x): self.a.append(x)
    def dequeue(self):
        if not self.a: raise RuntimeError("leer")
        return self.a.pop(0)
    def head(self):
        if not self.a: raise RuntimeError("leer")
        return self.a[0]

KONV = hinweis("Schreibweise wie im AB: **Stapel oben zuerst**, **Schlange vorne zuerst**, dynamische Reihung **Index 0 zuerst**, Elemente mit Komma getrennt, leere Struktur: `–`.")
SIMHINW = "Baue den Endzustand mit den Chips auf: beim **Stapel von unten nach oben** (erster Chip = unterstes Element), bei der **Schlange von vorne nach hinten**, bei der dynamischen Reihung ab Index 0."

# =====================================================================
# Level 4.1 – Kistenturm und Schiffsschlange (DS 24)
# =====================================================================
L1 = []
s = SimStack(); s.push("Tee"); s.push("Zimt"); s.push("Reis"); s.pop(); s.push("Seide"); s.push(s.top()); s.pop(); s.push("Zinn")
assert ", ".join(s.a) == v("L1_01.r")
L1.append(add(aufgabe("W4-L1-01", "Der Kistenturm", 1, "ADT-Befehlsfolgen", [],
    [text("Der Kran stapelt Kisten. Führe die Anweisungen aus und gib den Inhalt des Stapels **am Ende** an."), code(C["L1_01"]), text(SIMHINW)],
    adtsim("stapel", []), {"inhalt": L_(v("L1_01.r"))},
    ["push legt oben auf, pop nimmt das oberste weg, top liest nur.", "Zeile 7: s.push(s.top()) legt eine Kopie des Verweises auf das oberste Element noch einmal oben auf."],
    [text("Ablauf (oben zuerst): Tee → Zimt, Tee → Reis, Zimt, Tee → (pop) Zimt, Tee → Seide, Zimt, Tee → Seide, Seide, Zimt, Tee → (pop) Seide, Zimt, Tee → Zinn, Seide, Zimt, Tee. "
          "Von unten nach oben also %s. Typischer Fehler: nach top() ein Element entfernen – top liest nur." % v("L1_01.r"))])))

q = SimQueue(); q.enqueue("Möwe"); q.enqueue("Albatros"); q.enqueue(q.head()); q.dequeue(); q.enqueue("Kormoran"); q.enqueue(q.dequeue()); q.dequeue()
assert ", ".join(q.a) == v("L1_02.r")
L1.append(add(aufgabe("W4-L1-02", "Die Schiffsschlange", 1, "ADT-Befehlsfolgen", [],
    [text("Vor der Mole warten Schiffe. Führe die Anweisungen aus und gib den Inhalt der Schlange am Ende an."), code(C["L1_02"]), text(SIMHINW)],
    adtsim("schlange", []), {"inhalt": L_(v("L1_02.r"))},
    ["enqueue stellt hinten an, dequeue nimmt vorne weg, head liest nur.", "q.enqueue(q.dequeue()) rotiert: das vorderste Schiff wandert nach hinten."],
    [text("Ablauf (vorne zuerst): Möwe → Möwe, Albatros → Möwe, Albatros, Möwe → (dequeue) Albatros, Möwe → Albatros, Möwe, Kormoran → (rotieren) Möwe, Kormoran, Albatros → (dequeue) %s." % v("L1_02.r"))])))

L1.append(add(aufgabe("W4-L1-03", "Was liefert der Kran?", 1, "ADT-Befehlsfolgen", [],
    [text("Gib zu den Zeilen 4, 5, 6, 8 und 9 die Rückgabe an."), code(C["L1_03"]),
     tabelle(["Zeile", "Anweisung", "Rückgabe"], [["4", "s.isEmpty()", "[[g4]]"], ["5", "s.top()", "[[g5]]"], ["6", "s.pop()", "[[g6]]"], ["8", "s.pop()", "[[g8]]"], ["9", "s.top()", "[[g9]]"]])],
    gaps({"g4": auswahl(["true", "false"]), "g5": zahl(), "g6": zahl(), "g8": zahl(), "g9": zahl()}),
    {"g4": [v("L1_03.z4")], "g5": [v("L1_03.z5")], "g6": [v("L1_03.z6")], "g8": [v("L1_03.z8")], "g9": [v("L1_03.z9")]},
    ["top() und pop() liefern beide das oberste Element – nur pop() entfernt es."],
    [text("Nach Zeile 3 liegt 5 auf 12. isEmpty() → false, top() → 5 (bleibt liegen), pop() → 5 (wird entfernt), dann 30 auflegen und wieder entnehmen → 30, zum Schluss top() → 12.")])))

mz = C["L1_04"].split("\n")
zeilen = [["0", "(Start)", "3, 7, 5", "8, 2, 6"]]
F = {}; Lo = {}
for i, z in enumerate(mz, 1):
    qv, sv = L_(v("L1_04.q%d" % i)), oben(v("L1_04.s%d" % i))
    if i in (1, 4, 6):
        zeilen.append([str(i), z, liste(qv), liste(sv)])
    else:
        zeilen.append([str(i), z, "[[q%d]]" % i, "[[s%d]]" % i])
        F["q%d" % i] = txt("code", 14); Lo["q%d" % i] = listvar(qv); F["s%d" % i] = txt("code", 14); Lo["s%d" % i] = listvar(sv)
L1.append(add(aufgabe("W4-L1-04", "Kräne im Wechselspiel", 2, "ADT-Befehlsfolgen", ["P4", "P8"],
    [text("Ein Stapel s und eine Schlange q (Inhaltstyp Ganzzahl) haben den Startzustand **s = 8, 2, 6 (oben zuerst)** und **q = 3, 7, 5 (vorne zuerst)**. Ergänze die Zustände nach jeder Zeile."),
     KONV,
     tabelle(["Nr.", "Anweisung", "q (vorne → hinten)", "s (oben → unten)"], zeilen),
     text("Wert von x nach Zeile 4: [[x]]")],
    gaps(dict(F, x=zahl())), dict(Lo, x=[v("L1_04.x")]),
    ["In Zeile 4 wird zuerst s.pop() ausgewertet, dann q.dequeue().", "Zeile 7: top() liest nur – das Element bleibt auf s."],
    [text("Endzustand q = %s, s = %s (oben zuerst), x = %s. In Zeile 4 muss gecastet werden: pop() und dequeue() liefern Object, gerechnet wird erst nach (Integer) (P4). "
          "Beim Hineinlegen (push, enqueue) wird die Zahl automatisch verpackt." % (liste(L_(v("L1_04.q7"))), liste(oben(v("L1_04.s7"))), v("L1_04.x")))])))

L1.append(add(aufgabe("W4-L1-05", "Wo kracht es?", 2, "Fehler im Java-Code", ["P1"],
    [text("Das Programmstück wird ausgeführt. In einer Zeile bricht es mit einem Laufzeitfehler ab."), code(C["L1_05"]),
     text("**Teil 1:** Markiere die Zeile, in der der Laufzeitfehler auftritt.\n\n**Teil 2:** Welcher Laufzeitfehler ist es? [[g1]]")],
    [lines(1, 1), gaps({"g1": auswahl(["IllegalStateException", "ClassCastException", "IndexOutOfBoundsException", "NullPointerException"])})],
    [{"zeilen": [int(v("L1_05.zeile"))]}, {"g1": [v("L1_05.ex")]}],
    ["Skizziere die Schlange nach jeder Zeile.", "head() auf einer leeren Schlange ist nicht erlaubt."],
    [text("Nach Zeile 5: Galeone, Kogge; Zeile 6 und 7 entnehmen beide – die Schlange ist leer. In Zeile %s greift head() auf die leere Schlange zu → %s. "
          "Im Abitur müssen solche Laufzeitfehler durch eine Abfrage wie `if (!q.isEmpty())` ausgeschlossen werden (P1)." % (v("L1_05.zeile"), v("L1_05.ex")))])))

L16 = C["L1_06"].replace("Kiste k = (Kiste) kran.top();", "Kiste k = [[g1]] kran.top();").replace("int nummer = (Integer) zoll.dequeue();", "int nummer = [[g2]] zoll.dequeue();").replace("char c = (Character) zeichen.pop();", "char c = [[g3]] zeichen.pop();")
compile_fail("L1_06_ohneCast", "static void f() { Stack kran = new Stack(); kran.push(new Kiste(\"Zinn\", 6)); Kiste k = kran.top(); }", "incompatible types: Object cannot be converted to Kiste")
L1.append(add(aufgabe("W4-L1-06", "Casten am Kai", 2, "Datentypen und Ausdrücke", ["P4"],
    [text("Die Klassen der Bibliothek „Niedersachsen“ speichern alles als `Object`. Ergänze die Casts."), code(L16),
     text("Ein Mitschüler schreibt zusätzlich `int n = (Integer) kran.top();`. Was passiert? [[g4]]")],
    gaps({"g1": txt("code", 10), "g2": txt("code", 10), "g3": txt("code", 12),
          "g4": auswahl(["Der Compiler meldet einen Fehler.", "Es kompiliert, beim Ausführen kommt es zur ClassCastException.", "n erhält das Gewicht der Kiste.", "n erhält den Wert 0."])}),
    {"g1": ["(Kiste)"], "g2": ["(Integer)"], "g3": ["(Character)"], "g4": ["Es kompiliert, beim Ausführen kommt es zur ClassCastException."]},
    ["Gecastet wird beim Herausholen, nicht beim Hineinlegen.", "Zahlen und Zeichen stecken als Integer bzw. Character im Stapel."],
    [text("Kiste k = (Kiste) kran.top(); int nummer = (Integer) zoll.dequeue(); char c = (Character) zeichen.pop();. Ohne Cast meldet javac „incompatible types: Object cannot be converted to Kiste“. "
          "Ein Cast von Object nach Integer ist für den Compiler erlaubt (es könnte ja eine Zahl sein) – geprüft wird erst beim Ausführen: Dort liegt eine Kiste → %s (P4)." % v("L1_06.cast"))])))

def erg_txt(e):
    out = []
    for teil in e.strip(";").split(";"):
        n, r = teil.split(":", 1)
        kw = "Kiste" if n == "1" else "Kisten"
        if "Exception" in r: out.append("%s %s → %s" % (n, kw, r))
        else: out.append("%s %s → %s, %s" % (n, kw, r[:-1], "unverändert" if r.endswith("=") else "VERÄNDERT"))
    return "; ".join(out)
zl = compile_fail("L1_07_diff", DIFF, "incompatible types")
assert zl == 2, zl
L1.append(add(aufgabe("W4-L1-07", "Bug-Hunt: Die Gewichtsdifferenz", 3, "Fehler im Java-Code", ["P1", "P2", "P4"],
    [text("`differenz(s)` soll für einen Stapel vom Inhaltstyp Kiste liefern, um wie viel die oberste Kiste schwerer ist als die darunter. Liegen weniger als zwei Kisten auf dem Stapel, soll 0 geliefert werden. s muss danach unverändert sein."),
     code(C["L1_07"]),
     text("**Teil 1:** Der Compiler meldet einen Fehler. Markiere die Zeile."),
     text("**Teil 2:** Nach Korrektur des Compilerfehlers: Bei einem Stapel mit genau einer Kiste tritt ein Laufzeitfehler in Zeile [[g1]] auf, bei einem leeren Stapel in Zeile [[g2]]."),
     text("Drei Mitschüler schlagen Korrekturen vor:"),
     text("**Fassung A**"), code(DIFF_A), text("**Fassung B**"), code(DIFF_B), text("**Fassung C**"), code(DIFF_C),
     text("**Teil 3:** Welche Fassung erfüllt alle Anforderungen?")],
    [lines(1, 1), gaps({"g1": zahl(), "g2": zahl()}), choice([("a", "Fassung A"), ("b", "Fassung B"), ("c", "Fassung C")])],
    [{"zeilen": [2]}, {"g1": ["3"], "g2": ["2"]}, {"richtig": ["a"]}],
    ["pop() liefert Object.", "Fassung B: Was passiert mit der entnommenen Kiste, wenn nur eine da war? Fassung C: Was passiert bei einem leeren Stapel?"],
    [text("Zeile 2: `s.pop()` liefert Object – ohne `(Kiste)` meldet javac „incompatible types“ (P4). Mit nur einer Kiste nimmt Zeile 2 sie weg, `s.top()` in Zeile 3 trifft den leeren Stapel; bei leerem Stapel scheitert schon pop() in Zeile 2 (P1). "
          "Getestet mit 0 bis 3 Kisten: A %s · B %s (eine Kiste bleibt verschwunden, P2) · C %s (Absturz bei leerem Stapel, P1). Nur A ist korrekt." %
          (erg_txt(v("L1_07A.erg")), erg_txt(v("L1_07B.erg")), erg_txt(v("L1_07C.erg"))))])))
assert "pop()" in v("L1_07.leer") and "top()" in v("L1_07.eins")
assert v("L1_07A.erg") == "0:0=;1:0=;2:3=;3:-1=;" and "!" in v("L1_07B.erg") and "Exception" in v("L1_07C.erg")

def stapelfolge_moeglich(folge):
    st, nxt = [], 1
    for x in folge:
        while nxt <= x: st.append(nxt); nxt += 1
        if not st or st[-1] != x: return False
        st.pop()
    return True
KR = [("a", "4, 3, 2, 1"), ("b", "1, 2, 3, 4"), ("c", "2, 4, 3, 1"), ("d", "3, 1, 2, 4"), ("e", "1, 4, 2, 3"), ("f", "2, 1, 4, 3")]
ri = [i for i, f in KR if stapelfolge_moeglich([int(x) for x in f.split(", ")])]
assert ri == ["a", "b", "c", "f"]
L1.append(add(aufgabe("W4-L1-08", "Kranfolgen", 3, "ADT-Befehlsfolgen", [],
    [text("Die Kisten 1, 2, 3, 4 kommen in dieser Reihenfolge am Kran an. Der Kran darf jederzeit die nächste ankommende Kiste auf seinen Stapel legen (push) oder die oberste Kiste abgeben (pop). Am Ende sind alle Kisten abgegeben. "
          "Welche Reihenfolgen der abgegebenen Kisten sind möglich? (Mehrere Antworten möglich.)")],
    choice(KR, True), {"richtig": ri},
    ["Wird eine Kiste abgegeben, liegen alle früher angekommenen, noch nicht abgegebenen Kisten in umgekehrter Reihenfolge darunter."],
    [text("Möglich sind %s. Bei 3, 1, 2, 4 liegt nach Abgabe von 3 die 2 über der 1 – 1 kann nicht vor 2 kommen. Bei 1, 4, 2, 3 liegt nach Abgabe von 4 die 3 oben, also muss 3 vor 2 kommen. "
          "Bei vier Kisten gibt es insgesamt 14 mögliche Folgen." % ", ".join(f for i, f in KR if i in ri))])))

# =====================================================================
# Level 4.2 – Kür: Zugbuch und Initiative (DS 25)
# =====================================================================
L2 = []
L2.append(add(aufgabe("W4-L2-01", "Welche Struktur passt?", 1, "Funktionsweise erläutern", ["P10"],
    [text("Ordne jeder Anwendung die am besten geeignete Datenstruktur zu.")],
    match([("e1", "Zurück-Knopf im Browser: die zuletzt besuchte Seite zuerst"), ("e2", "Support-Tickets werden in der Reihenfolge ihres Eingangs bearbeitet"),
           ("e3", "Bestenliste: neue Ergebnisse werden an der passenden Stelle einsortiert"), ("e4", "Tastaturpuffer: Tastendrücke werden der Reihe nach verarbeitet"),
           ("e5", "Rückgängig im Zeichenprogramm"), ("e6", "Spielerliste, aus der Spieler an beliebiger Stelle entfernt werden")],
          [("st", "Stapel (LIFO)"), ("sc", "Schlange (FIFO)"), ("da", "dynamische Reihung (Zugriff über Index)")]),
    {"e1": "st", "e2": "sc", "e3": "da", "e4": "sc", "e5": "st", "e6": "da"},
    ["Wird immer das Neueste, immer das Älteste oder ein Element an beliebiger Stelle gebraucht?"],
    [text("LIFO (zuletzt hinein, zuerst heraus) → Stapel: Zurück-Knopf, Rückgängig. FIFO → Schlange: Tickets, Tastaturpuffer. Einfügen/Entfernen an beliebiger Stelle → dynamische Reihung. "
          "Eine Begründung im Abitur nennt Zugriffsprinzip UND benötigte Operationen (P10).")])))

ZB_KARTE = klassenkarte("Zugbuch", ["- erledigt: Stapel", "- zurueckgenommen: Stapel"],
                        ["+ c Zugbuch()", "+ zug(z: Zeichenkette): nichts", "+ rueckgaengig(): Zeichenkette", "+ wiederholen(): Zeichenkette", "+ anzahlZuege(): Ganzzahl"])
ZB_INFO = text("`zug(z)` legt z auf **erledigt** und leert **zurueckgenommen**. `rueckgaengig()` nimmt den obersten Zug von erledigt, legt ihn auf zurueckgenommen und liefert ihn (`\"\"`, wenn nichts da ist). `wiederholen()` arbeitet genau umgekehrt.")
n = len(ZB_SEQ)
L2.append(add(aufgabe("W4-L2-02", "Das Zauberbuch: Rückgängig und Wiederholen", 2, "ADT-Befehlsfolgen", [],
    [ZB_KARTE, ZB_INFO, text("Ein neues Zugbuch b erhält nacheinander diese Aufrufe:"), code(ZB_TXT),
     text("Gib den Inhalt beider Stapel am Ende an. " + SIMHINW + "\n\n**Teil 1:** erledigt · **Teil 2:** zurueckgenommen")],
    [adtsim("stapel", []), adtsim("stapel", [])],
    [{"inhalt": L_(v("L2_ZB.e%d" % n))}, {"inhalt": L_(v("L2_ZB.z%d" % n))}],
    ["Ein neuer Zug leert den Stapel zurueckgenommen – danach kann nichts mehr wiederholt werden.", "rueckgaengig() auf leerem erledigt passiert nichts (Rückgabe \"\")."],
    [text("Zustände (unten → oben) nach jedem Aufruf: " + " | ".join("%d: erledigt %s / zurück %s" % (i, liste(L_(v("L2_ZB.e%d" % i))), liste(L_(v("L2_ZB.z%d" % i)))) for i in range(1, n + 1)) +
          ". Entscheidend: zug(\"Schild\") leert zurueckgenommen, deshalb liefert das letzte wiederholen() nur \"\".")])))

rueck = [(i, ZB_SEQ[i - 1][0], v("L2_ZB.r%d" % i)) for i in range(1, n + 1) if ZB_SEQ[i - 1][0] != "zug"]
opts = ["\"Feuer\"", "\"Eis\"", "\"Blitz\"", "\"Heilung\"", "\"Schild\"", "\"\" (leer)"]
def optv(r): return "\"\" (leer)" if r == '""' else r
F = {"g%d" % i: auswahl(opts) for i, _, _ in rueck}; Lo = {"g%d" % i: [optv(r)] for i, _, r in rueck}
assert all(Lo[k][0] in opts for k in Lo)
L2.append(add(aufgabe("W4-L2-03", "Was liefert das Zauberbuch?", 1, "ADT-Befehlsfolgen", [],
    [ZB_INFO, text("Gleiche Aufruffolge wie in der vorigen Aufgabe:"), code(ZB_TXT),
     tabelle(["Nr.", "Aufruf", "Rückgabe"], [[str(i), "b.%s()" % m, "[[g%d]]" % i] for i, m, _ in rueck])],
    gaps(F), Lo, ["Skizziere nach jedem Aufruf beide Stapel."],
    [text("Rückgaben: " + ", ".join("%d: %s" % (i, r) for i, _, r in rueck) + ". Aufruf 12 liefert \"\", weil zug(\"Schild\") in Aufruf 11 den Stapel zurueckgenommen geleert hat.")])))

IN_KARTE = klassenkarte("Initiative", ["- reihe: Schlange"], ["+ c Initiative()", "+ beitreten(name: Zeichenkette): nichts", "+ amZug(): Zeichenkette", "+ ausscheiden(name: Zeichenkette): Wahrheitswert"])
IN_INFO = text("`beitreten` stellt hinten an. `amZug()` entnimmt den Vordersten, stellt ihn sofort hinten wieder an und liefert seinen Namen. `ausscheiden(name)` entfernt das erste Vorkommen; die Reihenfolge der übrigen bleibt (Rückgabe: war name dabei?).")
m = len(IN_SEQ)
L2.append(add(aufgabe("W4-L2-04", "Initiative im Kampf", 2, "ADT-Befehlsfolgen", [],
    [IN_KARTE, IN_INFO, text("Ein neues Initiative-Objekt ini erhält nacheinander:"), code(IN_TXT), text("Gib den Inhalt von reihe am Ende an. " + SIMHINW)],
    adtsim("schlange", []), {"inhalt": L_(v("L2_IN.q%d" % m))},
    ["amZug() rotiert: vorne raus, hinten wieder rein.", "ausscheiden entfernt aus der Mitte – die anderen behalten ihre Reihenfolge."],
    [text("Zustände (vorne zuerst): " + " | ".join("%d: %s" % (i, liste(L_(v("L2_IN.q%d" % i)))) for i in range(1, m + 1)) + ".")])))

ret = [(i, IN_SEQ[i - 1], v("L2_IN.r%d" % i)) for i in range(1, m + 1) if IN_SEQ[i - 1][0] != "beitreten"]
F = {}; Lo = {}
for i, (mm, a), r in ret:
    if mm == "amZug": F["g%d" % i] = auswahl(["Aria", "Borin", "Cyra", "Drak", "Elva", "\"\" (leer)"]); Lo["g%d" % i] = [r]
    else: F["g%d" % i] = auswahl(["true", "false"]); Lo["g%d" % i] = [r]
L2.append(add(aufgabe("W4-L2-05", "Wer ist am Zug?", 1, "ADT-Befehlsfolgen", [],
    [IN_INFO, text("Gleiche Aufruffolge wie in der vorigen Aufgabe:"), code(IN_TXT),
     tabelle(["Nr.", "Aufruf", "Rückgabe"], [[str(i), ("ini.%s(\"%s\")" % (mm, a)) if a else "ini.%s()" % mm, "[[g%d]]" % i] for i, (mm, a), _ in ret])],
    gaps(F), Lo, ["Nach vier beitreten-Aufrufen steht Aria vorne."],
    [text("Rückgaben: " + ", ".join("%d: %s" % (i, r) for i, _, r in ret) + ". ausscheiden(\"Ork\") liefert false und lässt die Reihe unverändert.")])))

L2.append(add(aufgabe("W4-L2-06", "Bug-Hunt: Ausscheiden mit Nebenwirkungen", 2, "Fehler im Java-Code", ["P1", "P2"],
    [text("Ein Mitschüler schreibt `ausscheiden` so:"), code(C["L2_06"]),
     text("Welche Aussagen treffen zu? (Mehrere Antworten möglich.)")],
    choice([("a", "Ist name nicht in der Reihe, läuft die Schleife endlos."), ("b", "Bei leerer Reihe führt `reihe.head()` zu einem Laufzeitfehler."),
            ("c", "Die Reihenfolge der übrigen Teilnehmer kann sich ändern: Aus Aria, Borin, Cyra wird nach `ausscheiden(\"Borin\")` die Reihe Cyra, Aria."),
            ("d", "Die Methode liefert nie false."), ("e", "Die Methode ist korrekt, nur unnötig langsam.")], True),
    {"richtig": ["a", "b", "c", "d"]},
    ["Spiele ausscheiden(\"Ork\") und ausscheiden(\"Borin\") für Aria, Borin, Cyra durch."],
    [text("Gemessen: fehlender Name → %s, leere Reihe → %s, Aria, Borin, Cyra nach ausscheiden(\"Borin\") → %s (Aria ist nach hinten rotiert und verliert ihren Platz, P2). "
          "Außerdem gibt es kein return false. Richtig: über eine Hilfsschlange laufen und nur das erste Vorkommen nicht wieder anstellen (nächste Aufgabe)." % (v("L2_06.fehlt"), v("L2_06.leer"), v("L2_06.nach")))])))
assert v("L2_06.fehlt") == "endlos" and v("L2_06.leer") == "IllegalStateException"

aus = C["L2_07"].split("\n")
teile = [{"id": "t%d" % (i + 1), "code": z} for i, z in enumerate(aus)]
teile += [{"id": "d1", "code": "        if (n.equals(name)) {"}, {"id": "d2", "code": "            return true;"}, {"id": "d3", "code": "    while (reihe.head() != null) {"}]
assert len({t["code"] for t in teile}) == len(teile)
base = ["t%d" % i for i in range(1, 15)]
alt = list(base); alt[1], alt[2] = alt[2], alt[1]
L2.append(add(aufgabe("W4-L2-07", "Puzzle: Ausscheiden, aber richtig", 3, "Methode implementieren", ["P1", "P2", "P5"],
    [text("Baue `ausscheiden(name: Zeichenkette): Wahrheitswert` der Klasse Initiative (Attribut `reihe: Schlange`): Das **erste** Vorkommen von name wird entfernt, die übrigen behalten ihre Reihenfolge; Rückgabe true, wenn name dabei war. "
          "Drei Zeilen gehören nicht hinein.")],
    order(teile), {"reihenfolgen": [base, alt]},
    ["Alle Namen wandern durch eine Hilfsschlange – nur das erste Vorkommen nicht.", "Die Hilfsschlange wird am Ende zur neuen reihe."],
    [text("Die Schleife entnimmt alle Namen (Leer-Abfrage, P1), stellt alle außer dem ersten Vorkommen in hilf an (Vergleich mit equals, P5) und ersetzt reihe durch hilf – die Reihenfolge bleibt. "
          "`n.equals(name)` ohne `!gefunden` entfernte alle Vorkommen, ein `return true` mitten in der Schleife ließe die Reihe halb leer zurück (P2). "
          "Test: Aria, Borin, Cyra, Borin → ausscheiden(\"Borin\") = %s, danach %s; ausscheiden(\"Ork\") = %s." % (v("L2_07.r1"), v("L2_07.q1"), v("L2_07.r2")))])))

# =====================================================================
# Level 4.3 – Inventur: Struktur unverändert lassen (DS 26)
# =====================================================================
L3 = []
L3.append(add(aufgabe("W4-L3-01", "Die Umkehr-Maschine", 1, "ADT-Befehlsfolgen", [],
    [text("Ein Stapel s = A, B, C (oben zuerst) bzw. eine Schlange q = A, B, C (vorne zuerst) wird vollständig in eine leere Hilfsstruktur umgeschichtet und danach vollständig zurück. "
          "Ordne zu, wie die Struktur danach aussieht (gelesen oben bzw. vorne zuerst).")],
    match([("e1", "Stapel → Hilfsstapel → Stapel"), ("e2", "Stapel → Hilfsschlange → Stapel"), ("e3", "Schlange → Hilfsschlange → Schlange"),
           ("e4", "Schlange → Hilfsstapel → Schlange"), ("e5", "Schlange → Hilfsstapel → zweiter Hilfsstapel → Schlange")],
          [("k1", "A, B, C – unverändert"), ("k2", "C, B, A – umgedreht")]),
    {"e1": "k1" if v("L3_01.ss") == "A, B, C" else "k2", "e2": "k1" if v("L3_01.sq") == "A, B, C" else "k2", "e3": "k1" if v("L3_01.qq") == "A, B, C" else "k2",
     "e4": "k1" if v("L3_01.qs") == "A, B, C" else "k2", "e5": "k1" if v("L3_01.qss") == "A, B, C" else "k2"},
    ["Jeder Weg durch einen Stapel dreht die Reihenfolge um."],
    [text("Gemessen: Stapel über Hilfsstapel %s · Stapel über Hilfsschlange %s · Schlange über Hilfsschlange %s · Schlange über Hilfsstapel %s · Schlange über zwei Hilfsstapel %s. "
          "Regel: Jeder Durchgang durch einen Stapel dreht um; gerade Anzahl Umkehrungen → unverändert." % (v("L3_01.ss"), v("L3_01.sq"), v("L3_01.qq"), v("L3_01.qs"), v("L3_01.qss")))])))
assert [v("L3_01." + k) for k in ("ss", "sq", "qq", "qs", "qss")] == ["A, B, C", "C, B, A", "A, B, C", "C, B, A", "A, B, C"]

L3.append(add(aufgabe("W4-L3-02", "Zu früh zurückgekehrt", 1, "ADT-Befehlsfolgen", ["P2"],
    [text("Der Stapel s enthält (oben zuerst) Tee 4, Seide 3, Pfeffer 5, Zinn 6, Kaffee 4. Es wird `enthaelt(s, \"Pfeffer\")` aufgerufen:"), code(C["L3_02"]),
     text("Wie sieht s nach dem Aufruf aus? " + SIMHINW)],
    adtsim("stapel", ["Kaffee", "Zinn", "Pfeffer", "Seide", "Tee"]), {"inhalt": nur_namen(v("L3_02.s"))},
    ["Was passiert mit den Kisten in hilf, wenn mitten in der Schleife return ausgeführt wird?"],
    [text("Tee, Seide und Pfeffer werden entnommen und auf hilf gelegt; bei Pfeffer kehrt die Methode sofort mit true zurück. Die zweite Schleife wird nie erreicht: hilf ist eine lokale Variable – die drei Kisten sind verloren. "
          "s = Kaffee, Zinn (von unten). Regel: Ergebnis in einer Variablen merken, return erst nach dem Zurückschichten (P2).")])))

q = SimQueue([8, 3, 6, 2]); h = SimQueue(); summe = 0
zeilen = [["Start", "–", "0", "8, 3, 6, 2", "–"]]; F = {}; Lo = {}
i = 0
while q.a:
    x = q.dequeue(); summe += x; h.enqueue(x); i += 1
    zeilen.append(["auswerten", str(x), "[[s%d]]" % i, "[[q%d]]" % i if i % 2 else liste(q.a), "[[h%d]]" % i if i % 2 == 0 else liste(h.a)])
    F["s%d" % i] = zahl(); Lo["s%d" % i] = [str(summe)]
    if i % 2: F["q%d" % i] = txt("code", 12); Lo["q%d" % i] = listvar(q.a)
    else: F["h%d" % i] = txt("code", 12); Lo["h%d" % i] = listvar(h.a)
while h.a:
    q.enqueue(h.dequeue()); i += 1
    zeilen.append(["zurück", "–", str(summe), "[[q%d]]" % i, "[[h%d]]" % i])
    F["q%d" % i] = txt("code", 12); Lo["q%d" % i] = listvar(q.a); F["h%d" % i] = txt("code", 12); Lo["h%d" % i] = listvar(h.a)
assert str(summe) == v("L3_03.r") and liste(q.a) == v("L3_03.q")
L3.append(add(aufgabe("W4-L3-03", "Inventur über die Hilfsschlange", 2, "Tracetabelle", ["P8"],
    [text("`summe(q)` wird für q = 8, 3, 6, 2 (vorne zuerst) aufgerufen. Vervollständige die Tabelle: eine Zeile pro Schleifendurchlauf."), code(C["L3_03"]), KONV,
     tabelle(["Phase", "x", "summe", "q (vorne → hinten)", "hilf (vorne → hinten)"], zeilen)],
    gaps(F), Lo, ["Beim Auswerten wandert jede Zahl von vorne aus q nach hinten in hilf.", "Eine Schlange über eine Hilfsschlange behält die Reihenfolge."],
    [text("Nach dem Auswerten ist q leer und hilf = 8, 3, 6, 2; beim Zurückstellen wandert alles in derselben Reihenfolge zurück. Rückgabe %s, q danach wieder 8, 3, 6, 2 – unverändert. "
          "In Tracetabellen gehört jede Änderung in eine eigene Zeile (P8)." % v("L3_03.r"))])))

sch = C["L3_04"].split("\n")
teile = [{"id": "t%d" % (i + 1), "code": z} for i, z in enumerate(sch)]
teile += [{"id": "d1", "code": "        hilf.push(new Kiste(k.getName(), k.getGewicht()));"}, {"id": "d2", "code": "        Kiste k = s.pop();"}, {"id": "d3", "code": "    while (s.top() != null) {"}]
assert len({t["code"] for t in teile}) == len(teile) and len(sch) == 15
b = ["t%d" % i for i in range(1, 16)]
def sw(l, i, j): l = list(l); l[i], l[j] = l[j], l[i]; return l
b2 = sw(b, 1, 2)
b3 = b[:5] + ["t9", "t6", "t7", "t8"] + b[9:]
b4 = sw(b3, 1, 2)
L3.append(add(aufgabe("W4-L3-04", "Puzzle: Schwere Kisten zählen", 2, "Methode implementieren", ["P1", "P2", "P4"],
    [text("`anzahlSchwere(s: Stapel vom Inhaltstyp Kiste, grenze: Ganzzahl): Ganzzahl` soll zählen, wie viele Kisten schwerer als grenze sind. **s muss danach unverändert sein** (dieselben Kisten in derselben Reihenfolge). Drei Zeilen gehören nicht hinein.")],
    order(teile), {"reihenfolgen": [b, b2, b3, b4]},
    ["Muster: auswerten – zwischenlagern – zurückschichten – erst dann return.", "Ein Stapel über einen Hilfsstapel und zurück ergibt wieder die alte Reihenfolge."],
    [text("Leer-Abfrage in der Schleife (P1), Cast `(Kiste)` beim pop (P4), dieselbe Kiste k auf hilf legen – eine neue Kiste mit gleichen Werten wäre nicht „dieselbe“ (P2) – und alles zurückschichten. "
          "Getestet: Stapel Zimt 2, Reis 7, Tee 4, Kupfer 9 (oben zuerst), grenze 5 → %s, danach dieselben Objekte in derselben Reihenfolge: %s." % (v("L3_04.r"), v("L3_04.gleich")))])))

L35 = C["L3_05k"].replace("i < n", "i < [[g3]]").replace("q.enqueue(k);", "q.enqueue([[g4]]);")
L3.append(add(aufgabe("W4-L3-05", "Rotieren ohne Ende", 2, "Lückencode", ["P2"],
    [text("Diese Methode soll das größte Gewicht in q liefern (−1 bei leerer Schlange) und q unverändert lassen:"), code(C["L3_05"]),
     text("- Was passiert bei einer nicht leeren Schlange? [[g1]]\n- Was liefert der Aufruf für eine leere Schlange? [[g2]]"),
     text("Korrektur nach Muster 3 „Rotieren mit Zähler“: Die Anzahl n der Kisten wird mitgegeben."), code(L35)],
    gaps({"g1": auswahl(["Die Schleife läuft endlos.", "Es kommt zu einer IllegalStateException.", "Sie liefert das richtige Ergebnis.", "Sie liefert −1."]), "g2": zahl(),
          "g3": txt(), "g4": txt()}),
    {"g1": ["Die Schleife läuft endlos."], "g2": [v("L3_05.leer")], "g3": ["n"], "g4": ["k"]},
    ["Wird q in der ersten Fassung jemals leer?", "Nach genau n Runden ist jede Kiste einmal von vorne nach hinten gewandert."],
    [text("Jede entnommene Kiste wird sofort wieder angestellt – q wird nie leer: Endlosschleife (gemessen: %s). Für die leere Schlange läuft die Schleife nicht → −1. "
          "Mit bekannter Anzahl n reichen n Runden: Danach steht dieselbe Kiste wieder vorne (geprüft: Maximum %s, q unverändert: %s). Ohne bekannte Anzahl braucht man eine Hilfsschlange." %
          (v("L3_05.voll"), v("L3_05k.r"), v("L3_05k.gleich")))])))

SCHW = C["L3_06"].replace("k.getGewicht() > beste.getGewicht()", "k.getGewicht() [[g1]] beste.getGewicht()").replace("s.push(hilf.pop());", "s.push([[g2]]);").replace("return beste;", "return [[g3]];")
L3.append(add(aufgabe("W4-L3-06", "Lückencode: Die schwerste Kiste", 3, "Lückencode", ["P1", "P2"],
    [text("`schwerste(s)` liefert die schwerste Kiste des Stapels (null bei leerem Stapel), bei Gleichstand die **oberste** davon. s bleibt unverändert."), code(SCHW),
     text("Für s = Zinn 6, Reis 7, Kupfer 7, Tee 4 (oben zuerst) liefert die Methode die Kiste [[g4]].")],
    gaps({"g1": auswahl([">", ">=", "<", "=="]), "g2": txt("code", 12), "g3": txt(), "g4": auswahl(["Zinn", "Reis", "Kupfer", "Tee"])}),
    {"g1": [">"], "g2": ["hilf.pop()"], "g3": ["beste"], "g4": [v("L3_06.r")]},
    ["Die Kisten werden von oben nach unten entnommen. Welche der beiden 7-kg-Kisten kommt zuerst?"],
    [text("Mit `>` gewinnt bei Gleichstand die zuerst entnommene, also die obere Kiste: %s. Mit `>=` würde die spätere (untere) Kiste %s gewinnen. "
          "Zurückgeschichtet wird mit `s.push(hilf.pop())`, zurückgegeben `beste` – erst nach dem Zurückschichten (P2). `beste == null` als erste Prüfung verhindert den Zugriff auf null (P1)." % (v("L3_06.r"), v("L3_06f.r")))])))

L3.append(add(aufgabe("W4-L3-07", "Unverändert – wirklich?", 3, "Funktionsweise erläutern", ["P2"],
    [text("In einer Methode soll ein übergebener Stapel s vom Inhaltstyp Kiste nach der Auswertung **unverändert** sein. Welche Aussagen sind richtig? (Mehrere Antworten möglich.)")],
    choice([("a", "Wer `hilf.push(new Kiste(k.getName(), k.getGewicht()))` zwischenlagert und zurückschichtet, hat s nicht unverändert gelassen."),
            ("b", "Ein `return` mitten in der Auswerte-Schleife ist erlaubt, wenn das Ergebnis schon feststeht."),
            ("c", "Stapel und Schlange werden als Referenz übergeben – jedes pop() in der Methode verändert den Stapel des Aufrufers."),
            ("d", "Wer den Stapel über eine Hilfsschlange zwischenlagert und direkt zurückschichtet, erhält die umgekehrte Reihenfolge."),
            ("e", "Es genügt, den Stapel am Ende neu zu erzeugen: `s = new Stack();` und alle Kisten hineinzulegen.")], True),
    {"richtig": ["a", "c", "d"]},
    ["„Unverändert“ heißt: dieselben Objekte in derselben Reihenfolge – und zwar im Stapel des Aufrufers."],
    [text("a: Neue Kisten mit gleichen Werten sind nicht dieselben Objekte – Verweise von anderswo zeigen ins Leere (P2). b: Der halb abgebaute Stapel bleibt zurück. c: richtig – deshalb ist Zurückschichten nötig. "
          "d: richtig – Stapel → Schlange → Stapel dreht um. e: `s = new Stack()` ändert nur die lokale Variable s; der Stapel des Aufrufers bleibt leer zurück.")])))

L3.append(add(aufgabe("W4-L3-08", "Rotieren mit Zähler", 1, "ADT-Befehlsfolgen", [],
    [text("Die Schlange q = A, B, C, D, E (vorne zuerst) wird k-mal rotiert: `for (int i = 0; i < k; i++) { q.enqueue(q.dequeue()); }`. Gib q danach an (vorne zuerst, mit Komma)."),
     text("k = 3: [[g1]] · k = 5: [[g2]] · k = 7: [[g3]]")],
    gaps({"g1": txt("code", 14), "g2": txt("code", 14), "g3": txt("code", 14)}),
    {"g1": listvar(L_(v("L3_08.r3"))), "g2": listvar(L_(v("L3_08.r5"))), "g3": listvar(L_(v("L3_08.r7")))},
    ["Jede Runde wandert das vorderste Element nach hinten."],
    [text("k = 3: %s; nach k = 5 = Länge ist alles wieder wie vorher: %s; k = 7 wirkt wie 7 mod 5 = 2 Runden: %s. Genau so bleibt eine Schlange mit bekannter Anzahl beim Auswerten unverändert." %
          (v("L3_08.r3"), v("L3_08.r5"), v("L3_08.r7")))])))

# =====================================================================
# Level 4.4 – Die Ladeliste: dynamische Reihung (DS 27)
# =====================================================================
L4 = []
d = []
d.append(14); d.append(3); d.insert(0, 27); d.insert(2, 9); d[1] = 50; del d[0]; d.append(d[1]); d.insert(len(d), 8)
assert liste(d) == v("L4_01.r")
L4.append(add(aufgabe("W4-L4-01", "Die Ladeliste wächst und schrumpft", 1, "ADT-Befehlsfolgen", ["P6"],
    [text("Die Containernummern stehen in einer dynamischen Reihung. Führe die Anweisungen aus und gib den Inhalt am Ende an."), code(C["L4_01"]), text(SIMHINW)],
    adtsim("dynarray", []), {"inhalt": L_(v("L4_01.r"))},
    ["insertAt verschiebt die folgenden Elemente nach hinten, delete nach vorn – die Indizes ändern sich!", "setItem ersetzt nur, die Länge bleibt."],
    [text("Ablauf: 14 → 14, 3 → 27, 14, 3 → 27, 14, 9, 3 → 27, 50, 9, 3 → 50, 9, 3 → 50, 9, 3, 9 (getItem(1) = 9 angehängt) → %s (insertAt(getLength(), 8) hängt an)." % v("L4_01.r"))])))

f = [v("L4_02.f%d" % i) for i in range(7)]
op = [("a", "`d.getItem(4)`"), ("b", "`d.insertAt(4, x)`"), ("c", "`d.delete(4)`"), ("d", "`d.setItem(3, x)`"), ("e", "`d.insertAt(5, x)`"), ("f", "`d.getItem(-1)`"), ("g", "`d.delete(0)`")]
L4.append(add(aufgabe("W4-L4-02", "Index?", 1, "ADT-Befehlsfolgen", ["P1", "P6"],
    [text("Die dynamische Reihung d enthält genau 4 Elemente. Welche Aufrufe führen zu einem Laufzeitfehler? (Mehrere Antworten möglich.)")],
    choice(op, True), {"richtig": [o[0] for o, r in zip(op, f) if r != "ok"]},
    ["Gültige Indizes für getItem, setItem und delete: 0 bis getLength() − 1. insertAt darf zusätzlich getLength()."],
    [text("Laufzeitfehler (IndexOutOfBoundsException) bei getItem(4), delete(4), insertAt(5, x) und getItem(−1). insertAt(4, x) hängt an (i = getLength() ist erlaubt), setItem(3, x) und delete(0) sind gültig (P6: Grenzen genau kennen).")])))

names = ["Zimt", "Tee", "Tee", "Reis", "Tee", "Tee"]
dd = list(names); i = 0; rows_ = []
while i < len(dd):
    nm = dd[i]; ln = len(dd)
    if nm == "Tee":
        del dd[i]; rows_.append((i, ln, nm, "delete(%d)" % i, liste(dd)))
    else:
        rows_.append((i, ln, nm, "–", liste(dd)))
    i += 1
assert liste(dd) == ", ".join(nur_namen(v("L4_03.r")))
zeilen = []; F = {}; Lo = {}
for k, (i_, ln, nm, akt, nach) in enumerate(rows_):
    if k == 0: zeilen.append([str(i_), str(ln), nm, akt, nach]); continue
    zeilen.append([str(i_), "[[l%d]]" % k, "[[n%d]]" % k, akt, "[[d%d]]" % k])
    F["l%d" % k] = zahl(); Lo["l%d" % k] = [str(ln)]; F["n%d" % k] = auswahl(["Zimt", "Tee", "Reis"]); Lo["n%d" % k] = [nm]
    F["d%d" % k] = txt("code", 18); Lo["d%d" % k] = listvar(nach.split(", "))
L4.append(add(aufgabe("W4-L4-03", "Die Kiste, die übersprungen wurde", 2, "Tracetabelle", ["P6", "P8"],
    [text("`entferneName(d, \"Tee\")` soll alle Tee-Kisten entfernen. d = Zimt, Tee, Tee, Reis, Tee, Tee (Index 0 zuerst)."), code(C["L4_03"]),
     tabelle(["i", "d.getLength()", "Name an Index i", "Aktion", "d danach"], zeilen),
     text("Ergebnis nach dem Aufruf: [[e]] – richtig wäre: Zimt, Reis.")],
    gaps(dict(F, e=txt("code", 18))), dict(Lo, e=listvar(dd)),
    ["Nach delete(i) rückt der Nachfolger auf Index i – und dann kommt i++."],
    [text("Nach jedem delete(i) rückt die nächste Kiste auf Index i, das anschließende i++ springt über sie hinweg. Übrig bleiben %s. Der Fehler tritt nur auf, wenn zwei zu löschende Kisten direkt hintereinander stehen. "
          "Abhilfe: rückwärts laufen oder i nur erhöhen, wenn nicht gelöscht wurde (P6)." % liste(dd))])))

L4.append(add(aufgabe("W4-L4-04", "Bug-Hunt: Die leichteste Kiste", 2, "Fehler im Java-Code", ["P6"],
    [text("`entferneLeichteste(d)` soll die leichteste Kiste (bei Gleichstand die erste) entfernen und liefern; bei leerer Liste null."), code(C["L4_04"]),
     text("**Teil 1:** Markiere die fehlerhafte Zeile.\n\n**Teil 2:** Korrigiere die Schleifenbedingung: `for (int i = 1; [[g1]]; i++)`\n\n"
          "**Teil 3:** Nach der Korrektur liefert der Aufruf für d = Zinn 6, Tee 4, Reis 7, Kaffee 4 die Kiste [[g2]]; danach ist d = [[g3]] (nur Namen, mit Komma).")],
    [lines(1, 1), gaps({"g1": txt("code", 18), "g2": auswahl(["Zinn", "Tee", "Reis", "Kaffee"]), "g3": txt("code", 20)})],
    [{"zeilen": [6]}, {"g1": ["i<d.getLength()", "i<=d.getLength()-1"], "g2": [v("L4_04k.r")], "g3": listvar(nur_namen(v("L4_04k.d")))}],
    ["Der größte gültige Index ist d.getLength() − 1."],
    [text("Mit `i <= d.getLength()` greift getItem in der letzten Runde auf Index getLength() zu → %s (P6). Korrigiert: `i < d.getLength()`. "
          "Wegen `<` gewinnt bei Gleichstand die erste 4-kg-Kiste: %s; d danach %s." % (v("L4_04.r"), v("L4_04k.r"), liste(nur_namen(v("L4_04k.d")))))])))

base5 = ["Zimt 2", "Seide 3", "Tee 4", "Zinn 6", "Reis 7"]
pos = 0; rws = []
while pos < len(base5) and int(base5[pos].split()[1]) <= 4:
    rws.append((pos, base5[pos], "nein")); pos += 1
rws.append((pos, base5[pos], "ja"))
zeilen = [[str(p), "[[k%d]]" % p, "[[a%d]]" % p] for p, _, _ in rws]
F = {}; Lo = {}
for p, kk, a in rws:
    F["k%d" % p] = auswahl(base5); Lo["k%d" % p] = [kk]; F["a%d" % p] = auswahl(["ja", "nein"]); Lo["a%d" % p] = [a]
L4.append(add(aufgabe("W4-L4-05", "Sortiert verladen", 2, "Tracetabelle", ["P1"],
    [text("Die Ladeliste ist aufsteigend nach Gewicht sortiert: d = Zimt 2, Seide 3, Tee 4, Zinn 6, Reis 7. Es wird `einfuegenSortiert(d, new Kiste(\"Kaffee\", 4))` aufgerufen."), code(C["L4_05"]),
     tabelle(["pos", "d.getItem(pos)", "schwerer als 4 kg?"], zeilen),
     text("Kaffee wird an Index [[ix]] eingefügt. Ist die Liste leer, wird `getItem` [[lee]] aufgerufen.")],
    gaps(dict(F, ix=zahl(), lee=auswahl(["nie", "einmal mit Index 0", "einmal mit Index −1"]))), dict(Lo, ix=[str(pos)], lee=["nie"]),
    ["Die Schleife läuft, solange die Kiste an pos höchstens so schwer ist wie die neue.", "Kurzschluss: Ist pos < d.getLength() falsch, wird der rechte Teil nicht mehr ausgewertet."],
    [text("pos läuft über Zimt, Seide und Tee (nicht schwerer als 4 kg) und stoppt bei Zinn 6: insertAt(%d, Kaffee) – hinter der gleich schweren Tee-Kiste. Ergebnis: %s. "
          "Bei leerer Liste ist `pos < d.getLength()` sofort falsch – wegen des Kurzschlusses wird getItem nie aufgerufen, insertAt(0, k) ist erlaubt (P1)." % (pos, liste(nur_namen(v("L4_05.d")))))])))
assert ", ".join(nur_namen(v("L4_05.d"))) == "Zimt, Seide, Tee, Kaffee, Zinn, Reis"

L4.append(add(aufgabe("W4-L4-06", "Vom Code zum Struktogramm: Leichtgut entfernen", 3, "Code ↔ Struktogramm", ["P6", "P9"],
    [text("`entferneLeichte(d, grenze)` entfernt alle Kisten, die leichter als grenze sind, und liefert ihre Anzahl:"), code(C["L4_06"]),
     text("Vervollständige das Struktogramm nach EH § 5 (in Struktogrammen stehen keine Casts):"),
     struk("entferneLeichte(d: dynamische Reihung vom Inhaltstyp Kiste, grenze: Ganzzahl): Ganzzahl", [
         {"anw": "anzahl ← 0"}, {"anw": "i ← 0"},
         {"solange": "[[g1]]", "rumpf": [
             {"wenn": "d.getItem(i).getGewicht() < grenze", "dann": [{"aufruf": "[[g2]]"}, {"anw": "anzahl ← anzahl + 1"}], "sonst": [{"anw": "[[g3]]"}]}]},
         {"gib": "anzahl"}]),
     text("Für d = Zimt 2, Seide 3, Zinn 6, Wolle 3, Reis 7 und grenze 4 liefert der Aufruf [[g4]].")],
    gaps({"g1": txt("code", 18), "g2": txt("code", 12), "g3": txt("code", 10), "g4": zahl()}),
    {"g1": ["i<d.getLength()", "i<Längevond", "d.getLength()>i"], "g2": ["d.delete(i)"], "g3": ["i←i+1", "i<-i+1", "i←1+i"], "g4": [v("L4_06.r")]},
    ["Die Länge wird in jeder Runde neu abgefragt.", "Zuweisung im Struktogramm: ←"],
    [text("Schleife „solange i < d.getLength()“, im wahr-Zweig `d.delete(i)` und zählen, im falsch-Zweig `i ← i + 1` – nach einem Löschen bleibt i stehen, weil der Nachfolger nachrückt. "
          "Zuweisungen mit ←, keine Java-Syntax wie `i++` (P9). Ergebnis %s, übrig bleiben %s." % (v("L4_06.r"), liste(nur_namen(v("L4_06.d")))))])))

def dup_py(lst):
    lst = list(lst); vgl = 0; i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            vgl += 1
            if lst[j][0] == lst[i][0]: del lst[j]
            else: j += 1
        i += 1
    return lst, vgl
dl, dv = dup_py([("Tee", 4), ("Reis", 7), ("Tee", 3), ("Zimt", 2), ("Reis", 5), ("Tee", 1)])
assert liste(["%s %d" % x for x in dl]) == v("L4_07.d") and str(dv) == v("L4_07z.vgl")
L4.append(add(aufgabe("W4-L4-07", "Doppelt geladen", 3, "Effizienz", [],
    [text("`entferneDuplikate(d)` entfernt Kisten mit gleichem Namen; nur das erste Vorkommen bleibt, die Reihenfolge bleibt erhalten."), code(C["L4_07"]),
     text("d = Tee 4, Reis 7, Tee 3, Zimt 2, Reis 5, Tee 1.\n\n- d nach dem Aufruf (Name Gewicht, mit Komma, z. B. `Tee 4, Reis 7`): [[g1]]\n"
          "- Anzahl der Namensvergleiche (`equals`) dabei: [[g2]]\n- Anzahl der Namensvergleiche für eine Liste aus 6 Kisten mit lauter verschiedenen Namen: [[g3]]")],
    gaps({"g1": txt("code", 24), "g2": zahl(), "g3": zahl()}),
    {"g1": listvar(L_(v("L4_07.d"))), "g2": [v("L4_07z.vgl")], "g3": [v("L4_07z.vgl6")]},
    ["Gelöschte Kisten werden später nicht mehr verglichen.", "Ohne Duplikate wird jede Kiste mit jeder späteren verglichen."],
    [text("Übrig bleiben %s mit %s Vergleichen (i = 0: 5 Vergleiche, dabei werden Tee 3 und Tee 1 gelöscht; i = 1: 2 Vergleiche, Reis 5 gelöscht; i = 2: keiner). "
          "Ohne Duplikate: 5 + 4 + 3 + 2 + 1 = %s = n(n − 1)/2 – quadratischer Aufwand." % (v("L4_07.d"), v("L4_07z.vgl"), v("L4_07z.vgl6")))])))

L4.append(add(aufgabe("W4-L4-08", "Durch die Ladeliste laufen", 1, "Lückencode", ["P6"],
    [text("d ist eine dynamische Reihung vom Inhaltstyp Ganzzahl mit d = 4, 9, 1. Welche Schleifen addieren **alle** Werte ohne Laufzeitfehler? (Mehrere Antworten möglich.)")],
    choice([("a", "`for (int i = 0; i < d.getLength(); i++) { s += (Integer) d.getItem(i); }`"), ("b", "`for (Object o : d) { s += (Integer) o; }`"),
            ("c", "`for (int i = 0; i <= d.getLength(); i++) { s += (Integer) d.getItem(i); }`"), ("d", "`for (int i = 1; i < d.getLength(); i++) { s += (Integer) d.getItem(i); }`")], True),
    {"richtig": ["a", "b"]},
    ["Indizes von 0 bis getLength() − 1."],
    [text("a und b liefern %s (DynArray ist in der Online-IDE mit for-each durchlaufbar – vor dem Einsatz prüfen). c greift auf Index 3 zu → %s; d beginnt bei 1 und vergisst den ersten Wert (%s) – beides P6." %
          (v("L4_08.s1"), v("L4_08.s3"), v("L4_08.s4")))])))
assert v("L4_08.s1") == v("L4_08.s2") == "14"
assert v("TXT_ZB.e") == v("L2_ZB.e12") and v("TXT_IN.q") == v("L2_IN.q12") and v("TXT_ZB2.e") == v("B14.e") and v("TXT_L1_05.r") == "IllegalStateException" and v("TXT_L5_03.e") == v("L5_03.e12")

# =====================================================================
# Level 4.5 – Zollamt: Umformen, Klammern, Postfix (DS 28)
# =====================================================================
L5 = []
L5.append(add(aufgabe("W4-L5-01", "Von der Liste in den Kran", 1, "ADT-Befehlsfolgen", [],
    [text("Die Ladeliste wird in einen Stapel umgeladen:"), code(C["L5_01"]), text("Gib den Inhalt von s am Ende an. " + SIMHINW)],
    adtsim("stapel", []), {"inhalt": L_(v("L5_01.r"))},
    ["Index 0 wird zuerst gepusht und liegt deshalb unten."],
    [text("Nach der Schleife liegt Tee unten, Seide oben; pop() entfernt Seide. s (unten → oben) = %s." % v("L5_01.r"))])))

L5.append(add(aufgabe("W4-L5-02", "Umladen: Wer steht wo?", 1, "ADT-Befehlsfolgen", [],
    [text("Ordne jedem Umladevorgang das Ergebnis zu. Ausgangslage jeweils: Schlange q = A, B, C (vorne zuerst), Stapel s = A, B, C (oben zuerst) bzw. dynamische Reihung d = A, B, C (Index 0 zuerst). "
          "Das Ergebnis wird gelesen: Schlange vorne zuerst, Stapel oben zuerst, Reihung ab Index 0.")],
    match([("e1", "q → d mit `d.append(q.dequeue())`"), ("e2", "d → s mit `s.push(d.getItem(i))` für i = 0, 1, 2"), ("e3", "s → q mit `q.enqueue(s.pop())`"),
           ("e4", "q → d mit `d.insertAt(0, q.dequeue())`"), ("e5", "s → d mit `d.append(s.pop())`")],
          [("k1", "A, B, C"), ("k2", "C, B, A")]),
    {k: ("k1" if v("L5_02." + k) == "A, B, C" else "k2") for k in ("e1", "e2", "e3", "e4", "e5")},
    ["Wer zuerst herauskommt, steht im Ziel vorne/an Index 0/unten."],
    [text("Gemessen: e1 %s, e2 %s (A liegt unten), e3 %s, e4 %s (jedes neue Element vorne), e5 %s. Merke: Umgedreht wird beim Durchgang durch einen Stapel (push, dann von oben lesen) und mit insertAt(0, …)." %
          tuple(v("L5_02.e%d" % i) for i in range(1, 6)))])))

zeilen = [["4", "[[d4]]", "[[q4]]", "–", "–"], ["8", "Kupfer, Tee, Zimt, Wolle", "[[q8]]", "[[s8]]", "–"], ["12", "Kupfer, Tee, Zimt, Wolle", "–", "[[s12]]", "[[e12]]"]]
L5.append(add(aufgabe("W4-L5-03", "Umladen im Zollamt", 2, "Tracetabelle", ["P8"],
    [text("Die dynamische Reihung d enthält Kupfer, Tee, Zimt, Wolle (Index 0 zuerst)."), code(C["L5_03"]), KONV,
     tabelle(["nach Zeile", "d", "q (vorne zuerst)", "s (oben zuerst)", "e"], zeilen),
     text("Vergleiche e mit d: [[g]]")],
    gaps({"d4": txt("code", 22), "q4": txt("code", 22), "q8": txt("code", 22), "s8": txt("code", 22), "s12": txt("code", 22), "e12": txt("code", 22),
          "g": auswahl(["gleiche Reihenfolge", "umgekehrte Reihenfolge", "andere Elemente"])}),
    {"d4": listvar(L_(v("L5_03.d4"))), "q4": listvar(L_(v("L5_03.q4"))), "q8": listvar(L_(v("L5_03.q8"))), "s8": listvar(oben(v("L5_03.s8"))),
     "s12": listvar(oben(v("L5_03.s12"))), "e12": listvar(L_(v("L5_03.e12"))), "g": ["gleiche Reihenfolge"]},
    ["Zeilen 2–4 laufen rückwärts durch d.", "getItem liest nur – d bleibt unverändert."],
    [text("Nach Zeile 4: q = %s (rückwärts gelesen). Nach Zeile 8: q leer, s (oben zuerst) = %s. Nach Zeile 12: e = %s. "
          "Zwei Umkehrungen (rückwärts lesen, Stapel) heben sich auf – e hat dieselbe Reihenfolge wie d." % (v("L5_03.q4"), liste(oben(v("L5_03.s8"))), v("L5_03.e12")))])))

kt = [v("L5_04.t%d" % i) for i in range(7)]
kopt = [(chr(97 + i), "`%s`" % t) for i, t in enumerate(KL_TESTS[:6])]
L5.append(add(aufgabe("W4-L5-04", "Klammern im Frachtbrief", 1, "ADT-Befehlsfolgen", [],
    [text("Welche Ausdrücke sind richtig geklammert? (Mehrere Antworten möglich; andere Zeichen werden ignoriert.)")],
    choice(kopt, True), {"richtig": [kopt[i][0] for i in range(6) if kt[i] == "true"]},
    ["Jede schließende Klammer muss zur zuletzt geöffneten, noch offenen Klammer passen."],
    [text("Richtig: %s. `([)]`: Bei ) liegt [ oben. `(()`: am Ende bleibt ( offen. `}{`: } kommt bei leerem Stapel. Ein Zähler (+1/−1) würde `([)]` und `}{` fälschlich durchgehen lassen – man braucht einen Stapel." %
          ", ".join(KL_TESTS[i] for i in range(6) if kt[i] == "true"))])))

tr = [x.split(":") for x in v("L5_04.trace").strip(";").split(";")]
zeilen = []; F = {}; Lo = {}
for k, t in enumerate(tr):
    zeichen = t[0]
    stack_oben = list(reversed(L_(t[1])))
    aktion = "push" if len(t) == 2 else "pop → passt"
    zeilen.append([zeichen, aktion, "[[s%d]]" % k]); F["s%d" % k] = txt("code", 12); Lo["s%d" % k] = listvar(stack_oben, klammern=False)
L5.append(add(aufgabe("W4-L5-05", "Klammer-Trace", 2, "Tracetabelle", ["P8"],
    [text("Verfolge `klammernOk(\"({x}[y](z))\")` mit dem Klammer-Stapel. Gib nach jedem Klammerzeichen den Stapel an (oben zuerst, Zeichen ohne Anführungszeichen, z. B. `{, (`; leer: `–`)."),
     code(C["L5_04"]),
     tabelle(["Zeichen", "Aktion", "Stapel (oben → unten)"], zeilen),
     text("Rückgabe: [[r]]")],
    gaps(dict(F, r=auswahl(["true", "false"]))), dict(Lo, r=[v("L5_04.t6")]),
    ["Buchstaben werden ignoriert und erscheinen nicht in der Tabelle."],
    [text("Öffnende Klammern kommen oben auf, jede schließende entnimmt die passende: (, dann {, (, wieder (, dann [, (, …; am Ende ist der Stapel leer → %s. "
          "Der Stapel hat den Inhaltstyp Zeichen: push(c) verpackt automatisch, beim pop wird mit (Character) gecastet." % v("L5_04.t6"))])))

tr = [x.split(":") for x in v("L5_06.trace").strip(";").split(";")]
zeilen = []; F = {}; Lo = {}
for k, (c_, stck) in enumerate(tr):
    akt = "push %s" % c_ if c_.isdigit() else "rechnen"
    zeilen.append([c_, akt, "[[s%d]]" % k]); F["s%d" % k] = txt("code", 12); Lo["s%d" % k] = listvar(list(reversed(L_(stck))))
L5.append(add(aufgabe("W4-L5-06", "Der Rechenschieber des Zollmeisters", 2, "Tracetabelle", ["P8"],
    [text("Werte den Postfix-Ausdruck `83-52*+` aus (einstellige Zahlen, Rechenzeichen + − *). Gib nach jedem Zeichen den Stapel an (oben zuerst)."), code(C["L5_06"]),
     tabelle(["Zeichen", "Aktion", "Stapel (oben → unten)"], zeilen), text("Ergebnis: [[e]]")],
    gaps(dict(F, e=zahl())), dict(Lo, e=[v("L5_06.p0")]),
    ["Beim Rechenzeichen ist der zuerst entnommene Wert der RECHTE Operand b."],
    [text("8, 3 → 8 − 3 = 5; dann 5, 2 → 5 · 2 = 10 (Stapel 10, 5); + → 5 + 10 = %s. Die Ziffer wird mit `(int) c - (int) '0'` zur Zahl." % v("L5_06.p0"))])))

L5.append(add(aufgabe("W4-L5-07", "Postfix übersetzen", 3, "Funktionsweise erläutern", ["P4"],
    [text("Übersetze in Postfix-Schreibweise (Operanden in derselben Reihenfolge, ohne Leerzeichen) und berechne mit dem Postfix-Rechner."),
     tabelle(["Ausdruck", "Postfix", "Wert"], [["(7 − 2) · (3 + 1)", "[[p1]]", "[[w1]]"], ["9 − 4 − 2 (von links)", "[[p2]]", "[[w2]]"], ["9 − (4 − 2)", "[[p3]]", "[[w3]]"]]),
     text("Ein Mitschüler entnimmt beim Rechenzeichen zuerst den **linken** Operanden. Sein Rechner liefert für `94-2-` den Wert [[f]].")],
    gaps({"p1": txt("code", 10), "w1": zahl(), "p2": txt("code", 10), "w2": zahl(), "p3": txt("code", 10), "w3": zahl(), "f": zahl()}),
    {"p1": ["72-31+*"], "w1": [v("L5_06.p1")], "p2": ["94-2-"], "w2": [v("L5_06.p2")], "p3": ["942--"], "w3": [v("L5_06.p3")], "f": [v("L5_07f.p2")]},
    ["Das Rechenzeichen steht hinter seinen beiden Operanden.", "Klammern legen fest, welches Rechenzeichen zuletzt angewandt wird."],
    [text("72-31+* = %s, 94-2- = %s, 942-- = %s. Mit vertauschten Operanden: 4 − 9 = −5, dann 2 − (−5) = %s statt 3 – betroffen sind nur nicht kommutative Rechenzeichen wie −." %
          (v("L5_06.p1"), v("L5_06.p2"), v("L5_06.p3"), v("L5_07f.p2")))])))

L5.append(add(aufgabe("W4-L5-08", "Bug-Hunt: Klammerprüfung", 3, "Fehler im Java-Code", ["P1"],
    [text("Diese Fassung von klammernOk enthält zwei Fehler (`passt(auf, zu)` prüft, ob die Klammerarten zusammengehören)."), code(C["L5_08"]),
     text("**Teil 1:** `klammernOk(\"(()\")` liefert [[g1]], `klammernOk(\"())\")` führt zu [[g2]].\n\n**Teil 2:** Markiere die **zwei** fehlerhaften Zeilen.\n\n"
          "**Teil 3:** Korrigiere die letzte Anweisung: `return [[g3]];`")],
    [gaps({"g1": auswahl(["true", "false"]), "g2": auswahl(["true", "false", "IllegalStateException", "ClassCastException"]), "g3": txt("code", 16)}), lines(1, 2)],
    [{"g1": [v("L5_08.a")], "g2": [v("L5_08.b")], "g3": ["offen.isEmpty()"]}, {"zeilen": [8, 14]}],
    ["Was passiert bei einer schließenden Klammer, wenn der Stapel leer ist?", "Was bedeutet es, wenn am Ende noch Klammern auf dem Stapel liegen?"],
    [text("Zeile 8: pop() ohne Leer-Abfrage – bei \"())\" kommt die letzte ) bei leerem Stapel → %s (P1). Richtig: vorher `if (offen.isEmpty()) { return false; }`. "
          "Zeile 14: `return true` übersieht noch offene Klammern – \"(()\" liefert fälschlich %s. Richtig: `return offen.isEmpty();`." % (v("L5_08.b"), v("L5_08.a")))])))

# =====================================================================
# Level 4.6 – Kür: Die Flut – Schlange gegen Stapel (DS 29)
# =====================================================================
L6 = []
L6.append(add(aufgabe("W4-L6-01", "Schlange oder Stapel?", 1, "Funktionsweise erläutern", ["P10"],
    [text("Der iterative Flood-Fill (Level 4.6) merkt sich die noch zu bearbeitenden Felder in einer Ablage – einer Schlange oder einem Stapel. Markiert wird beim Einfügen. Welche Aussagen sind richtig? (Mehrere Antworten möglich.)")],
    choice([("a", "Beide Varianten markieren am Ende dieselben Felder."), ("b", "Die Schlangen-Variante breitet sich in Wellen um den Start aus (Breitensuche)."),
            ("c", "Die Stapel-Variante markiert die Felder in derselben Reihenfolge wie das rekursive Lüften aus Welt 3."),
            ("d", "Weil beim Einfügen markiert wird, kommt kein Feld zweimal in die Ablage."), ("e", "Mit der Schlange kann ein Feld zweimal markiert werden.")], True),
    {"richtig": ["a", "b", "d"]},
    ["Markiert wird genau die Menge der vom Start erreichbaren Felder – egal mit welcher Ablage."],
    [text("a, b, d sind richtig. c ist falsch: Die Stapel-Variante markiert alle freien Nachbarn eines Feldes sofort beim Einfügen und geht erst dann vom zuletzt eingefügten aus weiter – die Rekursion geht sofort vom ersten Nachbarn in die Tiefe. "
          "e ist falsch: Markierte Felder werden nicht erneut eingefügt.")])))

BE = ras(BECKEN)
qf = [[int(a) for a in p.split(",")] for p in v("L6_02.q").split("#")[0].strip(";").split(";")]
sf = [[int(a) for a in p.split(",")] for p in v("L6_02.s").split("#")[0].strip(";").split(";")]
FLUT_INFO = text("Algorithmus: Start markieren und in die Ablage legen. Solange die Ablage nicht leer ist: ein Feld entnehmen und seine Nachbarn in der Reihenfolge **oben, rechts, unten, links** prüfen – jeder freie, noch nicht markierte Nachbar wird **sofort markiert** und in die Ablage gelegt. Positionen werden als z · 1000 + s gespeichert.")
L6.append(add(aufgabe("W4-L6-02", "Die Flut mit Schlange", 2, "Tracetabelle", [],
    [FLUT_INFO, text("Im Hafenbecken (ohne Randmauer, '#' Mole) läuft die Flut ab (1|0) mit einer **Schlange**. Klicke die Felder in der Reihenfolge an, in der sie markiert werden (Start zuerst).")],
    grid(BE), {"zellen": qf, "reihenfolge": True},
    ["Die Schlange arbeitet die Felder in der Reihenfolge ab, in der sie markiert wurden.", "Von (1|0) aus werden zuerst (0|0) und (2|0) markiert."],
    [text("Reihenfolge: " + ", ".join("(%d|%d)" % (a, b) for a, b in qf) + ". Erst alle Felder mit Abstand 1 vom Start, dann Abstand 2 usw. – Wellen (Breitensuche).")])))
L6.append(add(aufgabe("W4-L6-03", "Die Flut mit Stapel", 2, "Tracetabelle", [],
    [FLUT_INFO, text("Gleiches Hafenbecken, Start (1|0), jetzt mit einem **Stapel** als Ablage. Klicke die Felder in der Reihenfolge an, in der sie markiert werden (Start zuerst).")],
    grid(BE), {"zellen": sf, "reihenfolge": True},
    ["Nach dem Start werden (0|0) und (2|0) markiert – entnommen wird aber das zuletzt eingefügte Feld (2|0)."],
    [text("Reihenfolge: " + ", ".join("(%d|%d)" % (a, b) for a, b in sf) + ". Der Stapel macht immer beim zuletzt eingefügten Feld weiter und läuft deshalb zuerst die untere Reihe entlang. "
          "Markiert werden dieselben 10 Felder wie mit der Schlange – nur die Reihenfolge ist anders.")])))
assert sorted(map(tuple, qf)) == sorted(map(tuple, sf))

L6.append(add(aufgabe("W4-L6-04", "Positionen verpacken", 1, "Datentypen und Ausdrücke", ["P4"],
    [text("Eine Position (z|s) wird als eine Ganzzahl gespeichert: pos = z · 1000 + s, zurück mit z = pos / 1000 und s = pos % 1000 (ganzzahlig)."),
     text("- (3|7) → pos = [[g1]]\n- pos = 12045 → z = [[g2]], s = [[g3]]\n- Mit pos = z · 10 + s hätten (1|12) und (2|2) denselben Wert [[g4]].")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": zahl(), "g4": zahl()}),
    {"g1": ["3007"], "g2": ["12"], "g3": ["45"], "g4": ["22"]},
    ["/ ist bei Ganzzahlen die ganzzahlige Division, % der Rest."],
    [text("3 · 1000 + 7 = 3007; 12045 / 1000 = 12, 12045 % 1000 = 45. Mit z · 10 + s: 1 · 10 + 12 = 22 = 2 · 10 + 2 – ab 10 Spalten fallen Positionen zusammen. z · 1000 + s funktioniert für alle Karten mit weniger als 1000 Spalten (P4: ganzzahlige Division).")])))

def verschieb(n): return sum(range(n))
L6.append(add(aufgabe("W4-L6-05", "Eine Frage des Aufwands", 1, "Effizienz", [],
    [text("Eine Schlange wird mit einer dynamischen Reihung nachgebaut: enqueue = `append(x)`, dequeue = `getItem(0)` und danach `delete(0)`. Intern verschiebt `delete(0)` jedes folgende Element um eine Stelle (ein Schritt je Verschiebung). "
          "n Kisten werden eingereiht und danach alle wieder entnommen."),
     text("Verschiebungen beim Entnehmen: n = 6: [[g1]] · n = 50: [[g2]] · Wie wächst die Zahl, wenn sich n verdoppelt? [[g3]]")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": auswahl(["etwa vervierfacht", "etwa verdoppelt", "bleibt gleich"])}),
    {"g1": [str(verschieb(6))], "g2": [str(verschieb(50))], "g3": ["etwa vervierfacht"]},
    ["Beim ersten delete(0) rücken n − 1 Elemente nach, beim zweiten n − 2 …"],
    [text("(n − 1) + (n − 2) + … + 0 = n(n − 1)/2: %d für n = 6, %d für n = 50 – quadratisch. Die Schlange der Bibliothek braucht pro Operation nur konstant viele Schritte. "
          "Die dynamische Reihung lohnt sich, wenn man an beliebigen Stellen zugreifen muss." % (verschieb(6), verschieb(50)))])))

teile = [{"id": "t%d" % (i + 1), "code": z} for i, z in enumerate(POP.split("\n"))]
teile += [{"id": "d1", "code": "    kopf = new Knoten(o, kopf);"}, {"id": "d2", "code": "    return kopf.getInhalt();"}, {"id": "d3", "code": "    if (kopf.getNaechster() == null) {"}]
assert len({t["code"] for t in teile}) == len(teile)
L6.append(add(aufgabe("W4-L6-06", "Expertenpfad: pop aus Knoten", 3, "Methode implementieren", ["P1"],
    [text("MeinStapel merkt sich nur den obersten Knoten `kopf` (null = leer). Jeder Knoten kennt seinen Inhalt und den Knoten darunter."),
     klassenkarte("Knoten", ["- inhalt: Object", "- naechster: Knoten"], ["+ c Knoten(inhalt: Object, naechster: Knoten)", "+ getInhalt(): Object", "+ getNaechster(): Knoten"]),
     code("public void push(Object inhalt) {\n    kopf = new Knoten(inhalt, kopf);\n}"),
     text("Baue `pop()`: Bei leerem Stapel soll wie bei Stack eine IllegalStateException ausgelöst werden. Drei Zeilen gehören nicht hinein.")],
    order(teile), {"reihenfolgen": [["t%d" % i for i in range(1, 9)]]},
    ["Erst den Inhalt sichern, dann kopf weiterschieben."],
    [text("Leer-Abfrage `kopf == null` zuerst (sonst NullPointerException, P1), Inhalt merken, kopf auf den nächsten Knoten setzen, Inhalt liefern. "
          "Mit `return kopf.getInhalt();` vor dem Weiterschieben würde nie etwas entfernt. In 400 zufälligen Befehlen verhält sich MeinStapel wie Stack: %s; push Erz, Holz, Gold → pop liefert %s, dann %s." %
          (v("L6_06.gleich"), v("L6_06.p1"), v("L6_06.p2")))])))

L6.append(add(aufgabe("W4-L6-07", "Eine Schlange aus zwei Stapeln", 3, "ADT-Befehlsfolgen", [],
    [text("Eine Schlange wird aus zwei Stapeln gebaut:"), code(C["L6_07"]),
     text("Aufrufe: enqueue A, B, C · dequeue · enqueue D · dequeue · dequeue · enqueue E · dequeue · dequeue.\n\n"
          "- Ausgabe aller dequeue-Rückgaben hintereinander (ohne Trennzeichen, z. B. `XYZ`): [[g1]]\n- Wert von `umgeschichtet` nach dem ersten dequeue: [[g2]] · am Ende: [[g3]]")],
    gaps({"g1": txt("code", 8), "g2": zahl(), "g3": zahl()}),
    {"g1": [v("L6_07.aus")], "g2": [v("L6_07.u1")], "g3": [v("L6_07.u")]},
    ["Umgeschichtet wird nur, wenn aus leer ist – dann alles von ein nach aus.", "Ein Durchgang durch zwei Stapel dreht die Reihenfolge zweimal um."],
    [text("Das erste dequeue schichtet A, B, C um (3) und liefert A. B und C kommen aus aus; D und E liegen in ein und werden erst beim vierten dequeue umgeschichtet (insgesamt %s). Ausgabe %s – genau die FIFO-Reihenfolge. "
          "Jedes Element wird höchstens einmal umgeschichtet." % (v("L6_07.u"), v("L6_07.aus")))])))

# =====================================================================
# BOSS – Die Postkutschenstation
# =====================================================================
B = []
B.append(add(aufgabe("W4-B-01", "Der Postsack", 1, "ADT-Befehlsfolgen", [],
    [text("Im Postsack liegen die Sendungen übereinander. Gib den Inhalt des Stapels am Ende an."), code(C["B01"]), text(SIMHINW)],
    adtsim("stapel", []), {"inhalt": L_(v("B01.r"))}, ["sack.push(sack.pop()) ändert nichts."],
    [text("Brief → Paket, Brief → (pop und wieder push) unverändert → Karte oben → wieder weg → Zeitung oben → noch einmal Zeitung. Von unten: %s." % v("B01.r"))])))
B.append(add(aufgabe("W4-B-02", "Am Schalter", 1, "ADT-Befehlsfolgen", [],
    [text("Reisende warten am Schalter. Gib die Schlange am Ende an."), code(C["B02"]), text(SIMHINW)],
    adtsim("schlange", []), {"inhalt": L_(v("B02.r"))}, ["warte.enqueue(warte.dequeue()) rotiert."],
    [text("Lotte, Mats, Nele → Mats, Nele, Lotte → Nele, Lotte → Nele, Lotte, Ole → %s." % v("B02.r"))])))
B.append(add(aufgabe("W4-B-03", "Der Fahrplan", 1, "ADT-Befehlsfolgen", ["P4", "P6"],
    [text("Die Abfahrtszeiten stehen in einer dynamischen Reihung. Gib sie am Ende an."), code(C["B03"]), text(SIMHINW)],
    adtsim("dynarray", []), {"inhalt": L_(v("B03.r"))}, ["insertAt(1, 11) schiebt 13 nach hinten."],
    [text("9 → 9, 13 → 9, 11, 13 → 7, 9, 11, 13 → 7, 9, 13 → 7, 9, 15 → %s (getItem(0) = 7, gecastet, + 5)." % v("B03.r"))])))
B.append(add(aufgabe("W4-B-04", "Die richtige Struktur für die Station", 1, "Funktionsweise erläutern", ["P10"],
    [text("Ordne jeder Aufgabe der Station die am besten geeignete Datenstruktur zu.")],
    match([("e1", "Am Pferdewechsel werden die zuletzt abgelegten Sättel zuerst wieder aufgelegt."), ("e2", "Fahrgäste steigen in der Reihenfolge ihrer Ankunft ein."),
           ("e3", "Der Fahrplan: Verbindungen werden nach Uhrzeit einsortiert, einzelne gestrichen."), ("e4", "Die Werkstatt repariert Kutschen der Reihe nach."),
           ("e5", "Im Sortierfach wird der oberste Brief zuerst bearbeitet.")],
          [("st", "Stapel"), ("sc", "Schlange"), ("da", "dynamische Reihung")]),
    {"e1": "st", "e2": "sc", "e3": "da", "e4": "sc", "e5": "st"}, ["LIFO, FIFO oder Index?"],
    [text("LIFO → Stapel (Sättel, Sortierfach), FIFO → Schlange (Fahrgäste, Werkstatt), Einfügen/Löschen an beliebiger Stelle → dynamische Reihung (Fahrplan).")])))
B.append(add(aufgabe("W4-B-05", "Der Methodenkopf", 1, "Methodenkopf und Signatur", ["P3", "P4"],
    [text("Gegeben ist die Signatur `anzahlNach(q: Schlange vom Inhaltstyp Reisender, ziel: Zeichenkette): Ganzzahl` (statische Methode). Ergänze den Java-Code."),
     code("public static [[g1]] anzahlNach([[g2]] q, [[g3]] ziel) {\n    int anzahl = 0;\n    // ...\n    Reisender r = [[g4]] q.dequeue();\n    // ...\n    return anzahl;\n}", nummern=False)],
    gaps({"g1": txt(), "g2": txt(), "g3": txt(), "g4": txt("code", 12)}),
    {"g1": ["int"], "g2": ["Queue"], "g3": ["String"], "g4": ["(Reisender)"]},
    ["Die Bibliotheksklassen sind nicht generisch: kein Queue<Reisender>."],
    [text("Ganzzahl → int, Schlange → Queue (ohne spitze Klammern), Zeichenkette → String; dequeue liefert Object, deshalb der Cast (Reisender) (P3, P4).")])))

mz = C["B06"].split("\n")
zeilen = [["0", "(Start)", "6, 1, 3", "9, 4"]]; F = {}; Lo = {}
for i, z in enumerate(mz, 1):
    qv, sv = L_(v("B06.q%d" % i)), oben(v("B06.s%d" % i))
    if i in (1, 4):
        zeilen.append([str(i), z, liste(qv), liste(sv)])
    else:
        zeilen.append([str(i), z, "[[q%d]]" % i, "[[s%d]]" % i])
        F["q%d" % i] = txt("code", 12); Lo["q%d" % i] = listvar(qv); F["s%d" % i] = txt("code", 12); Lo["s%d" % i] = listvar(sv)
B.append(add(aufgabe("W4-B-06", "Gepäck und Fahrkarten", 2, "ADT-Befehlsfolgen", ["P4"],
    [text("Stapel s und Schlange q (Inhaltstyp Ganzzahl) starten mit **s = 9, 4 (oben zuerst)** und **q = 6, 1, 3 (vorne zuerst)**."), KONV,
     tabelle(["Nr.", "Anweisung", "q (vorne → hinten)", "s (oben → unten)"], zeilen), text("Wert von y: [[y]]")],
    gaps(dict(F, y=zahl())), dict(Lo, y=[v("B06.y")]),
    ["Java wertet von links nach rechts aus: Im Ausdruck von Zeile 5 wird das erste pop() zuerst ausgeführt."],
    [text("Zeile 5: Das erste pop() liefert 1, das zweite 9 → y = 1 − 9 = %s. Endzustand q = %s, s = %s (oben zuerst)." % (v("B06.y"), liste(L_(v("B06.q6"))), liste(oben(v("B06.s6")))))])))

B.append(add(aufgabe("W4-B-07", "Die ersten beiden Reisenden", 2, "Fehler im Java-Code", ["P1", "P2"],
    [text("Die Methode soll die Namen der beiden vordersten Reisenden liefern; q soll unverändert bleiben."), code(C["B07"]),
     text("**Teil 1:** Markiere die Zeile, in der es bei einer Schlange mit genau einem Namen zum Laufzeitfehler kommt.\n\n**Teil 2:** Wie sieht q = Lotte, Mats, Nele nach dem Aufruf aus (vorne zuerst)? [[g1]]")],
    [lines(1, 1), gaps({"g1": txt("code", 18)})],
    [{"zeilen": [3]}, {"g1": listvar(L_(v("B07.q")))}],
    ["a und b werden hinten wieder angestellt – aber stehen sie dann noch vorne?"],
    [text("Bei nur einem Namen trifft das zweite dequeue() in Zeile 3 die leere Schlange (P1). Und selbst bei drei Namen ist q danach %s statt Lotte, Mats, Nele: a und b stehen jetzt hinten (P2). "
          "Richtig: über eine Hilfsschlange vollständig umschichten oder mit bekannter Anzahl rotieren." % liste(L_(v("B07.q"))))])))

anz = C["B08"].split("\n")
teile = [{"id": "t%d" % (i + 1), "code": z} for i, z in enumerate(anz)]
teile += [{"id": "d1", "code": "        if (r.getZiel() == ziel) {"}, {"id": "d2", "code": "    Stack hilf = new Stack();"}, {"id": "d3", "code": "    while (q.head() != null) {"}]
assert len({t["code"] for t in teile}) == len(teile) and len(anz) == 15
b = ["t%d" % i for i in range(1, 16)]
b3 = b[:5] + ["t9", "t6", "t7", "t8"] + b[9:]
B.append(add(aufgabe("W4-B-08", "Puzzle: Reisende zählen", 2, "Methode implementieren", ["P1", "P2", "P5"],
    [text("`anzahlNach(q, ziel)` zählt die Reisenden (Klasse Reisender mit getZiel()) mit dem angegebenen Ziel. q muss danach unverändert sein. Drei Zeilen gehören nicht hinein.")],
    order(teile), {"reihenfolgen": [b, sw(b, 1, 2), b3, sw(b3, 1, 2)]},
    ["Schlange über Hilfsschlange – die Reihenfolge bleibt."],
    [text("Hilfsschlange (ein Hilfsstapel würde umdrehen), Leer-Abfrage (P1), equals statt == (P5), dieselben Objekte zurückstellen (P2). Getestet: 2 Reisende zum Hafen, q unverändert: %s." % v("B08.gleich"))])))

q = SimQueue([4, 7, 2, 9, 5, 8]); h = SimQueue(); zeilen = []; F = {}; Lo = {}
for i in range(6):
    t_ = q.dequeue()
    (h if t_ % 2 == 0 else q).enqueue(t_)
    zeilen.append([str(i), str(t_), "[[q%d]]" % i if i % 2 == 0 else liste(q.a), "[[h%d]]" % i if i % 2 == 1 else liste(h.a)])
    if i % 2 == 0: F["q%d" % i] = txt("code", 16); Lo["q%d" % i] = listvar(q.a)
    else: F["h%d" % i] = txt("code", 16); Lo["h%d" % i] = listvar(h.a)
while h.a: q.enqueue(h.dequeue())
assert liste(q.a) == v("B09.q")
B.append(add(aufgabe("W4-B-09", "Die Fahrkarten werden umgeordnet", 2, "Tracetabelle", ["P8"],
    [text("Die Schlange q enthält die Fahrkartennummern 4, 7, 2, 9, 5, 8 (vorne zuerst). Es wird `umordnen(q, 6)` aufgerufen."), code(C["B09"]),
     tabelle(["i", "t", "q nach dem Durchlauf (vorne zuerst)", "hilf (vorne zuerst)"], zeilen),
     text("q am Ende: [[e]] · Funktionsweise: [[w]]")],
    gaps(dict(F, e=txt("code", 16), w=auswahl(["ungerade Nummern zuerst, dann gerade – jeweils in alter Reihenfolge", "aufsteigend sortiert", "umgekehrte Reihenfolge", "gerade Nummern zuerst"]))),
    dict(Lo, e=listvar(q.a), w=["ungerade Nummern zuerst, dann gerade – jeweils in alter Reihenfolge"]),
    ["Ungerade Nummern werden in q hinten wieder angestellt, gerade wandern nach hilf."],
    [text("Nach 6 Runden stehen die ungeraden Nummern 7, 9, 5 in q, die geraden 4, 2, 8 in hilf; danach wird hilf angehängt: %s. Beide Gruppen behalten ihre Reihenfolge (stabil)." % liste(q.a))])))

B.append(add(aufgabe("W4-B-10", "Verbindungen streichen", 2, "Fehler im Java-Code", ["P6"],
    [text("`streiche(d, grenze)` soll alle Abfahrtszeiten kleiner als grenze entfernen."), code(C["B10"]),
     text("Für d = 6, 7, 12, 5, 9 und grenze 8 liefert die Methode d = [[g1]] (richtig wäre 12, 9)."),
     text("Welche Änderungen beheben den Fehler? (Mehrere Antworten möglich.)")],
    [gaps({"g1": txt("code", 14)}),
     choice([("a", "Die Schleife rückwärts laufen lassen: `for (int i = d.getLength() - 1; i >= 0; i--)`"), ("b", "Nach `d.delete(i);` die Anweisung `i--;` einfügen."),
             ("c", "`i <= d.getLength()` statt `i < d.getLength()`"), ("d", "`<= grenze` statt `< grenze`")], True)],
    [{"g1": listvar(L_(v("B10.d")))}, {"richtig": [k for k, key in zip("abcd", ("B10a", "B10b", "B10c", "B10d")) if v(key + ".d") == "12, 9"]}],
    ["Nach delete(i) rückt der Nachfolger auf Index i."],
    [text("Gemessen: Original %s · rückwärts %s · mit i-- %s · mit <= getLength() %s · mit <= grenze %s. Nach einem delete rückt der Nachfolger nach und wird durch i++ übersprungen (P6)." %
          (v("B10.d"), v("B10a.d"), v("B10b.d"), v("B10c.d"), v("B10d.d")))])))
assert v("B10a.d") == v("B10b.d") == "12, 9"

B.append(add(aufgabe("W4-B-11", "Struktogramm: Einbuchen nach Uhrzeit", 3, "Code ↔ Struktogramm", ["P1", "P9"],
    [text("Der Fahrplan (dynamische Reihung vom Inhaltstyp Ganzzahl) ist aufsteigend sortiert. `einbuchen(plan, zeit)` fügt zeit so ein, dass er sortiert bleibt – hinter gleiche Zeiten. Laufzeitfehler sind auszuschließen."),
     struk("einbuchen(plan: dynamische Reihung vom Inhaltstyp Ganzzahl, zeit: Ganzzahl): nichts", [
         {"anw": "pos ← 0"}, {"solange": "[[g1]]", "rumpf": [{"anw": "pos ← pos + 1"}]}, {"aufruf": "plan.insertAt([[g2]], zeit)"}]),
     text("Für plan = 7, 9, 11, 14 ergibt `einbuchen(plan, 11)` den Fahrplan [[g3]].")],
    gaps({"g1": auswahl(["pos < plan.getLength() und plan.getItem(pos) ≤ zeit", "plan.getItem(pos) ≤ zeit und pos < plan.getLength()",
                         "pos < plan.getLength() und plan.getItem(pos) < zeit", "pos ≤ plan.getLength() und plan.getItem(pos) ≤ zeit"]),
          "g2": txt(), "g3": txt("code", 18)}),
    {"g1": ["pos < plan.getLength() und plan.getItem(pos) ≤ zeit"], "g2": ["pos"], "g3": listvar(L_(v("B11.p")))},
    ["Die Index-Abfrage muss LINKS stehen.", "≤ statt <: gleiche Zeiten werden übersprungen."],
    [text("Die Index-Abfrage steht links, damit `getItem(pos)` bei pos = Länge nicht mehr ausgewertet wird (vertauscht: %s beim Anhängen, P1); ≤ fügt hinter gleiche Zeiten ein. Ergebnis %s; eine leere Liste ergibt einfach {8}." %
          (v("B11f.p"), v("B11.p")))])))

B.append(add(aufgabe("W4-B-12", "Der unterste Postsack", 3, "Fehler im Java-Code", ["P1", "P2"],
    [code(C["B12"]), text("Welche Aussagen über `untersterSack(s)` (Stapel vom Inhaltstyp Zeichenkette) sind richtig? (Mehrere Antworten möglich.)")],
    choice([("a", "Für einen leeren Stapel kommt es zu einem Laufzeitfehler."), ("b", "s ist nach dem Aufruf umgedreht."),
            ("c", "Die Methode liefert das oberste Element."), ("d", "Für einen nicht leeren Stapel liefert sie das unterste Element, und s ist danach unverändert."),
            ("e", "Der Cast (String) ist überflüssig.")], True),
    {"richtig": ["a", "d"]},
    ["Nach dem Umschichten liegt das unterste Element von s oben auf hilf."],
    [text("Für Brief, Paket, Karte (Brief unten) liefert die Methode %s, s ist unverändert (%s). Bei leerem s ist hilf leer → hilf.top() → %s (P1). Korrektur: vorher `if (s.isEmpty()) { return \"\"; }` o. ä. "
          "Der Cast ist nötig, weil top() Object liefert." % (v("B12.r"), v("B12.gleich"), v("B12.leer")))])))

B.append(add(aufgabe("W4-B-13", "Der Fahrpreis-Rechner", 3, "Funktionsweise erläutern", ["P4"],
    [text("Die Station berechnet Fahrpreise mit dem Postfix-Rechner aus Level 4.5 (einstellige Zahlen, + − *)."),
     text("- `62*43-+` ergibt [[g1]]\n- `95-3*` ergibt [[g2]]; als Ausdruck mit Klammern: [[g3]]\n- Ein Rechner, der beim Rechenzeichen zuerst den linken Operanden entnimmt, liefert für `95-3*` den Wert [[g4]].")],
    gaps({"g1": zahl(), "g2": zahl(), "g3": auswahl(["(9 − 5) · 3", "9 − 5 · 3", "9 − (5 · 3)", "(9 − 3) · 5"]), "g4": zahl()}),
    {"g1": [v("L5_06.p4")], "g2": [v("L5_06.p5")], "g3": ["(9 − 5) · 3"], "g4": [v("L5_07f.p5")]},
    ["Der zuerst entnommene Wert ist der rechte Operand."],
    [text("62* = 12, 43- = 1, 12 + 1 = %s. 95- = 4, 4 · 3 = %s. Mit vertauschten Operanden: 5 − 9 = −4, dann 3 · (−4) = %s." % (v("L5_06.p4"), v("L5_06.p5"), v("L5_07f.p5")))])))

assert (v("B14.r8"), v("B14.r9"), v("B14.r10")) == ("Abfahrt 15", "Abfahrt 10", "Abfahrt 10")
B.append(add(aufgabe("W4-B-14", "Der Fahrplan-Editor", 3, "ADT-Befehlsfolgen", [],
    [ZB_KARTE, ZB_INFO, text("Der Fahrplan-Editor der Station benutzt ein Zugbuch b:"), code(ZB2_TXT),
     text("Gib beide Stapel am Ende an. " + SIMHINW + "\n\n**Teil 1:** erledigt · **Teil 2:** zurueckgenommen")],
    [adtsim("stapel", []), adtsim("stapel", [])],
    [{"inhalt": L_(v("B14.e"))}, {"inhalt": L_(v("B14.z"))}],
    ["Ein neuer Zug leert zurueckgenommen."],
    [text("Nach zug(\"Abfahrt 15\") ist zurueckgenommen leer. Danach: rueckgaengig → Abfahrt 15, rueckgaengig → Abfahrt 10, wiederholen → Abfahrt 10. Ende: erledigt (unten → oben) %s, zurueckgenommen %s." %
          (v("B14.e"), v("B14.z")))])))

B.append(add(aufgabe("W4-B-15", "Umsteigen", 2, "ADT-Befehlsfolgen", [],
    [text("Der Stapel s enthält Lotte, Mats, Nele (**oben zuerst**). Zuerst wird mit `while (!s.isEmpty()) { q.enqueue(s.pop()); }` in eine leere Schlange q umgeladen, danach mit `while (!q.isEmpty()) { s.push(q.dequeue()); }` zurück."), KONV,
     text("- q nach dem ersten Umladen (vorne zuerst): [[g1]]\n- s nach dem zweiten Umladen (oben zuerst): [[g2]]")],
    gaps({"g1": txt("code", 16), "g2": txt("code", 16)}),
    {"g1": listvar(L_(v("B15.q"))), "g2": listvar(oben(v("B15.s")))},
    ["Das oberste Element von s steht danach vorne in q."],
    [text("q = %s; zurück in den Stapel kommt Lotte zuerst und liegt unten: s = %s (oben zuerst) – umgedreht. Für „unverändert“ braucht man einen Hilfsstapel statt der Schlange." % (v("B15.q"), liste(oben(v("B15.s")))))])))

# =====================================================================
LEVELS = [
    ("W4-L1", "4.1", "Kistenturm und Schiffsschlange: Stapel und Schlange", [24], "AB 1 Stapel und Schlange – Teil 1 (Aufgaben 1–4, 9)",
     "AQ_W4_L4_Hafen_Geruest.txt – Level 4.1 (Klasse Hafen)",
     [hinweis("**Merke:** Stapel = LIFO (push, pop, top), Schlange = FIFO (enqueue, dequeue, head). Die Abitur-Klassen sind **nicht generisch**: Beim Herausholen wird gecastet, z. B. `(Kiste) s.pop()`, `(Integer) q.dequeue()`. "
              "**Leer?** – vor pop/top/dequeue/head immer `isEmpty()` prüfen."), KONV], L1),
    ("W4-L2", "4.2", "Kür: Zugbuch und Initiative – Spielmodule", [25], "AB 1 Stapel und Schlange – Teil 2 (Aufgaben 6–8)",
     "AQ_W4_L4_Hafen_Geruest.txt – Level 4.2 (Klassen Zugbuch und Initiative)",
     [hinweis("**Merke:** Rückgängig/Wiederholen = zwei Stapel; Zugreihenfolge = Schlange mit Rotieren. Eignung begründen: Zugriffsprinzip (LIFO, FIFO, Index) + benötigte Operationen."),
      text("Kür-Level: Baue Spielmodule für dein Dungeon-Spiel.")], L2),
    ("W4-L3", "4.3", "Inventur: Struktur unverändert lassen", [26], "AB 2 – Teil 1 (Aufgaben 1–5)",
     "AQ_W4_L4_Hafen_Geruest.txt – Level 4.3 (Klasse Unveraendert)",
     [hinweis("**Merke:** Unverändert = **dieselben Objekte in derselben Reihenfolge**. Rezept: auswerten – zwischenlagern – zurückschichten – erst dann `return`. "
              "Stapel über Hilfsstapel, Schlange über Hilfsschlange oder Rotieren mit bekannter Anzahl."), KONV], L3),
    ("W4-L4", "4.4", "Ladeliste: dynamische Reihung", [27], "AB 2 – Teil 2 (Aufgaben 6–10)",
     "AQ_W4_L4_Hafen_Geruest.txt – Level 4.4 (Klasse Ladeliste)",
     [hinweis("**Merke:** DynArray: getItem, setItem, delete nur für 0 ≤ i < getLength(); insertAt bis getLength(). insertAt schiebt nach hinten, delete nach vorn. "
              "Löschen in Schleifen: rückwärts laufen oder i nur ohne Löschen erhöhen. Erst merken (getItem), dann löschen."), KONV], L4),
    ("W4-L5", "4.5", "Zollamt: Umformen, Klammern, Postfix", [28], "AB 3 – Teil 1 (Aufgaben 1–4)",
     "AQ_W4_L4_Hafen_Geruest.txt – Level 4.5 (Klasse Umformen)",
     [hinweis("**Merke:** Jeder Weg durch einen Stapel dreht die Reihenfolge um, Schlange und append erhalten sie. Klammerprüfung: Leer? vor jedem pop, am Ende `isEmpty()`. "
              "Postfix: Der zuerst entnommene Wert ist der rechte Operand."), KONV], L5),
    ("W4-L6", "4.6", "Kür: Die Flut – Schlange gegen Stapel", [29], "AB 3 – Teil 2 (Aufgaben 5–7)",
     "AQ_W4_L4_Hafen_Geruest.txt – Level 4.6 (Klassen Expertenpfad, Knoten, MeinStapel)",
     [hinweis("**Merke:** Iterativer Flood-Fill: mit Schlange in Wellen (Breitensuche), mit Stapel in die Tiefe – dieselben Felder, andere Reihenfolge. Markiert wird beim Einfügen."),
      text("Kür-Level: Die Flut läuft ins Hafenbecken – und du baust einen Stapel aus Knoten.")], L6),
]

welt = {"version": 2, "welt": 4, "titel": "Der Hafen", "farbe": "#2E75B6", "levels": [],
        "boss": {"id": "W4-BOSS", "titel": "Die Postkutschenstation", "dauerMin": 25, "anzahl": 8, "mix": {"1": 3, "2": 3, "3": 2}, "pool": B},
        "aufgaben": A}
for lid, nr, titel, ds, ab, ide, intro, auf in LEVELS:
    welt["levels"].append({"id": lid, "nr": nr, "titel": titel, "ds": ds, "ab": ab, "ide": ide, "intro": intro, "aufgaben": auf})
json.dump(welt, open(SCRATCH + "/algolab/content/welt4.json", "w"), ensure_ascii=False, indent=1)
print("welt4.json:", len(A), "Aufgaben")
