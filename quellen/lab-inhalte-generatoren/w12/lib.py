"""Hilfsfunktionen fuer die Welt-1/2-Inhalte von Algo Quest Lab (Bloecke, Aufgaben, Java-Pruefung)."""
import os, subprocess, shutil, re, json, itertools

W = os.path.dirname(os.path.abspath(__file__))
SNIP = os.path.join(W, 'snip')
BASE = {1: os.path.join(W, 'base1', 'bin'), 2: os.path.join(W, 'base2', 'bin')}
LOG = []          # Pruefprotokoll (Text)
_counter = [0]


def log(msg):
    LOG.append(msg)


# ------------------------------------------------------------------ Bloecke
def text(md):
    return {"t": "text", "md": md}


def hinweis(md):
    return {"t": "hinweis", "md": md}


def code(src, nummern=True, markiere=None):
    b = {"t": "code", "code": src.strip('\n'), "nummern": nummern}
    if markiere:
        b["markiere"] = markiere
    return b


def tabelle(kopf, zeilen):
    return {"t": "tabelle", "kopf": kopf, "zeilen": [[str(c) for c in z] for z in zeilen]}


def reihung(werte, indizes=True, markiert=None):
    b = {"t": "reihung", "werte": werte, "indizes": indizes}
    if markiert:
        b["markiert"] = markiert
    return b


def klassenkarte(name, attribute, methoden):
    return {"t": "klassenkarte", "name": name, "attribute": attribute, "methoden": methoden}


def struktogramm(kopf, rumpf):
    return {"t": "struktogramm", "kopf": kopf, "rumpf": rumpf}


# ------------------------------------------------------------------ Interaktionen
def gaps(**felder):
    return {"kind": "gaps", "felder": felder}


def zahl(breite=None):
    f = {"typ": "zahl"}
    if breite:
        f["breite"] = breite
    return f


def auswahl(optionen):
    return {"typ": "auswahl", "optionen": list(optionen)}


def txt(norm="code", breite=None):
    f = {"typ": "text", "norm": norm}
    if breite:
        f["breite"] = breite
    return f


def choice(optionen, mehrfach=False):
    return {"kind": "choice", "mehrfach": mehrfach,
            "optionen": [{"id": k, "md": v} for k, v in optionen]}


def order(teile):
    return {"kind": "order", "teile": [{"id": k, "code": v} for k, v in teile]}


def lines(block, anzahl):
    return {"kind": "lines", "block": block, "anzahl": anzahl}


def match(elemente, kategorien):
    return {"kind": "match", "elemente": [{"id": k, "md": v} for k, v in elemente],
            "kategorien": [{"id": k, "md": v} for k, v in kategorien]}


def array_tausch(start, fertig=True):
    i = {"kind": "array", "modus": "tausch", "start": list(start)}
    if fertig:
        i["fertigKnopf"] = True
    return i


def array_klick(start):
    return {"kind": "array", "modus": "klick", "start": list(start)}


PUNKTE = {1: 10, 2: 20, 3: 30}


def aufgabe(id, titel, stufe, kategorie, fallen, inhalt, interaktion, loesung, tipps, erklaerung):
    if isinstance(erklaerung, str):
        erklaerung = [text(erklaerung)]
    return {"id": id, "titel": titel, "stufe": stufe, "punkte": PUNKTE[stufe], "kategorie": kategorie,
            "fallen": fallen, "inhalt": inhalt, "interaktion": interaktion, "loesung": loesung,
            "tipps": tipps, "erklaerung": erklaerung}


# ------------------------------------------------------------------ Java
def _javac(srcdir, outdir, cp):
    files = [os.path.join(srcdir, f) for f in os.listdir(srcdir) if f.endswith('.java')]
    r = subprocess.run(['javac', '-Xlint:none', '-encoding', 'UTF-8', '-cp', cp, '-d', outdir] + files,
                       capture_output=True, text=True)
    err = '\n'.join(l for l in r.stderr.splitlines() if 'JAVA_TOOL_OPTIONS' not in l)
    return r.returncode == 0, err


def java(welt, main_body, extra='', expect_ok=True, timeout=20):
    """Kompiliert ein Hauptprogramm (+ Zusatzklassen) gegen die LSG-Klassen der Welt und liefert stdout.
    Online-IDE-Stil: println(...) ohne System.out (statischer Import aus aq.H)."""
    _counter[0] += 1
    name = f'Snip{_counter[0]}'
    d = os.path.join(SNIP, name)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(os.path.join(d, 'src'))
    os.makedirs(os.path.join(d, 'bin'))
    src = ('package aq;\nimport static aq.H.*;\n' + extra + '\n'
           f'public class {name} {{\n  public static void main(String[] args) throws Exception {{\n'
           + main_body + '\n  }\n}\n')
    open(os.path.join(d, 'src', name + '.java'), 'w', encoding='utf-8').write(src)
    ok, err = _javac(os.path.join(d, 'src'), os.path.join(d, 'bin'), BASE[welt])
    if not ok:
        if expect_ok:
            raise RuntimeError(f'Kompilierfehler in {name}:\n{err}\n---\n{src}')
        return None, err
    r = subprocess.run(['java', '-cp', BASE[welt] + ':' + os.path.join(d, 'bin'), 'aq.' + name],
                       capture_output=True, text=True, timeout=timeout)
    out = r.stdout
    errout = '\n'.join(l for l in r.stderr.splitlines() if 'JAVA_TOOL_OPTIONS' not in l)
    return out, errout


def run(welt, main_body, extra=''):
    out, err = java(welt, main_body, extra)
    if err.strip():
        raise RuntimeError('Laufzeitfehler: ' + err + '\n' + main_body)
    return out.rstrip('\n').split('\n') if out.strip() else []


def compiles(welt, main_body, extra=''):
    out, err = java(welt, main_body, extra, expect_ok=False)
    return out is not None


def ide_to_java(code):
    """Online-IDE-Hauptprogramm-Code ist bereits gueltiger Methodenrumpf (println via H)."""
    return code


def check(cond, msg):
    if not cond:
        raise AssertionError('PRUEFUNG FEHLGESCHLAGEN: ' + msg)
    log('OK  ' + msg)


def strip_lnum(c):
    return c


def compile_standalone(sources):
    """sources: {Dateiname: Quelltext} ohne package -> (ok, fehlertext)."""
    _counter[0] += 1
    d = os.path.join(SNIP, f'SA{_counter[0]}')
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(os.path.join(d, 'src')); os.makedirs(os.path.join(d, 'bin'))
    for n, s in sources.items():
        open(os.path.join(d, 'src', n), 'w', encoding='utf-8').write(s)
    return _javac(os.path.join(d, 'src'), os.path.join(d, 'bin'), '.')


def varianten(*xs):
    """Akzeptierte Code-Antworten: jeweils mit und ohne abschliessendes ';' bzw. ' {'."""
    out = []
    for x in xs:
        for v in (x, x.rstrip(';'), x.rstrip('{').rstrip(), x + ';' if not x.endswith((';', '{')) else x):
            if v not in out:
                out.append(v)
    return out


def norm_code(s):
    return re.sub(r'\s+', '', s)


def zahlvarianten(s):
    out = [s]
    if '.' in s:
        out.append(s.replace('.', ','))
    return out


def kopf(*xs):
    """Methodenkoepfe: ohne und mit oeffnender Klammer."""
    out = []
    for x in xs:
        out += [x, x + ' {']
    return out


TYPEN = ["Ganzzahl", "Kommazahl", "Wahrheitswert", "Zeichen", "Zeichenkette", "nichts"]
WF = ["true", "false"]
JA_NEIN = ["ja", "nein"]
