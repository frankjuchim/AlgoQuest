"""Sortier- und Suchverfahren EXAKT wie in Welt 2 (AQ_W2_L2_Rangliste_LSG.txt), absteigend nach Punkten
(besser(a, b) = a > b), plus binaere Suche (aufsteigend, mid = (lo + hi) / 2). Jede Funktion protokolliert
Vertauschungen (Paare), Vergleiche (Aufrufe von besser) und Zustaende nach jedem Durchlauf der aeusseren Schleife."""
from lib import run, check


def selection(werte, key=lambda x: x):
    a = list(werte); n = len(a); comps = 0; swaps = []; states = []; comp_rows = []
    for i in range(n - 1):
        mx = i
        for j in range(i + 1, n):
            comps += 1
            if key(a[j]) > key(a[mx]):
                mx = j
        if mx != i:
            a[i], a[mx] = a[mx], a[i]; swaps.append([i, mx])
        states.append(list(a)); comp_rows.append((comps, len(swaps)))
    return dict(final=a, comps=comps, swaps=swaps, states=states, rows=comp_rows)


def insertion(werte, key=lambda x: x):
    a = list(werte); n = len(a); comps = 0; swaps = []; states = []; comp_rows = []
    for i in range(1, n):
        j = i
        while j > 0:
            comps += 1
            if key(a[j]) > key(a[j - 1]):
                a[j], a[j - 1] = a[j - 1], a[j]; swaps.append([j, j - 1]); j -= 1
            else:
                break
        states.append(list(a)); comp_rows.append((comps, len(swaps)))
    return dict(final=a, comps=comps, swaps=swaps, states=states, rows=comp_rows)


def bubble(werte, key=lambda x: x):
    a = list(werte); n = len(a); comps = 0; swaps = []; states = []; comp_rows = []
    getauscht = True; d = 0
    while getauscht:
        getauscht = False
        for j in range(0, n - 1 - d):
            comps += 1
            if key(a[j + 1]) > key(a[j]):
                a[j], a[j + 1] = a[j + 1], a[j]; swaps.append([j, j + 1]); getauscht = True
        d += 1
        states.append(list(a)); comp_rows.append((comps, len(swaps)))
    return dict(final=a, comps=comps, swaps=swaps, states=states, rows=comp_rows)


ALG = {'selection': selection, 'insertion': insertion, 'bubble': bubble}
JNAME = {'selection': 'selectionSort', 'insertion': 'insertionSort', 'bubble': 'bubbleSort'}
LOGRL = ('class LogRL extends Rangliste {\n  public LogRL(int k) { super(k); }\n'
         '  public void vertausche(int i, int j) { println("T;" + i + ";" + j); super.vertausche(i, j); }\n}')


def java_sort(kind, werte, namen=None):
    """Fuehrt die LSG-Methode der Rangliste aus (Unterklasse protokolliert vertausche)."""
    n = len(werte)
    namen = namen or [f'E{i}' for i in range(n)]
    main = f'LogRL r = new LogRL({n});' + ''.join(f' r.hinzufuegen(new Eintrag("{nm}", {v}, 0));' for nm, v in zip(namen, werte)) \
        + f' r.{JNAME[kind]}(); println("V;" + r.getVergleiche() + ";" + r.getVertauschungen());' \
        + ' for (int i = 0; i < r.getAnzahl(); i++) println("E;" + r.getEintrag(i).getName() + ";" + r.getEintrag(i).getPunkte());'
    out = run(2, main, LOGRL)
    swaps = [[int(x) for x in l.split(';')[1:]] for l in out if l.startswith('T;')]
    v = [l for l in out if l.startswith('V;')][0].split(';')
    final = [(l.split(';')[1], int(l.split(';')[2])) for l in out if l.startswith('E;')]
    return dict(swaps=swaps, comps=int(v[1]), nswaps=int(v[2]), final=final)


def sort_verified(kind, werte, tag):
    p = ALG[kind](werte)
    j = java_sort(kind, werte)
    check(p['swaps'] == j['swaps'] and p['comps'] == j['comps'] and [x[1] for x in j['final']] == p['final'],
          f'{tag}: {kind} auf {werte}: Tauschfolge {p["swaps"]}, {p["comps"]} Vergleiche = Java-LSG')
    return p


def binsearch(r, x):
    lo, hi = 0, len(r) - 1; mids = []; rows = []
    while lo <= hi:
        mid = (lo + hi) // 2
        mids.append(mid)
        if r[mid] == x:
            rows.append((lo, hi, mid, r[mid], 'gib mid zurück'))
            return dict(mids=mids, result=mid, rows=rows, lo=lo, hi=hi)
        if r[mid] < x:
            rows.append((lo, hi, mid, r[mid], 'lo ← mid + 1')); lo = mid + 1
        else:
            rows.append((lo, hi, mid, r[mid], 'hi ← mid − 1')); hi = mid - 1
    return dict(mids=mids, result=-1, rows=rows, lo=lo, hi=hi)


def search_verified(r, x, tag):
    p = binsearch(r, x)
    arr = '{' + ', '.join(map(str, r)) + '}'
    out = run(2, f'int[] r = {arr}; println(Suche.binaer(r, {x})); println(Suche.durchlaeufe);')
    check(int(out[0]) == p['result'] and int(out[1]) == len(p['mids']),
          f'{tag}: binaere Suche nach {x} -> {p["result"]}, mids {p["mids"]} ({len(p["mids"])} Durchlaeufe = Java Suche.binaer)')
    return p


def max_durchlaeufe(n):
    """Hoechstzahl der Schleifendurchlaeufe bei n Elementen (Rekursion ueber die groessere Haelfte)."""
    if n <= 0:
        return 0
    links = (n - 1) // 2               # Elemente lo .. mid-1
    rechts = n - 1 - links             # Elemente mid+1 .. hi (die groessere Haelfte, Monotonie)
    return 1 + max_durchlaeufe(max(links, rechts))


def max_durchlaeufe_brute(n):
    r = list(range(0, 2 * n, 2))
    best = 0
    for x in range(-1, 2 * n + 1):
        best = max(best, len(binsearch(r, x)['mids']))
    return best
