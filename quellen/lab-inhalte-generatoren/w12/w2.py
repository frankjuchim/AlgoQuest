"""Welt 2 – Die Rangliste: Aufgaben fuer Algo Quest Lab (Sortier-/Suchschritte per Skript + Java-LSG geprueft)."""
import itertools, random
from lib import *
from algos import *

A = []
LEVELS = []


def J(main, extra=''):
    return run(2, main, extra)


def fs(a):
    return ', '.join(str(x) for x in a)


SEL_CODE = '''public void selectionSort() {
    for (int i = 0; i < anzahl - 1; i++) {
        int maxIndex = i;
        for (int j = i + 1; j < anzahl; j++) {
            if (besser(eintraege[j], eintraege[maxIndex])) {
                maxIndex = j;
            }
        }
        if (maxIndex != i) {
            vertausche(i, maxIndex);
        }
    }
}'''
INS_CODE = '''public void insertionSort() {
    for (int i = 1; i < anzahl; i++) {
        int j = i;
        while (j > 0 && besser(eintraege[j], eintraege[j - 1])) {
            vertausche(j, j - 1);
            j--;
        }
    }
}'''
BUB_CODE = '''public void bubbleSort() {
    boolean getauscht = true;
    int durchlauf = 0;
    while (getauscht) {
        getauscht = false;
        for (int j = 0; j < anzahl - 1 - durchlauf; j++) {
            if (besser(eintraege[j + 1], eintraege[j])) {
                vertausche(j, j + 1);
                getauscht = true;
            }
        }
        durchlauf++;
    }
}'''
BESSER = hinweis('`besser(a, b)` liefert wahr, wenn `a` **mehr** Punkte hat (strikt `>`), und zählt einen Vergleich. '
                 'Sortiert wird **absteigend** – Platz 1 (meiste Punkte) an Index 0.')
TAUSCH_HINW = text('Wähle nacheinander die beiden Indizes jeder Vertauschung, genau in der Reihenfolge, in der das Verfahren '
                   'tauscht. Wenn keine Vertauschung mehr folgt, drücke „fertig".')


def swaps_text(p, start):
    a = list(start); teile = []
    for i, j in p['swaps']:
        a[i], a[j] = a[j], a[i]
        teile.append(f'({i}, {j}) → {fs(a)}')
    return ' · '.join(teile) if teile else 'keine'


# =====================================================================
# LEVEL 2.1 – Standardbausteine und lineare Suche (DS 13)
# =====================================================================
L = 'W2-L1'

# ---------- 01 Ausdruecke
ausdr = [('g1', '9 / 4'), ('g2', '(double) 9 / 4'), ('g3', '(double) (9 / 4)'), ('g4', '9 / 4.0'), ('g5', '9 % 4')]
out = J('\n'.join(f'println({x});' for _, x in ausdr))
check(out == ['2', '2.25', '2.0', '2.25', '1'], 'W2-L1-01 Ausdruecke per Java: 2 / 2.25 / 2.0 / 2.25 / 1')
A.append(aufgabe(
    f'{L}-01', 'Ganz oder Komma?', 1, 'Datentypen und Ausdrücke', ['P4'],
    [text('Gib an, was `println(…)` für jeden Ausdruck ausgibt – genau so, wie es auf der Konsole erscheint '
          '(Kommazahlen mit Punkt, z. B. `3.0`).'),
     tabelle(['Ausdruck', 'Ausgabe'], [[f'`{x}`', f'[[{g}]]'] for g, x in ausdr])],
    gaps(**{g: txt('code', 8) for g, _ in ausdr}), {g: zahlvarianten(v) for (g, _), v in zip(ausdr, out)},
    ['Ganzzahl / Ganzzahl rechnet ganzzahlig. Der Cast wirkt auf das, was direkt dahinter steht.'],
    '`9 / 4` sind zwei Ganzzahlen → ganzzahlige Division **2**. `(double) 9 / 4`: erst wird 9 zu 9.0, dann 9.0 / 4 = '
    '**2.25**. `(double) (9 / 4)`: erst 9 / 4 = 2, dann zu **2.0** – zu spät gecastet (P4)! `9 / 4.0` → **2.25**. '
    '`9 % 4` ist der Rest **1**. Genau diese Falle steckt im Baustein Durchschnitt.'))

# ---------- 02 match Bausteine
A.append(aufgabe(
    f'{L}-02', 'Welcher Baustein ist das?', 1, 'Funktionsweise erläutern', [],
    [text('Ordne jedes Code-Fragment aus der Klasse `Rangliste` dem Standardbaustein zu.')],
    match([('e1', '`int z = 0;` … `if (eintraege[i].getPunkte() > grenze) { z++; }` … `return z;`'),
           ('e2', '`int pos = 0;` … `if (eintraege[i].getZeit() < eintraege[pos].getZeit()) { pos = i; }` … `return pos;`'),
           ('e3', '`if (eintraege[i].getName().equals(name)) { return i; }` … nach der Schleife `return -1;`'),
           ('e4', '`for (int j = i + 1; j < anzahl; j++)` … `if (…equals(…)) { return true; }`'),
           ('e5', '`summe = summe + eintraege[i].getPunkte();` … `return (double) summe / anzahl;`')],
          [('z', 'Zählen'), ('m', 'Minimum/Maximum mit Index'), ('s', 'lineare Suche (erstes Vorkommen)'),
           ('d', 'Duplikate (jeder mit jedem)'), ('a', 'Durchschnitt')]),
    {'e1': 'z', 'e2': 'm', 'e3': 's', 'e4': 'd', 'e5': 'a'},
    ['Achte auf die Startwerte und darauf, was zurückgegeben wird.'],
    'Zählen: Zähler startet bei 0, `++` bei jedem Treffer. Minimum/Maximum: Rekordhalter = erster Eintrag (Index 0), '
    'wird bei einem besseren ersetzt. Lineare Suche: beim ersten Treffer sofort `return i`, −1 erst **nach** der Schleife. '
    'Duplikate: zwei Schleifen, die innere ab `i + 1`. Durchschnitt: Summe, dann Kommazahl-Division.'))

# ---------- 03 Trace besterEintrag
daten3 = [('Nox', 640), ('Pia', 910), ('Rex', 1210), ('Sun', 880), ('Taj', 1210)]
instr = '''class TB {
  static Eintrag besterEintrag(Eintrag[] eintraege, int anzahl) {
    if (anzahl == 0) { return null; }
    Eintrag bester = eintraege[0];
    for (int i = 1; i < anzahl; i++) {
      boolean b = eintraege[i].getPunkte() > bester.getPunkte();
      if (b) { bester = eintraege[i]; }
      println(i + ";" + b + ";" + bester.getName());
    }
    return bester;
  }
}'''
arr = 'Eintrag[] e = new Eintrag[8];' + ''.join(f' e[{i}] = new Eintrag("{n}", {p}, 100);' for i, (n, p) in enumerate(daten3))
lsg = 'Rangliste r = new Rangliste(8);' + ''.join(f' r.hinzufuegen(new Eintrag("{n}", {p}, 100));' for n, p in daten3)
out = J(arr + f' println(TB.besterEintrag(e, {len(daten3)}).getName()); ' + lsg + ' println(r.besterEintrag().getName());', instr)
check(out[-1] == out[-2] == 'Rex', 'W2-L1-03 besterEintrag: instrumentierte Kopie = LSG = Rex')
rows = [r.split(';') for r in out[:-2]]
names = [n for n, _ in daten3]
zeilen = [['–', '–', '–', 'Nox']]
loes, felder = {}, {}
for r in rows:
    i = r[0]
    zeilen.append([i, str(daten3[int(i)][1]), f'[[v{i}]]', f'[[b{i}]]'])
    loes[f'v{i}'] = ['wahr' if r[1] == 'true' else 'falsch']; felder[f'v{i}'] = auswahl(['wahr', 'falsch'])
    loes[f'b{i}'] = [r[2]]; felder[f'b{i}'] = auswahl(names)
loes['r'] = [out[-1]]; felder['r'] = auswahl(names)
A.append(aufgabe(
    f'{L}-03', 'Wer führt die Rangliste an?', 2, 'Tracetabelle', ['P8'],
    [text('Die Rangliste enthält (Index 0 bis 4): ' + ', '.join(f'{n} {p}' for n, p in daten3) + ' Punkte.'),
     code('''public Eintrag besterEintrag() {
    if (anzahl == 0) {
        return null;
    }
    Eintrag bester = eintraege[0];
    for (int i = 1; i < anzahl; i++) {
        if (eintraege[i].getPunkte() > bester.getPunkte()) {
            bester = eintraege[i];
        }
    }
    return bester;
}'''),
     tabelle(['i', 'eintraege[i].getPunkte()', 'getPunkte() > bester.getPunkte()', 'bester'], zeilen),
     text('Rückgabe: [[r]]')],
    gaps(**felder), loes, ['Bei Gleichstand ist `>` falsch – der erste Rekordhalter bleibt.'],
    'Start: Nox. i = 1: 910 > 640 → Pia. i = 2: 1210 > 910 → Rex. i = 3: 880 > 1210 falsch. i = 4: 1210 > 1210 **falsch** → '
    'Rex bleibt. Rückgabe **Rex** – bei Gleichstand der erste. Mit `>=` käme Taj heraus.'))

# ---------- 04 Bug-Hunt durchschnitt
code04 = '''public double durchschnitt() {
    int summe = 0;
    for (int i = 0; i < anzahl; i++) {
        summe = summe + eintraege[i].getPunkte();
    }
    return summe / anzahl;
}'''
stub = 'class RLD { Eintrag[] eintraege = new Eintrag[5]; int anzahl = 0;\n void add(int p) { eintraege[anzahl] = new Eintrag("X", p, 0); anzahl++; }\n'
out = J('RLD r = new RLD(); r.add(700); r.add(800); r.add(850); println(r.durchschnitt());', stub + code04 + '\n}')
check(out == ['783.0'], 'W2-L1-04 fehlerhafter Durchschnitt liefert 783.0')
o, e = java(2, 'RLD r = new RLD(); println(r.durchschnitt());', stub + code04 + '\n}')
check('ArithmeticException' in e, 'W2-L1-04 Originalcode bei leerer Liste: ArithmeticException (int / 0)')
v04 = ['return (double) summe / anzahl;', 'return summe / (double) anzahl;', 'return 1.0 * summe / anzahl;',
       'return summe * 1.0 / anzahl;', 'return (double) summe / (double) anzahl;', 'return summe / (anzahl * 1.0);']
for v in v04:
    c = code04.replace('    return summe / anzahl;', '    ' + v)
    out = J('RLD r = new RLD(); println(r.durchschnitt()); r.add(700); r.add(800); r.add(850); println(r.durchschnitt());', stub + c + '\n}')
    check(out == ['NaN', '783.3333333333334'], f'W2-L1-04 Korrektur "{v}" -> 783.33..., leere Liste NaN')
A.append(aufgabe(
    f'{L}-04', 'Der abgerundete Durchschnitt', 2, 'Fehler im Java-Code', ['P4'],
    [text('Für eine Rangliste mit 700, 800 und 850 Punkten liefert `durchschnitt()` den Wert `783.0` statt `783.33…`.'),
     code(code04),
     text('**a)** Markiere die fehlerhafte Zeile. **b)** Korrigierte Zeile: [[g1]]'),
     text('**c)** Mit deiner Korrektur wird `durchschnitt()` für eine **leere** Rangliste aufgerufen. Was passiert? [[g2]]')],
    [lines(1, 1), gaps(g1=txt('code', 34), g2=auswahl(['Ergebnis 0.0', 'Ergebnis NaN („keine Zahl") – die Leer-Abfrage fehlt',
                                                       'ArithmeticException (Division durch 0)', 'Ergebnis −1']))],
    [{'zeilen': [6]}, {'g1': varianten(*v04), 'g2': ['Ergebnis NaN („keine Zahl") – die Leer-Abfrage fehlt']}],
    ['Welchen Typ haben `summe` und `anzahl`?'],
    'Zeile 6: `summe / anzahl` sind zwei Ganzzahlen → ganzzahlige Division 2350 / 3 = 783, erst danach wird daraus 783.0 '
    '(P4). Richtig: `return (double) summe / anzahl;` – der Cast muss **vor** der Division wirken. Für die leere Liste '
    'rechnet Java dann 0.0 / 0 = **NaN** – laut Auftrag soll aber 0.0 kommen. Darum gehört an den Anfang '
    '`if (anzahl == 0) { return 0.0; }`. (Der Originalcode bricht bei leerer Liste mit einer ArithmeticException ab.)'))

# ---------- 05 Bausteine anwenden
daten5 = [('Nox', 640), ('Pia', 910), ('Rex', 1210), ('Sun', 880), ('Taj', 1210), ('Uma', 450)]
calls = [('g1', 'r.anzahlUeber(880)'), ('g2', 'r.anzahlUeber(1210)'), ('g3', 'r.indexVon("Taj")'), ('g4', 'r.indexVon("taj")'),
         ('g5', 'r.hoechstePunktzahl()'), ('g6', 'r.getEintrag(6) == null')]
out = J('Rangliste r = new Rangliste(8);' + ''.join(f' r.hinzufuegen(new Eintrag("{n}", {p}, 100));' for n, p in daten5)
        + ''.join(f' println({c});' for _, c in calls))
check(out == ['3', '0', '4', '-1', '1210', 'true'], 'W2-L1-05 Bausteine auf LSG-Rangliste: 3/0/4/-1/1210/true')
A.append(aufgabe(
    f'{L}-05', 'Die Späher im Einsatz', 1, 'Sortieren und Suchen', ['P5'],
    [text('Die Rangliste `r` (Kapazität 8) enthält (Index 0 bis 5): ' + ', '.join(f'{n} {p}' for n, p in daten5) +
          ' Punkte. Alle Bausteine sind wie in Level 2.1 implementiert (`anzahlUeber` zählt echt größer, `indexVon` '
          'vergleicht mit `equals`, `getEintrag` liefert bei ungültigem Index null).'),
     tabelle(['Aufruf', 'Ergebnis'], [[f'`{c}`', f'[[{g}]]'] for g, c in calls])],
    gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=zahl(), g5=zahl(), g6=auswahl(WF)),
    {g: [v] for (g, _), v in zip(calls, out)},
    ['`equals` unterscheidet Groß- und Kleinschreibung.'],
    '`anzahlUeber(880)` zählt 910, 1210, 1210 → **3** (880 selbst ist nicht *größer*). Über 1210 liegt niemand → **0**. '
    'Taj steht an Index **4**; "taj" mit kleinem t kommt nicht vor → **−1** (equals beachtet Groß-/Kleinschreibung). '
    'Maximum **1210**. Index 6 ist nicht belegt (anzahl = 6) → `getEintrag(6)` liefert null → **true**.'))

# ---------- 06 Trace Doppelschleife
daten6 = [520, 830, 610, 830, 400]
instr = '''class TD {
  static boolean hatGleichePunkte(int[] p, int anzahl) {
    int nr = 0;
    for (int i = 0; i < anzahl - 1; i++) {
      for (int j = i + 1; j < anzahl; j++) {
        nr++;
        boolean g = p[i] == p[j];
        println(nr + ";" + i + ";" + j + ";" + g);
        if (g) { return true; }
      }
    }
    return false;
  }
}'''
out = J('println(TD.hatGleichePunkte(new int[]{' + fs(daten6) + '}, 5)); println("X"); println(TD.hatGleichePunkte(new int[]{1, 2, 3, 4, 5, 6}, 6));', instr)
k = out.index('X')
rows = [r.split(';') for r in out[:k - 1]]
ret = out[k - 1]
n6 = len(out[k + 1:-1])
check(ret == 'true' and len(rows) == 6 and n6 == 15, 'W2-L1-06 hatGleichePunkte: true nach 6 Vergleichen; n = 6 ohne Gleiche: 15 Vergleiche')
zeilen, loes, felder = [], {}, {}
for r in rows:
    nr = r[0]
    zeilen.append([nr, f'[[i{nr}]]', f'[[j{nr}]]', f'[[q{nr}]]'])
    loes[f'i{nr}'] = [r[1]]; loes[f'j{nr}'] = [r[2]]; loes[f'q{nr}'] = ['wahr' if r[3] == 'true' else 'falsch']
    felder[f'i{nr}'] = zahl(); felder[f'j{nr}'] = zahl(); felder[f'q{nr}'] = auswahl(['wahr', 'falsch'])
loes['r'] = [ret]; felder['r'] = auswahl(WF)
loes['n'] = [str(n6)]; felder['n'] = zahl()
A.append(aufgabe(
    f'{L}-06', 'Jeder gegen jeden', 3, 'Tracetabelle', ['P8'],
    [text('`hatGleichePunkte()` prüft, ob zwei Einträge dieselbe Punktzahl haben. Punkte (Index 0 bis 4): ' + fs(daten6) + '.'),
     code('''public boolean hatGleichePunkte() {
    for (int i = 0; i < anzahl - 1; i++) {
        for (int j = i + 1; j < anzahl; j++) {
            if (eintraege[i].getPunkte() == eintraege[j].getPunkte()) {
                return true;
            }
        }
    }
    return false;
}'''),
     text('Trage jeden Vergleich in einer eigenen Zeile ein.'),
     tabelle(['Vergleich Nr.', 'i', 'j', 'gleich?'], zeilen),
     text('Rückgabe: [[r]] · Bei 6 Einträgen **ohne** gleiche Punkte gäbe es [[n]] Vergleiche.')],
    gaps(**felder), loes, ['Die innere Schleife beginnt bei `i + 1`.', 'Nach `return true` ist sofort Schluss.'],
    'Paare (0,1), (0,2), (0,3), (0,4), (1,2) sind verschieden; beim 6. Vergleich (1,3) sind 830 und 830 gleich → sofort '
    '`return true`. Ohne Treffer prüft die Methode alle Paare i < j: bei 6 Einträgen 5 + 4 + 3 + 2 + 1 = **15** = 6 · 5 / 2. '
    'Allgemein n(n − 1)/2 – die Formel begegnet dir beim Sortieren wieder.'))

# ---------- 07 Parsons indexVon
teile = [('a', 'public int indexVon(String name) {'), ('b', '    for (int i = 0; i < anzahl; i++) {'),
         ('c', '        if (eintraege[i].getName().equals(name)) {'), ('d', '            return i;'), ('e', '        }'),
         ('f', '    }'), ('g', '    return -1;'), ('h', '}'),
         ('x', '        if (eintraege[i].getName() == name) {'), ('y', '    for (int i = 0; i <= anzahl; i++) {'),
         ('z', '        } else { return -1; }')]
T = dict(teile)
reih = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
stub = 'class RLI { Eintrag[] eintraege = new Eintrag[5]; int anzahl = 0;\n void add(String n) { eintraege[anzahl] = new Eintrag(n, 1, 0); anzahl++; }\n'
for r in reih:
    out = J('RLI r = new RLI(); println(r.indexVon("A")); r.add("Nox"); r.add("Pia"); r.add("Pia"); println(r.indexVon(new String("Pia"))); println(r.indexVon("Rex"));',
            stub + '\n'.join(T[k] for k in r) + '\n}')
    check(out == ['-1', '1', '-1'], 'W2-L1-07 Parsons indexVon: leer -1, erstes Vorkommen 1, fehlt -1')
A.append(aufgabe(
    f'{L}-07', 'Puzzle: Steht Dorn schon drin?', 3, 'Methode implementieren', ['P5', 'P6'],
    [text('Setze `indexVon(name: Zeichenkette): Ganzzahl` zusammen: Index des **ersten** Eintrags mit diesem Namen, sonst −1. '
          'Nicht alle Teile werden gebraucht.')],
    order(teile), {'reihenfolgen': reih},
    ['Wann steht fest, dass der Name nicht vorkommt?'],
    'Lineare Suche: über die belegten Plätze (`i < anzahl`, nicht `<=`, P6), Namen mit `equals` (P5), beim ersten Treffer '
    'sofort `return i`. `return -1` steht **nach** der Schleife – ein `else { return -1; }` würde die Suche schon nach dem '
    'ersten Eintrag abbrechen.'))

# ---------- 08 Struktogramm-Luecken anzahlUeber
sg_loes = {'g1': ['0'], 'g2': ['anzahl − 1'], 'g3': ['>'], 'g4': ['zaehler + 1', '1 + zaehler'], 'g5': ['zaehler']}
probe = [700, 1200, 950, 300]
py = 0
for p in probe:
    if p > 900:
        py = py + 1
out = J('Rangliste r = new Rangliste(5);' + ''.join(f' r.hinzufuegen(new Eintrag("X", {p}, 1));' for p in probe) + ' println(r.anzahlUeber(900));')
check(out == [str(py)], 'W2-L1-08 Struktogramm mit Loesung (Python-Interpretation) = LSG anzahlUeber')
A.append(aufgabe(
    f'{L}-08', 'Vom Code zum Struktogramm', 2, 'Code ↔ Struktogramm', ['P9'],
    [code('''public int anzahlUeber(int grenze) {
    int zaehler = 0;
    for (int i = 0; i < anzahl; i++) {
        if (eintraege[i].getPunkte() > grenze) {
            zaehler++;
        }
    }
    return zaehler;
}'''),
     text('Vervollständige das Struktogramm nach EH § 5.'),
     struktogramm('anzahlUeber(grenze: Ganzzahl): Ganzzahl',
                  [{'anw': 'zaehler ← [[g1]]'},
                   {'zaehle': 'i von 0 bis [[g2]]', 'rumpf': [
                       {'wenn': 'eintraege[i].getPunkte() [[g3]] grenze', 'dann': [{'anw': 'zaehler ← [[g4]]'}], 'sonst': []}]},
                   {'gib': '[[g5]]'}])],
    gaps(g1=txt('code', 6), g2=auswahl(['anzahl', 'anzahl − 1', 'eintraege.length', 'Länge von eintraege − 1']),
         g3=auswahl(['>', '≥', '<', '=']), g4=txt('code', 14), g5=auswahl(['zaehler', 'anzahl', 'i', 'grenze'])),
    sg_loes, ['`zaehler++` schreibt man im Struktogramm als Zuweisung mit ←.'],
    'Im Struktogramm gibt es kein `++`: `zaehler ← zaehler + 1` (P9). Die Zählschleife läuft „von 0 bis anzahl − 1" – '
    'beide Grenzen **inklusive**, das entspricht `i < anzahl`. Am Ende „gib zaehler zurück".'))

LEVELS.append({"id": L, "nr": "2.1", "titel": "Die Highscore-Liste – Standardbausteine und lineare Suche", "ds": [13],
               "ab": "AB W2·1 Standardbausteine und Suchen",
               "ide": "AQ_W2_L2_Rangliste_Geruest.txt – Level 2.1 (Klasse Rangliste, Testklasse L21StandardTest)",
               "intro": [text('Standardbausteine auf einer Reihung von Objekten mit Füllstand `anzahl`: Zählen, Maximum/Minimum, '
                              'lineare Suche (erstes Vorkommen, sonst −1), Duplikate (jeder mit jedem), Durchschnitt.'),
                         hinweis('**Achtung Abi:** Rekord mit dem ersten Eintrag starten (nicht mit 0) · Schleifen bis '
                                 '`anzahl − 1` · `return -1` nach der Schleife · `equals` statt `==` · Kommazahl-Division mit Cast.')],
               "aufgaben": [a['id'] for a in A if a['id'].startswith(L + '-')]})

# =====================================================================
# LEVEL 2.2 – Sortieren (DS 14)
# =====================================================================
L = 'W2-L2'

for nr, kind, start, stufe, titel, code_, fallen in [
        ('01', 'selection', [40, 70, 20, 90, 60], 1, 'Auswahl der Besten', SEL_CODE, []),
        ('02', 'insertion', [30, 50, 10, 60, 40], 2, 'Einsortieren wie beim Kartenspiel', INS_CODE, []),
        ('03', 'bubble', [60, 20, 50, 80, 30], 2, 'Die Blasen steigen', BUB_CODE, [])]:
    p = sort_verified(kind, start, f'{L}-{nr}')
    nm = {'selection': 'Selectionsort', 'insertion': 'Insertionsort', 'bubble': 'Bubblesort mit Abbruch'}[kind]
    erkl = {'selection': 'Selectionsort sucht im Rest ab i den besten Eintrag und tauscht ihn nach vorn – aber nur, wenn er nicht '
                         'schon an Position i steht.',
            'insertion': 'Insertionsort lässt jeden Eintrag durch Nachbartausche nach links wandern, solange er besser als sein '
                         'linker Nachbar ist.',
            'bubble': 'Bubblesort vergleicht Nachbarn und tauscht, wenn der rechte besser ist; nach jedem Durchlauf ist hinten ein '
                      'Platz mehr fertig, ohne Vertauschung im Durchlauf endet das Verfahren.'}[kind]
    A.append(aufgabe(
        f'{L}-{nr}', f'{titel}: {nm.split()[0]}', stufe, 'Sortieren und Suchen', fallen,
        [text(f'Sortiere die Punkte mit **{nm}** genau nach dieser Methode der Rangliste:'), code(code_), BESSER,
         reihung(start), TAUSCH_HINW],
        array_tausch(start), {'tausche': p['swaps']},
        ['Notiere dir nebenher den Zustand nach jedem Durchlauf der äußeren Schleife.'],
        f'{erkl} Vertauschungen: {swaps_text(p, start)}. Insgesamt {len(p["swaps"])} Vertauschungen und {p["comps"]} Aufrufe '
        f'von `besser`.'))

# ---------- 04 Verfahren erkennen
daten4 = [25, 45, 15, 55, 35]
ps = {k: ALG[k](daten4) for k in ALG}
for k in ALG:
    sort_verified(k, daten4, f'{L}-04')
gezeigt = 'bubble'
check(all(ps[gezeigt]['states'][0] != ps[k]['states'][0] for k in ALG if k != gezeigt),
      'W2-L2-04 Zustand nach dem 1. Durchlauf unterscheidet Bubblesort eindeutig von Selection-/Insertionsort')
st = ps[gezeigt]['states']
A.append(aufgabe(
    f'{L}-04', 'Wer hat hier sortiert?', 1, 'Funktionsweise erläutern', [],
    [text('Eine Rangliste mit den Punkten ' + fs(daten4) + ' wird absteigend sortiert. Die Tabelle zeigt den Zustand nach jedem '
          'Durchlauf der äußeren Schleife.'),
     tabelle(['nach …', 'Index 0', 'Index 1', 'Index 2', 'Index 3', 'Index 4'],
             [['Start'] + daten4] + [[f'Durchlauf {i + 1}'] + s for i, s in enumerate(st)]),
     text('Welches Verfahren war das?')],
    choice([('s', 'Selectionsort'), ('i', 'Insertionsort'), ('b', 'Bubblesort mit Abbruch')]), {'richtig': ['b']},
    ['Wo steht nach dem ersten Durchlauf der kleinste Wert?'],
    f'Nach dem 1. Durchlauf steht der **schlechteste** Wert (15) ganz hinten – typisch für Bubblesort: Nachbarn werden '
    f'verglichen, der Schlechteste „sinkt" nach hinten. Selectionsort hätte zuerst den Besten nach vorn getauscht '
    f'({fs(ps["selection"]["states"][0])}), Insertionsort hätte nur die ersten beiden geordnet ({fs(ps["insertion"]["states"][0])}).'))

# ---------- 05 Insertionsort-Trace mit Zaehlern
daten5 = [35, 75, 55, 95]
p = sort_verified('insertion', daten5, f'{L}-05')
zeilen, loes, felder = [['Start'] + daten5 + ['0', '0']], {}, {}
for r, (s, (c, t)) in enumerate(zip(p['states'], p['rows']), start=1):
    z = [f'i = {r}']
    for idx, v in enumerate(s):
        g = f'w{r}{idx}'; z.append(f'[[{g}]]'); loes[g] = [str(v)]; felder[g] = zahl()
    for g, v in ((f'c{r}', c), (f't{r}', t)):
        z.append(f'[[{g}]]'); loes[g] = [str(v)]; felder[g] = zahl()
    zeilen.append(z)
A.append(aufgabe(
    f'{L}-05', 'Tracetabelle mit Strichliste', 2, 'Tracetabelle', ['P8'],
    [text('`insertionSort()` (siehe unten) sortiert die Punkte ' + fs(daten5) + ' absteigend. Gib den Zustand nach jedem Durchlauf '
          'der äußeren Schleife und die **fortlaufenden Summen** der Aufrufe von `besser` und `vertausche` an.'),
     code(INS_CODE), BESSER,
     tabelle(['nach …', 'Index 0', 'Index 1', 'Index 2', 'Index 3', 'Vergleiche (Summe)', 'Vertauschungen (Summe)'], zeilen)],
    gaps(**felder), loes,
    ['Ist `j > 0` falsch, wird `besser` gar nicht mehr aufgerufen (Kurzschluss von &&).'],
    f'i = 1: 75 > 35 → tauschen, danach j = 0 → Schleifenende ohne weiteren Vergleich (1 Vergleich). i = 2: 55 > 35 tauschen, '
    f'55 > 75 nein (2 Vergleiche). i = 3: 95 wandert bis ganz nach vorn (3 Vergleiche, 3 Tausche). Summen: '
    f'{p["comps"]} Vergleiche, {len(p["swaps"])} Vertauschungen.'))

# ---------- 06 Lueckencode bubbleSort
lc = '''public void bubbleSort() {
    boolean getauscht = [[g1]];
    int durchlauf = 0;
    while ([[g2]]) {
        getauscht = [[g3]];
        for (int j = 0; j < [[g4]]; j++) {
            if (besser([[g5]], eintraege[j])) {
                vertausche(j, j + 1);
                getauscht = [[g6]];
            }
        }
        durchlauf++;
    }
}'''
loes6 = {'g1': ['true'], 'g2': ['getauscht', 'getauscht == true'], 'g3': ['false'],
         'g4': ['anzahl - 1 - durchlauf', 'anzahl - durchlauf - 1', '(anzahl - 1) - durchlauf'],
         'g5': ['eintraege[j + 1]'], 'g6': ['true']}
RLB = '''class RLB {
  private Eintrag[] eintraege; private int anzahl; private int vergleiche; private int vertauschungen;
  public RLB(int k) { eintraege = new Eintrag[k]; }
  public void add(int p) { eintraege[anzahl] = new Eintrag("X", p, 0); anzahl++; }
  private boolean besser(Eintrag a, Eintrag b) { vergleiche++; return a.getPunkte() > b.getPunkte(); }
  public void vertausche(int i, int j) { Eintrag h = eintraege[i]; eintraege[i] = eintraege[j]; eintraege[j] = h; vertauschungen++; }
  public String info() { String s = vergleiche + "/" + vertauschungen + ":"; for (int i = 0; i < anzahl; i++) s += eintraege[i].getPunkte() + ","; return s; }
'''
tests = [[60, 20, 50, 80, 30], [90, 70, 50, 30], [10, 20, 30, 40, 50, 60], [5]]
for g2 in ['getauscht', 'getauscht == true']:
    for g4 in ['anzahl - 1 - durchlauf', 'anzahl - durchlauf - 1', '(anzahl - 1) - durchlauf']:
        m = lc.replace('[[g1]]', 'true').replace('[[g2]]', g2).replace('[[g3]]', 'false').replace('[[g4]]', g4) \
            .replace('[[g5]]', 'eintraege[j + 1]').replace('[[g6]]', 'true')
        for t in tests:
            out = J(f'RLB r = new RLB({len(t)});' + ''.join(f' r.add({v});' for v in t) + ' r.bubbleSort(); println(r.info());', RLB + m + '\n}')
            pb = bubble(t)
            check(out == [f'{pb["comps"]}/{len(pb["swaps"])}:' + ''.join(f'{v},' for v in pb['final'])],
                  f'W2-L2-06 Lueckencode ({g2}; {g4}) auf {t} = Skript-Bubblesort')
A.append(aufgabe(
    f'{L}-06', 'Lückencode: Die Notbremse', 3, 'Lückencode', ['P6'],
    [text('Ergänze `bubbleSort()` der Rangliste (absteigend, mit Abbruch): Die innere Schleife wird nach jedem Durchlauf um 1 '
          'kürzer; blieb ein Durchlauf ohne Vertauschung, endet das Verfahren.'), code(lc), BESSER],
    gaps(g1=auswahl(WF), g2=txt('code', 18), g3=auswahl(WF), g4=txt('code', 24), g5=txt('code', 18), g6=auswahl(WF)), loes6,
    ['`getauscht` muss vor dem ersten Durchlauf so stehen, dass die Schleife überhaupt startet.',
     'Nach dem Durchlauf mit `durchlauf = d` sind hinten d + 1 Plätze fertig.'],
    '`getauscht` startet mit true, damit der erste Durchlauf stattfindet; zu Beginn jedes Durchlaufs wird es auf false '
    'gesetzt und bei jeder Vertauschung auf true. Die innere Schleife läuft bis `j < anzahl - 1 - durchlauf`: Sie '
    'vergleicht `eintraege[j + 1]` mit `eintraege[j]` – ohne `- 1` würde `j + 1` die belegten Plätze verlassen (P6), ohne '
    '`- durchlauf` würden fertige Plätze unnötig erneut verglichen.'))

# ---------- 07 Stabilitaet
namen7 = ['Ola', 'Ben', 'Ivo', 'Kim', 'Lu']
found = None
for b, k_, l in itertools.product([400, 750, 900, 1000], repeat=3):
    if len({b, k_, l}) < 3:
        continue
    werte = [600, b, 600, k_, l]
    ent = list(zip(namen7, werte))
    s = selection(ent, key=lambda e: e[1])['final']
    ns = [e[0] for e in s]
    if ns.index('Ivo') < ns.index('Ola'):
        found = werte
        break
werte7 = found
js = java_sort('selection', werte7, namen7)
ji = java_sort('insertion', werte7, namen7)
sel_n = [x[0] for x in js['final']]
ins_n = [x[0] for x in ji['final']]
check(sel_n.index('Ivo') < sel_n.index('Ola') and ins_n.index('Ola') < ins_n.index('Ivo'),
      f'W2-L2-07 Daten {werte7}: Selectionsort (Java-LSG) {sel_n} instabil, Insertionsort {ins_n} stabil')
ps7 = selection(list(zip(namen7, werte7)), key=lambda e: e[1])


def sel_schritte(p, start):
    a = list(start); t = []
    for i, j in p['swaps']:
        a[i], a[j] = a[j], a[i]
        t.append(f'Tausch ({i}, {j}) → ' + ', '.join(n for n, _ in a))
    return ' · '.join(t)


A.append(aufgabe(
    f'{L}-07', 'Gleichstand im Ziel', 3, 'Sortieren und Suchen', [],
    [text('Bei Punktgleichstand soll vorne stehen, wer die Punkte **zuerst** erreicht hat (kleinerer Index). Die Rangliste enthält:'),
     tabelle(['Index'] + [str(i) for i in range(5)], [['Eintrag'] + [f'{n} {w}' for n, w in zip(namen7, werte7)]]),
     text('Die Liste wird einmal mit `selectionSort()` und einmal (vom selben Start aus) mit `insertionSort()` sortiert '
          '(Methoden wie in Level 2.2).'),
     text('Index von Ola nach selectionSort: [[g1]] · Index von Ivo nach selectionSort: [[g2]]'),
     text('Index von Ola nach insertionSort: [[g3]] · Stabil gearbeitet hat hier: [[g4]]')],
    gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=auswahl(['nur Selectionsort', 'nur Insertionsort', 'beide', 'keines'])),
    {'g1': [str(sel_n.index('Ola'))], 'g2': [str(sel_n.index('Ivo'))], 'g3': [str(ins_n.index('Ola'))], 'g4': ['nur Insertionsort']},
    ['Verfolge bei Selectionsort jeden weiten Tausch: Wer wird dabei nach hinten geschoben?'],
    'Selectionsort: ' + sel_schritte(ps7, list(zip(namen7, werte7))) +
    f' – Ergebnis {", ".join(sel_n)}. Ein **weiter Tausch** schiebt Ola hinter Ivo, obwohl beide 600 Punkte haben → nicht '
    f'stabil. Insertionsort tauscht nur Nachbarn und nur bei *strikt* besser – gleich gute überholen sich nie: '
    f'{", ".join(ins_n)} → stabil.'))

# ---------- 08 match Merkmale
A.append(aufgabe(
    f'{L}-08', 'Steckbriefe der Verfahren', 1, 'Funktionsweise erläutern', [],
    [text('Ordne jedes Merkmal dem Sortierverfahren aus Level 2.2 zu.')],
    match([('e1', 'sucht im unsortierten Rest den besten Eintrag und tauscht ihn an den Anfang des Restes'),
           ('e2', 'lässt den nächsten Eintrag so lange nach links wandern, wie er besser als sein linker Nachbar ist'),
           ('e3', 'vergleicht in jedem Durchlauf benachbarte Einträge über den ganzen restlichen Bereich; der schlechteste sinkt nach hinten'),
           ('e4', 'braucht bei jeder Eingabe der Länge n genau n(n − 1)/2 Vergleiche'),
           ('e5', 'endet, sobald ein Durchlauf ohne Vertauschung blieb'),
           ('e6', 'vertauscht insgesamt höchstens n − 1-mal')],
          [('s', 'Selectionsort'), ('i', 'Insertionsort'), ('b', 'Bubblesort mit Abbruch')]),
    {'e1': 's', 'e2': 'i', 'e3': 'b', 'e4': 's', 'e5': 'b', 'e6': 's'}, [],
    'Selectionsort: Maximum-Auswahl im Rest, höchstens ein Tausch pro Durchlauf (≤ n − 1), die Vergleiche hängen nicht von '
    'den Daten ab: immer n(n − 1)/2. Insertionsort: Einfügen durch Nachbartausche nach links. Bubblesort: Nachbarvergleiche '
    'über den Rest, Abbruch nach einem Durchlauf ohne Vertauschung.'))

LEVELS.append({"id": L, "nr": "2.2", "titel": "Ordnung im Ranking – Selection-, Insertion-, Bubblesort", "ds": [14],
               "ab": "AB W2·2 Sortieren",
               "ide": "AQ_W2_L2_Rangliste_Geruest.txt – Level 2.2 (Sortieren, Testklasse L22SortierTest)",
               "intro": [text('Alle drei Verfahren bestehen nur aus **vergleichen** (`besser`) und **vertauschen** (`vertausche`). '
                              'Sortiert wird absteigend: Platz 1 an Index 0.'),
                         hinweis('**Erkennungsmerkmale:** Selectionsort sucht das Extremum und tauscht weit · Insertionsort lässt '
                                 'einen Eintrag nach links wandern · Bubblesort vergleicht nur Nachbarn, Abbruch ohne Vertauschung.')],
               "aufgaben": [a['id'] for a in A if a['id'].startswith(L + '-')]})

# =====================================================================
# LEVEL 2.3 – Effizienz und Sortier-Duell (DS 15)
# =====================================================================
L = 'W2-L3'

# ---------- 01 Selectionsort zaehlen
random.seed(15)
for n in (6, 12):
    w = random.sample(range(100, 2000), n)
    p = sort_verified('selection', w, f'{L}-01 (n = {n})')
    check(p['comps'] == n * (n - 1) // 2, f'W2-L3-01 Selectionsort n = {n}: {p["comps"]} = n(n-1)/2')
first = selection(random.sample(range(100, 2000), 6))
check(first['rows'][0][0] == 5 and first['rows'][-1][0] - first['rows'][-2][0] == 1, 'W2-L3-01 erster Durchlauf 5, letzter 1 Vergleich')
A.append(aufgabe(
    f'{L}-01', 'Zählen statt Stoppuhr', 1, 'Effizienz', [],
    [text('`selectionSort()` (Level 2.2) sortiert eine Rangliste mit **n = 6** Einträgen. Gib die Zahl der Aufrufe von '
          '`besser` an.'),
     text('im 1. Durchlauf der äußeren Schleife: [[g1]] · im letzten Durchlauf: [[g2]] · insgesamt: [[g3]]'),
     text('insgesamt bei n = 12: [[g4]]')],
    gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=zahl()), {'g1': ['5'], 'g2': ['1'], 'g3': ['15'], 'g4': ['66']},
    ['Im Durchlauf i vergleicht die innere Schleife j = i + 1 … n − 1.'],
    'Im 1. Durchlauf wird der beste Eintrag unter n Einträgen gesucht: n − 1 = 5 Vergleiche, im 2. Durchlauf 4, … im '
    'letzten 1. Zusammen 5 + 4 + 3 + 2 + 1 = 15 = n(n − 1)/2. Für n = 12: 12 · 11 / 2 = **66** – unabhängig davon, wie die '
    'Daten aussehen.'))

# ---------- 02 Insertionsort-Zaehltabelle
inputs = [[90, 70, 50, 30, 10], [10, 30, 50, 70, 90], [70, 90, 30, 50, 10]]
zeilen, loes, felder = [], {}, {}
for k, w in enumerate(inputs, start=1):
    pi = sort_verified('insertion', w, f'{L}-02')
    psel = sort_verified('selection', w, f'{L}-02')
    zeilen.append([fs(w), f'[[c{k}]]', f'[[t{k}]]', f'[[s{k}]]'])
    loes[f'c{k}'] = [str(pi['comps'])]; loes[f't{k}'] = [str(len(pi['swaps']))]; loes[f's{k}'] = [str(psel['comps'])]
    felder[f'c{k}'] = zahl(); felder[f't{k}'] = zahl(); felder[f's{k}'] = zahl()
check([loes['c1'][0], loes['t1'][0], loes['c2'][0], loes['t2'][0]] == ['4', '0', '10', '10'], 'W2-L3-02 bester/schlechtester Fall Insertionsort n = 5')
A.append(aufgabe(
    f'{L}-02', 'Zähl-Kata: drei Ausgangslagen', 2, 'Effizienz', [],
    [text('`insertionSort()` und `selectionSort()` (Level 2.2, absteigend, jeder Aufruf von `besser` zählt) sortieren drei '
          'Ranglisten mit je fünf Einträgen. Gib die Zählerstände am Ende an.'),
     tabelle(['Punkte (Index 0 bis 4)', 'Insertionsort: Vergleiche', 'Insertionsort: Vertauschungen', 'Selectionsort: Vergleiche'], zeilen)],
    gaps(**felder), loes, ['Insertionsort: Jeder Eintrag kostet mindestens einen Vergleich, außer er wandert bis Index 0.'],
    'Schon absteigend sortiert = **bester Fall** für Insertionsort: jeder Eintrag nur 1 Vergleich → n − 1 = 4, keine '
    'Vertauschung. Aufsteigend = **schlechtester Fall**: jeder wandert ganz nach vorn → 1 + 2 + 3 + 4 = 10 Vergleiche und '
    f'10 Vertauschungen. Gemischte Lage: {loes["c3"][0]} Vergleiche, {loes["t3"][0]} Vertauschungen. Selectionsort braucht '
    'immer 10 = 5 · 4 / 2.'))

# ---------- 03 Verdopplung Zeit
f_ = (2000 * 1999 / 2) / (1000 * 999 / 2)
check(abs(0.8 * f_ - 3.2) < 0.01, 'W2-L3-03 0,8 s * 4,002 = 3,2 s')
A.append(aufgabe(
    f'{L}-03', 'Doppelt so viele Spieler', 1, 'Effizienz', ['P10'],
    [text('Das Sortieren von 1000 Einträgen mit Selectionsort dauert auf dem Server 0,8 Sekunden. Wie lange dauert es '
          'ungefähr für 2000 Einträge?')],
    choice([('a', 'etwa 1,6 Sekunden'), ('b', 'etwa 3,2 Sekunden'), ('c', 'etwa 0,9 Sekunden'), ('d', 'etwa 6,4 Sekunden')]),
    {'richtig': ['b']}, ['Wie hängt die Zahl der Vergleiche von n ab?'],
    'Die Zahl der Vergleiche ist n(n − 1)/2, wächst also **quadratisch**: 2000 · 1999 / 2 ≈ 4 · (1000 · 999 / 2). '
    'Verdoppelt man n, vervierfacht sich der Aufwand ungefähr → 4 · 0,8 s ≈ **3,2 s**. Abitur-Formulierung: „Verdoppelt '
    'man n, so vervierfacht sich die Zahl der Vergleiche ungefähr, da sie quadratisch von n abhängt."'))

# ---------- 04 Bubblesort bester/schlechtester Fall
base = [10, 20, 30, 40, 50]
allc = [bubble(list(pm))['comps'] for pm in itertools.permutations(base)]
worst, best = max(allc), min(allc)
opts4 = [('a', [10, 20, 30, 40, 50]), ('b', [50, 40, 30, 20, 10]), ('c', [30, 50, 40, 20, 10]), ('d', [50, 10, 20, 30, 40])]
richtig4 = []
for k, w in opts4:
    p = sort_verified('bubble', w, f'{L}-04')
    if p['comps'] == worst:
        richtig4.append(k)
check(worst == 10 and best == 4 and richtig4 == ['a', 'd'], f'W2-L3-04 alle 120 Permutationen: max {worst}, min {best}; Hoechstzahl bei {richtig4}')
A.append(aufgabe(
    f'{L}-04', 'Der ungünstigste Fall', 3, 'Effizienz', [],
    [text('`bubbleSort()` mit Abbruch (Level 2.2) sortiert fünf Einträge absteigend.'), code(BUB_CODE),
     text('**a)** Höchstzahl der Aufrufe von `besser` bei n = 5: [[g1]] · Mindestzahl: [[g2]]'),
     text('**b)** Bei welchen Eingaben wird die Höchstzahl erreicht? Wähle alle passenden aus.')],
    [gaps(g1=zahl(), g2=zahl()), choice([(k, f'`{fs(w)}`') for k, w in opts4], mehrfach=True)],
    [{'g1': [str(worst)], 'g2': [str(best)]}, {'richtig': richtig4}],
    ['Wann braucht Bubblesort alle n − 1 Durchläufe?', 'Probiere 50, 10, 20, 30, 40 von Hand.'],
    'Ohne Abbruch wären es immer 4 + 3 + 2 + 1 = **10** Vergleiche; mehr geht nicht. Im besten Fall (schon sortiert) '
    'endet das Verfahren nach dem 1. Durchlauf: **4** = n − 1. Die Höchstzahl entsteht, wenn im 3. Durchlauf noch getauscht '
    'wird, sodass auch der 4. Durchlauf (1 Vergleich) stattfindet: Das gilt für die aufsteigende Eingabe – aber auch für 50, 10, 20, 30, 40, weil die 40 pro Durchlauf '
    'nur einen Platz nach vorn rücken kann (gute Einträge „steigen" langsam, schlechte sinken schnell). Die umgekehrte Eingabe 50, 40, … ist schon richtig sortiert (bester Fall).'))

# ---------- 05 Insertionsort Verdopplung
res = {}
for n in (100, 200):
    for fall, w in (('worst', list(range(1, n + 1))), ('best', list(range(n, 0, -1)))):
        j = java_sort('insertion', w)
        res[(n, fall)] = j['comps']
check(res == {(100, 'worst'): 4950, (100, 'best'): 99, (200, 'worst'): 19900, (200, 'best'): 199},
      'W2-L3-05 Insertionsort (Java-LSG): n=100 4950/99, n=200 19900/199')
A.append(aufgabe(
    f'{L}-05', 'Verdopplung im Highscore', 3, 'Effizienz', ['P10'],
    [text('`insertionSort()` (Level 2.2, absteigend) – gib die Zahl der Aufrufe von `besser` an (ganze Zahlen ohne Tausenderpunkte).'),
     tabelle(['n', 'schlechtester Fall', 'bester Fall'], [['100', '[[g1]]', '[[g2]]'], ['200', '[[g3]]', '[[g4]]']]),
     text('Verdoppelt man n, wächst die Zahl der Vergleiche im schlechtesten Fall ungefähr auf das [[g5]]-Fache, im besten '
          'Fall ungefähr auf das [[g6]]-Fache (ganze Zahlen).')],
    gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=zahl(), g5=zahl(), g6=zahl()),
    {'g1': ['4950'], 'g2': ['99'], 'g3': ['19900'], 'g4': ['199'], 'g5': ['4'], 'g6': ['2']},
    ['Schlechtester Fall: aufsteigend sortierte Eingabe – jeder Eintrag wandert ganz nach vorn.'],
    'Schlechtester Fall (aufsteigende Eingabe): 1 + 2 + … + (n − 1) = n(n − 1)/2 → 4950 bzw. 19 900, Faktor ≈ **4** '
    '(quadratisch). Bester Fall (schon sortiert): je Eintrag 1 Vergleich → n − 1 = 99 bzw. 199, Faktor ≈ **2** (linear). '
    'Im Abitur immer begründen, **welcher** Fall betrachtet wird (P10).'))

# ---------- 06 Bubblesort auf fast sortierten Daten
start6 = [90, 80, 50, 70, 60, 40]
p = sort_verified('bubble', start6, f'{L}-06')
A.append(aufgabe(
    f'{L}-06', 'Fast sortiert', 2, 'Sortieren und Suchen', [],
    [text('Die Rangliste ist nach einem Nachtrag **fast** sortiert. Führe `bubbleSort()` mit Abbruch aus (Methode siehe unten).'),
     code(BUB_CODE), BESSER, reihung(start6), TAUSCH_HINW,
     text('Wie viele Aufrufe von `besser` waren es insgesamt? [[g1]] · Wie viele Durchläufe der äußeren Schleife? [[g2]]')],
    [array_tausch(start6), gaps(g1=zahl(), g2=zahl())],
    [{'tausche': p['swaps']}, {'g1': [str(p['comps'])], 'g2': [str(len(p['states']))]}],
    ['Auch der Durchlauf, in dem nichts mehr getauscht wird, zählt mit.'],
    f'Vertauschungen: {swaps_text(p, start6)}. Durchläufe: {len(p["states"])} – der letzte stellt nur fest, dass nichts mehr zu '
    f'tun ist (Abbruch). Vergleiche: ' + ' + '.join(str(len(start6) - 1 - d) for d in range(len(p['states']))) +
    f' = {p["comps"]} statt 15 ohne Abbruch.'))

# ---------- 07 Duplikat-Pruefung zaehlen
def dup_count(n):
    c = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            c += 1
    return c
c1000, c2000 = dup_count(1000), dup_count(2000)
check(c1000 == 499500 and c2000 == 1999000, 'W2-L3-07 hatDoppelteNamen ohne Treffer: n=1000 499500, n=2000 1999000 (Schleifen gezaehlt)')
A.append(aufgabe(
    f'{L}-07', 'Der Doppelgänger-Detektor', 1, 'Effizienz', [],
    [text('`hatDoppelteNamen()` vergleicht jeden Eintrag mit jedem späteren (innere Schleife ab `i + 1`) und gibt beim ersten '
          'gleichen Namen sofort true zurück.'),
     text('Gib ganze Zahlen ohne Tausenderpunkte ein. Namensvergleiche bei 1000 Einträgen **ohne** doppelte Namen: [[g1]] · bei 2000 Einträgen ohne doppelte Namen: [[g2]] · '
          'bei 1000 Einträgen, wenn Index 0 und Index 1 denselben Namen haben: [[g3]]')],
    gaps(g1=zahl(), g2=zahl(), g3=zahl()), {'g1': [str(c1000)], 'g2': [str(c2000)], 'g3': ['1']},
    ['Wie viele Paare (i, j) mit i < j gibt es bei n Einträgen?'],
    'Ohne Treffer werden alle Paare geprüft: n(n − 1)/2 → 1000 · 999 / 2 = **499 500** und 2000 · 1999 / 2 = **1 999 000** '
    '(etwa das Vierfache). Steht das Doppel ganz vorn, ist schon nach dem **1.** Vergleich Schluss – der beste Fall.'))

# ---------- 08 Aussagen
def bubble_ohne(w):
    a = list(w); c = 0; n = len(a)
    for d in range(n - 1):
        for j in range(n - 1 - d):
            c += 1
            if a[j + 1] > a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return c
n = 7
sortiert = list(range(n, 0, -1))
check(insertion(sortiert)['comps'] == n - 1 and bubble(sortiert)['comps'] == n - 1 and bubble_ohne(sortiert) == n * (n - 1) // 2
      and len({selection(list(pm))['comps'] for pm in itertools.permutations(range(6))}) == 1,
      'W2-L3-08 Aussagen geprueft: Insertion/Bubble bester Fall n-1, Bubble ohne Abbruch n(n-1)/2, Selection konstant')
A.append(aufgabe(
    f'{L}-08', 'Abi-Sätze zur Effizienz', 2, 'Effizienz', ['P10'],
    [text('Welche Aussagen über die Verfahren aus Level 2.2 (n Einträge, gezählt werden Aufrufe von `besser`) sind **richtig**?')],
    choice([('a', 'Verdoppelt man n, so vervierfacht sich die Zahl der Vergleiche von Selectionsort ungefähr, da sie quadratisch von n abhängt.'),
            ('b', 'Insertionsort braucht bei einer schon sortierten Liste n(n − 1)/2 Vergleiche.'),
            ('c', 'Selectionsort braucht für jede Eingabe der Länge n gleich viele Vergleiche.'),
            ('d', 'Die Laufzeit in Sekunden ist ein gutes Maß für den Aufwand eines Algorithmus.'),
            ('e', 'Bubblesort mit Abbruch braucht im besten Fall n − 1 Vergleiche.'),
            ('f', 'Bubblesort **ohne** Abbruch braucht im besten Fall ebenfalls nur n − 1 Vergleiche.')], mehrfach=True),
    {'richtig': ['a', 'c', 'e']}, [],
    'Richtig: a, c, e. Insertionsort braucht auf sortierten Daten nur n − 1 Vergleiche (b falsch). Sekunden hängen von '
    'Rechner, Browser und Tempo-Regler ab – gezählt werden Grundoperationen (d falsch). Ohne Abbruch läuft Bubblesort immer '
    'alle Durchläufe: n(n − 1)/2 Vergleiche (f falsch).'))

LEVELS.append({"id": L, "nr": "2.3", "titel": "Das Sortier-Duell – Effizienz durch Zählen", "ds": [15],
               "ab": "AB W2·3 Effizienz und binäre Suche – Teil A (Aufgaben 0–3)",
               "ide": "AQ_W2_SortierDuell_Geruest.txt – Sortier-Duell (MeinSortierer.duellSort, Duell.starten)",
               "intro": [text('Aufwand misst man nicht in Sekunden, sondern durch **Zählen** von Vergleichen und Vertauschungen – '
                              'abhängig von n und vom Fall (bester, schlechtester, mittlerer).'),
                         hinweis('**Achtung Abi:** Selectionsort immer n(n − 1)/2 Vergleiche · Verdopplung von n → etwa vierfache '
                                 'Vergleiche (quadratisch) · schlechtesten Fall mit Eingabe angeben und begründen. Keine O-Notation nötig.')],
               "aufgaben": [a['id'] for a in A if a['id'].startswith(L + '-')]})

# =====================================================================
# LEVEL 2.4 – Binaere Suche (DS 16)
# =====================================================================
L = 'W2-L4'
BIN_CODE = '''public static int binaer(int[] r, int x) {
    int lo = 0;
    int hi = r.length - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (r[mid] == x) {
            return mid;
        } else if (r[mid] < x) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return -1;
}'''
KLICK_HINW = text('Klicke nacheinander die Indizes an, die das Verfahren als `mid` prüft (mid = (lo + hi) / 2, ganzzahlig).')

# ---------- 01 Klick-Suche (Treffer)
r1 = [4, 11, 17, 23, 30, 36, 42, 49, 57, 63, 70, 78, 85]
p1 = search_verified(r1, 57, f'{L}-01')
A.append(aufgabe(
    f'{L}-01', 'Halbieren statt Durchsuchen', 1, 'Sortieren und Suchen', [],
    [text('Die Reihung ist **aufsteigend** sortiert. Gesucht wird x = 57 mit der binären Suche:'), code(BIN_CODE), reihung(r1), KLICK_HINW],
    array_klick(r1), {'folge': p1['mids']},
    ['Erster Schritt: lo = 0, hi = 12 → mid = 6.'],
    'Trace: ' + ' · '.join(f'lo = {a}, hi = {b}, mid = {c}, r[mid] = {d} → {e}' for a, b, c, d, e in p1['rows']) +
    f'. Nach {len(p1["mids"])} Durchläufen gefunden (lineare Suche: {r1.index(57) + 1} Prüfungen).'))

# ---------- 02 Klick-Suche (kein Treffer) + Endwerte
r2 = [6, 13, 21, 28, 34, 41, 47, 55, 62, 69, 74, 88]
p2 = search_verified(r2, 50, f'{L}-02')
A.append(aufgabe(
    f'{L}-02', 'Die Zahl, die es nicht gibt', 2, 'Sortieren und Suchen', [],
    [text('Gesucht wird x = 50 – diese Zahl kommt **nicht** vor. Die Methode `binaer` ist dieselbe wie oben:'), code(BIN_CODE), reihung(r2), KLICK_HINW,
     text('Rückgabewert: [[g1]] · Die Schleife endet mit lo = [[g2]] und hi = [[g3]] · Schleifendurchläufe: [[g4]]')],
    [array_klick(r2), gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=zahl())],
    [{'folge': p2['mids']}, {'g1': [str(p2['result'])], 'g2': [str(p2['lo'])], 'g3': [str(p2['hi'])], 'g4': [str(len(p2['mids']))]}],
    ['Die Schleife endet, sobald lo > hi ist.'],
    'Trace: ' + ' · '.join(f'lo = {a}, hi = {b}, mid = {c}, r[mid] = {d} → {e}' for a, b, c, d, e in p2['rows']) +
    f'. Danach ist lo = {p2["lo"]} > hi = {p2["hi"]}: Der Bereich ist leer, Rückgabe **−1**. Übrigens: lo zeigt jetzt genau auf '
    'die Stelle, an der 50 eingefügt werden müsste.'))

# ---------- 03 Tracetabelle lo/hi/mid
r3 = [3, 8, 14, 19, 25, 31, 36, 40, 47, 53, 58, 66, 71, 79, 84]
x3 = 71
p3 = search_verified(r3, x3, f'{L}-03')
AKT = ['lo ← mid + 1', 'hi ← mid − 1', 'gib mid zurück']
zeilen, loes, felder = [], {}, {}
for k, (lo, hi, mid, rm, akt) in enumerate(p3['rows'], start=1):
    zeilen.append([str(k)] + [f'[[{c}{k}]]' for c in 'lhmra'])
    for c, v in zip('lhmr', (lo, hi, mid, rm)):
        loes[f'{c}{k}'] = [str(v)]; felder[f'{c}{k}'] = zahl()
    loes[f'a{k}'] = [akt]; felder[f'a{k}'] = auswahl(AKT)
A.append(aufgabe(
    f'{L}-03', 'Tracetabelle: lo, hi, mid', 2, 'Tracetabelle', ['P8'],
    [text(f'Führe `binaer(r, {x3})` (iterative binäre Suche, mid = (lo + hi) / 2) für diese aufsteigend sortierte Reihung von Hand aus. '
          'Trage die Werte **zu Beginn** jedes Schleifendurchlaufs ein.'), reihung(r3),
     tabelle(['Durchlauf', 'lo', 'hi', 'mid', 'r[mid]', 'Aktion'], zeilen)],
    gaps(**felder), loes, ['mid wird abgerundet: (7 + 14) / 2 = 10.'],
    'Eine Zeile pro Schleifendurchlauf mit den Werten **zu Beginn** des Durchlaufs und der Aktion. ' +
    ' · '.join(f'({a}, {b}) → mid {c}, r[mid] = {d}: {e}' for a, b, c, d, e in p3['rows']) + f'. Rückgabe {p3["result"]}.'))

# ---------- 04 maximale Durchlaeufe
ns = [1, 7, 8, 100, 200, 1000, 1000000]
mx = {n: max_durchlaeufe(n) for n in ns}
for n in [1, 7, 8, 100, 200, 1000]:
    check(max_durchlaeufe_brute(n) == mx[n], f'W2-L4-04 n = {n}: hoechstens {mx[n]} Durchlaeufe (alle x durchprobiert)')
check(mx[1000000] == 20, 'W2-L4-04 n = 1 000 000: 20 Durchlaeufe (Rekursion ueber die groessere Haelfte)')
out = J('int[] r = new int[100]; for (int i = 0; i < 100; i++) r[i] = 2 * i; int best = 0;'
        ' for (int x = -1; x <= 200; x++) { Suche.binaer(r, x); if (Suche.durchlaeufe > best) best = Suche.durchlaeufe; } println(best);')
check(out == [str(mx[100])], 'W2-L4-04 Java-LSG Suche.binaer: n = 100 hoechstens 7 Durchlaeufe')
A.append(aufgabe(
    f'{L}-04', 'Wie oft höchstens?', 1, 'Effizienz', [],
    [text('Gib an, wie viele Schleifendurchläufe die binäre Suche bei n Elementen **höchstens** braucht.'),
     tabelle(['n'] + [f'{n:,}'.replace(',', ' ') for n in ns], [['max. Durchläufe'] + [f'[[n{k}]]' for k in range(len(ns))]])],
    gaps(**{f'n{k}': zahl() for k in range(len(ns))}), {f'n{k}': [str(mx[n])] for k, n in enumerate(ns)},
    ['Nach jedem erfolglosen Durchlauf bleibt höchstens die Hälfte übrig: 100 → 50 → 25 → 12 → 6 → 3 → 1.'],
    'Jeder Durchlauf halbiert den Bereich mindestens. Höchstzahl = Anzahl der Halbierungen, bis 1 Element übrig ist, plus '
    'dieser letzte Durchlauf: ⌊log₂ n⌋ + 1. 2⁶ = 64 ≤ 100 < 128 → 7; 1000 < 1024 → 10; 1 000 000 < 2²⁰ → 20. '
    'Verdoppelt man n, kommt **höchstens ein** Durchlauf hinzu.'))

# ---------- 05 Bug-Hunt binaere Suche
code05 = '''public static int binaer(int[] r, int x) {
    int lo = 0;
    int hi = r.length - 1;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (r[mid] == x) {
            return mid;
        } else if (r[mid] < x) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    return -1;
}'''
cap = code05.replace('    while (lo < hi) {', '    int schutz = 0;\n    while (lo < hi) {\n        schutz++; if (schutz > 1000) { return -99; }')
SB = 'class SB {\n' + '{code}' + '\n}'
out = J('println(SB.binaer(new int[]{5, 9, 14, 20}, 20)); println(SB.binaer(new int[]{7}, 7));', SB.replace('{code}', cap))
check(out == ['-99', '-1'], 'W2-L4-05 fehlerhafte Suche: Endlosschleife bei x = 20 (lo = mid), 1-elementige Reihung nicht geprueft (lo < hi)')
v4 = ['while (lo <= hi) {', 'while (hi >= lo) {']
v9 = ['lo = mid + 1;', 'lo = 1 + mid;']
for a4 in v4:
    for a9 in v9:
        fx = code05.replace('    while (lo < hi) {', '    ' + a4).replace('            lo = mid;', '            ' + a9)
        out = J('int[] r = {5, 9, 14, 20, 26, 31, 40}; String s = ""; for (int x = 0; x <= 45; x++) { if (SB.binaer(r, x) != Suche.binaer(r, x)) s += x; }'
                ' println("diff:" + s); println(SB.binaer(new int[]{7}, 7)); println(SB.binaer(new int[0], 7));', SB.replace('{code}', fx))
        check(out == ['diff:', '0', '-1'], f'W2-L4-05 Korrektur {a4} / {a9} = LSG Suche.binaer fuer alle x')
A.append(aufgabe(
    f'{L}-05', 'Die Suche hängt sich auf', 2, 'Fehler im Java-Code', ['P6'],
    [text('Diese binäre Suche enthält **zwei** Fehler: Für r = {5, 9, 14, 20} und x = 20 endet sie nie, und für r = {7} und '
          'x = 7 liefert sie −1.'), code(code05),
     text('**a)** Markiere die beiden fehlerhaften Zeilen. **b)** Korrigierte Schleifenbedingung: [[g1]]'),
     text('Korrigierte Zeile im `else if`-Zweig: [[g2]]')],
    [lines(1, 2), gaps(g1=txt('code', 22), g2=txt('code', 18))],
    [{'zeilen': [4, 9]}, {'g1': varianten(*v4), 'g2': varianten(*v9)}],
    ['Spiele r = {5, 9, 14, 20}, x = 20 Schritt für Schritt durch.'],
    'Zeile 4: Mit `lo < hi` wird ein Bereich aus genau einem Element (lo = hi) nicht mehr geprüft – richtig `lo <= hi` (P6). '
    'Zeile 9: `lo = mid` schließt mid nicht aus. Bei lo = 2, hi = 3 ist mid = 2, r[2] = 14 < 20 → lo bleibt 2: '
    'Endlosschleife. Richtig `lo = mid + 1`.'))

# ---------- 06 Struktogramm-Luecken
sg = struktogramm('binaer(r: Reihung von Ganzzahl, x: Ganzzahl): Ganzzahl',
                  [{'anw': 'lo ← 0'}, {'anw': 'hi ← [[g1]]'},
                   {'solange': 'lo [[g2]] hi', 'rumpf': [
                       {'anw': 'mid ← (lo + hi) / 2'},
                       {'wenn': 'r[mid] = x', 'dann': [{'gib': 'mid'}],
                        'sonst': [{'wenn': 'r[mid] < x', 'dann': [{'anw': 'lo ← [[g3]]'}], 'sonst': [{'anw': 'hi ← [[g4]]'}]}]}]},
                   {'gib': '[[g5]]'}])
O1 = ['Länge von r', 'Länge von r − 1', '0']
O2 = ['<', '≤', '>', '≠']
O3 = ['mid', 'mid + 1', 'mid − 1']
O5 = ['−1', 'mid', 'lo', 'hi']
loes6 = {'g1': ['Länge von r − 1'], 'g2': ['≤'], 'g3': ['mid + 1'], 'g4': ['mid − 1'], 'g5': ['−1']}


def sg_python(r, x, a):
    lo = 0; hi = len(r) - 1 if a['g1'] == 'Länge von r − 1' else len(r)
    ops = {'<': lambda p, q: p < q, '≤': lambda p, q: p <= q, '>': lambda p, q: p > q, '≠': lambda p, q: p != q}
    steps = 0
    while ops[a['g2']](lo, hi):
        steps += 1
        if steps > 100:
            return 'endlos'
        mid = (lo + hi) // 2
        if mid >= len(r):
            return 'fehler'
        if r[mid] == x:
            return mid
        d = {'mid': 0, 'mid + 1': 1, 'mid − 1': -1}
        if r[mid] < x:
            lo = mid + d[a['g3']]
        else:
            hi = mid + d[a['g4']]
    return -1


rr = [3, 8, 14, 19, 25, 31]
check(all(sg_python(rr, x, {k: v[0] for k, v in loes6.items()}) == binsearch(rr, x)['result'] for x in range(0, 40)),
      'W2-L4-06 Struktogramm mit Loesung = Skript-Binaersuche fuer alle x')
A.append(aufgabe(
    f'{L}-06', 'Das Struktogramm der Halbierung', 1, 'Code ↔ Struktogramm', ['P9'],
    [text('Vervollständige das Struktogramm der binären Suche (aufsteigend sortierte Reihung r) nach EH § 5.'), sg],
    gaps(g1=auswahl(O1), g2=auswahl(O2), g3=auswahl(O3), g4=auswahl(O3), g5=auswahl(O5)), loes6,
    ['Der Bereich lo … hi enthält am Anfang alle Indizes.'],
    'hi startet beim letzten Index „Länge von r − 1". Gesucht wird, **solange lo ≤ hi** (auch ein einzelnes Element wird '
    'geprüft). Ist r[mid] < x, liegt x rechts: lo ← mid + 1, sonst links: hi ← mid − 1 – mid selbst ist ja schon geprüft. '
    'Ist der Bereich leer, „gib −1 zurück".'))

# ---------- 07 Parsons binaer
teile = [('a', 'public static int binaer(int[] r, int x) {'), ('b', '    int lo = 0;'), ('c', '    int hi = r.length - 1;'),
         ('d', '    while (lo <= hi) {'), ('e', '        int mid = (lo + hi) / 2;'), ('f', '        if (r[mid] == x) {'),
         ('g', '            return mid;'), ('h', '        } else if (r[mid] < x) {'), ('i', '            lo = mid + 1;'),
         ('j', '        } else {'), ('k', '            hi = mid - 1;'), ('l', '        }'), ('m', '    }'), ('n', '    return -1;'),
         ('o', '}'),
         ('x', '    while (lo < hi) {'), ('y', '            lo = mid;'), ('z', '    int hi = r.length;')]
T = dict(teile)
reih = [list('abcdefghijklmno'), list('acbdefghijklmno')]
for r in reih:
    m = '\n'.join(T[k] for k in r)
    out = J('int[] r = {2, 7, 11, 15, 20, 24, 29, 33, 38}; String s = ""; for (int x = 0; x <= 40; x++) { if (SP.binaer(r, x) != Suche.binaer(r, x)) s += x; }'
            ' println("diff:" + s); println(SP.binaer(new int[0], 3));', 'class SP {\n' + m + '\n}')
    check(out == ['diff:', '-1'], f'W2-L4-07 Parsons binaer Reihenfolge {"".join(r)} = LSG Suche.binaer fuer alle x')
A.append(aufgabe(
    f'{L}-07', 'Puzzle: Die Suchmaschine', 3, 'Methode implementieren', ['P6'],
    [text('Setze die iterative binäre Suche `binaer(r: Reihung von Ganzzahl, x: Ganzzahl): Ganzzahl` zusammen: Index eines '
          'Vorkommens von x in der aufsteigend sortierten Reihung r, sonst −1. Nicht alle Teile werden gebraucht.')],
    order(teile), {'reihenfolgen': reih}, ['Achte auf die vier Fallen: Bedingung, beide Grenzen, Rückgabe nach der Schleife.'],
    '`lo = 0` und `hi = r.length - 1` (Reihenfolge egal), Schleife **solange lo ≤ hi**, mid ganzzahlig, Treffer sofort '
    'zurückgeben, sonst eine Hälfte **ohne** mid ausschließen (`mid + 1` bzw. `mid - 1`). −1 erst nach der Schleife. '
    'Distraktoren: `lo < hi` prüft ein einzelnes Element nicht, `lo = mid` kann endlos laufen, `hi = r.length` greift '
    'hinter das Ende (P6).'))

# ---------- 08 Lohnt sich Sortieren?
N8, S8 = 500000, 5000
lin = S8 * N8
ins_w = N8 * (N8 - 1) // 2
b8 = max_durchlaeufe(N8)
check(S8 == 5000 and N8 == 500000 and b8 == 19 and lin == 2500000000 and ins_w == 124999750000 and ins_w + S8 * b8 > lin,
      'W2-L4-08 500 000 Eintraege, 5000 Suchen: linear 2,5e9 < Insertionsort 1,25e11 + 5000*19')
A.append(aufgabe(
    f'{L}-08', 'Erst sortieren, dann suchen?', 3, 'Effizienz', ['P10'],
    [text('Eine **unsortierte** Bestenliste hat 500 000 Einträge. Es soll 5 000-mal nach einem Wert gesucht werden. '
          'Rechne jeweils mit dem **schlechtesten** Fall. Gib Anzahlen als ganze Zahl ohne Tausenderpunkte ein (z. B. 1250000).'),
     text('Vergleiche, wenn 5 000-mal linear gesucht wird: [[g1]]'),
     text('Vergleiche, um die Liste zuerst mit Insertionsort zu sortieren: [[g2]]'),
     text('Durchläufe **einer** binären Suche danach höchstens: [[g3]]'),
     text('Urteil: [[g4]]')],
    gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=auswahl(['Sortieren lohnt sich hier', 'Sortieren lohnt sich hier nicht'])),
    {'g1': [str(lin)], 'g2': [str(ins_w)], 'g3': [str(b8)], 'g4': ['Sortieren lohnt sich hier nicht']},
    ['Lineare Suche im schlechtesten Fall: alle n Elemente prüfen.'],
    f'Linear: {S8} · 500 000 = 2,5 · 10⁹ Vergleiche. Insertionsort im schlechtesten Fall: 500 000 · 499 999 / 2 ≈ 1,25 · 10¹¹ – '
    f'schon das Sortieren kostet etwa 50-mal so viel wie alle linearen Suchen zusammen; die {S8} binären Suchen '
    f'(je höchstens {b8} Durchläufe) fallen kaum ins Gewicht. Erst bei sehr vielen Suchen (oder mit einem schnelleren '
    'Sortierverfahren, Welt 3) lohnt sich das Sortieren.'))

LEVELS.append({"id": L, "nr": "2.4", "titel": "Halbieren statt Durchsuchen – binäre Suche", "ds": [16],
               "ab": "AB W2·3 Effizienz und binäre Suche – Teil B (Aufgaben 4–7)",
               "ide": "AQ_W2_L2_Rangliste_Geruest.txt – IDE-Level 2.3 (Klasse Suche, Testklasse L23SucheTest)",
               "intro": [text('Die **binäre Suche** funktioniert nur auf sortierten Daten: Ein Blick auf `r[mid]` mit '
                              'mid = (lo + hi) / 2 schließt eine ganze Hälfte aus.'),
                         hinweis('**Die vier Fallen:** nur auf sortierten Daten · Bedingung `lo <= hi` · `lo = mid + 1` bzw. '
                                 '`hi = mid - 1` · `return -1` nach der Schleife. Höchstens ⌊log₂ n⌋ + 1 Durchläufe, Verdopplung → +1.')],
               "aufgaben": [a['id'] for a in A if a['id'].startswith(L + '-')]})

import w2boss  # noqa: E402
BOSS_AUFGABEN = w2boss.build()
A.extend(BOSS_AUFGABEN)

WELT = {"version": 2, "welt": 2, "titel": "Die Rangliste", "farbe": "#1F7A7A",
        "levels": LEVELS,
        "boss": {"id": "W2-BOSS", "titel": "Das Wettfischen am Drachensee", "dauerMin": 25, "anzahl": 8,
                 "mix": {"1": 3, "2": 3, "3": 2}, "pool": [a['id'] for a in BOSS_AUFGABEN]},
        "aufgaben": A}
