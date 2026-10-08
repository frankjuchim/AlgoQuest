# Eigenvalidierung welt<N>.json gegen SPEC_AlgoLab §3–§5 (+ §10 Inhaltsanforderungen)
import json, re, sys
from collections import Counter

LAB_KATEGORIEN = ["Datentypen und Ausdrücke", "Methodenkopf und Signatur", "Klasse vs. Objekt", "Bestandteile einer Klasse",
                  "Objektkarten und Referenzen", "Klassendiagramm", "Struktogramm lesen", "Code ↔ Struktogramm", "Tracetabelle",
                  "Rekursionstabelle", "Fehler im Java-Code", "Fehler im Struktogramm", "Lückencode", "Methode implementieren",
                  "ADT-Befehlsfolgen", "Sortieren und Suchen", "Effizienz", "Bäume", "Funktionsweise erläutern"]
FALLEN = {"P%d" % i for i in range(1, 11)}
BLOCK_T = {"text", "code", "struktogramm", "tabelle", "baum", "reihung", "raster", "klassenkarte", "adt", "hinweis"}
KINDS = {"gaps", "choice", "order", "lines", "match", "tree", "array", "grid", "adtsim"}
GAP = re.compile(r"\[\[([A-Za-z0-9_]+)\]\]")

err = []
def E(where, msg): err.append("%s: %s" % (where, msg))

def parse_baum(s):
    s = s.replace(" ", "")
    pos = 0
    def node():
        nonlocal pos
        if pos < len(s) and s[pos] == "-":
            pos += 1; return None
        m = re.match(r"[^(),]+", s[pos:])
        if not m: raise ValueError("Wert erwartet bei %d" % pos)
        val = m.group(0); pos += len(val)
        l = r = None
        if pos < len(s) and s[pos] == "(":
            pos += 1; l = node()
            if s[pos] != ",": raise ValueError("Komma erwartet")
            pos += 1; r = node()
            if s[pos] != ")": raise ValueError(") erwartet")
            pos += 1
        return (val, l, r)
    t = node()
    if pos != len(s): raise ValueError("Rest: " + s[pos:])
    return t

def pfade(t, p=""):
    if t is None: return set()
    return {p} | pfade(t[1], p + "L") | pfade(t[2], p + "R")

def strukt_texts(nodes, where):
    out = []
    for n in nodes:
        if not isinstance(n, dict) or len(set(n) & {"anw", "wenn", "solange", "zaehle", "wiederhole", "gib", "aufruf"}) != 1:
            E(where, "ungültiger Struktogramm-Knoten %r" % n); continue
        if "anw" in n: out.append(n["anw"])
        if "gib" in n: out.append(n["gib"])
        if "aufruf" in n: out.append(n["aufruf"])
        if "wenn" in n:
            out.append(n["wenn"]); out += strukt_texts(n.get("dann", []), where); out += strukt_texts(n.get("sonst", []), where)
            if "dann" not in n or "sonst" not in n: E(where, "wenn ohne dann/sonst")
        if "solange" in n: out.append(n["solange"]); out += strukt_texts(n["rumpf"], where)
        if "zaehle" in n: out.append(n["zaehle"]); out += strukt_texts(n["rumpf"], where)
        if "wiederhole" in n: out += strukt_texts(n["wiederhole"], where); out.append(n["bis"])
    return out

def block_texts(b, where):
    t = b.get("t")
    if t not in BLOCK_T: E(where, "unbekannter Block %r" % t); return []
    if t in ("text", "hinweis"): return [b["md"]]
    if t == "code":
        if not isinstance(b.get("code"), str) or not b["code"].strip(): E(where, "leerer Code")
        if "markiere" in b:
            n = b["code"].count("\n") + 1
            if any(not (1 <= x <= n) for x in b["markiere"]): E(where, "markiere außerhalb")
        return [b["code"]]
    if t == "struktogramm": return [b["kopf"]] + strukt_texts(b["rumpf"], where)
    if t == "tabelle":
        k = len(b["kopf"])
        for z in b["zeilen"]:
            if len(z) != k: E(where, "Tabellenzeile mit %d statt %d Zellen" % (len(z), k))
        return list(b["kopf"]) + [str(c) for z in b["zeilen"] for c in z]
    if t == "baum":
        try: parse_baum(b["baum"])
        except Exception as ex: E(where, "Baum nicht parsebar: %s" % ex)
        return []
    if t == "reihung":
        if not isinstance(b["werte"], list): E(where, "reihung.werte keine Liste")
        return []
    if t == "raster":
        z = b["zeilen"]
        if not z or len({len(r) for r in z}) != 1: E(where, "raster nicht rechteckig")
        return []
    if t == "klassenkarte": return [b["name"]] + b.get("attribute", []) + b.get("methoden", [])
    if t == "adt":
        if b["art"] not in ("stapel", "schlange", "dynarray"): E(where, "adt.art ungültig")
        return []
    return []

def norm(s, how):
    if how == "code": return re.sub(r"\s+", "", s)
    if how == "text": return re.sub(r"\s+", " ", s.strip()).lower()
    return s

def pruefe_teil(ia, lo, inhalt, where, gaps_ids):
    k = ia.get("kind")
    if k not in KINDS: E(where, "unbekannte Interaktion %r" % k); return k
    if k == "gaps":
        felder = ia["felder"]
        if set(felder) != set(lo): E(where, "felder %s ≠ loesung %s" % (sorted(felder), sorted(lo)))
        for fid, f in felder.items():
            if fid not in gaps_ids: E(where, "Feld %s ohne [[%s]] im Inhalt" % (fid, fid))
            typ = f.get("typ")
            if typ not in ("text", "zahl", "auswahl"): E(where, "Feld %s: typ %r" % (fid, typ))
            ans = lo.get(fid)
            if not isinstance(ans, list) or not ans or not all(isinstance(a, str) for a in ans): E(where, "Lösung %s keine nichtleere String-Liste" % fid); continue
            if typ == "zahl":
                for a in ans:
                    try: float(a.replace(",", "."))
                    except ValueError: E(where, "Feld %s: Lösung %r nicht numerisch" % (fid, a))
            if typ == "auswahl":
                if not f.get("optionen"): E(where, "Feld %s ohne optionen" % fid)
                for a in ans:
                    if a not in f.get("optionen", []): E(where, "Feld %s: Lösung %r nicht in optionen" % (fid, a))
            if typ == "text" and f.get("norm", "code") not in ("code", "text", "exakt"): E(where, "Feld %s: norm ungültig" % fid)
            if typ == "text":
                nn = [norm(a, f.get("norm", "code")) for a in ans]
                if any(x == "" for x in nn): E(where, "Feld %s: leere Lösung" % fid)
    elif k == "choice":
        ids = [o["id"] for o in ia["optionen"]]
        if len(ids) != len(set(ids)): E(where, "doppelte choice-ids")
        r = lo.get("richtig", [])
        if not r: E(where, "choice ohne richtige Antwort")
        if any(x not in ids for x in r): E(where, "choice: unbekannte id in richtig")
        if not ia.get("mehrfach") and len(r) != 1: E(where, "Einfachauswahl mit %d richtigen" % len(r))
        if len(ids) < 3: E(where, "choice mit < 3 Optionen")
    elif k == "order":
        ids = [t["id"] for t in ia["teile"]]
        if len(ids) != len(set(ids)): E(where, "doppelte order-ids")
        for t in ia["teile"]:
            if not (("code" in t) ^ ("md" in t)): E(where, "order-Teil braucht code ODER md")
        rf = lo.get("reihenfolgen", [])
        if not rf: E(where, "order ohne reihenfolgen")
        for r in rf:
            if any(x not in ids for x in r): E(where, "order: unbekannte id")
            if len(r) != len(set(r)): E(where, "order: id doppelt in Reihenfolge")
        texts = [t.get("code", t.get("md")) for t in ia["teile"]]
        if len(texts) != len(set(texts)): E(where, "order: identische Teile (mehrdeutig)")
    elif k == "lines":
        b = ia["block"]
        if not (0 <= b < len(inhalt)) or inhalt[b]["t"] != "code": E(where, "lines.block zeigt nicht auf Code-Block"); return k
        n = inhalt[b]["code"].count("\n") + 1
        z = lo.get("zeilen", [])
        if len(z) != ia["anzahl"]: E(where, "lines.anzahl %d ≠ %d Lösungszeilen" % (ia["anzahl"], len(z)))
        if any(not (1 <= x <= n) for x in z): E(where, "lines: Zeile außerhalb 1..%d" % n)
    elif k == "match":
        el = [e["id"] for e in ia["elemente"]]; ka = [c["id"] for c in ia["kategorien"]]
        if set(lo) != set(el): E(where, "match: Lösung deckt Elemente nicht ab")
        if any(c not in ka for c in lo.values()): E(where, "match: unbekannte Kategorie")
    elif k == "tree":
        if ia["modus"] == "klick":
            try: t = parse_baum(ia["baum"])
            except Exception as ex: E(where, "tree.baum: %s" % ex); return k
            P = pfade(t)
            if any(p not in P for p in lo["folge"]): E(where, "tree: Pfad existiert nicht")
        elif ia["modus"] == "bauen":
            try: parse_baum(ia["start"]); parse_baum(lo["baum"])
            except Exception as ex: E(where, "tree bauen: %s" % ex)
        else: E(where, "tree.modus ungültig")
    elif k == "array":
        n = len(ia["start"])
        if ia["modus"] == "tausch":
            for p in lo["tausche"]:
                if len(p) != 2 or p[0] == p[1] or any(not (0 <= x < n) for x in p): E(where, "array-tausch: ungültiges Paar %r" % p)
            if not lo["tausche"]: E(where, "array-tausch ohne Tausch")
        elif ia["modus"] == "klick":
            if any(not (0 <= x < n) for x in lo["folge"]): E(where, "array-klick: Index außerhalb")
        else: E(where, "array.modus ungültig")
    elif k == "grid":
        R = ia["raster"]
        if not R or len({len(r) for r in R}) != 1: E(where, "grid.raster nicht rechteckig"); return k
        for c in lo["zellen"]:
            if not (0 <= c[0] < len(R) and 0 <= c[1] < len(R[0])): E(where, "grid: Zelle außerhalb %r" % c)
        if len({tuple(c) for c in lo["zellen"]}) != len(lo["zellen"]): E(where, "grid: Zelle doppelt")
        if "reihenfolge" not in lo: E(where, "grid: reihenfolge fehlt")
    elif k == "adtsim":
        if ia["art"] not in ("stapel", "schlange", "dynarray"): E(where, "adtsim.art ungültig")
        if not isinstance(lo.get("inhalt"), list) or not all(isinstance(x, str) for x in lo["inhalt"]): E(where, "adtsim: inhalt keine String-Liste")
        if not isinstance(ia.get("start"), list): E(where, "adtsim: start fehlt")
    return k

def pruefe(path, welt_nr):
    W = json.load(open(path))
    for key in ("version", "welt", "titel", "farbe", "levels", "boss", "aufgaben"):
        if key not in W: E(path, "Schlüssel %s fehlt" % key)
    if W["version"] != 2 or W["welt"] != welt_nr: E(path, "version/welt")
    auf = {}
    for a in W["aufgaben"]:
        if a["id"] in auf: E(a["id"], "doppelte id")
        auf[a["id"]] = a
    kinds = Counter(); used = Counter()
    lvl_ids = set()
    for L in W["levels"]:
        if not re.fullmatch(r"W%d-L\d+" % welt_nr, L["id"]): E(L["id"], "Level-id")
        for key in ("nr", "titel", "ds", "ab", "ide", "intro", "aufgaben"):
            if key not in L: E(L["id"], "fehlt %s" % key)
        for b in L["intro"]: block_texts(b, L["id"] + "/intro")
        n = len(L["aufgaben"])
        if not (6 <= n <= 8): E(L["id"], "%d Aufgaben (6–8 verlangt)" % n)
        st = Counter()
        for aid in L["aufgaben"]:
            if aid not in auf: E(L["id"], "Verweis auf fehlende Aufgabe %s" % aid); continue
            if not aid.startswith(L["id"] + "-"): E(aid, "id passt nicht zum Level")
            used[aid] += 1; lvl_ids.add(aid); st[auf[aid]["stufe"]] += 1
        if not (st[1] >= 2 and st[2] >= 2 and st[3] >= 1): E(L["id"], "Stufenmix %s" % dict(st))
    bo = W["boss"]
    for key in ("id", "titel", "dauerMin", "anzahl", "mix", "pool"):
        if key not in bo: E("boss", "fehlt %s" % key)
    if bo["id"] != "W%d-BOSS" % welt_nr: E("boss", "id")
    if not (20 <= bo["dauerMin"] <= 30): E("boss", "dauerMin")
    if bo["anzahl"] != 8 or bo["mix"] != {"1": 3, "2": 3, "3": 2}: E("boss", "anzahl/mix")
    if not (14 <= len(bo["pool"]) <= 16): E("boss", "Pool-Größe %d" % len(bo["pool"]))
    bst = Counter()
    for aid in bo["pool"]:
        if aid not in auf: E("boss", "fehlende Aufgabe %s" % aid); continue
        if not re.fullmatch(r"W%d-B-\d\d" % welt_nr, aid): E(aid, "Boss-id")
        if aid in lvl_ids: E(aid, "Boss-Aufgabe auch im Level")
        used[aid] += 1; bst[auf[aid]["stufe"]] += 1
    for s, n in bo["mix"].items():
        if bst[int(s)] < n: E("boss", "Mix nicht erfüllbar: Stufe %s nur %d" % (s, bst[int(s)]))
    for aid, a in auf.items():
        w = aid
        if used[aid] != 1: E(w, "wird %d-mal verwendet" % used[aid])
        if not re.fullmatch(r"W%d-(L\d+-\d\d|B-\d\d)" % welt_nr, aid): E(w, "id-Format")
        if a["stufe"] not in (1, 2, 3) or a["punkte"] != {1: 10, 2: 20, 3: 30}[a["stufe"]]: E(w, "stufe/punkte")
        if a["kategorie"] not in LAB_KATEGORIEN: E(w, "Kategorie %r" % a["kategorie"])
        if not set(a["fallen"]) <= FALLEN: E(w, "fallen")
        if not a.get("titel"): E(w, "titel")
        if not a.get("erklaerung"): E(w, "keine Erklärung")
        if not a.get("tipps"): E(w, "keine Tipps")
        texts = []
        for b in a["inhalt"]: texts += block_texts(b, w)
        for b in a["erklaerung"]:
            block_texts(b, w + "/erkl")
            for tt in [b.get("md", ""), b.get("code", "")]:
                if GAP.search(tt): E(w, "Lücke in Erklärung")
        gap_ids = []
        for tt in texts: gap_ids += GAP.findall(tt)
        if len(gap_ids) != len(set(gap_ids)): E(w, "Lücken-id doppelt im Inhalt")
        ia, lo = a["interaktion"], a["loesung"]
        if isinstance(ia, list):
            if not isinstance(lo, list) or len(lo) != len(ia): E(w, "Interaktions-Array ≠ Lösungs-Array"); continue
            parts = list(zip(ia, lo))
        else:
            if isinstance(lo, list): E(w, "Lösung Array bei Einzelinteraktion"); continue
            parts = [(ia, lo)]
        gap_felder = set()
        for i_, l_ in parts:
            k = pruefe_teil(i_, l_, a["inhalt"], w, set(gap_ids)); kinds[k if k != "array" else "array-" + i_["modus"]] += 1
            if k == "gaps": gap_felder |= set(i_["felder"])
        if set(gap_ids) != gap_felder: E(w, "Lücken im Inhalt %s ≠ felder %s" % (sorted(set(gap_ids) - gap_felder), sorted(gap_felder - set(gap_ids))))
        if sum(1 for i_, _ in parts if i_["kind"] == "gaps") > 1: E(w, "mehr als ein gaps-Teil")
    ka = {k.split("-")[0] for k in kinds}
    if len(ka) < 5: E(path, "nur %d Interaktionsarten" % len(ka))
    return W, kinds

if __name__ == "__main__":
    for path, n in [(p, int(re.search(r"welt(\d)", p).group(1))) for p in sys.argv[1:]]:
        err.clear()
        W, kinds = pruefe(path, n)
        st = Counter(a["stufe"] for a in W["aufgaben"])
        print("==", path, "|", len(W["aufgaben"]), "Aufgaben | Stufen", dict(sorted(st.items())), "| Interaktionen", dict(kinds))
        for L in W["levels"]:
            A = {a["id"]: a for a in W["aufgaben"]}
            s = Counter(A[i]["stufe"] for i in L["aufgaben"])
            ks = Counter()
            for i in L["aufgaben"]:
                ia = A[i]["interaktion"]
                for x in (ia if isinstance(ia, list) else [ia]): ks[x["kind"] + ("-" + x["modus"] if "modus" in x else "")] += 1
            print("  %s %s %-50s ds=%s n=%d S=%s %s" % (L["id"], L["nr"], L["titel"], L["ds"], len(L["aufgaben"]), dict(sorted(s.items())), dict(ks)))
        A = {a["id"]: a for a in W["aufgaben"]}
        print("  BOSS %s „%s“ pool=%d Stufen=%s" % (W["boss"]["id"], W["boss"]["titel"], len(W["boss"]["pool"]), dict(sorted(Counter(A[i]["stufe"] for i in W["boss"]["pool"]).items()))))
        print("  FEHLER:", len(err))
        for e in err: print("   -", e)
