package aq.ni;

import java.util.ArrayList;
import java.util.Iterator;

/** Nachbau der Klasse DynArray der Bibliothek „Niedersachsen“ (nicht generisch, Inhalt Object). */
public class DynArray implements Iterable<Object> {
    private final ArrayList<Object> daten = new ArrayList<>();

    public DynArray() {}
    public boolean isEmpty() { return daten.isEmpty(); }
    public int getLength() { return daten.size(); }
    private void pruefe(int index, int grenze) {
        if (index < 0 || index >= grenze) throw new IndexOutOfBoundsException("Index " + index + ", Laenge " + daten.size());
    }
    public Object getItem(int index) { pruefe(index, daten.size()); return daten.get(index); }
    public void setItem(int index, Object x) {
        if (x == null) throw new IllegalArgumentException("setItem(null)");
        pruefe(index, daten.size());
        daten.set(index, x);
    }
    public void append(Object x) {
        if (x == null) throw new IllegalArgumentException("append(null)");
        daten.add(x);
    }
    public void insertAt(int index, Object x) {
        if (x == null) throw new IllegalArgumentException("insertAt(null)");
        pruefe(index, daten.size() + 1);
        daten.add(index, x);
    }
    public void delete(int index) { pruefe(index, daten.size()); daten.remove(index); }
    public Iterator<Object> iterator() { return daten.iterator(); }
}
