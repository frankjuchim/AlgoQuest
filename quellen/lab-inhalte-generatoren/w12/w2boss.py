"""Welt 2 – Boss-Pool „Das Wettfischen am Drachensee" (neuer Kontext, Transfer)."""
from lib import *
from algos import *

FANG = '''
class Fang {
    private String angler;
    private int gewicht;
    public Fang(String angler, int gewicht) { this.angler = angler; this.gewicht = gewicht; }
    public String getAngler() { return angler; }
    public int getGewicht() { return gewicht; }
}

class Wettfischen {
    private Fang[] faenge;
    private int anzahl;

    public Wettfischen(int plaetze) { faenge = new Fang[plaetze]; anzahl = 0; }

    public boolean melden(Fang f) {
        if (f == null || anzahl == faenge.length) { return false; }
        faenge[anzahl] = f; anzahl++; return true;
    }
    public int getAnzahl() { return anzahl; }
    public Fang getFang(int i) { if (i < 0 || i >= anzahl) { return null; } return faenge[i]; }

    public Fang schwersterFang() {
        if (anzahl == 0) { return null; }
        Fang bester = faenge[0];
        for (int i = 1; i < anzahl; i++) {
            if (faenge[i].getGewicht() > bester.getGewicht()) { bester = faenge[i]; }
        }
        return bester;
    }
    public int anzahlUeber(int grenze) {
        int z = 0;
        for (int i = 0; i < anzahl; i++) { if (faenge[i].getGewicht() > grenze) { z++; } }
        return z;
    }
    public int indexVon(String angler) {
        for (int i = 0; i < anzahl; i++) { if (faenge[i].getAngler().equals(angler)) { return i; } }
        return -1;
    }
    public int kleinstesGewicht() {
        if (anzahl == 0) { return -1; }
        int min = faenge[0].getGewicht();
        for (int i = 1; i < anzahl; i++) { if (faenge[i].getGewicht() < min) { min = faenge[i].getGewicht(); } }
        return min;
    }
    public String liste() {
        String s = "";
        for (int i = 0; i < anzahl; i++) { s = s + faenge[i].getAngler() + faenge[i].getGewicht() + ","; }
        return s;
    }
}
'''
KONTEXT = text('**Das Wettfischen am Drachensee.** Beim Wettfischen meldet jede Anglerin und jeder Angler den schwersten Fang. '
               'Ein `Fang` hat die Attribute `angler` (Zeichenkette) und `gewicht` (Ganzzahl, in Gramm). Die Klasse '
               '`Wettfischen` verwaltet die Fänge in der Reihung `faenge`; belegt sind lückenlos die Felder 0 bis `anzahl − 1`, '
               'alle übrigen enthalten `null`. Platz 1 hat das **größte** Gewicht.')
KK = [klassenkarte('Fang', ['- angler: Zeichenkette', '- gewicht: Ganzzahl'],
                   ['+ c Fang(angler: Zeichenkette, gewicht: Ganzzahl)', '+ getAngler(): Zeichenkette', '+ getGewicht(): Ganzzahl']),
      klassenkarte('Wettfischen', ['- faenge: Reihung von Fang', '- anzahl: Ganzzahl'],
                   ['+ c Wettfischen(plaetze: Ganzzahl)', '+ melden(f: Fang): Wahrheitswert', '+ getFang(i: Ganzzahl): Fang',
                    '+ schwersterFang(): Fang', '+ anzahlUeber(grenze: Ganzzahl): Ganzzahl', '+ indexVon(angler: Zeichenkette): Ganzzahl',
                    '+ kleinstesGewicht(): Ganzzahl', '…'])]
TAUSCH = text('Wähle nacheinander die beiden Indizes jeder Vertauschung in der Reihenfolge des Verfahrens; danach „fertig".')
KLICK = text('Klicke nacheinander die Indizes an, die als `mid` geprüft werden (mid = (lo + hi) / 2, ganzzahlig).')


def J(main, extra=''):
    return run(2, main, FANG + extra)


def fs(a):
    return ', '.join(str(x) for x in a)


def build():
    B = []
    P = 'W2-B'

    # ---------------- B-01 Selectionsort tauschen
    s1 = [420, 980, 310, 760, 550]
    p = sort_verified('selection', s1, f'{P}-01')
    B.append(aufgabe(
        f'{P}-01', 'Die schwersten Fische nach vorn', 1, 'Sortieren und Suchen', [],
        [KONTEXT, text('Die Gewichte werden mit **Selectionsort** absteigend sortiert: Suche im Rest ab i das größte Gewicht und '
                       'tausche es an Position i – nur, wenn es nicht schon dort steht.'), reihung(s1), TAUSCH],
        array_tausch(s1), {'tausche': p['swaps']}, [],
        'Durchläufe: ' + ' · '.join(f'i = {i}: {fs(st)}' for i, st in enumerate(p['states'])) +
        '. Tausche: ' + ', '.join(f'({i}, {j})' for i, j in p['swaps']) + ' – höchstens ein Tausch pro Durchlauf.'))

    # ---------------- B-02 binaere Suche klicken
    nr = [3, 9, 15, 22, 27, 34, 40, 46, 51, 58, 64]
    p2 = search_verified(nr, 15, f'{P}-02')
    B.append(aufgabe(
        f'{P}-02', 'Startnummer 15', 1, 'Sortieren und Suchen', [],
        [KONTEXT, text('Die Startnummern stehen **aufsteigend** sortiert in einer Reihung. Mit der binären Suche (lo = 0, '
                       'hi = Länge − 1, solange lo ≤ hi) wird die Startnummer 15 gesucht.'), reihung(nr), KLICK],
        array_klick(nr), {'folge': p2['mids']}, [],
        'Trace: ' + ' · '.join(f'lo = {a}, hi = {b}, mid = {c}, r[mid] = {d} → {e}' for a, b, c, d, e in p2['rows']) + '.'))

    # ---------------- B-03 Selectionsort zaehlen
    for n in (8, 16):
        pp = sort_verified('selection', list(range(n * 7 % 13, n * 7 % 13 + n)), f'{P}-03 n = {n}')
        check(pp['comps'] == n * (n - 1) // 2, f'{P}-03 n = {n}: {pp["comps"]} Vergleiche')
    B.append(aufgabe(
        f'{P}-03', 'Zählen am Steg', 1, 'Effizienz', ['P10'],
        [KONTEXT, text('Die Fänge werden mit Selectionsort sortiert; gezählt werden die Gewichtsvergleiche.'),
         text('Vergleiche bei 8 Fängen: [[g1]] · bei 16 Fängen: [[g2]] · Bei Verdopplung der Fänge wächst die Zahl der '
              'Vergleiche etwa auf das [[g3]]-Fache (ganze Zahl).')],
        gaps(g1=zahl(), g2=zahl(), g3=zahl()), {'g1': ['28'], 'g2': ['120'], 'g3': ['4']}, [],
        'Selectionsort vergleicht immer (n − 1) + (n − 2) + … + 1 = n(n − 1)/2: 8 · 7 / 2 = **28**, 16 · 15 / 2 = **120** '
        '(≈ 4,3-fach, für große n gegen 4): Die Vergleichszahl hängt quadratisch von n ab.'))

    # ---------------- B-04 Verfahren erkennen (Code)
    code04 = '''public static void ordne(int[] r) {
    for (int i = 1; i < r.length; i++) {
        int j = i;
        while (j > 0 && r[j] < r[j - 1]) {
            int h = r[j];
            r[j] = r[j - 1];
            r[j - 1] = h;
            j--;
        }
    }
}'''
    out = run(2, 'int[] r = {5, 2, 9, 1}; SO.ordne(r); println(r[0] + "," + r[1] + "," + r[2] + "," + r[3]);', 'class SO {\n' + code04 + '\n}')
    check(out == ['1,2,5,9'], f'{P}-04 ordne sortiert aufsteigend')
    B.append(aufgabe(
        f'{P}-04', 'Welches Verfahren angelt hier?', 1, 'Funktionsweise erläutern', [],
        [code(code04), text('Um welches Verfahren handelt es sich, und in welche Richtung wird sortiert?')],
        choice([('a', 'Insertionsort, aufsteigend'), ('b', 'Insertionsort, absteigend'), ('c', 'Selectionsort, aufsteigend'),
                ('d', 'Bubblesort, aufsteigend')]),
        {'richtig': ['a']}, [],
        'Der Eintrag an Position i wandert durch **Nachbartausche nach links**, solange er kleiner als sein linker Nachbar ist '
        '– typisch für Insertionsort. Weil kleinere Werte nach vorn wandern (`r[j] < r[j − 1]`), wird **aufsteigend** sortiert.'))

    # ---------------- B-05 Bausteine
    daten = [('Ada', 820), ('Bo', 1340), ('Cem', 760), ('Dina', 1340), ('Eli', 590)]
    out = J('Wettfischen w = new Wettfischen(8);' + ''.join(f' w.melden(new Fang("{a}", {g}));' for a, g in daten)
            + ' println(w.schwersterFang().getAngler()); println(w.anzahlUeber(800)); println(w.indexVon("Eli")); println(w.kleinstesGewicht());')
    chk = run(2, 'Rangliste r = new Rangliste(8);' + ''.join(f' r.hinzufuegen(new Eintrag("{a}", {g}, 0));' for a, g in daten)
              + ' println(r.besterEintrag().getName()); println(r.anzahlUeber(800)); println(r.indexVon("Eli"));')
    check(out[:3] == chk and out == ['Bo', '3', '4', '590'], f'{P}-05 Wettfischen-Bausteine = Rangliste-LSG: Bo/3/4/590')
    B.append(aufgabe(
        f'{P}-05', 'Die Waage am Steg', 1, 'Sortieren und Suchen', [],
        [KONTEXT] + KK + [text('Gemeldet sind (Index 0 bis 4): ' + ', '.join(f'{a} {g} g' for a, g in daten) + '. `schwersterFang()` '
                              'liefert bei Gleichstand den ersten, `anzahlUeber` zählt echt größere Gewichte.'),
                         tabelle(['Aufruf', 'Ergebnis'], [['`schwersterFang().getAngler()`', '[[g1]]'], ['`anzahlUeber(800)`', '[[g2]]'],
                                                          ['`indexVon("Eli")`', '[[g3]]'], ['`kleinstesGewicht()`', '[[g4]]']])],
        gaps(g1=auswahl([a for a, _ in daten]), g2=zahl(), g3=zahl(), g4=zahl()),
        {'g1': [out[0]], 'g2': [out[1]], 'g3': [out[2]], 'g4': [out[3]]}, [],
        'Maximum: Bo und Dina haben 1340 g – bei Gleichstand bleibt der **erste** (Bo). Über 800 g: 820, 1340, 1340 → **3**. '
        'Eli steht an Index **4**. Minimum: **590**.'))

    # ---------------- B-06 Insertionsort tauschen
    s6 = [350, 610, 480, 720, 290, 500]
    p = sort_verified('insertion', s6, f'{P}-06')
    B.append(aufgabe(
        f'{P}-06', 'Einsortieren am Steg', 2, 'Sortieren und Suchen', [],
        [KONTEXT, text('Die Gewichte werden mit **Insertionsort** absteigend sortiert: Für i = 1, 2, … wandert das Gewicht an '
                       'Position i durch Nachbartausche nach links, solange es **größer** als sein linker Nachbar ist.'),
         reihung(s6), TAUSCH],
        array_tausch(s6), {'tausche': p['swaps']}, [],
        'Zustände nach jedem Durchlauf: ' + ' · '.join(f'i = {i + 1}: {fs(st)}' for i, st in enumerate(p['states'])) +
        f'. {len(p["swaps"])} Nachbartausche, {p["comps"]} Vergleiche.'))

    # ---------------- B-07 Bubblesort-Trace
    s7 = [45, 30, 60, 55, 20]
    p = sort_verified('bubble', s7, f'{P}-07')
    zeilen, loes, felder = [['Start'] + s7 + ['0', '0']], {}, {}
    for r, (st, (c, t)) in enumerate(zip(p['states'], p['rows']), start=1):
        z = [f'Durchlauf {r}']
        for idx, v in enumerate(st):
            g = f'w{r}{idx}'; z.append(f'[[{g}]]'); loes[g] = [str(v)]; felder[g] = zahl()
        for g, v in ((f'c{r}', c), (f't{r}', t)):
            z.append(f'[[{g}]]'); loes[g] = [str(v)]; felder[g] = zahl()
        zeilen.append(z)
    B.append(aufgabe(
        f'{P}-07', 'Tracetabelle: Blasen im See', 2, 'Tracetabelle', ['P8'],
        [KONTEXT, text('Die Gewichte (in 10 g) werden mit **Bubblesort mit Abbruch** absteigend sortiert: In jedem Durchlauf werden '
                       'Nachbarn von links nach rechts verglichen und getauscht, wenn der rechte größer ist; die innere Schleife wird '
                       'nach jedem Durchlauf um 1 kürzer; ein Durchlauf ohne Tausch beendet das Verfahren.'),
         tabelle(['nach …', 'Index 0', 'Index 1', 'Index 2', 'Index 3', 'Index 4', 'Vergleiche (Summe)', 'Vertauschungen (Summe)'], zeilen)],
        gaps(**felder), loes, [],
        f'Es sind {len(p["states"])} Durchläufe – der letzte bleibt ohne Vertauschung und beendet das Verfahren. Summen: '
        f'{p["comps"]} Vergleiche, {len(p["swaps"])} Vertauschungen.'))

    # ---------------- B-08 Bug-Hunt Minimum mit 0
    code08 = '''public int kleinstesGewicht() {
    if (anzahl == 0) {
        return -1;
    }
    int min = 0;
    for (int i = 0; i < anzahl; i++) {
        if (faenge[i].getGewicht() < min) {
            min = faenge[i].getGewicht();
        }
    }
    return min;
}'''
    ext = FANG.replace('class Wettfischen {', 'class Wettfischen {\n' + code08.replace('kleinstesGewicht(', 'kleinstesB(') + '\n')
    out = run(2, 'Wettfischen w = new Wettfischen(5); w.melden(new Fang("A", 820)); w.melden(new Fang("B", 760)); w.melden(new Fang("C", 590)); println(w.kleinstesB());', ext)
    check(out == ['0'], f'{P}-08 fehlerhafte Methode liefert 0')
    v5 = ['int min = faenge[0].getGewicht();', 'int min = this.faenge[0].getGewicht();']
    for v in v5:
        e2 = FANG.replace('class Wettfischen {', 'class Wettfischen {\n' + code08.replace('kleinstesGewicht(', 'kleinstesB(').replace('    int min = 0;', '    ' + v) + '\n')
        out = run(2, 'Wettfischen w = new Wettfischen(5); println(w.kleinstesB()); w.melden(new Fang("A", 820)); w.melden(new Fang("B", 760)); w.melden(new Fang("C", 590)); println(w.kleinstesB());', e2)
        check(out == ['-1', '590'], f'{P}-08 Korrektur "{v}" -> -1 / 590')
    B.append(aufgabe(
        f'{P}-08', 'Der Null-Gramm-Fisch', 2, 'Fehler im Java-Code', [],
        [KONTEXT, text('`kleinstesGewicht()` soll das kleinste gemeldete Gewicht liefern (−1, wenn nichts gemeldet ist).'), code(code08),
         text('**a)** Markiere die fehlerhafte Zeile. **b)** Korrigierte Zeile: [[g1]] **c)** Für die Gewichte 820, 760, 590 liefert '
              'die fehlerhafte Methode: [[g2]]')],
        [lines(2, 1), gaps(g1=txt('code', 36), g2=zahl())],
        [{'zeilen': [5]}, {'g1': varianten(*v5), 'g2': ['0']}], [],
        'Zeile 5: Der Rekord startet mit 0 – kein echtes Gewicht ist kleiner, die Methode liefert immer **0**. Der Rekordhalter '
        'muss das **erste** gemeldete Gewicht sein: `int min = faenge[0].getGewicht();` (sicher, weil vorher auf `anzahl == 0` '
        'geprüft wird). Die Schleife darf dann bei 0 oder 1 beginnen.'))

    # ---------------- B-09 erfolglose Suche + Endwerte
    p9 = search_verified(nr, 50, f'{P}-09')
    B.append(aufgabe(
        f'{P}-09', 'Startnummer 50 – gibt es nicht', 2, 'Sortieren und Suchen', ['P8'],
        [KONTEXT, text('Gesucht wird die Startnummer 50 in den aufsteigend sortierten Startnummern (binäre Suche wie üblich).'),
         reihung(nr), KLICK, text('Rückgabewert: [[g1]] · Schleifendurchläufe: [[g2]] · Endwerte: lo = [[g3]], hi = [[g4]]')],
        [array_klick(nr), gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=zahl())],
        [{'folge': p9['mids']}, {'g1': [str(p9['result'])], 'g2': [str(len(p9['mids']))], 'g3': [str(p9['lo'])], 'g4': [str(p9['hi'])]}], [],
        'Trace: ' + ' · '.join(f'lo = {a}, hi = {b}, mid = {c}, r[mid] = {d} → {e}' for a, b, c, d, e in p9['rows']) +
        f'. Dann lo = {p9["lo"]} > hi = {p9["hi"]} → Rückgabe −1.'))

    # ---------------- B-10 Insertionsort zaehlen + schlechtester Fall
    s10 = [500, 200, 400, 300]
    p = sort_verified('insertion', s10, f'{P}-10')
    worst6 = max(insertion(list(pm))['comps'] for pm in __import__('itertools').permutations(range(6)))
    opts = [('a', [60, 50, 40, 30, 20, 10]), ('b', [10, 20, 30, 40, 50, 60]), ('c', [10, 60, 20, 50, 30, 40]), ('d', [60, 10, 50, 20, 40, 30])]
    richtig = [k for k, w in opts if sort_verified('insertion', w, f'{P}-10')['comps'] == worst6]
    check(worst6 == 15 and richtig == ['b'], f'{P}-10 schlechtester Fall n = 6: 15 Vergleiche nur bei aufsteigender Eingabe')
    B.append(aufgabe(
        f'{P}-10', 'Wie viel Arbeit macht das Einsortieren?', 2, 'Effizienz', [],
        [KONTEXT, text('Insertionsort sortiert absteigend nach Gewicht; gezählt wird jeder Gewichtsvergleich (der Vergleich entfällt, '
                       'wenn j = 0 ist).'),
         text(f'**a)** Gewichte {fs(s10)}: Vergleiche [[g1]], Vertauschungen [[g2]]'),
         text('**b)** Vergleiche im schlechtesten Fall bei 6 Fängen: [[g3]]'),
         text('**c)** Welche Eingabe führt bei 6 Fängen zum schlechtesten Fall?')],
        [gaps(g1=zahl(), g2=zahl(), g3=zahl()), choice([(k, f'`{fs(w)}`') for k, w in opts])],
        [{'g1': [str(p['comps'])], 'g2': [str(len(p['swaps']))], 'g3': [str(worst6)]}, {'richtig': richtig}], [],
        f'a) i = 1: 200 > 500 nein (1). i = 2: 400 > 200 tauschen, 400 > 500 nein (2). i = 3: 300 > 200 tauschen, 300 > 400 nein (2) '
        f'→ {p["comps"]} Vergleiche, {len(p["swaps"])} Vertauschungen. b/c) Am meisten Arbeit, wenn **jeder** Eintrag bis ganz nach '
        'vorn wandern muss – bei aufsteigend sortierter Eingabe: 1 + 2 + 3 + 4 + 5 = **15** = 6 · 5 / 2.'))

    # ---------------- B-11 match Merkmale
    B.append(aufgabe(
        f'{P}-11', 'Steckbriefe am Steg', 2, 'Funktionsweise erläutern', ['P10'],
        [text('Ordne jede Aussage dem passenden Verfahren zu.')],
        match([('e1', 'funktioniert nur auf sortierten Daten'),
               ('e2', 'braucht bei jeder Eingabe der Länge n genau n(n − 1)/2 Vergleiche'),
               ('e3', 'endet, sobald ein Durchlauf ohne Vertauschung blieb'),
               ('e4', 'fügt das nächste Element durch Nachbartausche in den sortierten linken Teil ein'),
               ('e5', 'Verdopplung von n → höchstens ein Durchlauf mehr'),
               ('e6', 'vertauscht insgesamt höchstens n − 1-mal')],
              [('s', 'Selectionsort'), ('i', 'Insertionsort'), ('b', 'Bubblesort mit Abbruch'), ('bs', 'binäre Suche')]),
        {'e1': 'bs', 'e2': 's', 'e3': 'b', 'e4': 'i', 'e5': 'bs', 'e6': 's'}, [],
        'Binäre Suche: nur auf sortierten Daten, halbiert den Bereich → Verdopplung kostet höchstens einen Durchlauf. '
        'Selectionsort: Vergleichszahl unabhängig von den Daten, höchstens ein Tausch je Durchlauf. Bubblesort: Abbruch nach '
        'einem Durchlauf ohne Tausch. Insertionsort: Einfügen durch Nachbartausche.'))

    # ---------------- B-12 Parsons eintragen (sortiert einfuegen)
    teile = [('a', 'public boolean eintragen(Fang f) {'), ('b', '    if (f == null || anzahl == faenge.length) {'),
             ('c', '        return false;'), ('d', '    }'), ('e', '    int i = anzahl;'),
             ('f', '    while (i > 0 && faenge[i - 1].getGewicht() < f.getGewicht()) {'), ('g', '        faenge[i] = faenge[i - 1];'),
             ('h', '        i--;'), ('i', '    }'), ('j', '    faenge[i] = f;'), ('k', '    anzahl++;'), ('l', '    return true;'),
             ('m', '}'),
             ('x', '    while (faenge[i - 1].getGewicht() < f.getGewicht() && i > 0) {'), ('y', '        faenge[i - 1] = faenge[i];'),
             ('z', '    int i = anzahl - 1;')]
    T = dict(teile)
    reih = [list('abcdefghijklm'), list('abcdefghikjlm')]
    for r in reih:
        m = '\n'.join(T[k] for k in r)
        ext = FANG.replace('class Wettfischen {', 'class Wettfischen {\n' + m + '\n')
        out = run(2, 'Wettfischen w = new Wettfischen(5); println(w.eintragen(null)); w.eintragen(new Fang("A", 500)); w.eintragen(new Fang("B", 900));'
                  ' w.eintragen(new Fang("C", 500)); w.eintragen(new Fang("D", 100)); w.eintragen(new Fang("E", 700)); println(w.eintragen(new Fang("F", 1)));'
                  ' println(w.liste());', ext)
        check(out == ['false', 'false', 'B900,E700,A500,C500,D100,'], f'{P}-12 Parsons eintragen ({"".join(r)}): sortiert, stabil, voll -> false')
    B.append(aufgabe(
        f'{P}-12', 'Puzzle: Nachmeldung', 3, 'Methode implementieren', ['P1', 'P6'],
        [KONTEXT, text('`eintragen(f: Fang): Wahrheitswert` fügt `f` so in die absteigend nach Gewicht sortierte Reihung ein, dass sie '
                       'sortiert bleibt: Leichtere Fänge rücken eine Position nach hinten, bei gleichem Gewicht kommt `f` dahinter. '
                       'Ist `f` null oder sind alle Plätze belegt, wird false geliefert. Nicht alle Teile werden gebraucht.')],
        order(teile), {'reihenfolgen': reih}, ['Von hinten beginnen: Der erste freie Platz hat den Index `anzahl`.'],
        'Erst die Abfrage gegen Laufzeitfehler (P1). Dann von hinten (`i = anzahl`) jeden **leichteren** Fang nach rechts '
        'schieben (`faenge[i] = faenge[i - 1]`). `i > 0` muss **vor** dem Zugriff auf `faenge[i - 1]` stehen – sonst wird bei '
        'i = 0 der Index −1 angefasst (P6). Bei gleichem Gewicht stoppt die Schleife (`<` ist strikt) → stabil. Zum Schluss '
        'f in die Lücke, `anzahl` erhöhen (diese beiden Zeilen dürfen auch vertauscht sein).'))

    # ---------------- B-13 Effizienz Suche
    m500, m1000 = max_durchlaeufe(500), max_durchlaeufe(1000)
    check(m500 == max_durchlaeufe_brute(500) == 9 and m1000 == 10, f'{P}-13 binaere Suche n = 500: 9, n = 1000: 10 Durchlaeufe')
    B.append(aufgabe(
        f'{P}-13', 'Tausend Startnummern', 3, 'Effizienz', ['P10'],
        [KONTEXT, text('Die Startnummern liegen aufsteigend sortiert vor. Rechne mit dem **schlechtesten** Fall.'),
         text('Durchläufe der binären Suche bei 500 Startnummern: [[g1]] · bei 1000 Startnummern: [[g2]]'),
         text('Geprüfte Elemente der linearen Suche bei 1000 Startnummern: [[g3]]'),
         text('Die Zahl der Startnummern verdoppelt sich. Dann braucht die binäre Suche höchstens [[g4]]')],
        gaps(g1=zahl(), g2=zahl(), g3=zahl(),
             g4=auswahl(['einen Durchlauf mehr', 'doppelt so viele Durchläufe', 'viermal so viele Durchläufe', 'gleich viele Durchläufe'])),
        {'g1': [str(m500)], 'g2': [str(m1000)], 'g3': ['1000'], 'g4': ['einen Durchlauf mehr']}, [],
        '2⁸ = 256 ≤ 500 < 512 → höchstens 8 + 1 = **9** Durchläufe; 512 ≤ 1000 < 1024 → **10**. Jeder Durchlauf halbiert den '
        'Bereich – bei doppelt so vielen Nummern braucht man genau eine Halbierung mehr. Die lineare Suche prüft im '
        'schlechtesten Fall alle **1000**.'))

    # ---------------- B-14 Bug-Hunt Reihenfolge der Bedingungen
    code14 = '''public static void sortiere(int[] r) {
    for (int i = 1; i < r.length; i++) {
        int j = i;
        while (r[j] > r[j - 1] && j > 0) {
            int h = r[j];
            r[j] = r[j - 1];
            r[j - 1] = h;
            j--;
        }
    }
}'''
    inputs = [('a', [9, 7, 5]), ('b', [5, 7, 9]), ('c', [9, 5, 7]), ('d', [4])]
    crash = []
    for k, w in inputs:
        o, e = java(2, 'int[] r = {' + fs(w) + '}; SX.sortiere(r);', 'class SX {\n' + code14 + '\n}')
        if 'ArrayIndexOutOfBoundsException' in e:
            crash.append(k)
    check(crash == ['b'], f'{P}-14 nur {{5, 7, 9}} loest ArrayIndexOutOfBoundsException aus')
    v4 = ['while (j > 0 && r[j] > r[j - 1]) {', 'while (0 < j && r[j] > r[j - 1]) {']
    for v in v4:
        fx = code14.replace('    while (r[j] > r[j - 1] && j > 0) {', '        ' + v.strip()).replace('            while', '        while')
        fx = code14.replace('while (r[j] > r[j - 1] && j > 0) {', v)
        out = run(2, 'int[] r = {5, 7, 9, 1, 8}; SX.sortiere(r); String s = ""; for (int x : r) s += x + ","; println(s);', 'class SX {\n' + fx + '\n}')
        check(out == ['9,8,7,5,1,'], f'{P}-14 Korrektur "{v}" sortiert absteigend')
    B.append(aufgabe(
        f'{P}-14', 'Der Absturz am Ufer', 3, 'Fehler im Java-Code', ['P1', 'P6'],
        [text('Diese Methode soll eine Reihung von Gewichten absteigend sortieren. Bei manchen Eingaben stürzt sie ab.'), code(code14),
         text('**a)** Markiere die fehlerhafte Zeile. **b)** Korrigierte Zeile: [[g1]]'),
         text('**c)** Bei welcher Eingabe stürzt die **ursprüngliche** Methode ab?')],
        [lines(1, 1), gaps(g1=txt('code', 40)), choice([(k, f'`{{{fs(w)}}}`') for k, w in inputs])],
        [{'zeilen': [4]}, {'g1': varianten(*v4)}, {'richtig': crash}], [],
        'Zeile 4: `&&` wertet von links aus. Muss ein Element bis ganz nach vorn wandern, ist irgendwann j = 0 – dann wird '
        'zuerst `r[0] > r[-1]` ausgewertet → **ArrayIndexOutOfBoundsException** (P1/P6). Richtig: erst `j > 0`, dann der '
        'Vergleich. Bei {5, 7, 9} muss die 7 an Index 0 → Absturz; {9, 7, 5} und {9, 5, 7} lassen kein Element bis ganz nach vorn wandern.'))

    # ---------------- B-15 Struktogramm lesen: Bubblesort von rechts (aufsteigend)
    s15 = [6, 2, 8, 1]
    sg = struktogramm('ordne(r: Reihung von Ganzzahl): nichts',
                      [{'zaehle': 'i von 0 bis Länge von r − 2', 'rumpf': [
                          {'zaehle': 'j von Länge von r − 1 abwärts bis i + 1', 'rumpf': [
                              {'wenn': 'r[j] < r[j − 1]', 'dann': [{'anw': 'h ← r[j]'}, {'anw': 'r[j] ← r[j − 1]'}, {'anw': 'r[j − 1] ← h'}],
                               'sonst': []}]}]}])
    java15 = '''class SR {
  static void ordne(int[] r) {
    for (int i = 0; i <= r.length - 2; i++) {
      for (int j = r.length - 1; j >= i + 1; j--) {
        if (r[j] < r[j - 1]) { int h = r[j]; r[j] = r[j - 1]; r[j - 1] = h; SR.t++; }
      }
      String s = ""; for (int x : r) s += x + ","; println(s);
    }
  }
  static int t = 0;
}'''
    out = run(2, 'int[] r = {' + fs(s15) + '}; SR.ordne(r); println(SR.t);', java15)
    states = [[int(v) for v in l.rstrip(',').split(',')] for l in out[:-1]]
    a = list(s15); pys = []; t = 0
    for i in range(len(a) - 1):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]; t += 1
        pys.append(list(a))
    check(states == pys and int(out[-1]) == t, f'{P}-15 Struktogramm-Trace (Java = Python): {states}, {t} Vertauschungen')
    zeilen, loes, felder = [['Start'] + s15], {}, {}
    for i, st in enumerate(states):
        z = [f'i = {i}']
        for idx, v in enumerate(st):
            g = f'w{i}{idx}'; z.append(f'[[{g}]]'); loes[g] = [str(v)]; felder[g] = zahl()
        zeilen.append(z)
    loes['t'] = [str(t)]; felder['t'] = zahl()
    loes['v'] = ['Bubblesort']; felder['v'] = auswahl(['Selectionsort', 'Insertionsort', 'Bubblesort', 'binäre Suche'])
    B.append(aufgabe(
        f'{P}-15', 'Das fremde Ordnungsritual', 3, 'Struktogramm lesen', ['P8', 'P9'],
        [text('Die Operation `ordne` ist als Struktogramm gegeben (r ist eine Reihung von Ganzzahlen).'), sg,
         text('Dokumentiere die Belegung von r = {' + fs(s15) + '} nach jedem Durchlauf der äußeren Schleife.'),
         tabelle(['nach …', 'r[0]', 'r[1]', 'r[2]', 'r[3]'], zeilen),
         text('Vertauschungen insgesamt: [[t]] · Es handelt sich um: [[v]]')],
        gaps(**felder), loes, ['Die innere Schleife läuft von rechts nach links.'],
        'Die innere Schleife vergleicht von rechts nach links **Nachbarn** und tauscht, wenn das kleinere rechts steht. So '
        'wandert das kleinste Element des Restes in jedem Durchlauf nach vorn an Position i („steigt auf") – das ist '
        f'**Bubblesort** (aufsteigend). Zustände: ' + ' · '.join(fs(s) for s in states) + f'; {t} Vertauschungen.'))
    return B
