# Eigenvalidierung welt<N>.json gegen SPEC_AlgoLab §3–§5 (+ §10 Mengenvorgaben)
import json, re, sys, collections
sys.path.insert(0, "/tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad/algolab/w56")
from common import parse, ks, node_at, LAB_KATEGORIEN, PUNKTE, nodes_pre

PH = re.compile(r"\[\[([A-Za-z0-9_]+)\]\]")
FALLEN = {"P%d" % i for i in range(1, 11)}
BLOCK_KEYS = {"text": {"md"}, "code": {"code"}, "struktogramm": {"kopf", "rumpf"}, "tabelle": {"kopf", "zeilen"}, "baum": {"baum"},
              "reihung": {"werte"}, "raster": {"zeilen"}, "klassenkarte": {"name", "attribute", "methoden"}, "adt": {"art", "inhalt"},
              "hinweis": {"md"}}
KNOTEN = {"anw", "wenn", "solange", "zaehle", "wiederhole", "gib", "aufruf"}
fehler = []
def F(msg): fehler.append(msg)

def strings_of_block(b):
    t = b["t"]
    if t in ("text", "hinweis"): yield b["md"]
    elif t == "code": yield b["code"]
    elif t == "tabelle":
        for k in b["kopf"]: yield k
        for z in b["zeilen"]:
            for c in z: yield c
    elif t == "struktogramm":
        yield b["kopf"]
        yield from strings_of_knoten(b["rumpf"])
    elif t == "klassenkarte":
        yield b["name"]; yield from b["attribute"]; yield from b["methoden"]

def strings_of_knoten(lst):
    for k in lst:
        if not isinstance(k, dict) or len(set(k) & KNOTEN) != 1:
            F("Struktogrammknoten ungültig: %r" % k); continue
        if "anw" in k: yield k["anw"]
        if "gib" in k: yield k["gib"]
        if "aufruf" in k: yield k["aufruf"]
        if "wenn" in k:
            yield k["wenn"]; yield from strings_of_knoten(k.get("dann", [])); yield from strings_of_knoten(k.get("sonst", []))
        if "solange" in k: yield k["solange"]; yield from strings_of_knoten(k["rumpf"])
        if "zaehle" in k: yield k["zaehle"]; yield from strings_of_knoten(k["rumpf"])
        if "wiederhole" in k: yield from strings_of_knoten(k["wiederhole"]); yield k["bis"]

def check_blocks(ctx, blocks, erlaube_luecken):
    phs = []
    if not isinstance(blocks, list) or not blocks: F("%s: Blockliste leer" % ctx); return phs
    for i, b in enumerate(blocks):
        t = b.get("t")
        if t not in BLOCK_KEYS: F("%s: Blocktyp %r" % (ctx, t)); continue
        if not BLOCK_KEYS[t] <= set(b): F("%s: Block %d (%s) Felder fehlen" % (ctx, i, t))
        if t == "baum":
            try: parse(b["baum"])
            except Exception as e: F("%s: Baum nicht parsebar %r (%s)" % (ctx, b["baum"], e))
        if t == "tabelle":
            for z in b["zeilen"]:
                if len(z) != len(b["kopf"]): F("%s: Tabellenzeile Länge %d ≠ Kopf %d" % (ctx, len(z), len(b["kopf"])))
        if t == "adt" and b["art"] not in ("stapel", "schlange", "dynarray"): F("%s: adt-art" % ctx)
        if t == "raster" and len({len(z) for z in b["zeilen"]}) != 1: F("%s: raster ungleich lang" % ctx)
        for s in strings_of_block(b):
            if not isinstance(s, str): F("%s: Nicht-String in Block %d" % (ctx, i)); continue
            if "TODO" in s: F("%s: TODO" % ctx)
            phs += PH.findall(s)
    if phs and not erlaube_luecken: F("%s: Lücken in Erklärung/Intro: %s" % (ctx, phs))
    return phs

def num(s):
    try: float(str(s).replace(",", ".")); return True
    except: return False

def check_inter(ctx, it, lo, inhalt, alle_felder):
    k = it.get("kind")
    if k == "gaps":
        felder = it["felder"]
        for fid, f in felder.items():
            if fid in alle_felder: F("%s: Feld %s doppelt" % (ctx, fid))
            alle_felder.add(fid)
            if f.get("typ") not in ("text", "zahl", "auswahl"): F("%s: Feldtyp %s" % (ctx, fid))
            if f.get("typ") == "auswahl" and not f.get("optionen"): F("%s: auswahl ohne optionen %s" % (ctx, fid))
            if f.get("norm") not in (None, "code", "text", "exakt"): F("%s: norm %s" % (ctx, fid))
        if set(lo) != set(felder): F("%s: loesung-Schlüssel %s ≠ felder %s" % (ctx, sorted(lo), sorted(felder)))
        for fid, acc in lo.items():
            if not isinstance(acc, list) or not acc or not all(isinstance(a, str) and a != "" for a in acc):
                F("%s: Lösung %s keine nicht-leere String-Liste: %r" % (ctx, fid, acc)); continue
            f = felder.get(fid, {})
            if f.get("typ") == "zahl" and not all(num(a) for a in acc): F("%s: zahl-Lösung %s nicht numerisch %r" % (ctx, fid, acc))
            if f.get("typ") == "auswahl" and not all(a in f["optionen"] for a in acc): F("%s: auswahl-Lösung %s nicht in optionen" % (ctx, fid))
    elif k == "choice":
        ids = [o["id"] for o in it["optionen"]]
        if len(ids) != len(set(ids)) or len(ids) < 2: F("%s: choice-ids" % ctx)
        r = lo.get("richtig")
        if not r or not set(r) <= set(ids): F("%s: choice richtig %r" % (ctx, r))
        if not it.get("mehrfach") and len(r or []) != 1: F("%s: Einfachauswahl mit %d richtigen" % (ctx, len(r or [])))
        if it.get("mehrfach") is None: F("%s: mehrfach fehlt" % ctx)
    elif k == "order":
        ids = [t["id"] for t in it["teile"]]
        if len(ids) != len(set(ids)): F("%s: order-ids doppelt" % ctx)
        for t in it["teile"]:
            if not (t.get("code") or t.get("md")): F("%s: order-Teil leer" % ctx)
        rf = lo.get("reihenfolgen")
        if not rf: F("%s: keine reihenfolgen" % ctx)
        for r in rf or []:
            if not set(r) <= set(ids) or len(r) != len(set(r)): F("%s: Reihenfolge mit unbekannten/doppelten ids %r" % (ctx, r))
        if rf and len({tuple(sorted(r)) for r in rf}) != 1: F("%s: Reihenfolgen nutzen verschiedene Teilmengen" % ctx)
    elif k == "lines":
        b = it.get("block")
        if not isinstance(b, int) or b >= len(inhalt) or inhalt[b]["t"] != "code": F("%s: lines-block %r kein Codeblock" % (ctx, b)); return
        n = len(inhalt[b]["code"].split("\n"))
        z = lo.get("zeilen", [])
        if len(z) != it.get("anzahl") or len(set(z)) != len(z): F("%s: lines anzahl %r ≠ %r" % (ctx, it.get("anzahl"), z))
        if not all(isinstance(x, int) and 1 <= x <= n for x in z): F("%s: lines-Zeile außerhalb 1..%d: %r" % (ctx, n, z))
    elif k == "match":
        el = {e["id"] for e in it["elemente"]}; ka = {c["id"] for c in it["kategorien"]}
        if set(lo) != el or not set(lo.values()) <= ka: F("%s: match-Lösung" % ctx)
    elif k == "tree":
        if it.get("modus") == "klick":
            try: t = parse(it["baum"])
            except Exception as e: F("%s: klick-baum %s" % (ctx, e)); return
            fo = lo.get("folge")
            if not fo or len(fo) != len(set(fo)): F("%s: folge leer/doppelt" % ctx)
            for p in fo or []:
                if not re.fullmatch(r"[LR]*", p) or node_at(t, p) is None: F("%s: Pfad %r existiert nicht" % (ctx, p))
        elif it.get("modus") == "bauen":
            try:
                st = parse(it["start"]); ziel = parse(lo["baum"])
            except Exception as e: F("%s: bauen nicht parsebar %s" % (ctx, e)); return
            if ks(ziel) != lo["baum"]: F("%s: Lösungsbaum nicht normalisiert %r" % (ctx, lo["baum"]))
            vorrat = collections.Counter([n.v for p, n in nodes_pre(st)] + [str(w) for w in it.get("werte", [])])
            bedarf = collections.Counter([n.v for p, n in nodes_pre(ziel)])
            if bedarf - vorrat: F("%s: Werte im Zielbaum weder im Start noch in werte: %s" % (ctx, dict(bedarf - vorrat)))
        else: F("%s: tree-modus" % ctx)
    elif k == "array":
        st = it["start"]
        if it.get("modus") == "tausch":
            for p in lo.get("tausche", []):
                if len(p) != 2 or not all(isinstance(i, int) and 0 <= i < len(st) for i in p) or p[0] == p[1]: F("%s: Tauschpaar %r" % (ctx, p))
        elif it.get("modus") == "klick":
            if not lo.get("folge") or not all(isinstance(i, int) and 0 <= i < len(st) for i in lo["folge"]): F("%s: array-klick folge" % ctx)
        else: F("%s: array-modus" % ctx)
    elif k == "grid":
        R = it["raster"]
        for z in lo.get("zellen", []):
            if not (0 <= z[0] < len(R) and 0 <= z[1] < len(R[0])): F("%s: Zelle %r außerhalb" % (ctx, z))
        if "reihenfolge" not in lo: F("%s: grid reihenfolge fehlt" % ctx)
    elif k == "adtsim":
        if it.get("art") not in ("stapel", "schlange", "dynarray"): F("%s: adtsim art" % ctx)
        if not isinstance(lo.get("inhalt"), list): F("%s: adtsim inhalt" % ctx)
    else:
        F("%s: unbekannte Interaktion %r" % (ctx, k))
    return k

def validate(path):
    d = json.load(open(path))
    n = d["welt"]
    for k in ("version", "welt", "titel", "farbe", "levels", "boss", "aufgaben"):
        if k not in d: F("Top-Level-Feld %s fehlt" % k)
    if d["version"] != 2: F("version ≠ 2")
    auf = {}
    for a in d["aufgaben"]:
        if a["id"] in auf: F("Aufgaben-id doppelt %s" % a["id"])
        auf[a["id"]] = a
    kinds = collections.Counter(); level_ids = set(); benutzt = collections.Counter()
    stat = []
    for L in d["levels"]:
        if not re.fullmatch(r"W%d-L\d+" % n, L["id"]): F("Level-id %s" % L["id"])
        if L["id"] in level_ids: F("Level-id doppelt")
        level_ids.add(L["id"])
        for k in ("nr", "titel", "ds", "ab", "ide", "intro", "aufgaben"):
            if k not in L: F("%s: Feld %s fehlt" % (L["id"], k))
        check_blocks(L["id"] + "/intro", L["intro"], False)
        if not 6 <= len(L["aufgaben"]) <= 8: F("%s: %d Aufgaben (6–8 gefordert)" % (L["id"], len(L["aufgaben"])))
        st = collections.Counter()
        lk = set()
        for aid in L["aufgaben"]:
            if aid not in auf: F("%s: Verweis auf fehlende Aufgabe %s" % (L["id"], aid)); continue
            if not aid.startswith(L["id"] + "-"): F("%s: Aufgabe %s passt nicht zum Level" % (L["id"], aid))
            benutzt[aid] += 1; st[auf[aid]["stufe"]] += 1
            it = auf[aid]["interaktion"]; lk |= {x["kind"] + ("-" + x.get("modus", "") if x.get("modus") else "") for x in (it if isinstance(it, list) else [it])}
        stat.append((L["id"], L["nr"], L["titel"], L["ds"], len(L["aufgaben"]), dict(sorted(st.items())), sorted(lk)))
    bo = d["boss"]
    if not re.fullmatch(r"W%d-BOSS" % n, bo["id"]): F("Boss-id")
    if bo["anzahl"] != 8 or sum(bo["mix"].values()) != bo["anzahl"]: F("Boss anzahl/mix")
    if not 20 <= bo["dauerMin"] <= 30: F("Boss dauerMin")
    if not 14 <= len(bo["pool"]) <= 16: F("Boss-Pool %d (14–16)" % len(bo["pool"]))
    pst = collections.Counter()
    for aid in bo["pool"]:
        if not re.fullmatch(r"W%d-B-\d\d" % n, aid): F("Boss-id-Format %s" % aid)
        if aid not in auf: F("Boss-Pool verweist auf fehlende %s" % aid); continue
        benutzt[aid] += 1; pst[auf[aid]["stufe"]] += 1
    for s, m in bo["mix"].items():
        if pst[int(s)] < m: F("Boss-Mix nicht erfüllbar: Stufe %s braucht %d, Pool hat %d" % (s, m, pst[int(s)]))
    for aid in auf:
        if benutzt[aid] != 1: F("Aufgabe %s %d-mal verwendet" % (aid, benutzt[aid]))
    for aid, a in auf.items():
        ctx = aid
        if not re.fullmatch(r"W%d-(L\d+-\d\d|B-\d\d)" % n, aid): F("%s: id-Format" % aid)
        for k in ("titel", "stufe", "punkte", "kategorie", "fallen", "inhalt", "interaktion", "loesung", "erklaerung"):
            if k not in a: F("%s: Feld %s fehlt" % (aid, k))
        if a["stufe"] not in (1, 2, 3) or a["punkte"] != PUNKTE[a["stufe"]]: F("%s: stufe/punkte" % aid)
        if a["kategorie"] not in LAB_KATEGORIEN: F("%s: Kategorie %r" % (aid, a["kategorie"]))
        if not set(a["fallen"]) <= FALLEN: F("%s: fallen %r" % (aid, a["fallen"]))
        phs = check_blocks(ctx + "/inhalt", a["inhalt"], True)
        check_blocks(ctx + "/erklaerung", a["erklaerung"], False)
        for tp in a.get("tipps", []):
            if not isinstance(tp, str) or not tp: F("%s: Tipp leer" % aid)
        its = a["interaktion"]; los = a["loesung"]
        if isinstance(its, list):
            if not isinstance(los, list) or len(los) != len(its): F("%s: Mehrteilig, loesung-Länge passt nicht" % aid); continue
        else:
            its, los = [its], [los]
        felder = set()
        for i, (it, lo) in enumerate(zip(its, los)):
            k = check_inter("%s[%d]" % (aid, i), it, lo, a["inhalt"], felder)
            kinds[k] += 1
        if collections.Counter(phs) != collections.Counter(felder) or len(phs) != len(set(phs)):
            F("%s: Lücken im Inhalt %s ↔ felder %s" % (aid, sorted(phs), sorted(felder)))
    if len(kinds) < 5: F("weniger als 5 Interaktionsarten: %s" % dict(kinds))
    return d, stat, kinds, pst

if __name__ == "__main__":
    for p in sys.argv[1:]:
        fehler.clear()
        d, stat, kinds, pst = validate(p)
        print("==", p)
        for s in stat: print("  ", s)
        print("   Boss-Pool Stufen:", dict(sorted(pst.items())), "| Interaktionen:", dict(kinds))
        print("   FEHLER:" if fehler else "   OK – keine Fehler", len(fehler))
        for f in fehler: print("   -", f)
