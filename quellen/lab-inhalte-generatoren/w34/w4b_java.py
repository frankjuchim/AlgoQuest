# Welt 4 – Boss-Pool-Snippets „Die Postkutschenstation“
from w4_java import *

REISENDER = '''
static class Reisender {
    private String name;
    private String ziel;
    public Reisender(String name, String ziel) { this.name = name; this.ziel = ziel; }
    public String getName() { return name; }
    public String getZiel() { return ziel; }
}
'''

seq("B01", '''
Stack sack = new Stack();
sack.push("Brief");
sack.push("Paket");
sack.push(sack.pop());
sack.push("Karte");
sack.pop();
sack.push("Zeitung");
sack.push(sack.top());
''', "st(sack)")

seq("B02", '''
Queue warte = new Queue();
warte.enqueue("Lotte");
warte.enqueue("Mats");
warte.enqueue("Nele");
warte.enqueue(warte.dequeue());
warte.dequeue();
warte.enqueue("Ole");
warte.enqueue(warte.head());
''', "qu(warte)")

seq("B03", '''
DynArray plan = new DynArray();
plan.append(9);
plan.append(13);
plan.insertAt(1, 11);
plan.insertAt(0, 7);
plan.delete(2);
plan.setItem(plan.getLength() - 1, 15);
plan.insertAt(2, (Integer) plan.getItem(0) + 5);
''', "da(plan)")

ANZ = '''
public static int anzahlNach(Queue q, String ziel) {
    Queue hilf = new Queue();
    int anzahl = 0;
    while (!q.isEmpty()) {
        Reisender r = (Reisender) q.dequeue();
        if (r.getZiel().equals(ziel)) {
            anzahl++;
        }
        hilf.enqueue(r);
    } // Ende auswerten
    while (!hilf.isEmpty()) {
        q.enqueue(hilf.dequeue());
    } // Ende zurueckstellen
    return anzahl;
}
'''
reg("B08", REISENDER + ANZ, '''Queue q = new Queue(); Reisender[] r = {new Reisender("Lotte", "Hafen"), new Reisender("Mats", "Burg"), new Reisender("Nele", "Hafen"), new Reisender("Ole", "Mühle")};
for (Reisender x : r) q.enqueue(x); out(K+"r", anzahlNach(q, "Hafen")); boolean gleich = true; for (Reisender x : r) if (q.dequeue() != x) gleich = false; out(K+"gleich", gleich); out(K+"leer", anzahlNach(new Queue(), "Hafen"));''',
    shown=ANZ)

L_B06 = '''
s.push(q.dequeue());
q.enqueue((Integer) s.pop() + (Integer) q.head());
s.push(q.dequeue());
q.enqueue(s.top());
int y = (Integer) s.pop() - (Integer) s.pop();
s.push(y);
'''
body = "Stack s = new Stack(); s.push(4); s.push(9); Queue q = new Queue(); q.enqueue(6); q.enqueue(1); q.enqueue(3);\nout(K+\"s0\", st(s)); out(K+\"q0\", qu(q));\n"
for i, z in enumerate(L_B06.strip("\n").split("\n"), 1):
    body += z + "\nout(K+\"s%d\", st(s)); out(K+\"q%d\", qu(q));\n" % (i, i)
    if z.startswith("int y"): body += "out(K+\"y\", y);\n"
reg("B06", "static void lauf() {\n" + body + "}", "lauf();", shown=L_B06)

ERSTE = '''
public static String ersteZwei(Queue q) {
    String a = (String) q.dequeue();
    String b = (String) q.dequeue();
    q.enqueue(a);
    q.enqueue(b);
    return a + " und " + b;
}
'''
reg("B07", ERSTE, '''Queue q = new Queue(); q.enqueue("Lotte"); q.enqueue("Mats"); q.enqueue("Nele"); out(K+"r", ersteZwei(q)); out(K+"q", qu(q));
Queue e = new Queue(); e.enqueue("Lotte"); try { ersteZwei(e); } catch (IllegalStateException x) { out(K+"eins", x.getMessage()); }''')

UMORDNEN = '''
public static void umordnen(Queue q, int n) {
    Queue hilf = new Queue();
    for (int i = 0; i < n; i++) {
        int t = (Integer) q.dequeue();
        if (t % 2 == 0) {
            hilf.enqueue(t);
        } else {
            q.enqueue(t);
        }
    }
    while (!hilf.isEmpty()) {
        q.enqueue(hilf.dequeue());
    }
}
'''
reg("B09", UMORDNEN, 'Queue q = new Queue(); for (int t : new int[]{4, 7, 2, 9, 5, 8}) q.enqueue(t); umordnen(q, 6); out(K+"q", qu(q));')

STREICHE = '''
public static void streiche(DynArray d, int grenze) {
    for (int i = 0; i < d.getLength(); i++) {
        if ((Integer) d.getItem(i) < grenze) {
            d.delete(i);
        }
    }
}
'''
PR_STR = 'DynArray d = new DynArray(); for (int t : new int[]{6, 7, 12, 5, 9}) d.append(t); try { streiche(d, 8); out(K+"d", da(d)); } catch (Exception e) { out(K+"d", ex(e)); }'
reg("B10", STREICHE, PR_STR)
reg("B10a", '''
public static void streiche(DynArray d, int grenze) {
    for (int i = d.getLength() - 1; i >= 0; i--) {
        if ((Integer) d.getItem(i) < grenze) {
            d.delete(i);
        }
    }
}
''', PR_STR)
reg("B10b", STREICHE.replace("d.delete(i);", "d.delete(i);\n            i--;"), PR_STR)
reg("B10c", STREICHE.replace("i < d.getLength()", "i <= d.getLength()"), PR_STR)
reg("B10d", STREICHE.replace("< grenze", "<= grenze"), PR_STR)

EINB = '''
public static void einbuchen(DynArray plan, int zeit) {
    int pos = 0;
    while (pos < plan.getLength() && (Integer) plan.getItem(pos) <= zeit) {
        pos++;
    }
    plan.insertAt(pos, zeit);
}
'''
reg("B11", EINB, '''DynArray p = new DynArray(); for (int t : new int[]{7, 9, 11, 14}) p.append(t); einbuchen(p, 11); out(K+"p", da(p)); einbuchen(p, 16); out(K+"p2", da(p)); DynArray e = new DynArray(); einbuchen(e, 8); out(K+"e", da(e));''')
reg("B11f", EINB.replace("pos < plan.getLength() && (Integer) plan.getItem(pos) <= zeit", "(Integer) plan.getItem(pos) <= zeit && pos < plan.getLength()"),
    '''DynArray p = new DynArray(); for (int t : new int[]{7, 9, 11, 14}) p.append(t); try { einbuchen(p, 16); out(K+"p", da(p)); } catch (Exception e) { out(K+"p", ex(e)); }''')

UNTEN = '''
public static String untersterSack(Stack s) {
    Stack hilf = new Stack();
    while (!s.isEmpty()) {
        hilf.push(s.pop());
    }
    String unten = (String) hilf.top();
    while (!hilf.isEmpty()) {
        s.push(hilf.pop());
    }
    return unten;
}
'''
reg("B12", UNTEN, '''Stack s = new Stack(); s.push("Brief"); s.push("Paket"); s.push("Karte"); String vor = st(s); out(K+"r", untersterSack(s)); out(K+"gleich", st(s).equals(vor));
try { untersterSack(new Stack()); out(K+"leer", "ok"); } catch (IllegalStateException e) { out(K+"leer", "IllegalStateException"); }''')

ZB2 = [("zug", "Abfahrt 8"), ("zug", "Abfahrt 10"), ("zug", "Abfahrt 12"), ("rueckgaengig", None), ("rueckgaengig", None), ("wiederholen", None),
       ("zug", "Abfahrt 15"), ("rueckgaengig", None), ("rueckgaengig", None), ("wiederholen", None)]
p = "Zugbuch b = new Zugbuch();\n"
for i, (m, a) in enumerate(ZB2, 1):
    p += ('b.zug("%s");\n' % a) if m == "zug" else ('out(K+"r%d", b.%s());\n' % (i, m))
p += 'out(K+"e", st(b.erledigt)); out(K+"z", st(b.zurueckgenommen));'
reg("B14", ZUGBUCH, p)

reg("B15", "", '''Stack s = new Stack(); s.push("Nele"); s.push("Mats"); s.push("Lotte"); Queue q = new Queue(); while (!s.isEmpty()) { q.enqueue(s.pop()); } out(K+"q", qu(q));
while (!q.isEmpty()) { s.push(q.dequeue()); } out(K+"s", st(s));
DynArray d = new DynArray(); while (!s.isEmpty()) { d.insertAt(0, s.pop()); } out(K+"d", da(d));''')

# --- woertliche Kompilierproben fuer angezeigte Aufruffolgen ---
ZB_TXT = "\n".join(('b.zug("%s");' % a) if m == "zug" else ("b.%s();" % m) for m, a in ZB_SEQ)
IN_TXT = "\n".join(('ini.%s("%s");' % (m, a)) if a else ("ini.%s();" % m) for m, a in IN_SEQ)
ZB2_TXT = "\n".join(('b.zug("%s");' % a) if m == "zug" else ("b.%s();" % m) for m, a in ZB2)
reg("TXT_ZB", ZUGBUCH + "static String lauf() {\nZugbuch b = new Zugbuch();\n" + ZB_TXT + "\nreturn st(b.erledigt);\n}", 'out(K+"e", lauf());')
reg("TXT_IN", INITIATIVE + "static String lauf() {\nInitiative ini = new Initiative();\n" + IN_TXT + "\nreturn qu(ini.reihe);\n}", 'out(K+"q", lauf());')
reg("TXT_ZB2", ZUGBUCH + "static String lauf() {\nZugbuch b = new Zugbuch();\n" + ZB2_TXT + "\nreturn st(b.erledigt);\n}", 'out(K+"e", lauf());')
reg("TXT_L1_05", "static void lauf() {\n" + L1_05.strip("\n") + "\n}", 'try { lauf(); out(K+"r", "ok"); } catch (IllegalStateException e) { out(K+"r", ex(e)); }')
reg("TXT_L5_03", "static String lauf(DynArray d) {\n" + L5_03.strip("\n") + "\nreturn da(e);\n}", 'DynArray d = new DynArray(); for (String n : new String[]{"Kupfer", "Tee", "Zimt", "Wolle"}) d.append(n); out(K+"e", lauf(d));')
reg("TXT_B05", REISENDER + "public static int anzahlNach(Queue q, String ziel) {\n    int anzahl = 0;\n    // ...\n    Reisender r = (Reisender) q.dequeue();\n    // ...\n    return anzahl;\n}", 'Queue q = new Queue(); q.enqueue(new Reisender("Lotte", "Hafen")); out(K+"r", anzahlNach(q, "Hafen"));')
