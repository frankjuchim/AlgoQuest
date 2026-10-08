# SPEC – Algo Quest, Welt 0 „Die Akademie“ (Basics + eigene Methoden) + Umnummerierung

Grundkonventionen: /tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad/SPEC_AlgoQuest_W0_W1.md
(LIES ZUERST VOLLSTÄNDIG – Didaktik, XP, EH-2025-Notation, Gestaltung, Online-IDE/JUnit-Dialekt, Kommentarstil).
Ergänzend: …/scratchpad/SPEC_AlgoQuest_W2.md (Welt 2, gleiche Arbeitsweise).
Fertige Materialien als Vorbild: /mnt/user-data/outputs/AlgoQuest/Welt0, Welt1, Welt2, Werkzeuge, WebApp.
Generator-Skripte (wiederverwenden, in eigenen Unterordner kopieren!): …/scratchpad/ab, w2_ab (ABs, render.py = Struktogramm-
Renderer), pptx, w2_pptx (Folien, aq_common.js), boss, w2_boss (Boss/Kata/Lehrerhinweise), code, w2_code (Java-Harness,
Mutationstests). Welt-1/2-Dateien NUR verändern, wenn dein Auftrag die Umnummerierung ausdrücklich enthält.

## 1. Neue Struktur (gilt ab jetzt, Planung aktualisiert)
Die Einheit hat 40 DS (36 Kern + 4 Kür) in 14 Wochen, meist 3 DS/Woche. Welt 0 wurde von 2 auf 7 DS erweitert und heißt jetzt
„Die Akademie“ (Kick-off, Basics, eigene Methoden). Begründung: Im Abitur ist jede Implementierung eine Methode mit vorgegebener
Signatur (in allen 22 Abi-Aufgaben 2022–2026 wurde implementiert). Eigene Methoden brauchen viel Raum.
Story: Bevor das Studio Helden schmieden darf, durchläuft es die Akademie der Baumeister: Werkstatt (Basics), Vorratskammer
(Reihungen), Zauberschule (eigene Methoden = Zauberformeln: Name, Zutaten = Parameter, Wirkung = Rückgabe), Aufnahmeprüfung (Boss 0).

| DS | Wo. | Inhalt | Material |
| 1 | 1 | Kick-off: Gilden, XP-System, echte Block-1-Aufgabe; Online-IDE, erster JUnit-Test; Level 0 Diagnose | Kickoff.pptx, AB Portal Teil A, L0 Diagnose (vorhanden) |
| 2 | 1 | Basics: Datentypen (int, double, boolean, char, String), Variablen, Zuweisung, Operatoren (/ und % bei Ganzzahlen, Casting, Vergleich, logische Operatoren), Zufallszahlen im Bereich + ganzzahliges Runden (EH §2), Verzweigung (if/else, else-if), Schleifen (while, for, do-while kurz); Tracetabelle; Struktogramm nach §5 | NEU AB2 Werkstatt; AB Portal Teil B (vorhanden) als Notations-Referenz; Level L0.2 |
| 3 | 1 | Reihungen 1D: anlegen (new int[n], Literal), Zugriff, length, for und for-each, ArrayIndexOutOfBounds, Kopie vs. Referenz (int[] b = a), neue Reihung zurückgeben; erlaubte Zeichenketten-Operationen (EH §1) | NEU AB3 Vorratskammer; Level L0.3 |
| 4 | 2 | Eigene Methoden I: Anatomie einer Methode; Signatur in Abi-Notation ↔ Java-Kopf (Typnamen-Übersetzung, „nichts“ = void); Parameter vs. Argumente; return beendet; jede Verzweigung braucht return; void-Methoden; Aufruf und Rückgabewert verwenden; lokale Variablen, Gültigkeit; Methode ruft Methode; Methodenaufruf tracen (Aufrufprotokoll) | NEU AB4 Zauberschule Teil 1; Level L0.4 |
| 5 | 2 | Eigene Methoden II: Reihungen als Parameter und Rückgabe; Wertübergabe (int-Parameter ändern wirkt nicht nach außen) vs. Referenz (Reihungsinhalt ändern wirkt nach außen); neue Reihung vs. in-place; Hilfsmethoden und Zerlegung (Methode nutzt eigene Methode); Standardbausteine als Methoden | NEU AB4 Zauberschule Teil 2; Level L0.5 |
| 6 | 2 | Methoden-Werkstatt (Papier dominant): Rezept Aufgabentext → Signatur → Randfälle → Struktogramm → Java auf Papier → Abi-Check → Papier-Compiler; Fehlergalerie (fehlender Rückgabepfad, Off-by-one, = statt ==, ganzzahlige Division, Parameter überschrieben, Rückgabe in der Schleife zu früh, Reihung verändert statt Kopie); Abi-Format „Implementieren Sie die Methode …“ mit BE | NEU AB5 Methoden-Werkstatt; Papier-Compiler 0 |
| 7 | 3 | Boss 0 „Aufnahmeprüfung der Akademie“ | NEU Boss 0 + EH |
Welt 1 = DS 8–12, Welt 2 = DS 13–17, Welt 3 = DS 18–23, Welt 4 = DS 24–30, Welt 5 = DS 31–36, Welt 6 = DS 37–40.
Woche je DS: W1 1–3 · W2 4–6 · W3 7–9 · W4 10–12 · W5 13–15 · W6 16–18 · W7 19–21 · W8 22–24 · W9 25–27 · W10 28–30 ·
W11 31–33 · W12 34–36 · W13 37–38 · W14 39–40. Kür-DS: 20, 25, 29, 33. Quest-Map (Wochenbalken): Welt 0 W1–W3 (bis 2,33),
Welt 1 2,33–4, Welt 2 4–5,67, Welt 3 5,67–7,67, Welt 4 7,67–10, Welt 5 10–12, Welt 6 12–14; Bosse 0–5 + Klausur.
Umnummerierung alt → neu: Welt-1-DS 3,4,5,6,7 → 8,9,10,11,12; Welt-2-DS 8,9,10,11,12 → 13,14,15,16,17.

## 2. Online-IDE Akademie – EXAKTE API (static-Methoden, alle Materialien identisch!)
Eine Gerüst-/LSG-Datei: Welt0/AQ_W0_Akademie_Geruest.txt und Welt0/AQ_W0_Akademie_LSG.txt.
Testklassen L02WerkstattTest, L03VorratTest, L04ZauberTest, L05ZauberIITest; Präfixe basis_/erweiterung_/experte_; 10/20/30 XP.
Nur sichere Sprachmittel (keine Generics, Collections, Lambdas, String.format, Math.round/Math.floor/Math.ceil NICHT verwenden
– Runden/Aufrunden sollen die Schüler selbst mit Casting, / und % lösen; Math.random() erlaubt; erlaubte String-Operationen).

class Werkstatt (L0.2, DS 2)
  Basis:       istGerade(n: Ganzzahl): Wahrheitswert
               restGold(gold: Ganzzahl, preis: Ganzzahl): Ganzzahl        → Gold, das übrig bleibt, wenn man so viele Tränke zum
                                                                            Preis preis kauft wie möglich (preis > 0)  [gold % preis]
               kistenBenoetigt(anzahl: Ganzzahl, proKiste: Ganzzahl): Ganzzahl → Aufrunden ohne Math: (anzahl + proKiste − 1) / proKiste
                                                                            oder mit %; anzahl >= 0, proKiste > 0
  Erweiterung: schadensstufe(schaden: Ganzzahl): Zeichenkette            → "kein" (<= 0), "leicht" (1–9), "mittel" (10–29), "schwer" (>= 30)
               durchschnitt(a: Ganzzahl, b: Ganzzahl, c: Ganzzahl): Kommazahl → exakte Kommazahl (Falle: ganzzahlige Division)
               quersumme(n: Ganzzahl): Ganzzahl                           → n >= 0, Schleife mit % 10 und / 10; quersumme(0) = 0
  Experte:     potenz(basis: Ganzzahl, exponent: Ganzzahl): Ganzzahl       → exponent >= 0, Schleife, potenz(x, 0) = 1
               ggT(a: Ganzzahl, b: Ganzzahl): Ganzzahl                    → a, b > 0, euklidischer Algorithmus (Schleife)
               istPrimzahl(n: Ganzzahl): Wahrheitswert                    → n < 2 → false

class Vorrat (L0.3, DS 3)
  Basis:       anzahlLeer(r: Reihung von Ganzzahl): Ganzzahl              → Anzahl der Fächer mit Wert 0
               letzterWert(r): Ganzzahl                                   → letztes Element, −1 bei leerer Reihung
               enthaelt(r, x: Ganzzahl): Wahrheitswert
  Erweiterung: umgedreht(r): Reihung von Ganzzahl                         → NEUE Reihung in umgekehrter Reihenfolge, r bleibt unverändert
               verdopple(r): nichts                                       → verdoppelt jeden Wert IN r (in-place)
               anzahlAnstiege(r): Ganzzahl                                → Anzahl i mit r[i] > r[i−1]
  Experte:     zaehleZeichen(s: Zeichenkette, c: Zeichen): Ganzzahl
               ohneVokale(s: Zeichenkette): Zeichenkette                  → entfernt a,e,i,o,u (groß/klein) – nur charAt, length, +
               beginntMit(s: Zeichenkette, anfang: Zeichenkette): Wahrheitswert
                                                                            → nur length/charAt bzw. substring + equals; anfang länger als s → false

class Zauber (L0.4, DS 4)
  Basis:       heilwert(stufe: Ganzzahl): Ganzzahl                        → stufe * 15
               istStaerker(a: Ganzzahl, b: Ganzzahl): Wahrheitswert       → a > b
               spruchtext(name: Zeichenkette, stufe: Ganzzahl): Zeichenkette → name + " (Stufe " + stufe + ")"   z. B. "Feuerball (Stufe 3)"
  Erweiterung: manaKosten(stufe: Ganzzahl, verstaerkt: Wahrheitswert): Ganzzahl → 10 * stufe, verstärkt doppelt
               kannZaubern(mana: Ganzzahl, stufe: Ganzzahl, verstaerkt: Wahrheitswert): Wahrheitswert → mana >= manaKosten(...) (MUSS manaKosten nutzen)
               max3(a: Ganzzahl, b: Ganzzahl, c: Ganzzahl): Ganzzahl       → mit Hilfsmethode max2(a, b) (max2 ebenfalls public static, vorgegeben oder Basis)
  Experte:     runden(wert: Kommazahl): Ganzzahl                         → kaufmännisch für wert >= 0 per Casting: (int)(wert + 0.5)
               wuerfelImBereich(von: Ganzzahl, bis: Ganzzahl): Ganzzahl    → gleichverteilte Zufallszahl von..bis (inkl.), von <= bis
               zauberkette(stufe: Ganzzahl): Zeichenkette                  → "1-2-…-stufe", stufe <= 0 → "" (z. B. 3 → "1-2-3")

class ZauberII (L0.5, DS 5) – Reihungen als Parameter/Rückgabe, Wert vs. Referenz, Hilfsmethoden
  Basis:       fuelle(r: Reihung von Ganzzahl, wert: Ganzzahl): nichts    → setzt jedes Element auf wert (wirkt nach außen!)
               erhoeheAlle(r, bonus: Ganzzahl): nichts                    → in-place
               erhoehteKopie(r, bonus: Ganzzahl): Reihung von Ganzzahl     → NEUE Reihung, r unverändert (Test prüft beides)
  Erweiterung: istImBereich(x: Ganzzahl, von: Ganzzahl, bis: Ganzzahl): Wahrheitswert → von <= x <= bis
               zaehleImBereich(r, von, bis): Ganzzahl                     → nutzt istImBereich
               indexDesMinimums(r): Ganzzahl                              → −1 bei leerer Reihung, erstes Minimum
               tauscheErstesUndLetztes(r): nichts                         → bei Länge < 2 nichts tun
  Experte:     zweitgroesster(r): Ganzzahl                                → zweitgrößter WERT unter verschiedenen Werten; existiert keiner
                                                                            (Länge < 2 oder alle gleich) → −1
               verschmelze(a: Reihung von Ganzzahl, b: Reihung von Ganzzahl): Reihung von Ganzzahl → a, b aufsteigend sortiert →
                                                                            neue aufsteigend sortierte Reihung aller Werte (Vorbereitung Mergesort)
Zusätzlich Papier-Compiler 0 (DS 6): Testklasse PapierCompiler0Test für eine Methode, die auf dem AB5 handschriftlich entsteht:
  anzahlUeberDurchschnitt(r: Reihung von Ganzzahl): Ganzzahl → Anzahl der Werte, die echt größer als
  der Durchschnitt (Kommazahl) sind; leere Reihung → 0. Gehört in class Werkstattpruefung (eigene Klasse, Gerüst leer mit TODO).

## 3. Boss 0 (DS 7) – NEUER Kontext „Die Bibliothek der Akademie“
Ausleihzahlen der Zauberbücher als Reihung von Ganzzahlen (+ evtl. Reihung von Zeichenketten für Titel). ≈ 24 BE, 60 min,
AFB ≈ 30/53/17 %. Teilaufgaben-Typen: (a) Signaturen Abi-Notation ↔ Java-Methodenkopf übersetzen und Bestandteile benennen;
(b) Tracetabelle eines Methodenaufrufs mit Hilfsmethode (Aufrufprotokoll); (c) Wert- vs. Referenzübergabe: Ausgabe vorhersagen
und begründen; (d) Struktogramm nach §5 für eine Methode auf einer Reihung entwickeln; (e) Methode implementieren (mit Randfall
leere Reihung; Papier-Compiler, Testklasse im EH-Anhang); (f) Fehler in einer Methode finden (fehlender Rückgabepfad oder
ganzzahlige Division oder Off-by-one) und korrigieren.

## 4. Kata-Karten Akademie
Werkzeuge/kata_w0_akademie.json, Schema wie kata_w0_w1.json, "welt": 0, ids "W0-09" … "W0-22" (14 Karten; die vorhandenen
W0-01…W0-08 bleiben). Kategorien wie bisher PLUS neue Kategorie exakt "Methodenkopf und Signatur" (Abi-Signatur ↔ Java-Kopf,
Parameter/Rückgabetyp bestimmen, Aufruf mit passenden Argumenten). Themen: Datentypen/Casting/ganzzahlige Division, % und /,
Verzweigung, Schleifen-Trace, Reihungen (Index, length, for-each, Referenz-Kopie), Zeichenketten erlaubt/verboten, Methodenkopf,
Wert vs. Referenz, Hilfsmethode, fehlender Rückgabepfad, Methode implementieren. Plus Werkzeuge/AQ_Kata-Karten_W0_Akademie.docx.

## 5. Dateinamen (neu)
Welt0/AQ_W0_Akademie.pptx (Input-Folien DS 2–7)
Welt0/AQ_W0_AB2_Werkstatt_Basics.docx + Welt0/AQ_W0_AB2_LSG.docx                       (DS 2, L0.2)
Welt0/AQ_W0_AB3_Vorratskammer_Reihungen.docx + Welt0/AQ_W0_AB3_LSG.docx                 (DS 3, L0.3)
Welt0/AQ_W0_AB4_Zauberschule_Methoden.docx + Welt0/AQ_W0_AB4_LSG.docx                   (DS 4–5, L0.4 + L0.5)
Welt0/AQ_W0_AB5_Methoden-Werkstatt.docx + Welt0/AQ_W0_AB5_LSG.docx                      (DS 6, Papier-Compiler 0)
Welt0/AQ_W0_Akademie_Geruest.txt + Welt0/AQ_W0_Akademie_LSG.txt
Welt0/AQ_W0_Boss0_Bibliothek.docx + Welt0/AQ_W0_Boss0_Erwartungshorizont.docx
Werkzeuge/kata_w0_akademie.json + Werkzeuge/AQ_Kata-Karten_W0_Akademie.docx
Lehrerhinweise neu aufgeteilt (ersetzen AQ_W0-W1_Lehrerhinweise.docx):
  Werkzeuge/AQ_W0_Lehrerhinweise.docx (DS 1–7), Werkzeuge/AQ_W1_Lehrerhinweise.docx (DS 8–12),
  Werkzeuge/AQ_W2_Lehrerhinweise.docx (umnummeriert auf DS 13–17)
Das vorhandene AB „Portal“ (AQ_W0_AB_Portal.docx) bleibt AB 1 (DS 1, Teil B dient in DS 2 als Notations-Referenz).
