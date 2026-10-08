#!/usr/bin/env python3
"""Eigen-Validator fuer Algo-Quest-Lab-Weltdateien nach SPEC_AlgoLab.md §3–§5.
Aufruf: validate.py welt1.json [welt2.json …]  -> Exit 0 bei Erfolg, Fehlerliste sonst."""
import json, re, sys
from collections import Counter

LAB_KATEGORIEN = ["Datentypen und Ausdrücke", "Methodenkopf und Signatur", "Klasse vs. Objekt", "Bestandteile einer Klasse",
                  "Objektkarten und Referenzen", "Klassendiagramm", "Struktogramm lesen", "Code ↔ Struktogramm", "Tracetabelle",
                  "Rekursionstabelle", "Fehler im Java-Code", "Fehler im Struktogramm", "Lückencode", "Methode implementieren",
                  "ADT-Befehlsfolgen", "Sortieren und Suchen", "Effizienz", "Bäume", "Funktionsweise erläutern"]
FALLEN = {f'P{i}' for i in range(1, 11)}
PH = re.compile(r'\[\[([A-Za-z0-9_]+)\]\]')
BLOCKS = {'text', 'code', 'struktogramm', 'tabelle', 'baum', 'reihung', 'raster', 'klassenkarte', 'adt', 'hinweis'}
KINDS = {'gaps', 'choice', 'order', 'lines', 'match', 'tree', 'array', 'grid', 'adtsim'}


class V:
    def __init__(self):
        self.err = []

    def e(self, where, msg):
        self.err.append(f'{where}: {msg}')


def strings_of(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, list):
        for y in x:
            yield from strings_of(y)
    elif isinstance(x, dict):
        for y in x.values():
            yield from strings_of(y)


def check_sg_nodes(v, w, nodes):
    if not isinstance(nodes, list):
        v.e(w, 'Struktogramm-Rumpf ist keine Liste'); return
    for n in nodes:
        if not isinstance(n, dict) or not n:
            v.e(w, f'ungueltiger Knoten {n!r}'); continue
        if 'anw' in n or 'gib' in n or 'aufruf' in n:
            k = next(iter(n));
            if len(n) != 1 or not isinstance(n[k], str):
                v.e(w, f'Knoten {n!r}')
        elif 'wenn' in n:
            if set(n) - {'wenn', 'dann', 'sonst'} or 'dann' not in n:
                v.e(w, f'wenn-Knoten {n!r}')
            check_sg_nodes(v, w, n.get('dann', [])); check_sg_nodes(v, w, n.get('sonst', []))
        elif 'solange' in n or 'zaehle' in n:
            k = 'solange' if 'solange' in n else 'zaehle'
            if set(n) != {k, 'rumpf'}:
                v.e(w, f'{k}-Knoten {n!r}')
            check_sg_nodes(v, w, n.get('rumpf', []))
        elif 'wiederhole' in n:
            if set(n) != {'wiederhole', 'bis'}:
                v.e(w, f'wiederhole-Knoten {n!r}')
            check_sg_nodes(v, w, n['wiederhole'])
        else:
            v.e(w, f'unbekannter Knoten {n!r}')


def parse_tree(s):
    s = s.replace(' ', ''); pos = [0]
    def node():
        if s[pos[0]:pos[0] + 1] == '-':
            pos[0] += 1; return None
        m = re.match(r'[^(),]+', s[pos[0]:])
        if not m:
            raise ValueError('Wert erwartet bei ' + str(pos[0]))
        pos[0] += len(m.group(0))
        if s[pos[0]:pos[0] + 1] == '(':
            pos[0] += 1; node()
            if s[pos[0]] != ',':
                raise ValueError('Komma erwartet')
            pos[0] += 1; node()
            if s[pos[0]] != ')':
                raise ValueError(') erwartet')
            pos[0] += 1
        return True
    node()
    if pos[0] != len(s):
        raise ValueError('Rest: ' + s[pos[0]:])


def check_blocks(v, w, blocks, allow_gaps=True):
    if not isinstance(blocks, list) or not blocks:
        v.e(w, 'Blockliste leer oder keine Liste'); return
    for i, b in enumerate(blocks):
        ww = f'{w}[{i}]'
        t = b.get('t') if isinstance(b, dict) else None
        if t not in BLOCKS:
            v.e(ww, f'unbekannter Blocktyp {t!r}'); continue
        if t in ('text', 'hinweis') and not isinstance(b.get('md'), str):
            v.e(ww, 'md fehlt')
        if t == 'code':
            if not isinstance(b.get('code'), str):
                v.e(ww, 'code fehlt')
            for m in b.get('markiere', []):
                if not isinstance(m, int) or m < 1 or m > len(b['code'].split('\n')):
                    v.e(ww, f'markiere {m} ausserhalb')
        if t == 'struktogramm':
            if not isinstance(b.get('kopf'), str):
                v.e(ww, 'kopf fehlt')
            check_sg_nodes(v, ww, b.get('rumpf'))
        if t == 'tabelle':
            k = b.get('kopf'); z = b.get('zeilen')
            if not isinstance(k, list) or not isinstance(z, list):
                v.e(ww, 'kopf/zeilen fehlen')
            else:
                for r in z:
                    if len(r) != len(k):
                        v.e(ww, f'Zeile {r} hat {len(r)} statt {len(k)} Zellen')
                    if not all(isinstance(c, str) for c in r):
                        v.e(ww, f'Zelle kein String in {r}')
        if t == 'baum':
            try:
                parse_tree(b['baum'])
            except Exception as ex:
                v.e(ww, f'Baum nicht parsebar: {ex}')
        if t == 'reihung' and not isinstance(b.get('werte'), list):
            v.e(ww, 'werte fehlt')
        if t == 'klassenkarte':
            if not isinstance(b.get('name'), str) or not isinstance(b.get('attribute'), list) or not isinstance(b.get('methoden'), list):
                v.e(ww, 'name/attribute/methoden fehlen')
        if t == 'raster' and not isinstance(b.get('zeilen'), list):
            v.e(ww, 'zeilen fehlt')
        if t == 'adt' and b.get('art') not in ('stapel', 'schlange', 'dynarray'):
            v.e(ww, 'art ungueltig')
        for s in strings_of(b):
            if '[[' in s or ']]' in s:
                rest = PH.sub('', s)
                if '[[' in rest:
                    v.e(ww, f'ungueltige Lueckenschreibweise in {s[:60]!r}')
                if not allow_gaps and PH.search(s):
                    v.e(ww, f'Luecke in Erklaerung/Intro: {s[:60]!r}')


def num(s):
    return float(str(s).replace(',', '.').replace('−', '-').strip())


def check_inter(v, w, it, lo, inhalt):
    k = it.get('kind')
    if k not in KINDS:
        v.e(w, f'unbekannte Interaktion {k!r}'); return set()
    if not isinstance(lo, dict):
        v.e(w, 'loesung ist kein Objekt'); return set()
    ids = set()
    if k == 'gaps':
        f = it.get('felder')
        if not isinstance(f, dict) or not f:
            v.e(w, 'felder leer'); return set()
        if set(lo) != set(f):
            v.e(w, f'loesung-Schluessel {sorted(lo)} != felder {sorted(f)}')
        for fid, fd in f.items():
            ids.add(fid)
            typ = fd.get('typ')
            ans = lo.get(fid)
            if typ not in ('text', 'zahl', 'auswahl'):
                v.e(w, f'Feld {fid}: typ {typ!r}')
            if not isinstance(ans, list) or not ans or not all(isinstance(a, str) and a != '' for a in ans):
                v.e(w, f'Feld {fid}: Loesung muss nichtleere Liste von Strings sein'); continue
            if typ == 'auswahl':
                opts = fd.get('optionen')
                if not isinstance(opts, list) or len(opts) < 2 or len(set(opts)) != len(opts):
                    v.e(w, f'Feld {fid}: optionen fehlen/doppelt')
                elif any(a not in opts for a in ans):
                    v.e(w, f'Feld {fid}: Loesung {ans} nicht in optionen {opts}')
            if typ == 'zahl':
                for a in ans:
                    try:
                        num(a)
                    except ValueError:
                        v.e(w, f'Feld {fid}: Zahl-Loesung {a!r} nicht numerisch')
            if typ == 'text' and fd.get('norm', 'code') not in ('code', 'text', 'exakt'):
                v.e(w, f'Feld {fid}: norm {fd.get("norm")!r}')
    elif k == 'choice':
        opts = it.get('optionen', [])
        oids = [o.get('id') for o in opts]
        if len(oids) < 2 or len(set(oids)) != len(oids) or not all(isinstance(o.get('md'), str) for o in opts):
            v.e(w, 'choice-optionen ungueltig')
        r = lo.get('richtig')
        if not isinstance(r, list) or not r or any(x not in oids for x in r) or len(set(r)) != len(r):
            v.e(w, f'choice-loesung {r} ungueltig')
        elif not it.get('mehrfach') and len(r) != 1:
            v.e(w, 'Einfachauswahl mit mehreren richtigen Antworten')
        if set(lo) != {'richtig'}:
            v.e(w, 'choice-loesung hat fremde Schluessel')
    elif k == 'order':
        teile = it.get('teile', [])
        tids = [t.get('id') for t in teile]
        if len(set(tids)) != len(tids) or not all(('code' in t) or ('md' in t) for t in teile):
            v.e(w, 'order-teile ungueltig')
        rs = lo.get('reihenfolgen')
        if not isinstance(rs, list) or not rs:
            v.e(w, 'reihenfolgen fehlen')
        else:
            for r in rs:
                if any(x not in tids for x in r) or len(set(r)) != len(r):
                    v.e(w, f'Reihenfolge {r} ungueltig')
            if len({tuple(r) for r in rs}) != len(rs):
                v.e(w, 'doppelte Reihenfolgen')
    elif k == 'lines':
        bi = it.get('block')
        if not isinstance(bi, int) or bi < 0 or bi >= len(inhalt) or inhalt[bi].get('t') != 'code':
            v.e(w, f'lines.block {bi} zeigt nicht auf einen code-Block'); return set()
        n = len(inhalt[bi]['code'].split('\n'))
        z = lo.get('zeilen')
        if not isinstance(z, list) or len(z) != it.get('anzahl') or len(set(z)) != len(z) or any(not (1 <= x <= n) for x in z):
            v.e(w, f'lines-loesung {z} passt nicht zu anzahl {it.get("anzahl")} / {n} Zeilen')
    elif k == 'match':
        el = [e.get('id') for e in it.get('elemente', [])]
        ka = [e.get('id') for e in it.get('kategorien', [])]
        if len(set(el)) != len(el) or len(set(ka)) != len(ka) or len(ka) < 2:
            v.e(w, 'match-ids doppelt/zu wenige Kategorien')
        if set(lo) != set(el) or any(lo[x] not in ka for x in lo):
            v.e(w, 'match-loesung passt nicht')
    elif k == 'array':
        st = it.get('start')
        if not isinstance(st, list) or not st:
            v.e(w, 'array.start fehlt'); return set()
        n = len(st)
        if it.get('modus') == 'tausch':
            t = lo.get('tausche')
            if not isinstance(t, list) or any(not (isinstance(p, list) and len(p) == 2 and p[0] != p[1] and all(0 <= q < n for q in p)) for p in t):
                v.e(w, f'tausche {t} ungueltig')
        elif it.get('modus') == 'klick':
            f = lo.get('folge')
            if not isinstance(f, list) or not f or any(not (isinstance(q, int) and 0 <= q < n) for q in f):
                v.e(w, f'folge {f} ungueltig')
        else:
            v.e(w, f'array.modus {it.get("modus")!r}')
    elif k == 'tree':
        if it.get('modus') == 'klick':
            try:
                parse_tree(it['baum'])
            except Exception as ex:
                v.e(w, f'tree.baum: {ex}')
            if not all(isinstance(p, str) and set(p) <= {'L', 'R'} for p in lo.get('folge', [None])):
                v.e(w, 'tree-folge ungueltig')
        elif it.get('modus') == 'bauen':
            for s in (it.get('start', ''), lo.get('baum', '')):
                try:
                    parse_tree(s)
                except Exception as ex:
                    v.e(w, f'tree: {ex}')
    return ids


def validate(path, v):
    d = json.load(open(path, encoding='utf-8'))
    W = f'{path.split("/")[-1]}'
    n = d.get('welt')
    if d.get('version') != 2 or not isinstance(n, int):
        v.e(W, 'version/welt')
    if not re.fullmatch(r'#[0-9A-Fa-f]{6}', d.get('farbe', '')):
        v.e(W, 'farbe')
    aufg = d.get('aufgaben', [])
    byid = {}
    for a in aufg:
        if a['id'] in byid:
            v.e(W, f'doppelte id {a["id"]}')
        byid[a['id']] = a
    used = Counter()
    kinds = Counter()
    stats = []
    for L in d.get('levels', []):
        w = f'{W}/{L.get("id")}'
        if not re.fullmatch(rf'W{n}-L\d+', L.get('id', '')):
            v.e(w, 'Level-id')
        for f in ('nr', 'titel', 'ab', 'ide'):
            if not isinstance(L.get(f), str) or not L[f]:
                v.e(w, f'{f} fehlt')
        if not isinstance(L.get('ds'), list) or not all(isinstance(x, int) for x in L['ds']):
            v.e(w, 'ds')
        check_blocks(v, w + '/intro', L.get('intro'), allow_gaps=False)
        ids = L.get('aufgaben', [])
        if not (6 <= len(ids) <= 8):
            v.e(w, f'{len(ids)} Aufgaben (6–8 verlangt)')
        st = Counter()
        for i in ids:
            used[i] += 1
            if i not in byid:
                v.e(w, f'Verweis auf unbekannte Aufgabe {i}')
            elif not re.fullmatch(rf'{L["id"]}-\d\d', i):
                v.e(w, f'Aufgaben-id {i} passt nicht zum Level')
            else:
                st[byid[i]['stufe']] += 1
        stats.append((L['id'], L['nr'], L['titel'], L['ds'], len(ids), dict(sorted(st.items()))))
    b = d.get('boss', {})
    wb = f'{W}/boss'
    if b.get('id') != f'W{n}-BOSS' or not isinstance(b.get('titel'), str):
        v.e(wb, 'id/titel')
    if not (20 <= b.get('dauerMin', 0) <= 30) or b.get('anzahl') != 8 or b.get('mix') != {'1': 3, '2': 3, '3': 2}:
        v.e(wb, 'dauerMin/anzahl/mix')
    pool = b.get('pool', [])
    if not (14 <= len(pool) <= 16):
        v.e(wb, f'Pool hat {len(pool)} Aufgaben')
    pst = Counter()
    for i in pool:
        used[i] += 1
        if i not in byid or not re.fullmatch(rf'W{n}-B-\d\d', i):
            v.e(wb, f'Pool-id {i}')
        else:
            pst[str(byid[i]['stufe'])] += 1
    for s, m in b.get('mix', {}).items():
        if pst[s] < m:
            v.e(wb, f'Mix nicht erfuellbar: Stufe {s} {pst[s]} < {m}')
    if sum(b.get('mix', {}).values()) != b.get('anzahl'):
        v.e(wb, 'Summe mix != anzahl')
    for i in byid:
        if used[i] != 1:
            v.e(W, f'Aufgabe {i} ist {used[i]}-mal referenziert (genau 1 verlangt)')
    for a in aufg:
        w = f'{W}/{a.get("id")}'
        if not re.fullmatch(rf'W{n}-(L\d+|B)-\d\d', a.get('id', '')):
            v.e(w, 'id-Format')
        if a.get('stufe') not in (1, 2, 3) or a.get('punkte') != {1: 10, 2: 20, 3: 30}.get(a.get('stufe')):
            v.e(w, 'stufe/punkte')
        if a.get('kategorie') not in LAB_KATEGORIEN:
            v.e(w, f'kategorie {a.get("kategorie")!r}')
        if not isinstance(a.get('fallen'), list) or not set(a['fallen']) <= FALLEN:
            v.e(w, 'fallen')
        if not isinstance(a.get('titel'), str) or not a['titel']:
            v.e(w, 'titel')
        if 'tipps' in a and (not isinstance(a['tipps'], list) or not all(isinstance(t, str) for t in a['tipps'])):
            v.e(w, 'tipps')
        check_blocks(v, w + '/inhalt', a.get('inhalt'))
        check_blocks(v, w + '/erklaerung', a.get('erklaerung'), allow_gaps=False)
        its, los = a.get('interaktion'), a.get('loesung')
        if isinstance(its, list):
            if not isinstance(los, list) or len(los) != len(its):
                v.e(w, 'interaktion-Array und loesung-Array unterschiedlich lang'); continue
        else:
            its, los = [its], [los]
        gap_ids = []
        for k, (it, lo) in enumerate(zip(its, los)):
            kinds[it.get('kind')] += 1
            gap_ids += list(check_inter(v, f'{w}/interaktion[{k}]', it, lo, a.get('inhalt', [])))
        if len(gap_ids) != len(set(gap_ids)):
            v.e(w, 'Feld-ids in mehreren gaps-Teilen doppelt')
        ph = [m for s in strings_of(a.get('inhalt', [])) for m in PH.findall(s)]
        c = Counter(ph)
        for g in set(gap_ids):
            if c[g] != 1:
                v.e(w, f'Luecke [[{g}]] kommt {c[g]}-mal im Inhalt vor (genau 1 verlangt)')
        for g in c:
            if g not in gap_ids:
                v.e(w, f'Luecke [[{g}]] im Inhalt ohne Feld')
    return d, stats, kinds, pst


if __name__ == '__main__':
    v = V()
    for p in sys.argv[1:]:
        d, stats, kinds, pst = validate(p, v)
        print(f'== {p}: {len(d["aufgaben"])} Aufgaben, Interaktionsarten {dict(kinds)} ({len(kinds)} Arten), Boss-Pool Stufen {dict(sorted(pst.items()))}')
        for s in stats:
            print('   ', s)
        if len(kinds) < 5:
            v.e(p, f'nur {len(kinds)} Interaktionsarten')
    if v.err:
        print('\nFEHLER:')
        for e in v.err:
            print('  -', e)
        sys.exit(1)
    print('\nVALIDIERUNG: alles gruen')
