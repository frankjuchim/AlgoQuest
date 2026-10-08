# Welt 4 – Java-Snippets (woertlich wie angezeigt) mit NI-Stub (Stack/Queue/DynArray Object-basiert)
from lib import *

J = JavaProg("W4Check", ni=True)
C = {}      # angezeigter Code

def reg(key, code, probe, extra="", shown=None):
    C[key] = (shown if shown is not None else code).strip("\n")
    J.add(key, code.strip("\n"), probe, None, extra)

def seq(key, shown, ret, probe_extra=""):
    """Anweisungsfolge: angezeigt = shown; kompiliert als Methode lauf(), Rueckgabe-Ausdruck ret (String)."""
    code = "static String lauf() {\n" + shown.strip("\n") + "\nreturn " + ret + ";\n}"
    reg(key, code, 'out(K+"r", lauf());' + probe_extra, shown=shown)

# ======================= L1: Stapel und Schlange =======================
seq("L1_01", '''
Stack s = new Stack();
s.push("Tee");
s.push("Zimt");
s.push("Reis");
s.pop();
s.push("Seide");
s.push(s.top());
s.pop();
s.push("Zinn");
''', "st(s)")

seq("L1_02", '''
Queue q = new Queue();
q.enqueue("Möwe");
q.enqueue("Albatros");
q.enqueue(q.head());
q.dequeue();
q.enqueue("Kormoran");
q.enqueue(q.dequeue());
q.dequeue();
''', "qu(q)")

L1_03 = '''
Stack s = new Stack();
s.push(12);
s.push(5);
s.isEmpty();
s.top();
s.pop();
s.push(30);
s.pop();
s.top();
'''
reg("L1_03", "static void lauf() {\n" + L1_03.strip("\n") + "\n}",
    'Stack s = new Stack(); s.push(12); s.push(5); out(K+"z4", s.isEmpty()); out(K+"z5", s.top()); out(K+"z6", s.pop()); s.push(30); out(K+"z8", s.pop()); out(K+"z9", s.top()); out(K+"ende", st(s)); lauf();',
    shown=L1_03)

L1_04 = '''
q.enqueue(s.pop());
s.push(q.dequeue());
q.enqueue(q.head());
int x = (Integer) s.pop() * (Integer) q.dequeue();
s.push(x);
s.push(q.dequeue());
q.enqueue(s.top());
'''
mz = L1_04.strip("\n").split("\n")
body = "Stack s = new Stack(); s.push(6); s.push(2); s.push(8); Queue q = new Queue(); q.enqueue(3); q.enqueue(7); q.enqueue(5);\nout(K+\"s0\", st(s)); out(K+\"q0\", qu(q));\n"
for i, z in enumerate(mz, 1):
    body += z + "\nout(K+\"s%d\", st(s)); out(K+\"q%d\", qu(q));\n" % (i, i)
    if z.startswith("int x"): body += "out(K+\"x\", x);\n"
reg("L1_04", "static void lauf() {\n" + body + "}", "lauf();", shown=L1_04)

L1_05 = '''
Queue q = new Queue();
q.enqueue("Kogge");
q.enqueue("Galeone");
String a = (String) q.dequeue();
q.enqueue(a);
q.dequeue();
q.dequeue();
String b = (String) q.head();
q.enqueue(b);
'''
body = "int zeile = 0;\ntry {\n"
for i, z in enumerate(L1_05.strip("\n").split("\n"), 1):
    body += "zeile = %d;\n%s\n" % (i, z)
body += "out(K+\"r\", \"ok\");\n} catch (Exception e) { out(K+\"zeile\", zeile); out(K+\"ex\", ex(e)); }\n"
reg("L1_05", "static void lauf() {\n" + body + "}", "lauf();", shown=L1_05)

L1_06 = '''
Stack kran = new Stack();     // Stapel vom Inhaltstyp Kiste
Queue zoll = new Queue();     // Schlange vom Inhaltstyp Ganzzahl
Stack zeichen = new Stack();  // Stapel vom Inhaltstyp Zeichen
kran.push(new Kiste("Zinn", 6));
zoll.enqueue(17);
zeichen.push('#');
Kiste k = (Kiste) kran.top();
int nummer = (Integer) zoll.dequeue();
char c = (Character) zeichen.pop();
'''
reg("L1_06", "static String lauf() {\n" + L1_06.strip("\n") + "\nreturn k.getName() + \"|\" + nummer + \"|\" + c;\n}",
    'out(K+"r", lauf()); Stack kran = new Stack(); kran.push(new Kiste("Zinn", 6)); try { int n = (Integer) kran.top(); out(K+"cast", "ok"); } catch (ClassCastException e) { out(K+"cast", "ClassCastException"); }',
    shown=L1_06)

DIFF = '''
public static int differenz(Stack s) {
    Kiste oben = s.pop();
    Kiste darunter = (Kiste) s.top();
    s.push(oben);
    return oben.getGewicht() - darunter.getGewicht();
}
'''
DIFF_OK = DIFF.replace("Kiste oben = s.pop();", "Kiste oben = (Kiste) s.pop();")
reg("L1_07", DIFF_OK, '''Stack e = new Stack(); try { differenz(e); } catch (IllegalStateException x) { out(K+"leer", x.getMessage()); }
Stack s1 = new Stack(); s1.push(new Kiste("Tee", 4)); try { differenz(s1); } catch (IllegalStateException x) { out(K+"eins", x.getMessage()); }
Stack s2 = new Stack(); s2.push(new Kiste("Tee", 4)); s2.push(new Kiste("Reis", 7)); out(K+"zwei", differenz(s2)); out(K+"zweiS", st(s2));''', shown=DIFF)
DIFF_A = '''
public static int differenz(Stack s) {
    if (s.isEmpty()) {
        return 0;
    }
    Kiste oben = (Kiste) s.pop();
    int d = 0;
    if (!s.isEmpty()) {
        d = oben.getGewicht() - ((Kiste) s.top()).getGewicht();
    }
    s.push(oben);
    return d;
}
'''
DIFF_B = '''
public static int differenz(Stack s) {
    if (s.isEmpty()) {
        return 0;
    }
    Kiste oben = (Kiste) s.pop();
    if (s.isEmpty()) {
        return 0;
    }
    Kiste darunter = (Kiste) s.top();
    s.push(oben);
    return oben.getGewicht() - darunter.getGewicht();
}
'''
DIFF_C = '''
public static int differenz(Stack s) {
    Kiste oben = (Kiste) s.pop();
    if (s.isEmpty()) {
        s.push(oben);
        return 0;
    }
    Kiste darunter = (Kiste) s.top();
    s.push(oben);
    return oben.getGewicht() - darunter.getGewicht();
}
'''
for nm, cd in (("A", DIFF_A), ("B", DIFF_B), ("C", DIFF_C)):
    reg("L1_07" + nm, cd, '''String erg = "";
for (int n = 0; n <= 3; n++) { Stack s = new Stack(); Kiste[] k = {new Kiste("Tee", 4), new Kiste("Reis", 7), new Kiste("Zinn", 6)}; for (int i = 0; i < n; i++) s.push(k[i]);
  String vor = st(s); try { int d = differenz(s); erg += n + ":" + d + (st(s).equals(vor) ? "=" : "!") + ";"; } catch (Exception e) { erg += n + ":" + ex(e) + ";"; } }
out(K+"erg", erg);''', shown=cd)

# ======================= L2: Spielmodule =======================
ZUGBUCH = '''
static class Zugbuch {
    private Stack erledigt = new Stack();
    private Stack zurueckgenommen = new Stack();
    public void zug(String z) { erledigt.push(z); zurueckgenommen = new Stack(); }
    public String rueckgaengig() { if (erledigt.isEmpty()) { return ""; } String z = (String) erledigt.pop(); zurueckgenommen.push(z); return z; }
    public String wiederholen() { if (zurueckgenommen.isEmpty()) { return ""; } String z = (String) zurueckgenommen.pop(); erledigt.push(z); return z; }
    public int anzahlZuege() { Stack h = new Stack(); int a = 0; while (!erledigt.isEmpty()) { h.push(erledigt.pop()); a++; } while (!h.isEmpty()) { erledigt.push(h.pop()); } return a; }
}
'''
INITIATIVE = '''
static class Initiative {
    private Queue reihe = new Queue();
    public void beitreten(String name) { reihe.enqueue(name); }
    public String amZug() { if (reihe.isEmpty()) { return ""; } String n = (String) reihe.dequeue(); reihe.enqueue(n); return n; }
    public boolean ausscheiden(String name) { Queue h = new Queue(); boolean g = false; while (!reihe.isEmpty()) { String n = (String) reihe.dequeue(); if (!g && n.equals(name)) { g = true; } else { h.enqueue(n); } } while (!h.isEmpty()) { reihe.enqueue(h.dequeue()); } return g; }
}
'''
ZB_SEQ = [("zug", "Feuer"), ("zug", "Eis"), ("rueckgaengig", None), ("zug", "Blitz"), ("zug", "Heilung"), ("rueckgaengig", None),
          ("rueckgaengig", None), ("wiederholen", None), ("wiederholen", None), ("rueckgaengig", None), ("zug", "Schild"), ("wiederholen", None)]
p = "Zugbuch b = new Zugbuch();\n"
for i, (m, a) in enumerate(ZB_SEQ, 1):
    if m == "zug": p += 'b.zug("%s"); out(K+"r%d", "-");\n' % (a, i)
    else: p += 'out(K+"r%d", "\\"" + b.%s() + "\\"");\n' % (i, m)
    p += 'out(K+"e%d", st(b.erledigt)); out(K+"z%d", st(b.zurueckgenommen));\n' % (i, i)
reg("L2_ZB", ZUGBUCH, p)

IN_SEQ = [("beitreten", "Aria"), ("beitreten", "Borin"), ("beitreten", "Cyra"), ("beitreten", "Drak"), ("amZug", None), ("amZug", None),
          ("ausscheiden", "Cyra"), ("amZug", None), ("beitreten", "Elva"), ("ausscheiden", "Ork"), ("amZug", None), ("amZug", None)]
p = "Initiative ini = new Initiative();\n"
for i, (m, a) in enumerate(IN_SEQ, 1):
    if m == "beitreten": p += 'ini.beitreten("%s"); out(K+"r%d", "-");\n' % (a, i)
    elif m == "amZug": p += 'out(K+"r%d", ini.amZug());\n' % i
    else: p += 'out(K+"r%d", ini.ausscheiden("%s"));\n' % (i, a)
    p += 'out(K+"q%d", qu(ini.reihe));\n' % i
reg("L2_IN", INITIATIVE, p)

AUS_BUG = '''
public boolean ausscheiden(String name) {
    while (!((String) reihe.head()).equals(name)) {
        reihe.enqueue(reihe.dequeue());
    }
    reihe.dequeue();
    return true;
}
'''
reg("L2_06", "Queue reihe = new Queue();\n" + AUS_BUG, '''
T_L2_06 a = new T_L2_06(); for (String n : new String[]{"Aria", "Borin", "Cyra"}) a.reihe.enqueue(n); a.ausscheiden("Borin"); out(K+"nach", qu(a.reihe));
T_L2_06 b = new T_L2_06(); try { b.ausscheiden("Aria"); out(K+"leer", "ok"); } catch (IllegalStateException e) { out(K+"leer", "IllegalStateException"); }
final T_L2_06 c = new T_L2_06(); c.reihe.enqueue("Aria"); c.reihe.enqueue("Borin");
Thread t = new Thread(() -> c.ausscheiden("Ork")); t.setDaemon(true); t.start(); t.join(800); out(K+"fehlt", t.isAlive() ? "endlos" : "endet");''', shown=AUS_BUG)

AUS_OK = '''
public boolean ausscheiden(String name) {
    Queue hilf = new Queue();
    boolean gefunden = false;
    while (!reihe.isEmpty()) {
        String n = (String) reihe.dequeue();
        if (!gefunden && n.equals(name)) {
            gefunden = true;
        } else {
            hilf.enqueue(n);
        }
    }
    reihe = hilf;
    return gefunden;
}
'''
reg("L2_07", "Queue reihe = new Queue();\n" + AUS_OK, '''
T_L2_07 a = new T_L2_07(); for (String n : new String[]{"Aria", "Borin", "Cyra", "Borin"}) a.reihe.enqueue(n);
out(K+"r1", a.ausscheiden("Borin")); out(K+"q1", qu(a.reihe)); out(K+"r2", a.ausscheiden("Ork")); out(K+"q2", qu(a.reihe));
T_L2_07 b = new T_L2_07(); out(K+"leer", b.ausscheiden("Aria"));''', shown=AUS_OK)

# ======================= L3: unveraendert =======================
ENTH_BUG = '''
public static boolean enthaelt(Stack s, String name) {
    Stack hilf = new Stack();
    while (!s.isEmpty()) {
        Kiste k = (Kiste) s.pop();
        hilf.push(k);
        if (k.getName().equals(name)) {
            return true;
        }
    }
    while (!hilf.isEmpty()) {
        s.push(hilf.pop());
    }
    return false;
}
'''
reg("L3_02", ENTH_BUG, '''Stack s = new Stack(); for (Kiste k : new Kiste[]{new Kiste("Kaffee", 4), new Kiste("Zinn", 6), new Kiste("Pfeffer", 5), new Kiste("Seide", 3), new Kiste("Tee", 4)}) s.push(k);
out(K+"r", enthaelt(s, "Pfeffer")); out(K+"s", st(s));
Stack t = new Stack(); for (Kiste k : new Kiste[]{new Kiste("Kaffee", 4), new Kiste("Zinn", 6)}) t.push(k); out(K+"r2", enthaelt(t, "Gold")); out(K+"t", st(t));''')

SUMME = '''
public static int summe(Queue q) {
    Queue hilf = new Queue();
    int summe = 0;
    while (!q.isEmpty()) {
        int x = (Integer) q.dequeue();
        summe = summe + x;
        hilf.enqueue(x);
    }
    while (!hilf.isEmpty()) {
        q.enqueue(hilf.dequeue());
    }
    return summe;
}
'''
reg("L3_03", SUMME, 'Queue q = new Queue(); q.enqueue(8); q.enqueue(3); q.enqueue(6); q.enqueue(2); out(K+"r", summe(q)); out(K+"q", qu(q));')

SCHWERE = '''
public static int anzahlSchwere(Stack s, int grenze) {
    Stack hilf = new Stack();
    int anzahl = 0;
    while (!s.isEmpty()) {
        Kiste k = (Kiste) s.pop();
        if (k.getGewicht() > grenze) {
            anzahl++;
        }
        hilf.push(k);
    } // Ende auswerten
    while (!hilf.isEmpty()) {
        s.push(hilf.pop());
    } // Ende zurueckschichten
    return anzahl;
}
'''
reg("L3_04", SCHWERE, '''Stack s = new Stack(); Kiste[] k = {new Kiste("Kupfer", 9), new Kiste("Tee", 4), new Kiste("Reis", 7), new Kiste("Zimt", 2)}; for (Kiste x : k) s.push(x);
String vor = st(s); out(K+"r", anzahlSchwere(s, 5)); boolean gleich = true; for (int i = k.length - 1; i >= 0; i--) { if (s.pop() != k[i]) gleich = false; } out(K+"gleich", gleich); out(K+"leer", anzahlSchwere(new Stack(), 5));''')

MAXROT = '''
public static int maxGewicht(Queue q) {
    int max = -1;
    while (!q.isEmpty()) {
        Kiste k = (Kiste) q.dequeue();
        if (k.getGewicht() > max) {
            max = k.getGewicht();
        }
        q.enqueue(k);
    }
    return max;
}
'''
reg("L3_05", MAXROT, '''out(K+"leer", maxGewicht(new Queue()));
final Queue q = new Queue(); q.enqueue(new Kiste("Tee", 4)); q.enqueue(new Kiste("Reis", 7));
Thread t = new Thread(() -> maxGewicht(q)); t.setDaemon(true); t.start(); t.join(800); out(K+"voll", t.isAlive() ? "endlos" : "endet");''')
MAXN = '''
public static int maxGewicht(Queue q, int n) {
    int max = -1;
    for (int i = 0; i < n; i++) {
        Kiste k = (Kiste) q.dequeue();
        if (k.getGewicht() > max) {
            max = k.getGewicht();
        }
        q.enqueue(k);
    }
    return max;
}
'''
reg("L3_05k", MAXN, '''Queue q = new Queue(); Kiste[] k = {new Kiste("Tee", 4), new Kiste("Reis", 7), new Kiste("Zinn", 6)}; for (Kiste x : k) q.enqueue(x);
out(K+"r", maxGewicht(q, 3)); boolean gleich = true; for (Kiste x : k) if (q.dequeue() != x) gleich = false; out(K+"gleich", gleich); out(K+"leer", maxGewicht(new Queue(), 0));''')

SCHWERSTE = '''
public static Kiste schwerste(Stack s) {
    Stack hilf = new Stack();
    Kiste beste = null;
    while (!s.isEmpty()) {
        Kiste k = (Kiste) s.pop();
        if (beste == null || k.getGewicht() > beste.getGewicht()) {
            beste = k;
        }
        hilf.push(k);
    }
    while (!hilf.isEmpty()) {
        s.push(hilf.pop());
    }
    return beste;
}
'''
PR_SCHW = '''Stack s = new Stack(); Kiste[] k = {new Kiste("Tee", 4), new Kiste("Kupfer", 7), new Kiste("Reis", 7), new Kiste("Zinn", 6)}; for (Kiste x : k) s.push(x);
Kiste b = schwerste(s); out(K+"r", b.getName()); boolean gleich = true; for (int i = k.length - 1; i >= 0; i--) { if (s.pop() != k[i]) gleich = false; } out(K+"gleich", gleich); out(K+"leer", schwerste(new Stack()) == null);'''
reg("L3_06", SCHWERSTE, PR_SCHW)
reg("L3_06f", SCHWERSTE.replace("k.getGewicht() > beste", "k.getGewicht() >= beste"), PR_SCHW)

reg("L3_08", '''static String rot(int n) { Queue q = new Queue(); for (String x : new String[]{"A", "B", "C", "D", "E"}) q.enqueue(x); for (int i = 0; i < n; i++) { q.enqueue(q.dequeue()); } return qu(q); }''',
    'out(K+"r3", rot(3)); out(K+"r5", rot(5)); out(K+"r7", rot(7));')

reg("L3_01", '''static String weg(boolean stapelQuelle, boolean hilfStapel, int stufen) {
  Object quelle; if (stapelQuelle) { Stack s = new Stack(); for (String x : new String[]{"C", "B", "A"}) s.push(x); quelle = s; } else { Queue q = new Queue(); for (String x : new String[]{"A", "B", "C"}) q.enqueue(x); quelle = q; }
  // umschichten in Hilfsstruktur(en) und zurueck
  java.util.List<Object> h = new java.util.ArrayList<>();
  Object cur = quelle; boolean curStapel = stapelQuelle;
  for (int st = 0; st < stufen; st++) { Object ziel = hilfStapel ? new Stack() : new Queue(); move(cur, curStapel, ziel, hilfStapel); cur = ziel; curStapel = hilfStapel; }
  move(cur, curStapel, quelle, stapelQuelle);
  return stapelQuelle ? obenZuerst((Stack) quelle) : qu((Queue) quelle); }
static void move(Object von, boolean vonStapel, Object nach, boolean nachStapel) {
  while (vonStapel ? !((Stack) von).isEmpty() : !((Queue) von).isEmpty()) { Object o = vonStapel ? ((Stack) von).pop() : ((Queue) von).dequeue(); if (nachStapel) ((Stack) nach).push(o); else ((Queue) nach).enqueue(o); } }
static String obenZuerst(Stack s) { String[] t = st(s).split(", "); StringBuilder b = new StringBuilder(); for (int i = t.length - 1; i >= 0; i--) { if (b.length() > 0) b.append(", "); b.append(t[i]); } return b.toString(); }''',
    'out(K+"ss", weg(true, true, 1)); out(K+"sq", weg(true, false, 1)); out(K+"qq", weg(false, false, 1)); out(K+"qs", weg(false, true, 1)); out(K+"qss", weg(false, true, 2));')

# ======================= L4: DynArray =======================
seq("L4_01", '''
DynArray d = new DynArray();
d.append(14);
d.append(3);
d.insertAt(0, 27);
d.insertAt(2, 9);
d.setItem(1, 50);
d.delete(0);
d.append(d.getItem(1));
d.insertAt(d.getLength(), 8);
''', "da(d)")

reg("L4_02", '''static String teste(int fall) { DynArray d = new DynArray(); d.append(5); d.append(6); d.append(7); d.append(8);
 try { switch (fall) { case 0: d.getItem(4); break; case 1: d.insertAt(4, 1); break; case 2: d.delete(4); break; case 3: d.setItem(3, 1); break; case 4: d.insertAt(5, 1); break; case 5: d.getItem(-1); break; case 6: d.delete(0); break; } return "ok"; } catch (Exception e) { return ex(e); } }''',
    'for (int i = 0; i <= 6; i++) out(K+"f"+i, teste(i));')

ENTF_NAME = '''
public static void entferneName(DynArray d, String name) {
    for (int i = 0; i < d.getLength(); i++) {
        Kiste k = (Kiste) d.getItem(i);
        if (k.getName().equals(name)) {
            d.delete(i);
        }
    }
}
'''
reg("L4_03", ENTF_NAME, 'DynArray d = new DynArray(); for (String n : new String[]{"Zimt", "Tee", "Tee", "Reis", "Tee", "Tee"}) d.append(new Kiste(n, 1)); entferneName(d, "Tee"); out(K+"r", da(d));')

LEICHT_BUG = '''
public static Kiste entferneLeichteste(DynArray d) {
    if (d.isEmpty()) {
        return null;
    }
    int minIndex = 0;
    for (int i = 1; i <= d.getLength(); i++) {
        Kiste k = (Kiste) d.getItem(i);
        if (k.getGewicht() < ((Kiste) d.getItem(minIndex)).getGewicht()) {
            minIndex = i;
        }
    }
    Kiste leicht = (Kiste) d.getItem(minIndex);
    d.delete(minIndex);
    return leicht;
}
'''
PR_LEICHT = '''DynArray d = new DynArray(); for (Kiste k : new Kiste[]{new Kiste("Zinn", 6), new Kiste("Tee", 4), new Kiste("Reis", 7), new Kiste("Kaffee", 4)}) d.append(k);
try { Kiste k = entferneLeichteste(d); out(K+"r", k.getName()); out(K+"d", da(d)); } catch (Exception e) { out(K+"r", ex(e)); }'''
reg("L4_04", LEICHT_BUG, PR_LEICHT)
reg("L4_04k", LEICHT_BUG.replace("i <= d.getLength()", "i < d.getLength()"), PR_LEICHT)

EINF = '''
public static void einfuegenSortiert(DynArray d, Kiste k) {
    int pos = 0;
    while (pos < d.getLength() && ((Kiste) d.getItem(pos)).getGewicht() <= k.getGewicht()) {
        pos++;
    }
    d.insertAt(pos, k);
}
'''
reg("L4_05", EINF, '''DynArray d = new DynArray(); for (Kiste k : new Kiste[]{new Kiste("Zimt", 2), new Kiste("Seide", 3), new Kiste("Tee", 4), new Kiste("Zinn", 6), new Kiste("Reis", 7)}) d.append(k);
einfuegenSortiert(d, new Kiste("Kaffee", 4)); out(K+"d", da(d)); einfuegenSortiert(d, new Kiste("Anker", 9)); out(K+"d2", da(d)); DynArray e = new DynArray(); einfuegenSortiert(e, new Kiste("Wolle", 3)); out(K+"e", da(e));''')

ENTF_LEICHTE = '''
public static int entferneLeichte(DynArray d, int grenze) {
    int anzahl = 0;
    int i = 0;
    while (i < d.getLength()) {
        Kiste k = (Kiste) d.getItem(i);
        if (k.getGewicht() < grenze) {
            d.delete(i);
            anzahl++;
        } else {
            i++;
        }
    }
    return anzahl;
}
'''
reg("L4_06", ENTF_LEICHTE, '''DynArray d = new DynArray(); for (Kiste k : new Kiste[]{new Kiste("Zimt", 2), new Kiste("Seide", 3), new Kiste("Zinn", 6), new Kiste("Wolle", 3), new Kiste("Reis", 7)}) d.append(k);
out(K+"r", entferneLeichte(d, 4)); out(K+"d", da(d));''')

DUP = '''
public static void entferneDuplikate(DynArray d) {
    for (int i = 0; i < d.getLength(); i++) {
        String name = ((Kiste) d.getItem(i)).getName();
        int j = i + 1;
        while (j < d.getLength()) {
            if (((Kiste) d.getItem(j)).getName().equals(name)) {
                d.delete(j);
            } else {
                j++;
            }
        }
    }
}
'''
reg("L4_07", DUP, '''DynArray d = new DynArray(); for (Kiste k : new Kiste[]{new Kiste("Tee", 4), new Kiste("Reis", 7), new Kiste("Tee", 3), new Kiste("Zimt", 2), new Kiste("Reis", 5), new Kiste("Tee", 1)}) d.append(k);
entferneDuplikate(d); out(K+"d", da(d));''')
reg("L4_07z", DUP.replace("if (((Kiste) d.getItem(j)).getName().equals(name)) {", "vgl++;\n            if (((Kiste) d.getItem(j)).getName().equals(name)) {"),
    '''DynArray d = new DynArray(); for (Kiste k : new Kiste[]{new Kiste("Tee", 4), new Kiste("Reis", 7), new Kiste("Tee", 3), new Kiste("Zimt", 2), new Kiste("Reis", 5), new Kiste("Tee", 1)}) d.append(k);
vgl = 0; entferneDuplikate(d); out(K+"vgl", vgl);
DynArray e = new DynArray(); for (String n : new String[]{"A", "B", "C", "D", "E", "F"}) e.append(new Kiste(n, 1)); vgl = 0; entferneDuplikate(e); out(K+"vgl6", vgl);''', extra="static int vgl = 0;")

reg("L4_08", '''static int s1(DynArray d) { int s = 0; for (int i = 0; i < d.getLength(); i++) { s += (Integer) d.getItem(i); } return s; }
static int s2(DynArray d) { int s = 0; for (Object o : d) { s += (Integer) o; } return s; }
static int s3(DynArray d) { int s = 0; for (int i = 0; i <= d.getLength(); i++) { s += (Integer) d.getItem(i); } return s; }
static int s4(DynArray d) { int s = 0; for (int i = 1; i < d.getLength(); i++) { s += (Integer) d.getItem(i); } return s; }''',
    '''DynArray d = new DynArray(); d.append(4); d.append(9); d.append(1); out(K+"s1", s1(d)); out(K+"s2", s2(d)); try { out(K+"s3", s3(d)); } catch (Exception e) { out(K+"s3", ex(e)); } out(K+"s4", s4(d));''')

# ======================= L5: Umformen, Klammern, Postfix =======================
seq("L5_01", '''
DynArray d = new DynArray();
d.append("Tee");
d.append("Zinn");
d.append("Reis");
d.append("Seide");
Stack s = new Stack();
for (int i = 0; i < d.getLength(); i++) {
    s.push(d.getItem(i));
}
s.pop();
''', "st(s)")

reg("L5_02", '''static Queue q3() { Queue q = new Queue(); q.enqueue("A"); q.enqueue("B"); q.enqueue("C"); return q; }
static Stack s3() { Stack s = new Stack(); s.push("C"); s.push("B"); s.push("A"); return s; }
static DynArray d3() { DynArray d = new DynArray(); d.append("A"); d.append("B"); d.append("C"); return d; }''',
    '''Queue q = q3(); DynArray d = new DynArray(); while (!q.isEmpty()) { d.append(q.dequeue()); } out(K+"e1", da(d));
DynArray d2 = d3(); Stack s = new Stack(); for (int i = 0; i < d2.getLength(); i++) { s.push(d2.getItem(i)); } String o = ""; while (!s.isEmpty()) { o += (o.isEmpty() ? "" : ", ") + s.pop(); } out(K+"e2", o);
Stack s2 = s3(); Queue q2 = new Queue(); while (!s2.isEmpty()) { q2.enqueue(s2.pop()); } out(K+"e3", qu(q2));
Queue q4 = q3(); DynArray d4 = new DynArray(); while (!q4.isEmpty()) { d4.insertAt(0, q4.dequeue()); } out(K+"e4", da(d4));
Stack s5 = s3(); DynArray d5 = new DynArray(); while (!s5.isEmpty()) { d5.append(s5.pop()); } out(K+"e5", da(d5));''')

L5_03 = '''
Queue q = new Queue();
for (int i = d.getLength() - 1; i >= 0; i--) {
    q.enqueue(d.getItem(i));
}
Stack s = new Stack();
while (!q.isEmpty()) {
    s.push(q.dequeue());
}
DynArray e = new DynArray();
while (!s.isEmpty()) {
    e.append(s.pop());
}
'''
z = L5_03.strip("\n").split("\n")
body = 'DynArray d = new DynArray(); for (String n : new String[]{"Kupfer", "Tee", "Zimt", "Wolle"}) d.append(n);\n' + "\n".join(z[:4]) + '\nout(K+"d4", da(d)); out(K+"q4", qu(q));\n' + "\n".join(z[4:8]) + '\nout(K+"q8", qu(q)); out(K+"s8", st(s));\n' + "\n".join(z[8:]) + '\nout(K+"s12", st(s)); out(K+"e12", da(e)); out(K+"d12", da(d));\n'
reg("L5_03", "static void lauf() {\n" + body + "}", "lauf();", shown=L5_03)

KLAMMER = '''
public static boolean passt(char auf, char zu) {
    return (auf == '(' && zu == ')') || (auf == '[' && zu == ']') || (auf == '{' && zu == '}');
}

public static boolean klammernOk(String s) {
    Stack offen = new Stack();
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == '(' || c == '[' || c == '{') {
            offen.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            if (offen.isEmpty()) {
                return false;
            }
            char auf = (Character) offen.pop();
            if (!passt(auf, c)) {
                return false;
            }
        }
    }
    return offen.isEmpty();
}
'''
KL_TESTS = ["{a[b(c)]}", "([)]", "(()", "x(y)[z]{}", "}{", "[(a+b)*(c-d)]", "({x}[y](z))"]
reg("L5_04", KLAMMER, "".join('out(K+"t%d", klammernOk("%s"));' % (i, t) for i, t in enumerate(KL_TESTS)) +
    '''String s = "({x}[y](z))"; Stack offen = new Stack(); String tr = ""; for (int i = 0; i < s.length(); i++) { char c = s.charAt(i); if (c == '(' || c == '[' || c == '{') { offen.push(c); tr += c + ":" + st(offen) + ";"; } else if (c == ')' || c == ']' || c == '}') { char a = (Character) offen.pop(); tr += c + ":" + st(offen) + ":" + passt(a, c) + ";"; } } out(K+"trace", tr);''')

KL_BUG = '''
public static boolean klammernOk(String s) {
    Stack offen = new Stack();
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == '(' || c == '[' || c == '{') {
            offen.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            char auf = (Character) offen.pop();
            if (!passt(auf, c)) {
                return false;
            }
        }
    }
    return true;
}
'''
reg("L5_08", KL_BUG + '''
public static boolean passt(char auf, char zu) {
    return (auf == '(' && zu == ')') || (auf == '[' && zu == ']') || (auf == '{' && zu == '}');
}''', '''out(K+"a", klammernOk("(()")); try { out(K+"b", klammernOk("())")); } catch (Exception e) { out(K+"b", ex(e)); } out(K+"c", klammernOk("[()]"));''', shown=KL_BUG)

POSTFIX = '''
public static int postfix(String ausdruck) {
    Stack werte = new Stack();
    for (int i = 0; i < ausdruck.length(); i++) {
        char c = ausdruck.charAt(i);
        if (c >= '0' && c <= '9') {
            werte.push((int) c - (int) '0');
        } else {
            int b = (Integer) werte.pop();
            int a = (Integer) werte.pop();
            if (c == '+') {
                werte.push(a + b);
            } else if (c == '-') {
                werte.push(a - b);
            } else {
                werte.push(a * b);
            }
        }
    }
    return (Integer) werte.pop();
}
'''
PF_TESTS = ["83-52*+", "72-31+*", "94-2-", "942--", "62*43-+", "95-3*", "953-*"]
reg("L5_06", POSTFIX, "".join('out(K+"p%d", postfix("%s"));' % (i, t) for i, t in enumerate(PF_TESTS)) +
    '''String s = "83-52*+"; Stack w = new Stack(); String tr = ""; for (int i = 0; i < s.length(); i++) { char c = s.charAt(i); if (c >= '0' && c <= '9') { w.push((int) c - (int) '0'); } else { int b = (Integer) w.pop(); int a = (Integer) w.pop(); w.push(c == '+' ? a + b : c == '-' ? a - b : a * b); } tr += c + ":" + st(w) + ";"; } out(K+"trace", tr);''')
reg("L5_07f", POSTFIX.replace("int b = (Integer) werte.pop();\n            int a = (Integer) werte.pop();", "int a = (Integer) werte.pop();\n            int b = (Integer) werte.pop();"),
    "".join('out(K+"p%d", postfix("%s"));' % (i, t) for i, t in enumerate(PF_TESTS)))

# ======================= L6: Flut, Aufwand, Knoten =======================
FLUT = '''
static String flute(String[] k, int z, int s, boolean mitSchlange) {
    char[][] karte = new char[k.length][k[0].length()]; for (int a = 0; a < k.length; a++) karte[a] = k[a].toCharArray();
    String spur = ""; Queue q = new Queue(); Stack st = new Stack(); int max = 0, n = 1;
    karte[z][s] = '+'; spur += z + "," + s + ";";
    if (mitSchlange) q.enqueue(z * 1000 + s); else st.push(z * 1000 + s);
    int[] dz = {-1, 0, 1, 0}; int[] ds = {0, 1, 0, -1};
    while (!q.isEmpty() || !st.isEmpty()) {
        int pos = mitSchlange ? (Integer) q.dequeue() : (Integer) st.pop(); n--;
        int pz = pos / 1000, ps = pos % 1000;
        for (int r = 0; r < 4; r++) { int nz = pz + dz[r], ns = ps + ds[r];
            if (nz >= 0 && nz < karte.length && ns >= 0 && ns < karte[0].length && karte[nz][ns] == '.') {
                karte[nz][ns] = '+'; spur += nz + "," + ns + ";"; if (mitSchlange) q.enqueue(nz * 1000 + ns); else st.push(nz * 1000 + ns); n++; } }
        if (n > max) max = n; }
    return spur + "#" + max;
}
'''
BECKEN = ["....", ".#..", "...#"]
reg("L6_02", FLUT, 'out(K+"q", flute(new String[]{%s}, 1, 0, true)); out(K+"s", flute(new String[]{%s}, 1, 0, false));' % (", ".join('"%s"' % x for x in BECKEN), ", ".join('"%s"' % x for x in BECKEN)))

MEIN = '''
static class Knoten {
    private Object inhalt;
    private Knoten naechster;
    public Knoten(Object inhalt, Knoten naechster) { this.inhalt = inhalt; this.naechster = naechster; }
    public Object getInhalt() { return inhalt; }
    public Knoten getNaechster() { return naechster; }
}
static class MeinStapel {
    private Knoten kopf = null;
    public boolean isEmpty() { return kopf == null; }
    public void push(Object inhalt) { kopf = new Knoten(inhalt, kopf); }
    public Object top() { if (kopf == null) { throw new IllegalStateException("Der Stapel ist leer."); } return kopf.getInhalt(); }
%s
}
'''
POP = '''public Object pop() {
    if (kopf == null) {
        throw new IllegalStateException("Der Stapel ist leer.");
    }
    Object o = kopf.getInhalt();
    kopf = kopf.getNaechster();
    return o;
}'''
reg("L6_06", MEIN % POP, '''MeinStapel m = new MeinStapel(); Stack s = new Stack(); long seed = 7; boolean gleich = true;
for (int i = 0; i < 400; i++) { seed = (seed * 1103515245 + 12345) % 2147483648L; int op = (int) (seed % 3);
  if (op == 0) { m.push(i); s.push(i); } else { Object a = null, b = null; String ea = "", eb = ""; try { a = m.pop(); } catch (IllegalStateException e) { ea = "ISE"; } try { b = s.pop(); } catch (IllegalStateException e) { eb = "ISE"; } if (!ea.equals(eb) || (a != null && !a.equals(b))) gleich = false; } }
out(K+"gleich", gleich);
MeinStapel x = new MeinStapel(); x.push("Erz"); x.push("Holz"); x.push("Gold"); out(K+"p1", x.pop()); out(K+"p2", x.pop()); out(K+"top", x.top());''')

ZWEI = '''
static class ZweiStapelSchlange {
    private Stack ein = new Stack();
    private Stack aus = new Stack();
    int umgeschichtet = 0;

    public void enqueue(Object x) {
        ein.push(x);
    }

    public Object dequeue() {
        if (aus.isEmpty()) {
            while (!ein.isEmpty()) {
                aus.push(ein.pop());
                umgeschichtet++;
            }
        }
        return aus.pop();
    }
}
'''
reg("L6_07", ZWEI, '''ZweiStapelSchlange z = new ZweiStapelSchlange(); String o = "";
z.enqueue("A"); z.enqueue("B"); z.enqueue("C"); o += z.dequeue(); out(K+"u1", z.umgeschichtet); z.enqueue("D"); o += z.dequeue(); o += z.dequeue(); z.enqueue("E"); o += z.dequeue(); out(K+"u4", z.umgeschichtet); o += z.dequeue();
out(K+"aus", o); out(K+"u", z.umgeschichtet);''')
