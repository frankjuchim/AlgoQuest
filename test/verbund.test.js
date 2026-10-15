'use strict';
// Verbundvertrag (README Teil H): Plattform-Manifest unter /api/plattform.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const request = require('supertest');
const H = require('./helpers');
const { pruefeManifest } = require('../scripts/vertrag_pruefen');

const SEED = path.join(__dirname, '..', 'seed');

test('Manifest: öffentlich, vertragsgemäß, Version wie /healthz, CORS für das Portal', async () => {
  const app = H.makeApp({ seedDir: SEED, weltDateien: [] });
  const r = await request(app).get('/api/plattform').expect(200);
  assert.equal(r.headers['access-control-allow-origin'], '*');
  const m = r.body;
  assert.deepEqual(pruefeManifest(m), []);
  assert.equal(m.id, 'algoquest');
  assert.equal(m.vertrag, '1.3');
  assert.deepEqual(m.niveaus, ['eA', 'gA']);
  assert.match(m.kurs, /eA und gA/);
  assert.equal(m.urls.niveaus, '/themen#niveaus');
  assert.ok(!('ssoStart' in m.urls)); // ohne Portal kein SSO-Einstieg
  assert.equal(m.auth.modus, 'lokal');
  assert.equal(m.auth.sso, false);
  assert.equal(m.umfang.welten, 7);
  assert.ok(m.umfang.aufgaben > 300);
  const h = (await request(app).get('/healthz')).body;
  assert.equal(h.version, m.version);
  // keine Lösungen, keine Kurs- oder Schülerdaten
  const text = JSON.stringify(m);
  for (const v of ['loesung', 'kurscode', 'schueler', 'code"']) assert.ok(!text.toLowerCase().includes(v), v);
});

test('Manifest: Umgebung (PORTAL_URL, AUTH_MODUS, PLATTFORM_URL) wird übernommen', async () => {
  const app = H.makeApp({ seedDir: SEED, weltDateien: [], umgebung: { PORTAL_URL: 'https://portal.example', AUTH_MODUS: 'beides', PLATTFORM_URL: 'https://algoquest.example' } });
  const m = (await request(app).get('/api/plattform')).body;
  assert.equal(m.auth.portal, 'https://portal.example');
  assert.equal(m.auth.modus, 'beides');
  assert.equal(m.basis, 'https://algoquest.example');
});

test('pruefeManifest erkennt Vertragsverstöße', () => {
  assert.ok(pruefeManifest(null).length);
  const f = pruefeManifest({ vertrag: '2.0', id: 'Algo Quest', urls: { ssoStart: '//boese.example' }, auth: { modus: 'x', sso: true }, faehigkeiten: [] });
  for (const teil of ['vertrag', 'id:', 'urls.gast', 'auth.modus', 'urls.ssoStart', '"gast"']) assert.ok(f.some((x) => x.includes(teil)), teil);
});
