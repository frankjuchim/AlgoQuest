# Erklärvideos – Arbeitsweise und Format

**Nicht öffentlich.** Der Ordner `materialien/Videos/` ist Arbeitsmaterial für die Aufnahme (Skripte, Folien) und
kommt nicht ins Docker-Image. Öffentlich werden erst die fertigen Videos auf YouTube; verlinkt werden sie später im Lab.

Die Übersicht der Videos (Inhalte, Länge, Reihenfolge, Tipps) steht in [`00_Uebersicht.md`](00_Uebersicht.md).

## Je Video ein Ordner

```
NN_Kurztitel/
  video.json                          Quelle – hier wird bearbeitet (Folien, Sprechertext, Metadaten)
  AQ_VideoNN_Kurztitel_Folien.pptx    ERZEUGT: Folien zum Abfilmen, Sprechertext in den Notizen (Referentenansicht)
  AQ_VideoNN_Kurztitel_Skript.md      ERZEUGT: Drehbuch mit Lernzielen, YouTube-Text, Kapitelmarken, Folie für Folie
  bilder/                             ERZEUGT: Struktogramme, Bäume, Stapel … (mit dem Renderer des Labs) und Screenshots
  quellbilder/                        optional: von Hand bzw. per Skript zusammengesetzte Bilder (z. B. Klassendiagramme mit
                                      Pfeilen), eingebunden über "bilddateien" – bei Änderungen der Inhalte von Hand erneuern
```

Nach jeder Änderung an einer `video.json`:

```
python3 werkzeuge/video_folien.py NN_Kurztitel      # ein Video neu erzeugen (ohne Angabe: alle)
python3 werkzeuge/video_folien.py --pruefen         # Kamera-Zone frei, Skripte aktuell, Bilder vorhanden
```

Die Folien kannst du danach auch direkt in PowerPoint nachbearbeiten. Dann aber nicht erneut erzeugen, sonst sind
die Handänderungen weg (oder die Änderung zusätzlich in die `video.json` übernehmen).

## Kamera-Zone

Auf jeder Folie bleibt **unten rechts** ein Bereich frei (ab 9,35 in von links und 4,55 in von oben, also etwa das
rechte untere Viertel): Dort liegt in der Aufnahme dein Kamerabild. Der Generator bricht ab, wenn etwas hineinragt.
Folienformat 16:9 (13,33 × 7,5 in), Schrift Calibri/Consolas, Farben wie in den übrigen Materialien.

## Format der `video.json`

```json
{
 "nr": 1, "kurz": "Struktogramm_und_Tracetabelle",
 "titel": "…", "untertitel": "…", "welt": 0, "weltname": "Welt 0 · Die Akademie", "farbe": "#7F6000",
 "laenge": "8–10 min", "zielgruppe": "…", "einsatz": "Welt, DS, Lab-Level, Arbeitsblatt",
 "lernziele": ["…"], "hinweise": ["Hinweise für die Aufnahme, geprüfte Werte …"],
 "youtube": {"titel": "…", "beschreibung": "…", "tags": ["…"]},
 "bilder": { "name": { "t": "struktogramm", … , "_breite": 480 } },
 "bilddateien": { "name": "materialien/WebApp/Screenshots/schueler_code.jpg" },
 "folien": [ { "typ": "…", "titel": "…", "kapitel": "…", "regie": "…", "sprechertext": "…", "pause_s": 0 } ]
}
```

- `bilder`: Blöcke im Format von `docs/AUFGABENFORMAT.md` §5 (`struktogramm`, `baum`, `reihung`, `adt`, `raster`,
  `klassenkarte`, `tabelle` …), gerendert mit dem Lab-Renderer. `_breite` (px) begrenzt die Breite, ein schmaleres
  Struktogramm wird dabei höher und auf der Folie größer.
- `bilddateien`: vorhandene Bilder (z. B. Screenshots aus `materialien/WebApp/Screenshots/`) werden nach `bilder/` kopiert.
- Pro Folie: `sprechertext` (wird zu Notizen und Drehbuch; Länge ≈ 130 Wörter je Minute), `kapitel` (YouTube-Kapitelmarke
  ab dieser Folie), `regie` (Hinweis für die Aufnahme), `pause_s` (Denkpause, zählt zur Länge).
- In Texten: `` `Code` `` wird in Consolas gesetzt, `**fett**` fett. Punktlisten: Unterpunkte beginnen mit `"  - "`.

### Folientypen

| `typ` | Felder | Aufbau |
|---|---|---|
| `titel` | – (nutzt `titel`, `untertitel`, `weltname` des Videos) | Titelfolie |
| `punkte` | `punkte`, opt. `groesse` | Stichpunkte links; rechts oben optional `bild`, `tabelle` oder `kasten` |
| `code` | `code`, opt. `markiere` (Zeilen rot), `nummern` (Standard true), `groesse` (Standard 18), `unten` (Stichpunkte unter dem Code) | Code links, rechts oben optional `bild`/`tabelle`/`kasten`; Schrift wird automatisch so verkleinert, dass nichts umbricht |
| `bild` | `bild`, opt. `text` (eine Zeile darüber), `bild2` | großes Bild links, rechts oben optional `kasten`/`tabelle`/`bild2` |
| `tabelle` | `tabelle: {kopf, zeilen, groesse, hervorheben: [Zeilenindex], breiten}`, opt. `text`, `tabellenbreite` | Tabelle links, rechts optional `kasten`/`bild` |
| `pause` | `aufgabe`, opt. `code`, `kasten`/`bild` | „⏸ Video anhalten“ – Aufgabe zum Mitmachen |
| `merke` | `punkte` | grüner Zusammenfassungskasten |
| `ende` | `links: {"Lab": "…", "Arbeitsblatt": "…"}`, `naechstes` | Verweise ins Lab, nächstes Video |

Rechte Spalte (`punkte`, `code`, `bild`, `tabelle`, `pause`): `kasten: {farbe: blau|gold|gruen|rot, titel, text: [...]}`,
`bild` oder `tabelle`; Beginn der rechten Spalte mit `teilung` (in, Standard 8,2) verschiebbar. Die rechte Spalte endet
immer über der Kamera-Zone.

## Inhaltliche Regeln

- **Keine Lösungen verraten:** Beispiele eigens für das Video wählen, nicht aus Lab-Aufgaben, Arbeitsblättern, Bossen,
  Warm-up-Karten oder Klausuren übernehmen.
- **Alles nachrechnen:** Java-Code mit `javac`/`java` (für Stapel, Schlange, DynArray, BinTree mit dem Nachbau der
  Bibliothek „Niedersachsen“ in `werkzeuge/ide-pruefung/java`), Traces und Bäume per Programm. Geprüfte Werte in
  `hinweise` festhalten.
- Konventionen wie in den Materialien (CLAUDE.md): EH §5/§6, „Reihung“ statt „Array“, deutsche Typnamen,
  Tracetabellen nur mit Variablen und `// → Tabellenzeile`, Rekursionstiefe ab 0, Baumhöhe (leer 0, Blatt 1),
  `equals` statt `==` bei Zeichenketten, NI-Klassen nicht generisch (Casts), Fallen P1–P10 mit Nummer.
- Ansprache: Schülerinnen und Schüler werden geduzt. Zitierte Abitur-Aufgaben bleiben gesiezt („Stellen Sie … dar“).
- Keine Klarnamen, keine echten Kurscodes oder Schülerdaten in Folien und Screenshots.
