package aq.ni;

/** Nachbau der Klasse Stack der Bibliothek „Niedersachsen“ (nicht generisch, Inhalt Object). */
public class Stack {
    private Object[] daten = new Object[8];
    private int n = 0;

    public Stack() {}
    public boolean isEmpty() { return n == 0; }
    public void push(Object pContent) {
        if (pContent == null) throw new IllegalArgumentException("push(null)");
        if (n == daten.length) daten = java.util.Arrays.copyOf(daten, 2 * n);
        daten[n++] = pContent;
    }
    public Object pop() {
        if (n == 0) throw new IllegalStateException("pop auf leerem Stapel");
        Object o = daten[--n];
        daten[n] = null;
        return o;
    }
    public Object top() {
        if (n == 0) throw new IllegalStateException("top auf leerem Stapel");
        return daten[n - 1];
    }
}
