"""Welt 1 – Die Heldenschmiede: Aufgaben fuer Algo Quest Lab (mit Java-Verifikation)."""
from lib import *

A = []          # alle Aufgaben
LEVELS = []
TYPEN_KK = TYPEN


def J(main, extra=''):
    return run(1, main, extra)


# =====================================================================
# LEVEL 1.1 – Klasse und Objekt (DS 8)
# =====================================================================
L = 'W1-L1'

# ---------- 01 match Klasse/Objekt/Attributwert
code01 = '''Held lio = new Held("Lio");
Monster ork = new Monster("Ork", 45, 7);
lio.nimmSchaden(30);'''
out = J(code01 + '\nprintln(lio.getLeben()); println(ork.getLeben()); println(lio.getName());')
check(out == ['70', '45', 'Lio'], 'W1-L1-01 Lio hat nach nimmSchaden(30) 70 Leben, Ork 45')
A.append(aufgabe(
    f'{L}-01', 'Bauplan, Exemplar oder Zustand?', 1, 'Klasse vs. Objekt', [],
    [text('Im Hauptprogramm der Heldenschmiede steht:'), code(code01),
     text('Ordne jede Beschreibung zu: Ist das eine **Klasse** (Bauplan), ein **Objekt** (konkretes Exemplar) '
          'oder ein **Attributwert** (Teil des Zustands eines Objekts)?')],
    match([('e1', '`Held` – legt fest, dass jeder Held einen Namen, Leben und Stärke hat'),
           ('e2', 'das Exemplar, das `new Held("Lio")` erzeugt'),
           ('e3', '`leben = 70` bei Lio nach Zeile 3'),
           ('e4', '`Monster` – beschreibt, was alle Gegner können'),
           ('e5', 'der Ork mit 45 Leben und Stärke 7'),
           ('e6', '`name = "Lio"`')],
          [('k', 'Klasse'), ('o', 'Objekt'), ('w', 'Attributwert')]),
    {'e1': 'k', 'e2': 'o', 'e3': 'w', 'e4': 'k', 'e5': 'o', 'e6': 'w'},
    ['Eine Klasse gibt es einmal im Programm, Objekte entstehen erst mit `new` – beliebig viele.'],
    'Die **Klasse** ist der Bauplan (`Held`, `Monster`): Sie legt fest, *welche* Attribute und Methoden es gibt. '
    'Ein **Objekt** ist ein mit `new` erzeugtes Exemplar mit eigenen Werten (Lio, der Ork). '
    'Ein **Attributwert** gehört zum Zustand genau eines Objekts: Lio hat nach `nimmSchaden(30)` den Wert `leben = 70`, '
    'der Ork behält seine 45 – Schaden für Lio ändert nichts an anderen Objekten.'))

# ---------- 02 match Bestandteile
held_kopf = '''public class Held {
    private String name;
    private int leben;
    private int maxLeben;
    private int staerke;
    private int gold;

    public Held(String name) { ... }
    public int getGold() { ... }
    public boolean istBesiegt() { ... }
    public void heilen(int punkte) { ... }
    public void erhalteGold(int betrag) { ... }
}'''
refl = J('''
java.lang.reflect.Field f = Held.class.getDeclaredField("gold");
println(java.lang.reflect.Modifier.isPrivate(f.getModifiers()));
println(Held.class.getDeclaredMethod("getGold").getReturnType());
println(Held.class.getDeclaredMethod("istBesiegt").getReturnType());
println(Held.class.getDeclaredMethod("heilen", int.class).getReturnType());
println(Held.class.getDeclaredMethod("erhalteGold", int.class).getReturnType());
println(Held.class.getDeclaredConstructor(String.class) != null);''')
check(refl == ['true', 'int', 'boolean', 'void', 'void', 'true'], 'W1-L1-02 Held: gold privat, getGold int, istBesiegt boolean, heilen/erhalteGold void')
A.append(aufgabe(
    f'{L}-02', 'Anatomie eines Helden', 1, 'Bestandteile einer Klasse', [],
    [text('Hier siehst du das Gerüst der Klasse `Held` (Methodenrümpfe ausgelassen).'), code(held_kopf),
     text('Ordne jedes Element dem passenden Bestandteil zu. *Sondierend* = liefert nur eine Information, ändert nichts; '
          '*verändernd* = ändert den Zustand des Objekts.')],
    match([('e1', '`private int gold;`'), ('e2', '`public Held(String name)`'), ('e3', '`public int getGold()`'),
           ('e4', '`public boolean istBesiegt()`'), ('e5', '`public void heilen(int punkte)`'),
           ('e6', '`public void erhalteGold(int betrag)`'), ('e7', '`private int maxLeben;`')],
          [('att', 'Attribut'), ('kon', 'Konstruktor'), ('son', 'sondierende Methode'), ('ver', 'verändernde Methode')]),
    {'e1': 'att', 'e2': 'kon', 'e3': 'son', 'e4': 'son', 'e5': 'ver', 'e6': 'ver', 'e7': 'att'},
    ['Der Konstruktor heißt wie die Klasse und hat keinen Rückgabetyp.'],
    '**Attribute** (`gold`, `maxLeben`) speichern den Zustand und sind privat. Der **Konstruktor** `Held(String name)` '
    'heißt wie die Klasse, hat keinen Rückgabetyp und setzt die Startwerte. **Sondierend** sind `getGold()` und '
    '`istBesiegt()` – sie liefern nur einen Wert. **Verändernd** sind `heilen` und `erhalteGold`: Sie ändern `leben` '
    'bzw. `gold` – kontrolliert (nie über `maxLeben`, nur positive Beträge).'))

# ---------- 03 choice mehrfach Kapselung
ok_set = compiles(1, 'Held aria = new Held("Aria");\naria.leben = 500;')
check(ok_set is False, 'W1-L1-03 aria.leben = 500 ist ein Uebersetzungsfehler (privat)')
ok_void, _ = compile_standalone({'Tuer.java': 'class Tuer { private int n; public void Tuer(int n) { this.n = n; } }\n'
                                 'class T { void t() { Tuer t = new Tuer(); t.Tuer(3); } }'})
check(ok_void, 'W1-L1-03 "public void Held(...)" waere eine normale Methode (kompiliert, kein Konstruktor)')
A.append(aufgabe(
    f'{L}-03', 'Privat ist Absicht', 2, 'Bestandteile einer Klasse', [],
    [text('Welche Aussagen über die Klasse `Held` (Attribute privat, Methoden öffentlich, kein Setter für `leben`) '
          'sind **richtig**? Wähle alle richtigen aus.')],
    choice([('a', 'Weil `leben` privat ist, kann ein Hauptprogramm nur über Methoden wie `nimmSchaden` oder `heilen` darauf einwirken.'),
            ('b', 'Ein Konstruktor hat den Rückgabetyp `void`.'),
            ('c', 'Ein Konstruktor heißt genauso wie die Klasse und wird bei `new` aufgerufen.'),
            ('d', 'Die Anweisung `aria.leben = 500;` im Hauptprogramm ist erlaubt, weil `leben` ein Attribut von `aria` ist.'),
            ('e', 'Dass es keinen Setter für `leben` gibt, ist Absicht: So kann die Klasse selbst darauf achten, dass `leben` nie unter 0 oder über `maxLeben` liegt.'),
            ('f', 'Im Konstruktor bezeichnet `this.name` den Parameter `name`.')], mehrfach=True),
    {'richtig': ['a', 'c', 'e']},
    ['Prüfe jede Aussage einzeln. Was bedeutet das Minuszeichen in der Klassenkarte?'],
    'Richtig sind a, c und e. Das ist **Kapselung**: Private Attribute sind nur innerhalb der Klasse zugreifbar – '
    '`aria.leben = 500;` ist ein Übersetzungsfehler (d falsch). Ein Konstruktor hat **keinen** Rückgabetyp (b falsch); '
    'schreibt man `public void Held(…)`, entsteht eine gewöhnliche Methode und die Attribute behalten ihre Standardwerte. '
    '`this.name` ist das **Attribut** des eigenen Objekts, `name` allein der Parameter (f falsch).'))

# ---------- 04 gaps Klassenkarte
held_java = '''public class Held {
    private String name;
    private int leben;
    private int maxLeben;
    private int staerke;
    private int gold;

    public Held(String name) { ... }
    public String getName() { ... }
    public int getLeben() { ... }
    public boolean istBesiegt() { ... }
    public void nimmSchaden(int schaden) { ... }
    public void heilen(int punkte) { ... }
    public void erhalteGold(int betrag) { ... }
}'''
refl = J('''
java.lang.reflect.Field f = Held.class.getDeclaredField("name");
println(java.lang.reflect.Modifier.isPrivate(f.getModifiers()) ? "-" : "+");
println(Held.class.getDeclaredField("leben").getType());
println(Held.class.getDeclaredConstructor(String.class).getParameterTypes()[0].getSimpleName());
println(Held.class.getDeclaredMethod("istBesiegt").getReturnType());
println(Held.class.getDeclaredMethod("nimmSchaden", int.class).getReturnType());''')
DE = {'int': 'Ganzzahl', 'String': 'Zeichenkette', 'boolean': 'Wahrheitswert', 'void': 'nichts', 'double': 'Kommazahl', 'char': 'Zeichen'}
loes04 = {'g1': [refl[0]], 'g2': [DE[refl[1]]], 'g3': [DE[refl[2]]], 'g4': [DE[refl[3]]], 'g5': [DE[refl[4]]]}
check(loes04 == {'g1': ['-'], 'g2': ['Ganzzahl'], 'g3': ['Zeichenkette'], 'g4': ['Wahrheitswert'], 'g5': ['nichts']},
      'W1-L1-04 Klassenkarte Held per Reflection aus LSG-Klasse abgeleitet')
A.append(aufgabe(
    f'{L}-04', 'Die Klassenkarte des Helden', 2, 'Klassendiagramm', [],
    [text('Übertrage den Java-Code in die Klassenkarte nach EH § 6 (Sichtbarkeit, deutsche Typnamen, Konstruktor mit `c`).'),
     code(held_java),
     klassenkarte('Held', ['[[g1]] name: Zeichenkette', '- leben: [[g2]]', '- maxLeben: Ganzzahl', '- staerke: Ganzzahl', '- gold: Ganzzahl'],
                  ['+ c Held(name: [[g3]])', '+ getName(): Zeichenkette', '+ getLeben(): Ganzzahl', '+ istBesiegt(): [[g4]]',
                   '+ nimmSchaden(schaden: Ganzzahl): [[g5]]', '+ heilen(punkte: Ganzzahl): nichts', '+ erhalteGold(betrag: Ganzzahl): nichts'])],
    gaps(g1=auswahl(['+', '-']), g2=auswahl(TYPEN), g3=auswahl(TYPEN), g4=auswahl(TYPEN), g5=auswahl(TYPEN)),
    loes04,
    ['Übersetzung: int → Ganzzahl, String → Zeichenkette, boolean → Wahrheitswert, void → nichts.'],
    '`private` wird zu **−**, `public` zu **+**. Java-Typen werden in die deutschen Typnamen der Ergänzenden Hinweise '
    'übersetzt: `int` → Ganzzahl, `String` → Zeichenkette, `boolean` → Wahrheitswert. Eine Methode ohne Rückgabe '
    '(`void`) bekommt `: nichts`. Der Konstruktor steht mit vorangestelltem `c` und ohne Rückgabetyp in der Karte.'))

# ---------- 05 gaps Objektkarte nach Code
code05 = '''Held h = new Held("Brann");
h.nimmSchaden(35);
h.erhalteGold(-5);
h.erhalteGold(12);
h.heilen(50);
h.nimmSchaden(120);
h.heilen(15);
h.erhalteGold(8);'''
out = J(code05 + '\nprintln(h.getLeben()); println(h.getMaxLeben()); println(h.getStaerke()); println(h.getGold()); println(h.istBesiegt());')
A.append(aufgabe(
    f'{L}-05', 'Brann im Dauerstress', 3, 'Objektkarten und Referenzen', [],
    [text('Der Code wird ausgeführt (alle Methoden wie in Level 1.1 implementiert: `leben` nie unter 0 und nie über '
          '`maxLeben`, `erhalteGold` nur bei positivem Betrag).'), code(code05),
     text('Vervollständige die Objektkarte von `h` **nach** Zeile 8 und gib an, was `h.istBesiegt()` dann liefert.'),
     tabelle(['h: Held', 'Wert'], [['name', '"Brann"'], ['leben', '[[g1]]'], ['maxLeben', '[[g2]]'], ['staerke', '[[g3]]'],
                                   ['gold', '[[g4]]']]),
     text('`h.istBesiegt()` liefert [[g5]].')],
    gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=zahl(), g5=auswahl(WF)),
    {'g1': [out[0]], 'g2': [out[1]], 'g3': [out[2]], 'g4': [out[3]], 'g5': [out[4]]},
    ['Gehe Zeile für Zeile vor und notiere nach jeder Zeile `leben` und `gold`.',
     'Achte auf die Grenzen: Zeile 5 heilt nicht über 100, Zeile 6 setzt nicht unter 0.'],
    f'Ablauf von `leben`: 100 → 65 (Z. 2) → Z. 5: 65 + 50 = 115, begrenzt auf `maxLeben` = 100 → Z. 6: 100 − 120 < 0, '
    f'also 0 → Z. 7: 15. `gold`: −5 wird ignoriert, dann 12 und 8 → **{out[3]}**. `staerke` bleibt 10, `maxLeben` 100. '
    f'Da `leben` = {out[0]} > 0 ist, liefert `istBesiegt()` **{out[4]}** – ein Held mit 0 Leben kann durch Heilen wieder '
    'kampffähig werden.'))
check(out == ['15', '100', '10', '20', 'false'], 'W1-L1-05 Objektkarte Brann: 15/100/10/20/false (Java)')

# ---------- 06 Bug-Hunt this
code06 = '''public class Held {
    private String name;
    private int leben;
    private int maxLeben;

    public Held(String name) {
        name = name;
        maxLeben = 100;
        leben = maxLeben;
    }

    public String getName() {
        return name;
    }
}'''
bug = code06.replace('public class Held', 'class HeldB').replace('public Held(', 'public HeldB(')
out = J('HeldB h = new HeldB("Lio");\nprintln(h.getName());', bug)
check(out == ['null'], 'W1-L1-06 fehlerhafter Konstruktor: getName() liefert null')
for v in ['this.name = name;']:
    out2 = J('HeldB h = new HeldB("Lio");\nprintln(h.getName());', bug.replace('        name = name;', '        ' + v))
    check(out2 == ['Lio'], 'W1-L1-06 Korrektur this.name = name liefert "Lio"')
A.append(aufgabe(
    f'{L}-06', 'Der namenlose Held', 2, 'Fehler im Java-Code', [],
    [text('Nach `Held h = new Held("Lio");` liefert `h.getName()` nicht `"Lio"`. Der Compiler meldet keinen Fehler.'),
     code(code06),
     text('**a)** Markiere die fehlerhafte Zeile. **b)** Korrigierte Zeile: [[g1]] '
          '**c)** Was liefert `h.getName()` mit dem fehlerhaften Code? [[g2]]')],
    [lines(1, 1), gaps(g1=txt('code', 30), g2=auswahl(['"Lio"', 'null', '""', 'Übersetzungsfehler']))],
    [{'zeilen': [7]}, {'g1': varianten('this.name = name;'), 'g2': ['null']}],
    ['Der Parameter heißt genauso wie das Attribut. Welches `name` ist in Zeile 7 links gemeint?'],
    'In Zeile 7 verdeckt der Parameter `name` das gleichnamige Attribut: `name = name;` weist den Parameter sich selbst zu. '
    'Das Attribut behält seinen Standardwert `null`, deshalb liefert `getName()` **null** – und kein Compiler warnt. '
    'Korrektur: `this.name = name;` – `this.name` ist das Attribut des eigenen Objekts.'))

# ---------- 07 Parsons nimmSchaden
teile07 = [('a', 'public void nimmSchaden(int schaden) {'), ('b', '    leben = leben - schaden;'), ('c', '    if (leben < 0) {'),
           ('d', '        leben = 0;'), ('e', '    }'), ('f', '}'),
           ('x', '    return leben;'), ('y', '    if (leben > maxLeben) {'), ('z', 'public int nimmSchaden(int schaden) {')]
reih07 = [['a', 'b', 'c', 'd', 'e', 'f']]
T = dict(teile07)
for r in reih07:
    meth = '\n'.join(T[k] for k in r)
    out = J('HeldN h = new HeldN(); h.nimmSchaden(30); println(h.getLeben()); h.nimmSchaden(80); println(h.getLeben());'
            ' h.nimmSchaden(0); println(h.getLeben());',
            'class HeldN { private int leben = 100; private int maxLeben = 100;\n' + meth + '\npublic int getLeben() { return leben; } }')
    check(out == ['70', '0', '0'], 'W1-L1-07 Parsons nimmSchaden: 100-30=70, dann 0 (nie unter 0)')
A.append(aufgabe(
    f'{L}-07', 'Puzzle: Schaden mit Grenze', 3, 'Methode implementieren', ['P3'],
    [text('Setze die Methode `nimmSchaden(schaden: Ganzzahl): nichts` der Klasse `Held` zusammen: Der Schaden wird von '
          '`leben` abgezogen, `leben` fällt aber **nie unter 0**. Nicht alle Teile werden gebraucht.')],
    order(teile07), {'reihenfolgen': reih07},
    ['`: nichts` in der Signatur bedeutet in Java `void` – und dann gibt es kein `return` mit Wert.'],
    'Erst abziehen, dann korrigieren: `leben = leben - schaden;` und danach `if (leben < 0) { leben = 0; }`. '
    'Die Distraktoren: `public int …` und `return leben;` widersprechen der Signatur `: nichts` (P3 Signatur verfehlt); '
    '`if (leben > maxLeben)` gehört zu `heilen`, nicht zu `nimmSchaden`.'))

# ---------- 08 choice Objektkarte-Notation
A.append(aufgabe(
    f'{L}-08', 'Die richtige Objektkarte', 1, 'Objektkarten und Referenzen', [],
    [text('Ein Objekt wurde mit `Held held1 = new Held("Aria");` erzeugt. Welche Darstellung ist eine korrekte '
          '**Objektkarte** nach EH § 6?')],
    choice([('a', 'Kopf `held1: Held` · Zeilen `name = "Aria"`, `leben = 100`, `maxLeben = 100`, …'),
            ('b', 'Kopf `Held: held1` · Zeilen `name = "Aria"`, `leben = 100`, …'),
            ('c', 'Kopf `held1: Held` · Zeilen `- name: Zeichenkette`, `- leben: Ganzzahl`, …'),
            ('d', 'Kopf `Held` · Zeilen `+ c Held(name: Zeichenkette)`, `+ getLeben(): Ganzzahl`, …')]),
    {'richtig': ['a']},
    ['Eine Objektkarte zeigt ein Exemplar mit konkreten Werten zu einem Zeitpunkt.'],
    'Richtig ist a: Kopf **objektname: Klasse**, darunter jedes Attribut mit seinem **konkreten Wert** '
    '(Zeichenketten in Anführungszeichen). b vertauscht Objektname und Klasse, c zeigt Attribute mit Typen – das ist '
    'der Aufbau einer **Klassenkarte**, d ist der Methodenteil einer Klassenkarte.'))

LEVELS.append({"id": L, "nr": "1.1", "titel": "Die Schmiede öffnet – Klasse und Objekt", "ds": [8],
               "ab": "AB W1·1 Klassen und Objekte – Infoteile 1–3, Aufgaben 0–2",
               "ide": "AQ_W1_L1_Heldenschmiede_Geruest.txt – Level 1.1 (Klasse Held, Testklasse L11HeldTest)",
               "intro": [text('Eine **Klasse** ist ein Bauplan (Attribute + Methoden), ein **Objekt** ein mit `new` erzeugtes '
                              'Exemplar mit eigenen Attributwerten.'),
                         hinweis('**Merke:** Attribute `private` (−), Methoden und Konstruktoren `public` (+). Der Konstruktor '
                                 'heißt wie die Klasse und hat keinen Rückgabetyp. `this.name` ist das Attribut, `name` der Parameter.')],
               "aufgaben": [a['id'] for a in A if a['id'].startswith(L + '-')]})

# =====================================================================
# LEVEL 1.2 – Konstruktoren, Monster, Referenzen (DS 9)
# =====================================================================
L = 'W1-L2'

# ---------- 01 Welcher Konstruktor?
aufrufe = [('g1', 'new Held("Lio")'), ('g2', 'new Held("Mira", 120, 9)'), ('g3', 'new Held("Tom", 90)'),
           ('g4', 'new Held(120, 9, "Kai")'), ('g5', 'new Monster("Ork")'), ('g6', 'new Monster("Ork", 45, 7)')]
loes = {}
for g, a in aufrufe:
    var = 'Monster' if 'Monster' in a else 'Held'
    if not compiles(1, f'{var} x = {a};'):
        loes[g] = ['Übersetzungsfehler']
    elif var == 'Monster':
        loes[g] = ['Monster(name, leben, staerke)']
    else:
        ml = J(f'Held x = {a}; println(x.getMaxLeben()); println(x.getStaerke());')
        loes[g] = ['Held(name)'] if ml == ['100', '10'] else ['Held(name, maxLeben, staerke)']
check(loes == {'g1': ['Held(name)'], 'g2': ['Held(name, maxLeben, staerke)'], 'g3': ['Übersetzungsfehler'],
               'g4': ['Übersetzungsfehler'], 'g5': ['Übersetzungsfehler'], 'g6': ['Monster(name, leben, staerke)']},
      'W1-L2-01 Konstruktorwahl per javac/Laufzeit bestimmt')
opts = ['Held(name)', 'Held(name, maxLeben, staerke)', 'Monster(name, leben, staerke)', 'Übersetzungsfehler']
A.append(aufgabe(
    f'{L}-01', 'Zwei Wege in die Schmiede', 1, 'Bestandteile einer Klasse', ['P3'],
    [text('`Held` hat zwei Konstruktoren: `Held(name: Zeichenkette)` und `Held(name: Zeichenkette, maxLeben: Ganzzahl, '
          'staerke: Ganzzahl)`. `Monster` hat nur `Monster(name: Zeichenkette, leben: Ganzzahl, staerke: Ganzzahl)`. '
          'Gib an, welcher Konstruktor aufgerufen wird – oder ob der Compiler meckert.'),
     tabelle(['Aufruf', 'Konstruktor'], [[f'`{a}`', f'[[{g}]]'] for g, a in aufrufe])],
    gaps(**{g: auswahl(opts) for g, _ in aufrufe}), loes,
    ['Java wählt den Konstruktor nach Anzahl, Reihenfolge und Typen der Argumente.'],
    'Beim **Überladen** entscheidet die Parameterliste: Ein Argument vom Typ Zeichenkette → `Held(name)`, '
    'Zeichenkette + zwei Ganzzahlen → der zweite Konstruktor. `new Held("Tom", 90)` passt zu keiner Parameterliste, '
    '`new Held(120, 9, "Kai")` hat die richtige Anzahl, aber die falsche Reihenfolge der Typen. '
    '`Monster` hat keinen Konstruktor mit nur einem Namen → Übersetzungsfehler.'))

# ---------- 02 Referenzen umgebogen
code02 = '''Held x = new Held("Kira");
Held y = new Held("Kira", 120, 8);
Held z = x;
x = y;
z.nimmSchaden(30);
x.nimmSchaden(10);
println(y.getLeben());
println(z.getLeben());
println(x == y);
println(z == x);'''
out = J(code02)
anz_obj = code02.count('new Held')
A.append(aufgabe(
    f'{L}-02', 'Die Referenz wird umgebogen', 2, 'Objektkarten und Referenzen', [],
    [code(code02),
     text('Nach Zeile 4 gibt es [[g1]] Held-Objekte. Gib die vier Ausgaben an: Zeile 7: [[g2]] · Zeile 8: [[g3]] · '
          'Zeile 9: [[g4]] · Zeile 10: [[g5]]')],
    gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=auswahl(WF), g5=auswahl(WF)),
    {'g1': [str(anz_obj)], 'g2': [out[0]], 'g3': [out[1]], 'g4': [out[2]], 'g5': [out[3]]},
    ['Zeichne Variablen als Kästchen mit Pfeil. Zeile 3 kopiert nur den Pfeil, Zeile 4 biegt den Pfeil von x um.'],
    f'Nur `new` erzeugt Objekte – es gibt **{anz_obj}**. Nach Zeile 3 zeigen x und z auf Kira (maxLeben 100). '
    f'Zeile 4 biegt **nur x** auf das Objekt von y um; z zeigt weiter auf die erste Kira. '
    f'Also trifft `z.nimmSchaden(30)` die erste Kira (100 → {out[1]}) und `x.nimmSchaden(10)` das Objekt von y '
    f'(120 → {out[0]}). `x == y` ist **{out[2]}** (dieselbe Referenz), `z == x` ist **{out[3]}**.'))
check(out == ['110', '70', 'true', 'false'] and anz_obj == 2, 'W1-L2-02 Ausgaben 110/70/true/false, 2 Objekte (Java)')

# ---------- 03 Kampf-Trace
code03 = '''Held h = new Held("Aria");
Monster m = new Monster("Ork", 45, 7);
int runde = 0;
while (!m.istBesiegt()) {
    runde++;
    h.angreifen(m);
    if (!m.istBesiegt()) {
        m.angreifen(h);
    }
}
println(runde + " / " + h.getLeben());'''
instr = code03.replace('        m.angreifen(h);\n    }\n', '        m.angreifen(h);\n    }\n    println(runde + ";" + m.getLeben() + ";" + h.getLeben());\n')
out = J(instr)
rows = [r.split(';') for r in out[:-1]]
final = out[-1]
zeilen = [['0', '45', '100']]
loes = {}
k = 1
for r in rows:
    z = [r[0]]
    for v in r[1:]:
        loes[f'c{k}'] = [v]
        z.append(f'[[c{k}]]')
        k += 1
    zeilen.append(z)
check(len(rows) == 5 and final == '5 / 72', 'W1-L2-03 Kampf Aria gegen Ork: 5 Runden, Aria 72 Leben (Java-Trace)')
A.append(aufgabe(
    f'{L}-03', 'Aria gegen den Ork', 2, 'Tracetabelle', ['P8'],
    [text('Aria (100 Leben, Stärke 10) kämpft gegen einen Ork. `angriffswert()` ist hier noch einfach die Stärke.'),
     code(code03),
     text('Vervollständige die Tracetabelle: Werte **am Ende** jedes Schleifendurchlaufs.'),
     tabelle(['runde', 'm.getLeben()', 'h.getLeben()'], zeilen)],
    gaps(**{f'c{i}': zahl() for i in range(1, k)}), loes,
    ['Der Ork schlägt nur zurück, wenn er nach Arias Schlag noch lebt.'],
    'In jeder Runde nimmt der Ork 10 Schaden (45 → 35 → 25 → 15 → 5 → 0). In den Runden 1–4 lebt er danach noch '
    'und schlägt mit Stärke 7 zurück (100 → 93 → 86 → 79 → 72). In Runde 5 ist er besiegt und schlägt nicht mehr zurück. '
    f'Ausgabe: `{final}`. Merke für Tracetabellen (P8): jede Wertänderung, eine Zeile pro Durchlauf, Endwerte nicht vergessen.'))

# ---------- 04 null-Referenz
code04 = '''Held h = null;
h.nimmSchaden(10);
println(h.getLeben());'''
o, e = java(1, code04)
check('NullPointerException' in e, 'W1-L2-04 h = null; h.nimmSchaden(10) -> NullPointerException')
A.append(aufgabe(
    f'{L}-04', 'Ein Held aus dem Nichts', 1, 'Fehler im Java-Code', ['P1'],
    [code(code04), text('Was passiert, wenn dieses Hauptprogramm ausgeführt wird?')],
    choice([('a', 'Übersetzungsfehler in Zeile 1, weil eine Variable vom Typ `Held` nicht `null` sein darf.'),
            ('b', 'Laufzeitfehler (NullPointerException) in Zeile 2: Es gibt kein Objekt, das Schaden nehmen könnte.'),
            ('c', 'Ausgabe `90` – Java legt automatisch einen Standard-Helden an.'),
            ('d', 'Ausgabe `0`, weil `h` noch keine Leben hat.')]),
    {'richtig': ['b']},
    ['`null` heißt: Die Variable verweist auf **kein** Objekt.'],
    'Der Code wird übersetzt – `null` ist für jede Objektvariable erlaubt. Beim Ausführen von Zeile 2 soll aber eine '
    'Methode eines Objekts aufgerufen werden, das es nicht gibt: **NullPointerException**, das Programm bricht ab. '
    'Im Abitur gilt (P1): Laufzeitfehler müssen ausgeschlossen werden, z. B. mit `if (h != null) { … }`.'))

# ---------- 05 match == / equals
code05 = '''Held a = new Held("Ilka");
Held b = new Held("Ilka");
Held c = a;
c.erhalteGold(10);'''
ausdr = [('e1', 'a == b'), ('e2', 'a == c'), ('e3', 'a.getName().equals(b.getName())'), ('e4', 'b == c'),
         ('e5', 'a.getGold() == c.getGold()'), ('e6', 'a.getGold() == b.getGold()')]
out = J(code05 + '\n' + '\n'.join(f'println({x});' for _, x in ausdr))
loes = {k: ('w' if v == 'true' else 'f') for (k, _), v in zip(ausdr, out)}
check(out == ['false', 'true', 'true', 'false', 'true', 'false'], 'W1-L2-05 Referenzvergleiche per Java ausgewertet')
A.append(aufgabe(
    f'{L}-05', 'Gleich oder dasselbe?', 2, 'Objektkarten und Referenzen', ['P5'],
    [code(code05), text('Ordne jeden Ausdruck seinem Wert **nach Zeile 4** zu.')],
    match([(k, f'`{x}`') for k, x in ausdr], [('w', 'true'), ('f', 'false')]), loes,
    ['`==` vergleicht bei Objekten die Referenzen (Pfeile), nicht die Inhalte.'],
    '`a` und `b` sind zwei verschiedene Objekte mit gleichen Werten → `a == b` ist false, `b == c` auch. `c = a` kopiert '
    'die Referenz → `a == c` ist true, und `c.erhalteGold(10)` ändert genau dieses Objekt (a und c haben 10 Gold, b hat 0). '
    'Inhalte von Zeichenketten vergleicht man mit **equals** (P5) – in der Online-IDE vergleicht `==` Zeichenketten zwar '
    'inhaltlich, im Abitur und in echtem Java aber nicht.'))

# ---------- 06 Bug-Hunt Monster (2 Fehler)
code06 = '''public class Monster {
    private String name;
    private int leben;
    private int staerke;

    public Monster(String name, int leben, int staerke) {
        this.name = name;
        this.leben = leben;
        this.staerke = staerke;
    }

    public void nimmSchaden(int schaden) {
        leben = leben - schaden;
        if (leben < 0) {
            leben = 0;
        }
    }

    public boolean istBesiegt() {
        return leben < 0;
    }

    public void angreifen(Held h) {
        h.leben = h.leben - staerke;
    }
}'''
mx = code06.replace('public class Monster', 'class MonsterX').replace('public Monster(', 'public MonsterX(')
lines_src = mx.split('\n')
check(lines_src[19].strip() == 'return leben < 0;' and lines_src[23].strip() == 'h.leben = h.leben - staerke;', 'W1-L2-06 Zeilennummern 20/24')
check(not compiles(1, 'MonsterX m = new MonsterX("Wolf", 20, 5);', mx), 'W1-L2-06 Zeile 24: Zugriff auf privates h.leben -> Uebersetzungsfehler')
v24 = ['h.nimmSchaden(staerke);', 'h.nimmSchaden(this.staerke);', 'h.nimmSchaden(getStaerke());', 'h.nimmSchaden(this.getStaerke());']
v20 = ['return leben <= 0;', 'return leben == 0;', 'return leben < 1;', 'return this.leben <= 0;']
nur24 = mx.replace('        h.leben = h.leben - staerke;', '        ' + v24[0])
out = J('MonsterX m = new MonsterX("Wolf", 20, 5); m.nimmSchaden(25); println(m.istBesiegt());', nur24)
check(out == ['false'], 'W1-L2-06 Zeile 20: mit "< 0" ist ein Monster mit 0 Leben nie besiegt')
for a20 in v20:
    for a24 in v24:
        fx = mx.replace('        return leben < 0;', '        ' + a20).replace('        h.leben = h.leben - staerke;', '        ' + a24)
        fx = fx.replace('    public boolean istBesiegt()', '    public int getStaerke() { return staerke; }\n    public boolean istBesiegt()')
        out = J('MonsterX m = new MonsterX("Wolf", 20, 5); Held h = new Held("Aria"); m.angreifen(h); println(h.getLeben());'
                ' m.nimmSchaden(25); println(m.istBesiegt()); MonsterX n = new MonsterX("Ork", 9, 3); println(n.istBesiegt());', fx)
        check(out == ['95', 'true', 'false'], f'W1-L2-06 Korrektur "{a20}" + "{a24}" korrekt')
A.append(aufgabe(
    f'{L}-06', 'Das unbesiegbare Monster', 3, 'Fehler im Java-Code', ['P3'],
    [text('In dieser Klasse `Monster` stecken **zwei** Fehler: Einer verhindert das Übersetzen, der andere sorgt dafür, '
          'dass kein Monster jemals besiegt ist.'), code(code06),
     text('**a)** Markiere die beiden fehlerhaften Zeilen. **b)** Korrigiere sie (je eine Zeile Java).'),
     text('Korrektur der Zeile mit `istBesiegt`: [[g1]]'),
     text('Korrektur der Zeile in `angreifen`: [[g2]]')],
    [lines(1, 2), gaps(g1=txt('code', 28), g2=txt('code', 34))],
    [{'zeilen': [20, 24]}, {'g1': varianten(*v20), 'g2': varianten(*v24)}],
    ['`leben` kann wegen `nimmSchaden` nie negativ werden …', '`leben` ist in `Held` privat.'],
    'Zeile 20: `leben` wird in `nimmSchaden` nie kleiner als 0, also ist `leben < 0` immer falsch – richtig ist '
    '`return leben <= 0;`. Zeile 24: `leben` ist in `Held` **privat**, der Zugriff `h.leben` aus `Monster` ist ein '
    'Übersetzungsfehler. Außerdem würde direkter Zugriff die Grenze „nie unter 0" umgehen. Richtig: '
    '`h.nimmSchaden(staerke);` – der Held kümmert sich selbst um seinen Zustand (Kapselung).'))

# ---------- 07 Parsons kampf
teile07 = [('a', 'public static int kampf(Held h, Monster m) {'), ('b', '    int runde = 0;'),
           ('c', '    while (!m.istBesiegt() && !h.istBesiegt()) {'), ('d', '        runde++;'),
           ('e', '        h.angreifen(m);'), ('f', '        if (!m.istBesiegt()) {'), ('g', '            m.angreifen(h);'),
           ('h', '        }'), ('i', '    }'), ('j', '    return runde;'), ('k', '}'),
           ('x', '        m.nimmSchaden(h.staerke);'), ('y', '    while (m.istBesiegt() || h.istBesiegt()) {'),
           ('z', '    return h.getLeben();')]
T = dict(teile07)
reih07 = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
          ['a', 'b', 'c', 'e', 'd', 'f', 'g', 'h', 'i', 'j', 'k'],
          ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'd', 'i', 'j', 'k']]
for r in reih07:
    meth = '\n'.join(T[k] for k in r)
    out = J('println(Arena.kampf(new Held("Aria"), new Monster("Ork", 45, 7)));'
            ' Held w = new Held("Wicht", 10, 1); println(Arena.kampf(w, new Monster("Troll", 90, 16))); println(w.istBesiegt());'
            ' println(Arena.kampf(new Held("Aria"), new Monster("Maus", 3, 1)));',
            'class Arena {\n' + meth + '\n}')
    check(out == ['5', '1', 'true', '1'], f'W1-L2-07 Parsons kampf Reihenfolge {"".join(r)}: 5 / 1 / true / 1')
A.append(aufgabe(
    f'{L}-07', 'Puzzle: Die Arena', 3, 'Methode implementieren', ['P3'],
    [text('Die Klassenmethode `kampf(h: Held, m: Monster): Ganzzahl` lässt Held und Monster kämpfen, bis einer besiegt ist, '
          'und liefert die Zahl der Runden. In jeder Runde schlägt der Held zuerst; das Monster schlägt nur zurück, wenn es '
          'danach noch nicht besiegt ist. Setze die Methode zusammen – nicht alle Teile werden gebraucht.')],
    order(teile07), {'reihenfolgen': reih07},
    ['Welche Bedingung muss gelten, damit **weitergekämpft** wird?'],
    'Gekämpft wird, **solange** beide noch nicht besiegt sind: `!m.istBesiegt() && !h.istBesiegt()`. Pro Runde: '
    'Zähler erhöhen, Held greift an, Monster schlägt nur zurück, falls es noch lebt. Der Rundenzähler darf auch nach dem '
    'Angriff erhöht werden – das ändert das Ergebnis nicht. Distraktoren: `h.staerke` ist privat; die `while`-Bedingung '
    'mit `||` und ohne `!` bricht sofort ab; `return h.getLeben()` verfehlt die Signatur (Rundenzahl, P3).'))

# ---------- 08 Signatur -> Java-Kopf
heads = {'g1': 'public Monster(String name, int leben, int staerke)', 'g2': 'public boolean istBesiegt()',
         'g3': 'public void angreifen(Held h)'}
ok, err = compile_standalone({'M.java': 'class Held {}\nclass Monster {\n' + '\n'.join(h + ' { ' + ('return false; ' if 'boolean' in h else '') + '}' for h in heads.values()) + '\n}'})
check(ok, 'W1-L2-08 Methodenkoepfe kompilieren')
refl = J('println(Monster.class.getDeclaredConstructor(String.class, int.class, int.class) != null);'
         'println(Monster.class.getDeclaredMethod("istBesiegt").getReturnType());'
         'println(Monster.class.getDeclaredMethod("angreifen", Held.class).getReturnType());')
check(refl == ['true', 'boolean', 'void'], 'W1-L2-08 Koepfe stimmen mit LSG-Klasse Monster ueberein')
A.append(aufgabe(
    f'{L}-08', 'Von der Karte zum Kopf', 1, 'Methodenkopf und Signatur', ['P3'],
    [klassenkarte('Monster', ['- name: Zeichenkette', '- leben: Ganzzahl', '- staerke: Ganzzahl'],
                  ['+ c Monster(name: Zeichenkette, leben: Ganzzahl, staerke: Ganzzahl)', '+ getName(): Zeichenkette',
                   '+ getLeben(): Ganzzahl', '+ getStaerke(): Ganzzahl', '+ nimmSchaden(schaden: Ganzzahl): nichts',
                   '+ istBesiegt(): Wahrheitswert', '+ angreifen(h: Held): nichts']),
     text('Schreibe die Java-Köpfe mit Sichtbarkeit (ohne `{`, Parameternamen wie in der Klassenkarte):'),
     text('Konstruktor: [[g1]]'), text('`istBesiegt`: [[g2]]'), text('`angreifen`: [[g3]]')],
    gaps(g1=txt('code', 48), g2=txt('code', 30), g3=txt('code', 32)),
    {g: kopf(h) for g, h in heads.items()},
    ['Ganzzahl → int, Zeichenkette → String, Wahrheitswert → boolean, nichts → void. Ein Konstruktor hat keinen Rückgabetyp.'],
    '`+` wird zu `public`. Der Konstruktor heißt wie die Klasse und hat **keinen** Rückgabetyp: '
    '`public Monster(String name, int leben, int staerke)`. `: Wahrheitswert` → `boolean`, `: nichts` → `void`; '
    'der Parametertyp `Held` bleibt als Klassenname stehen: `public void angreifen(Held h)`.'))

LEVELS.append({"id": L, "nr": "1.2", "titel": "Doppelgänger – Konstruktoren und Referenzen", "ds": [9],
               "ab": "AB W1·1 Klassen und Objekte – Infoteil 4, Aufgaben 3–5",
               "ide": "AQ_W1_L1_Heldenschmiede_Geruest.txt – Level 1.2 (zweiter Konstruktor, Klasse Monster, Testklasse L12MonsterTest)",
               "intro": [text('Eine Klasse darf mehrere **Konstruktoren** haben, wenn sich die Parameterlisten unterscheiden '
                              '(Überladen). Eine Objektvariable speichert eine **Referenz** (einen Pfeil) auf ein Objekt.'),
                         hinweis('**Merke:** `Held b = a;` kopiert nur den Pfeil – es gibt danach immer noch **ein** Objekt. '
                                 '`==` vergleicht Referenzen, Inhalte vergleicht man mit `equals`. `null` = kein Objekt.')],
               "aufgaben": [a['id'] for a in A if a['id'].startswith(L + '-')]})

# =====================================================================
# LEVEL 1.3 – Inventar: Reihung von Objekten, Klassendiagramm (DS 10)
# =====================================================================
L = 'W1-L3'
INV = ('java.lang.reflect.Field fi = Held.class.getDeclaredField("inventar"); fi.setAccessible(true);'
       ' Gegenstand[] inv = (Gegenstand[]) fi.get(h);')

# ---------- 01 Inventar-Zustand
code01 = '''Held h = new Held("Aria");
h.aufnehmen(new Gegenstand("Seil", 3));
boolean ok = h.aufnehmen(null);
h.aufnehmen(new Gegenstand("Kompass", 25));'''
out = J(code01 + '\n' + INV + '\nprintln(h.getAnzahl()); println(inv.length);'
        ' for (int i = 0; i < inv.length; i++) { if (inv[i] != null && inv[i].getName().equals("Kompass")) println(i); }'
        ' println(inv[2] == null ? "null" : inv[2].getName()); println(ok);')
check(out == ['2', '5', '1', 'null', 'false'], 'W1-L3-01 Inventar per Reflection: anzahl 2, Laenge 5, Kompass Index 1, inventar[2] null, ok false')
A.append(aufgabe(
    f'{L}-01', 'Was steckt im Rucksack?', 1, 'Objektkarten und Referenzen', ['P1'],
    [text('`inventar` ist eine Reihung von Gegenstand der Länge 5, `anzahl` zählt die belegten Plätze. `aufnehmen` legt '
          'einen Gegenstand an den Index `anzahl` und liefert false bei `null` oder vollem Inventar.'), code(code01),
     text('Nach Zeile 4 gilt: `anzahl` = [[g1]] · `inventar.length` = [[g2]] · der Kompass liegt an Index [[g3]] · '
          '`inventar[2]` enthält [[g4]] · `ok` hat den Wert [[g5]]')],
    gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=auswahl(['null', 'den Kompass', 'das Seil', 'einen leeren Gegenstand']),
         g5=auswahl(WF)),
    {'g1': [out[0]], 'g2': [out[1]], 'g3': [out[2]], 'g4': [out[3]], 'g5': [out[4]]},
    ['`new Gegenstand[5]` erzeugt fünf leere Plätze – noch keinen Gegenstand.'],
    'Das Seil kommt an Index 0, `anzahl` wird 1. `aufnehmen(null)` liefert **false** und ändert nichts. Der Kompass '
    'kommt an Index `anzahl` = **1**, danach ist `anzahl` = **2**. Die Reihung hat weiterhin die Länge **5**; die Plätze '
    '2 bis 4 enthalten **null**. Deshalb laufen Schleifen nur bis `anzahl − 1` (P1).'))

# ---------- 02 Assoziation
A.append(aufgabe(
    f'{L}-02', 'Eine Linie zum Rucksack', 1, 'Klassendiagramm', [],
    [text('Im Klassendiagramm ist `Held` durch eine Linie mit `Gegenstand` verbunden, aber **nicht** mit `Monster` – '
          'obwohl `Held` die Methode `angreifen(m: Monster): nichts` hat. Welche Begründung ist richtig?')],
    choice([('a', '`Held` hat ein Attribut vom Typ „Reihung von Gegenstand" (dauerhafte Beziehung); ein Monster wird nur '
                  'als Parameter kurz benutzt und nicht gespeichert.'),
            ('b', 'Linien zeichnet man nur zu Klassen, die weniger Methoden haben.'),
            ('c', '`angreifen` liefert nichts zurück, deshalb gibt es keine Beziehung.'),
            ('d', 'Die Linie zu `Gegenstand` muss eigentlich die Kardinalität 0..5 tragen; zu `Monster` fehlt sie nur aus Platzgründen.')]),
    {'richtig': ['a']},
    ['Wann zeichnen wir nach EH § 6 eine Linie zwischen zwei Klassen?'],
    'Eine **Assoziation** zeichnen wir, wenn eine Klasse ein **Attribut** vom Typ der anderen Klasse hat (auch als '
    'Reihung): `- inventar: Reihung von Gegenstand`. Ein Monster wird nur als Parameter übergeben und nicht gespeichert. '
    'Nach EH § 6 sind Assoziationen einfache, unbeschriftete Linien **ohne** Kardinalitäten.'))

# ---------- 03 Bug-Hunt gesamtWert
code03 = '''public int gesamtWert() {
    int summe = 0;
    for (int i = 0; i < inventar.length; i++) {
        summe = summe + inventar[i].getWert();
    }
    return summe;
}'''
stub = ('class HeldG { private Gegenstand[] inventar = new Gegenstand[5]; private int anzahl = 0;\n'
        ' public void aufnehmen(Gegenstand g) { inventar[anzahl] = g; anzahl++; }\n')
o, e = java(1, 'HeldG h = new HeldG(); h.aufnehmen(new Gegenstand("Seil", 3)); h.aufnehmen(new Gegenstand("Krone", 50)); println(h.gesamtWert());',
            stub + code03 + '\n}')
check('NullPointerException' in e, 'W1-L3-03 gesamtWert bis inventar.length -> NullPointerException')
v03 = ['for (int i = 0; i < anzahl; i++) {', 'for (int i = 0; i <= anzahl - 1; i++) {', 'for (int i = 0; anzahl > i; i++) {']
for v in v03:
    out = J('HeldG h = new HeldG(); println(h.gesamtWert()); h.aufnehmen(new Gegenstand("Seil", 3)); h.aufnehmen(new Gegenstand("Krone", 50)); println(h.gesamtWert());',
            stub + code03.replace('    for (int i = 0; i < inventar.length; i++) {', '    ' + v) + '\n}')
    check(out == ['0', '53'], f'W1-L3-03 Korrektur "{v}" liefert 0 bzw. 53')
A.append(aufgabe(
    f'{L}-03', 'Absturz im Schatzzimmer', 2, 'Fehler im Java-Code', ['P1', 'P6'],
    [text('Ein Held mit zwei Gegenständen ruft `gesamtWert()` auf – das Programm stürzt ab.'), code(code03),
     text('**a)** Markiere die fehlerhafte Zeile. **b)** Korrigierte Zeile: [[g1]] **c)** Welcher Laufzeitfehler tritt auf? [[g2]]')],
    [lines(1, 1), gaps(g1=txt('code', 36), g2=auswahl(['NullPointerException', 'ArrayIndexOutOfBoundsException', 'kein Fehler, Ergebnis 0']))],
    [{'zeilen': [3]}, {'g1': varianten(*v03), 'g2': ['NullPointerException']}],
    ['Welche Plätze der Reihung sind belegt, welche enthalten `null`?'],
    'Die Schleife läuft bis `inventar.length − 1` = 4, belegt sind aber nur die Indizes 0 bis `anzahl − 1`. Bei i = 2 ist '
    '`inventar[2]` gleich `null`, der Aufruf `getWert()` darauf löst eine **NullPointerException** aus (P1). Richtig: '
    '`for (int i = 0; i < anzahl; i++)` – Schleifengrenzen immer am Füllstand ausrichten (P6).'))

# ---------- 04 Trace wertvollsterGegenstand
code04 = '''public Gegenstand wertvollsterGegenstand() {
    if (anzahl == 0) {
        return null;
    }
    Gegenstand bester = inventar[0];
    for (int i = 1; i < anzahl; i++) {
        if (inventar[i].getWert() > bester.getWert()) {
            bester = inventar[i];
        }
    }
    return bester;
}'''
items = [('Fackel', 5), ('Kompass', 25), ('Seil', 3), ('Kristall', 25), ('Krone', 20)]
instr = ('class TW { static Gegenstand[] inventar; static int anzahl;\n static Gegenstand wertvollsterGegenstand() {\n'
         ' if (anzahl == 0) { return null; }\n Gegenstand bester = inventar[0];\n for (int i = 1; i < anzahl; i++) {\n'
         '  boolean b = inventar[i].getWert() > bester.getWert();\n  if (b) { bester = inventar[i]; }\n'
         '  println(i + ";" + inventar[i].getWert() + ";" + b + ";" + bester.getName());\n }\n return bester; } }')
main = ('TW.inventar = new Gegenstand[5]; TW.anzahl = 5;' + ''.join(f' TW.inventar[{i}] = new Gegenstand("{n}", {w});' for i, (n, w) in enumerate(items))
        + ' println(TW.wertvollsterGegenstand().getName());'
        + ' Held h = new Held("Aria");' + ''.join(f' h.aufnehmen(new Gegenstand("{n}", {w}));' for n, w in items)
        + ' println(h.wertvollsterGegenstand().getName());')
out = J(main, instr)
rows = [r.split(';') for r in out[:-2]]
check(out[-2] == out[-1] == 'Kompass', 'W1-L3-04 instrumentierte Kopie == LSG-Methode: Kompass (Gleichstand -> erster)')
names = [n for n, _ in items]
zeilen, loes, felder = [['–', '–', '–', 'Fackel']], {}, {}
for r in rows:
    k = r[0]
    zeilen.append([k, r[1], f'[[v{k}]]', f'[[b{k}]]'])
    loes[f'v{k}'] = ['wahr' if r[2] == 'true' else 'falsch']
    loes[f'b{k}'] = [r[3]]
    felder[f'v{k}'] = auswahl(['wahr', 'falsch'])
    felder[f'b{k}'] = auswahl(names)
felder['r'] = auswahl(names)
loes['r'] = [out[-1]]
A.append(aufgabe(
    f'{L}-04', 'Der wertvollste Schatz', 2, 'Tracetabelle', ['P8'],
    [text('Das Inventar enthält (Index 0 bis 4): ' + ', '.join(f'{n} ({w} Gold)' for n, w in items) + '; `anzahl` = 5.'),
     code(code04),
     text('Vervollständige die Tracetabelle (eine Zeile pro Schleifendurchlauf, `bester` am Ende des Durchlaufs).'),
     tabelle(['i', 'inventar[i].getWert()', 'inventar[i].getWert() > bester.getWert()', 'bester'], zeilen),
     text('Rückgabe: [[r]]')],
    gaps(**felder), loes,
    ['Bei Gleichstand gilt `>` nicht – der bisherige Rekord bleibt.'],
    'Start: `bester` = Fackel (5). i = 1: 25 > 5 → Kompass. i = 2: 3 > 25 falsch. i = 3: 25 > 25 **falsch** – bei '
    'Gleichstand bleibt der erste (Kompass). i = 4: 20 > 25 falsch. Rückgabe: **Kompass**. Mit `>=` käme der Kristall '
    'heraus – die Aufgabe verlangt aber „bei Gleichstand der erste".'))

# ---------- 05 Lueckencode enthaelt
code05 = '''public boolean enthaelt(String name) {
    for (int i = 0; i < [[g1]]; i++) {
        if (inventar[i].getName().[[g2]]) {
            return [[g3]];
        }
    }
    return [[g4]];
}'''
loes05 = {'g1': ['anzahl', 'this.anzahl'], 'g2': ['equals(name)'], 'g3': ['true'], 'g4': ['false']}
stub5 = ('class HeldE { private Gegenstand[] inventar = new Gegenstand[5]; private int anzahl = 0;\n'
         ' public void aufnehmen(Gegenstand g) { inventar[anzahl] = g; anzahl++; }\n')
for g1 in ['anzahl', 'this.anzahl']:
    m = code05.replace('[[g1]]', g1).replace('[[g2]]', 'equals(name)').replace('[[g3]]', 'true').replace('[[g4]]', 'false')
    out = J('HeldE h = new HeldE(); println(h.enthaelt("Seil")); h.aufnehmen(new Gegenstand("Seil", 3)); h.aufnehmen(new Gegenstand("Krone", 50));'
            ' println(h.enthaelt("Krone")); println(h.enthaelt(new String("Seil"))); println(h.enthaelt("Fackel"));', stub5 + m + '\n}')
    check(out == ['false', 'true', 'true', 'false'], f'W1-L3-05 Lueckencode enthaelt mit {g1} korrekt')
A.append(aufgabe(
    f'{L}-05', 'Hab ich das dabei?', 2, 'Lückencode', ['P5', 'P6'],
    [text('`enthaelt(name: Zeichenkette): Wahrheitswert` liefert true, wenn ein Gegenstand mit genau diesem Namen im '
          'Inventar liegt. Ergänze die Lücken.'), code(code05)],
    gaps(g1=txt('code', 10), g2=txt('code', 14), g3=auswahl(WF), g4=auswahl(WF)), loes05,
    ['Wie vergleicht man Zeichenketten im Abitur?', 'Wann steht fest, dass der Name **nicht** vorkommt?'],
    'Die Schleife läuft nur über belegte Plätze (`i < anzahl`). Zeichenketten vergleicht man mit `equals(name)` (P5). '
    'Beim ersten Treffer steht das Ergebnis fest: `return true;`. Erst **nach** der Schleife ist klar, dass kein '
    'Gegenstand passt: `return false;` – ein `return false` im else-Zweig würde schon nach dem ersten Gegenstand abbrechen.'))

# ---------- 06 Parsons aufnehmen
teile06 = [('a', 'public boolean aufnehmen(Gegenstand g) {'), ('b', '    if (g == null || anzahl == inventar.length) {'),
           ('c', '        return false;'), ('d', '    }'), ('e', '    inventar[anzahl] = g;'), ('f', '    anzahl++;'),
           ('g', '    return true;'), ('h', '}'),
           ('x', '    inventar[anzahl + 1] = g;'), ('y', '    if (g == null && anzahl == inventar.length) {'),
           ('z', '    anzahl = anzahl + g.getWert();')]
T = dict(teile06)
reih06 = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
for r in reih06:
    meth = '\n'.join(T[k] for k in r)
    out = J('HeldA h = new HeldA(); println(h.aufnehmen(null));'
            ' for (int i = 0; i < 6; i++) { println(h.aufnehmen(new Gegenstand("G" + i, i))); } println(h.getAnzahl()); println(h.letzter());',
            'class HeldA { private Gegenstand[] inventar = new Gegenstand[5]; private int anzahl = 0;\n' + meth
            + '\npublic int getAnzahl() { return anzahl; } public String letzter() { return inventar[anzahl - 1].getName(); } }')
    check(out == ['false', 'true', 'true', 'true', 'true', 'true', 'false', '5', 'G4'], 'W1-L3-06 Parsons aufnehmen: null/voll -> false, sonst ans Ende')
A.append(aufgabe(
    f'{L}-06', 'Puzzle: Ab in den Rucksack', 3, 'Methode implementieren', ['P1'],
    [text('Setze `aufnehmen(g: Gegenstand): Wahrheitswert` zusammen: false, wenn `g` null ist oder das Inventar voll ist; '
          'sonst kommt `g` an das Ende der belegten Plätze, `anzahl` wird erhöht und true geliefert. '
          'Nicht alle Teile werden gebraucht.')],
    order(teile06), {'reihenfolgen': reih06},
    ['Der nächste freie Platz hat den Index `anzahl`.'],
    'Zuerst die Abfrage, die Laufzeitfehler ausschließt (P1): `g == null || anzahl == inventar.length` – mit **oder**, '
    'denn jede der beiden Bedingungen allein verbietet das Einfügen. Dann `inventar[anzahl] = g;` **vor** `anzahl++;` – '
    'der freie Platz hat den Index `anzahl`. `inventar[anzahl + 1]` würde eine Lücke lassen.'))

# ---------- 07 Aliasing im Inventar
code07 = '''Gegenstand f = new Gegenstand("Fackel", 5);
Held a = new Held("Aria");
Held b = a;
a.aufnehmen(f);
b.aufnehmen(f);
b.aufnehmen(new Gegenstand("Krone", 80));
Held c = new Held("Aria");
c.aufnehmen(new Gegenstand("Krone", 80));
println(a.getAnzahl());
println(a.gesamtWert());
println(c.gesamtWert());
println(a.wertvollsterGegenstand() == c.wertvollsterGegenstand());
println(a.enthaelt("Krone") && c.enthaelt("Krone"));'''
out = J(code07)
check(out == ['3', '90', '80', 'false', 'true'], 'W1-L3-07 Aliasing: 3 / 90 / 80 / false / true (Java)')
A.append(aufgabe(
    f'{L}-07', 'Zwei Namen, ein Rucksack', 3, 'Objektkarten und Referenzen', [],
    [code(code07), text('Gib die fünf Ausgaben an: [[g1]] · [[g2]] · [[g3]] · [[g4]] · [[g5]]')],
    gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=auswahl(WF), g5=auswahl(WF)),
    {'g1': [out[0]], 'g2': [out[1]], 'g3': [out[2]], 'g4': [out[3]], 'g5': [out[4]]},
    ['Wie viele Held-Objekte gibt es? Auf welches Objekt verweisen a und b?'],
    'a und b verweisen auf **dasselbe** Held-Objekt – alle drei `aufnehmen`-Aufrufe landen in einem Inventar: '
    'Fackel, Fackel (dieselbe Referenz zweimal!) und Krone → `getAnzahl()` = 3, `gesamtWert()` = 5 + 5 + 80 = 90. '
    'c ist ein eigenes Objekt mit einer **anderen** Krone (80). Die beiden Kronen haben gleiche Werte, sind aber '
    'verschiedene Objekte → `==` liefert false. `enthaelt` vergleicht Namen mit equals → true.'))

# ---------- 08 match EH-Notation
A.append(aufgabe(
    f'{L}-08', 'Abi-Notation im Klassendiagramm', 1, 'Klassendiagramm', [],
    [text('Welche Einträge sind nach EH § 6 **korrekt** notiert, welche nicht?')],
    match([('e1', '`- inventar: Reihung von Gegenstand`'), ('e2', '`+ c Held(name: Zeichenkette)`'),
           ('e3', '`+ getAnzahl(): int`'), ('e4', '`- inventar: Gegenstand[]`'),
           ('e5', '`+ aufnehmen(g: Gegenstand): Wahrheitswert`'), ('e6', 'Linie Held – Gegenstand mit der Beschriftung `0..5`'),
           ('e7', '`anzahl: Ganzzahl` (ohne Zeichen davor)')],
          [('ok', 'korrekt nach EH § 6'), ('no', 'nicht korrekt')]),
    {'e1': 'ok', 'e2': 'ok', 'e3': 'no', 'e4': 'no', 'e5': 'ok', 'e6': 'no', 'e7': 'no'},
    ['Deutsche Typnamen, Sichtbarkeit ist Pflicht, Assoziationen ohne Kardinalitäten.'],
    'Korrekt sind die Einträge mit **deutschen Typnamen** und **Sichtbarkeit**: „Reihung von Gegenstand", '
    '`+ c Held(…)`, `: Wahrheitswert`. Falsch sind Java-Typen (`int`, `Gegenstand[]`), fehlende Sichtbarkeit und '
    'Kardinalitäten an Linien – Assoziationen sind nach EH § 6 einfache, unbeschriftete Linien.'))

LEVELS.append({"id": L, "nr": "1.3", "titel": "Der Rucksack – Reihung von Objekten", "ds": [10],
               "ab": "AB W1·1 Klassen und Objekte – Infoteil 5, Aufgaben 6–8 (Papier-Compiler)",
               "ide": "AQ_W1_L1_Heldenschmiede_Geruest.txt – Level 1.3 (Gegenstand, Inventar, Testklasse L13InventarTest)",
               "intro": [text('Das Inventar ist eine **Reihung von Gegenstand** mit Füllstand `anzahl`: belegt sind die '
                              'Indizes 0 bis `anzahl − 1`, dahinter steht `null`.'),
                         hinweis('**Achtung Abi:** Schleifen bis `anzahl − 1`, nicht bis `inventar.length − 1`; vor dem Einfügen '
                                 'auf `null` und „voll" prüfen; Namen mit `equals` vergleichen. Assoziation = einfache Linie ohne Kardinalität.')],
               "aufgaben": [a['id'] for a in A if a['id'].startswith(L + '-')]})

# =====================================================================
# LEVEL 1.4 – Vererbung (DS 11)
# =====================================================================
L = 'W1-L4'

# ---------- 01 match geerbt/neu/ueberschrieben
refl = J('''
for (String m : new String[]{"getName", "getWert", "getSchaden", "beschreibung"}) {
  boolean inW = false; for (java.lang.reflect.Method x : Waffe.class.getDeclaredMethods()) if (x.getName().equals(m)) inW = true;
  boolean inG = false; for (java.lang.reflect.Method x : Gegenstand.class.getDeclaredMethods()) if (x.getName().equals(m)) inG = true;
  println(m + ";" + inW + ";" + inG);
}
println(Waffe.class.getDeclaredField("schaden") != null);''')
kat = {}
for r in refl[:-1]:
    m, inW, inG = r.split(';')
    kat[m] = 'ue' if inW == inG == 'true' else ('neu' if inW == 'true' else 'erb')
check(kat == {'getName': 'erb', 'getWert': 'erb', 'getSchaden': 'neu', 'beschreibung': 'ue'} and refl[-1] == 'true',
      'W1-L4-01 Waffe: getName/getWert geerbt, getSchaden neu, beschreibung ueberschrieben (Reflection)')
A.append(aufgabe(
    f'{L}-01', 'Was hat die Waffe?', 1, 'Klassendiagramm', [],
    [klassenkarte('Gegenstand', ['- name: Zeichenkette', '- wert: Ganzzahl'],
                  ['+ c Gegenstand(name: Zeichenkette, wert: Ganzzahl)', '+ getName(): Zeichenkette', '+ getWert(): Ganzzahl',
                   '+ beschreibung(): Zeichenkette']),
     klassenkarte('Waffe', ['- schaden: Ganzzahl'],
                  ['+ c Waffe(name: Zeichenkette, wert: Ganzzahl, schaden: Ganzzahl)', '+ getSchaden(): Ganzzahl',
                   '+ beschreibung(): Zeichenkette']),
     text('`Waffe` erbt von `Gegenstand` (Pfeil mit hohler Spitze zu `Gegenstand`). Ordne zu, wie die Elemente zu einem '
          '**Waffe**-Objekt gehören.')],
    match([('e1', '`getName()`'), ('e2', '`getWert()`'), ('e3', '`getSchaden()`'), ('e4', '`beschreibung()`'),
           ('e5', 'Attribut `schaden`')],
          [('erb', 'nur geerbt (unverändert aus Gegenstand)'), ('neu', 'neu in Waffe'), ('ue', 'in Waffe überschrieben')]),
    {'e1': 'erb', 'e2': 'erb', 'e3': 'neu', 'e4': 'ue', 'e5': 'neu'},
    ['In der Unterklasse stehen nur neue und überschriebene Elemente.'],
    'Nach EH § 6 stehen in der Unterklasse **nur neue und überschriebene** Elemente. `schaden` und `getSchaden()` sind '
    'neu. `beschreibung()` steht in beiden Karten mit gleicher Signatur → **überschrieben**. `getName()` und `getWert()` '
    'werden nur geerbt – jedes Waffe-Objekt besitzt sie trotzdem (ebenso die privaten Attribute name und wert, die aber '
    'nur über die Getter erreichbar sind).'))

# ---------- 02 kompiliert ja/nein
stmts = [('g1', 'Gegenstand g = new Trank("Met", 8, 15);'),
         ('g2', 'Waffe w = new Gegenstand("Stock", 1);'),
         ('g3', 'Gegenstand g = new Waffe("Speer", 40, 11);\nprintln(g.getSchaden());'),
         ('g4', 'Gegenstand g = new Schluessel("Silberschluessel", 12, 4);\nprintln(g.beschreibung());'),
         ('g5', 'Held h = new Held("Aria");\nh.ausruesten(new Waffe("Speer", 40, 11));'),
         ('g6', 'Held h = new Held("Aria");\nh.trinken(new Gegenstand("Met", 8));')]
loes = {g: ['ja' if compiles(1, s) else 'nein'] for g, s in stmts}
check([loes[g][0] for g, _ in stmts] == ['ja', 'nein', 'nein', 'ja', 'ja', 'nein'], 'W1-L4-02 Uebersetzbarkeit per javac bestimmt')
A.append(aufgabe(
    f'{L}-02', 'Wird das übersetzt?', 1, 'Fehler im Java-Code', ['P4'],
    [text('Entscheide für jeden Ausschnitt, ob er **übersetzt** wird (Klassen `Gegenstand`, `Waffe`, `Trank`, '
          '`Schluessel`, `Held` wie in Level 1.4).'),
     tabelle(['Anweisung(en)', 'übersetzt?'], [[f'`{s.replace(chr(10), " ")}`', f'[[{g}]]'] for g, s in stmts])],
    gaps(**{g: auswahl(JA_NEIN) for g, _ in stmts}), loes,
    ['Der Typ der **Variable** entscheidet, welche Methoden aufgerufen werden dürfen.'],
    'Ein Objekt der Unterklasse darf einer Variable der Oberklasse zugewiesen werden („jeder Trank ist ein Gegenstand") – '
    'umgekehrt nicht (`Waffe w = new Gegenstand(…)` ✗). Der Typ der Variable bestimmt, welche Methoden der Compiler '
    'erlaubt: `getSchaden()` gibt es in `Gegenstand` nicht ✗; `beschreibung()` schon ✓. `ausruesten` erwartet eine '
    'Waffe ✓, `trinken` einen Trank – ein beliebiger Gegenstand passt nicht ✗.'))

# ---------- 03 Polymorphe Ausgabe
code03 = '''Gegenstand[] kiste = new Gegenstand[3];
kiste[0] = new Waffe("Speer", 40, 11);
kiste[1] = new Schluessel("Gitterschluessel", 6, 2);
kiste[2] = new Trank("Met", 8, 15);
for (Gegenstand g : kiste) {
    println(g.beschreibung());
}'''
out = J(code03)
opts = [['Waffe: Speer (40 Gold), Schaden 11', 'Speer (40 Gold)', 'Speer (40 Gold), Schaden 11', 'Gegenstand: Speer (40 Gold)'],
        ['Gitterschluessel (6 Gold)', 'Schluessel: Gitterschluessel (6 Gold), Tuer 2', 'Gitterschluessel (6 Gold), Tuer 2', 'Übersetzungsfehler'],
        ['Trank: Met (8 Gold), heilt 15', 'Met (8 Gold)', 'Trank: Met (8 Gold)', 'Met (8 Gold), heilt 15']]
for o_, line in zip(opts, out):
    check(line in o_ and o_.count(line) == 1, f'W1-L4-03 Ausgabe "{line}" eindeutig unter den Optionen')
A.append(aufgabe(
    f'{L}-03', 'Die Schatzkiste spricht', 2, 'Funktionsweise erläutern', [],
    [code(code03), text('Gib die drei Ausgabezeilen an.'),
     text('Zeile 1: [[g1]]'), text('Zeile 2: [[g2]]'), text('Zeile 3: [[g3]]')],
    gaps(g1=auswahl(opts[0]), g2=auswahl(opts[1]), g3=auswahl(opts[2])),
    {'g1': [out[0]], 'g2': [out[1]], 'g3': [out[2]]},
    ['Welche Klassen überschreiben `beschreibung()`, welche nicht?'],
    'Die Reihung hat den Typ „Reihung von Gegenstand", aber welche Version von `beschreibung()` läuft, entscheidet das '
    '**Objekt** (dynamisches Binden): Waffe und Trank haben die Methode überschrieben und rufen `super.beschreibung()` '
    'auf. `Schluessel` überschreibt **nicht** → die geerbte Version liefert nur „Gitterschluessel (6 Gold)".'))

# ---------- 04 Golem: welche Methode laeuft
golem = '''class Golem extends Monster {
    public Golem(String name, int leben, int staerke) {
        super(name, leben, staerke);
    }

    // ueberschreibt nimmSchaden aus Monster: Steinhaut haelt 5 Schaden ab
    public void nimmSchaden(int schaden) {
        if (schaden > 5) {
            super.nimmSchaden(schaden - 5);
        }
    }
}'''
code04 = '''Monster m = new Golem("Steingolem", 60, 9);
Held h = new Held("Aria");
h.angreifen(m);
println(m.getLeben());'''
out = J(code04, golem)
check(out == ['55'], 'W1-L4-04 Golem nimmt 10 - 5 = 5 Schaden -> 55')
A.append(aufgabe(
    f'{L}-04', 'Die Steinhaut', 2, 'Funktionsweise erläutern', [],
    [text('Ein Golem ist ein Monster mit Steinhaut:'), code(golem.replace('class Golem', 'public class Golem')),
     text('Was gibt das folgende Hauptprogramm aus? (Aria: Stärke 10, keine Waffe)'), code(code04)],
    choice([('a', '`50` – `m` hat den Typ `Monster`, also läuft `nimmSchaden` aus `Monster`.'),
            ('b', '`55` – das Objekt ist ein Golem, also läuft die überschriebene Methode aus `Golem`.'),
            ('c', 'Übersetzungsfehler – `angreifen` erwartet ein `Monster`, kein `Golem`-Objekt.'),
            ('d', '`60` – ein Golem nimmt keinen Schaden.')]),
    {'richtig': ['b']},
    ['Typ der Variable: Was darf aufgerufen werden? Typ des Objekts: Welche Version läuft?'],
    '`h.angreifen(m)` ruft `m.nimmSchaden(10)` auf. Das Objekt ist ein **Golem** – durch dynamisches Binden läuft dessen '
    'Version: 10 > 5, also `super.nimmSchaden(5)` → 60 − 5 = **55**. Der Typ der Variable (`Monster`) entscheidet nur, '
    'dass `nimmSchaden` überhaupt aufgerufen werden darf. Ein Golem *ist ein* Monster, darum passt er als Argument.'))

# ---------- 05 Amulett: super nicht zuerst
code05 = '''public class Amulett extends Gegenstand {
    private int magie;

    public Amulett(String name, int wert, int magie) {
        this.magie = magie;
        super(name, wert);
    }

    public int getMagie() {
        return magie;
    }

    public String beschreibung() {
        return "Amulett: " + super.beschreibung() + ", Magie " + magie;
    }
}'''
am = code05.replace('public class Amulett', 'class Amulett')
check(not compiles(1, 'Amulett a = new Amulett("Mondstein", 70, 4);', am), 'W1-L4-05 super nicht als erste Anweisung -> Uebersetzungsfehler (Java 21)')
fixed = am.replace('        this.magie = magie;\n        super(name, wert);', '        super(name, wert);\n        this.magie = magie;')
out = J('Gegenstand a = new Amulett("Mondstein", 70, 4); println(a.beschreibung());', fixed)
check(out == ['Amulett: Mondstein (70 Gold), Magie 4'], 'W1-L4-05 korrigiertes Amulett liefert Beschreibung')
A.append(aufgabe(
    f'{L}-05', 'Das störrische Amulett', 2, 'Fehler im Java-Code', ['P3'],
    [text('Diese Klasse wird **nicht übersetzt**. Der Fehler lässt sich beheben, indem man zwei Zeilen vertauscht.'),
     code(code05),
     text('**a)** Markiere die beiden Zeilen, die vertauscht werden müssen. **b)** Wähle die Begründung.')],
    [lines(1, 2), choice([('a', '`super(…)` muss die erste Anweisung im Konstruktor einer Unterklasse sein.'),
                          ('b', '`magie` ist privat und darf im Konstruktor nicht gesetzt werden.'),
                          ('c', 'Eine Unterklasse darf keine eigenen Attribute haben.'),
                          ('d', '`beschreibung()` darf nicht überschrieben werden.')])],
    [{'zeilen': [5, 6]}, {'richtig': ['a']}],
    ['Was muss zuerst existieren: der Gegenstand-Teil oder das Amulett-Extra?'],
    'Der Konstruktor einer Unterklasse ruft als **erste** Anweisung den Konstruktor der Oberklasse auf: '
    '`super(name, wert);` setzt die privaten geerbten Attribute. Erst danach folgt `this.magie = magie;`. '
    f'Mit vertauschten Zeilen liefert `beschreibung()` z. B. „{out[0]}".'))

# ---------- 06 Gesamtprogramm
code06 = '''Held kai = new Held("Kai", 80, 12);
Waffe dolch = new Waffe("Dolch", 15, 4);
Waffe hammer = new Waffe("Kriegshammer", 60, 14);
kai.aufnehmen(dolch);
kai.aufnehmen(new Trank("Heiltrank", 20, 25));
kai.aufnehmen(hammer);
kai.aufnehmen(new Schluessel("Turmschluessel", 9, 3));
kai.ausruesten(dolch);
kai.nimmSchaden(50);
kai.trinken(new Trank("Elixier", 50, 40));
kai.ausruesten(hammer);
println(kai.getLeben());
println(kai.angriffswert());
println(kai.gesamtWert());
println(kai.wertvollsterGegenstand().beschreibung());'''
out = J(code06)
check(out == ['70', '26', '104', 'Waffe: Kriegshammer (60 Gold), Schaden 14'], 'W1-L4-06 Ausgaben 70/26/104/Kriegshammer (Java)')
o4 = ['Waffe: Kriegshammer (60 Gold), Schaden 14', 'Kriegshammer (60 Gold)', 'Trank: Elixier (50 Gold), heilt 40', 'Waffe: Dolch (15 Gold), Schaden 4']
A.append(aufgabe(
    f'{L}-06', 'Kai rüstet auf', 3, 'Objektkarten und Referenzen', [],
    [text('Alle Methoden sind wie in Level 1.4 implementiert (`trinken` heilt um den Heilwert, nie über `maxLeben`; '
          '`angriffswert` = Stärke + Schaden der ausgerüsteten Waffe).'), code(code06),
     text('Ausgaben: Zeile 12: [[g1]] · Zeile 13: [[g2]] · Zeile 14: [[g3]]'), text('Zeile 15: [[g4]]')],
    gaps(g1=zahl(), g2=zahl(), g3=zahl(), g4=auswahl(o4)),
    {'g1': [out[0]], 'g2': [out[1]], 'g3': [out[2]], 'g4': [out[3]]},
    ['Das Elixier wird getrunken, aber nicht aufgenommen.', 'Welche Waffe ist am Ende ausgerüstet?'],
    'leben: 80 − 50 = 30, das Elixier heilt 40 → **70** (≤ maxLeben 80). Am Ende ist der Hammer ausgerüstet: '
    'Stärke 12 + Schaden 14 = **26**. Im Inventar liegen Dolch, Heiltrank, Hammer und Schlüssel (das Elixier nicht!): '
    '15 + 20 + 60 + 9 = **104**. Der wertvollste ist der Hammer; weil er eine Waffe ist, läuft die überschriebene '
    '`beschreibung()`.'))

# ---------- 07 Parsons Klasse Trank
teile07 = [('a', 'public class Trank extends Gegenstand {'), ('b', '    private int heilwert;'),
           ('c', '    public Trank(String name, int wert, int heilwert) {'), ('d', '        super(name, wert);'),
           ('e', '        this.heilwert = heilwert;'), ('f', '    } // Ende Konstruktor'),
           ('g', '    public String beschreibung() {'),
           ('h', '        return "Trank: " + super.beschreibung() + ", heilt " + heilwert;'), ('i', '    } // Ende beschreibung'),
           ('j', '}'),
           ('x', '        return "Trank: " + name + " (" + wert + " Gold), heilt " + heilwert;'),
           ('y', '        this.name = name;'), ('z', 'public class Trank implements Gegenstand {')]
T = dict(teile07)
reih07 = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']]
for r in reih07:
    cls = '\n'.join(T[k] for k in r).replace('public class Trank', 'class TrankX').replace('public Trank(', 'public TrankX(')
    out = J('Gegenstand t = new TrankX("Heiltrank", 20, 30); println(t.beschreibung()); println(t.getWert());', cls)
    check(out == ['Trank: Heiltrank (20 Gold), heilt 30', '20'], 'W1-L4-07 Parsons Trank kompiliert und beschreibt korrekt')
bad = '\n'.join(T[k] for k in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x', 'i', 'j']).replace('public class Trank', 'class TrankX').replace('public Trank(', 'public TrankX(')
check(not compiles(1, 'new TrankX("A", 1, 2);', bad), 'W1-L4-07 Distraktor mit name/wert (privat) kompiliert nicht')
A.append(aufgabe(
    f'{L}-07', 'Puzzle: Der Trank', 3, 'Methode implementieren', ['P3'],
    [klassenkarte('Trank', ['- heilwert: Ganzzahl'],
                  ['+ c Trank(name: Zeichenkette, wert: Ganzzahl, heilwert: Ganzzahl)', '+ beschreibung(): Zeichenkette', '…']),
     text('Setze die Klasse `Trank` (Unterklasse von `Gegenstand`) zusammen – in der üblichen Reihenfolge: Attribut, '
          'Konstruktor, Methode. `beschreibung()` soll z. B. „Trank: Heiltrank (20 Gold), heilt 30" liefern. '
          'Nicht alle Teile werden gebraucht.')],
    order(teile07), {'reihenfolgen': reih07},
    ['`name` und `wert` sind in `Gegenstand` privat.'],
    'Vererbung in Java: `extends` (nicht `implements`). Der Konstruktor ruft zuerst `super(name, wert)` auf und setzt '
    'dann das eigene Attribut. In `beschreibung()` liefert `super.beschreibung()` den Text „Heiltrank (20 Gold)" – ein '
    'direkter Zugriff auf `name` oder `wert` ist ein Übersetzungsfehler, weil sie in `Gegenstand` privat sind.'))

# ---------- 08 Vererbungspfeil
A.append(aufgabe(
    f'{L}-08', 'Der Stammbaum-Pfeil', 1, 'Klassendiagramm', [],
    [text('Wie wird „`Waffe` erbt von `Gegenstand`" im Klassendiagramm nach EH § 6 dargestellt?')],
    choice([('a', 'Pfeil mit hohler Dreiecksspitze von `Waffe` zu `Gegenstand`.'),
            ('b', 'Pfeil mit hohler Dreiecksspitze von `Gegenstand` zu `Waffe`.'),
            ('c', 'Einfache Linie zwischen `Waffe` und `Gegenstand`.'),
            ('d', 'Linie mit der Beschriftung „erbt" und der Kardinalität 1.')]),
    {'richtig': ['a']},
    ['Die Spitze zeigt auf die allgemeinere Klasse.'],
    'Vererbung: Pfeil mit **hohler Dreiecksspitze** von der Unterklasse **zur Oberklasse** („Waffe ist ein Gegenstand"). '
    'Eine einfache Linie bedeutet nach EH § 6 eine Assoziation (ein Attribut vom Typ der anderen Klasse). Beschriftungen '
    'und Kardinalitäten werden nicht verwendet.'))

LEVELS.append({"id": L, "nr": "1.4", "titel": "Die Waffenkammer – Vererbung und Polymorphie", "ds": [11],
               "ab": "AB W1·2 Vererbung – Infoteile 1–2, Aufgaben 1–5",
               "ide": "AQ_W1_L1_Heldenschmiede_Geruest.txt – Level 1.4 (Waffe, Trank, Schluessel; Testklasse L14VererbungTest)",
               "intro": [text('Eine **Unterklasse** (`extends`) erbt Attribute und Methoden und ergänzt eigene. Ihr Konstruktor '
                              'ruft zuerst `super(…)` auf. Überschreiben = gleiche Signatur neu definieren.'),
                         hinweis('**Merke:** Der Typ der **Variable** entscheidet, was aufgerufen werden *darf*; der Typ des '
                                 '**Objekts** entscheidet, welche Version *läuft* (dynamisches Binden).')],
               "aufgaben": [a['id'] for a in A if a['id'].startswith(L + '-')]})

import w1boss  # noqa: E402  (Boss-Pool)
BOSS_AUFGABEN = w1boss.build()
A.extend(BOSS_AUFGABEN)

WELT = {"version": 2, "welt": 1, "titel": "Die Heldenschmiede", "farbe": "#A0522D",
        "levels": LEVELS,
        "boss": {"id": "W1-BOSS", "titel": "Der Reitstall der Heldenschmiede", "dauerMin": 25, "anzahl": 8,
                 "mix": {"1": 3, "2": 3, "3": 2}, "pool": [a['id'] for a in BOSS_AUFGABEN]},
        "aufgaben": A}
