# Erklärvideo 0: Algo Quest Lab: So funktioniert’s

> Beitreten, weiterspielen, Punkte sammeln – dein Start in die Übungsplattform

| | |
|---|---|
| **Welt** | Welt 0 · Die Akademie |
| **Zielgruppe** | Informatik eA (LK), Kickoff der Einheit; auch für alle, die später einsteigen oder ihren Zugang verloren haben |
| **Länge** | Ziel 4–5 min · Sprechtext ca. 4:27 min (bei 130 Wörtern/min, inkl. Pausen) |
| **Einsatz** | Welt 0, DS 1 (Kickoff) · Lab-Level 0.1 · AB W0·1 „Das Portal“, Infoteil „So funktioniert Algo Quest“ und Aufgabe 2 |
| **Folien** | `AQ_Video00_Algo_Quest_Lab_Folien.pptx` (16 Folien, Sprechertext auch in den Notizen) |

## Lernziele

- Dem Kurs im Lab beitreten (Kurscode + Name) und den persönlichen Code sicher notieren
- Auf jedem Gerät mit Name + persönlichem Code weiterspielen – ohne Kurscode
- Weltkarte, Level und Aufgaben bedienen; wissen, wie Punkte entstehen und was Tipps und „Lösung zeigen“ kosten
- Boss, Trainingsplatz, Warm-up-Trainer und Themenseite kennen

## Hinweise für die Aufnahme

- Die Screenshots in screenshots/ sind eigens für dieses Video entstanden (lokale Demo-Instanz mit frischer Datenbank, Kurs „Informatik LK“, Schülername „Lena S.“). Kurscode und persönlicher Code darauf sind zufällig und gehören zu keinem echten Kurs. Die Aufgabe mit Tipp stammt aus der Beispielwelt der Tests (Welt 9 „Testwelt“), nicht aus den echten Welten – das Video verrät also keine Lösung.
- Die älteren Screenshots in materialien/WebApp/Screenshots/ wurden bewusst nicht verwendet: weltkarte_alle_welten.jpg zeigt noch „Kata“ und „Reitstall der Gilde“ (veraltete Begriffe), warmup_trainer.jpg zeigt den Lösungsteil einer echten Warm-up-Karte.
- Punkteregeln geprüft im Code (src/domain.js punkteFuer, src/services/lernen.js): Punkte nur beim ERSTEN Lösen, Faktor = max(25 %, 1 − 25 % je Fehlversuch − 20 % je Tipp), gerundet; „Lösung zeigen“ = 0 Punkte (danach weiter üben möglich). Standardpunkte je Stufe: ★ 10, ★★ 20, ★★★ 30.
- Beispielwerte mit Node nachgerechnet: 10 P. ohne Fehler → 10; 20 P. mit 1 Tipp → 16; 20 P. mit 1 Tipp und 1 Fehlversuch → 11 (so auch im Screenshot „Noch bis zu 11 Punkte möglich“); 20 P. mit 4 Fehlversuchen → 5 (Untergrenze 25 %).
- Boss (src/services/boss.js, stand.js): Standard „auto“ = frei ab 60 % der Level-Punkte der Welt (die Lehrkraft kann Bosse auch sperren oder sofort öffnen); kein Feedback während des Kampfes, Auswertung am Ende, besiegt ab 50 %, bester Versuch zählt, neuer Versuch frühestens 12 h nach dem letzten. Boss Welt 0: 8 Aufgaben, 25 Minuten (Screenshot).
- Trainingsplatz: 1 Punkt je gelöster Zufallsaufgabe, höchstens 30 Punkte pro Tag (TRAINING_MAX_PUNKTE_TAG). Warm-up-Trainer: keine Punkte, Leitner-Fächer 1–5 (Wartezeit 0/1/3/7/14 Tage), Abzeichen für 30 Karten in Fach 5.
- Weiterspielen: Name + persönlicher Code genügen; das Feld Kurscode erscheint nur, wenn derselbe Name mit diesem Code in mehreren Kursen vorkommt (public/index.html). Im Profil („Dein Zugang“) lässt sich der Code wieder anzeigen.
- Folie „Probier es aus“: im Schnitt „Video anhalten“ einblenden. Für die Aufnahme ggf. live im Browser zeigen – dann eine Demo-Instanz bzw. einen Testkurs nehmen, keinen echten Kurscode zeigen.

## YouTube

**Titel:** Algo Quest Lab: So funktioniert’s – Beitreten, Punkte, Boss & Training | Algo Quest #0

**Beschreibung:**

```
Dein Start ins Algo Quest Lab: So trittst du deinem Kurs bei, notierst deinen persönlichen Code und spielst auf jedem Gerät weiter. Außerdem: Weltkarte und Level, wie Punkte entstehen (und was Tipps kosten), der Boss-Kampf auf Zeit, der Trainingsplatz, der Warm-up-Trainer und die Themenseite mit allen Arbeitsblättern.

Teil der Unterrichtsreihe „Algo Quest – Das Dungeon der Datenstrukturen“ (Informatik eA, Niedersachsen).
Zum Lab: https://algoquest.frankjuchim.de
Themen und Arbeitsblätter: https://algoquest.frankjuchim.de/themen

Kapitel:
0:00 Einstieg
0:30 Kurs beitreten
1:11 Weiterspielen
1:29 Weltkarte und Level
1:59 Punkte und Tipps
2:41 Boss, Training, Warm-up
3:25 Themenseite
3:37 Probier es aus
4:01 Zusammenfassung
```

_Zeitmarken sind aus der Textlänge geschätzt – nach dem Schnitt anpassen._

**Tags:** Informatik Abitur, Niedersachsen, Algo Quest Lab, Informatik LK, Java, Übungsplattform, Algo Quest

## Drehbuch

### Folie 1 · 0:00 – Algo Quest Lab: So funktioniert’s

*Regie: Kamera unten rechts, kurzer, lockerer Einstieg.*

Hallo und willkommen zur Algo Quest! In diesem kurzen Video zeige ich dir das Algo Quest Lab, unsere Übungsplattform für die ganze Einheit: wie du beitrittst, wie du weiterspielst und wie du Punkte sammelst.

### Folie 2 · 0:16 – Was ist das Algo Quest Lab?

Im Lab übst du zu jeder Doppelstunde mit Aufgaben im Abitur-Stil, und jede Antwort wird sofort geprüft. Es läuft im Browser, auf Laptop, Tablet oder Handy. Punkte, Ränge und Abzeichen entstehen automatisch.

### Folie 3 · 0:30 – Schritt 1: Kurs beitreten

*Regie: Auf Kurscode-Feld und Namensfeld zeigen.*

Öffne algoquest punkt frankjuchim punkt de oder scanne den QR-Code aus dem Unterricht – dann ist der Kurscode schon eingetragen. Unter Kurs beitreten wählst du deinen Namen: Vorname und Anfangsbuchstabe des Nachnamens, zum Beispiel Lena S. Bitte nicht den vollen Namen, denn er steht im Scoreboard des Kurses.

### Folie 4 · 0:53 – Schritt 2: Deinen Code notieren!

*Regie: Auf den großen Code im gestrichelten Kasten zeigen.*

Danach zeigt dir das Lab deinen persönlichen Code. Das ist dein Schlüssel: Schreib ihn sofort ins Heft oder mach ein Foto. Den Code behältst du für dich. Und falls er doch verloren geht: Deine Lehrkraft kann ihn dir anzeigen.

### Folie 5 · 1:11 – Weiterspielen: Name + Code

Beim nächsten Mal, zu Hause oder an einem anderen Gerät, wählst du Weiterspielen. Dort brauchst du nur deinen Namen und deinen persönlichen Code – keinen Kurscode mehr. Solange du angemeldet bist, findest du den Code auch in deinem Profil.

### Folie 6 · 1:29 – Die Weltkarte

Nach der Anmeldung landest du auf der Weltkarte. Oben stehen deine Punkte und dein Rang, darunter die sieben Welten. Jede Welt hat ein Level pro Doppelstunde, einen Trainingsplatz und am Ende einen Boss, der anfangs gesperrt ist.

### Folie 7 · 1:46 – Ein Level von innen

Ein Level beginnt mit einem Merke-Kasten und nennt das passende Arbeitsblatt. Darunter stehen die Aufgaben. Die Sterne zeigen die Stufe – dafür gibt es zehn, zwanzig oder dreißig Punkte.

### Folie 8 · 1:59 – Prüfen, Tipp, Lösung zeigen

*Regie: Auf die rot markierten Lücken, den Tipp-Kasten und die Meldung „Noch bis zu 11 Punkte möglich“ zeigen.*

In jeder Aufgabe gibt es drei Knöpfe: Prüfen gibt dir sofort Rückmeldung, falsche Lücken werden rot. Ein Tipp hilft dir weiter. Und Lösung zeigen zeigt die Lösung mit Erklärung. Unten steht, wie viele Punkte noch möglich sind.

### Folie 9 · 2:16 – So entstehen deine Punkte

Punkte gibt es nur beim ersten Lösen. Jeder Fehlversuch kostet ein Viertel, jeder Tipp ein Fünftel. Zwanzig Punkte werden mit einem Tipp also zu sechzehn, mit Tipp und Fehlversuch zu elf. Ein Viertel bleibt mindestens. Nur Lösung zeigen bringt null Punkte. Und: Punkte zeigen deinen Fortschritt, in die Note fließen sie nicht ein.

### Folie 10 · 2:41 – Der Boss: Abi auf Zeit

Am Ende jeder Welt wartet der Boss – eine Probe auf Zeit wie im Abitur. Er wird frei, sobald du sechzig Prozent der Level-Punkte der Welt hast, außer deine Lehrkraft schaltet ihn anders. Rückmeldung gibt es erst am Ende, ab fünfzig Prozent ist er besiegt. Es zählt dein bester Versuch, danach sind zwölf Stunden Pause.

### Folie 11 · 3:06 – Der Trainingsplatz

Auf dem Trainingsplatz bekommst du immer neue Zufallsaufgaben. Jede gelöste bringt einen Punkt, höchstens dreißig pro Tag.

### Folie 12 · 3:14 – Der Warm-up-Trainer

Der Warm-up-Trainer ist eine Lernkartei: Karte ziehen, auf Papier lösen, aufdecken und ehrlich einschätzen. Sichere Karten kommen seltener dran. Punkte gibt es hier keine.

### Folie 13 · 3:25 – Die Themenseite /themen

Auf der Themenseite unter Schrägstrich themen findest du alle Arbeitsblätter als PDF, sortiert nach Welten, Aufgabentypen und den Fallen P1 bis P10. Üben öffnet das passende Level.

### Folie 14 · 3:37 – Probier es aus!

Jetzt bist du dran: Halte das Video an, tritt bei und notiere deinen Code. Melde dich einmal ab und mit Name und Code wieder an – dann weißt du, dass dein Zugang klappt. Und dann löse die erste Aufgabe in Level null Punkt eins.

*(ca. 3 s Pause zum Mitdenken – im Schnitt ggf. kürzen und Hinweis „Video anhalten“ einblenden)*

### Folie 15 · 4:01 – Das nimmst du mit

Kurz gesagt: einmal mit Kurscode und Namen beitreten, den Code notieren, danach überall mit Name und Code weiterspielen. Punkte gibt es beim ersten Lösen, Fehlversuche und Tipps kosten etwas.

### Folie 16 · 4:14 – 

Weiter geht es im Lab mit Level null Punkt eins. Im nächsten Video zeige ich dir, wie du Algorithmen als Struktogramm und Tracetabelle aufschreibst. Viel Spaß im Dungeon!
