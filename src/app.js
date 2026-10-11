'use strict';
const path = require('node:path');
const fs = require('node:fs');
const express = require('express');
const helmet = require('helmet');
const { openDatabase } = require('./db');
const { createServices } = require('./services');
const S = require('./security');
const { schuelerRoutes } = require('./routes/schueler');
const { lehrerRoutes } = require('./routes/lehrer');
const { adminRoutes } = require('./routes/admin');
const { gastRoutes } = require('./routes/gast');
const { createThemen } = require('./services/themen');
const { createLehrkraftMaterial, URL_LEHRKRAFT } = require('./services/lehrkraftMaterial');
const { createGast } = require('./services/gast');
const { createManifest } = require('./services/manifest');

const PUBLIC_DIR = path.join(__dirname, '..', 'public');
const ROOT_DIR = path.join(__dirname, '..');
const LEHRKRAFT_SESSION_MS = 8 * 3600 * 1000; // 8 Stunden
const SCHUELER_SESSION_MS = 30 * 24 * 3600 * 1000; // 30 Tage
const VERSION = require('../package.json').version;

/**
 * Express-App erzeugen.
 * @param {object} opts
 * @param {string} opts.dbFile            SQLite-Datei oder ':memory:'
 * @param {string} opts.sessionSecret     Geheimnis zum Signieren der Cookies
 * @param {string} [opts.adminEmail]      Superadmin-Login (Standard „admin“)
 * @param {string} [opts.adminPassword]   Superadmin-Passwort (leer = Superadmin-Login gesperrt)
 * @param {string|null} [opts.seedDir]    Ordner mit welten/*.json und kata/*.json
 * @param {string[]} [opts.weltDateien]   zusätzliche Welt-Dateien (Tests/Entwicklung)
 * @param {string|number|boolean} [opts.trustProxy]
 * @param {Function} [opts.log]
 * @param {Function} [opts.now]           Uhr (ms) – für Tests
 * @param {Function} [opts.random]        Zufall [0,1) für Boss-Ziehung – für Tests
 * @param {Function} [opts.trainingSeed]  Seed-Quelle für Generatoren – für Tests
 * @param {string|null} [opts.arbeitsblaetterDir] Ordner mit den Arbeitsblatt-PDFs (Standard: ARBEITSBLAETTER_DIR,
 *                                         sonst ./arbeitsblaetter im Image bzw. materialien/Arbeitsblaetter_PDF im Repo)
 * @param {string|null} [opts.materialienDir] Ordner mit Lehrkraft_PDF/ und Loesungen_Portal/ (nur Lehrkräfte;
 *                                         Standard: MATERIALIEN_DIR, sonst ./materialien)
 */
function createApp(opts) {
  const log = opts.log || (() => {});
  const db = openDatabase(opts.dbFile, { log });
  const ctx = { db, now: opts.now || (() => Date.now()), log, random: opts.random, trainingSeed: opts.trainingSeed };
  const svc = createServices(ctx);
  const secret = opts.sessionSecret;
  const superadminAktiv = !!opts.adminPassword;

  svc.konten.sichereSuperadmin(opts.adminEmail || 'admin', opts.adminPassword || '');
  ladeInhalte(svc, opts, log);
  const abDir = arbeitsblaetterOrdner(opts);
  const themen = createThemen(ctx, { inhalte: svc.inhalte }, {
    verzeichnis: ladeVerzeichnis(opts, log),
    pdfVorhanden: (datei) => !!abDir && fs.existsSync(path.join(abDir, datei))
  });
  const material = createLehrkraftMaterial({ materialienDir: materialienOrdner(opts), abDir, log });
  const gast = createGast(ctx, { datei: gastDatei(opts), inhalte: svc.inhalte, material, log });
  const manifest = createManifest({ inhalte: svc.inhalte, version: VERSION, umgebung: opts.umgebung || process.env });

  const app = express();
  app.disable('x-powered-by');
  app.set('trust proxy', opts.trustProxy ?? 1);

  app.use(
    helmet({
      contentSecurityPolicy: {
        useDefaults: true,
        directives: {
          'default-src': ["'self'"],
          'script-src': ["'self'"],
          'style-src': ["'self'"],
          'img-src': ["'self'", 'data:'],
          'connect-src': ["'self'"],
          'font-src': ["'self'"],
          'object-src': ["'none'"],
          'base-uri': ["'self'"],
          'form-action': ["'self'"],
          'frame-ancestors': ["'none'"],
          'upgrade-insecure-requests': null
        }
      },
      crossOriginEmbedderPolicy: false,
      referrerPolicy: { policy: 'same-origin' }
    })
  );
  // Schul-Werkzeug: nichts indexieren (Beamer-Board ausdrücklich noindex)
  app.use((req, res, next) => {
    res.set('X-Robots-Tag', 'noindex, nofollow');
    next();
  });

  /* ---------- Sitzungen lesen ---------- */
  app.use((req, res, next) => {
    const cookies = S.parseCookies(req.headers.cookie);
    req.sS = cookies[S.COOKIE_SCHUELER] ? S.verify(cookies[S.COOKIE_SCHUELER], secret) : null;
    req.sL = cookies[S.COOKIE_LEHRKRAFT] ? S.verify(cookies[S.COOKIE_LEHRKRAFT], secret) : null;
    next();
  });

  app.get('/healthz', (req, res) => {
    try {
      db.prepare('SELECT 1').get();
      res.json({ status: 'ok', version: VERSION });
    } catch {
      res.status(500).json({ status: 'error' });
    }
  });

  // Plattform-Manifest (Verbundvertrag, README Teil H) – öffentlich, auch für Browser des Portals lesbar
  app.get('/api/plattform', (req, res) => {
    res.set('Access-Control-Allow-Origin', '*');
    res.set('Cache-Control', 'public, max-age=300');
    res.json(manifest(`${req.protocol}://${req.get('host')}`));
  });

  app.get('/robots.txt', (req, res) => res.type('text').send('User-agent: *\nDisallow: /\n'));

  /* ---------- Seiten ---------- */
  const page = (file) => (req, res) => {
    res.set('Cache-Control', 'no-store');
    res.sendFile(path.join(PUBLIC_DIR, file));
  };
  app.get('/', page('index.html'));
  app.get('/k/:code', page('index.html'));
  app.get('/spiel', page('spiel.html'));
  app.get('/lehrer', page('lehrer.html'));
  app.get('/lehrer/urkunden', page('urkunden.html'));
  app.get('/admin', (req, res) => res.redirect('/lehrer#/admin'));
  app.get('/board/:code', page('board.html'));
  app.get('/datenschutz', page('datenschutz.html'));
  app.get('/themen', page('themen.html'));
  app.get('/gast', page('gast.html'));
  app.use('/static', express.static(path.join(PUBLIC_DIR, 'static'), { maxAge: '1h', index: false }));
  // Arbeitsblätter (Schülerfassung, PDF) – nur .pdf, ohne Verzeichnislisten
  if (abDir) {
    app.use('/arbeitsblaetter', (req, res, next) => (req.path.toLowerCase().endsWith('.pdf') ? next() : res.status(404).end()));
    app.use('/arbeitsblaetter', express.static(abDir, { maxAge: '1h', index: false, dotfiles: 'deny' }));
  }

  /* ---------- API ---------- */
  const api = express.Router();
  api.use(S.sameOriginCheck);
  api.use(express.json({ limit: '30mb' }));
  api.use((req, res, next) => {
    res.set('Cache-Control', 'no-store');
    next();
  });

  const helpers = {
    svc,
    secret,
    superadminAktiv,
    now: ctx.now,
    setSchuelerCookie: (req, res, row) => S.setCookie(req, res, S.COOKIE_SCHUELER, { s: row.id, g: row.session_gen }, secret, SCHUELER_SESSION_MS),
    setLehrkraftCookie: (req, res, row) => S.setCookie(req, res, S.COOKIE_LEHRKRAFT, { l: row.id, g: row.session_gen }, secret, LEHRKRAFT_SESSION_MS),
    clearSchueler: (req, res) => S.clearCookie(req, res, S.COOKIE_SCHUELER),
    clearLehrkraft: (req, res) => S.clearCookie(req, res, S.COOKIE_LEHRKRAFT),
    schueler: (req) => (req.sS && Number.isInteger(req.sS.s) ? svc.kurse.ausSession(req.sS.s, req.sS.g) : null),
    lehrkraft: (req) => (req.sL && Number.isInteger(req.sL.l) ? svc.konten.ausSession(req.sL.l, req.sL.g, { superadminAktiv }) : null),
    material,
    gast,
    reload: () => ladeInhalte(svc, opts, log),
    sichereAdmin: () => svc.konten.sichereSuperadmin(opts.adminEmail || 'admin', opts.adminPassword || '')
  };

  api.get('/sitzung', (req, res) => {
    const s = helpers.schueler(req);
    const l = helpers.lehrkraft(req);
    let schueler = null;
    if (s) {
      const k = svc.kurse.kursRow(s.kurs_id);
      schueler = { name: s.name, kurs: k ? k.name : '' };
    }
    res.json({ schueler, lehrkraft: l ? svc.konten.ansicht(l) : null, version: VERSION });
  });

  /* Öffentliche Themenübersicht (ohne Lösungen) */
  api.get('/themen', (req, res) => res.json(themen.uebersicht()));

  /* Öffentliches Beamer-Board (nur wenn im Kurs aktiviert) */
  api.get('/board/:code', (req, res) => {
    const b = svc.auswertung.board(req.params.code);
    if (!b) return res.status(404).json({ error: 'Kein Board für diesen Kurscode (oder im Kurs nicht aktiviert).' });
    res.json(b);
  });

  /* Lehrkraft-Downloads (Lösungen u. a.): nur angemeldete Lehrkräfte, nur verzeichnete Dateien – sonst 404 */
  app.get(URL_LEHRKRAFT.replace(/\/$/, '') + '/*datei', (req, res) => {
    const l = helpers.lehrkraft(req);
    const rel = [].concat(req.params.datei).join('/');
    const abs = l && !l.muss_pw_aendern ? material.datei(rel) : null;
    res.set('Cache-Control', 'private, no-store');
    if (!abs) return res.status(404).type('text').send('Nicht gefunden.');
    res.sendFile(abs);
  });

  schuelerRoutes(api, helpers);
  lehrerRoutes(api, helpers);
  adminRoutes(api, helpers);
  gastRoutes(api, helpers);

  api.use((req, res) => res.status(404).json({ error: 'Unbekannte API-Route.' }));
  app.use('/api', api);

  app.use((req, res) => res.status(404).sendFile(path.join(PUBLIC_DIR, '404.html')));

  // eslint-disable-next-line no-unused-vars
  app.use((err, req, res, next) => {
    if (err && err.type === 'entity.parse.failed') return res.status(400).json({ error: 'Ungültiges JSON.' });
    if (err && err.type === 'entity.too.large') return res.status(413).json({ error: 'Datei zu groß.' });
    const status = err && Number.isInteger(err.status) ? err.status : 500;
    if (status >= 500) log(err && err.stack ? err.stack : String(err));
    const body = { error: status >= 500 ? 'Interner Fehler.' : err.message };
    if (err && err.details) body.details = err.details;
    if (err && err.extra) Object.assign(body, err.extra);
    if (req.path.startsWith('/api/')) return res.status(status).json(body);
    res.status(status).type('text').send(body.error);
  });

  app.locals.db = db;
  app.locals.services = svc;
  app.locals.ctx = ctx;
  return app;
}

function arbeitsblaetterOrdner(opts) {
  if (opts.arbeitsblaetterDir !== undefined) return opts.arbeitsblaetterDir;
  const kandidaten = [process.env.ARBEITSBLAETTER_DIR, path.join(ROOT_DIR, 'arbeitsblaetter'), path.join(ROOT_DIR, 'materialien', 'Arbeitsblaetter_PDF')];
  return kandidaten.find((d) => d && fs.existsSync(d)) || null;
}

/** Demo-Aufgaben des Gastmodus: seedDir/gast/demo.json (opts.gastDatei überschreibt; null = kein Schüler-Gastmodus). */
function gastDatei(opts) {
  if (opts.gastDatei !== undefined) return opts.gastDatei;
  const seedDir = opts.seedDir === undefined ? path.join(ROOT_DIR, 'seed') : opts.seedDir;
  const repo = path.join(ROOT_DIR, 'seed', 'gast', 'demo.json');
  return (seedDir && fs.existsSync(path.join(seedDir, 'gast', 'demo.json')) && path.join(seedDir, 'gast', 'demo.json')) || (fs.existsSync(repo) ? repo : null);
}

function materialienOrdner(opts) {
  if (opts.materialienDir !== undefined) return opts.materialienDir;
  const kandidaten = [process.env.MATERIALIEN_DIR, path.join(ROOT_DIR, 'materialien')];
  return kandidaten.find((d) => d && fs.existsSync(d)) || null;
}

/** seedDir/arbeitsblaetter.json (Verzeichnis der Arbeitsblätter); fehlt sie, zeigt /themen nur die Level. */
function ladeVerzeichnis(opts, log) {
  const seedDir = opts.seedDir === undefined ? path.join(ROOT_DIR, 'seed') : opts.seedDir;
  const datei = seedDir && path.join(seedDir, 'arbeitsblaetter.json');
  if (!datei || !fs.existsSync(datei)) return null;
  try {
    return JSON.parse(fs.readFileSync(datei, 'utf8'));
  } catch (e) {
    log(`arbeitsblaetter.json nicht lesbar: ${e.message}`);
    return null;
  }
}

/** Seed: seedDir/welten/*.json (+ opts.weltDateien) und seedDir/kata/*.json. Fehler werden nur protokolliert. */
function ladeInhalte(svc, opts, log) {
  const lies = (dir) => {
    if (!dir || !fs.existsSync(dir)) return [];
    return fs
      .readdirSync(dir)
      .filter((f) => f.toLowerCase().endsWith('.json'))
      .sort()
      .map((f) => path.join(dir, f));
  };
  const quellen = (dateien) => {
    const out = [];
    for (const f of dateien) {
      try {
        out.push({ name: path.basename(f), text: fs.readFileSync(f, 'utf8') });
      } catch (e) {
        log(`Seed ${f} nicht lesbar: ${e.message}`);
      }
    }
    return out;
  };
  const seedDir = opts.seedDir === undefined ? path.join(__dirname, '..', 'seed') : opts.seedDir;
  const welten = [...lies(seedDir && path.join(seedDir, 'welten')), ...(opts.weltDateien || [])];
  let ergebnis = [];
  try {
    ergebnis = svc.inhalte.seedWelten(quellen(welten));
  } catch (e) {
    log(`Welt-Seed fehlgeschlagen: ${e.stack || e.message}`);
    svc.inhalte.lade();
  }
  for (const r of ergebnis) {
    if (r.status === 'übersprungen') log(`Welt-Seed ${r.datei}: ÜBERSPRUNGEN – ${r.fehler.slice(0, 5).join(' · ')}`);
    else if (r.status === 'geladen') log(`Welt-Seed ${r.datei}: ${r.aufgaben} Aufgaben geladen${r.ausgelassen ? `, ${r.ausgelassen} fehlerhafte ausgelassen` : ''}${r.fehler.length ? ` (${r.fehler.length} Fehler, z. B. ${r.fehler[0]})` : ''}.`);
  }
  const kata = svc.kata.seed(quellen(lies(seedDir && path.join(seedDir, 'warmup'))));
  for (const r of kata) {
    if (r.fehler) log(`Warm-up-Seed ${r.datei} fehlgeschlagen: ${r.fehler}`);
    else if (!r.uebersprungen) log(`Warm-up-Seed ${r.datei}: ${r.neu} neu, ${r.aktualisiert} aktualisiert.`);
  }
  return { welten: ergebnis, kata };
}

module.exports = { createApp, ladeInhalte, VERSION };
