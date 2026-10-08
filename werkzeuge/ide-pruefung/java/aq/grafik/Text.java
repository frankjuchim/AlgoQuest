package aq.grafik;

/** Nachbau von Text(x, y, schriftgroesse, text). */
public class Text extends Figur {
    private String text;
    public Text(double x, double y, double groesse, String text) { this.text = text; }
    public void setText(Object t) { lebt(); text = String.valueOf(t); }
    public String getText() { return text; }
    public void setFontsize(double g) { lebt(); }
    public double getWidth() { return text.length() * 8; }
}
