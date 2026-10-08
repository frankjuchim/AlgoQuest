"""Welt 1 – Boss-Pool „Der Reitstall der Heldenschmiede" (neuer Kontext, Transfer)."""
from lib import *

RT = '''
class Reittier {
    private String name;
    private int tempo;
    private int ausdauer;
    private boolean gesattelt;

    public Reittier(String name) {
        this.name = name;
        tempo = 10;
        ausdauer = 100;
        gesattelt = false;
    }

    public Reittier(String name, int tempo, int ausdauer) {
        this.name = name;
        this.tempo = tempo;
        this.ausdauer = ausdauer;
        gesattelt = false;
    }

    public String getName() { return name; }
    public int getTempo() { return tempo; }
    public int getAusdauer() { return ausdauer; }
    public boolean istGesattelt() { return gesattelt; }

    public void satteln() { gesattelt = true; }

    public void reiten(int strecke) {
        if (gesattelt) {
            ausdauer = ausdauer - strecke;
            if (ausdauer < 0) {
                ausdauer = 0;
            }
        }
    }

    public boolean istBereit() { return gesattelt && ausdauer > 0; }
}

class Greif extends Reittier {
    private int spannweite;

    public Greif(String name, int tempo, int ausdauer, int spannweite) {
        super(name, tempo, ausdauer);
        this.spannweite = spannweite;
    }

    public int getSpannweite() { return spannweite; }

    public int getTempo() { return super.getTempo() * 2; }
}

class Stall {
    private Reittier[] boxen;
    private int anzahl;

    public Stall(int groesse) {
        boxen = new Reittier[groesse];
        anzahl = 0;
    }

    public boolean einstellen(Reittier r) {
        if (r == null || anzahl == boxen.length) {
            return false;
        }
        boxen[anzahl] = r;
        anzahl++;
        return true;
    }

    public int getAnzahl() { return anzahl; }

    public Reittier getReittier(int i) {
        if (i < 0 || i >= anzahl) {
            return null;
        }
        return boxen[i];
    }

    public Reittier schnellstes() {
        if (anzahl == 0) {
            return null;
        }
        Reittier bester = boxen[0];
        for (int i = 1; i < anzahl; i++) {
            if (boxen[i].getTempo() > bester.getTempo()) {
                bester = boxen[i];
            }
        }
        return bester;
    }

    public int anzahlBereit() {
        int zaehler = 0;
        for (int i = 0; i < anzahl; i++) {
            if (boxen[i].istBereit()) {
                zaehler++;
            }
        }
        return zaehler;
    }

    public Reittier finde(String name) {
        for (int i = 0; i < anzahl; i++) {
            if (boxen[i].getName().equals(name)) {
                return boxen[i];
            }
        }
        return null;
    }
}
'''

KK_REITTIER = klassenkarte('Reittier', ['- name: Zeichenkette', '- tempo: Ganzzahl', '- ausdauer: Ganzzahl', '- gesattelt: Wahrheitswert'],
                           ['+ c Reittier(name: Zeichenkette)', '+ c Reittier(name: Zeichenkette, tempo: Ganzzahl, ausdauer: Ganzzahl)',
                            '+ getName(): Zeichenkette', '+ getTempo(): Ganzzahl', '+ getAusdauer(): Ganzzahl',
                            '+ istGesattelt(): Wahrheitswert', '+ satteln(): nichts', '+ reiten(strecke: Ganzzahl): nichts',
                            '+ istBereit(): Wahrheitswert'])
KK_GREIF = klassenkarte('Greif', ['- spannweite: Ganzzahl'],
                        ['+ c Greif(name: Zeichenkette, tempo: Ganzzahl, ausdauer: Ganzzahl, spannweite: Ganzzahl)',
                         '+ getSpannweite(): Ganzzahl', '+ getTempo(): Ganzzahl'])
KK_STALL = klassenkarte('Stall', ['- boxen: Reihung von Reittier', '- anzahl: Ganzzahl'],
                        ['+ c Stall(groesse: Ganzzahl)', '+ einstellen(r: Reittier): Wahrheitswert', '+ getAnzahl(): Ganzzahl',
                         '+ getReittier(i: Ganzzahl): Reittier', '+ schnellstes(): Reittier', '+ anzahlBereit(): Ganzzahl',
                         '+ finde(name: Zeichenkette): Reittier'])
KONTEXT = text('**Der Reitstall der Heldenschmiede.** Die Heldenschmiede verwaltet ihre Reittiere. Ein neues Reittier ist nicht gesattelt; '
               '`Reittier(name)` setzt tempo = 10 und ausdauer = 100. `reiten(strecke)` verringert die Ausdauer nur, wenn das '
               'Tier gesattelt ist, und nie unter 0. `istBereit()` ist wahr, wenn das Tier gesattelt ist und Ausdauer > 0 hat. '
               'Ein `Greif` ist ein Reittier, das doppelt so schnell ist (`getTempo()` überschrieben). Im `Stall` stehen die '
               'Tiere lückenlos in `boxen[0]` bis `boxen[anzahl − 1]`.')


def J(main):
    return run(1, main, RT)


def build():
    B = []
    P = 'W1-B'

    # ---------------- B-01 match Bestandteile
    refl = J('''for (String m : new String[]{"getTempo", "istBereit", "satteln", "reiten"}) {
      for (java.lang.reflect.Method x : Reittier.class.getDeclaredMethods()) if (x.getName().equals(m)) println(m + ";" + x.getReturnType());
    }''')
    check(refl == ['getTempo;int', 'istBereit;boolean', 'satteln;void', 'reiten;void'], 'W1-B-01 Rueckgabetypen Reittier')
    B.append(aufgabe(
        f'{P}-01', 'Anatomie des Reittiers', 1, 'Bestandteile einer Klasse', [],
        [KONTEXT, KK_REITTIER, text('Ordne jedes Element der Klassenkarte dem passenden Bestandteil zu.')],
        match([('e1', '`- ausdauer: Ganzzahl`'), ('e2', '`+ c Reittier(name: Zeichenkette)`'), ('e3', '`+ getTempo(): Ganzzahl`'),
               ('e4', '`+ istBereit(): Wahrheitswert`'), ('e5', '`+ satteln(): nichts`'), ('e6', '`+ reiten(strecke: Ganzzahl): nichts`')],
              [('att', 'Attribut'), ('kon', 'Konstruktor'), ('son', 'sondierende Methode'), ('ver', 'verändernde Methode')]),
        {'e1': 'att', 'e2': 'kon', 'e3': 'son', 'e4': 'son', 'e5': 'ver', 'e6': 'ver'}, [],
        '`ausdauer` ist ein privates Attribut. `c` kennzeichnet den Konstruktor. `getTempo()` und `istBereit()` liefern nur '
        'Informationen (sondierend), `satteln()` und `reiten(…)` verändern den Zustand (`gesattelt` bzw. `ausdauer`).'))

    # ---------------- B-02 gaps Klassenkarte aus Java
    java_rt = '''public class Reittier {
    private String name;
    private int tempo;
    private int ausdauer;
    private boolean gesattelt;

    public Reittier(String name, int tempo, int ausdauer) { ... }
    public boolean istBereit() { ... }
    public void reiten(int strecke) { ... }
    ...
}'''
    refl = J('''java.lang.reflect.Field f = Reittier.class.getDeclaredField("gesattelt");
    println(java.lang.reflect.Modifier.isPrivate(f.getModifiers()) ? "-" : "+"); println(f.getType());
    println(Reittier.class.getDeclaredConstructor(String.class, int.class, int.class).getParameterTypes()[1]);
    println(Reittier.class.getDeclaredMethod("istBereit").getReturnType());
    println(Reittier.class.getDeclaredMethod("reiten", int.class).getReturnType());''')
    DE = {'int': 'Ganzzahl', 'boolean': 'Wahrheitswert', 'void': 'nichts'}
    loes = {'g1': [refl[0]], 'g2': [DE[refl[1]]], 'g3': [DE[refl[2]]], 'g4': [DE[refl[3]]], 'g5': [DE[refl[4]]]}
    check(loes == {'g1': ['-'], 'g2': ['Wahrheitswert'], 'g3': ['Ganzzahl'], 'g4': ['Wahrheitswert'], 'g5': ['nichts']}, 'W1-B-02 Klassenkarte aus Reflection')
    B.append(aufgabe(
        f'{P}-02', 'Vom Code zur Karte', 1, 'Klassendiagramm', ['P4'],
        [text('Ergänze die Klassenkarte zum Java-Code nach EH § 6.'), code(java_rt),
         klassenkarte('Reittier', ['- name: Zeichenkette', '- tempo: Ganzzahl', '- ausdauer: Ganzzahl', '[[g1]] gesattelt: [[g2]]'],
                      ['+ c Reittier(name: Zeichenkette, tempo: [[g3]], ausdauer: Ganzzahl)', '+ istBereit(): [[g4]]',
                       '+ reiten(strecke: Ganzzahl): [[g5]]', '…'])],
        gaps(g1=auswahl(['+', '-']), g2=auswahl(TYPEN), g3=auswahl(TYPEN), g4=auswahl(TYPEN), g5=auswahl(TYPEN)), loes, [],
        '`private` → −; `boolean` → Wahrheitswert; `int` → Ganzzahl; `void` → nichts. Konstruktoren tragen ein `c` und '
        'keinen Rückgabetyp; nicht gezeigte Elemente werden durch „…" ersetzt.'))

    # ---------------- B-03 choice welcher Aufruf
    calls = [('a', 'new Reittier("Blitz")'), ('b', 'new Reittier("Blitz", 14, 80)'), ('c', 'new Reittier("Blitz", 14)'),
             ('d', 'new Greif("Sturm", 12, 90, 6)')]
    fehl = [k for k, c in calls if not compiles(1, f'Reittier r = {c};', RT)]
    check(fehl == ['c'], 'W1-B-03 nur new Reittier("Blitz", 14) uebersetzt nicht')
    B.append(aufgabe(
        f'{P}-03', 'Der falsche Stallschlüssel', 1, 'Bestandteile einer Klasse', ['P3'],
        [KONTEXT, KK_REITTIER, KK_GREIF, text('Welcher Ausdruck führt zu einem **Übersetzungsfehler**?')],
        choice([(k, f'`{c}`') for k, c in calls]), {'richtig': fehl}, [],
        '`Reittier` ist überladen: ein Konstruktor mit einem Parameter, einer mit drei. Für (Zeichenkette, Ganzzahl) gibt '
        'es **keinen** passenden Konstruktor. `new Greif(…)` mit vier Argumenten passt zum Greif-Konstruktor.'))

    # ---------------- B-04 choice Klassendiagramm
    B.append(aufgabe(
        f'{P}-04', 'Linien und Pfeile im Stall', 1, 'Klassendiagramm', [],
        [KONTEXT, KK_STALL, text('Welche Beschreibung des Klassendiagramms mit `Stall`, `Reittier` und `Greif` entspricht EH § 6?')],
        choice([('a', '`Stall` – `Reittier`: einfache Linie ohne Beschriftung; `Greif` → `Reittier`: Pfeil mit hohler Dreiecksspitze zu `Reittier`.'),
                ('b', '`Stall` – `Reittier`: Linie mit Kardinalität `0..*`; `Reittier` → `Greif`: Pfeil mit hohler Spitze zu `Greif`.'),
                ('c', '`Stall` – `Greif`: einfache Linie, weil Greife auch im Stall stehen; `Greif` → `Reittier`: einfache Linie.'),
                ('d', 'Keine Linie zwischen `Stall` und `Reittier`, weil `boxen` eine Reihung ist; `Greif` → `Reittier`: Pfeil mit hohler Spitze.')]),
        {'richtig': ['a']}, [],
        '`Stall` hat das Attribut `boxen: Reihung von Reittier` → Assoziation als einfache, unbeschriftete Linie zu '
        '`Reittier` (auch bei Reihungen, ohne Kardinalitäten). Vererbung: hohle Dreiecksspitze von der Unterklasse `Greif` '
        'zur Oberklasse `Reittier`. Eine zusätzliche Linie Stall – Greif ist nicht nötig: Ein Greif *ist ein* Reittier.'))

    # ---------------- B-05 Signatur -> Java-Kopf
    heads = {'g1': 'public void satteln()', 'g2': 'public Reittier getReittier(int i)', 'g3': 'public Stall(int groesse)'}
    ok, err = compile_standalone({'S.java': 'class Reittier { public void satteln() {} }\nclass Stall {\n public Reittier getReittier(int i) { return null; }\n public Stall(int groesse) {}\n}'})
    check(ok, 'W1-B-05 Methodenkoepfe kompilieren')
    B.append(aufgabe(
        f'{P}-05', 'Köpfe für den Stall', 1, 'Methodenkopf und Signatur', ['P3'],
        [text('Schreibe zu den Signaturen aus den Klassenkarten die Java-Köpfe mit Sichtbarkeit (ohne `{`).'),
         text('`+ satteln(): nichts` (in Reittier) → [[g1]]'),
         text('`+ getReittier(i: Ganzzahl): Reittier` (in Stall) → [[g2]]'),
         text('`+ c Stall(groesse: Ganzzahl)` → [[g3]]')],
        gaps(g1=txt('code', 26), g2=txt('code', 36), g3=txt('code', 26)), {g: kopf(h) for g, h in heads.items()}, [],
        '`: nichts` → `void`; der Rückgabetyp `Reittier` ist ein Klassenname und bleibt stehen; `Ganzzahl` → `int`. '
        'Der Konstruktor hat keinen Rückgabetyp und heißt wie die Klasse: `public Stall(int groesse)`.'))

    # ---------------- B-06 Referenzen
    code06 = '''Reittier r1 = new Reittier("Blitz", 14, 60);
Reittier r2 = r1;
Reittier r3 = new Reittier("Blitz", 14, 60);
r2.satteln();
r1.reiten(25);
r3.reiten(25);
println(r1.getAusdauer());
println(r3.getAusdauer());
println(r1 == r3);
println(r1.getName().equals(r3.getName()));'''
    out = J(code06)
    check(out == ['35', '60', 'false', 'true'], 'W1-B-06 Ausgaben 35/60/false/true')
    B.append(aufgabe(
        f'{P}-06', 'Zwei Blitze', 2, 'Objektkarten und Referenzen', ['P5'],
        [KONTEXT, code(code06),
         text('Es gibt [[g0]] Reittier-Objekte. Ausgaben: [[g1]] · [[g2]] · [[g3]] · [[g4]]')],
        gaps(g0=zahl(), g1=zahl(), g2=zahl(), g3=auswahl(WF), g4=auswahl(WF)),
        {'g0': [str(code06.count('new Reittier'))], 'g1': [out[0]], 'g2': [out[1]], 'g3': [out[2]], 'g4': [out[3]]}, [],
        'Zwei `new` → **2** Objekte; r1 und r2 verweisen auf dasselbe. `r2.satteln()` sattelt also auch „r1" → `reiten(25)` '
        'wirkt: 60 − 25 = **35**. r3 ist ein eigenes, **nicht gesatteltes** Objekt → Ausdauer bleibt **60**. '
        '`r1 == r3` vergleicht Referenzen → false; `equals` vergleicht die Namen inhaltlich → true.'))

    # ---------------- B-07 Trace schnellstes (Polymorphie + Gleichstand)
    stall = [('Reittier', 'Blitz', 14, 60), ('Reittier', 'Moos', 9, 80), ('Greif', 'Sturm', 8, 90), ('Reittier', 'Nebel', 16, 70),
             ('Greif', 'Funke', 7, 50)]
    def mk(t):
        k, n, tp, a = t
        return f'new Greif("{n}", {tp}, {a}, 5)' if k == 'Greif' else f'new Reittier("{n}", {tp}, {a})'
    instr = RT.replace('            if (boxen[i].getTempo() > bester.getTempo()) {\n                bester = boxen[i];\n            }',
                       '            if (boxen[i].getTempo() > bester.getTempo()) {\n                bester = boxen[i];\n            }\n'
                       '            println(i + ";" + boxen[i].getTempo() + ";" + bester.getName());')
    out = run(1, 'Stall s = new Stall(6);' + ''.join(f' s.einstellen({mk(t)});' for t in stall) + ' println(s.schnellstes().getName());', instr)
    rows = [r.split(';') for r in out[:-1]]
    names = [t[1] for t in stall]
    zeilen = [['–', '–', 'Blitz']]
    loes, felder = {}, {}
    for r in rows:
        i = r[0]
        zeilen.append([i, f'[[t{i}]]', f'[[b{i}]]'])
        loes[f't{i}'] = [r[1]]; felder[f't{i}'] = zahl()
        loes[f'b{i}'] = [r[2]]; felder[f'b{i}'] = auswahl(names)
    loes['r'] = [out[-1]]; felder['r'] = auswahl(names)
    check(out[-1] == 'Sturm' and [r[1] for r in rows] == ['9', '16', '16', '14'], 'W1-B-07 schnellstes(): Sturm (Greif 8*2=16, Gleichstand mit Nebel)')
    B.append(aufgabe(
        f'{P}-07', 'Wer ist am schnellsten?', 2, 'Tracetabelle', ['P8'],
        [KONTEXT,
         code('''public Reittier schnellstes() {
    if (anzahl == 0) {
        return null;
    }
    Reittier bester = boxen[0];
    for (int i = 1; i < anzahl; i++) {
        if (boxen[i].getTempo() > bester.getTempo()) {
            bester = boxen[i];
        }
    }
    return bester;
}'''),
         text('Im Stall stehen (Index 0 bis 4): ' + ', '.join(f'{n} ({k}, tempo = {tp})' for k, n, tp, a in stall) + '.'),
         tabelle(['i', 'boxen[i].getTempo()', 'bester (Name)'], zeilen), text('Rückgabe: [[r]]')],
        gaps(**felder), loes, [],
        'Für Greife läuft die **überschriebene** `getTempo()`: Sturm 8 · 2 = 16, Funke 7 · 2 = 14. i = 1: 9 > 14? nein. '
        'i = 2: 16 > 14 → Sturm. i = 3: Nebel 16 > 16? **nein** (Gleichstand → der erste bleibt). i = 4: 14 > 16? nein. '
        'Rückgabe: **Sturm**.'))

    # ---------------- B-08 choice Polymorphie
    code08 = '''Reittier a = new Greif("Sturm", 8, 90, 6);
Greif g = new Greif("Wolke", 5, 70, 4);
println(a.getTempo() + g.getTempo());'''
    out = J(code08)
    check(out == ['26'], 'W1-B-08 16 + 10 = 26')
    B.append(aufgabe(
        f'{P}-08', 'Doppelt so schnell', 2, 'Funktionsweise erläutern', [],
        [KONTEXT, KK_GREIF, code(code08), text('Was wird ausgegeben?')],
        choice([('a', '`13`'), ('b', '`26`'), ('c', '`21`'), ('d', 'Übersetzungsfehler, weil `a` den Typ `Reittier` hat')]),
        {'richtig': ['b']}, [],
        'Beide Objekte sind Greife. Auch über die Variable `a` vom Typ `Reittier` läuft die **überschriebene** Methode des '
        'Objekts (dynamisches Binden): 8 · 2 = 16 und 5 · 2 = 10, zusammen **26**. `getTempo()` gibt es in `Reittier`, '
        'der Aufruf ist also erlaubt.'))

    # ---------------- B-09 Bug-Hunt finde (3 Fehler)
    code09 = '''public Reittier finde(String name) {
    for (int i = 0; i <= anzahl; i++) {
        if (boxen[i].getName() == name) {
            return boxen[i];
        }
        return null;
    }
    return null;
}'''
    bug = RT.replace('class Stall {', 'class Stall {\n    public Reittier findeB(String name) {\n' +
                     '\n'.join('    ' + l for l in code09.split('\n')[1:]) + '\n')
    o, e = java(1, 'Stall s = new Stall(3); s.einstellen(new Reittier("Blitz")); s.einstellen(new Reittier("Moos")); println(s.findeB("Moos"));', RT.replace('class Stall {', 'class Stall {\n' + code09.replace('finde(', 'findeB(') + '\n'))
    check(o.strip() == 'null', 'W1-B-09 Fehler Zeile 6: zweites Tier wird nie gefunden (null)')
    o, e = java(1, 'Stall s = new Stall(3); println(s.findeB("Moos"));', RT.replace('class Stall {', 'class Stall {\n' + code09.replace('finde(', 'findeB(') + '\n'))
    check('NullPointerException' in e, 'W1-B-09 Fehler Zeile 2: leerer Stall -> boxen[0] null -> NullPointerException')
    v2 = ['for (int i = 0; i < anzahl; i++) {', 'for (int i = 0; i <= anzahl - 1; i++) {']
    v3 = ['if (boxen[i].getName().equals(name)) {', 'if (name.equals(boxen[i].getName())) {']
    for a2 in v2:
        for a3 in v3:
            fx = code09.replace('finde(', 'findeB(').replace('    for (int i = 0; i <= anzahl; i++) {', '    ' + a2) \
                .replace('        if (boxen[i].getName() == name) {', '        ' + a3).replace('        return null;\n    }\n    return null;', '    }\n    return null;')
            out = run(1, 'Stall s = new Stall(3); println(s.findeB("Moos")); s.einstellen(new Reittier("Blitz")); s.einstellen(new Reittier("Moos"));'
                      ' s.einstellen(new Reittier("Nebel")); println(s.findeB(new String("Moos")).getName()); println(s.findeB("Wind"));',
                      RT.replace('class Stall {', 'class Stall {\n' + fx + '\n'))
            check(out == ['null', 'Moos', 'null'], f'W1-B-09 Korrektur ({a2} / {a3} / Zeile 6 loeschen) korrekt')
    B.append(aufgabe(
        f'{P}-09', 'Die verlorene Box', 3, 'Fehler im Java-Code', ['P1', 'P5', 'P6'],
        [KONTEXT, text('`finde(name)` soll das erste Reittier mit dem Namen liefern, sonst null. Die Implementierung enthält **drei** Fehler.'),
         code(code09),
         text('**a)** Markiere die drei fehlerhaften Zeilen. **b)** Korrigiere: Zeile mit der Schleife: [[g1]]'),
         text('Zeile mit der Bedingung: [[g2]]'),
         text('Die dritte fehlerhafte Zeile muss [[g3]]')],
        [lines(2, 3), gaps(g1=txt('code', 36), g2=txt('code', 40),
                           g3=auswahl(['gelöscht werden (nur das return nach der Schleife bleibt)', 'durch `return boxen[i];` ersetzt werden',
                                       'in den if-Block verschoben werden', 'bleiben, sie ist korrekt']))],
        [{'zeilen': [2, 3, 6]}, {'g1': varianten(*v2), 'g2': varianten(*v3), 'g3': ['gelöscht werden (nur das return nach der Schleife bleibt)']}],
        ['Was passiert bei einem leeren Stall? Was, wenn das gesuchte Tier an Index 1 steht?'],
        'Zeile 2: `i <= anzahl` greift auf `boxen[anzahl]` zu – dort steht `null` (bzw. Index außerhalb) → Laufzeitfehler '
        '(P1/P6); richtig `i < anzahl`. Zeile 3: Zeichenketten mit `equals` vergleichen, nicht mit `==` (P5). Zeile 6: '
        '`return null` **in** der Schleife beendet die Suche schon nach dem ersten Tier – es muss weg, das `return null` nach '
        'der Schleife genügt.'))

    # ---------------- B-10 match Ausdruecke
    code10 = '''Stall s = new Stall(4);
Reittier a = new Reittier("Blitz");
Reittier b = new Greif("Sturm", 8, 90, 6);
s.einstellen(a);
s.einstellen(b);
s.einstellen(a);'''
    ausdr = [('e1', 's.getAnzahl() == 3'), ('e2', 's.getReittier(0) == s.getReittier(2)'), ('e3', 's.getReittier(1) == b'),
             ('e4', 's.getReittier(1).getTempo() == 8'), ('e5', 's.getReittier(2) == b'), ('e6', 's.getReittier(5) == null')]
    out = J(code10 + '\n' + '\n'.join(f'println({x});' for _, x in ausdr))
    loes = {k: ('w' if v == 'true' else 'f') for (k, _), v in zip(ausdr, out)}
    check(out == ['true', 'true', 'true', 'false', 'false', 'true'], 'W1-B-10 Ausdruecke per Java')
    B.append(aufgabe(
        f'{P}-10', 'Doppelt eingestellt', 2, 'Objektkarten und Referenzen', ['P1'],
        [KONTEXT, code(code10), text('Ordne jeden Ausdruck seinem Wert nach Zeile 6 zu.')],
        match([(k, f'`{x}`') for k, x in ausdr], [('w', 'true'), ('f', 'false')]), loes, [],
        'Die Reihung speichert **Referenzen**: Box 0 und Box 2 verweisen auf dasselbe Objekt a (anzahl = 3). Box 1 verweist '
        'auf den Greif b; sein `getTempo()` liefert 16, nicht 8. `getReittier(5)` ist ein ungültiger Index → null (laut '
        'Klassenbeschreibung, kein Laufzeitfehler).'))

    # ---------------- B-11 Parsons anzahlBereit
    teile = [('a', 'public int anzahlBereit() {'), ('b', '    int zaehler = 0;'), ('c', '    for (int i = 0; i < anzahl; i++) {'),
             ('d', '        if (boxen[i].istBereit()) {'), ('e', '            zaehler++;'), ('f', '        }'), ('g', '    }'),
             ('h', '    return zaehler;'), ('i', '}'),
             ('x', '    for (int i = 0; i < boxen.length; i++) {'), ('y', '            return zaehler;'),
             ('z', '        if (boxen[i].istBereit() == "true") {')]
    T = dict(teile)
    reih = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']]
    for r in reih:
        m = '\n'.join(T[k] for k in r).replace('anzahlBereit(', 'anzahlBereitP(')
        out = run(1, 'Stall s = new Stall(5); println(s.anzahlBereitP()); Reittier a = new Reittier("A"); a.satteln(); s.einstellen(a);'
                  ' s.einstellen(new Reittier("B")); Reittier c = new Reittier("C", 10, 5); c.satteln(); c.reiten(9); s.einstellen(c);'
                  ' Greif g = new Greif("G", 5, 5, 2); g.satteln(); s.einstellen(g); println(s.anzahlBereitP());',
                  RT.replace('class Stall {', 'class Stall {\n' + m + '\n'))
        check(out == ['0', '2'], 'W1-B-11 Parsons anzahlBereit')
    B.append(aufgabe(
        f'{P}-11', 'Puzzle: Bereit zum Ausritt', 2, 'Methode implementieren', ['P1', 'P6'],
        [KONTEXT, text('Setze `anzahlBereit(): Ganzzahl` der Klasse `Stall` zusammen: Sie liefert die Anzahl der Reittiere, '
                       'die bereit sind. Nicht alle Teile werden gebraucht.')],
        order(teile), {'reihenfolgen': reih}, [],
        'Zähl-Baustein: Zähler mit 0 starten, über die **belegten** Boxen laufen (`i < anzahl` – `boxen.length` würde auf '
        '`null` zugreifen, P1/P6), bei jedem bereiten Tier erhöhen und **nach** der Schleife zurückgeben. `istBereit()` '
        'liefert einen Wahrheitswert, der direkt als Bedingung dient – der Vergleich mit dem Text "true" ist falsch.'))

    # ---------------- B-12 Gesamtprogramm
    code12 = '''Stall s = new Stall(3);
Reittier blitz = new Reittier("Blitz", 14, 40);
Greif sturm = new Greif("Sturm", 8, 90, 6);
s.einstellen(blitz);
s.einstellen(sturm);
s.einstellen(new Reittier("Moos"));
boolean ok = s.einstellen(new Reittier("Nebel"));
blitz.satteln();
sturm.satteln();
blitz.reiten(50);
sturm.reiten(30);
println(ok);
println(s.anzahlBereit());
println(s.schnellstes().getName());
println(blitz.getAusdauer() + sturm.getAusdauer());'''
    out = J(code12)
    check(out == ['false', '1', 'Sturm', '60'], 'W1-B-12 Ausgaben false/1/Sturm/60')
    B.append(aufgabe(
        f'{P}-12', 'Ein voller Stall', 3, 'Objektkarten und Referenzen', ['P1'],
        [KONTEXT, KK_STALL, code(code12), text('Ausgaben: Zeile 12: [[g1]] · Zeile 13: [[g2]] · Zeile 14: [[g3]] · Zeile 15: [[g4]]')],
        gaps(g1=auswahl(WF), g2=zahl(), g3=auswahl(['Blitz', 'Sturm', 'Moos', 'Nebel']), g4=zahl()),
        {'g1': [out[0]], 'g2': [out[1]], 'g3': [out[2]], 'g4': [out[3]]}, [],
        'Der Stall hat 3 Boxen – Nebel passt nicht mehr: `ok` = **false**. Blitz: 40 − 50 → 0 (nie unter 0), also nicht '
        'bereit; Sturm: 90 − 30 = 60, gesattelt → bereit; Moos ist nicht gesattelt → **1** bereites Tier. Tempo: Blitz 14, '
        'Sturm 8 · 2 = 16, Moos 10 → **Sturm**. Ausdauer zusammen: 0 + 60 = **60**.'))

    # ---------------- B-13 Bug-Hunt Greif
    code13 = '''public class Greif extends Reittier {
    private int spannweite;

    public Greif(String name, int tempo, int ausdauer, int spannweite) {
        super(name, tempo, ausdauer);
        spannweite = spannweite;
    }

    public int getSpannweite() {
        return spannweite;
    }

    public int getTempo() {
        return tempo * 2;
    }
}'''
    base = RT.split('class Greif')[0] + RT[RT.index('class Stall'):]
    gx = code13.replace('public class Greif', 'class GreifX').replace('public Greif(', 'public GreifX(')
    check(not compiles(1, 'GreifX g = new GreifX("S", 8, 90, 6);', base + gx), 'W1-B-13 Zeile 14: tempo privat -> Uebersetzungsfehler')
    v6 = ['this.spannweite = spannweite;']
    v14 = ['return super.getTempo() * 2;', 'return 2 * super.getTempo();', 'return super.getTempo() + super.getTempo();']
    nur14 = gx.replace('        return tempo * 2;', '        ' + v14[0])
    out = run(1, 'GreifX g = new GreifX("S", 8, 90, 6); println(g.getSpannweite());', base + nur14)
    check(out == ['0'], 'W1-B-13 Zeile 6: ohne this bleibt spannweite 0')
    for a6 in v6:
        for a14 in v14:
            fx = gx.replace('        spannweite = spannweite;', '        ' + a6).replace('        return tempo * 2;', '        ' + a14)
            out = run(1, 'Reittier g = new GreifX("S", 8, 90, 6); println(g.getTempo()); println(((GreifX) g).getSpannweite());', base + fx)
            check(out == ['16', '6'], f'W1-B-13 Korrektur {a6} / {a14}')
    rek = gx.replace('        spannweite = spannweite;', '        this.spannweite = spannweite;').replace('        return tempo * 2;', '        return getTempo() * 2;')
    o, e = java(1, 'Reittier g = new GreifX("S", 8, 90, 6); println(g.getTempo());', base + rek)
    check('StackOverflowError' in e, 'W1-B-13 "return getTempo() * 2" ruft sich selbst auf -> StackOverflowError (nicht akzeptiert)')
    B.append(aufgabe(
        f'{P}-13', 'Der flügellahme Greif', 3, 'Fehler im Java-Code', ['P3'],
        [KONTEXT, text('Die Klasse `Greif` enthält **zwei** Fehler.'), code(code13),
         text('**a)** Markiere die beiden fehlerhaften Zeilen. **b)** Korrektur der Zeile im Konstruktor: [[g1]]'),
         text('Korrektur der Zeile in `getTempo()`: [[g2]]')],
        [lines(2, 2), gaps(g1=txt('code', 32), g2=txt('code', 32))],
        [{'zeilen': [6, 14]}, {'g1': varianten(*v6), 'g2': varianten(*v14)}],
        ['Kann die Unterklasse auf das private Attribut `tempo` zugreifen?'],
        'Zeile 6: Ohne `this` wird der Parameter sich selbst zugewiesen, das Attribut bleibt 0 → `this.spannweite = spannweite;`. '
        'Zeile 14: `tempo` ist in `Reittier` privat → Übersetzungsfehler. Richtig: `return super.getTempo() * 2;`. '
        'Achtung: `return getTempo() * 2;` ohne `super` ruft die eigene Methode immer wieder auf (Endlosrekursion).'))

    # ---------------- B-14 kompiliert?
    stmts = [('g1', 'Reittier r = new Greif("Sturm", 8, 90, 6);'), ('g2', 'Greif g = new Reittier("Blitz");'),
             ('g3', 'Reittier r = new Greif("Sturm", 8, 90, 6);\nprintln(r.getSpannweite());'),
             ('g4', 'Stall s = new Stall(2);\ns.einstellen(new Greif("Wolke", 5, 70, 4));'),
             ('g5', 'Greif g = new Greif("Wolke", 5, 70, 4);\nReittier r = g;\nprintln(r.getTempo());')]
    loes = {g: ['ja' if compiles(1, s, RT) else 'nein'] for g, s in stmts}
    check([loes[g][0] for g, _ in stmts] == ['ja', 'nein', 'nein', 'ja', 'ja'], 'W1-B-14 Uebersetzbarkeit per javac')
    B.append(aufgabe(
        f'{P}-14', 'Typen im Stall', 2, 'Fehler im Java-Code', ['P4'],
        [KONTEXT, KK_GREIF, text('Entscheide, ob die Anweisungen übersetzt werden.'),
         tabelle(['Anweisung(en)', 'übersetzt?'], [[f'`{s.replace(chr(10), " ")}`', f'[[{g}]]'] for g, s in stmts])],
        gaps(**{g: auswahl(JA_NEIN) for g, _ in stmts}), loes, [],
        'Ein Greif darf überall stehen, wo ein Reittier erwartet wird (Variable, Parameter von `einstellen`) – umgekehrt nicht. '
        'Über eine Variable vom Typ `Reittier` sind nur Methoden aus `Reittier` aufrufbar: `getSpannweite()` ✗, `getTempo()` ✓ '
        '(es läuft dann die Greif-Version).'))

    # ---------------- B-15 choice: welcher Code erzeugt den Zustand?
    varis = [('a', 'Reittier a = new Reittier("Blitz"); Reittier b = new Reittier("Moos"); Reittier c = a; c.satteln(); a.reiten(30);'),
             ('b', 'Reittier a = new Reittier("Blitz"); Reittier c = new Reittier("Blitz"); Reittier b = c; a.satteln(); a.reiten(30);'),
             ('c', 'Reittier a = new Reittier("Blitz"); Reittier b = new Reittier("Moos"); Reittier c = a; a.reiten(30); c.satteln();'),
             ('d', 'Reittier a = new Reittier("Blitz"); Reittier b = a; Reittier c = a; b.satteln(); c.reiten(30);')]
    richtig = []
    for k, v in varis:
        out = J(v + ' println(a == c); println(a != b && b != c); println(a.getAusdauer()); println(b.getAusdauer());')
        if out == ['true', 'true', '70', '100']:
            richtig.append(k)
    check(richtig == ['a'], 'W1-B-15 nur Variante a erzeugt den beschriebenen Zustand (Java)')
    B.append(aufgabe(
        f'{P}-15', 'Welcher Code war es?', 3, 'Objektkarten und Referenzen', [],
        [KONTEXT, text('Nach Ausführung eines Programmausschnitts gilt: Es gibt genau **zwei** Reittier-Objekte. `a` und `c` '
                       'verweisen auf **dasselbe** Objekt mit ausdauer = 70; `b` verweist auf das **andere** Objekt mit '
                       'ausdauer = 100. Welcher Ausschnitt erzeugt genau diesen Zustand?')],
        choice([(k, f'`{v}`') for k, v in varis]), {'richtig': richtig},
        ['Zeichne für jede Variante die Objektkarten mit Referenzpfeilen.'],
        'Nur a passt: zwei `new`, `c = a` (gleiches Objekt), erst satteln, dann reiten → 100 − 30 = 70. In b sind a und c '
        'verschiedene Objekte; in c wird geritten, **bevor** gesattelt ist – die Ausdauer bleibt 100; in d gibt es nur ein '
        'Objekt, auf das alle drei Variablen zeigen.'))
    return B
