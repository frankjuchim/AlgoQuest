# SPEC – „Algo Quest Lab“ (WebApp v2.0) – interaktive Übungsplattform

Ersetzt die bisherige XP-/Gilden-WebApp (v1.x) vollständig. Vorbild: automatenlab.frankjuchim.de (Weltkarte mit Leveln,
Module mit automatisch geprüften Übungen, Abzeichen) – aber MIT serverseitigem Fortschritt, Kurs-Scoreboard und Lehrkraft-Bereich.
SCRATCH = /tmp/claude-0/-home-claude/3cd22a81-f637-5ed7-b623-6c1c326592db/scratchpad
Bisherige App (Code-Basis zum Wiederverwenden: security.js, Express-/Helmet-Setup, Dockerfile, Kata-Leitner, Tests):
/mnt/user-data/outputs/AlgoQuest/WebApp (v1.6). Neue App entsteht in SCRATCH/algolab/app und wird am Ende nach
/mnt/user-data/outputs/AlgoQuest/WebApp kopiert (alte Dateien ersetzen; docs/ neu).
Inhalte der Einheit (Konventionen, NI-API, Welten): SCRATCH/SPEC_AlgoQuest_W0_W1.md, …_W0_Akademie.md, …_W2 … _W6.md.

## 1. Grundentscheidungen (vom Auftraggeber festgelegt)
- KEINE Gilden, KEINE manuelle XP-Buchung, KEINE Wettbewerbe. Punkte entstehen nur automatisch durch gelöste Aufgaben/Bosse.
- Schüler melden sich SELBST an: Kurscode + Name → erhalten persönlichen Code (Format `ABC-123`, Alphabet ohne 0/O/1/I).
  Wiederanmeldung auf jedem Gerät mit Kurscode + Name + Code. Name je Kurs eindeutig (case-insensitiv, getrimmt, 2–30 Zeichen,
  Buchstaben/Ziffern/Leerzeichen/.-'). Empfehlung im UI: „Vorname + Initial (z. B. Lena S.)“.
- Scoreboard mit Namen (kursintern in der App; Beamer-Ansicht /board/<KURSCODE> nur wenn im Kurs aktiviert; noindex).
- Lehrkräfte: Registrierung auf Anfrage (Name, E-Mail, Schule, Passwort, Nachricht) → Status „wartet“ → Superadmin bestätigt/lehnt ab.
  Superadmin = Konto aus Umgebungsvariablen ADMIN_EMAIL (Standard „admin“) + ADMIN_PASSWORD (wird beim Start angelegt/aktualisiert).
  Lehrkräfte sehen nur EIGENE Kurse; Superadmin sieht alles. Passwörter mit crypto.scrypt (Salt, Parameter dokumentiert).
  Keine E-Mail-Versand-Funktion: Passwort-Reset = Superadmin setzt Einmal-Passwort, Lehrkraft muss es beim Login ändern.
- Kurs-Verwaltung (Lehrkraft): Kurs anlegen (Name → Kurscode 6 Zeichen), Beitritts-Link + QR-Code (serverseitig als SVG, npm `qrcode`),
  Schülerliste (Name, Code anzeigen, Punkte, gelöste Aufgaben, zuletzt aktiv): Name ändern, Code neu erzeugen, Schüler löschen,
  ALLE Schüler des Kurses löschen (Bestätigung durch Eintippen des Kursnamens), Kurs löschen.
  Einstellungen: Welten freigeschaltet (Standard alle), Bosse: „automatisch“ (ab 60 % der Weltpunkte) / „gesperrt“ / „offen“,
  Scoreboard für Schüler sichtbar ja/nein, Beamer-Board aktiv ja/nein, Anmeldung neuer Schüler offen ja/nein.
  Auswertung: Fortschrittsmatrix Schüler × Level (% Punkte), Boss-Ergebnisse, Aufgabenstatistik (Lösungsquote, Ø Fehlversuche,
  häufig gewählte falsche Antworten optional), „Fallen-Profil“ des Kurses (P1–P10 aus SPEC_AlgoQuest_W6.md §2), CSV-Export.
- Online-IDE bleibt extern: Level-Seiten zeigen eine Karte „Programmieren in der Online-IDE“ mit Dateiname/Level aus den ABs
  (reine Info + „erledigt“-Häkchen für den eigenen Überblick, 0 Punkte).
- Upgrade von v1.x: Erkennt die App eine alte Datenbank (meta.schema_version ≤ 2 bzw. Tabelle guilds), wird sie nach
  `algoquest.v1-backup-<datum>.db` umbenannt und neu angelegt (Log-Hinweis). Keine Datenübernahme.
- Datenschutz: nur Name + Code + Lernstand; Datenschutzhinweis-Seite (Vorlage, von Schule anzupassen); Löschfunktionen;
  keine externen Ressourcen/CDNs, keine Tracking-Cookies, Session-Cookie httpOnly/SameSite=Lax/secure hinter HTTPS.

## 2. Schüler-Oberfläche (Vanilla-JS-SPA oder Mehrseiten, kein Build-Schritt; tablet-/iPad-tauglich, Touch, ≥ 44 px Ziele)
- Start: Kurs beitreten (Kurscode + Name) | Weiterspielen (Kurscode + Name + Code). Nach Beitritt großer Hinweis „Notiere deinen Code“.
- Weltkarte: Welten 0–6 (0 Akademie, 1 Heldenschmiede, 2 Rangliste, 3 Labyrinth, 4 Hafen, 5 Wald, 6 Endgegner) mit Leveln
  (Fortschrittsring je Level), Boss-Knoten je Welt, gesperrte Welten ausgegraut.
- Level-Seite: Intro (kurzer Merkkasten), Liste der Aufgaben (Status ungelöst/gelöst/Lösung angesehen, Punkte), IDE-Karte, AB-Verweis.
- Aufgaben-Ansicht: Inhalt (Blöcke §4), Interaktion, Knöpfe „Prüfen“, „Tipp“ (falls vorhanden), „Lösung zeigen“ (Bestätigung:
  „danach 0 Punkte“), Feedback je Feld/Schritt, nach Lösen/Aufdecken: Erklärung. „Nächste Aufgabe“.
- Trainingsplatz (je Welt, falls Generatoren vorhanden): Zufallsaufgaben aus Generatoren §6, 1 Punkt je gelöster, max. 30 Punkte/Tag.
- Boss-Kampf je Welt (§5). Kata-Trainer (Leitner, aus v1 übernehmen, ohne Punkte, alle Karten seed/kata/*.json).
- Mein Profil: Punkte, Rang (Novize/Lehrling/Geselle/Meister/Großmeister bei 0/10/30/55/80 % der erreichbaren Level-Punkte aller
  freigeschalteten Welten), Abzeichen (§7), Fortschritt je Welt, „Deine Fallen“ (Fehlversuche je P-Kategorie, aus `fallen` der Aufgaben),
  Code anzeigen.
- Scoreboard (falls aktiviert): Rang, Name, Punkte, Abzeichen-Anzahl; Filter gesamt / je Welt; eigener Eintrag hervorgehoben.
- Beamer-Board /board/<KURSCODE>: Top 15 + Weltfortschritt des Kurses (Balken) + letzte 8 Erfolge („Lena S. hat den Hafen-Boss
  besiegt“); Auto-Reload 60 s; nur wenn aktiviert.
- Gestaltung: Algo-Quest-Farben #1F4E79 (primär), Gold #B8860B, Grün #548235, Rot #C00000, Kästen #DBE7F5; Weltfarben je Welt;
  Monospace-Code mit Zeilennummern; Struktogramme nach EH §5 als HTML/CSS (Kasten-Notation, Verzweigung mit Dreieckskopf
  „wahr/falsch“, Schleifen kopfgesteuert/fußgesteuert, „gib … zurück“); hell, gut lesbar, Druck nicht nötig.

## 3. Aufgaben-Datei (Seed) – VERBINDLICHES FORMAT
Datei je Welt: `seed/welten/welt<N>.json` (UTF-8). Bei jedem Start Upsert nach id (Lernstände bleiben).
```json
{
  "version": 2, "welt": 4, "titel": "Der Hafen", "farbe": "#2E75B6",
  "levels": [
    { "id": "W4-L1", "nr": "4.1", "titel": "Stapel", "ds": [24], "ab": "AB 1 Stapel und Schlange, Teil A",
      "ide": "AQ_W4_L4_Hafen_Geruest.txt – Level 4.1 (Klasse Stapelei)", "intro": [ /* Blöcke */ ],
      "aufgaben": ["W4-L1-01", "W4-L1-02"] }
  ],
  "boss": { "id": "W4-BOSS", "titel": "Die Fähre im Nebelhafen", "dauerMin": 25, "anzahl": 8,
            "mix": { "1": 3, "2": 3, "3": 2 }, "pool": ["W4-B-01", "…"] },
  "aufgaben": [ /* Aufgaben, siehe unten */ ]
}
```
Aufgabe:
```json
{ "id": "W4-L1-01", "titel": "Was liegt oben?", "stufe": 1, "punkte": 10,
  "kategorie": "ADT-Befehlsfolgen", "fallen": ["P1"],
  "inhalt": [ /* Blöcke §4 – dürfen Lücken [[id]] enthalten */ ],
  "interaktion": { "kind": "gaps", "felder": { "g1": { "typ": "zahl" } } },
  "loesung": { "g1": ["7"] },
  "tipps": ["Der Stapel arbeitet nach dem LIFO-Prinzip."],
  "erklaerung": [ /* Blöcke */ ] }
```
- `id`: `W<n>-L<k>-<nn>` (Level) bzw. `W<n>-B-<nn>` (Boss-Pool); eindeutig. stufe 1/2/3 → punkte Standard 10/20/30.
- `kategorie`: genau ein Wert aus LAB_KATEGORIEN = [„Datentypen und Ausdrücke“, „Methodenkopf und Signatur“, „Klasse vs. Objekt“,
  „Bestandteile einer Klasse“, „Objektkarten und Referenzen“, „Klassendiagramm“, „Struktogramm lesen“, „Code ↔ Struktogramm“,
  „Tracetabelle“, „Rekursionstabelle“, „Fehler im Java-Code“, „Fehler im Struktogramm“, „Lückencode“, „Methode implementieren“,
  „ADT-Befehlsfolgen“, „Sortieren und Suchen“, „Effizienz“, „Bäume“, „Funktionsweise erläutern“] (genau diese Schreibweise).
  `fallen`: Teilmenge von P1–P10 (darf leer sein).
- `interaktion` darf auch ein ARRAY von Interaktionen sein (mehrteilige Aufgabe); dann ist `loesung` ein Array gleicher Länge.
  Gelöst = alle Teile richtig.
- Alle Java-Codes in Aufgaben: gültiges Online-IDE-Java mit NI-Bibliothek (nicht generisch, Casts), per javac + NI-Stub geprüft;
  Struktogramme nach EH §5; Rekursionstiefe Erstaufruf = 0; Höhe leerer Baum 0 / Blatt 1; Konventionen der Welt-Specs.

## 4. Inhaltsblöcke (Anzeige) – `{ "t": … }`
- `text`: `{ "t":"text", "md":"…" }` Mini-Markdown: **fett**, *kursiv*, `code`, Absätze (Leerzeile), Listen („- “), Lücken [[g1]].
- `code`: `{ "t":"code", "code":"…", "nummern":true, "markiere":[3] }` (Java, Lücken [[g1]] im Code erlaubt).
- `struktogramm`: `{ "t":"struktogramm", "kopf":"summe(r: Reihung von Ganzzahl): Ganzzahl", "rumpf":[ Knoten… ] }`
  Knoten: `{"anw":"s ← 0"}` · `{"wenn":"x > 0","dann":[…],"sonst":[…]}` · `{"solange":"i < n","rumpf":[…]}` ·
  `{"zaehle":"i von 0 bis n − 1","rumpf":[…]}` · `{"wiederhole":[…],"bis":"x = 0"}` · `{"gib":"s"}` (rendert „gib s zurück“) ·
  `{"aufruf":"tausche(r, i, j)"}`. Texte dürfen Lücken [[g1]] enthalten.
- `tabelle`: `{ "t":"tabelle", "kopf":["i","s"], "zeilen":[["0","[[c1]]"],["1","[[c2]]"]] }` (Trace-/Rekursions-/Verarbeitungstabellen).
- `baum`: `{ "t":"baum", "baum":"8(3(1,6(4,7)),10(-,14(13,-)))" }` Klammerformat: `wert(links,rechts)`, leer `-`, Blatt `x`
  (≙ `x(-,-)`); Werte ohne `(),` ; Leerzeichen um Werte ignorieren.
- `reihung`: `{ "t":"reihung", "werte":[5,2,9], "indizes":true, "markiert":{"1":"gold"} }`
- `raster`: `{ "t":"raster", "zeilen":[[1,0],[0,1]] }` (2D-Reihung mit Indizes).
- `klassenkarte`: `{ "t":"klassenkarte", "name":"Held", "attribute":["- name: Zeichenkette"], "methoden":["c Held(n: Zeichenkette)","+ getName(): Zeichenkette"] }`
- `adt`: `{ "t":"adt", "art":"stapel"|"schlange"|"dynarray", "inhalt":[…] }` (Stapel: letztes Element = oben; Schlange: erstes = vorn).
- `hinweis`: `{ "t":"hinweis", "md":"…" }` (farbiger Kasten).

## 5. Interaktionen und Prüfregeln (Prüfung NUR serverseitig; Client erhält nie `loesung`, bis gelöst oder aufgedeckt)
1. `gaps` – Felder an [[id]]-Stellen in beliebigen Blöcken. `felder: {id: {typ: "text"|"zahl"|"auswahl", optionen?: [...], breite?: n, norm?: "code"|"text"|"exakt"}}`.
   loesung `{id: [akzeptierte Antworten…]}`. Vergleich: zahl → numerisch (Komma = Punkt, ±1e-9); auswahl → exakt;
   text Standard norm "code" = alle Leerzeichen entfernen, Groß/Klein beachten; "text" = Whitespace zusammenfassen, Groß/Klein egal;
   "exakt". Feedback je Feld.
2. `choice` – `optionen: [{id, md}]`, `mehrfach: bool`; loesung `{ "richtig": ["a","c"] }` (Menge exakt). Client mischt Reihenfolge.
3. `order` (Parsons/Puzzle) – `teile: [{id, code|md}]`; loesung `{ "reihenfolgen": [[ids…], …] }` (eine passt → richtig; nicht
   genannte Teile = Distraktoren, dürfen nicht verwendet werden). Feedback: erste falsche Position.
4. `lines` (Bug-Hunt) – `block`: Index des Code-Blocks in `inhalt`, `anzahl`: wie viele Zeilen zu wählen; loesung `{ "zeilen": [4] }`
   (1-basiert, Menge exakt). Typisch kombiniert mit einem zweiten Teil `gaps` für die Korrektur.
5. `match` – `elemente: [{id, md}]`, `kategorien: [{id, md}]`; loesung `{ elementId: kategorieId, … }`; Feedback je Element.
6. `tree` – `modus`:
   - `"klick"`: `baum` (Anzeige), Schüler klickt Knoten nacheinander; loesung `{ "folge": ["", "L", "LR", …] }` (Pfade: "" Wurzel,
     L/R je Schritt). Schrittprüfung erlaubt (§5.10).
   - `"bauen"`: `start` (Klammerstring, "-" = leer), Schüler fügt an leeren Stellen Werte ein / ändert / entfernt Knoten (mit Teilbaum)
     bzw. „nur Knoten entfernen“ ist nicht nötig; loesung `{ "baum": "…" }` – Vergleich nach Normalisierung (Leerzeichen, x ≙ x(-,-)).
     Optional `werte`: Liste der zu verwendenden Werte (als Chips angezeigt).
7. `array` – `start: [...]`, `modus`:
   - `"tausch"`: Schüler wählt zwei Indizes → Tausch wird ausgeführt und angezeigt; loesung `{ "tausche": [[i,j], …] }`
     (Paare ungeordnet, Reihenfolge der Tausche exakt); Schrittprüfung erlaubt. Optional `fertigKnopf` für „keine weiteren Tausche“.
   - `"klick"`: Schüler klickt Indizes nacheinander (z. B. mitte bei binärer Suche); loesung `{ "folge": [3, 5, 4] }`; Schrittprüfung.
8. `grid` – `raster` (Anzeige); Schüler markiert Zellen; loesung `{ "zellen": [[r,c], …], "reihenfolge": false }`.
9. `adtsim` – `art`, `start` (Inhalt), Schüler baut den Endzustand durch Eingabe der Elemente (Liste von Strings; Chips hinzufügen,
   entfernen, verschieben); loesung `{ "inhalt": [...] }` (Stapel: unten → oben; Schlange: vorn → hinten).
10. Schrittprüfung: POST …/pruefen mit `teilweise: true` (nur für tree-klick, array-tausch, array-klick, order) → Antwort
   `{ ok: bool, ersteFalschePosition }`; ein falscher Schritt zählt als Fehlversuch.
- Punkte: beim ERSTEN Lösen `round(punkte × max(0.25, 1 − 0.25·Fehlversuche − 0.2·genutzteTipps))`; nach „Lösung zeigen“ 0 Punkte
  (Aufgabe bleibt übbar, Status „angesehen“). Erneutes Lösen bringt keine Punkte.
- API (Vorschlag, Plattform-Agent legt fest und dokumentiert in README): GET /api/welten, /api/welten/:n, /api/aufgaben/:id (ohne
  loesung), POST /api/aufgaben/:id/pruefen, POST …/tipp, POST …/aufdecken, Boss-Endpunkte, Profil, Scoreboard, Admin-API.

## 6. Generatoren (Trainingsplatz, serverseitig, Seed-basiert, deterministisch testbar)
Mindestens: Stapel/Schlange-Befehlsfolge → Endzustand (adtsim), DynArray-Befehlsfolge (append/insertAt/delete/setItem) → Inhalt,
BST einfügen (tree bauen), Traversierung pre/in/post/level (tree klick), Bubble-/Selection-/Insertionsort ein Durchlauf (array tausch),
binäre Suche (array klick, mitte = (lo + hi) / 2), Ausdruck → Typ und Wert (gaps; int/double/String/boolean, ganzzahlige Division,
Casts, String-Verkettung, char-Arithmetik nur wenn in Welt 0 eingeführt). Jeder Generator mit Unit-Tests (Lösung korrekt, Grenzfälle).

## 7. Boss-Kampf (je Welt)
Freischaltung gemäß Kurseinstellung (automatisch ab 60 % der Level-Punkte der Welt). Start → Server zieht `anzahl` Aufgaben gemäß
`mix` aus `pool`, Timer `dauerMin` (serverseitig durchgesetzt, Kulanz 30 s). KEIN Feedback während des Kampfes (eine Abgabe je
Aufgabe, änderbar bis „Kampf beenden“). Auswertung am Ende: je Aufgabe richtig/falsch + Erklärung; Boss-Punkte = Summe der Punkte
richtiger Aufgaben; zählt der BESTE Versuch; neuer Versuch frühestens nach 12 h. „Besiegt“ ab 50 %. Aufgaben im Boss-Pool sind
eigene Aufgaben (nicht in Leveln).

## 8. Abzeichen (automatisch, Regeln im Code; Symbol + Name + Beschreibung)
Erste Schritte (1. Aufgabe), Zehnerserie (10 Aufgaben in Folge ohne Fehlversuch), Fleißig (50 gelöst), Unermüdlich (150 gelöst),
Weltenbummler (in jeder Welt ≥ 1 Aufgabe), je Welt „<Welt> gemeistert“ (alle Level-Aufgaben gelöst) und „<Boss> besiegt“,
Makellos (Boss mit 100 %), Fallensucher (je 3 Aufgaben mit fallen P1–P10 ohne Fehlversuch), Trainingsprofi (100 Trainingsaufgaben),
Ohne Tipp (20 Stufe-3-Aufgaben ohne Tipp), Kata-Meister (30 Karten in Fach 5).

## 9. Technik
Node 20, Express 5, better-sqlite3, helmet (strikte CSP, keine Inline-Skripte), `qrcode` (QR als SVG). Kein Frontend-Build,
keine CDNs. Tests: node:test + supertest (API, Rechte/Isolation Kurs↔Lehrkraft, Rate-Limits, Prüfer je Interaktion, Generatoren,
Boss-Timer, Punkteformel, Upgrade-Erkennung v1). `npm run validate` = Inhalts-Validator für seed/welten/*.json (Schema, ids, Verweise,
Lücken ↔ felder, Lösung passt zu Interaktion, Klammerbäume parsebar, order-Lösungen nur bekannte ids, Punkte/Stufen, Kategorien,
Boss-Mix erfüllbar) mit verständlichen Fehlermeldungen. Dockerfile/captain-definition wie v1 (Port 80, /app/data persistent).
Umgebungsvariablen: ADMIN_EMAIL, ADMIN_PASSWORD, SESSION_SECRET, PORT, DATA_DIR, TRUST_PROXY.
README (deutsch): Funktionen, CapRover-Deploy, Upgrade von v1 (alte DB wird gesichert, neu begonnen), Rollen, Datenschutz, API, Seed-Format
(Verweis auf docs/AUFGABENFORMAT.md mit vollständiger Formatbeschreibung §3–§5 und Beispielen).

## 10. Inhalte je Welt (Content-Agenten)
- Levels passend zu den Arbeitsblättern/DS der Welt (Quelle: /mnt/user-data/outputs/AlgoQuest/Welt<N>/*.docx, Lehrerhinweise
  Werkzeuge/AQ_W<N>_Lehrerhinweise.docx, Werkzeuge/AQ_Gesamtuebersicht_DS1-40.docx, Kata-JSON, IDE-Gerüste). Typisch 1 Level je
  DS bzw. AB-Teil (Kür-DS als eigenes Level mit „Kür“ im Titel). Level-Titel kurz und spielerisch + Fachbegriff.
- Je Level 6–8 Aufgaben (Stufenmix ≈ 40 % Stufe 1 / 40 % Stufe 2 / 20 % Stufe 3), je Welt mindestens 5 verschiedene Interaktionsarten,
  bevorzugt Abi-Klassiker: Tracetabellen, Rekursionstabellen, Struktogramm ↔ Code, Bug-Hunt (lines + gaps), Lückencode, Code-Puzzle
  (order), ADT-Simulation, Baum-Interaktion, Sortier-Schritte. Jede Aufgabe mit Erklärung (warum; bei Fallen: P-Nummer nennen).
- Boss-Pool je Welt 14–16 eigene Aufgaben (anzahl 8, dauerMin 20–30, Mix 3/3/2), abiturnah formuliert.
- Eigene Daten, nicht 1:1 aus ABs/Bossen kopiert (gleiche Konzepte, neue Werte) – Ausnahme: Testbäume/Kontexte der Welt (z. B.
  Baumschule-Bäume W5) dürfen wiederverwendet werden.
- Alle Lösungen PROGRAMMATISCH erzeugt/geprüft: Java-Snippets mit javac 21 + NI-Stub (SCRATCH/w4_code/harness/NI.java) ausführen,
  Traces/Rekursionstabellen per instrumentiertem Programm, Bäume/Sortierschritte per Skript; Prüfskript im Arbeitsordner.
- Eigenvalidierung gegen §3–§5 (Skript), da der Plattform-Validator parallel entsteht; Abschluss mit Kennzahlen je Level.
