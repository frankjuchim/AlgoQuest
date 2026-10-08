package aq.ni;

/**
 * Nachbau der Klasse BinTree der Bibliothek „Niedersachsen“: Ein nicht leerer Baum hat immer zwei
 * (ggf. leere) Teilbäume; Zugriffe auf einen leeren Baum werfen IllegalStateException.
 */
public class BinTree {
    private Object item;
    private BinTree links, rechts;

    public BinTree() {}
    public BinTree(Object o) { setItem(o); }
    public boolean isEmpty() { return item == null; }
    private void nichtLeer(String op) { if (item == null) throw new IllegalStateException(op + " auf leerem Baum"); }
    public Object getItem() { nichtLeer("getItem"); return item; }
    public void setItem(Object o) {
        if (o == null) throw new IllegalArgumentException("setItem(null)");
        if (item == null) { links = new BinTree(); rechts = new BinTree(); }
        item = o;
    }
    public boolean isLeaf() { return item != null && links.isEmpty() && rechts.isEmpty(); }
    public BinTree getLeft() { nichtLeer("getLeft"); return links; }
    public BinTree getRight() { nichtLeer("getRight"); return rechts; }
    public void setLeft(BinTree b) {
        nichtLeer("setLeft");
        if (b == null) throw new IllegalArgumentException("setLeft(null)");
        links = b;
    }
    public void setRight(BinTree b) {
        nichtLeer("setRight");
        if (b == null) throw new IllegalArgumentException("setRight(null)");
        rechts = b;
    }
    public void setEmpty() { item = null; links = null; rechts = null; }
}
