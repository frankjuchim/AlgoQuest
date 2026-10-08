package aq.ni;

/** Nachbau der Klasse Queue der Bibliothek „Niedersachsen“ (nicht generisch, Inhalt Object). */
public class Queue {
    private final java.util.ArrayDeque<Object> daten = new java.util.ArrayDeque<>();

    public Queue() {}
    public boolean isEmpty() { return daten.isEmpty(); }
    public void enqueue(Object neu) {
        if (neu == null) throw new IllegalArgumentException("enqueue(null)");
        daten.addLast(neu);
    }
    public Object dequeue() {
        if (daten.isEmpty()) throw new IllegalStateException("dequeue auf leerer Schlange");
        return daten.removeFirst();
    }
    public Object head() {
        if (daten.isEmpty()) throw new IllegalStateException("head auf leerer Schlange");
        return daten.peekFirst();
    }
}
