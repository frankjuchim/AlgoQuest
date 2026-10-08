**Lehrerhandreichung · Welt 0**

**Algo Quest – Lehrerhinweise DS 1 bis 7**

Diese Handreichung beschreibt den Verlauf der Doppelstunden 1 bis 7 (à 90 min, Wochen 1–3) der Einheit „Algo Quest – Das Dungeon der Datenstrukturen“: Welt 0 „Die Akademie“ mit Kick-off, Basics (Werkstatt, Vorratskammer), eigenen Methoden (Zauberschule), Methoden-Werkstatt und Boss-Kampf 0. Grund für den Umfang: In allen 22 Abituraufgaben 2022–2026 wurde implementiert – immer als Methode mit vorgegebener Signatur. Welt 1 „Heldenschmiede“ (DS 8–12) beschreibt AQ_W1_Lehrerhinweise.docx. Grundlage: KC 2017 und Ergänzende Hinweise (Neufassung 2025).

**Überblick**

| **DS** | **Wo.** | **Thema**                                                               | **Online-IDE-Level** | **Kata (Einstieg / Zusatz)**                           |
|--------|---------|-------------------------------------------------------------------------|----------------------|--------------------------------------------------------|
| 1      | 1       | Kick-off: Das Portal öffnet sich + Level 0 „Diagnose“                   | L0 Diagnose          | – (AB 1, Aufgabe 4 als erste Kata)                     |
| 2      | 1       | L0.2 Die Werkstatt: Datentypen, Operatoren, Verzweigungen, Schleifen    | L0.2                 | W0-01, W0-02, W0-03, W0-04, W0-09, W0-10, W0-11, W0-12 |
| 3      | 1       | L0.3 Die Vorratskammer: Reihungen und Zeichenketten                     | L0.3                 | W0-05, W0-06, W0-08, W0-13, W0-14, W0-15               |
| 4      | 2       | L0.4 Die Zauberschule I: Eigene Methoden bauen und aufrufen             | L0.4                 | W0-16, W0-17                                           |
| 5      | 2       | L0.5 Die Zauberschule II: Reihungen als Parameter, Wert und Referenz    | L0.5                 | W0-07, W0-18, W0-19, W0-20                             |
| 6      | 2       | Die Methoden-Werkstatt: Von der Aufgabe zur Methode + Papier-Compiler 0 | Papier-Compiler 0    | W0-21, W0-22                                           |
| 7      | 3       | Boss-Kampf 0: Aufnahmeprüfung – Die Bibliothek der Akademie             | Papier-Compiler Boss | – (Boss-Training: W0-17, W0-18, W0-19, W0-21)          |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>DS-Rhythmus (in jeder regulären DS)</strong></p>
<p><strong>10' Papier-Kata</strong> (ohne Gerät) · <strong>15' Input / Unplugged</strong> · <strong>50' Online-IDE-Level</strong> (in DS 6: Papier-Werkstatt) · <strong>15' Sicherung</strong></p>
<p>Handschrift-Stufen: 1 Lesen/Tracen (DS 1–3) · 2 Lücken/Köpfe schreiben (DS 4–5) · 3 Papier-first „Papier-Compiler“ (DS 6) · 4 Abi auf Zeit (Boss 0, DS 7).</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Differenzierung: Die Diagnose aus DS 1 steuert die Pfade</strong></p>
<p>Die Vorkenntnisse aus der Einführungsphase sind erfahrungsgemäß sehr unterschiedlich. Level 0 „Diagnose“ (DS 1) ordnet jede Person einem Pfad zu; die Pfade bestimmen die Auswahl der Papier-Aufgaben und das Ziel-Level in DS 2–6. Ein Wechsel ist jederzeit möglich (Rückmeldung nach jeder DS).</p>
<table style="width:100%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 45%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Pfad</strong></th>
<th><strong>Diagnose (DS 1)</strong></th>
<th><strong>Vorgehen in DS 2–6</strong></th>
<th><strong>Rolle in der Gilde</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>A – Fundament</strong></td>
<td>Basis nicht vollständig grün</td>
<td>Infoteile mit der Lehrkraft, ★-Aufgaben, Level jeweils Basis (+ Erweiterung, wenn möglich); Tipps-Kästen und Übersetzungstabelle; Struktogramm vor dem Code</td>
<td>bekommt Mentor-Unterstützung</td>
</tr>
<tr class="even">
<td><strong>B – Standard</strong></td>
<td>Basis + Erweiterung grün</td>
<td>★★-Aufgaben, Level bis Erweiterung, Experte als Ziel; Bug-Hunts</td>
<td>arbeitet selbstständig</td>
</tr>
<tr class="odd">
<td><strong>C – Expertise</strong></td>
<td>alle drei Stufen grün</td>
<td>★★★-Aufgaben, Experte-Stufen, „Für Schnelle“ (Side-Quests 15–40 XP); Mentor-Aufträge</td>
<td>Mentor (+10 XP je Einsatz)</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>XP-System (fließt nicht in die Note ein; öffentlich nur die Gilden-Rangliste)</strong></p>
<ul>
<li><p>IDE-Level Basis / Erweiterung / Experte: 10 / 20 / 30 XP (Level 0.2–0.5 je bis 60 XP) · Papier-Kata korrekt: 5 XP · Papier-Aufgaben auf den ABs: je 5 XP · Papier-Compiler (Handschrift unverändert abgetippt, alle Tests grün): 30 XP, +10 beim ersten Versuch.</p></li>
<li><p>Boss-Kampf: 2 XP je erreichter BE · Side-Quest 15–40 · Mentor 10 · Bug-Bounty (Fehler im Material gefunden) 15.</p></li>
<li><p>Ränge: Novize → Lehrling → Geselle → Meister → Großmeister („abiturbereit“). Badges in Welt 0 v. a. Trace-Detektiv, Struktogramm-Architekt, Papier-Compiler (PC 0, Boss 0), Fehlerjäger (Boss 0), Mentor.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Vorbereitung Online-IDE (einmalig)**

- Auf online-ide.de eine Klasse für den Kurs anlegen; Lernende treten bei.

- Workspace Level 0 (AQ_W0_L0_Diagnose_Geruest.txt) und Workspace „AlgoQuest_W0_Akademie“ (AQ_W0_Akademie_Geruest.txt – **eine** Datei für Level 0.2 bis 0.5 und Papier-Compiler 0) über **„An Klasse austeilen“** verteilen. Die …\_LSG.txt-Dateien nicht austeilen.

- Testklassen der Akademie: L02WerkstattTest, L03VorratTest, L04ZauberTest, L05ZauberIITest, PapierCompiler0Test; Stufen an den Präfixen basis\_ / erweiterung\_ / experte\_. Im unbearbeiteten Gerüst ist keiner der 70 aktiven Tests grün; 19 Tests liegen in Freischalt-Blöcken.

- Freischalt-Blöcke: LEVEL-0.4-START/ENDE Erweiterung, LEVEL-0.4-START/ENDE Experte (je in L04ZauberTest und im Hauptprogramm) und PAPIER-COMPILER-0-START/ENDE (Testklasse und Hauptprogramm). Freischalten = die beiden Markerzeilen löschen.

- Online-IDE-Besonderheiten: println(...) ohne System.out; Anweisungen außerhalb von Klassen bilden das Hauptprogramm; **== vergleicht Zeichenketten inhaltlich** (anders als Java und Abitur) – im Unterricht konsequent equals verlangen.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Vor Einsatz prüfen</strong></p>
<ul>
<li><p>Freischalt-Blöcke (Testmethoden bzw. eine ganze Testklasse in Blockkommentaren) und Testrunner mit einem Lernenden-Account in der aktuellen IDE-Version durchspielen – auch, dass Tests nach dem Freischalten im Testrunner erscheinen.</p></li>
<li><p>Werkzeugkarten (AQ_Werkzeugkarten.docx) nennen als Rundungsweg (int) Math.round(x); in der Akademie ist Math.round bewusst tabu (Runden mit (int) (x + 0.5), AB 2 Infoteil 3). Karte ggf. anpassen oder im Unterricht kommentieren.</p></li>
<li><p>Input-Folien Welt0/AQ_W0_Akademie.pptx (DS 2–7) mit den ABs abgleichen (Beispiele, Notation „neue Reihung von Ganzzahl der Länge n“).</p></li>
<li><p>Kata-WebApp: Die Karten W0-09 bis W0-22 stehen in Werkzeuge/kata_w0_akademie.json; prüfen, ob sie in den WebApp-Seed übernommen sind (WebApp/seed enthält kata_w0_w1.json und kata_w2.json).</p></li>
<li><p>Bibliothek „niedersachsen“ (Stack, Queue, DynArray, BinTree) wird erst ab Welt 4 pro Workspace aktiviert – vermutlicher Menüpfad: Rechtsklick auf den Workspace → Einstellungen; vor Welt 4 prüfen.</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Dateien (Ausgabeordner AlgoQuest/)**

| **Datei**                                                         | **Inhalt**                                                                        | **DS**   |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|----------|
| Welt0/AQ_W0_Kickoff.pptx                                          | Kick-off-Folien (Story, XP, Abituraufgabe)                                        | 1        |
| Welt0/AQ_W0_AB_Portal.docx / …\_LSG.docx                          | AB 1 Portal: Teil A Start/Diagnose, Teil B Notations-Referenz                     | 1–2      |
| Welt0/AQ_W0_L0_Diagnose_Geruest.txt / …\_LSG.txt                  | Level 0 „Diagnose“                                                                | 1        |
| Welt0/AQ_W0_Akademie.pptx                                         | Input-Folien der Akademie                                                         | 2–7      |
| Welt0/AQ_W0_AB2_Werkstatt_Basics.docx / AQ_W0_AB2_LSG.docx        | AB 2 Werkstatt: Datentypen, Operatoren, Zufall/Runden, Verzweigung, Schleifen     | 2        |
| Welt0/AQ_W0_AB3_Vorratskammer_Reihungen.docx / AQ_W0_AB3_LSG.docx | AB 3 Vorratskammer: Reihungen, Referenz/Kopie, Zeichenketten                      | 3        |
| Welt0/AQ_W0_AB4_Zauberschule_Methoden.docx / AQ_W0_AB4_LSG.docx   | AB 4 Zauberschule: Teil 1 Methoden, Teil 2 Wert/Referenz, Hilfsmethoden           | 4–5      |
| Welt0/AQ_W0_AB5_Methoden-Werkstatt.docx / AQ_W0_AB5_LSG.docx      | AB 5 Methoden-Werkstatt: Rezept, Fehlergalerie, Papier-Compiler 0, Peer-Korrektur | 6        |
| Welt0/AQ_W0_Akademie_Geruest.txt / …\_LSG.txt                     | Level 0.2–0.5 und Papier-Compiler 0 (eine Datei)                                  | 2–6      |
| Welt0/AQ_W0_Boss0_Bibliothek.docx                                 | Boss-Kampf 0 (Aufgabenheft mit Antwortbogen)                                      | 7        |
| Welt0/AQ_W0_Boss0_Erwartungshorizont.docx                         | Erwartungshorizont, Bewertungsbogen, Papier-Compiler-Workspace                    | 7        |
| Werkzeuge/AQ_Werkzeugkarten.docx                                  | Abi-Check, Struktogramm-Spickblatt, Typnamen, Zeichenketten-Operationen, Vorlagen | ab 1     |
| Werkzeuge/AQ_Kata-Karten_W0-W1.docx / kata_w0_w1.json             | Kata W0-01 bis W0-08 (und Welt 1)                                                 | 2–5      |
| Werkzeuge/AQ_Kata-Karten_W0_Akademie.docx / kata_w0_akademie.json | Kata W0-09 bis W0-22                                                              | 2–6      |
| WebApp/                                                           | Kata-WebApp und XP-Verwaltung                                                     | optional |

**DS 1** Welt 0 – Die Akademie · Woche 1

**Kick-off: Das Portal öffnet sich + Level 0 „Diagnose“**

**Ziele**

- Die Lernenden kennen Story, Spielregeln (Gilden, XP, Ränge, Badges) und den DS-Rhythmus der Einheit und sehen an einer echten Block-1-Abituraufgabe, dass jede Implementierung eine Methode mit vorgegebener Signatur ist und von Hand geschrieben wird.

- Sie bilden feste, leistungsgemischte Gilden, richten Online-IDE und WebApp ein und führen ihren ersten JUnit-Test im Testrunner aus.

- Sie diagnostizieren ihren Stand aus der Einführungsphase (Level 0: Reihungen, Schleifen, Zeichenketten). Das Ergebnis legt den Pfad für DS 2–6 fest (Differenzierung, Tabelle in der Übersicht).

**Verlauf**

| **Phase**   | **Zeit** | **Inhalt / Ablauf**                                                                                                                                                                                                              | **Sozialform** | **Material / Datei**                                  | **XP**   |
|-------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------|----------|
| Papier-Kata | 10'      | „Das Rätsel am Portaltor“ (AB 1, Aufgabe 4) ohne Gerät; Auflösung im Plenum; Kata-Prinzip erklären (jede DS beginnt so, korrekt gelöst +5 XP).                                                                                   | EA → Plenum    | Welt0/AQ_W0_AB_Portal.docx (Aufgabe 4)                | +5       |
| Input       | 15'      | Kick-off-Folien: Story, Welten-Karte, Akademie als Welt 0, XP-/Rang-/Badge-System (XP nicht notenrelevant), echte Abituraufgabe „Implementieren Sie die Methode …“. Gilden gründen (AB 1, Aufgabe 1).                            | Plenum, GA     | Welt0/AQ_W0_Kickoff.pptx; AB 1 Teil A                 | –        |
| Online-IDE  | 50'      | WebApp-Login und IDE einrichten (AB 1, Aufgabe 2), erster Testlauf. Level 0 „Diagnose“ (AB 1, Aufgabe 3): Basis → Erweiterung → Experte, Fehlerlogbuch beginnen.                                                                 | EA in Gilden   | Welt0/AQ_W0_L0_Diagnose_Geruest.txt (LSG: …\_LSG.txt) | 10/20/30 |
| Sicherung   | 15'      | Diagnose-Check-in: Jede Person notiert, welche Stufen grün sind (Zettel/WebApp) → Lehrkraft ordnet Pfad A/B/C zu. Ausblick auf die Akademie (Werkstatt, Vorratskammer, Zauberschule, Aufnahmeprüfung); Werkzeugkarten austeilen. | EA → Plenum    | Werkzeuge/AQ_Werkzeugkarten.docx                      | –        |

**Hinweise**

*Typische Schwierigkeiten:*

- Erstes Einloggen und Workspace-Verteilung kosten Zeit – Klasse und Workspaces vorher anlegen und mit einem Test-Account prüfen.

- anzahlVokale: Griff zu toLowerCase – im Abitur nicht erlaubt; auf AB 1, Teil B (erlaubte Zeichenketten-Operationen) verweisen.

- durchschnitt: ganzzahlige Division und fehlende Leer-Abfrage – wird in DS 2 systematisch aufgegriffen.

*Differenzierung:*

- Die Diagnose ist die Grundlage der Pfade A/B/C (siehe Übersicht); Gilden so mischen, dass in jeder Gilde mindestens eine Person aus Pfad C sitzt (Mentor-Rolle, +10 XP).

- Wer Experte schafft: Debugger-Side-Quest (AB 1, Aufgabe 8) oder Mentor; wer an Basis scheitert: Struktogramm-Spickkarte, Lösungsweg mit der Lehrkraft.

*Vorbereitung:*

- Online-IDE: Klasse anlegen, Workspace Level 0 über „An Klasse austeilen“ verteilen; Testrunner einmal selbst ausführen.

- WebApp-Zugangszettel (Kurscode, PIN) drucken; Gilden vorläufig leistungsgemischt planen und nach der Diagnose ggf. anpassen.

- Diagnose-Übersicht (Name \| Basis \| Erweiterung \| Experte \| Pfad) für die eigene Planung vorbereiten.

**Kata-Karten**

Keine Kata-Karte – „Das Rätsel am Portaltor“ (AB 1, Aufgabe 4) ist die erste Kata.

**DS 2** Welt 0 – Die Akademie · Woche 1

**L0.2 Die Werkstatt: Datentypen, Operatoren, Verzweigungen, Schleifen**

**Ziele**

- Die Lernenden bestimmen Werte von Ausdrücken mit Ganzzahl- und Kommazahl-Division, %, Casts, Vergleichen und logischen Operatoren und kennen die Casting-Falle.

- Sie bilden ganzzahlige Zufallszahlen in einem Bereich und runden ganzzahlig ohne Math.round (EH 2025).

- Sie verfolgen Verzweigungsketten und Schleifen in Tracetabellen und übersetzen zwischen Java und Struktogramm nach EH § 5.

**Verlauf**

| **Phase**    | **Zeit** | **Inhalt / Ablauf**                                                                                                                                                                                                          | **Sozialform** | **Material / Datei**                                                                              | **XP**                 |
|--------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------|------------------------|
| Papier-Kata  | 10'      | Pfad A: Struktogramm lesen/übersetzen (W0-01/W0-02); Pfad B/C: Waage des Alchemisten oder Zahlenschloss (W0-09/W0-12).                                                                                                       | EA → PA        | Kata W0-01, W0-02, W0-03, W0-04, W0-09, W0-10, W0-11, W0-12 (eine wählen)                         | +5                     |
| Input        | 15'      | AB 2, Aufgabe 0 (Blitz-Kata „Was rechnet Java?“) als Vorhersage – Auflösung mit Infoteil 2; Casting-Falle und -7 % 2 live in der IDE; Zufallsformel aus dem Würfel herleiten (Infoteil 3); else-if-Reihenfolge an Aufgabe 4. | Plenum         | Welt0/AQ_W0_Akademie.pptx (DS 2); AB 2 Infoteile 1–4; AB 1 Teil B als Notations-Referenz          | –                      |
| Papier + IDE | 50'      | 20' Papier nach Pfad (A: Aufgaben 1, 2, 5 · B: 2–6 · C: 4, 6, Für Schnelle), danach 30' Level 0.2 in der Klasse Werkstatt (Testklasse L02WerkstattTest).                                                                     | EA in Gilden   | Welt0/AQ_W0_AB2_Werkstatt_Basics.docx (LSG: AQ_W0_AB2_LSG.docx); Welt0/AQ_W0_Akademie_Geruest.txt | Papier je +5; 10/20/30 |
| Sicherung    | 15'      | Bug-Hunt (Aufgabe 8) im Plenum; Wert-Rätsel aus dem Hauptprogramm („jahr bleibt 2026“) als Vorgriff auf DS 5; Rest der Papieraufgaben als Hausaufgabe.                                                                       | Plenum         | AB 2, Aufgabe 8                                                                                   | –                      |

**Hinweise**

*Typische Schwierigkeiten:*

- -3 % 2 ist −1 → n % 2 == 1 als Ungerade-Test ist falsch (Test basis_istGerade_negativ).

- (double) (summe / 3) castet zu spät; (int) Math.random() \* 6 liefert immer 0 bzw. 1.

- kistenBenoetigt ohne Math.ceil: viele addieren immer 1 – Test mit 10 / 5 zeigt den Fehler.

- else-if-Ketten in falscher Reihenfolge (Aufgabe 4); Struktogramm der Kette als Schachtelung im Falsch-Zweig.

*Differenzierung:*

- Pfad A (Diagnose-Basis unvollständig): Infoteile mit Lehrkraft, Aufgaben 1, 2, 5 und Level-0.2-Basis; Tipps-Kasten von Aufgabe 7 nutzen.

- Pfad B (Basis + Erweiterung grün): Aufgaben 2–6, Level 0.2 bis Erweiterung.

- Pfad C (alle Stufen grün): Aufgaben 4, 6 c–e und Experte (ggT, istPrimzahl, potenz), danach Für Schnelle oder Mentor.

*Vorbereitung:*

- Workspace „AlgoQuest_W0_Akademie“ mit AQ_W0_Akademie_Geruest.txt austeilen (eine Datei für DS 2–6); Bibliothek „niedersachsen“ ist **nicht** nötig.

- AB 1 Teil B (Notations-Referenz) mitbringen lassen; Karopapier für Struktogramme.

**Kata-Karten**

W0-01 Das Rätsel des Portalwächters · W0-02 Vom Code zum Bauplan · W0-03 Spurensuche im Portal · W0-04 Der kaputte Bauplan · W0-09 Die Waage des Alchemisten · W0-10 Die Sanduhr der Akademie · W0-11 Der Türsteher der Bibliothek · W0-12 Das Zahlenschloss

**DS 3** Welt 0 – Die Akademie · Woche 1

**L0.3 Die Vorratskammer: Reihungen und Zeichenketten**

**Ziele**

- Die Lernenden legen eindimensionale Reihungen an, greifen über Index und length zu und wählen begründet zwischen Zählschleife und for-each.

- Sie unterscheiden Referenz und Kopie (Speicherbild mit Pfeilen) und liefern neue Reihungen zurück, ohne das Original zu verändern.

- Sie bearbeiten Zeichenketten nur mit den erlaubten Operationen und ersetzen verbotene durch erlaubte.

**Verlauf**

| **Phase**         | **Zeit** | **Inhalt / Ablauf**                                                                                                                                                                                                   | **Sozialform** | **Material / Datei**                                                   | **XP**                 |
|-------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------|------------------------|
| Papier-Kata       | 10'      | Inventur (W0-13) oder Rückwärts durchs Portal (W0-05); Pfad C: Zwei Schilder, ein Regal (W0-14).                                                                                                                      | EA             | Kata W0-05, W0-06, W0-08, W0-13, W0-14, W0-15 (eine wählen)            | +5                     |
| Input / Unplugged | 15'      | Regal-Unplugged: Becher/Schuhkartons als Fächer mit Indexnummern, Klebezettel als Variablen, Schnur als Referenz. int\[\] b = a; = zweite Schnur zum selben Regal; echte Kopie = zweites Regal. Danach Infoteile 1–3. | Plenum         | Welt0/AQ_W0_Akademie.pptx (DS 3); AB 3 Infoteile                       | –                      |
| Papier + IDE      | 50'      | 15' Papier (Aufgaben 0–3, Pfad C zusätzlich 4), dann 35' Level 0.3 in der Klasse Vorrat (Testklasse L03VorratTest).                                                                                                   | EA in Gilden   | Welt0/AQ_W0_AB3_Vorratskammer_Reihungen.docx (LSG: AQ_W0_AB3_LSG.docx) | Papier je +5; 10/20/30 |
| Sicherung         | 15'      | Regal-Rätsel (Aufgabe 3): Speicherbild an der Tafel; Tabelle „erlaubt/verboten“ (Infoteil 5) mit Aufgabe 5 b/c; Referenz-Rätsel aus dem Hauptprogramm.                                                                | Plenum         | AB 3, Aufgaben 3 und 5                                                 | –                      |

**Hinweise**

*Typische Schwierigkeiten:*

- r.length vs. s.length(); letzter Index length - 1; r\[r.length\].

- for-each zum Verändern (verdopple) – ändert nur die Kopie x.

- int\[\] neu = r; als vermeintliche Kopie (umgedreht, verdreifacht); == bei Reihungen.

- Zeichen vs. Zeichenkette: charAt(i) == "e" kompiliert nicht; substring-Ende ausschließlich.

*Differenzierung:*

- Pfad A: Aufgaben 0–2, Level 0.3 Basis; Infoteil 2 (for oder for-each) mit Lehrkraft.

- Pfad B: Aufgaben 1–4, Level 0.3 bis Erweiterung.

- Pfad C: Aufgaben 3–5 und 7, Experte (ohneVokale, beginntMit), Für Schnelle (Reindrängler, Caesar).

*Vorbereitung:*

- Material für das Regal-Unplugged (5–6 Becher, Klebezettel, zwei Schnüre).

- AB 3 kopieren; Karopapier für Speicherbilder.

**Kata-Karten**

W0-05 Rückwärts durchs Portal · W0-06 Der Spiegelzauber · W0-08 Das Zählwerk des Portals · W0-13 Inventur in der Vorratskammer · W0-14 Zwei Schilder, ein Regal · W0-15 Die verbotenen Bücher

**DS 4** Welt 0 – Die Akademie · Woche 2

**L0.4 Die Zauberschule I: Eigene Methoden bauen und aufrufen**

**Ziele**

- Die Lernenden benennen die Bestandteile einer Methode und übersetzen sicher zwischen Abi-Signatur und Java-Methodenkopf (Typnamen, „nichts“ = void, Parameterreihenfolge).

- Sie unterscheiden Parameter und Argumente, verwenden Rückgabewerte und prüfen, ob jeder Ablauf ein return hat; sie kennen lokale Variablen und ihre Gültigkeit.

- Sie verfolgen Methodenaufrufe mit Hilfsmethode in einem Aufrufprotokoll und schreiben in Level 0.4 Methodenköpfe selbst (Freischalten der Stufen).

**Verlauf**

| **Phase**         | **Zeit** | **Inhalt / Ablauf**                                                                                                                                                                                                                                                                               | **Sozialform** | **Material / Datei**                                                                               | **XP**                 |
|-------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------|------------------------|
| Papier-Kata       | 10'      | Zauberformeln übersetzen (W0-16); Pfad C: Passt der Schlüssel ins Schloss? (W0-17).                                                                                                                                                                                                               | EA → PA        | Kata W0-16, W0-17                                                                                  | +5                     |
| Input / Unplugged | 15'      | Zauberformel-Unplugged: Eine Person „ist“ die Methode heilwert(stufe) mit Formelkarte; andere übergeben Argument-Zettel und erhalten einen Ergebnis-Zettel. Zweite Person spielt kannZaubern und ruft die erste auf → Aufrufprotokoll an der Tafel. Danach Infoteile 1–3 (Anatomie, Übersetzung). | Plenum         | Welt0/AQ_W0_Akademie.pptx (DS 4); AB 4 Teil 1                                                      | –                      |
| Papier → IDE      | 50'      | 15' Papier: Aufgaben 1–3 (Pfad A: 0, 1, 3). Dann Level 0.4: zuerst Köpfe auf Papier (Aufgabe 7 a), Basis in der IDE, Erweiterung/Experte nach Kopf-Schreiben freischalten (zwei Blöcke je Stufe).                                                                                                 | EA in Gilden   | Welt0/AQ_W0_AB4_Zauberschule_Methoden.docx (LSG: AQ_W0_AB4_LSG.docx); Klasse Zauber, L04ZauberTest | Papier je +5; 10/20/30 |
| Sicherung         | 15'      | Aufrufprotokoll Runen (Aufgabe 6) gemeinsam; Compiler-Detektiv (Aufgabe 4) als Blitzrunde; Freischalt-Probleme sammeln; Abi-Check für Methoden (Kasten am Ende von AB 4).                                                                                                                         | Plenum         | AB 4, Aufgaben 4 und 6                                                                             | –                      |

**Hinweise**

*Typische Schwierigkeiten:*

- Methodenkopf: Ganzzahl statt int, fehlender Rückgabetyp, int a, b, void bei Rückgabe – nach dem Freischalten zeigt der Compiler auf die **Testzeile**.

- Freischalten: nur /\* oder \*/ gelöscht, nur ein Block geöffnet; Tests verändert statt Kopf korrigiert.

- „missing return statement“ bei else-if-Ketten ohne letztes return; Aufruf aus dem Hauptprogramm ohne Klassennamen.

- kannZaubern rechnet neu statt manaKosten aufzurufen (Test merkt es nicht → Code-Review in der Gilde).

*Differenzierung:*

- Pfad A: Aufgaben 0, 1, 3; Level 0.4 Basis + Erweiterung mit Übersetzungstabelle; Lehrkraft prüft Köpfe vor dem Freischalten.

- Pfad B: Aufgaben 1–5; Level 0.4 vollständig.

- Pfad C: Aufgaben 2, 4, 6 und Experte; Für Schnelle (römische Zahlen, Kalender); Mentor beim Freischalten.

*Vorbereitung:*

- Formelkarten für das Unplugged (heilwert, manaKosten, kannZaubern) und Argument-/Ergebniszettel.

- Freischalten einmal selbst im Lernenden-Workspace durchspielen (beide Blöcke je Stufe, Hauptprogramm-Ausgabe prüfen).

**Kata-Karten**

W0-16 Zauberformeln übersetzen · W0-17 Passt der Schlüssel ins Schloss?

**DS 5** Welt 0 – Die Akademie · Woche 2

**L0.5 Die Zauberschule II: Reihungen als Parameter, Wert und Referenz**

**Ziele**

- Die Lernenden erklären die Wertübergabe: Ein int-Parameter ist eine Kopie, ein Reihungs-Parameter eine Kopie der Referenz; sie sagen Ausgaben vorher und begründen sie mit Speicherbildern.

- Sie unterscheiden in-place-Methoden (nichts) und Methoden, die eine neue Reihung liefern, und wählen den Rückgabetyp nach dem Aufgabentext.

- Sie zerlegen Probleme mit Hilfsmethoden und verwenden vorgegebene Methoden („darf verwendet werden“).

**Verlauf**

| **Phase**         | **Zeit** | **Inhalt / Ablauf**                                                                                                                                                                                        | **Sozialform** | **Material / Datei**                          | **XP**                 |
|-------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------|------------------------|
| Papier-Kata       | 10'      | Original oder Kopie? (W0-18); Pfad A: Die Spannweite des Portals (W0-07); Pfad C: Nur die geraden Runen (W0-20).                                                                                           | EA             | Kata W0-07, W0-18, W0-19, W0-20 (eine wählen) | +5                     |
| Input / Unplugged | 15'      | Regal-Unplugged aus DS 3 mit „Methodenraum“ (Kreidekreis): Beim Aufruf wird der Zettel mit der Zahl kopiert, bei Reihungen die Schnur verdoppelt. Die drei Fälle aus Infoteil 7 nachspielen; Merke-Kasten. | Plenum         | Welt0/AQ_W0_Akademie.pptx (DS 5); AB 4 Teil 2 | –                      |
| Papier + IDE      | 50'      | 10' Aufgabe 8 (Vorhersage, ohne Gerät), dann Level 0.5 in der Klasse ZauberII (L05ZauberIITest); Pfad C zusätzlich Aufgabe 10.                                                                             | EA in Gilden   | AB 4 Teil 2; Klasse ZauberII                  | Papier je +5; 10/20/30 |
| Sicherung         | 15'      | Speicherbilder zu Aufgabe 8 vergleichen; Aufgabe 9 (in-place oder neu) im Plenum; Bug-Hunt (Aufgabe 12) als Hausaufgabe.                                                                                   | Plenum         | AB 4, Aufgaben 8, 9, 12                       | –                      |

**Hinweise**

*Typische Schwierigkeiten:*

- r = new int\[…\] in der Methode „soll“ die Reihung leeren – wirkt nicht nach außen (basis_fuelle_ueberschreibt).

- erhoehteKopie mit int\[\] neu = r; – Ergebnis stimmt, Original verändert (Test prüft beides).

- zweitgroesster: Ein-Durchlauf-Version vergisst, das alte Maximum zu verschieben; Start mit 0.

- verschmelze: Rest-Schleifen vergessen; \|\| statt && in der Reißverschluss-Bedingung.

*Differenzierung:*

- Pfad A: Aufgabe 8 mit Speicherbild-Vorlage, Level 0.5 Basis + istImBereich/zaehleImBereich.

- Pfad B: Aufgaben 8, 9, Level 0.5 bis Erweiterung.

- Pfad C: Aufgaben 10 und 12, Experte (zweitgroesster, verschmelze – Vorbereitung Mergesort), Für Schnelle (Rotation, Anagramm).

*Vorbereitung:*

- Unplugged-Material aus DS 3 wiederverwenden; Kreide/Seil für den „Methodenraum“.

- Hauptprogramm-Ausgaben von Level 0.5 kennen (LSG-Datei), um Vorhersagen schnell zu prüfen.

**Kata-Karten**

W0-07 Die Spannweite des Portals · W0-18 Original oder Kopie? · W0-19 Würfelpunkte der Akademie · W0-20 Nur die geraden Runen

**DS 6** Welt 0 – Die Akademie · Woche 2

**Die Methoden-Werkstatt: Von der Aufgabe zur Methode + Papier-Compiler 0**

**Ziele**

- Die Lernenden wenden das Rezept „Aufgabentext → Signatur → Randfälle → Struktogramm → Java auf Papier → Abi-Check → Papier-Compiler“ an.

- Sie erkennen die zehn häufigsten Implementierungsfehler (Fehlergalerie) in fremdem und eigenem Code und korrigieren sie.

- Sie implementieren Methoden im Abitur-Format handschriftlich, prüfen sie mit dem Papier-Compiler und bewerten Lösungen anderer nach Kernpunkten.

**Verlauf**

| **Phase**   | **Zeit** | **Inhalt / Ablauf**                                                                                                                                                                                                       | **Sozialform**            | **Material / Datei**                                                                        | **XP**          |
|-------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------------------------------------------------------------------------|-----------------|
| Papier-Kata | 10'      | Der Compiler streikt (W0-21) – fehlender Rückgabepfad als Einstieg in die Fehlergalerie.                                                                                                                                  | EA → PA                   | Kata W0-21, W0-22                                                                           | +5              |
| Input       | 15'      | Rezept (Infoteil 1) am vorgemachten Beispiel laengsteSerie live durchgehen – besonders Schritt 3 (Serie am Ende!) und Schritt 6; Fehlergalerie überfliegen.                                                               | Plenum                    | Welt0/AQ_W0_Akademie.pptx (DS 6); AB 5 S. 1–5                                               | –               |
| Werkstatt   | 50'      | 8' Fehler-Bingo (Aufgabe 1) · 15' Papier-Compiler 0 von Hand (Aufgabe 2 a–d) · 5' abtippen, Freischalten, PapierCompiler0Test · 17' eine Wahlaufgabe (3, 4 oder 5) nach Rezept · 5' Lösungen gildenübergreifend tauschen. | EA (IDE nur zum Abtippen) | Welt0/AQ_W0_AB5_Methoden-Werkstatt.docx (LSG: AQ_W0_AB5_LSG.docx); Klasse Werkstattpruefung | 30 (+10); je +5 |
| Sicherung   | 15'      | Peer-Korrektur mit Kernpunkt-Bogen (Aufgabe 6) – Kernpunkt-Folie aus der LSG zeigen; Fehlerlogbuch ausfüllen. Boss-0-Ankündigung (Ablauf, Werkzeugkarten als einzige Hilfe); Boss-Training als Hausaufgabe.               | PA → EA                   | AB 5, Aufgabe 6 und Fehlerlogbuch; Kata W0-17, W0-18, W0-19, W0-21, W0-22                   | Mentor +10      |

**Hinweise**

*Typische Schwierigkeiten:*

- Papier-Compiler: ganzzahliger Durchschnitt fällt nur bei negativen Werten auf (Test durchschnittIstKommazahl); fehlende Leer-Abfrage bleibt wegen NaN grün – im Abitur trotzdem Abzug.

- Abtippen „mit Verbesserungen“ – Regel: unverändert, Korrektur erst nach dem ersten Testlauf (sonst kein +10).

- Peer-Korrektur zu großzügig: Nur Kernpunkte zählen; Alternativen mit der Lehrkraft klären.

*Differenzierung:*

- Pfad A: Wahlaufgabe 3 oder 5, Struktogramm vor dem Java-Code verpflichtend; Fehler-Bingo in PA.

- Pfad B: Wahlaufgabe nach Wahl, Zeitlimit 2,5 min pro BE.

- Pfad C: Aufgabe 4 (mit Hilfsmethode) und eine weitere als Boss-Training; Mentor bei der Peer-Korrektur.

*Vorbereitung:*

- Kernpunkt-Folie (LSG AB 5, letzte Tabelle) bereitlegen; Papier-Compiler-Ergebnisse direkt in der Stunde in der WebApp buchen.

- Prüfen, dass im Lernenden-Workspace die Klasse Werkstattpruefung leer ist und die beiden PAPIER-COMPILER-0-Blöcke noch auskommentiert sind.

**Kata-Karten**

W0-21 Der Compiler streikt · W0-22 Das Rezept der Akademie

**DS 7** Welt 0 – Die Akademie · Woche 3

**Boss-Kampf 0: Aufnahmeprüfung – Die Bibliothek der Akademie**

**Ziele**

- Die Lernenden übertragen Signatur-, Trace-, Wert/Referenz- und Implementierungswissen auf einen neuen Kontext (Bibliothek) unter Abiturbedingungen (60 min, handschriftlich, Operatoren, BE).

- Sie überprüfen ihre handschriftliche Implementierung mit dem Papier-Compiler.

- Sie bewerten Lösungen anderer anhand von Kernpunkten (Peer-Korrektur).

**Verlauf**

| **Phase**       | **Zeit** | **Inhalt / Ablauf**                                                                                                                                                             | **Sozialform** | **Material / Datei**                                        | **XP**   |
|-----------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------|----------|
| Start           | 2'       | Geräte weg, Werkzeugkarten auf den Tisch, Boss-Hefte austeilen.                                                                                                                 | Plenum         | Welt0/AQ_W0_Boss0_Bibliothek.docx                           | –        |
| Boss-Kampf      | 60'      | Bearbeitung a)–f) (24 BE, ≈ 2,5 min je BE) auf dem Antwortbogen im Heft.                                                                                                        | EA             | Boss-Heft; Werkzeugkarten                                   | 2 je BE  |
| Papier-Compiler | 13'      | Aufgabe e) unverändert in den Workspace „W0 Boss 0 – Papier-Compiler“ abtippen, BossTest starten (8 Tests), Ergebnis im Heft ankreuzen.                                         | EA (IDE)       | Workspace laut EH-Anhang (Klasse Bibliothek, BossTest)      | 30 (+10) |
| Peer-Korrektur  | 15'      | Hefte gildenübergreifend tauschen; a), b), d) nach den Kernpunkten des Erwartungshorizonts bewerten. c), e), f) korrigiert die Lehrkraft; XP-Vergabe in der Folgestunde (DS 8). | PA / GA        | Welt0/AQ_W0_Boss0_Erwartungshorizont.docx (Bewertungsbogen) | Badges   |

**Hinweise**

*Typische Schwierigkeiten:*

- Zeitmanagement: Viele verweilen zu lange bei a) – auf die BE-Angaben und das Zeitbudget hinweisen.

- b\) Aufrufprotokoll: lokale Variable s der Hilfsmethode wird nicht notiert bzw. bei sterne(0) falsch belegt.

- c\) Referenzfalle (jahresabschluss lenkt nur die lokale Referenz um); f) ganzzahlige Division wird übersehen, weil der Compiler nur den fehlenden Rückgabepfad meldet.

*Differenzierung:*

- Nachteilsausgleich wie in Klausuren; bei Bedarf Struktogramm statt Java in e) (Teilpunkte nach EH).

- Wer früher fertig ist: Abi-Check-Liste und Fehlerlogbuch auf die eigenen Antworten anwenden.

*Vorbereitung:*

- Boss-Hefte drucken; Papier-Compiler-Workspace mit Klasse Bibliothek (Gerüst aus dem EH-Anhang) und Testklasse BossTest anlegen und austeilen; einmal mit der Musterlösung testen (8/8 grün).

- Kernpunkt-Tabellen aus dem EH als Folie oder Ausdruck für die Peer-Korrektur.

**Kata-Karten**

Boss-Training (Hausaufgabe zwischen DS 6 und DS 7): W0-17 Passt der Schlüssel ins Schloss? · W0-18 Original oder Kopie? · W0-19 Würfelpunkte der Akademie · W0-21 Der Compiler streikt sowie W0-22 und die nicht gewählten Abi-Aufgaben von AB 5.

**Boss-0-Ablauf im Detail**

| **Teilaufgabe** | **Operator / Inhalt**                                                                                               | **BE** | **AFB I / II / III**    |
|-----------------|---------------------------------------------------------------------------------------------------------------------|--------|-------------------------|
| a\)             | Angeben, Benennen, Erläutern: Signaturen ↔ Java-Köpfe, Parameter und Argumente, Typprüfung                          | 4      | 2 / 2 / 0               |
| b\)             | Dokumentieren: Aufrufprotokoll sterneSumme mit Hilfsmethode sterne; Analysieren                                     | 4      | 1 / 3 / 0               |
| c\)             | Angeben, Begründen, Beurteilen: Wertübergabe und Referenz (eintragen, jahresabschluss)                              | 3      | 1 / 1 / 1               |
| d\)             | Entwickeln: Struktogramm indexMeistgeliehen (Leer-Abfrage, kleinster Index)                                         | 4      | 1 / 2 / 1               |
| e\)             | Implementieren: neueAuflage (neue Reihung passender Länge, Hilfsmethode)                                            | 5      | 1 / 3 / 1               |
| f\)             | Identifizieren, Erläutern: drei Fehler in durchschnitt (Rückgabepfad, Off-by-one, ganzzahlige Division) + Korrektur | 4      | 1 / 2 / 1               |
| Summe           | 60 min · 24 BE · 48 XP                                                                                              | 24     | 7 / 13 / 4 (29/54/17 %) |

- **Boss (60 min):** Bearbeitung ohne Gerät; nur Werkzeugkarten. Antwortbogen im Heft (Linien, Tracetabelle, Zeichenflächen).

- **Papier-Compiler (13 min):** e) unverändert abtippen → BossTest (8 Tests). Erster Versuch grün: 30 + 10 XP und Badge Papier-Compiler; nach Korrektur grün: 30 XP.

- **Peer-Korrektur (15 min):** Hefte gildenübergreifend tauschen, a), b), d) nach Kernpunkten bewerten (Kernpunkt-Tabellen im EH). Lehrkraft korrigiert c), e), f) und kontrolliert stichprobenartig.

- **Auswertung (DS 8):** XP = 2 × BE in die Gilden-Rangliste; Badge Fehlerjäger, wenn in e) und f) alle Leer- und Index-Abfragen und jeder Rückgabepfad korrekt sind. Häufige Fehler (Referenzfalle, ganzzahlige Division, fehlender Rückgabepfad) als Kata-Wiederholung in Welt 1 aufgreifen.
