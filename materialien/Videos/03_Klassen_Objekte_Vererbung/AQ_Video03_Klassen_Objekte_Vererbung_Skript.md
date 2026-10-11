# Erklärvideo 3: Klassen, Objekte und Vererbung

> Vom Bauplan zum Objekt – mit Klassenkarte nach EH §6

| | |
|---|---|
| **Welt** | Welt 1 · Die Heldenschmiede |
| **Zielgruppe** | Informatik eA (LK), Welt 1; auch zur Wiederholung vor Boss, Klausur und Abitur |
| **Länge** | Ziel 9–11 min · Sprechtext ca. 9:35 min (bei 130 Wörtern/min, inkl. Pausen) |
| **Einsatz** | Welt 1, DS 8–11 · Lab-Level 1.1–1.4 · AB W1·1 „Klassen und Objekte“, AB W1·2 „Vererbung“ |
| **Folien** | `AQ_Video03_Klassen_Objekte_Vererbung_Folien.pptx` (17 Folien, Sprechertext auch in den Notizen) |

## Lernziele

- Klasse und Objekt unterscheiden; Attribute, Konstruktor (mit this) und Methoden einer Klasse benennen
- Eine Klasse als Klassenkarte nach EH §6 darstellen (+/- Pflicht, Konstruktor mit c, deutsche Typnamen) und Objekte als Objektkarte
- Referenzen verstehen: zwei Variablen können auf dasselbe Objekt zeigen; null vor dem Zugriff abfragen
- Assoziation und Vererbung im Klassendiagramm darstellen; super(...) und Überschreiben anwenden
- Bei überschriebenen Methoden begründen, welche Version läuft (das Objekt entscheidet)

## Hinweise für die Aufnahme

- Das durchgehende Beispiel (Klassen Waechter, Hauptmann, Tor; Namen Torvak, Elra, Brom, Kael, Nordtor) ist eigens für das Video gewählt und kommt in Lab, Arbeitsblättern, Bossen und Warm-up nicht vor – so verrät das Video keine Lösungen.
- Code geprüft mit javac/java (Java 21): w2 = new Waechter("Elra", 4) nach w2.verstaerken(5) → abwehr() = 9; a = new Waechter("Brom", 6), b = a, b.verstaerken(2) → a.abwehr() = 8; c = null → c.abwehr() wirft NullPointerException.
- Tor: istSicher() ohne Wächter = false, mit Torvak (6) = false, mit new Hauptmann("Elra", 6, 5) = true (11 ≥ 10). Waechter w = new Hauptmann("Elra", 6, 5): w.abwehr() = 11, w.getName() = "Elra".
- Pause-Aufgabe geprüft: Ausgabe 6, 9, 9 (q und r zeigen auf denselben Hauptmann Kael; ruestung 4 + 2 = 6, abwehr 6 + 3 = 9).
- Fehlerfolie geprüft: Konstruktor mit name = name (ohne this) → getName() liefert null; in Hauptmann return ruestung + schild → Compilerfehler „ruestung has private access in Waechter“; Hauptmann h = new Waechter("Brom", 6) → Compilerfehler „incompatible types“.
- Klassendiagramme (Assoziation, Vererbung), Objektkarten und Referenzbild sind zusammengesetzte Bilder in quellbilder/ (aus den Klassenkarten des Lab-Renderers, Pfeile ergänzt), weil der Generator noch keinen Block für Klassendiagramme mit Linien und Pfeilen hat.
- Folie „Kurz pausieren“: im Schnitt einen Hinweis „Video anhalten“ einblenden; die Lösung kommt erst auf der nächsten Folie.

## YouTube

**Titel:** Klassen, Objekte und Vererbung fürs Informatik-Abitur (Niedersachsen) | Algo Quest #3

**Beschreibung:**

```
Klasse oder Objekt? Was gehört in eine Klassenkarte nach den Ergänzenden Hinweisen (§6)? Und welche Methode läuft eigentlich, wenn eine Unterklasse sie überschreibt? In diesem Video lernst du an einem durchgehenden Beispiel aus dem Dungeon: Konstruktor und this, Objektkarten, Referenzen und null, Assoziation, Vererbung mit super – und die typischen Fehler, die im Abitur Punkte kosten.

Teil der Unterrichtsreihe „Algo Quest – Das Dungeon der Datenstrukturen“ (Informatik eA).
Üben mit sofortiger Rückmeldung: https://algoquest.frankjuchim.de/themen

Kapitel:
0:00 Einstieg
0:54 Klasse und Objekt
2:14 Klassenkarte
3:17 Referenzen und null
3:58 Assoziation
4:50 Vererbung
5:59 Welche Methode läuft?
6:38 Selbst ausprobieren
7:41 Typische Fehler
8:30 Zusammenfassung
```

_Zeitmarken sind aus der Textlänge geschätzt – nach dem Schnitt anpassen._

**Tags:** Informatik Abitur, Niedersachsen, Klassen und Objekte, Vererbung, Klassendiagramm, Objektorientierung, Java, Informatik LK, Algo Quest

## Drehbuch

### Folie 1 · 0:00 – Klassen, Objekte und Vererbung

*Regie: Kamera unten rechts, freundlicher Einstieg, Titelfolie im Hintergrund.*

Hallo und willkommen zur Algo Quest! Heute geht es um das Fundament der objektorientierten Programmierung: Klassen, Objekte und Vererbung. Im Abitur musst du Klassen lesen, erläutern, als Klassenkarte darstellen und in Java implementieren. Dafür gibt es feste Regeln – und ein paar Fallen, in die fast jeder einmal tappt. Wir bauen heute gemeinsam ein kleines Beispiel aus dem Dungeon: die Wächter, die die Tore bewachen.

### Folie 2 · 0:30 – Worum geht es im Abitur?

Typische Arbeitsaufträge im Abitur sind zum Beispiel: Erläutern Sie die Klasse. Stellen Sie die Klasse als Klassenkarte dar. Implementieren Sie den Konstruktor oder eine Methode. Oder: Geben Sie die Ausgabe des Programms an. Für die Klassenkarte gelten die Regeln aus den Ergänzenden Hinweisen, Paragraf sechs. Rechts siehst du, was heute drankommt.

### Folie 3 · 0:54 – Klasse und Objekt

Zuerst der wichtigste Unterschied. Eine Klasse ist ein Bauplan. Sie legt fest, welche Eigenschaften – die Attribute – und welche Fähigkeiten – die Methoden – alle Objekte dieser Art haben. Ein Objekt ist ein konkretes Exemplar nach diesem Bauplan, mit eigenen Werten. Erzeugt wird es mit new, und dabei setzt der Konstruktor die Startwerte. Aus einer Klasse kannst du beliebig viele Objekte bauen. Unser Beispiel: die Wächter des Dungeons. Jeder Wächter hat einen Namen und eine Rüstung, und seine Abwehr hängt von der Rüstung ab.

### Folie 4 · 1:33 – Die Klasse Waechter in Java

*Regie: Beim Konstruktor auf Zeile 6 zeigen: this.name links, Parameter name rechts.*

So sieht die Klasse in Java aus. Oben stehen die Attribute name und ruestung. Sie sind private – von außen kommt niemand direkt heran, das nennt man Datenkapselung. Darunter der Konstruktor. Er heißt genau wie die Klasse und hat keinen Rückgabetyp, nicht einmal void. Achte auf this: Der Parameter heißt auch name. Mit this Punkt name ist das Attribut des Objekts gemeint, rechts steht der Parameter. Dann folgen die öffentlichen Methoden: getName liefert den Namen, verstaerken erhöht die Rüstung, und abwehr gibt den Abwehrwert zurück – vorerst einfach die Rüstung.

### Folie 5 · 2:14 – Die Klassenkarte nach EH §6

Im Abitur stellst du eine Klasse als Klassenkarte dar. Sie hat drei Felder: oben der Klassenname, in der Mitte die Attribute, unten Konstruktoren und Methoden. Die Sichtbarkeit ist Pflicht: Plus für öffentlich, Minus für privat. Vor den Konstruktor schreibst du ein kleines c. Der Typ steht immer hinter dem Namen, durch einen Doppelpunkt getrennt, und zwar mit den deutschen Typnamen: Ganzzahl statt int, Zeichenkette statt String, und nichts statt void.

### Folie 6 · 2:47 – Objekte erzeugen – die Objektkarte

Jetzt erzeugen wir zwei Objekte: Torvak mit Rüstung sechs und Elra mit Rüstung vier. Danach wird Elra um fünf verstärkt. Den Zustand zur Laufzeit zeigst du mit Objektkarten. Im Kopf steht der Objektname, ein Doppelpunkt und die Klasse. Darunter stehen keine Typen, sondern die aktuellen Werte – Zeichenketten in Anführungszeichen. Beide Objekte haben dieselben Attribute, aber eigene Werte: Torvak hat Rüstung sechs, Elra inzwischen neun.

### Folie 7 · 3:17 – Referenzen und null

Jetzt wird es spannend. Eine Variable wie a enthält nicht das Objekt selbst, sondern eine Referenz darauf – einen Verweis. Die Zuweisung b gleich a kopiert deshalb nur diese Referenz. a und b zeigen auf dasselbe Objekt. Wenn wir über b verstärken, ändert sich auch das, was wir über a sehen: Die Ausgabe ist acht, nicht sechs. In der Objektkarte zeichnest du eine Referenz als Pfeil. Und null bedeutet: Diese Variable zeigt auf gar kein Objekt. Rufst du darauf eine Methode auf, stürzt das Programm mit einer NullPointerException ab.

### Folie 8 · 3:58 – Assoziation: Ein Tor kennt seinen Wächter

Objekte arbeiten zusammen. Ein Tor im Dungeon hat einen Wächter: Die Klasse Tor hat ein Attribut waechter vom Typ Waechter. Eine solche Beziehung heißt Assoziation. Im Klassendiagramm nach EH zeichnest du sie als einfache Linie zwischen den beiden Klassen – ohne Zahlen an den Enden, also ohne Kardinalitäten. Solange noch kein Wächter zugeteilt ist, ist das Attribut waechter null.

### Folie 9 · 4:25 – Vor dem Zugriff: null abfragen

Und genau deshalb musst du vor dem Zugriff prüfen. Die Methode istSicher soll wahr liefern, wenn das Tor einen Wächter mit Abwehr mindestens zehn hat. Ohne die Abfrage in Zeile zwei würde waechter Punkt abwehr bei einem Tor ohne Wächter abstürzen. Das ist Falle P1: Laufzeitfehler nicht ausgeschlossen. Merke dir: erst prüfen, dann zugreifen.

### Folie 10 · 4:50 – Vererbung: Ein Hauptmann ist ein Waechter

Nun zur Vererbung. Ein Hauptmann ist ein besonderer Wächter: Er hat zusätzlich einen Schild. Mit extends erbt Hauptmann alles von Waechter – Attribute und Methoden. Neu ist nur das Attribut schild. Im Konstruktor ruft super den Konstruktor der Oberklasse auf, der name und ruestung setzt. Das muss die erste Anweisung sein. Und die Methode abwehr wird überschrieben: gleiche Signatur, neues Verhalten. Weil ruestung in Waechter private ist, holt sich Hauptmann den Wert über super Punkt abwehr und addiert den Schild.

### Folie 11 · 5:27 – Vererbung im Klassendiagramm

Im Klassendiagramm zeigt ein Pfeil mit hohler Dreiecksspitze von der Unterklasse zur Oberklasse. Lies ihn als: Ein Hauptmann ist ein Waechter. In der Karte der Unterklasse stehen nur die neuen Elemente – hier schild und der eigene Konstruktor – und die überschriebenen Methoden. Steht abwehr in beiden Karten, weißt du: Die Methode wird in Hauptmann überschrieben. Was nicht gezeigt wird, kannst du in der Oberklasse mit drei Punkten andeuten.

### Folie 12 · 5:59 – Welche Methode läuft?

Jetzt die Frage, die im Abitur gern gestellt wird: Welche Methode läuft? Die Variable w hat den Typ Waechter, das Objekt ist aber ein Hauptmann. Das ist erlaubt, denn ein Hauptmann ist ein Waechter. Bei w Punkt abwehr entscheidet das Objekt: Es läuft die Version von Hauptmann, also sechs plus fünf gleich elf. Das nennt man dynamische Bindung. getName ist nicht überschrieben, also läuft die geerbte Version. Umgekehrt geht es nicht: Ein beliebiger Waechter ist kein Hauptmann – die letzte Zeile lässt sich nicht übersetzen.

### Folie 13 · 6:38 – Kurz pausieren: Jetzt du!

Jetzt bist du dran. Halte das Video an und gib die drei Ausgaben des Programms an. Zeichne dir dazu die Objekte und die Pfeile der Referenzen auf. Überlege: Wie viele Objekte gibt es eigentlich, und welche Version von abwehr läuft jeweils?

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 14 · 7:02 – Auflösung

Hier die Auflösung. Es gibt nur zwei Objekte: Brom und Kael. r gleich q kopiert nur die Referenz, r und q zeigen also beide auf Kael. Durch r Punkt verstaerken steigt Kaels Rüstung von vier auf sechs. Brom bleibt unverändert, seine Abwehr ist sechs. Bei q und r läuft die Version von Hauptmann, denn das Objekt ist ein Hauptmann: sechs plus drei gleich neun – zweimal. Wer bei r sechs oder bei q sieben geschrieben hat, hat entweder die Referenz oder die dynamische Bindung übersehen.

### Folie 15 · 7:41 – Typische Fehler – und wie du sie vermeidest

Die häufigsten Fehler, mit den Nummern aus unserer Fallen-Liste. P1: eine Methode auf null aufrufen, ohne vorher abzufragen. P3, Signatur verfehlt: Wer dem Konstruktor einen Rückgabetyp wie void gibt, schreibt in Java eine gewöhnliche Methode und keinen Konstruktor mehr. P4: Typen, die nicht zusammenpassen – ein Waechter-Objekt in einer Hauptmann-Variablen. Ein Klassiker ist auch name gleich name ohne this: Dann weist du den Parameter sich selbst zu, und das Attribut bleibt null. In der Unterklasse kommst du an private Attribute der Oberklasse nicht direkt heran – nutze super oder einen Getter. Und in der Klassenkarte fehlen gern die Sichtbarkeiten, oder es stehen Java-Typen und Kardinalitäten darin.

### Folie 16 · 8:30 – Das nimmst du mit

Fassen wir zusammen. Eine Klasse ist der Bauplan, ein Objekt ein Exemplar mit eigenen Werten, und der Konstruktor setzt die Startwerte. In der Klassenkarte sind Sichtbarkeiten Pflicht, Konstruktoren bekommen ein c, und die Typen stehen deutsch hinter dem Namen. Variablen speichern Referenzen – frag null ab, bevor du zugreifst. Assoziationen sind einfache Linien, Vererbung ein hohler Pfeil zur Oberklasse. Und bei überschriebenen Methoden entscheidet immer das Objekt.

### Folie 17 · 9:01 – 

Und jetzt du! Im Algo Quest Lab findest du dazu die Level eins Punkt eins bis eins Punkt vier – von der Schmiede bis zur Waffenkammer, jeweils mit sofortiger Rückmeldung. Auf den Arbeitsblättern Klassen und Objekte und Vererbung kannst du alles noch einmal nachlesen und üben. Im nächsten Video geht es in die Rangliste: Wir sortieren und suchen – und zählen, wie viel Arbeit das eigentlich ist. Bis dahin – viel Erfolg in der Heldenschmiede!
