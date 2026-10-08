# Hilfsfunktionen fuer den Aufbau von welt0.json und die Java-Pruefung
import os, re, subprocess, shutil, json

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "java")

TASKS = {}      # id -> aufgabe (dict)
ORDER = []      # Reihenfolge der ids
CHECKS = []     # (id, fn)
PUNKTE = {1: 10, 2: 20, 3: 30}

# ---------------------------------------------------------------- Bloecke
def txt(md): return {"t": "text", "md": md}
def hin(md): return {"t": "hinweis", "md": md}
def code(c, nummern=True, markiere=None):
    b = {"t": "code", "code": c.strip("\n"), "nummern": nummern}
    if markiere: b["markiere"] = markiere
    return b
def sg(kopf, rumpf): return {"t": "struktogramm", "kopf": kopf, "rumpf": rumpf}
def tab(kopf, zeilen): return {"t": "tabelle", "kopf": kopf, "zeilen": zeilen}
def rei(werte, indizes=True, markiert=None):
    b = {"t": "reihung", "werte": werte, "indizes": indizes}
    if markiert: b["markiert"] = markiert
    return b

# Struktogramm-Knoten
def A(s): return {"anw": s}
def W(b, dann, sonst=None): return {"wenn": b, "dann": dann, "sonst": sonst or []}
def SOL(b, rumpf): return {"solange": b, "rumpf": rumpf}
def Z(b, rumpf): return {"zaehle": b, "rumpf": rumpf}
def G(s): return {"gib": s}
def AUF(s): return {"aufruf": s}

# Felder
def fz(): return {"typ": "zahl"}
def ft(breite=None, norm=None):
    f = {"typ": "text"}
    if breite: f["breite"] = breite
    if norm: f["norm"] = norm
    return f
def fa(opts): return {"typ": "auswahl", "optionen": list(opts)}
WF = ["true", "false"]
WFS = ["w", "f"]
TYPEN = ["int", "double", "boolean", "char", "String"]

def gaps(felder): return {"kind": "gaps", "felder": felder}
def choice(optionen, mehrfach=False):
    return {"kind": "choice", "optionen": [{"id": k, "md": v} for k, v in optionen], "mehrfach": mehrfach}
def order(teile):
    return {"kind": "order", "teile": [{"id": k, "code": v} for k, v in teile]}
def lines(block, anzahl): return {"kind": "lines", "block": block, "anzahl": anzahl}
def match(elemente, kategorien):
    return {"kind": "match", "elemente": [{"id": k, "md": v} for k, v in elemente],
            "kategorien": [{"id": k, "md": v} for k, v in kategorien]}
def arr(start, modus, fertigKnopf=None):
    d = {"kind": "array", "start": start, "modus": modus}
    if fertigKnopf is not None: d["fertigKnopf"] = fertigKnopf
    return d

def T(id, titel, stufe, kategorie, fallen, inhalt, interaktion, loesung, erklaerung, tipps=None, check=None):
    assert id not in TASKS, id
    a = {"id": id, "titel": titel, "stufe": stufe, "punkte": PUNKTE[stufe], "kategorie": kategorie,
         "fallen": fallen, "inhalt": inhalt, "interaktion": interaktion, "loesung": loesung,
         "tipps": tipps or [], "erklaerung": erklaerung}
    TASKS[id] = a
    ORDER.append(id)
    if check: CHECKS.append((id, check))
    return a

# ---------------------------------------------------------------- Vergleich (wie Server §5)
def norm_text(s, norm):
    if norm == "exakt": return s
    if norm == "text": return re.sub(r"\s+", " ", s.strip()).lower()
    return re.sub(r"\s+", "", s)  # code

def accepts(feld, answers, value):
    value = str(value)
    if feld["typ"] == "zahl":
        try: v = float(value.replace(",", "."))
        except ValueError: return False
        return any(abs(float(str(a).replace(",", ".")) - v) <= 1e-9 for a in answers)
    if feld["typ"] == "auswahl":
        return value in answers
    n = feld.get("norm", "code")
    return norm_text(value, n) in [norm_text(a, n) for a in answers]

def part(task, i=None):
    """liefert (interaktion, loesung) fuer Teil i (oder einzige)"""
    inter, loes = task["interaktion"], task["loesung"]
    if isinstance(inter, list): return inter[i], loes[i]
    return inter, loes

def expect(task, gid, value, i=None):
    inter, loes = part(task, i)
    f = inter["felder"][gid]
    if not accepts(f, loes[gid], value):
        raise AssertionError(f"{task['id']} Feld {gid}: Java liefert {value!r}, Loesung {loes[gid]!r}")

# ---------------------------------------------------------------- Java
HEAD = """
    static void println(Object o) { System.out.println(o); }
    static void println() { System.out.println(); }
    static void print(Object o) { System.out.print(o); }
    static String typ(int x) { return "int"; }
    static String typ(double x) { return "double"; }
    static String typ(boolean x) { return "boolean"; }
    static String typ(char x) { return "char"; }
    static String typ(String x) { return "String"; }
    static String arr(int[] r) { StringBuilder b = new StringBuilder(); for (int i = 0; i < r.length; i++) { if (i > 0) b.append(","); b.append(r[i]); } return b.toString(); }
    static void out(String k, Object v) { System.out.println(k + "=" + v); }
"""
_cnt = [0]

def _src(cls, methods, main, extra=""):
    return f"public class {cls} {{\n{HEAD}\n{methods}\n    public static void main(String[] args) throws Exception {{\n{main}\n    }}\n}}\n{extra}\n"

def jrun(methods, main, extra=""):
    """kompiliert und startet; liefert dict key->value aus Zeilen key=value und Liste aller Zeilen"""
    _cnt[0] += 1
    cls = f"Chk{_cnt[0]}"
    d = os.path.join(JDIR, cls); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, cls + ".java")
    open(p, "w").write(_src(cls, methods, main, extra))
    r = subprocess.run(["javac", "-encoding", "UTF-8", "-d", d, p], capture_output=True, text=True)
    if r.returncode != 0:
        raise AssertionError("javac-Fehler:\n" + r.stderr + "\n" + open(p).read())
    r = subprocess.run(["java", "-cp", d, cls], capture_output=True, text=True, timeout=20)
    if r.returncode != 0:
        raise AssertionError("Laufzeitfehler:\n" + r.stderr)
    out = {}
    lines_ = r.stdout.splitlines()
    for ln in lines_:
        if "=" in ln:
            k, v = ln.split("=", 1); out[k] = v
    return out, lines_

def jcompile(methods, main="", extra=""):
    """nur kompilieren; liefert (ok, stderr)"""
    _cnt[0] += 1
    cls = f"Cmp{_cnt[0]}"
    d = os.path.join(JDIR, cls); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, cls + ".java")
    open(p, "w").write(_src(cls, methods, main, extra))
    r = subprocess.run(["javac", "-encoding", "UTF-8", "-d", d, p], capture_output=True, text=True)
    return r.returncode == 0, r.stderr

def reset_java():
    shutil.rmtree(JDIR, ignore_errors=True); os.makedirs(JDIR)

def assemble_order(task, seq):
    teile = {t["id"]: t["code"] for t in task["interaktion"]["teile"]} if not isinstance(task["interaktion"], list) \
        else {t["id"]: t["code"] for p in task["interaktion"] if p["kind"] == "order" for t in p["teile"]}
    return "\n".join(teile[s] for s in seq)

def fill(src, mapping):
    for k, v in mapping.items():
        src = src.replace(f"[[{k}]]", v)
    assert "[[" not in src, src
    return src
