# Mutationstest: jede Mutation muss den Validator rot machen
import json, copy, subprocess, sys, os
src = json.load(open("../content/welt0.json", encoding="utf-8"))
T = {a["id"]: a for a in src["aufgaben"]}
def mut(name, fn):
    d = copy.deepcopy(src); fn(d, {a["id"]: a for a in d["aufgaben"]})
    json.dump(d, open("/tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad/algolab/w0/_mut.json", "w"), ensure_ascii=False)
    r = subprocess.run([sys.executable, "validate.py", "_mut.json"], capture_output=True, text=True)
    print(("erkannt  " if r.returncode else "VERPASST ") + name)
    return r.returncode != 0
ok = all([
  mut("Kategorie falsch", lambda d, t: t["W0-L1-01"].update(kategorie="Datentypen")),
  mut("Punkte passen nicht", lambda d, t: t["W0-L1-02"].update(punkte=20)),
  mut("Lücke ohne Feld", lambda d, t: t["W0-L1-02"]["inhalt"][0].update(md=t["W0-L1-02"]["inhalt"][0]["md"] + " [[zz]]")),
  mut("Feld ohne Lücke", lambda d, t: t["W0-L2-01"]["interaktion"]["felder"].update(g9={"typ": "zahl"}) or t["W0-L2-01"]["loesung"].update(g9=["1"])),
  mut("auswahl-Lösung nicht in Optionen", lambda d, t: t["W0-L1-04"]["loesung"][0].update(b1=["x"])),
  mut("order unbekannte id", lambda d, t: t["W0-L1-06"]["loesung"]["reihenfolgen"][0].append("zz")),
  mut("lines-Block kein Code", lambda d, t: t["W0-L1-07"]["interaktion"][0].update(block=0)),
  mut("match-Kategorie unbekannt", lambda d, t: t["W0-L1-01"]["loesung"].update(e1="k99")),
  mut("Boss-Mix unerfüllbar", lambda d, t: d["boss"].update(pool=d["boss"]["pool"][:5] + d["boss"]["pool"][5:11])),
  mut("Level verweist ins Leere", lambda d, t: d["levels"][0]["aufgaben"].append("W0-L1-99")),
  mut("Fallen ungültig", lambda d, t: t["W0-L3-01"].update(fallen=["P11"])),
  mut("Tauschpaar außerhalb", lambda d, t: t["W0-L3-06"]["loesung"]["tausche"].append([0, 9])),
  mut("choice einfach mit 2 richtigen", lambda d, t: t["W0-L4-02"]["loesung"][0].update(richtig=["a", "b"])),
  mut("Zahl-Lösung keine Zahl", lambda d, t: t["W0-L2-01"]["loesung"].update(g1=["vier"])),
  mut("Struktogramm-Knoten unbekannt", lambda d, t: t["W0-L1-08"]["inhalt"][2]["rumpf"].append({"foo": "x"})),
])
os.remove("_mut.json")
print("Mutationstest:", "alle erkannt" if ok else "LÜCKEN")
