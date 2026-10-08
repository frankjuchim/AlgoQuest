'use strict';
// Themenübersicht /themen: öffentlich, ohne Lösungen, Verweise auf Level und Arbeitsblatt-PDFs; PDF-Auslieferung.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const fs = require('node:fs');
const request = require('supertest');
const H = require('./helpers');

const SEED = path.join(__dirname, '..', 'seed');
const PDF_DIR = path.join(__dirname, '..', 'materialien', 'Arbeitsblaetter_PDF');

test('Themenübersicht: öffentlich, alle Welten und Level, keine Lösungen/Erklärungen/Tipps', async () => {
  const app = H.makeApp({ seedDir: SEED, weltDateien: [], arbeitsblaetterDir: PDF_DIR });
  const r = await request(app).get('/api/themen').expect(200);
  const d = r.body;
  assert.equal(d.welten.length, 7);
  const levels = d.welten.flatMap((w) => w.levels);
  assert.equal(levels.length, 36);
  const text = JSON.stringify(d);
  for (const verboten of ['"loesung"', '"erklaerung"', '"tipps"', '"inhalt"', '"interaktion"']) assert.ok(!text.includes(verboten), verboten);
  // Jedes Level ist einem Arbeitsblatt zugeordnet, und jedes Arbeitsblatt hat eine ausgelieferte PDF
  for (const l of levels) assert.ok(l.abBlatt && l.abBlatt.url, `Level ${l.id} ohne Arbeitsblatt (${l.ab})`);
  const abs = d.welten.flatMap((w) => w.arbeitsblaetter);
  assert.equal(abs.length, 20);
  for (const a of abs) assert.match(a.url, /^\/arbeitsblaetter\/Welt_\d_[A-Za-z]+\/AQ_W\d-AB\d_[A-Za-z0-9_-]+\.pdf$/);
  assert.ok(d.werkzeugkarten.url.endsWith('.pdf'));
  // Querschnitte: Kategorien und Fallen verweisen auf existierende Level
  const ids = new Set(levels.map((l) => l.id));
  for (const k of d.kategorien) for (const o of k.orte) assert.ok(ids.has(o.id));
  assert.equal(d.fallen.length, 10);
  assert.equal(d.fallen[0].p, 'P1');
  assert.ok(d.fallen.every((f) => f.anzahl > 0));
});

test('Arbeitsblatt-PDFs: werden ausgeliefert; Verzeichnisse, andere Dateien und Pfad-Tricks nicht', async () => {
  const app = H.makeApp({ seedDir: SEED, weltDateien: [], arbeitsblaetterDir: PDF_DIR });
  const d = (await request(app).get('/api/themen')).body;
  const url = d.welten[4].arbeitsblaetter[0].url;
  const r = await request(app).get(url).expect(200);
  assert.equal(r.headers['content-type'], 'application/pdf');
  assert.equal(r.body.subarray(0, 5).toString(), '%PDF-');
  await request(app).get('/arbeitsblaetter/').expect(404);
  await request(app).get('/arbeitsblaetter/Welt_4_Hafen/').expect(404);
  await request(app).get('/arbeitsblaetter/..%2f..%2fpackage.json').expect(404);
  await request(app).get('/arbeitsblaetter/%2e%2e/%2e%2e/seed/arbeitsblaetter.json').expect(404);
  await request(app).get('/themen').expect(200).expect('Content-Type', /html/);
});

test('Themenübersicht ohne Arbeitsblatt-Ordner: Level ja, PDF-Links leer', async () => {
  const app = H.makeApp({ seedDir: SEED, weltDateien: [], arbeitsblaetterDir: null });
  const d = (await request(app).get('/api/themen').expect(200)).body;
  assert.equal(d.welten.length, 7);
  assert.ok(d.welten.flatMap((w) => w.arbeitsblaetter).every((a) => a.url === null));
});

test('Verzeichnis seed/arbeitsblaetter.json passt zu den Quellen und den erzeugten PDFs', () => {
  const v = JSON.parse(fs.readFileSync(path.join(SEED, 'arbeitsblaetter.json'), 'utf8'));
  const mat = path.join(__dirname, '..', 'materialien');
  const alle = [v.werkzeugkarten, ...v.welten.flatMap((w) => w.arbeitsblaetter.map((a) => ({ ...a, datei: `${w.ordner}/${a.datei}` })))];
  for (const a of alle) {
    assert.ok(fs.existsSync(path.join(mat, a.quelle)), `Quelle fehlt: ${a.quelle}`);
    assert.ok(fs.existsSync(path.join(PDF_DIR, a.datei)), `PDF fehlt: ${a.datei} (python3 werkzeuge/arbeitsblaetter_pdf.py)`);
    assert.match(path.basename(a.datei), /^[A-Za-z0-9_.-]+$/, 'Dateiname ohne Umlaute und Leerzeichen');
  }
});
