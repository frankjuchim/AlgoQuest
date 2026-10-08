# Unabhaengige Nachpruefung der fertigen JSON-Dateien (zusaetzlich zur Java-Verifikation beim Erzeugen)
import json, re, sys
sys.path.insert(0, "/tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad/algolab/w56")
from common import *

C = SCRATCH + "/algolab/content/"
w5 = json.load(open(C + "welt5.json")); w6 = json.load(open(C + "welt6.json"))
A = {a["id"]: a for a in w5["aufgaben"] + w6["aufgaben"]}
ok = 0
def check(bed, msg):
    global ok
    if not bed: raise SystemExit("FEHLER: " + msg)
    ok += 1
def parts(a):
    it, lo = a["interaktion"], a["loesung"]
    return list(zip(it, lo)) if isinstance(it, list) else [(it, lo)]

# 1) array-tausch: Tausche anwenden
def apply(start, tausche):
    r = list(start)
    for i, j in tausche: r[i], r[j] = r[j], r[i]
    return r
for aid in ["W6-L3-04", "W6-L3-05"]:
    for it, lo in parts(A[aid]):
        check(apply(it["start"], lo["tausche"]) == sorted(it["start"]), aid + " sortiert")
for it, lo in parts(A["W6-L4-06"]):
    r = apply(it["start"], lo["tausche"]); p = r.index(it["start"][0])
    check(all(x < it["start"][0] for x in r[:p]) and all(x >= it["start"][0] for x in r[p + 1:]), "zerlege Partition")
# Selectionsort-Tauschfolge unabhaengig nachrechnen
def sel(r):
    r = list(r); t = []
    for i in range(len(r) - 1):
        m = min(range(i, len(r)), key=lambda k: (r[k], k))
        if m != i: r[i], r[m] = r[m], r[i]; t.append([i, m])
    return t
check(parts(A["W6-L3-04"])[0][1]["tausche"] == sel(parts(A["W6-L3-04"])[0][0]["start"]), "Selectionsort-Folge")
def ins(r):
    r = list(r); t = []
    for i in range(1, len(r)):
        j = i
        while j > 0 and r[j - 1] > r[j]: r[j - 1], r[j] = r[j], r[j - 1]; t.append([j - 1, j]); j -= 1
    return t
check(parts(A["W6-L3-05"])[0][1]["tausche"] == ins(parts(A["W6-L3-05"])[0][0]["start"]), "Insertionsort-Folge")
def zerl(r):
    r = list(r); t = []; piv = r[0]; g = 0
    for i in range(1, len(r)):
        if r[i] < piv: g += 1; r[g], r[i] = r[i], r[g]; t.append([g, i])
    r[0], r[g] = r[g], r[0]; t.append([0, g]); return t
check(parts(A["W6-L4-06"])[0][1]["tausche"] == zerl(parts(A["W6-L4-06"])[0][0]["start"]), "zerlege-Folge")

# 2) array-klick: binaere Suche
def bmids(r, x):
    lo, hi, out = 0, len(r) - 1, []
    while lo <= hi:
        m = (lo + hi) // 2; out.append(m)
        if r[m] == x: break
        if r[m] < x: lo = m + 1
        else: hi = m - 1
    return out
for aid, x in [("W6-L2-02", 50), ("W6-B-04", 6)]:
    it, lo = parts(A[aid])[0]
    check(lo["folge"] == bmids(it["start"], x), aid + " mids")

# 3) grid: Flood-Fill
it, lo = parts(A["W6-L4-02"])[0]
R = it["raster"]; seen = set(); st = [(0, 0)]
while st:
    z, s = st.pop()
    if 0 <= z < len(R) and 0 <= s < len(R[0]) and R[z][s] == 0 and (z, s) not in seen:
        seen.add((z, s)); st += [(z + 1, s), (z - 1, s), (z, s + 1), (z, s - 1)]
check(sorted(map(tuple, lo["zellen"])) == sorted(seen) and len(seen) < sum(r.count(0) for r in R), "Flood-Fill")

# 4) adtsim: Befehlsfolgen in Python
s, q = [], [3, 7, 1, 9]
s.append(q.pop(0)); q.append(s[-1]); s.append(q.pop(0)); q.append(s.pop()); s.append(q.pop(0)); s.append(q[0])
l = [lo for it, lo in parts(A["W6-L4-03"])]
check(l[0]["inhalt"] == [str(x) for x in s] and l[1]["inhalt"] == [str(x) for x in q], "Mischaufgabe")
d = []; d.append("Axt"); d.append("Bogen"); d.insert(1, "Dolch"); d.append("Elixier"); del d[0]; d[1] = "Fackel"; d.insert(3, "Gift")
check(parts(A["W6-L4-04"])[0][1]["inhalt"] == d, "DynArray")
check(parts(A["W6-L1-03"])[0][1]["inhalt"] == list(reversed(parts(A["W6-L1-03"])[0][0]["start"])), "Stapel umgedreht")
qq = parts(A["W6-B-06"])[0][0]["start"]
check(parts(A["W6-B-06"])[0][1]["inhalt"] == [str(x) for x in qq[:-1]], "maxGold verliert letztes")
dd = [x for x in parts(A["W6-B-11"])[0][0]["start"]]; i = 0
while i < len(dd):
    if dd[i].endswith(":0"): del dd[i]
    i += 1
check(parts(A["W6-B-11"])[0][1]["inhalt"] == dd, "Löschen im Vorwärtslauf")

# 5) tree-klick: Pfadfolgen unabhaengig je nach Aufgabentyp
art = {"W5-L1-02": "pre", "W5-L1-03": "in", "W5-L1-08": "post", "W5-L3-04": "level", "W5-B-01": "in", "W5-B-02": "level"}
fn = {"pre": nodes_pre, "in": nodes_in, "post": nodes_post, "level": nodes_level}
for aid, a in art.items():
    it, lo = parts(A[aid])[0]
    check(lo["folge"] == paths(fn[a](parse(it["baum"]))), aid + " Traversierung")
it, lo = parts(A["W5-B-15"])[1]; check(lo["folge"] == paths(nodes_pre(parse(it["baum"]))), "B-15 pre")
for aid, x in [("W5-L4-01", 70), ("W5-B-03", 40)]:
    it, lo = parts(A[aid])[0]; t = parse(it["baum"])
    check(is_bst(t) and lo["folge"] == bst_path(t, x)[0], aid + " Suchweg")
# klick-Folgen muessen alle Knoten genau einmal enthalten (Traversierungen)
for aid in list(art) + ["W5-L3-07"]:
    it, lo = parts(A[aid])[0]
    check(sorted(lo["folge"]) == sorted(paths(nodes_pre(parse(it["baum"])))), aid + " vollständig")

# 6) tree-bauen: BST-Eigenschaft und Inorder-Probe bei Such-/Loeschaufgaben
for aid in ["W5-L4-02", "W5-L4-03", "W5-L4-05", "W5-L4-06", "W5-L4-07", "W5-L5-04", "W5-B-06", "W5-B-07"]:
    for it, lo in parts(A[aid]):
        if it["kind"] == "tree":
            check(is_bst(parse(lo["baum"])), aid + " ist BST")
for aid, x in [("W5-L4-06", 65), ("W5-L4-07", 41), ("W5-B-07", 23)]:
    it, lo = [p for p in parts(A[aid]) if p[0]["kind"] == "tree"][0]
    alt = vals(nodes_in(parse(it["start"]))); neu = vals(nodes_in(parse(lo["baum"])))
    check(neu == [v for v in alt if v != str(x)], aid + " Inorder-Probe")
for it, lo in parts(A["W5-L4-05"]):
    alt = vals(nodes_in(parse(it["start"]))); neu = vals(nodes_in(parse(lo["baum"])))
    check(len(neu) == len(alt) - 1 and set(neu) < set(alt), "L4-05 Inorder-Probe")

# 7) gaps: akzeptierte Antworten nach Normalisierung eindeutig/nicht leer; zahl numerisch
def normal(v, f):
    n = f.get("norm", "code")
    if f["typ"] == "zahl": return float(v.replace(",", "."))
    if n == "code": return re.sub(r"\s+", "", v)
    if n == "text": return re.sub(r"\s+", " ", v).strip().lower()
    return v
for a in w5["aufgaben"] + w6["aufgaben"]:
    for it, lo in parts(a):
        if it["kind"] == "gaps":
            for fid, acc in lo.items():
                f = it["felder"][fid]
                ns = [normal(v, f) for v in acc]
                check(all(n != "" for n in ns), a["id"] + " leere Antwort")

# 8) Klammerbaeume: keine Werte mit verbotenen Zeichen, '-' nie als Wert
for a in w5["aufgaben"] + w6["aufgaben"]:
    for b in a["inhalt"] + a["erklaerung"]:
        if b["t"] == "baum":
            for p, n in nodes_pre(parse(b["baum"])):
                check(n.v not in ("-", "") and not any(c in n.v for c in "(),"), a["id"] + " Baumwert")

# 9) W6: jede Aufgabe benennt mindestens eine Falle; Erklaerung/Inhalt nennt die P-Nummer
for a in w6["aufgaben"]:
    check(len(a["fallen"]) >= 1, a["id"] + " ohne Falle")
    txt = json.dumps(a["inhalt"] + a["erklaerung"], ensure_ascii=False)
    for p in a["fallen"]:
        check(re.search(r"\b%s\b" % p, txt) is not None, "%s nennt %s nicht" % (a["id"], p))
# W5: Aufgaben mit fallen nennen die P-Nummer in der Erklaerung oder im Inhalt
for a in w5["aufgaben"]:
    txt = json.dumps(a["inhalt"] + a["erklaerung"], ensure_ascii=False)
    for p in a["fallen"]:
        check(re.search(r"\b%s\b" % p, txt) is not None, "%s nennt %s nicht" % (a["id"], p))

# 10) Reservierte Klausur-/Probeklausur-Kontexte nicht verwendet
alltxt = json.dumps([w5, w6], ensure_ascii=False)
for wort in ["Paketstation", "Ladepark", "Kletterhalle", "Ladesäule", "Ladesaeule", "Paket", "Fach 10"]:
    check(wort not in alltxt, "reservierter Kontext: " + wort)
print("Zusatzprüfungen OK:", ok)
