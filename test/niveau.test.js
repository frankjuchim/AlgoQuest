'use strict';
// Niveau nach KC 2017 (Lernfeld Algorithmen und Datenstrukturen): alle · eA (nur LK) · plus (über den KC hinaus)
const { test } = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const H = require('./helpers');
const { validiereWelt } = require('../src/content/validator');

const SEED = path.join(__dirname, '..', 'seed');

test('Seed: alle Level der Welten 0–6 haben ein gültiges Niveau; eA-Themen laut KC sind markiert', () => {
  const fs = require('node:fs');
  const niveau = {};
  for (let w = 0; w <= 6; w++) {
    const d = JSON.parse(fs.readFileSync(path.join(SEED, 'welten', `welt${w}.json`), 'utf8'));
    for (const l of d.levels) {
      assert.ok(['alle', 'eA', 'plus'].includes(l.niveau), l.id);
      niveau[l.id] = l.niveau;
    }
    for (const a of d.aufgaben) if (a.kategorie === 'Effizienz' || a.kategorie === 'Rekursionstabelle') {
      const l = d.levels.find((x) => x.aufgaben.includes(a.id));
      const n = a.niveau || (l ? l.niveau : d.boss.niveau);
      assert.notEqual(n, 'alle', `${a.id}: ${a.kategorie} gehört zur Erweiterung eA`);
    }
  }
  // Rekursion (Welt 3) und Bäume (Welt 5) nur eA bzw. darüber hinaus; Grundlagen, Reihungen, Stapel/Schlange für alle
  for (const id of ['W3-L1', 'W3-L5', 'W5-L1', 'W5-L4', 'W1-L4', 'W2-L3']) assert.equal(niveau[id], 'eA', id);
  for (const id of ['W0-L1', 'W1-L1', 'W2-L1', 'W2-L2', 'W2-L4', 'W4-L1', 'W4-L4']) assert.equal(niveau[id], 'alle', id);
  for (const id of ['W3-L4', 'W5-L3']) assert.equal(niveau[id], 'plus', id);
});

test('Validator: ungültiges Niveau wird gemeldet', () => {
  const d = {
    version: 2, welt: 9, titel: 'T',
    levels: [{ id: 'W9-L1', titel: 'L', niveau: 'LK', aufgaben: ['W9-L1-01'] }],
    aufgaben: [{ id: 'W9-L1-01', titel: 'A', stufe: 1, kategorie: 'Datentypen und Ausdrücke', niveau: 'x', inhalt: [{ t: 'text', md: 'a' }], interaktion: { kind: 'choice', optionen: [{ id: 'a', md: 'a' }, { id: 'b', md: 'b' }] }, loesung: { richtig: ['a'] }, erklaerung: [{ t: 'text', md: 'a' }] }]
  };
  const f = validiereWelt(d, { datei: 't.json' }).fehler.map((x) => x.meldung).join(' | ');
  assert.match(f, /niveau muss alle \| eA \| plus/);
});

test('API: Niveau an Weltkarte, Level, Aufgabe und Themen; Kursart als Einstellung', async () => {
  const sz = await H.szenario({ seedDir: SEED, weltDateien: [] });
  const { s, lk, kurs, app } = sz;
  const w = (await s.get('/api/welten').expect(200)).body;
  assert.equal(w.kursart, 'eA');
  const w2 = w.welten.find((x) => x.nr === 2);
  assert.deepEqual(w2.levels.map((l) => l.niveau), ['alle', 'alle', 'eA', 'alle', 'eA']);
  assert.equal(w2.levels[3].gemischt, true); // 2.4: binäre Suche für alle, Effizienz-Aufgaben nur LK
  const l = (await s.get('/api/levels/W2-L4').expect(200)).body;
  assert.equal(l.level.niveau, 'alle');
  assert.equal(l.aufgaben.find((a) => a.id === 'W2-L4-04').niveau, 'eA');
  assert.equal(l.aufgaben.find((a) => a.id === 'W2-L4-01').niveau, 'alle');
  assert.equal((await s.get('/api/aufgaben/W2-L4-04').expect(200)).body.aufgabe.niveau, 'eA');
  const t = (await H.client(app).get('/api/themen').expect(200)).body;
  assert.equal(t.welten.find((x) => x.nr === 3).levels[0].niveau, 'eA');
  // Kursart
  assert.equal((await lk.patch(`/api/lehrer/kurse/${kurs.id}`).send({ einstellungen: { kursart: 'GK' } })).status, 400);
  const r = await lk.patch(`/api/lehrer/kurse/${kurs.id}`).send({ einstellungen: { kursart: 'gA' } }).expect(200);
  assert.equal(r.body.einstellungen.kursart, 'gA');
  assert.equal((await s.get('/api/welten')).body.kursart, 'gA');
  assert.equal((await s.get('/api/levels/W2-L4')).body.kursart, 'gA');
});

test('Grundkurs: Boss zieht nur Aufgaben für alle (Welt 2 ohne Effizienz-Aufgaben), Leistungskurs aus dem ganzen Pool', async () => {
  const app = H.makeApp({ seedDir: SEED, weltDateien: [] });
  const admin = await H.adminClient(app);
  const lk = await H.lehrkraftClient(app, admin);
  const kurs = await H.kursAnlegen(lk);
  await lk.patch(`/api/lehrer/kurse/${kurs.id}`).send({ einstellungen: { boss: 'offen', kursart: 'gA' } }).expect(200);
  const kat = app.locals.services.inhalte.katalog;
  const eaImPool = kat.welten.get(2).boss.pool.filter((id) => kat.aufgaben.get(id)._niveau !== 'alle');
  assert.ok(eaImPool.length >= 3);
  for (let i = 0; i < 6; i++) {
    const s = await H.schuelerClient(app, kurs.code, `Gast ${String.fromCharCode(65 + i)}.`);
    const k = (await s.post('/api/boss/2/start').send({}).expect(201)).body;
    const ids = k.aufgaben.map((a) => a.id);
    assert.ok(ids.length > 0);
    for (const id of ids) assert.ok(!eaImPool.includes(id), `${id} ist nur LK`);
  }
});
