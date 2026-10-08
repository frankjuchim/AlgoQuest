# CLAUDE.md – Algo Quest

## Projektüberblick

„Algo Quest – Das Dungeon der Datenstrukturen“ ist die LK-Einheit **Algorithmik und Datenstrukturen**
(Informatik eA, Niedersachsen, Abitur ab 2027; KC 2017 + Ergänzende Hinweise Neufassung 2025 = „EH“).
40 Doppelstunden in 7 Welten: 0 Akademie · 1 Heldenschmiede · 2 Rangliste · 3 Labyrinth · 4 Hafen · 5 Wald · 6 Endgegner.

Das Repo enthält zweierlei:

1. **WebApp „Algo Quest Lab“ v2.0** (Hauptverzeichnis): Node 20, Express 5, better-sqlite3, helmet, qrcode;
   Vanilla-JS-Oberfläche ohne Build-Schritt, keine CDNs, strikte CSP ohne Inline-Skripte.
   Live: https://algoquest.frankjuchim.de (CapRover, `captain-definition` + `Dockerfile`, Port 80, Datenbank in `/app/data`).
2. **Unterrichtsmaterial** (`materialien/`, docx/pptx – maßgebliche Fassung) und **Spezifikationen** (`quellen/specs/`).

> ⚠️ **`main` ist direkt mit CapRover verbunden: Jeder Push auf `main` startet sofort den Live-Build.**
> Nur auf Feature-Branches arbeiten; nach `main` nur nach ausdrücklicher Freigabe und mit grünen Tests.

## Ordnerstruktur

```
src/                 Server
  app.js             Express, Helmet/CSP, Sitzungen; security.js (Passwörter, Cookies, Rate-Limits)
  server.js          Start (PORT, DATA_DIR)
  db.js, domain.js   Schema/Upgrade, Konstanten (Welten, Ränge, Fallen)
  routes/            API: schueler.js, lehrer.js, admin.js
  services/          Fachlogik: inhalte (Seed), konten, kurse, lernen, stand/Abzeichen, boss, training,
                     auswertung, kata (= Warm-up-Trainer), backup
  content/           format.js, checker.js (Prüfer, serverseitig), validator.js, generators.js (Trainingsplatz)
public/              Oberfläche: spiel.html (Schüler), lehrer.html (Lehrkraft + Superadmin), board.html,
                     index.html, datenschutz.html (VORLAGE!), static/js/shared/baum.js (Klammerbäume, Server + Browser)
seed/welten/         welt0–6.json = Lab-Aufgaben (Format: docs/AUFGABENFORMAT.md) – maßgeblich, nicht neu generieren
seed/warmup/         Warm-up-Karten (Leitner-Trainer), {"version":1,"karten":[…]}
scripts/validate.js  Inhalts-Validator
test/                node:test + supertest; fixtures/welt_beispiel.json (jede Interaktion/jeder Block); e2e/e2e.js (Playwright)
docs/                AUFGABENFORMAT.md (verbindlich), Screenshots
materialien/         00_Lehrerhinweise (Einstieg: AQ_Gesamtuebersicht_DS1-40.docx), Welt<N>_<Name>/
                     1_Praesentation · 2_Arbeitsblaetter · 3_Online-IDE (Gerüste/LSG .txt) · 4_Boss · 5_Loesungen,
                     Werkzeuge/Warm-up-Karten, WebApp/ (Screenshots, Anleitungen)
quellen/specs/       SPEC_AlgoLab.md (App), SPEC_AlgoQuest_W0_W1.md (Grundkonventionen, Welt-1-API), W0_Akademie, W2–W6,
                     SPEC_Materialanpassung.md, LAB_LEVELS.md
quellen/lab-inhalte-generatoren/  historische Python-Generatoren der Lab-Aufgaben (nur Referenz, JSON ist maßgeblich)
```

## Befehle

```
npm install
npm test            # Unit-/API-Tests (node:test + supertest)
npm run validate    # Inhalts-Validator für seed/welten/*.json (auch: node scripts/validate.js <datei> [--json])
npm run e2e         # Playwright-Durchlauf (Chromium; CHROMIUM_PATH/PLAYWRIGHT_BROWSERS_PATH), Screenshots nach docs/
npm run dev         # lokal auf Port 3000, Superadmin admin / admin1234, Daten in ./data
WELT_DATEIEN=test/fixtures/welt_beispiel.json npm run dev   # mit Beispielwelt
```

In der Cloud-Umgebung: Chromium liegt unter `/opt/pw-browsers` (kein `playwright install`).
docx/pptx rendern: `soffice --headless --convert-to pdf --outdir <scratch> <datei>`.

## Konventionen

### Sprache und Ansprache
- Alles auf Deutsch (Code-Bezeichner, Kommentare, Commit-Messages, UI, Doku).
- Schülerinnen und Schüler werden **geduzt**; Prüfungsaufgaben (Bosse, Klausuren, Erwartungshorizonte) im
  **Abitur-Stil gesiezt** („Implementieren Sie …“, Operatoren, [x BE]).
- Begriffe: **„Warm-up“** (nicht Kata), **„Team“** (keine Gilden), **keine XP**. Punkte entstehen nur automatisch
  im Lab (gelöste Aufgaben, Bosse, Trainingsplatz) – keine manuelle Punktevergabe.
  (Interne Bezeichner wie `kata.js` oder `/api/kata/*` sind Altlast und bleiben; nichts davon in sichtbaren Texten.)
- „Reihung“, nie „Array“ (in Schülertexten); Typnamen nach EH: Ganzzahl, Kommazahl, Wahrheitswert, Zeichen,
  Zeichenkette, nichts.

### Online-IDE (online-ide.de, Bibliothek „Niedersachsen“)
- `Stack`, `Queue`, `DynArray`, `BinTree` sind **nicht generisch**: Inhalte sind `Object`, Casts nötig,
  z. B. `int x = (Integer) s.pop();` – exakte API in `quellen/specs/SPEC_AlgoQuest_W4.md` §0 und `SPEC_AlgoQuest_W5.md` §0.
- `==` vergleicht dort Zeichenketten inhaltlich (anders als echtes Java) → im Code-Review **immer `equals` verlangen**.
- `println(...)` ohne `System.out`; Anweisungen außerhalb von Klassen = Hauptprogramm; JUnit mit `@Test`,
  `assertEquals(expected, actual, "Meldung")`.
- Nur die erlaubten Zeichenketten-Operationen: `length`, `charAt`, `substring`, `+`, `equals`, `contains`,
  `compareTo`, `(int) c` / `(char) n` – kein `toLowerCase`, `split`, `indexOf`, `trim`, `replace` …
- Gerüste (`materialien/Welt*/3_Online-IDE/*.txt`): Kopfblock, „GERÜST – hier nichts verändern“ / „DEIN TEIL“,
  Umlaute in Kommentaren als ae/oe/ue/ss.

### Notation (EH)
- Struktogramme nach **EH §5**: Zuweisung `←`, „gib … zurück“, „für i von 0 bis n − 1“, „für jedes x in r“,
  Verzweigung als Dreieck (wahr/falsch), Kopf `name(p: Typ): Typ`, keine Java-Syntax im Struktogramm.
- Klassenkarten/-diagramme nach **EH §6**: `+`/`-` Pflicht, Konstruktor mit `c`, Assoziation ohne Kardinalitäten.
- **Rekursionstiefe:** Erstaufruf = Tiefe 0. **Baumhöhe:** leerer Baum 0, Blatt 1.

### Fallen P1–P10
Verbindlich nach `quellen/specs/SPEC_AlgoQuest_W6.md` §2 (gleiche Nummern/Kurztitel überall – Lab-Feld `fallen`,
Materialien, Warm-up, Lehrerhinweise):
P1 Laufzeitfehler nicht ausgeschlossen · P2 Struktur zerstört statt unverändert · P3 Signatur verfehlt ·
P4 Typen und Casts · P5 Zeichenketten mit == statt equals / unerlaubte Operationen · P6 Off-by-one ·
P7 Rekursion (Basisfall, Ergebnis nicht verwendet, Tiefe) · P8 Trace-Tabelle unvollständig/Konvention verletzt ·
P9 Struktogramm nicht nach EH §5 · P10 Operator verfehlt.

### Qualitätssicherung (vor jedem Commit)
- **Jede Aufgabenlösung programmatisch prüfen:** Java-Code mit `javac`/`java` (+ Nachbau der NI-Bibliothek, nicht
  generisch), Traces/Rekursionstabellen per instrumentiertem Programm, Bäume/Sortierschritte per Skript.
  Prüfskripte ins Scratchpad, nicht ins Repo.
- `npm test` **und** `npm run validate` müssen grün sein, bevor committet wird.
- Neue Aufgaben im Format von `docs/AUFGABENFORMAT.md`; jede Aufgabe mit Erklärung (bei Fallen P-Nummer nennen).

### Datenschutz und Sicherheit
- **Lösungen, Erklärungen und nicht abgerufene Tipps verlassen den Server nie vor dem Lösen bzw. Aufdecken**;
  Boss-Aufgaben nur im laufenden Kampf; Prüfung ausschließlich serverseitig. Neue Endpunkte entsprechend testen.
- Keine Klarnamen außer dem selbst gewählten Schülernamen (in Beispieldaten, Screenshots, Tests, Materialien).
- Keine externen Ressourcen/CDNs, keine Inline-Skripte (CSP), Ausgaben nur als DOM-Textknoten.

### Materialien (docx/pptx)
- Die Dateien in `materialien/` sind die maßgebliche Fassung → **direkt bearbeiten** (nicht aus Generatoren neu erzeugen).
- Danach mit `soffice` nach PDF rendern und das Ergebnis prüfen (Layout, Seitenumbrüche, Sonderzeichen ← ≤ ≠).
- Gestaltung: #1F4E79 primär, Gold #B8860B, Grün #548235, Rot #C00000, Kasten #DBE7F5; Calibri 11 pt, Consolas 10 pt.

## Offene Punkte
- IDE-Gerüste sind nur mit `javac` + Nachbau der NI-Bibliothek getestet, noch nicht in der echten Online-IDE.
- `public/datenschutz.html` ist eine Vorlage und muss von der Schule angepasst werden.
