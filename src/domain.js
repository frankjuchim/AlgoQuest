'use strict';
// Fachliche Konstanten (SPEC_AlgoLab §2–§8): Welten, Kategorien, Fallen, Ränge, Abzeichen-Grundlagen.

/** Standardwerte je Welt (werden von den Welt-Dateien überschrieben, falls dort titel/farbe gesetzt sind). */
const WELTEN = [
  { nr: 0, name: 'Akademie', titel: 'Die Akademie', farbe: '#7F6000' },
  { nr: 1, name: 'Heldenschmiede', titel: 'Die Heldenschmiede', farbe: '#C55A11' },
  { nr: 2, name: 'Rangliste', titel: 'Die Rangliste', farbe: '#7030A0' },
  { nr: 3, name: 'Labyrinth', titel: 'Das Labyrinth', farbe: '#375623' },
  { nr: 4, name: 'Hafen', titel: 'Der Hafen', farbe: '#2E75B6' },
  { nr: 5, name: 'Wald', titel: 'Der Wald', farbe: '#548235' },
  { nr: 6, name: 'Endgegner', titel: 'Der Endgegner', farbe: '#C00000' }
];
const WELT_MAP = Object.fromEntries(WELTEN.map((w) => [w.nr, w]));

/** LAB_KATEGORIEN (SPEC §3) – genau diese Schreibweise. */
const LAB_KATEGORIEN = [
  'Datentypen und Ausdrücke',
  'Methodenkopf und Signatur',
  'Klasse vs. Objekt',
  'Bestandteile einer Klasse',
  'Objektkarten und Referenzen',
  'Klassendiagramm',
  'Struktogramm lesen',
  'Code ↔ Struktogramm',
  'Tracetabelle',
  'Rekursionstabelle',
  'Fehler im Java-Code',
  'Fehler im Struktogramm',
  'Lückencode',
  'Methode implementieren',
  'ADT-Befehlsfolgen',
  'Sortieren und Suchen',
  'Effizienz',
  'Bäume',
  'Funktionsweise erläutern'
];

/** Kategorien der Kata-Karten (v1-Liste + Lab-Kategorien, damit alle Seed-Dateien importierbar sind). */
const KATA_KATEGORIEN = [
  ...new Set([
    'Klasse vs. Objekt',
    'Bestandteile einer Klasse',
    'Objektkarten und Referenzen',
    'Klassendiagramm',
    'Struktogramm lesen',
    'Code ↔ Struktogramm',
    'Tracetabelle',
    'Fehler im Java-Code',
    'Fehler im Struktogramm',
    'Lückencode',
    'Methode implementieren',
    'Verändern und Erweitern',
    'Funktionsweise erläutern',
    'Methodenkopf und Signatur',
    ...LAB_KATEGORIEN
  ])
];

/** Top 10 Punktverluste (SPEC_AlgoQuest_W6 §2). */
const FALLEN = [
  { p: 'P1', titel: 'Laufzeitfehler nicht ausgeschlossen', text: 'isEmpty vor top/pop/head/dequeue/getItem/getLeft; Indexgrenzen 0 … getLength()−1' },
  { p: 'P2', titel: 'Struktur zerstört statt unverändert', text: 'Stapel/Schlange nach dem Durchlauf nicht wiederhergestellt, obwohl gefordert' },
  { p: 'P3', titel: 'Signatur verfehlt', text: 'Rückgabetyp, Parameter, Name, static/Sichtbarkeit; Rückgabe fehlt auf einem Pfad' },
  { p: 'P4', titel: 'Typen und Casts', text: '(Integer) vergessen, Zeichen vs. Zeichenkette, ganzzahlige Division' },
  { p: 'P5', titel: 'Zeichenketten mit == statt equals', text: 'nicht erlaubte String-Operationen' },
  { p: 'P6', titel: 'Off-by-one', text: '< statt <=, getLength() statt getLength()−1, Startindex' },
  { p: 'P7', titel: 'Rekursion', text: 'Basisfall fehlt/falsch, Ergebnis des rekursiven Aufrufs nicht verwendet, Rekursionstiefe falsch (Erstaufruf = 0)' },
  { p: 'P8', titel: 'Trace-/Dokumentationstabelle unvollständig', text: 'vorgegebene Spalten, jede Wertänderung, Endwerte' },
  { p: 'P9', titel: 'Struktogramm nicht nach EH §5', text: '←, „gib … zurück“, Schleifenarten, Fallunterscheidung; Java-Syntax im Struktogramm' },
  { p: 'P10', titel: 'Operator verfehlt', text: '„erläutern“ als bloße Nennung, „begründen“ ohne Begründung, kein Bezug zum Material, Fachbegriffe fehlen' }
];
const FALLEN_IDS = FALLEN.map((f) => f.p);

/** Ränge: Anteil der erreichbaren Level-Punkte aller freigeschalteten Welten. */
const RAENGE = [
  { name: 'Novize', ab: 0 },
  { name: 'Lehrling', ab: 0.1 },
  { name: 'Geselle', ab: 0.3 },
  { name: 'Meister', ab: 0.55 },
  { name: 'Großmeister', ab: 0.8 }
];

function rangFuer(anteil) {
  let idx = 0;
  for (let i = 0; i < RAENGE.length; i++) if (anteil >= RAENGE[i].ab - 1e-9) idx = i;
  const next = RAENGE[idx + 1] || null;
  return {
    name: RAENGE[idx].name,
    index: idx,
    anteil,
    naechster: next ? { name: next.name, ab: next.ab } : null
  };
}

/** Standardpunkte je Stufe. */
const STUFEN_PUNKTE = { 1: 10, 2: 20, 3: 30 };

/** Punkteformel (SPEC §5): beim ersten Lösen. */
function punkteFuer(punkte, fehlversuche, tipps) {
  const faktor = Math.max(0.25, 1 - 0.25 * fehlversuche - 0.2 * tipps);
  return Math.round(punkte * faktor);
}

/** Kurseinstellungen (Standard). */
const STANDARD_EINSTELLUNGEN = {
  welten: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], // alle (auch spätere Zusatzwelten)
  boss: 'auto', // auto | gesperrt | offen
  scoreboard: true,
  beamer: false,
  anmeldung: true
};

const BOSS_AUTO_ANTEIL = 0.6;
const BOSS_BESIEGT_ANTEIL = 0.5;
const BOSS_SPERRE_MS = 12 * 3600 * 1000;
const BOSS_KULANZ_MS = 30 * 1000;
const TRAINING_MAX_PUNKTE_TAG = 30;

/** Leitner: Wartezeit in Tagen je Fach (1..5). */
const LEITNER_INTERVAL_DAYS = { 1: 0, 2: 1, 3: 3, 4: 7, 5: 14 };

module.exports = {
  WELTEN,
  WELT_MAP,
  LAB_KATEGORIEN,
  KATA_KATEGORIEN,
  FALLEN,
  FALLEN_IDS,
  RAENGE,
  rangFuer,
  STUFEN_PUNKTE,
  punkteFuer,
  STANDARD_EINSTELLUNGEN,
  BOSS_AUTO_ANTEIL,
  BOSS_BESIEGT_ANTEIL,
  BOSS_SPERRE_MS,
  BOSS_KULANZ_MS,
  TRAINING_MAX_PUNKTE_TAG,
  LEITNER_INTERVAL_DAYS
};
