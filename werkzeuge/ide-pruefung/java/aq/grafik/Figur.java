package aq.grafik;

/**
 * Gemeinsame Oberklasse der Grafik-Nachbauten (Online-IDE: Shape/FilledShape). Die Methoden haben keine Wirkung –
 * geprüft wird nur, dass die Programme kompilieren und ohne Laufzeitfehler durchlaufen. Farben dürfen als Zahl
 * (0xRRGGBB) oder Zeichenkette ("red", "#ff0000") übergeben werden.
 */
public class Figur {
    private boolean zerstoert;

    protected void lebt() {
        if (zerstoert) throw new IllegalStateException("Figur wurde bereits mit destroy() entfernt");
    }
    public void setFillColor(Object farbe) { lebt(); }
    public void setFillColor(Object farbe, double alpha) { lebt(); }
    public void setBorderColor(Object farbe) { lebt(); }
    public void setBorderColor(Object farbe, double alpha) { lebt(); }
    public void setBorderWidth(double breite) { lebt(); }
    public void setAlpha(double alpha) { lebt(); }
    public void setVisible(boolean sichtbar) { lebt(); }
    public void move(double dx, double dy) { lebt(); }
    public void moveTo(double x, double y) { lebt(); }
    public void rotate(double winkel) { lebt(); }
    public void scale(double faktor) { lebt(); }
    public void bringToFront() { lebt(); }
    public void sendToBack() { lebt(); }
    public void destroy() { zerstoert = true; }
}
