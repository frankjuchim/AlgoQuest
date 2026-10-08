# Baut welt0.json und fuehrt alle Java-Pruefungen aus
import json, os, sys, traceback, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib

MODULES = [m for m in ["level1", "level2", "level3", "level4", "level5", "level6", "boss"]
           if os.path.exists(os.path.join(lib.HERE, m + ".py"))]
levels, boss = [], None
for m in MODULES:
    mod = importlib.import_module(m)
    for name in dir(mod):
        if name.startswith("LEVEL") and isinstance(getattr(mod, name), dict):
            levels.append(getattr(mod, name))
    if hasattr(mod, "BOSS"): boss = mod.BOSS
levels.sort(key=lambda l: l["id"])

only = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "--nocheck" else None
if "--nocheck" not in sys.argv:
    lib.reset_java()
    fails = 0
    for tid, fn in lib.CHECKS:
        if only and not tid.startswith(only): continue
        try:
            fn(lib.TASKS[tid]); print("ok  ", tid)
        except Exception as e:
            fails += 1; print("FAIL", tid); traceback.print_exc()
    missing = [t for t in lib.ORDER if t not in {c[0] for c in lib.CHECKS}]
    print(f"Pruefungen: {len(lib.CHECKS)} Aufgaben geprueft, {fails} Fehler; ohne Pruefung: {missing}")
    if fails: sys.exit(1)

welt = {"version": 2, "welt": 0, "titel": "Die Akademie", "farbe": "#7F6000",
        "levels": levels, "boss": boss, "aufgaben": [lib.TASKS[i] for i in lib.ORDER]}
if boss is None: del welt["boss"]
out = os.path.join(os.path.dirname(lib.HERE), "content", "welt0.json")
json.dump(welt, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("geschrieben:", out, len(lib.ORDER), "Aufgaben")
