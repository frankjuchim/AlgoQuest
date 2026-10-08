#!/usr/bin/env python3
"""Erzeugt content/welt1.json und content/welt2.json (alle Loesungen per Java/Skript geprueft) und validiert sie."""
import json, os, subprocess, sys
import lib
import w1, w2

# Bug-Hunt: markierte Zeilen muessen genau die fehlerhaften Anweisungen enthalten
ERWARTET = {'W1-L1-06': ['name = name;'], 'W1-L2-06': ['return leben < 0;', 'h.leben = h.leben - staerke;'],
            'W1-L3-03': ['i < inventar.length'], 'W1-L4-05': ['this.magie = magie;', 'super(name, wert);'],
            'W1-B-09': ['i <= anzahl', '== name', 'return null;'], 'W1-B-13': ['spannweite = spannweite;', 'return tempo * 2;'],
            'W2-L1-04': ['return summe / anzahl;'], 'W2-L4-05': ['while (lo < hi)', 'lo = mid;'],
            'W2-B-08': ['int min = 0;'], 'W2-B-14': ['while (r[j] > r[j - 1] && j > 0)']}
for mod in (w1, w2):
    for a in mod.A:
        its = a['interaktion'] if isinstance(a['interaktion'], list) else [a['interaktion']]
        los = a['loesung'] if isinstance(a['loesung'], list) else [a['loesung']]
        for it, lo in zip(its, los):
            if it['kind'] == 'lines':
                zeilen = a['inhalt'][it['block']]['code'].split('\n')
                markiert = [zeilen[z - 1] for z in lo['zeilen']]
                lib.check(all(any(e in m for m in markiert) for e in ERWARTET[a['id']]) and len(markiert) == len(ERWARTET[a['id']]),
                          f"{a['id']} Bug-Hunt-Zeilen {lo['zeilen']}: {[m.strip() for m in markiert]}")

OUT = os.path.join(os.path.dirname(lib.W), 'content')
os.makedirs(OUT, exist_ok=True)
for mod, n in ((w1, 1), (w2, 2)):
    p = os.path.join(OUT, f'welt{n}.json')
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(mod.WELT, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('geschrieben:', p, len(mod.WELT['aufgaben']), 'Aufgaben')
open(os.path.join(lib.W, 'pruefprotokoll.txt'), 'w', encoding='utf-8').write('\n'.join(lib.LOG) + f'\n\n{len(lib.LOG)} Pruefungen OK\n')
print(len(lib.LOG), 'Pruefungen OK')
r = subprocess.run([sys.executable, os.path.join(lib.W, 'validate.py'), os.path.join(OUT, 'welt1.json'), os.path.join(OUT, 'welt2.json')])
sys.exit(r.returncode)
