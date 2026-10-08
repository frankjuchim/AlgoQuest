# SPEC – Algo Quest, Welt 2 „Die Rangliste“ (verbindlich für alle Teil-Agenten)

Grundlage bleibt die Spec für Welt 0/1 – ALLE Konventionen dort gelten weiter (Didaktik, XP, Notation EH 2025,
Gestaltung, Online-IDE-Besonderheiten, JUnit-Dialekt, Kommentarstil):
/tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad/SPEC_AlgoQuest_W0_W1.md
LIES SIE ZUERST VOLLSTÄNDIG.

Fertige Welt-0/1-Materialien als Stil- und Qualitätsvorbild (bitte ansehen, Layout/Generatoren wiederverwenden!):
/mnt/user-data/outputs/AlgoQuest/Welt0, Welt1, Werkzeuge, WebApp
Wiederverwendbare Generator-Skripte im Scratchpad (/tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad/):
- ab/lib.js, ab/w1_ab1.js, ab/w1_lsg1.js, ab/render.py (Struktogramm-Renderer nach EH §5), ab/images.py  → Arbeitsblätter
- pptx/aq_common.js, pptx/build_w1.js → Folien
- boss/boss_docx.js, boss/kata_docx.js, boss/lehrer_docx.js, boss/cards.py, boss/verify_kata.py, boss/lib.js → Boss, Kata, Lehrerhinweise
- code/harness, code/check_geruest.py, code/mutate.py, code/lint.py → Java-Verifikation Online-IDE-Code
Kopiere Skripte in deinen eigenen Unterordner (…/scratchpad/w2_<deinname>/) und ändere dort; Welt-0/1-Dateien NICHT verändern.

Ausgabeordner Welt 2: /mnt/user-data/outputs/AlgoQuest/Welt2/ (und Werkzeuge/ für Kata/Lehrerhinweise).

## 1. Didaktischer Ort (aus der Planung)
Welt 2 – Die Rangliste: Suchen, Sortieren, Effizienz (Wochen 4–5, 5 DS). Ziel: Standardbausteine und Sortierverfahren
von Hand beherrschen und bewerten. Spielmodul: Highscore-Liste des Dungeon-Spiels.
| DS | Inhalt | Arbeitsform | Abi-Bezug |
| 8  | Standardbausteine auf Reihungen von Objekten: Maximum/Minimum, Zählen, lineare Suche (erstes Vorkommen, −1), Duplikate, Durchschnitt | IDE L2.1; Papier-Kata | 24H-A b, 24H-B c/d, 26H-B b |
| 9  | Selection-, Insertion-, Bubblesort unplugged (Spielkarten) und auf Objekten; sortiertes Einfügen | IDE L2.2 | 25H-B e, 25N-A l |
| 10 | Effizienz: Vergleiche und Vertauschungen zählen, bester/schlechtester Fall, n(n−1)/2, Verdopplung → vierfache Vergleiche; Sortier-Duell | Sortier-Duell-Gerüst, Visualisierung | 23H-C d, 22N-C d |
| 11 | Binäre Suche iterativ: Trace lo/hi/mid, maximale Durchläufe (n = 100 → 7), Verdopplung → +1 Durchlauf; O-Notation nur als Ausblick | IDE L2.3; Papier: Trace | 24N-A d/e, 22N-B d |
| 12 | Boss 2: Trace, Analyse und Implementierung (Maximum/sortiertes Einfügen) auf Zeit; Papier-Compiler 2 | Papier | 24H-B d–g |
Effizienz wird im Abitur NIE per O-Notation geprüft, sondern über Zählen, Worst-Case-Eingaben und Verdopplung.
O-Notation höchstens als Kasten „Ausblick“.

## 2. Domäne Welt 2 – EXAKTE Klassen-API (alle Materialien identisch!)
Alle Attribute private (-), Methoden public (+), außer explizit anders angegeben. Sortierung = ABSTEIGEND nach punkte
(Platz 1 = meiste Punkte). Bei Gleichstand bleibt die Reihenfolge beliebig (Stabilität ist Thema auf AB, nicht in Tests,
außer wo angegeben).

class Eintrag
  - name: Zeichenkette; - punkte: Ganzzahl; - zeit: Ganzzahl   (Spielzeit in Sekunden)
  + c Eintrag(name: Zeichenkette, punkte: Ganzzahl, zeit: Ganzzahl)
  + getName(): Zeichenkette; + getPunkte(): Ganzzahl; + getZeit(): Ganzzahl
  + beschreibung(): Zeichenkette  → name + ": " + punkte + " Punkte (" + zeit + " s)"   z. B. "Aria: 1200 Punkte (95 s)"

class Rangliste
  - eintraege: Reihung von Eintrag; - anzahl: Ganzzahl; - vergleiche: Ganzzahl; - vertauschungen: Ganzzahl
  + c Rangliste(kapazitaet: Ganzzahl)                → leere Reihung der Länge kapazitaet, anzahl = 0, Zähler 0
  + getAnzahl(): Ganzzahl
  + getEintrag(i: Ganzzahl): Eintrag                 → null bei ungültigem Index (i < 0 oder i >= anzahl)
  + hinzufuegen(e: Eintrag): Wahrheitswert           → false, wenn e == null oder voll; sonst ans Ende, true
  + getVergleiche(): Ganzzahl; + getVertauschungen(): Ganzzahl; + zaehlerZuruecksetzen(): nichts
  - besser(a: Eintrag, b: Eintrag): Wahrheitswert    → vergleiche++; gib a.getPunkte() > b.getPunkte() zurück
                                                       (VORGEGEBEN im Gerüst; ALLE Sortier-/Einfüge-Vergleiche von
                                                       Einträgen laufen ausschließlich über besser(...))
  + vertausche(i: Ganzzahl, j: Ganzzahl): nichts     → tauscht eintraege[i] und eintraege[j], vertauschungen++
  Level 2.1 – Standardbausteine (DS 8):
  + hoechstePunktzahl(): Ganzzahl                    → −1 bei leerer Liste
  + besterEintrag(): Eintrag                         → null bei leerer Liste; bei Gleichstand der erste
  + anzahlUeber(grenze: Ganzzahl): Ganzzahl          → Anzahl mit punkte > grenze
  + indexVon(name: Zeichenkette): Ganzzahl           → erstes Vorkommen (equals!), sonst −1
  + durchschnitt(): Kommazahl                        → 0.0 bei leerer Liste (Kommazahl-Division!)
  + hatDoppelteNamen(): Wahrheitswert                → true, wenn ein Name mindestens zweimal vorkommt
  Level 2.2 – Sortieren (DS 9):
  + istSortiert(): Wahrheitswert                     → absteigend (gleiche Nachbarn erlaubt); leere/1-elementige Liste → true
                                                       (vergleicht direkt über getPunkte, NICHT über besser → zählt nicht)
  + selectionSort(): nichts                          → Maximum-Auswahl: genau n(n−1)/2 Aufrufe von besser bei n Einträgen;
                                                       vertausche nur, wenn Maximum-Index ≠ i
  + insertionSort(): nichts                          → Einfügen von links nach rechts mit vertausche benachbarter Elemente;
                                                       bei bereits sortierter Liste genau n−1 Vergleiche und 0 Vertauschungen;
                                                       stabil
  + bubbleSort(): nichts                             → mit Abbruch, wenn ein Durchlauf ohne Vertauschung blieb;
                                                       bei sortierter Liste genau n−1 Vergleiche
  + einfuegenSortiert(e: Eintrag): Wahrheitswert     → setzt voraus, dass die Liste absteigend sortiert ist; false bei null/voll;
                                                       schiebt schlechtere Einträge nach rechts (ohne vertausche) und fügt e
                                                       so ein, dass die Liste sortiert bleibt; e wird HINTER gleich gute
                                                       Einträge gesetzt (stabil); Vergleiche über besser
Static-Klasse Suche (Level 2.3, DS 11) – auf Reihungen von Ganzzahlen, AUFSTEIGEND sortiert:
  + static durchlaeufe: Ganzzahl (öffentlich lesbar, wird von jeder Suche zu Beginn auf 0 gesetzt)
  + static linear(r: Reihung von Ganzzahl, x: Ganzzahl): Ganzzahl  → erster Index oder −1; durchlaeufe = Zahl geprüfter Elemente
  + static binaer(r: Reihung von Ganzzahl, x: Ganzzahl): Ganzzahl  → iterativ mit lo, hi, mid = (lo + hi) / 2; Index eines
        Vorkommens oder −1; durchlaeufe = Zahl der Schleifendurchläufe (höchstens ⌊log2 n⌋ + 1; n = 100 → höchstens 7)
  + static einfuegeposition(r: Reihung von Ganzzahl, x: Ganzzahl): Ganzzahl → Experte: kleinster Index i mit r[i] >= x
        (r.length, wenn x größer als alle), per binärer Suche
  Leere Reihung: linear/binaer → −1, einfuegeposition → 0.

Level-Einteilung (eine Gerüstdatei, getrennte Testklassen, Testmethoden-Präfixe basis_/erweiterung_/experte_):
  L21StandardTest (DS 8) · L22SortierTest (DS 9, prüft Sortierergebnis UND exakte Vergleichszahlen wie oben) · L23SucheTest (DS 11)
  Basis/Erweiterung/Experte = 10/20/30 XP.

## 3. Sortier-Duell (DS 10) – Wettbewerbs-Gerüst
Datei Welt2/AQ_W2_SortierDuell_Geruest.txt (+ _LSG.txt), aufbauend auf dem Visualisierungs-Gerüst des Lehrers
(Projekt-Doc "09_Sortiervisualisierung_Geruest.txt", Projects-Tool project_read). Korrigiere dessen bekannten Fehler
(Kopfkommentar nennt Vis.tausche, Methode heißt vertausche → einheitlich `vertausche`).
- Balken-Visualisierung (World/Rectangle/Text, SystemTools.setSpeed) wie im Original.
- Befehle für Schüler: Vis.laenge(), Vis.kleiner(i, j) (zählt Vergleich), Vis.vertausche(i, j) (zählt Vertauschung).
  Im Duell-Modus KEIN Vis.wert(i) (sonst Schummeln) – stattdessen liefert wert(i) im Duell -1 oder ist nicht verfügbar; erkläre die Regel.
- Faire, reproduzierbare Datensätze ohne Math.random: eigener Pseudozufallsgenerator (LCG mit festem Startwert) in Vis.
  Vier Duell-Runden je n = 40: "zufall" (Seed 2027), "fast sortiert" (sortiert, dann 4 feste Vertauschungen),
  "umgekehrt", "viele gleiche" (Werte nur aus {100, 200, …, 500}).
- Duell.starten(): führt MeinSortierer.duellSort() auf allen vier Runden aus, prüft jeweils auf korrekte Sortierung (aufsteigend),
  summiert Vergleiche (Hauptwertung) und Vertauschungen (Tiebreak), gibt eine Ergebniszeile aus:
  "DUELL-ERGEBNIS: Vergleiche = …, Vertauschungen = …, gueltig = ja/nein" – diese Zahl trägt die Lehrkraft in der WebApp ein.
- MeinSortierer enthält Vorlagen bubbleSort (fertig), selectionSort/insertionSort (TODO) und duellSort (frei; Standard: ruft insertionSort).
- LSG: Musterlösungen + ein deutlich besseres duellSort (z. B. Insertionsort mit binärer Suche der Einfügestelle – aber Achtung:
  Verschieben nur über vertausche – oder Mergesort-artig über vertausche; entscheide, was mit nur kleiner/vertausche geht) +
  Tabelle der Referenzwerte (Vergleiche je Runde für Bubble/Selection/Insertion/LSG-Duell), damit die Lehrkraft Ergebnisse einordnen kann.

## 4. Boss 2 (DS 12) – NEUER Kontext (Transfer!)
„Das Turnier der Bogenschützen“ (oder ähnlich, nicht Highscore): Klasse Schuetze (name, ringe, …) in einer Reihung/Klasse Turnier.
≈ 24 BE, 60 min, AFB ≈ 30/53/17 %. Teilaufgaben-Typen: Tracetabelle eines gegebenen Sortierverfahrens (z. B. Insertionsort,
Zustand nach jedem äußeren Durchlauf), Verfahren identifizieren und Funktionsweise erläutern, Vergleiche zählen + Worst-Case-Eingabe
angeben + Verdopplung abschätzen, Methode implementieren (z. B. sortiert einfügen oder Maximum mit Bedingung) mit Leer-/null-Abfragen,
binäre Suche: Trace lo/hi/mid + maximale Durchläufe begründen, Fehler in Struktogramm/Code finden.

## 5. Kata-Karten Welt 2
Datei Werkzeuge/kata_w2.json, Schema exakt wie Spec W0/W1 §5 (gleiche Felder, gleiche Kategorien-Strings), ids "W2-01" … ,
"welt": 2, 12–14 Karten: Tracetabelle (Selection/Insertion/Bubble, binäre Suche lo/hi/mid), Struktogramm lesen, Code ↔ Struktogramm,
Fehler im Java-Code (Off-by-one in Schleifengrenze, max mit 0 initialisiert, == bei Zeichenketten, fehlende Leerabfrage),
Fehler im Struktogramm, Lückencode (Insertionsort-Innenschleife), Methode implementieren (anzahlUeber, indexVon, sortiert einfügen),
Verändern und Erweitern (aufsteigend statt absteigend, zusätzlich Vertauschungen zählen), Funktionsweise erläutern
(Verfahren erkennen, Vergleiche zählen, Verdopplung).
Außerdem Werkzeuge/AQ_Kata-Karten_W2.docx (druckbar wie W0/W1).

## 6. WebApp-Erweiterung (v1.1)
- Neues Modul „Wettbewerbe“ (für Sortier-Duell, später Dungeon-Rennen): Lehrkraft legt Wettbewerb je Kurs an (Name, Einheit z. B.
  „Vergleiche“, Wertungsrichtung „weniger ist besser“/„mehr ist besser“, aktiv/abgeschlossen), trägt Ergebnisse je GILDE ein
  (Wert, optional Tiebreak-Wert, gültig ja/nein, Kommentar). Board zeigt aktive Wettbewerbe als Rangliste der Gilden.
  Optional Button: „Sieger: Badge Speedrunner an Gildenmitglieder vergeben“ bzw. XP-Bonus buchen (über bestehende Funktionen).
- Seed: Karten aus seed/kata_w0_w1.json UND seed/kata_w2.json (alle seed/*.json beim Start importieren, idempotent nach id);
  bestehende Datenbanken bekommen neue Karten beim nächsten Start (upsert), ohne Lernstände zu verlieren.
- Kata-Trainer: Welt-Filter enthält Welt 2.
- Tests erweitern, alle grün; Docker-Build prüfen.

## 7. Dateinamen Welt 2 (verbindlich)
Welt2/AQ_W2_Rangliste.pptx
Welt2/AQ_W2_AB1_Standardbausteine_und_Suchen.docx (+ Welt2/AQ_W2_AB1_LSG.docx)        → DS 8 (L2.1)
Welt2/AQ_W2_AB2_Sortieren.docx (+ Welt2/AQ_W2_AB2_LSG.docx)                           → DS 9 (L2.2)
Welt2/AQ_W2_AB3_Effizienz_und_binaere_Suche.docx (+ Welt2/AQ_W2_AB3_LSG.docx)         → DS 10–11 (Sortier-Duell, L2.3)
Welt2/AQ_W2_L2_Rangliste_Geruest.txt · Welt2/AQ_W2_L2_Rangliste_LSG.txt
Welt2/AQ_W2_SortierDuell_Geruest.txt · Welt2/AQ_W2_SortierDuell_LSG.txt
Welt2/AQ_W2_Boss2_Turnier.docx · Welt2/AQ_W2_Boss2_Erwartungshorizont.docx
Werkzeuge/kata_w2.json · Werkzeuge/AQ_Kata-Karten_W2.docx · Werkzeuge/AQ_W2_Lehrerhinweise.docx (DS 8–12)
WebApp/ (aktualisiert)
