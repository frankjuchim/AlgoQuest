# Prueft: Jeder Code-Block (ohne Lücken) ist woertlich (whitespace-normalisiert) Teil eines kompilierten Java-Quelltexts
import json, re, glob
src = ""
for f in glob.glob("java_*/src/aq/*.java") + glob.glob("javafail_*/src/aq/*.java"):
    src += open(f).read()
norm = lambda t: re.sub(r"\s+", "", t)
src = src.replace("__(", "(")                                   # Instrumentierungs-Umbenennung rueckgaengig
src = re.sub(r'out\(K\+"[^"]*", [^;]*\);', "", src)          # eingeschobene Proben
src = re.sub(r"zeile = \d+;", "", src)
S = norm(src)
for w in ("welt3", "welt4"):
    W = json.load(open("../content/%s.json" % w))
    nicht = []
    n = 0
    for a in W["aufgaben"]:
        for b in a["inhalt"]:
            if b["t"] != "code": continue
            n += 1
            teile = [norm(x) for x in re.split(r"\[\[[A-Za-z0-9_]+\]\]", b["code"]) if norm(x)]
            # Kommentar-Zeilen (// ...) koennen im Quelltext umgebrochen sein -> ok
            if not all(t in S for t in teile):
                nicht.append((a["id"], b["code"][:70].replace("\n", " ")))
    print(w, "Code-Blöcke:", n, "nicht woertlich kompiliert:", len(nicht))
    for x in nicht: print("   ", x)
