# Erklärvideos zur Algo Quest – Übersicht

**Nicht öffentlich** – Arbeitsmaterial für die Aufnahme. Arbeitsweise und Dateiformat: [`LIESMICH.md`](LIESMICH.md).

## Die Idee

Kurze Erklärvideos auf dem Kanal **frankjuchim**, jeweils zu einem Abitur-Kernthema der Einheit. Präsentation im
Hintergrund, Kamera klein unten rechts. Jedes Video verweist auf das passende Level im Lab, später wird es dort
verlinkt.

**Warum sich das lohnt:**

- **Nacharbeiten und Wiederholen:** Wer gefehlt hat oder vor dem Boss bzw. der Klausur wiederholt, hat die
  Kernidee in zehn Minuten wieder.
- **Abi-Vorbereitung:** Die Videos decken genau die Notationen und Fallen ab, die im Abitur Punkte kosten (EH §5/§6,
  P1–P10). Sie bleiben über die Einheit hinaus nützlich.
- **Entlastung im Unterricht:** Die Werkzeug-Videos (Lab, Online-IDE) ersparen wiederholte Erklärungen.
- **Reichweite:** Die Themen sind für das niedersächsische Abitur allgemein relevant, nicht nur für den eigenen Kurs.

**Damit es funktioniert:**

- **Keine Lösungen verraten:** Alle Beispiele sind eigens für die Videos gewählt und stammen nicht aus Lab-Aufgaben,
  Arbeitsblättern, Bossen, Warm-up-Karten oder Klausuren.
- **Zeitlos halten:** keine Daten, keine Kursnamen, keine Kurscodes, keine Schülernamen.

## Die Videos

Neun Videos: zwei Werkzeug-Videos und je ein Kernvideo pro Welt.

| Nr. | Video | Welt · Einsatz | Länge | Inhalt (Kern) |
|---|---|---|---|---|
| 00 | **Algo Quest Lab: So funktioniert’s** | Kickoff, DS 1 | 4–5 min | Beitritt mit Kurscode und Name, persönlicher Code, Weiterspielen mit Name und Code, Weltkarte, Level, Tipps und Punkte, Boss, Trainingsplatz, Warm-up, Themenseite |
| 01 | **Struktogramm und Tracetabelle** | W0, DS 1–2 · Level 0.1/0.2 | 8–10 min | Bausteine nach EH §5, Java → Struktogramm, Tracetabelle (nur Variablen, `// → Tabellenzeile`), Fallen P4/P6/P8/P9 |
| 02 | **Die Online-IDE: Gerüst, Testrunner, Bibliothek** | W0, DS 2 (und W4) | 5–6 min | Workspace importieren, Gerüst „DEIN TEIL“, Testrunner lesen, `println`, Bibliothek „Niedersachsen“ einschalten, typische Stolpersteine |
| 03 | **Klassen, Objekte, Vererbung** | W1 · Level 1.1–1.4 | 9–11 min | Klasse vs. Objekt, Klassenkarte nach EH §6, Konstruktor, Referenzen/null, Assoziation, Vererbung mit super, Überschreiben |
| 04 | **Sortieren und binäre Suche** | W2 · Level 2.2–2.4 | 10–12 min | Selection-, Insertion-, Bubblesort im Vergleich, Vergleiche zählen n(n − 1)/2, binäre Suche mit lo/hi/mid, Effizienz |
| 05 | **Rekursion verstehen** | W3 · Level 3.1/3.2 | 9–11 min | Basisfall und Rekursionsschritt, Aufrufstapel, Rekursionstabelle mit Tiefe (Start bei 0), Aufrufbaum, P7 |
| 06 | **Stapel und Schlange** | W4 · Level 4.1/4.3 | 9–11 min | ADT-Schnittstellen nach EH §4, NI-Klassen nicht generisch (Casts), Laufzeitfehler vermeiden (P1), Struktur unverändert lassen (P2) |
| 07 | **Binärbäume und Suchbäume** | W5 · Level 5.1/5.2/5.4 | 10–12 min | Begriffe und Höhe (leer 0, Blatt 1), pre-/in-/postorder, rekursives Muster mit `isEmpty`, Suchbaum: suchen und einfügen |
| 08 | **Abi-Check: die 10 Fallen** | W6 · Level 6.1/6.2 | 9–11 min | Operatoren und Zeitplanung, P1–P10 mit Mini-Beispielen, Checkliste vor der Abgabe |

**Produktionsreihenfolge:** 00 und 01 zuerst, weil sie zum Start gebraucht werden. Danach jeweils etwa eine Woche
vor Beginn der Welt, 08 vor der Generalprobe.

**Länge:** Die Kernvideos dauern 8–12 Minuten, die Werkzeug-Videos 4–6 Minuten. Jedes Video hat nur ein Lernziel,
Vertiefungen bleiben im Lab und auf den Arbeitsblättern. Wird ein Skript länger als 12 Minuten, besser kürzen oder
teilen.

## Aufbau jedes Videos

1. **Einstieg (≤ 30 s):** Worum geht es, warum ist das abiturrelevant?
2. **Erklärung am Beispiel:** ein durchgehendes, eigenes Beispiel aus dem Dungeon-Setting.
3. **⏸ Pause-Aufgabe:** „Video anhalten“, selbst probieren, danach die Auflösung. Das aktiviert mehr als reines
   Zuschauen.
4. **Typische Fehler:** mit den Fallen-Nummern P1–P10, wie im Lab und auf den Arbeitsblättern.
5. **Zusammenfassung:** drei bis vier Merksätze.
6. **Weiter im Lab:** konkretes Level und Arbeitsblatt, Ausblick auf das nächste Video. Die letzten 20 s eignen sich
   für den YouTube-Abspann (Endcard).

## Was im Ordner liegt

Je Video gibt es:

- **Folien** (`…_Folien.pptx`): im Hausstil der Materialien, mit freier **Kamera-Zone unten rechts**. Der
  Sprechertext steht in den **Notizen**, sodass die Referentenansicht als Teleprompter dient.
- **Drehbuch** (`…_Skript.md`): Lernziele, Hinweise zur Aufnahme mit den nachgerechneten Werten, YouTube-Titel,
  Beschreibung, Kapitelmarken und Tags, Folie für Folie mit Sprechertext und Regieanweisungen.
- **`video.json`:** die Quelle. Nach Änderungen erzeugt `python3 werkzeuge/video_folien.py` Folien und Drehbuch neu.

Der Sprechertext ist ein Vorschlag zum freien Sprechen, nicht zum Ablesen. Kürze ihn ruhig auf deine Formulierungen.

## Tipps zur Aufnahme

- **Szene (z. B. OBS):** Folien als Fenster- oder Bildschirmaufnahme in 1920 × 1080. Die Kamera unten rechts
  braucht etwa 22–25 % der Breite, gern mit abgerundetem Rahmen und leichtem Schatten. Die Kamera-Zone der Folien ist
  dafür freigehalten. Den Hintergrund ruhig halten oder weichzeichnen.
- **Ton vor Bild:** Ein Ansteck- oder USB-Mikrofon nah am Mund, ein kleiner Raum mit Stoff (Vorhänge, Teppich), kein
  Hall. Rauschunterdrückung und Limiter in OBS bringen viel.
- **Licht:** Das Gesicht frontal von vorn beleuchten, z. B. Fensterlicht oder eine Leuchte hinter dem Bildschirm;
  kein Gegenlicht.
- **In Abschnitten aufnehmen:** Folie für Folie bzw. Kapitel für Kapitel. Versprecher werden so einfach
  herausgeschnitten, Kapitelmarken ergeben sich von selbst.
- **Zeigen statt nur sprechen:** Beim Tracen und bei Struktogrammen den Mauszeiger bzw. Laserpointer mitführen.
  Wichtige Zeilen kurz hervorheben oder hineinzoomen; DaVinci Resolve oder Shotcut genügen dafür.
- **Tempo:** etwas langsamer als im Unterricht sprechen; Denkpausen bei der Pause-Aufgabe nicht wegschneiden,
  stattdessen den Hinweis „Video anhalten“ einblenden.
- **Wiedererkennung:**
  - ein kurzes, gleiches Intro (≤ 5 s, gern ohne Musik);
  - ein Thumbnail-Muster mit Weltfarbe, Videonummer und einem großen Stichwort, z. B. „Tracetabelle“;
  - eine Playlist „Algo Quest“.
- **Untertitel:** die automatischen Untertitel von YouTube korrigieren, vor allem Fachbegriffe wie „Struktogramm“,
  „Insertionsort“, „pre-order“. Das hilft Gehörlosen, Nicht-Muttersprachlern und Schülern, die ohne Ton schauen.
- **Kapitelmarken:** Die Vorschläge stehen im Drehbuch. Die Zeiten sind geschätzt und müssen nach dem Schnitt
  angepasst werden. Die erste Marke muss bei 0:00 stehen.

## Veröffentlichung und Einbindung ins Lab

- **Erst „nicht gelistet“ hochladen:** einmal im Kurs testen, nachbessern und dann öffentlich schalten.
- **Kommentare:** moderieren oder auf „zur Prüfung zurückhalten“ stellen; das gilt besonders, solange Schüler aus
  dem eigenen Kurs kommentieren.
- **Datenschutz bei der Einbindung:** Ein eingebettetes YouTube-Video lädt schon beim Seitenaufruf Inhalte von Google.
  Für das Lab mit Schülerkonten empfehle ich deshalb:
  1. **Links statt Einbettung:** Ein Knopf „▶ Erklärvideo auf YouTube“ öffnet das Video in einem neuen Tab. Das ist
     einfach, datensparsam und mit der strengen CSP des Labs ohne Änderung möglich.
  2. **Alternativ 2-Klick-Lösung:** Erst nach einem Klick auf „Video laden“ wird `youtube-nocookie.com` eingebettet,
     mit einem Hinweis auf die Datenübertragung. Dafür muss die CSP (`frame-src`) gezielt erweitert und die
     Datenschutzerklärung ergänzt werden.
- **Wo im Lab:** Der Videolink kommt an drei Stellen, ohne Klarnamen und ohne Login-Pflicht:
  - am Kopf des passenden Levels (Merkkasten);
  - in der Themenübersicht `/themen` je Welt;
  - im Lehrkraft-Bereich unter „Materialien“.
- **Für die Einbindung brauche ich später nur je Video die YouTube-Adresse.** Die Zuordnung zu den Leveln steht in der
  Tabelle oben.
