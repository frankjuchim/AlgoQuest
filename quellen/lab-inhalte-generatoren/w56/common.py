# Gemeinsame Werkzeuge fuer die Inhalte Welt 5/6 (Algo Quest Lab)
# - Baum-Modell (Klammerformat), Traversierungen mit Pfaden, BST, Heap
# - Block-/Interaktions-Helfer nach SPEC_AlgoLab §3-§5
# - Java-Verifikation (javac 21 + NI-Stub)
import json, os, re, subprocess, shutil, itertools

SCRATCH = "/tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad"
W = SCRATCH + "/algolab/w56"
NI = SCRATCH + "/w4_code/harness/NI.java"

LAB_KATEGORIEN = ["Datentypen und Ausdrücke", "Methodenkopf und Signatur", "Klasse vs. Objekt",
    "Bestandteile einer Klasse", "Objektkarten und Referenzen", "Klassendiagramm", "Struktogramm lesen",
    "Code ↔ Struktogramm", "Tracetabelle", "Rekursionstabelle", "Fehler im Java-Code", "Fehler im Struktogramm",
    "Lückencode", "Methode implementieren", "ADT-Befehlsfolgen", "Sortieren und Suchen", "Effizienz", "Bäume",
    "Funktionsweise erläutern"]

# ---------------------------------------------------------------- Baum-Modell
class N:
    __slots__ = ("v", "l", "r")
    def __init__(self, v, l=None, r=None):
        self.v, self.l, self.r = v, l, r

def parse(s):
    pos = [0]
    def val():
        st = pos[0]
        while pos[0] < len(s) and s[pos[0]] not in "(),":
            pos[0] += 1
        return s[st:pos[0]].strip()
    def tree():
        v = val()
        if v == "-":
            return None
        if v == "":
            raise ValueError("leerer Wert in " + s)
        n = N(v)
        if pos[0] < len(s) and s[pos[0]] == "(":
            pos[0] += 1
            n.l = tree()
            if s[pos[0]] != ",":
                raise ValueError("Komma erwartet: " + s)
            pos[0] += 1
            n.r = tree()
            if s[pos[0]] != ")":
                raise ValueError(") erwartet: " + s)
            pos[0] += 1
        return n
    t = tree()
    if pos[0] != len(s):
        raise ValueError("Rest: " + s[pos[0]:])
    return t

def ks(t):
    if t is None:
        return "-"
    if t.l is None and t.r is None:
        return t.v
    return t.v + "(" + ks(t.l) + "," + ks(t.r) + ")"

def norm(s):
    return ks(parse(s))

def nodes_pre(t, p=""):
    if t is None:
        return []
    return [(p, t)] + nodes_pre(t.l, p + "L") + nodes_pre(t.r, p + "R")

def nodes_in(t, p=""):
    if t is None:
        return []
    return nodes_in(t.l, p + "L") + [(p, t)] + nodes_in(t.r, p + "R")

def nodes_post(t, p=""):
    if t is None:
        return []
    return nodes_post(t.l, p + "L") + nodes_post(t.r, p + "R") + [(p, t)]

def nodes_level(t):
    out, q = [], ([("", t)] if t else [])
    while q:
        p, n = q.pop(0)
        out.append((p, n))
        if n.l: q.append((p + "L", n.l))
        if n.r: q.append((p + "R", n.r))
    return out

def vals(lst):
    return [n.v for p, n in lst]

def paths(lst):
    return [p for p, n in lst]

def node_at(t, p):
    for c in p:
        if t is None:
            return None
        t = t.l if c == "L" else t.r
    return t

def hoehe(t):
    return 0 if t is None else 1 + max(hoehe(t.l), hoehe(t.r))

def anzahl(t):
    return 0 if t is None else 1 + anzahl(t.l) + anzahl(t.r)

def blaetter(t):
    if t is None: return []
    if t.l is None and t.r is None: return [t.v]
    return blaetter(t.l) + blaetter(t.r)

def copy(t):
    return None if t is None else N(t.v, copy(t.l), copy(t.r))

# BST mit int-Werten (Werte als Strings im Modell)
def bst_insert(t, x):
    if t is None:
        return N(str(x))
    w = int(t.v)
    if x < w: t.l = bst_insert(t.l, x)
    elif x > w: t.r = bst_insert(t.r, x)
    return t

def bst_from(seq):
    t = None
    for x in seq:
        t = bst_insert(t, x)
    return t

def bst_path(t, x):
    p, out = "", []
    while t is not None:
        out.append(p)
        w = int(t.v)
        if x == w: return out, True
        if x < w: t, p = t.l, p + "L"
        else: t, p = t.r, p + "R"
    return out, False

def bst_delete(t, x, variante="nachfolger"):
    if t is None: return None
    w = int(t.v)
    if x < w: t.l = bst_delete(t.l, x, variante); return t
    if x > w: t.r = bst_delete(t.r, x, variante); return t
    if t.l is None: return t.r
    if t.r is None: return t.l
    if variante == "nachfolger":
        m = t.r
        while m.l: m = m.l
        t.v = m.v; t.r = bst_delete(t.r, int(m.v), variante)
    else:
        m = t.l
        while m.r: m = m.r
        t.v = m.v; t.l = bst_delete(t.l, int(m.v), variante)
    return t

def is_bst(t, lo=None, hi=None):
    if t is None: return True
    w = int(t.v)
    if lo is not None and w <= lo: return False
    if hi is not None and w >= hi: return False
    return is_bst(t.l, lo, w) and is_bst(t.r, w, hi)

def nur_kinder(t):
    if t is None: return True
    w = int(t.v)
    if t.l and int(t.l.v) >= w: return False
    if t.r and int(t.r.v) <= w: return False
    return nur_kinder(t.l) and nur_kinder(t.r)

def ausgeglichen(r, lo=None, hi=None, log=None, tiefe=0):
    if lo is None: lo, hi = 0, len(r) - 1
    if lo > hi:
        if log is not None: log.append((tiefe, lo, hi, None))
        return None
    m = (lo + hi) // 2
    if log is not None: log.append((tiefe, lo, hi, m))
    n = N(str(r[m]))
    n.l = ausgeglichen(r, lo, m - 1, log, tiefe + 1)
    n.r = ausgeglichen(r, m + 1, hi, log, tiefe + 1)
    return n

def from_pre_in(pre, ino):
    if not pre: return None
    w = pre[0]; i = ino.index(w)
    return N(w, from_pre_in(pre[1:1 + i], ino[:i]), from_pre_in(pre[1 + i:], ino[i + 1:]))

def from_post_in(post, ino):
    if not post: return None
    w = post[-1]; i = ino.index(w)
    return N(w, from_post_in(post[:i], ino[:i]), from_post_in(post[i:-1], ino[i + 1:]))

# ---------------------------------------------------------------- Bloecke
def T(md): return {"t": "text", "md": md}
def H(md): return {"t": "hinweis", "md": md}
def C(code, nummern=True, markiere=None):
    b = {"t": "code", "code": code.strip("\n"), "nummern": nummern}
    if markiere: b["markiere"] = markiere
    return b
def BAUM(s):
    parse(s)
    return {"t": "baum", "baum": s}
def TAB(kopf, zeilen): return {"t": "tabelle", "kopf": kopf, "zeilen": zeilen}
def STR(kopf, rumpf): return {"t": "struktogramm", "kopf": kopf, "rumpf": rumpf}
def REIH(werte, markiert=None, indizes=True):
    b = {"t": "reihung", "werte": werte, "indizes": indizes}
    if markiert: b["markiert"] = markiert
    return b
def RAST(zeilen): return {"t": "raster", "zeilen": zeilen}
def ADT(art, inhalt): return {"t": "adt", "art": art, "inhalt": inhalt}
def KK(name, attribute, methoden): return {"t": "klassenkarte", "name": name, "attribute": attribute, "methoden": methoden}

# ---------------------------------------------------------------- Felder / Interaktionen
def Z(breite=None):
    f = {"typ": "zahl"}
    if breite: f["breite"] = breite
    return f
def TX(norm="code", breite=None):
    f = {"typ": "text", "norm": norm}
    if breite: f["breite"] = breite
    return f
def AW(optionen):
    return {"typ": "auswahl", "optionen": list(optionen)}
WF = ["wahr", "falsch"]
TFL = ["true", "false", "Laufzeitfehler"]

def gaps(felder): return {"kind": "gaps", "felder": felder}
def choice(optionen, mehrfach=False):
    return {"kind": "choice", "optionen": [{"id": i, "md": m} for i, m in optionen], "mehrfach": mehrfach}
def order(teile):
    out = []
    for i, x in teile:
        out.append({"id": i, "code": x})
    return {"kind": "order", "teile": out}
def lines(block, anzahl): return {"kind": "lines", "block": block, "anzahl": anzahl}
def match(elemente, kategorien):
    return {"kind": "match", "elemente": [{"id": i, "md": m} for i, m in elemente],
            "kategorien": [{"id": i, "md": m} for i, m in kategorien]}
def tree_klick(baum):
    parse(baum)
    return {"kind": "tree", "modus": "klick", "baum": baum}
def tree_bauen(start, werte=None):
    parse(start)
    d = {"kind": "tree", "modus": "bauen", "start": start}
    if werte is not None: d["werte"] = [str(w) for w in werte]
    return d
def array_tausch(start, fertigKnopf=False):
    d = {"kind": "array", "modus": "tausch", "start": start}
    if fertigKnopf: d["fertigKnopf"] = True
    return d
def array_klick(start): return {"kind": "array", "modus": "klick", "start": start}
def grid(raster): return {"kind": "grid", "raster": raster}
def adtsim(art, start): return {"kind": "adtsim", "art": art, "start": start}

PUNKTE = {1: 10, 2: 20, 3: 30}

def task(id, titel, stufe, kategorie, fallen, inhalt, interaktion, loesung, erklaerung, tipps=None):
    assert kategorie in LAB_KATEGORIEN, kategorie
    d = {"id": id, "titel": titel, "stufe": stufe, "punkte": PUNKTE[stufe], "kategorie": kategorie,
         "fallen": fallen, "inhalt": inhalt, "interaktion": interaktion, "loesung": loesung}
    if tipps: d["tipps"] = tipps
    d["erklaerung"] = erklaerung
    return d

# ---------------------------------------------------------------- Java
JHELP = r'''
package aq;
class K {
    static String k(BinTree b) {
        if (b.isEmpty()) return "-";
        String w = String.valueOf(b.getItem());
        if (b.isLeaf()) return w;
        return w + "(" + k(b.getLeft()) + "," + k(b.getRight()) + ")";
    }
    private static String s; private static int pos; private static boolean nurText;
    static BinTree baue(String str) { s = str; pos = 0; nurText = false; BinTree t = tree(); if (pos != s.length()) throw new RuntimeException("Rest"); return t; }
    static BinTree baueS(String str) { s = str; pos = 0; nurText = true; BinTree t = tree(); if (pos != s.length()) throw new RuntimeException("Rest"); return t; }
    private static String val() { int st = pos; while (pos < s.length() && "(),".indexOf(s.charAt(pos)) < 0) pos++; return s.substring(st, pos).trim(); }
    private static BinTree tree() {
        String v = val();
        if (v.equals("-")) return new BinTree();
        Object o = v;
        if (!nurText && v.matches("-?[0-9]+")) o = Integer.valueOf(Integer.parseInt(v));
        BinTree b = new BinTree(o);
        if (pos < s.length() && s.charAt(pos) == '(') { pos++; b.setLeft(tree()); pos++; b.setRight(tree()); pos++; }
        return b;
    }
    static String pre(BinTree b) { if (b.isEmpty()) return ""; return b.getItem() + " " + pre(b.getLeft()) + pre(b.getRight()); }
    static String in(BinTree b) { if (b.isEmpty()) return ""; return in(b.getLeft()) + b.getItem() + " " + in(b.getRight()); }
    static String post(BinTree b) { if (b.isEmpty()) return ""; return post(b.getLeft()) + post(b.getRight()) + b.getItem() + " "; }
    static String level(BinTree b) {
        String text = ""; Queue q = new Queue();
        if (!b.isEmpty()) q.enqueue(b);
        while (!q.isEmpty()) { BinTree k = (BinTree) q.dequeue(); text = text + k.getItem() + " ";
            if (!k.getLeft().isEmpty()) q.enqueue(k.getLeft()); if (!k.getRight().isEmpty()) q.enqueue(k.getRight()); }
        return text;
    }
    static void out(String key, Object v) { System.out.println("@@" + key + "=" + v); }
    // Zeile (1-basiert, relativ zum Snippet) des obersten Stack-Frames in Klasse cls
    static int zeile(Throwable e, String cls, int offset) {
        for (StackTraceElement st : e.getStackTrace()) if (st.getClassName().equals("aq." + cls)) return st.getLineNumber() - offset;
        return -1;
    }
}
'''

class Java:
    """Sammelt Klassen; jede Klasse: Snippet (gezeigter Code) + run()-Methode."""
    def __init__(self, name):
        self.name = name
        self.dir = W + "/java_" + name
        self.classes = []      # (cls, source)
        self.fails = []        # (key, cls, source)  -> erwartet Kompilierfehler
        self.results = {}

    def add(self, cls, snippet, run, extra=""):
        # Zeile 1: package, Zeile 2: class-Kopf, ab Zeile 3: Snippet
        src = "package aq;\nclass %s {\n%s\n%s\n    static void run() throws Exception {\n%s\n    }\n}\n" % (cls, snippet, extra, run)
        self.classes.append((cls, src))
        return 2  # Offset: Snippetzeile = Dateizeile - 2

    def add_raw(self, cls, src):
        self.classes.append((cls, src))

    def expect_compile_error(self, key, cls, snippet, extra=""):
        src = "package aq;\nclass %s {\n%s\n%s\n}\n" % (cls, snippet, extra)
        self.fails.append((key, cls, src))

    def run(self):
        if os.path.exists(self.dir): shutil.rmtree(self.dir)
        os.makedirs(self.dir + "/src/aq"); os.makedirs(self.dir + "/bin")
        shutil.copy(NI, self.dir + "/src/aq/NI.java")
        open(self.dir + "/src/aq/K.java", "w").write(JHELP)
        for cls, src in self.classes:
            open(self.dir + "/src/aq/%s.java" % cls, "w").write(src)
        main = "package aq;\npublic class Main {\n public static void main(String[] a) {\n"
        for cls, src in self.classes:
            if "static void run()" in src:
                main += '  try { %s.run(); } catch (Throwable e) { System.out.println("@@FEHLER.%s=" + e); }\n' % (cls, cls)
        main += " }\n}\n"
        open(self.dir + "/src/aq/Main.java", "w").write(main)
        files = [self.dir + "/src/aq/" + f for f in os.listdir(self.dir + "/src/aq")]
        r = subprocess.run(["javac", "-Xlint:none", "-encoding", "UTF-8", "-d", self.dir + "/bin"] + files,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr); raise SystemExit("javac-Fehler in " + self.name)
        r = subprocess.run(["java", "-Xss64m", "-cp", self.dir + "/bin", "aq.Main"], capture_output=True, text=True, timeout=300)
        for line in r.stdout.splitlines():
            if line.startswith("@@"):
                k, v = line[2:].split("=", 1)
                self.results[k] = v
        errs = {k: v for k, v in self.results.items() if k.startswith("FEHLER.")}
        if errs:
            raise SystemExit("Java-Laufzeitfehler: %s" % errs)
        # erwartete Kompilierfehler
        for key, cls, src in self.fails:
            d = self.dir + "/fail_" + cls
            os.makedirs(d + "/aq"); os.makedirs(d + "/bin")
            open(d + "/aq/%s.java" % cls, "w").write(src)
            shutil.copy(NI, d + "/aq/NI.java")
            r = subprocess.run(["javac", "-Xlint:none", "-encoding", "UTF-8", "-d", d + "/bin", d + "/aq/%s.java" % cls, d + "/aq/NI.java"],
                               capture_output=True, text=True)
            if r.returncode == 0:
                raise SystemExit("erwarteter Kompilierfehler blieb aus: " + key)
            m = re.search(r"%s\.java:(\d+): error: (.*)" % cls, r.stderr)
            self.results[key] = str(int(m.group(1)) - 2)
            self.results[key + ".msg"] = m.group(2)
        return self.results

def wl(lst):
    """Liste -> 'a b c ' (Format der Traversierungs-Zeichenkette)"""
    return "".join(str(x) + " " for x in lst)

# ---------------------------------------------------------------- Code-Puzzle (order) per Java pruefen
DECL = re.compile(r"\b(?:int|boolean|String|BinTree|double|char|Queue|Stack|DynArray)\s+(\w+)\s*=")
def _decl(code): return set(DECL.findall(code))
def _uses(code): return set(re.findall(r"\b([a-z]\w*)\b", code))

class OrderCheck:
    """Alle Permutationen der mittleren Teile werden kompiliert und getestet; gueltig = Tests gruen."""
    def __init__(self, java, key, teile, erst, mitte, letzt, test, praefix, signatur_vars=()):
        self.key, self.teile, self.erst, self.mitte, self.letzt = key, teile, erst, mitte, letzt
        self.kand = []
        n = 0
        for perm in itertools.permutations(mitte):
            ordnung = list(erst) + list(perm) + list(letzt)
            # Deklaration vor Benutzung (sonst Kompilierfehler)
            ok, bekannt = True, set(signatur_vars)
            alle_decl = set().union(*[_decl(teile[i]) for i in ordnung])
            for i in ordnung:
                if (_uses(teile[i]) & alle_decl) - bekannt - _decl(teile[i]):
                    ok = False; break
                bekannt |= _decl(teile[i])
            if not ok: continue
            code = "\n".join(teile[i] for i in ordnung)
            cls = "%s_%d" % (praefix, n); n += 1
            run = "        try {\n%s\n            K.out(\"%s.%s\", \"OK\");\n        } catch (Throwable e) { K.out(\"%s.%s\", \"FAIL \" + e); }" % (
                test, key, cls, key, cls)
            java.add(cls, code, run)
            self.kand.append((cls, ordnung))

    def gueltig(self, J):
        return [o for cls, o in self.kand if J.get(self.key + "." + cls) == "OK"]

def str_loesungen(aufgaben):
    """gaps-Loesungen immer als String-Listen"""
    for a in aufgaben:
        its, los = a["interaktion"], a["loesung"]
        if not isinstance(its, list): its, los = [its], [los]
        for it, lo in zip(its, los):
            if it["kind"] == "gaps":
                for k in lo: lo[k] = [str(v) for v in lo[k]]
