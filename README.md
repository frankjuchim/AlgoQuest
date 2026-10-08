# Algo Quest Lab 2.0 – interaktive Übungsplattform für den Informatik-LK

Algo Quest Lab ist die Übungsplattform zur Einheit „Algo Quest – Das Dungeon der Datenstrukturen“ (LK Informatik eA,
Niedersachsen). Schülerinnen und Schüler bearbeiten auf einer Weltkarte (Welt 0 Akademie … Welt 6 Endgegner) automatisch
geprüfte Aufgaben im Abitur-Stil – Tracetabellen, Struktogramme nach EH §5, Bug-Hunts, Code-Puzzles, ADT-Simulationen,
Baum- und Sortier-Interaktionen –, kämpfen gegen Bosse, trainieren mit Zufallsaufgaben und Warm-up-Karten und sammeln Punkte,
Ränge und Abzeichen. Lehrkräfte verwalten ihre Kurse und sehen Lernstand, Aufgabenstatistik und das „Fallen-Profil“ (P1–P10).

**v2.0 ersetzt die bisherige WebApp v1.x vollständig.** Punkte entstehen ausschließlich automatisch durch gelöste Aufgaben, Bosse und den Trainingsplatz.

![Weltkarte](docs/weltkarte_alle_welten.png)

## Funktionen

**Schüler** (Tablet/iPad-tauglich, Touch-Ziele ≥ 44 px, Tastatur und Screenreader)
- Selbstanmeldung: Kurscode + Name → persönlicher Code `ABC-123` („Notiere deinen Code“). Weiterspielen auf jedem Gerät mit
  Kurscode + Name + Code. Namen sind je Kurs eindeutig (Groß/Klein egal), 2–30 Zeichen.
- Weltkarte mit Fortschrittsringen je Level, Trainingsplatz- und Boss-Knoten, gesperrte Welten ausgegraut.
- Level-Seite: Merkkasten, Aufgabenliste (offen / gelöst / Lösung angesehen, Punkte), Karte „Programmieren in der Online-IDE“
  (nur Info + Häkchen, 0 Punkte).
- Aufgaben mit allen Blocktypen (Text, Code mit Zeilennummern und Lücken, Struktogramm als HTML/CSS nach EH §5, Tabelle,
  Baum als SVG, Reihung, Raster, Klassenkarte nach EH §6, ADT, Hinweis) und Interaktionen (Lücken, Auswahl, Puzzle,
  Bug-Hunt, Zuordnen, Baum klicken/bauen, Reihung tauschen/klicken, Raster, ADT-Simulation, mehrteilig, Schrittprüfung).
  „Prüfen“, „Tipp“, „Lösung zeigen“ (danach 0 Punkte), Feedback je Feld/Schritt, Erklärung nach dem Lösen.
- Punkte beim ersten Lösen: `round(punkte × max(0.25, 1 − 0.25·Fehlversuche − 0.2·Tipps))`.
- Trainingsplatz (Welten 0, 2, 4, 5, 6): Zufallsaufgaben aus Generatoren (Ausdruck → Typ/Wert, Bubble-/Selection-/Insertionsort
  ein Durchlauf, binäre Suche, Stapel/Schlange/dynamische Reihung, Suchbaum einfügen, Traversierungen); 1 Punkt je Aufgabe,
  höchstens 30 pro Tag.
- Boss-Kampf je Welt: Ziehung nach Stufen-Mix, serverseitiger Timer, kein Feedback während des Kampfes, Auswertung mit
  Erklärungen, bester Versuch zählt, neuer Versuch nach 12 h, „besiegt“ ab 50 %.
- Warm-up-Trainer (Leitner, 5 Fächer, aus v1 übernommen, ohne Punkte).
- Profil: Punkte, Rang (Novize/Lehrling/Geselle/Meister/Großmeister bei 0/10/30/55/80 % der Level-Punkte aller
  freigeschalteten Welten), Abzeichen, Fortschritt je Welt, „Deine Fallen“ (Fehlversuche je P1–P10), eigener Code.
- Scoreboard (falls aktiviert): gesamt oder je Welt, eigener Eintrag hervorgehoben.

**Lehrkräfte**
- Zugang auf Anfrage (Name, E-Mail, Schule, Passwort, Nachricht) → Freigabe durch den Superadmin.
- Kurse anlegen (Kurscode 6 Zeichen), Beitritts-Link `/k/<KURSCODE>` + QR-Code (SVG).
- Schülerliste (Name, Code, Punkte, gelöst, Rang, zuletzt aktiv): umbenennen, neuen Code erzeugen, löschen; alle Schüler
  löschen bzw. Kurs löschen (Bestätigung durch Eintippen des Kursnamens).
- Einstellungen: freigeschaltete Welten, Bosse automatisch (ab 60 % der Level-Punkte) / offen / gesperrt, Scoreboard für
  Schüler, Beamer-Board, Anmeldung neuer Schüler offen.
- Auswertung: Fortschrittsmatrix Schüler × Level, Boss-Ergebnisse, Aufgabenstatistik (Lösungsquote, Ø Fehlversuche, häufige
  falsche Antworten), Fallen-Profil des Kurses, CSV-Export (Übersicht, Matrix, Aufgaben).
- Abschluss-Urkunden (Kurs → „🏅 Urkunden“, Seite `/lehrer/urkunden?kurs=<id>`): eine A4-Urkunde je Schüler mit Name, Kurs,
  Rang, Punkten, gelösten Aufgaben, Abzeichen und Platzierung (überall / nur Platz 1–3 / ausblenden), Datum und
  Unterschriftslinie; Auswahl alle oder einzelne Schüler; optionale Leerzeile für den vollständigen Namen; Druckknopf (`@page` A4).
- Aufgaben-Vorschau („📖 Aufgaben“): Welt → Level (mit AB- und IDE-Verweis, Merkkasten) → Aufgabe mit eingesetzter Lösung,
  Tipps und Erklärung, inkl. Boss-Pool – zum Nachschlagen passend zu den Arbeitsblättern.
- Beamer-Board `/board/<KURSCODE>`: Top 15, Weltfortschritt des Kurses, letzte 8 Erfolge, Auto-Aktualisierung 60 s, noindex.

**Superadmin** (aus Umgebungsvariablen): Anfragen bestätigen/ablehnen, Lehrkräfte deaktivieren/aktivieren/löschen,
Einmal-Passwort setzen (Passwort-Reset ohne E-Mail), alle Kurse sehen, Seed-Bericht/Inhalte neu einlesen, Warm-up-Import,
Backup/Restore (JSON).

## Rollen

| Rolle | Anmeldung | sieht |
|---|---|---|
| Schüler | Kurscode + Name + Code | eigener Lernstand, Scoreboard des eigenen Kurses (falls aktiv) |
| Lehrkraft | E-Mail + Passwort (nach Freigabe) | nur eigene Kurse (fremde Kurse → 404) |
| Superadmin | `ADMIN_EMAIL` + `ADMIN_PASSWORD` | alles |

## Betrieb mit CapRover

1. Neue App anlegen (z. B. `algoquest`), **HTTP-Port 80**, „Persistent Data“ aktivieren und das Verzeichnis
   **`/app/data`** als Persistent Directory einbinden (hier liegt die SQLite-Datenbank `algoquest.db`).
2. Umgebungsvariablen setzen:

   | Variable | Bedeutung |
   |---|---|
   | `ADMIN_EMAIL` | Login des Superadmins (Standard `admin`) |
   | `ADMIN_PASSWORD` | Passwort des Superadmins (mind. 10 Zeichen empfohlen; ohne → Superadmin-Login gesperrt). Wird bei jedem Start gesetzt; eine Änderung beendet bestehende Superadmin-Sitzungen. |
   | `SESSION_SECRET` | langer Zufallswert (≥ 16 Zeichen) zum Signieren der Sitzungs-Cookies – ohne ihn müssen sich nach jedem Neustart alle neu anmelden |
   | `PORT` | Standard 80 |
   | `DATA_DIR` | Standard `/app/data` |
   | `TRUST_PROXY` | Standard `1` (ein Proxy, z. B. CapRover/nginx); `false` ohne Proxy |

3. HTTPS in CapRover aktivieren (Cookies werden dann automatisch `secure`).
4. Deploy: Die App ist per GitHub-Webhook mit dem Branch `main` verbunden – **jeder Push auf `main` baut und startet die
   Live-Version** (`captain-definition` → `Dockerfile`). Deshalb auf Feature-Branches arbeiten; die GitHub Action
   „Prüfung“ führt bei jedem Push und Pull Request `npm test`, `npm run validate` und die Inhaltsprüfungen aus.
   Alternativ: Ordner als tar hochladen oder `caprover deploy`.
   Healthcheck: `GET /healthz`.

Lokal: `npm install`, dann `npm run dev` (Port 3000, Superadmin `admin` / `admin1234`) bzw.
`WELT_DATEIEN=test/fixtures/welt_beispiel.json npm run dev` mit der Beispielwelt.

## Inhalte

- Welten: `seed/welten/welt<N>.json` – Format: **[docs/AUFGABENFORMAT.md](docs/AUFGABENFORMAT.md)**.
  Bei jedem Start Upsert nach id (Lernstände bleiben); fehlerhafte Aufgaben werden ausgelassen, eine unbrauchbare Datei
  übersprungen – die App startet immer (Bericht im Superadmin-Bereich unter „Inhalte“).
- Prüfen vor dem Deploy: `npm run validate` bzw. `node scripts/validate.js <datei>`.
- Warm-up-Karten: `seed/warmup/warmup_*.json` (`{"version": 1, "karten": [...]}`), zusätzlich Import im Superadmin-Bereich.

## Upgrade von v1.x

Beim Start erkennt Algo Quest Lab eine Datenbank der Vorgängerversion v1.x (an deren Tabellen bzw. `meta.schema_version ≤ 2`)
im selben `DATA_DIR`. Sie wird nach **`algoquest.v1-backup-<datum>.db`** umbenannt (inkl. WAL-Dateien; bei Namensgleichheit
mit Zähler) und eine neue Datenbank angelegt – **keine Datenübernahme**. Das Log enthält einen Hinweis. Die Sicherung kann
bei Bedarf mit jedem SQLite-Werkzeug geöffnet werden. Neue Schema-Version: 3.

## Datenschutz

- Gespeichert werden nur: selbst gewählter Schülername (Empfehlung „Vorname + Initial“), persönlicher Code, Kurszugehörigkeit,
  Lernstand (Fortschritt, Fehlversuche, Tipps, Punkte, Abzeichen, Boss-/Trainingsergebnisse, Warm-up-Kartei, zuletzt aktiv);
  bei Lehrkräften Name, E-Mail, Schule, Nachricht, Passwort-Hash (scrypt).
- Keine externen Ressourcen/CDNs, keine Tracking-Cookies; strikte Content-Security-Policy ohne Inline-Skripte;
  `X-Robots-Tag: noindex`.
- Sitzungs-Cookies: signiert (HMAC-SHA256), `httpOnly`, `SameSite=Lax`, hinter HTTPS `secure`; Schüler 30 Tage, Lehrkräfte 8 h.
- Löschfunktionen: einzelne Schüler, alle Schüler eines Kurses, Kurs, Lehrkraft (mit allen Kursen).
- Datenschutzhinweise: `/datenschutz` – **Vorlage**, von der Schule anzupassen (`public/datenschutz.html`).

## Sicherheit

- Lösungen, Erklärungen und noch nicht abgerufene Tipps verlassen den Server erst nach dem Lösen bzw. „Lösung zeigen“;
  Boss-Aufgaben sind nur im laufenden Kampf abrufbar; Prüfung ausschließlich serverseitig.
- Alle Eingaben werden validiert, SQL nur parametrisiert, Ausgaben XSS-sicher (DOM-Textknoten, eigenes Mini-Markdown).
- CSRF: schreibende API-Anfragen nur mit passender `Origin`/`Referer` und als JSON.
- Rate-Limits: Beitritt (60 / 10 min je IP), Schüler-Login (8 Fehlversuche / 15 min je Konto, 100 je IP),
  Lehrkraft-Login (8 je Konto, 20 je IP / 15 min), Registrierung (5 / h je IP), Prüfen/Tipp/Aufdecken (90 / min je Schüler).
- Passwörter: `crypto.scrypt`, N = 32768, r = 8, p = 1, 64 Byte, 16 Byte Salt je Passwort; Format
  `scrypt$N$r$p$salt$hash`. Mindestlänge 10 Zeichen.

## API-Übersicht

Alle Antworten JSON; schreibende Anfragen mit `Content-Type: application/json` und gleicher Herkunft.

**Öffentlich**
| Methode | Pfad | Zweck |
|---|---|---|
| GET | `/healthz` | Healthcheck |
| GET | `/api/sitzung` | angemeldeter Schüler/Lehrkraft |
| GET | `/api/kurs/:code` | Kursname, Anmeldung offen? |
| POST | `/api/schueler/beitreten` | `{kurscode, name}` → `{name, code, kurs}` |
| POST | `/api/schueler/anmelden` | `{kurscode, name, code}` |
| POST | `/api/schueler/abmelden` | |
| GET | `/api/board/:code` | Beamer-Board (nur wenn aktiviert) |
| POST | `/api/lehrer/registrieren` | `{name, email, schule, passwort, nachricht}` |
| POST | `/api/lehrer/anmelden` / `abmelden` | `{email, passwort}` |

**Schüler**
| Methode | Pfad | Zweck |
|---|---|---|
| GET | `/api/welten` | Weltkarte mit Fortschritt |
| GET | `/api/levels/:id` · POST `/api/levels/:id/ide` | Level-Seite · IDE-Häkchen `{erledigt}` |
| GET | `/api/aufgaben/:id` | Aufgabe ohne Lösung (+ Zustand; Lösung erst nach Lösen/Aufdecken) |
| POST | `/api/aufgaben/:id/pruefen` | `{antwort, teilweise?, teil?}` → `{ok, teile, felder?, ersteFalschePosition?, zustand, geloest, punkteErhalten, neueAbzeichen}` |
| POST | `/api/aufgaben/:id/tipp` · `/aufdecken` | nächster Tipp · Lösung zeigen (0 Punkte) |
| GET | `/api/training/:welt` · POST `/api/training/:welt/neu` | Trainingsplatz · neue Aufgabe `{generator?}` |
| GET/POST | `/api/training/aufgabe/:id` · `/pruefen` · `/aufdecken` | Trainingsaufgabe |
| GET | `/api/boss/:welt` · POST `/api/boss/:welt/start` | Status (frei, Sperre, Versuche) · Kampf starten |
| GET | `/api/boss/kampf/:id` | laufend: Aufgaben + gespeicherte Antworten; beendet: Auswertung |
| PUT | `/api/boss/kampf/:id/antwort` | `{aufgabeId, antwort}` (ohne Feedback) |
| POST | `/api/boss/kampf/:id/beenden` | auswerten |
| GET | `/api/profil` · `/api/scoreboard?welt=` | Profil · Scoreboard |
| GET/POST | `/api/kata/meta` · `/api/kata/statistik` · `/api/kata/ziehen` · `/api/kata/antwort` | Warm-up-Trainer |

**Lehrkraft** (Präfix `/api/lehrer`; nach Einmal-Passwort nur `ich` und `passwort`)
| Methode | Pfad | Zweck |
|---|---|---|
| GET · POST | `/ich` · `/passwort` | Konto · Passwortwechsel `{alt, neu}` |
| GET | `/inhalte` | geladene Welten/Level |
| GET · POST | `/kurse` | eigene Kurse (Superadmin: alle) · anlegen `{name}` |
| GET · PATCH · DELETE | `/kurse/:id` | Kurs · `{name?, einstellungen?}` · löschen `{bestaetigung}` |
| GET | `/kurse/:id/schueler` | Schülerliste |
| PATCH · DELETE | `/kurse/:id/schueler/:sid` | umbenennen `{name}` · löschen |
| POST | `/kurse/:id/schueler/:sid/neuer-code` | neuer persönlicher Code |
| POST | `/kurse/:id/alle-schueler-loeschen` | `{bestaetigung: Kursname}` |
| GET | `/kurse/:id/scoreboard?welt=` · `/auswertung` | Scoreboard · Auswertung |
| GET | `/kurse/:id/export.csv?art=uebersicht\|matrix\|aufgaben` | CSV (Semikolon, UTF-8 mit BOM) |
| GET | `/kurse/:id/qr.svg` | QR-Code des Beitritts-Links |
| GET | `/kurse/:id/urkunden` | Daten für die Abschluss-Urkunden |
| GET | `/vorschau` · `/vorschau/:aufgabeId` | Aufgaben-Vorschau: Welten/Level/Boss-Pool · Aufgabe mit Lösung, Tipps, Erklärung |

**Superadmin** (Präfix `/api/admin`)
| Methode | Pfad | Zweck |
|---|---|---|
| GET | `/lehrkraefte` | alle Konten inkl. Anfragen |
| POST | `/lehrkraefte/:id/status` | `{status: aktiv\|abgelehnt\|deaktiviert}` |
| POST | `/lehrkraefte/:id/einmalpasswort` | Einmal-Passwort (wird einmal angezeigt) |
| DELETE | `/lehrkraefte/:id` | Konto mit Kursen löschen |
| GET · POST | `/backup` · `/restore` | JSON-Sicherung (Format 2) |
| GET · POST · DELETE | `/katas` · `/katas/import` · `/katas/:id` | Warm-up-Karten |
| GET · POST | `/inhalte` · `/inhalte/neu-laden` | Seed-Bericht · Welt-Dateien neu einlesen |

## Entwicklung und Tests

```
npm test            # node:test + supertest (API, Rechte, Prüfer, Generatoren, Boss, Abzeichen, Upgrade, CSV, Validator …)
npm run validate    # Inhalts-Validator für seed/welten/*.json
npm run e2e         # Playwright-Durchlauf (Chromium), Screenshots nach docs/
```

Für `npm run e2e` wird `playwright-core` (devDependency) mit einem vorhandenen Chromium genutzt
(`CHROMIUM_PATH` oder `PLAYWRIGHT_BROWSERS_PATH`, sonst `npx playwright install chromium`).

Aufbau: `src/app.js` (Express, Helmet/CSP, Sitzungen), `src/routes/*` (API), `src/services/*` (Fachlogik: Inhalte/Seed,
Konten, Kurse, Lernen, Stand/Abzeichen, Boss, Training, Auswertung, Warm-up, Backup), `src/content/*` (Format, Prüfer,
Validator, Generatoren), `public/` (Vanilla-JS-Oberfläche ohne Build: `spiel.html` Schüler, `lehrer.html` Lehrkräfte und
Superadmin, `board.html`, `index.html`), `public/static/js/shared/baum.js` (Klammerbäume, Server und Browser).
