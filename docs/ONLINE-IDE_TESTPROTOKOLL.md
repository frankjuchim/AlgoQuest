# Testprotokoll: Gerüste in der echten Online-IDE

Alle Online-IDE-Dateien sind automatisch geprüft, und zwar mit javac (Java 21) gegen einen Nachbau der Bibliothek
„Niedersachsen“ (`python3 werkzeuge/ide-pruefung/ide_pruefen.py`, läuft auch als GitHub-Prüfung). Ein Probelauf in
der echten Online-IDE ersetzt das nicht. Dieses Protokoll braucht etwa 45 Minuten. Die Zahlen unten sind die
Sollwerte aus dem Prüfstand.

## Vorbereitung (einmalig, ca. 5 min)

1. Auf online-ide.de mit einem **Test-Account** anmelden (nicht im Kurs-Account).
2. `materialien/Online-IDE/AQ_Alle_Welten_Workspaces.json` importieren, für die Musterlösungen zusätzlich
   `Lehrkraft/AQ_Musterloesungen_Workspaces.json`.
3. ☐ Nach dem Import stehen 13 Gerüst-Workspaces und 14 LSG-Workspaces in der Liste.
4. ☐ Bei den Workspaces von W4, W5 und W6 ist die Bibliothek aktiv: Rechtsklick → „Einstellungen“ → Häkchen
   „Abiturklassen Niedersachsen“. W0–W3 brauchen sie nicht.

## A. Musterlösungen: alle Tests grün?

Je Workspace die Datei öffnen, Programm einmal starten (das Hauptprogramm darf keinen Fehler melden), dann im
Reiter „Testrunner“ alle Testklassen ausführen.

| ☐ | Workspace | Testklassen (Anzahl Tests) | Soll |
|---|---|---|---|
| ☐ | LSG W0 Diagnose | DiagnoseBasisTest (10), DiagnoseErweiterungTest (12), DiagnoseExperteTest (9) | 31/31 grün |
| ☐ | LSG W0 Akademie | L02WerkstattTest (21), L03VorratTest (19), L04ZauberTest (18), L05ZauberIITest (25), PapierCompiler0Test (6) | 89/89 grün |
| ☐ | LSG W1 Heldenschmiede | L11HeldTest (14), L12MonsterTest (12), L13InventarTest (19), L14VererbungTest (14) | 59/59 grün |
| ☐ | LSG W2 Rangliste | L21StandardTest (16), L22SortierTest (22), L23SucheTest (13) | 51/51 grün |
| ☐ | LSG W3 Labyrinth | L31RekursionTest (18), L32KarteTest (20), L33TeileHerrscheTest (17) | 55/55 grün |
| ☐ | LSG W4 Hafen | L41 (10), L42 (10), L43 (10), L44 (12), L45 (7), L46ExpertenpfadTest (12) | 61/61 grün |
| ☐ | LSG W5 Wald | L51BaumTest (11), L52RekursivTest (8), L53AkinatorTest (8), L54SuchbaumTest (11) | 38/38 grün |
| ☐ | LSG W6 Papier-Compiler Probeklausur | ProbeklausurTest (17) | 17/17 grün |

Grafikprogramme ohne Tests: ☐ LSG W2 Sortier-Duell · ☐ LSG W3 Fraktale · ☐ LSG W3 Dungeon-Rennen ·
☐ LSG W5 Baumzeichner. Hier nur prüfen, dass das Programm startet, die Animation läuft und am Ende keine
Fehlermeldung kommt. Beim Baumzeichner zusätzlich ☐ `destroy()` auf Text und ☐ die Fenstergröße bei großen Bäumen.

## B. Gerüste: kompilieren, Hauptprogramm läuft, Tests anfangs (fast) alle rot

| ☐ | Workspace | Tests | Soll vor dem Bearbeiten |
|---|---|---|---|
| ☐ | W0 Diagnose – Das Portal | 31 | 6 grün (Platzhalter-Rückgaben passen zufällig: `basis_summe_leereReihung`, `basis_zaehle_leereReihung`, `basis_zaehle_nichtEnthalten`, `erweiterung_sortiert_nein`, `experte_palindrom_grossUndKlein`, `experte_palindrom_nein`) |
| ☐ | W0 Akademie | 70 (+19 nach dem Freischalten) | 0 grün |
| ☐ | W1 Heldenschmiede | 45 (+14 nach dem Freischalten von Level 1.4) | 5 grün (`basis_istBesiegt_neuerHeld`, `erweiterung_istBesiegt_beiEinemLeben`, `erweiterung_enthaeltLeer`, `experte_enthaeltNurExakterName`, `experte_wertvollsterLeer`) |
| ☐ | W2 Rangliste | 51 | 1 grün (`experte_sortieren_leerUndEinEintrag`) |
| ☐ | W3 Labyrinth | 55 | 0 grün |
| ☐ | W4 Hafen | 57 (+4 nach dem Freischalten von Level 4.6) | 0 grün |
| ☐ | W5 Wald | 38 | 0 grün |
| ☐ | W5 Runenbuch – Testumgebung (AB 3) | 2 | 0 grün |
| ☐ | W6 Papier-Compiler Probeklausur | 17 | 0 grün |
| ☐ | Lehrkraft W6 Klausur Ladepark | 25 | 3 grün (VorgabenTest); nach Einsetzen der Musterlösung vom Dateiende 25/25 |
| ☐ | Lehrkraft W6 Nachschreibklausur Kletterhalle | 29 | 4 grün; nach Einsetzen der Musterlösung 29/29 |

Grafik-Gerüste: ☐ W2 Sortier-Duell · ☐ W3 Fraktale · ☐ W3 Dungeon-Rennen · ☐ W5 Baumzeichner starten ohne Fehler.

## C. Freischalt-Blöcke

☐ W0 Akademie: Zeilen `/* LEVEL-0.4-START …` und `… LEVEL-0.4-ENDE */` löschen (Erweiterung, dann Experte). Danach
erscheinen zusätzliche Tests in L04ZauberTest. Dasselbe gilt für `PAPIER-COMPILER-0`, danach erscheint
PapierCompiler0Test. ☐ W1 Level 1.4 und ☐ W4 Level 4.6 genauso. Erwartung: Nach dem Freischalten kompiliert das Gerüst
erst, wenn die geforderten Klassen bzw. Methodenköpfe geschrieben sind. Das ist so gewollt.

## D. Dialekt der Online-IDE (die eigentlichen Unsicherheiten)

| ☐ | Punkt | So prüfen | Erwartung / Folge |
|---|---|---|---|
| ☐ | `assertEquals` mit Kommazahlen | LSG W0 Diagnose: `DiagnoseErweiterungTest` (durchschnitt) | grün. Sonst Toleranz klären und Tests anpassen |
| ☐ | Casts `(Integer)`, `(Character)`, `(String)` mit Unboxing | LSG W4 Hafen: Hauptprogramm und L41–L45 | grün, keine Typfehler |
| ☐ | Exceptions der Bibliothek fangbar | In LSG W4 `obersterWert` die Leerabfrage löschen → `basis_obersterWert_leer` | rot mit „LAUFZEITFEHLER: top, pop …“ |
| ☐ | BinTree auf leerem Baum | In LSG W5 Wald die Abfrage `isEmpty()` in einer Methode löschen | Test rot mit Laufzeitfehler-Hinweis |
| ☐ | Endlosschleife im Testrunner | In LSG W4 `ausscheiden` den Zähler entfernen | Wie reagiert der Testrunner? Notieren (Anhalten-Knopf?) |
| ☐ | for-each über DynArray | Kurztest: `for (Object o : d) { println(o); }` | Läuft es? Die Musterlösungen kommen ohne aus |
| ☐ | Array-Literale `{…}` in Tests | LSG W0/W2 | kompiliert |
| ☐ | Private Hilfsmethoden in Testklassen | LSG W4/W5: Testrunner-Liste | Sie erscheinen nicht als Tests |

### `==` bei Zeichenketten: bekannte Lücke

Die Online-IDE vergleicht Zeichenketten mit `==` inhaltlich. Diese Tests sollen „`==` statt `equals`“ erkennen. In
der Online-IDE bleiben sie bei falscher Lösung aber **grün**, nur im Prüfstand (echtes Java) werden sie rot:

- W1 `L13InventarTest.experte_enthaeltMitEquals`
- W2 `L21StandardTest.experte_indexVonMitEquals`
- W5 `L51BaumTest.experte_berechne_equals`
- W6 Klausur/Nachschreibklausur: Teile d) und n) bzw. d) (Vergleich von Kennzeichen/Namen)

☐ Probe: In LSG W1 `enthaelt` auf `==` umstellen. Bleibt `experte_enthaeltMitEquals` grün, ist die Lücke bestätigt.
Folge: `equals` im Code-Review und bei der Korrektur von Hand prüfen (Falle P5).

## Ergebnis

Datum: ________  Version der Online-IDE: ________  Geprüft von: ________

Abweichungen bitte als Notiz in diese Datei oder an Claude geben. Die Gerüste und Musterlösungen werden dann
angepasst, und die Workspaces werden mit `python3 werkzeuge/workspaces_erzeugen.py` neu erzeugt.
