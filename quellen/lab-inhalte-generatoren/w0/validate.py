#!/usr/bin/env python3
"""Eigen-Validator fuer welt<N>.json gegen SPEC_AlgoLab §3–§5 (unabhaengig vom Plattform-Validator).
Aufruf: python3 validate.py <welt.json>   -> Exitcode 0 = gruen"""
import json, re, sys
from collections import Counter

LAB_KATEGORIEN = ["Datentypen und Ausdrücke", "Methodenkopf und Signatur", "Klasse vs. Objekt", "Bestandteile einer Klasse",
                  "Objektkarten und Referenzen", "Klassendiagramm", "Struktogramm lesen", "Code ↔ Struktogramm", "Tracetabelle",
                  "Rekursionstabelle", "Fehler im Java-Code", "Fehler im Struktogramm", "Lückencode", "Methode implementieren",
                  "ADT-Befehlsfolgen", "Sortieren und Suchen", "Effizienz", "Bäume", "Funktionsweise erläutern"]
FALLEN = {f"P{i}" for i in range(1, 11)}
BLOCK = {"text", "code", "struktogramm", "tabelle", "baum", "reihung", "raster", "klassenkarte", "adt", "hinweis"}
KINDS = {"gaps", "choice", "order", "lines", "match", "tree", "array", "grid", "adtsim"}
GAP = re.compile(r"\[\[([A-Za-z0-9_-]{1,40})\]\]")
PUNKTE = {1: 10, 2: 20, 3: 30}
ERR, WARN = [], []

def err(where, msg): ERR.append(f"{where}: {msg}")
def warn(where, msg): WARN.append(f"{where}: {msg}")

def node_texts(nodes, out, where):
    if not isinstance(nodes, list): err(where, "Struktogramm-Rumpf ist keine Liste"); return
    for k in nodes:
        if not isinstance(k, dict): err(where, f"Knoten {k!r} kein Objekt"); continue
        keys = set(k)
        if keys == {"anw"} or keys == {"gib"} or keys == {"aufruf"}: out.append(next(iter(k.values())))
        elif keys <= {"wenn", "dann", "sonst"} and "wenn" in keys and "dann" in keys:
            out.append(k["wenn"]); node_texts(k["dann"], out, where); node_texts(k.get("sonst", []), out, where)
        elif keys == {"solange", "rumpf"} or keys == {"zaehle", "rumpf"}:
            out.append(k.get("solange", k.get("zaehle"))); node_texts(k["rumpf"], out, where)
        elif keys == {"wiederhole", "bis"}:
            out.append(k["bis"]); node_texts(k["wiederhole"], out, where)
        else: err(where, f"unbekannter Struktogramm-Knoten {sorted(keys)}")
        for v in k.values():
            if isinstance(v, str) and not v.strip() and v != "": err(where, "leerer Knotentext")

def block_texts(b, where):
    out = []
    if not isinstance(b, dict) or b.get("t") not in BLOCK: err(where, f"ungültiger Block {str(b)[:60]}"); return out
    t = b["t"]
    if t in ("text", "hinweis"):
        if not isinstance(b.get("md"), str) or not b["md"].strip(): err(where, f"{t}: md fehlt"); return out
        out.append(b["md"])
    elif t == "code":
        if not isinstance(b.get("code"), str) or not b["code"].strip(): err(where, "code fehlt"); return out
        out.append(b["code"])
        if "markiere" in b and not all(isinstance(x, int) and 1 <= x <= b["code"].count("\n") + 1 for x in b["markiere"]):
            err(where, "markiere außerhalb des Codes")
    elif t == "struktogramm":
        if not isinstance(b.get("kopf"), str) or not b["kopf"]: err(where, "Struktogramm ohne kopf")
        else: out.append(b["kopf"])
        node_texts(b.get("rumpf"), out, where)
    elif t == "tabelle":
        kopf, zeilen = b.get("kopf"), b.get("zeilen")
        if not isinstance(kopf, list) or not isinstance(zeilen, list) or not zeilen: err(where, "tabelle: kopf/zeilen fehlen"); return out
        out += [str(x) for x in kopf]
        for z in zeilen:
            if not isinstance(z, list) or len(z) != len(kopf): err(where, f"tabelle: Zeile mit {len(z) if isinstance(z, list) else '?'} statt {len(kopf)} Zellen")
            else: out += [str(x) for x in z]
    elif t == "reihung":
        if not isinstance(b.get("werte"), list): err(where, "reihung: werte fehlen")
        else: out += [str(x) for x in b["werte"]]
    else:
        warn(where, f"Blocktyp {t} nicht tief geprüft")
    return out

def check_answers_gaps(ia, lo, where):
    felder = ia.get("felder")
    if not isinstance(felder, dict) or not felder: err(where, "gaps ohne felder"); return set()
    if not isinstance(lo, dict): err(where, "gaps-Lösung kein Objekt"); return set(felder)
    if set(lo) != set(felder): err(where, f"Lösung/Felder verschieden: {set(lo) ^ set(felder)}")
    for gid, f in felder.items():
        typ = f.get("typ")
        if typ not in ("text", "zahl", "auswahl"): err(where, f"Feld {gid}: typ {typ}")
        ans = lo.get(gid)
        if not isinstance(ans, list) or not ans or not all(isinstance(a, str) and a.strip() for a in ans):
            err(where, f"Feld {gid}: Antwortliste leer/ungültig"); continue
        if typ == "zahl":
            for a in ans:
                try: float(a.replace(",", "."))
                except ValueError: err(where, f"Feld {gid}: '{a}' ist keine Zahl")
        if typ == "auswahl":
            opts = f.get("optionen")
            if not isinstance(opts, list) or len(opts) < 2 or len(set(opts)) != len(opts): err(where, f"Feld {gid}: optionen ungültig")
            elif not set(ans) <= set(opts): err(where, f"Feld {gid}: Antwort nicht in optionen")
        if typ == "text" and f.get("norm", "code") not in ("code", "text", "exakt"): err(where, f"Feld {gid}: norm")
        if typ == "text":
            n = f.get("norm", "code")
            norm = (lambda s: re.sub(r"\s+", "", s)) if n == "code" else (lambda s: re.sub(r"\s+", " ", s.strip()).lower()) if n == "text" else (lambda s: s)
            if len({norm(a) for a in ans}) != len(ans): warn(where, f"Feld {gid}: doppelte Antwortvarianten nach Normalisierung")
    return set(felder)

def check_part(ia, lo, inhalt, where):
    kind = ia.get("kind")
    if kind not in KINDS: err(where, f"kind {kind}"); return set()
    if kind == "gaps": return check_answers_gaps(ia, lo, where)
    if kind == "choice":
        ids = [o.get("id") for o in ia.get("optionen", [])]
        if len(ids) < 2 or len(set(ids)) != len(ids) or not all(o.get("md") for o in ia["optionen"]): err(where, "choice: optionen")
        r = lo.get("richtig") if isinstance(lo, dict) else None
        if not isinstance(r, list) or not r or not set(r) <= set(ids): err(where, "choice: richtig ungültig")
        elif not ia.get("mehrfach") and len(r) != 1: err(where, "choice: einfach, aber mehrere richtig")
        if ia.get("mehrfach") is None: err(where, "choice: mehrfach fehlt")
    elif kind == "order":
        teile = ia.get("teile", [])
        ids = [t.get("id") for t in teile]
        if len(set(ids)) != len(ids) or not all(("code" in t) ^ ("md" in t) for t in teile): err(where, "order: teile ungültig")
        txt = {t["id"]: t.get("code", t.get("md")) for t in teile}
        rf = lo.get("reihenfolgen") if isinstance(lo, dict) else None
        if not isinstance(rf, list) or not rf: err(where, "order: reihenfolgen fehlen")
        else:
            for seq in rf:
                if not set(seq) <= set(ids): err(where, f"order: unbekannte ids {set(seq) - set(ids)}")
                if len(set(seq)) != len(seq): err(where, "order: id doppelt in Reihenfolge")
                used = [txt[s] for s in seq if s in txt]
                if len(set(used)) != len(used): err(where, "order: identische Teile in der Lösung (mehrdeutig)")
            if len({tuple(s) for s in rf}) != len(rf): err(where, "order: doppelte Reihenfolge")
            unused = set(ids) - set(x for s in rf for x in s)
            for u in unused:
                if any(txt[u] == txt[s] for s in rf[0]): err(where, f"order: Distraktor {u} identisch mit Lösungsteil")
    elif kind == "lines":
        b = ia.get("block")
        if not isinstance(b, int) or not (0 <= b < len(inhalt)) or inhalt[b].get("t") != "code": err(where, "lines: block zeigt nicht auf code")
        else:
            n = inhalt[b]["code"].count("\n") + 1
            z = lo.get("zeilen") if isinstance(lo, dict) else None
            if not isinstance(z, list) or len(z) != ia.get("anzahl") or len(set(z)) != len(z) or not all(isinstance(x, int) and 1 <= x <= n for x in z):
                err(where, "lines: zeilen/anzahl ungültig")
            if inhalt[b].get("nummern") is False: err(where, "lines: Code-Block ohne Zeilennummern")
    elif kind == "match":
        el = [e.get("id") for e in ia.get("elemente", [])]; ka = [k.get("id") for k in ia.get("kategorien", [])]
        if len(set(el)) != len(el) or len(set(ka)) != len(ka) or len(ka) < 2: err(where, "match: ids")
        if not isinstance(lo, dict) or set(lo) != set(el) or not set(lo.values()) <= set(ka): err(where, "match: Lösung passt nicht")
    elif kind == "array":
        st = ia.get("start")
        if not isinstance(st, list) or not st: err(where, "array: start"); return set()
        if ia.get("modus") == "tausch":
            tw = lo.get("tausche") if isinstance(lo, dict) else None
            if not isinstance(tw, list) or not tw: err(where, "array: tausche fehlt")
            else:
                for p in tw:
                    if not (isinstance(p, list) and len(p) == 2 and all(isinstance(x, int) and 0 <= x < len(st) for x in p) and p[0] != p[1]):
                        err(where, f"array: Tauschpaar {p} ungültig")
        elif ia.get("modus") == "klick":
            f = lo.get("folge") if isinstance(lo, dict) else None
            if not isinstance(f, list) or not f or not all(isinstance(x, int) and 0 <= x < len(st) for x in f): err(where, "array: folge ungültig")
        else: err(where, "array: modus")
    else:
        warn(where, f"Interaktion {kind} nicht tief geprüft")
    return set()

def check_task(a, where):
    for k in ("id", "titel", "stufe", "punkte", "kategorie", "fallen", "inhalt", "interaktion", "loesung", "erklaerung"):
        if k not in a: err(where, f"Feld {k} fehlt")
    if a.get("stufe") not in PUNKTE: err(where, "stufe")
    elif a.get("punkte") != PUNKTE[a["stufe"]]: err(where, "punkte passen nicht zur stufe")
    if a.get("kategorie") not in LAB_KATEGORIEN: err(where, f"kategorie '{a.get('kategorie')}'")
    if not isinstance(a.get("fallen"), list) or not set(a["fallen"]) <= FALLEN or len(set(a["fallen"])) != len(a["fallen"]): err(where, "fallen")
    if not isinstance(a.get("tipps", []), list) or not all(isinstance(x, str) and x for x in a.get("tipps", [])): err(where, "tipps")
    if not isinstance(a.get("erklaerung"), list) or not a["erklaerung"]: err(where, "erklaerung fehlt")
    for b in a.get("erklaerung", []):
        if GAP.search(" ".join(block_texts(b, where + " (Erklärung)"))): err(where, "Lücke in der Erklärung")
    inhalt = a.get("inhalt", [])
    if not isinstance(inhalt, list) or not inhalt: err(where, "inhalt leer"); return set()
    gaps_in = []
    for i, b in enumerate(inhalt):
        for s in block_texts(b, f"{where} inhalt[{i}]"): gaps_in += GAP.findall(s)
    dup = [g for g, c in Counter(gaps_in).items() if c > 1]
    if dup: err(where, f"Lücke mehrfach im Inhalt: {dup}")
    ia, lo = a.get("interaktion"), a.get("loesung")
    parts = list(zip(ia, lo)) if isinstance(ia, list) else [(ia, lo)]
    if isinstance(ia, list) and (not isinstance(lo, list) or len(lo) != len(ia)): err(where, "mehrteilig: loesung-Array passt nicht")
    felder = []
    kinds = []
    for j, (p, l) in enumerate(parts):
        kinds.append(p.get("kind") + (":" + p["modus"] if p.get("modus") else ""))
        felder += list(check_part(p, l, inhalt, f"{where} teil {j}"))
    if len(felder) != len(set(felder)): err(where, "Feld-id in mehreren gaps-Teilen")
    if set(felder) != set(gaps_in): err(where, f"Lücken ↔ Felder: im Inhalt {sorted(set(gaps_in) - set(felder))}, ohne Lücke {sorted(set(felder) - set(gaps_in))}")
    if gaps_in and "gaps" not in [p.get("kind") for p, _ in parts]: err(where, "Lücken ohne gaps-Interaktion")
    if GAP.search(json.dumps(lo, ensure_ascii=False)): err(where, "Lücke in der Lösung")
    return kinds

def main(path):
    d = json.load(open(path, encoding="utf-8"))
    for k in ("version", "welt", "titel", "farbe", "levels", "boss", "aufgaben"):
        if k not in d: err("welt", f"{k} fehlt")
    if d.get("version") != 2: err("welt", "version != 2")
    n = d.get("welt")
    if not re.fullmatch(r"#[0-9A-Fa-f]{6}", d.get("farbe", "")): err("welt", "farbe")
    tasks = {}
    for a in d.get("aufgaben", []):
        if a.get("id") in tasks: err(a.get("id"), "id doppelt")
        tasks[a.get("id")] = a
    lvl_ids, lvl_tasks = set(), []
    stat = []
    all_kinds = Counter()
    for L in d.get("levels", []):
        w = L.get("id", "?")
        for k in ("id", "nr", "titel", "ds", "ab", "ide", "intro", "aufgaben"):
            if k not in L: err(w, f"Level-Feld {k} fehlt")
        if not re.fullmatch(rf"W{n}-L\d+", w) or w in lvl_ids: err(w, "Level-id ungültig/doppelt")
        lvl_ids.add(w)
        if not isinstance(L.get("ds"), list) or not all(isinstance(x, int) for x in L["ds"]): err(w, "ds")
        for i, b in enumerate(L.get("intro", [])):
            if GAP.search(" ".join(block_texts(b, f"{w} intro[{i}]"))): err(w, "Lücke im Intro")
        ids = L.get("aufgaben", [])
        if not 6 <= len(ids) <= 8: err(w, f"{len(ids)} Aufgaben (6–8 gefordert)")
        st = Counter(); kinds = set()
        for tid in ids:
            if tid not in tasks: err(w, f"verweist auf unbekannte Aufgabe {tid}"); continue
            if not re.fullmatch(rf"{w}-\d\d", tid): err(tid, f"id passt nicht zum Level {w}")
            lvl_tasks.append(tid); st[tasks[tid]["stufe"]] += 1
            ks = check_task(tasks[tid], tid); kinds |= set(ks); all_kinds.update(ks)
        stat.append((w, L.get("nr"), L.get("titel"), L.get("ds"), len(ids), dict(sorted(st.items())), sorted(kinds)))
    if len(lvl_tasks) != len(set(lvl_tasks)): err("levels", "Aufgabe in mehreren Leveln")
    B = d.get("boss", {})
    for k in ("id", "titel", "dauerMin", "anzahl", "mix", "pool"):
        if k not in B: err("boss", f"{k} fehlt")
    pool = B.get("pool", [])
    if not 14 <= len(pool) <= 16: err("boss", f"Pool {len(pool)} (14–16)")
    if not 20 <= B.get("dauerMin", 0) <= 30: err("boss", "dauerMin")
    if B.get("anzahl") != 8 or B.get("mix") != {"1": 3, "2": 3, "3": 2}: err("boss", "anzahl/mix")
    if sum(B.get("mix", {}).values()) != B.get("anzahl"): err("boss", "Mix-Summe ≠ anzahl")
    pst = Counter()
    for tid in pool:
        if tid not in tasks: err("boss", f"unbekannt {tid}"); continue
        if not re.fullmatch(rf"W{n}-B-\d\d", tid): err(tid, "Boss-id")
        if tid in lvl_tasks: err(tid, "Boss-Aufgabe auch in Level")
        pst[tasks[tid]["stufe"]] += 1
        all_kinds.update(check_task(tasks[tid], tid))
    for s, c in B.get("mix", {}).items():
        if pst[int(s)] < c: err("boss", f"Mix nicht erfüllbar: Stufe {s} braucht {c}, Pool hat {pst[int(s)]}")
    orphan = set(tasks) - set(lvl_tasks) - set(pool)
    if orphan: err("aufgaben", f"weder Level noch Boss: {sorted(orphan)}")
    base_kinds = {k.split(":")[0] for k in all_kinds}
    if len(base_kinds) < 5: err("welt", f"nur {len(base_kinds)} Interaktionsarten")
    # Bericht
    print(f"Welt {n} „{d.get('titel')}“: {len(d.get('levels', []))} Level, {len(lvl_tasks)} Level-Aufgaben, Boss-Pool {len(pool)} {dict(sorted(pst.items()))}")
    for row in stat: print("  ", *row)
    print("  Interaktionen gesamt:", dict(all_kinds))
    print("  Kategorien:", dict(Counter(a["kategorie"] for a in tasks.values())))
    for w in WARN: print("WARNUNG", w)
    for e in ERR: print("FEHLER ", e)
    print("ERGEBNIS:", "GRÜN" if not ERR else f"ROT ({len(ERR)} Fehler)")
    return 0 if not ERR else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
