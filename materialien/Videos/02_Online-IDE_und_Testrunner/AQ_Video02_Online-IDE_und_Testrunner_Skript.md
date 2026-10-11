# Erklärvideo 2: Die Online-IDE: Gerüst, Testrunner und Bibliothek „Niedersachsen“

> So programmierst und testest du in der Algo Quest

| | |
|---|---|
| **Welt** | Welt 0 · Die Akademie |
| **Zielgruppe** | Informatik eA (LK), Beginn der Einheit (DS 1–2); Wiederholung zu Beginn von Welt 4 (Bibliothek „Niedersachsen“) |
| **Länge** | Ziel 5–6 min · Sprechtext ca. 5:24 min (bei 130 Wörtern/min, inkl. Pausen) |
| **Einsatz** | Welt 0, DS 1–2 · Online-IDE Level 0 „Diagnose“ · AB W0·1 „Das Portal“, Aufgaben 2 und 3 · Welt 4, DS 24 (Bibliothek einschalten) |
| **Folien** | `AQ_Video02_Online-IDE_und_Testrunner_Folien.pptx` (17 Folien, Sprechertext auch in den Notizen) |

## Lernziele

- Einen Workspace in der Online-IDE öffnen bzw. importieren und den Aufbau eines Gerüsts verstehen (Kopfblock, GERÜST, DEIN TEIL, Tests, Hauptprogramm)
- Den eigenen Teil schreiben, ohne Signatur oder Tests zu verändern
- Den Testrunner starten und eine Meldung von assertEquals(erwartet, tatsächlich, Meldung) lesen
- Besonderheiten der Online-IDE kennen: println ohne System.out, Hauptprogramm außerhalb von Klassen, Bibliothek „Niedersachsen“ (nicht generisch, Casts), == bei Zeichenketten

## Hinweise für die Aufnahme

- Das Video ist weitgehend eine Live-Demo. Die Folien dienen als roter Faden; an den mit „Regie“ markierten Stellen in die Online-IDE wechseln. Beim Wechsel das IDE-Fenster so anordnen (Browser-Zoom 125–150 %), dass Code, Testrunner und Ausgabe nicht unten rechts liegen – die Kamera-Ecke bleibt frei. Alternativ die Kamera in den IDE-Szenen kleiner stellen.
- Für die Demo einen Test-Workspace mit dem Beispiel aus dem Video anlegen (Klasse Fackellager, Testklasse FackellagerTest, Hauptprogramm) – nicht in einem Kurs-Workspace arbeiten. Der vollständige Quelltext steht unten in diesen Hinweisen bzw. ergibt sich aus den Folien.
- Das Beispiel fackeln(raeume) ist eigens für das Video gewählt und kommt in Gerüsten, Lab, Arbeitsblättern, Bossen und Warm-up nicht vor.
- Geprüft mit dem Prüfstand (werkzeuge/ide-pruefung/ide_pruefen.py, javac/java + Nachbau der Bibliothek): Lösung `return (raeume + 2) / 3;` → 4/4 Tests grün; erster Versuch `return raeume / 3;` → genauDrei und keinRaum grün, angebrochen rot [erwartet 3, tatsächlich 2], zehnRaeume rot [erwartet 4, tatsächlich 3]; Platzhalter `return 0;` → nur keinRaum grün. fackeln(0) = 0, fackeln(3) = 1, fackeln(7) = 3, fackeln(10) = 4.
- Geprüft mit javac/java gegen den Nachbau aq.ni.Stack: push(5), push(8), (Integer) pop() → 8, danach top() = 5; pop auf leerem Stapel → IllegalStateException. Zeichenketten in echtem Java: teil = "Dra"; rune = teil + "che"; rune == "Drache" → false, rune.equals("Drache") → true.
- VOR AUFNAHME IN DER ECHTEN IDE PRÜFEN: (1) Menüpfad zum Importieren (Quelle: materialien/Online-IDE/LIESMICH.md „Workspace-Bereich → Workspace importieren“) und wie ausgeteilte Workspaces bei Schülerinnen und Schülern erscheinen; (2) genaue Beschriftung des Häkchens für die Bibliothek – die Quellen nennen „Niedersachsen“ (Gerüst W4, SPEC W4 §0) bzw. „Abiturklassen Niedersachsen“ (Testprotokoll, LIESMICH Online-IDE); auf der Folie steht deshalb nur „Niedersachsen“; (3) wie der Testrunner eine fehlgeschlagene assertEquals-Meldung genau anzeigt (erwartet/tatsächlich + eigene Meldung?); (4) dass `println(rune == "Drache")` in der Online-IDE tatsächlich true ausgibt (laut CLAUDE.md und Testprotokoll vergleicht == dort inhaltlich; die Probe im Testprotokoll ist noch offen); (5) Name des Startknopfs und des Ausgabebereichs.
- Folie „Kurz pausieren“: im Schnitt „Video anhalten“ einblenden; die Auflösung folgt auf der nächsten Folie.

## YouTube

**Titel:** Online-IDE für Java: Gerüst, Testrunner & Bibliothek Niedersachsen | Algo Quest #2

**Beschreibung:**

```
So arbeitest du in der Online-IDE (online-ide.de): Workspace öffnen, Aufbau eines Gerüsts mit „DEIN TEIL“, eigene Methode schreiben, Tests im Testrunner starten und die Meldungen von assertEquals richtig lesen. Dazu die Besonderheiten der Online-IDE: println ohne System.out, Hauptprogramm außerhalb von Klassen, die Abitur-Bibliothek „Niedersachsen“ mit Stack, Queue, DynArray und BinTree (nicht generisch – Casts!) und warum du Zeichenketten immer mit equals vergleichst.

Teil der Unterrichtsreihe „Algo Quest – Das Dungeon der Datenstrukturen“ (Informatik eA, Niedersachsen).
Üben mit sofortiger Rückmeldung: https://algoquest.frankjuchim.de/themen

Kapitel:
0:00 Einstieg
0:46 Workspace öffnen
1:06 Aufbau eines Gerüsts
1:32 Eigener Teil
2:16 Testrunner
3:02 Selbst ausprobieren
3:27 Hauptprogramm
3:46 Bibliothek „Niedersachsen“
4:09 Stolpersteine
4:49 Zusammenfassung
```

_Zeitmarken sind aus der Textlänge geschätzt – nach dem Schnitt anpassen._

**Tags:** Informatik Abitur, Niedersachsen, Online-IDE, Java, Testrunner, JUnit, Informatik LK, Algo Quest

## Drehbuch

### Folie 1 · 0:00 – Die Online-IDE: Gerüst, Testrunner und Bibliothek „Niedersachsen“

*Regie: Kamera unten rechts, Titelfolie im Hintergrund.*

Hallo und willkommen zur Algo Quest! In diesem Video zeige ich dir die Online-IDE, mit der wir die ganze Einheit über programmieren: wie ein Gerüst aufgebaut ist, wie du deinen Teil schreibst und wie dir der Testrunner sagt, ob dein Code stimmt. Am Ende kommen die Stolpersteine, die im Abitur Punkte kosten.

### Folie 2 · 0:24 – Warum die Online-IDE?

Die Online-IDE läuft im Browser, du musst nichts installieren. Für jede Welt gibt es einen Workspace mit Gerüst und fertigen Tests, die dir sofort sagen, was schon klappt. Aber denk daran: Im Abitur schreibst du ohne Compiler. Deshalb gilt oft: erst auf Papier, dann abtippen und testen.

### Folie 3 · 0:46 – Schritt 1: Den Workspace öffnen

*Regie: In die IDE wechseln: Anmeldung und Workspace-Liste zeigen. IDE-Fenster so anordnen, dass unten rechts (Kamera) nichts Wichtiges liegt. Menüpfade vor der Aufnahme in der echten IDE prüfen.*

Melde dich auf online-ide punkt de an. Meistens teilt deine Lehrkraft die Workspaces aus, dann stehen sie in deiner Liste. Eine Workspace-Datei importierst du im Workspace-Bereich. Und notfalls legst du selbst einen Workspace an und fügst den Text des Gerüsts in eine neue Datei ein.

### Folie 4 · 1:06 – Der Aufbau eines Gerüsts

Jedes Gerüst ist gleich aufgebaut. Oben der Kopfblock mit Anleitung und Spielregeln – lies ihn! Im Bereich GERÜST stehen Hilfsklassen, die du nicht veränderst. Dein Arbeitsplatz ist DEIN TEIL. Darunter die Tests, die du nie veränderst. Und ganz unten der Programmstart. Teile, die mit LEVEL-START auskommentiert sind, schaltest du erst frei, wenn dein Level dran ist.

### Folie 5 · 1:32 – Dein Teil: eine Methode schreiben

*Regie: In der IDE die Klasse Fackellager im Test-Workspace zeigen.*

Ein eigenes Beispiel: Eine Fackel brennt drei Räume lang. Die Methode fackeln soll ausrechnen, wie viele Fackeln du brauchst. Über der Methode steht die Signatur in Abitur-Notation. Du ersetzt die TODO-Zeile und das vorläufige return null. Den Methodenkopf lässt du stehen – sonst findet ihn kein Test, und im Abitur wäre das Falle P3.

### Folie 6 · 1:57 – Ein Test von innen

So sieht ein Test aus, markiert mit at Test. assertEquals hat drei Teile: zuerst den erwarteten Wert, hier drei. Dann den tatsächlichen Wert, also das, was deine Methode liefert. Und eine Meldung, die du siehst, wenn der Test rot wird.

### Folie 7 · 2:16 – Den Testrunner starten

*Regie: Live in der IDE: Reiter „Testrunner“ öffnen, FackellagerTest mit dem Dreieckspfeil starten. Mit dem Platzhalter return 0 ist nur keinRaum grün.*

Öffne den Reiter Testrunner. Der grüne Dreieckspfeil neben der Testklasse startet alle Tests, der neben einem einzelnen Test nur diesen. Grün heißt bestanden, rot heißt: Meldung lesen! Mit dem vorläufigen return null ist ein Test übrigens schon grün – reiner Zufall.

### Folie 8 · 2:35 – Meldungen lesen

*Regie: In der IDE return raeume / 3 eintippen, Tests starten, die rote Meldung zeigen.*

Ein erster Versuch: return raeume durch drei. Der Test angebrochen bleibt rot: sieben Räume, drei Fackeln – erwartet drei, tatsächlich zwei. Jetzt weißt du, wo du suchen musst: Sieben durch drei ist bei Ganzzahlen zwei, der Rest fällt weg. Falle P4.

### Folie 9 · 2:54 – Korrigiert: alle Tests grün

Der Trick: Vor dem Teilen zwei addieren, dann wird aufgerundet. Tests noch einmal starten – jetzt sind alle grün.

### Folie 10 · 3:02 – Kurz pausieren: Jetzt du!

Jetzt du: Halte das Video an und schreib einen eigenen Test für zehn Räume. Und was hätte der erste Versuch geliefert?

*(ca. 5 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 11 · 3:17 – Auflösung: der Test zehnRaeume

Zehn Räume brauchen vier Fackeln. Der erste Versuch hätte drei geliefert, der Test wäre rot gewesen. Gute Tests prüfen genau solche Grenzfälle.

### Folie 12 · 3:27 – Hauptprogramm und println

*Regie: In der IDE das Programm mit dem Startknopf laufen lassen und die Ausgabe zeigen.*

In der Online-IDE sind alle Anweisungen außerhalb von Klassen das Hauptprogramm, eine main-Methode brauchst du nicht. Ausgeben kannst du mit println, ohne System punkt out. Mit dem grünen Startknopf läuft das Programm. So probierst du deine Methoden auch ohne Tests aus.

### Folie 13 · 3:46 – Ab Welt 4: Bibliothek „Niedersachsen“

*Regie: Rechtsklick auf den Workspace → Einstellungen zeigen (Beschriftung des Häkchens vorher in der echten IDE prüfen).*

Ab Welt vier brauchst du die Abitur-Klassen Stack, Queue, DynArray und BinTree. Dafür schaltest du die Bibliothek Niedersachsen ein: Rechtsklick auf den Workspace, Einstellungen, Häkchen setzen. In den Workspaces ab Welt vier ist sie schon an. Diese Klassen sind nicht generisch, sie speichern Object. Was du herausholst, musst du casten.

### Folie 14 · 4:09 – Stolperstein: == bei Zeichenketten

*Regie: Live zeigen, dass die Online-IDE bei Zeile 3 true ausgibt (vor der Aufnahme prüfen).*

Und der gemeinste Stolperstein: In der Online-IDE vergleicht das doppelte Gleichheitszeichen Zeichenketten nach ihrem Inhalt. Zeile drei gibt true aus, deine Tests bleiben grün. In echtem Java prüft es aber, ob es dasselbe Objekt ist – und dann kommt false heraus. Im Abitur zählt echtes Java: Vergleiche Zeichenketten immer mit equals. Falle P5.

### Folie 15 · 4:34 – Typische Fehler – und wie du sie vermeidest

Die typischen Fehler: P3, den Methodenkopf ändern. P4, den Cast vergessen. P5, Zeichenketten mit doppeltem Gleichheitszeichen vergleichen. Tests veränderst du nie. Und hängt der Testrunner, hast du wohl eine Endlosschleife: Programm anhalten, Schleifenbedingung prüfen.

### Folie 16 · 4:49 – Das nimmst du mit

Kurz gesagt: Du schreibst nur in deinem Teil. Im Testrunner liest du bei Rot die Meldung: erwartet, tatsächlich. Ausgabe mit println, Hauptprogramm außerhalb von Klassen. Ab Welt vier Bibliothek einschalten und casten. Und Zeichenketten immer mit equals.

### Folie 17 · 5:06 – 

Jetzt ab in die IDE: Starte mit Level null, der Diagnose – dazu passen die Aufgaben zwei und drei auf dem Arbeitsblatt Das Portal. Im nächsten Video geht es in die Heldenschmiede: Klassen, Objekte und Vererbung. Bis dann!
