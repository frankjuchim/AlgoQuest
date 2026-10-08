# Gemeinsame Hilfen fuer den Bau von welt3.json / welt4.json (Algo Quest Lab)
# - Java-Snippets werden WOERTLICH so kompiliert, wie sie in den Aufgaben stehen
#   (javac 21 + NI-Stub), Werte kommen aus der Ausfuehrung.
import json, os, re, subprocess, shutil

SCRATCH = "/tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad"
W = SCRATCH + "/algolab/w34"
NI = SCRATCH + "/w4_code/harness/NI.java"

LOG_JAVA = r'''
class Log {
    static java.util.List<String[]> rows = new java.util.ArrayList<>();
    static int tiefe = 0;
    static int enter(String call) { rows.add(new String[]{"" + tiefe, call, "?"}); tiefe++; return rows.size() - 1; }
    static void leave(int idx, Object ret) { tiefe--; rows.get(idx)[2] = String.valueOf(ret); }
    static void dump(String key) {
        for (int i = 0; i < rows.size(); i++) {
            String[] r = rows.get(i);
            System.out.println(key + "#" + i + "=" + r[0] + "|" + r[1] + "|" + r[2]);
        }
        System.out.println(key + "#n=" + rows.size());
        rows.clear(); tiefe = 0;
    }
    static void reset() { rows.clear(); tiefe = 0; }
}
'''

HELP_JAVA = r'''
    static void println(Object o) { System.out.println(o); }
    static void print(Object o) { System.out.print(o); }
    static void out(String k, Object v) { System.out.println(k + "=" + v); }
    static String capture(Runnable r) { java.io.PrintStream alt = System.out; java.io.ByteArrayOutputStream b = new java.io.ByteArrayOutputStream(); System.setOut(new java.io.PrintStream(b)); try { r.run(); } finally { System.setOut(alt); } return b.toString(); }
    static String arr(int[] r) { StringBuilder b = new StringBuilder(); for (int i = 0; i < r.length; i++) { if (i > 0) b.append(", "); b.append(r[i]); } return b.toString(); }
'''

NI_HELP_JAVA = r'''
    static String nm(Object o) { if (o instanceof Kiste) return ((Kiste) o).getName() + " " + ((Kiste) o).getGewicht(); return String.valueOf(o); }
    // Stapel von UNTEN nach OBEN, danach unveraendert
    static String st(Stack s) { java.util.ArrayList<Object> l = new java.util.ArrayList<>(); while (!s.isEmpty()) l.add(s.pop());
        StringBuilder b = new StringBuilder(); for (int i = l.size() - 1; i >= 0; i--) { s.push(l.get(i)); if (b.length() > 0) b.append(", "); b.append(nm(l.get(i))); }
        return b.length() == 0 ? "-" : b.toString(); }
    static String qu(Queue q) { java.util.ArrayList<Object> l = new java.util.ArrayList<>(); while (!q.isEmpty()) l.add(q.dequeue());
        StringBuilder b = new StringBuilder(); for (Object o : l) { q.enqueue(o); if (b.length() > 0) b.append(", "); b.append(nm(o)); }
        return b.length() == 0 ? "-" : b.toString(); }
    static String da(DynArray d) { StringBuilder b = new StringBuilder(); for (int i = 0; i < d.getLength(); i++) { if (i > 0) b.append(", "); b.append(nm(d.getItem(i))); }
        return b.length() == 0 ? "-" : b.toString(); }
    static String ex(Throwable t) { return t.getClass().getSimpleName(); }
'''

KISTE_JAVA = r'''
class Kiste {
    private String name;
    private int gewicht;
    public Kiste(String name, int gewicht) { this.name = name; this.gewicht = gewicht; }
    public String getName() { return name; }
    public int getGewicht() { return gewicht; }
    public String beschreibung() { return name + " (" + gewicht + " kg)"; }
}
'''


class JavaProg:
    """Sammelt Snippets: jedes Snippet = woertlicher Aufgabencode in eigener
    statischer Klasse T_<key>; optional instrumentiert (Methode umbenannt,
    Wrapper protokolliert Rekursionstiefe/Aufruf/Rueckgabe)."""

    def __init__(self, name, ni=False):
        self.name = name; self.ni = ni
        self.parts = []; self.probes = []; self.shown = {}

    def add(self, key, code, probe, wrap=None, extra=""):
        self.shown[key] = code
        body = code
        if wrap:
            for meth, wcode in wrap:
                pat = re.compile(r'([\w\[\]]+\s+)' + meth + r'\(')
                body, n = pat.subn(r'\g<1>' + meth + '__(', body, count=1)
                assert n == 1, (key, meth)
                body += "\n" + wcode
        self.parts.append("static class T_%s {\nstatic final String K = \"%s.\";\n%s\n%s\nstatic void probe() throws Exception {\n%s\n}\n}\n" % (key, key, body, extra, probe))
        self.probes.append("try { T_%s.probe(); } catch (Throwable t) { out(\"%s.FEHLER\", ex(t)); }" % (key, key))

    def source(self):
        s = "package aq;\n" + LOG_JAVA + (KISTE_JAVA if self.ni else "")
        s += "public class %s {\n%s%s\n" % (self.name, HELP_JAVA, NI_HELP_JAVA if self.ni else
                                           "    static String ex(Throwable t) { return t.getClass().getSimpleName(); }\n")
        s += "\n".join(self.parts)
        s += "\npublic static void main(String[] a) {\n" + "\n".join(self.probes) + "\n}\n}\n"
        return s

    def run(self):
        d = W + "/java_" + self.name
        shutil.rmtree(d, ignore_errors=True); os.makedirs(d + "/src/aq"); os.makedirs(d + "/bin")
        open(d + "/src/aq/%s.java" % self.name, "w").write(self.source())
        if self.ni:
            shutil.copy(NI, d + "/src/aq/NI.java")
        r = subprocess.run("javac -Xlint:none -encoding UTF-8 -d %s/bin %s/src/aq/*.java" % (d, d), shell=True,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr); raise SystemExit("KOMPILIERFEHLER " + self.name)
        r = subprocess.run("java -Xss2m -Dstdout.encoding=UTF-8 -Dfile.encoding=UTF-8 -cp %s/bin aq.%s" % (d, self.name), shell=True, capture_output=True, text=True,
                           timeout=120)
        out = r.stdout
        open(d + "/ausgabe.txt", "w").write(out)
        V = {}
        for line in out.splitlines():
            if "=" in line:
                k, v = line.split("=", 1); V[k] = v
        return V


def compile_fail(name, code, expect):
    """Prueft, dass ein Snippet NICHT kompiliert und die Meldung expect enthaelt."""
    d = W + "/javafail_" + name
    shutil.rmtree(d, ignore_errors=True); os.makedirs(d + "/src/aq"); os.makedirs(d + "/bin")
    code = code.strip("\n")
    vor = "package aq;\n" + KISTE_JAVA + "class X {\n"
    src = vor + code + "\n}\n"
    open(d + "/src/aq/X.java", "w").write(src)
    shutil.copy(NI, d + "/src/aq/NI.java")
    r = subprocess.run("javac -Xlint:none -encoding UTF-8 -d %s/bin %s/src/aq/*.java" % (d, d), shell=True,
                       capture_output=True, text=True)
    assert r.returncode != 0, "kompiliert unerwartet: " + name
    assert expect in r.stderr, (name, r.stderr)
    m = re.search(r'X\.java:(\d+): error', r.stderr)
    return int(m.group(1)) - vor.count("\n")  # Zeile im Snippet (1-basiert)


def rows(V, key):
    n = int(V[key + "#n"])
    out = []
    for i in range(n):
        t, c, r = V["%s#%d" % (key, i)].split("|", 2)
        out.append((int(t), c, r))
    return out


# ---------------- Bausteine ----------------
def text(md): return {"t": "text", "md": md}
def hinweis(md): return {"t": "hinweis", "md": md}
def code(c, nummern=True, markiere=None):
    b = {"t": "code", "code": c.strip("\n"), "nummern": nummern}
    if markiere: b["markiere"] = markiere
    return b
def tabelle(kopf, zeilen): return {"t": "tabelle", "kopf": kopf, "zeilen": zeilen}
def raster(z): return {"t": "raster", "zeilen": z}
def reihung(w, markiert=None):
    b = {"t": "reihung", "werte": w, "indizes": True}
    if markiert: b["markiert"] = markiert
    return b
def adt(art, inhalt): return {"t": "adt", "art": art, "inhalt": inhalt}
def baum(b): return {"t": "baum", "baum": b}
def struk(kopf, rumpf): return {"t": "struktogramm", "kopf": kopf, "rumpf": rumpf}
def klassenkarte(name, attr, meth): return {"t": "klassenkarte", "name": name, "attribute": attr, "methoden": meth}

def zahl(): return {"typ": "zahl"}
def txt(norm="code", breite=None):
    f = {"typ": "text", "norm": norm}
    if breite: f["breite"] = breite
    return f
def auswahl(opt): return {"typ": "auswahl", "optionen": opt}

def gaps(felder): return {"kind": "gaps", "felder": felder}
def choice(opts, mehrfach=False): return {"kind": "choice", "optionen": [{"id": i, "md": m} for i, m in opts], "mehrfach": mehrfach}
def order(teile): return {"kind": "order", "teile": teile}
def lines(block, anzahl): return {"kind": "lines", "block": block, "anzahl": anzahl}
def match(el, kat): return {"kind": "match", "elemente": [{"id": i, "md": m} for i, m in el], "kategorien": [{"id": i, "md": m} for i, m in kat]}
def grid(r): return {"kind": "grid", "raster": r}
def adtsim(art, start): return {"kind": "adtsim", "art": art, "start": start}

PUNKTE = {1: 10, 2: 20, 3: 30}

def aufgabe(id, titel, stufe, kategorie, fallen, inhalt, interaktion, loesung, tipps, erklaerung):
    return {"id": id, "titel": titel, "stufe": stufe, "punkte": PUNKTE[stufe], "kategorie": kategorie,
            "fallen": fallen, "inhalt": inhalt, "interaktion": interaktion, "loesung": loesung,
            "tipps": tipps, "erklaerung": erklaerung if isinstance(erklaerung, list) else [text(erklaerung)]}

def strvar(s):
    """akzeptierte Schreibweisen fuer eine Zeichenkette (mit/ohne Anfuehrungszeichen)"""
    return [s, '"' + s + '"']

LEER = ["–", "-", "leer", "—"]

def liste(items):
    return ", ".join(str(x) for x in items) if items else "–"

def listvar(items, klammern=True):
    """akzeptierte Varianten einer Liste: mit Komma (Leerzeichen egal bei norm code), leer -> LEER"""
    if not items:
        return LEER
    a = ", ".join(str(x) for x in items)
    v = [a]
    if len(items) > 1: v.append("; ".join(str(x) for x in items))
    if klammern: v.append("{" + a + "}")
    return v
