'use strict';
// Plattform-Manifest nach dem Verbundvertrag (README Teil H, Vertrag v1): öffentlich unter GET /api/plattform.
// Das Portal liest es, um Plattformen zu verlinken, ihren Stand anzuzeigen und die Vertragsversion zu prüfen.

const VERTRAG = '1.0';
const PLATTFORM = {
  id: 'algoquest',
  name: 'Algo Quest',
  titel: 'Algo Quest – Das Dungeon der Datenstrukturen',
  themenfeld: 'Algorithmik und Datenstrukturen',
  kurs: 'Informatik eA (LK), Niedersachsen, Abitur ab 2027',
  beschreibung: 'Übungsplattform mit automatisch geprüften Aufgaben im Abitur-Stil: Java-Grundlagen, Klassen, Suchen und Sortieren, Rekursion, Stapel und Schlange, Bäume – mit Bossen, Trainingsplatz und Warm-up-Karten.',
  farbe: '#1F4E79'
};
const FAEHIGKEITEN = ['gast', 'themen', 'lehrkraft-materialien', 'boss', 'training', 'warmup', 'scoreboard', 'beamer', 'urkunden', 'fallen-profil'];

/**
 * @param {{inhalte: object, version: string, umgebung?: object}} opt
 */
function createManifest({ inhalte, version, umgebung = process.env }) {
  return function manifest(basis) {
    const welten = [...inhalte.katalog.welten.values()].sort((a, b) => a.nr - b.nr);
    const portal = umgebung.PORTAL_URL || null;
    const modus = ['lokal', 'portal', 'beides'].includes(umgebung.AUTH_MODUS) ? umgebung.AUTH_MODUS : 'lokal';
    return {
      vertrag: VERTRAG,
      ...PLATTFORM,
      id: umgebung.PLATTFORM_ID || PLATTFORM.id,
      version,
      basis: umgebung.PLATTFORM_URL || basis,
      icon: '/static/favicon.svg',
      urls: { start: '/', gast: '/gast', themen: '/themen', lehrkraft: '/lehrer', datenschutz: '/datenschutz', healthz: '/healthz', ssoStart: null },
      auth: { modus, portal, sso: false },
      umfang: {
        welten: welten.length,
        level: welten.reduce((s, w) => s + w.levels.length, 0),
        aufgaben: welten.reduce((s, w) => s + (w.aufgabenAnzahl || 0) + (w.boss ? w.boss.pool.length : 0), 0),
        bosse: welten.filter((w) => w.boss).length
      },
      welten: welten.map((w) => ({ nr: w.nr, titel: w.titel, farbe: w.farbe, level: w.levels.length })),
      faehigkeiten: FAEHIGKEITEN
    };
  };
}

module.exports = { createManifest, VERTRAG };
