'use strict';
// Plattform-Verbund InfoLabs (VERTRAG.md v1.1 im Repo frankjuchim/labs, Phase 1):
//  - SSO: Konto aus dem geprüften Token übernehmen (Upsert nach sub), Kurse und Mitgliedschaften abgleichen
//  - Verbund-API: Löschen, Kursübersicht (nur Kennzahlen), Kurs umbenennen/sperren
// Portal-Kurse gehören dem Systemkonto „portal“; Zugriff haben die Lehrkräfte laut Token (kurs_lehrkraefte).
// Portal-Schüler haben je Kurs eine Zeile in „schueler“ (gleiche sub, kein persönlicher Code).

const V = require('../validate');
const { STANDARD_EINSTELLUNGEN } = require('../domain');

const SUB = /^[asl]:\d{1,15}$/;
const KURS_ID = /^k:\d{1,15}$/;

function createVerbund(ctx, { kurse, stand, inhalte }) {
  const { db } = ctx;
  const iso = () => new Date(ctx.now()).toISOString();

  /** Anzeigename aus dem Token: nach den Regeln für Schülernamen, sonst Ersatz. */
  function anzeigename(roh, ersatz) {
    try {
      return V.schuelerName(typeof roh === 'string' ? roh.slice(0, 30) : '');
    } catch {
      return { name: ersatz, key: ersatz.toLocaleLowerCase('de-DE') };
    }
  }

  /** Systemkonto, dem alle Portal-Kurse gehören (nicht anmeldbar). */
  function systemKonto() {
    const r = db.prepare("SELECT id FROM lehrkraefte WHERE sub = 'portal'").get();
    if (r) return r.id;
    return Number(
      db
        .prepare(
          "INSERT INTO lehrkraefte (email, name, schule, pw_hash, rolle, status, created_at, sub) VALUES ('portal@portal.invalid', 'InfoLabs', '', '!', 'lehrkraft', 'deaktiviert', ?, 'portal')"
        )
        .run(iso()).lastInsertRowid
    );
  }

  /** Portal-Kurs anlegen bzw. Namen aktualisieren. Liefert die Zeile. */
  function kursUpsert(k) {
    const name = typeof k.name === 'string' && k.name.trim() ? k.name.trim().slice(0, 80) : k.id;
    let r = db.prepare('SELECT * FROM kurse WHERE portal_id = ?').get(k.id);
    if (!r) {
      // Beitritt im Lab ist für Portal-Kurse gesperrt; der Kurscode dient nur dem Beamer-Board
      const e = { ...STANDARD_EINSTELLUNGEN, anmeldung: false };
      const info = db
        .prepare('INSERT INTO kurse (lehrkraft_id, name, code, einstellungen, created_at, portal_id) VALUES (?, ?, ?, ?, ?, ?)')
        .run(systemKonto(), name, kurse.neuerKursCode(), JSON.stringify(e), iso(), k.id);
      r = db.prepare('SELECT * FROM kurse WHERE id = ?').get(info.lastInsertRowid);
    } else if (r.name !== name) {
      db.prepare('UPDATE kurse SET name = ? WHERE id = ?').run(name, r.id);
      r.name = name;
    }
    return r;
  }

  /** Inhalt des Tokens prüfen (Signatur, iss, aud, Zeit, jti prüft der Aufrufer). */
  function pruefeInhalt(t) {
    if (!t || typeof t.sub !== 'string' || !SUB.test(t.sub)) return false;
    if (!['schueler', 'lehrkraft', 'superadmin'].includes(t.rolle)) return false;
    const praefix = { schueler: 's', lehrkraft: 'l', superadmin: 'a' }[t.rolle];
    if (t.sub[0] !== praefix) return false;
    if (!Array.isArray(t.kurse) || t.kurse.length > 500) return false;
    return t.kurse.every((k) => k && typeof k.id === 'string' && KURS_ID.test(k.id) && ['mitglied', 'lehrkraft'].includes(k.rolle));
  }

  /**
   * Lehrkraft bzw. Superadmin aus dem Token übernehmen. Liefert die Konto-Zeile oder { fehler }.
   */
  function lehrkraftAnmelden(t) {
    const rolle = t.rolle === 'superadmin' ? 'superadmin' : 'lehrkraft';
    const name = typeof t.name === 'string' && t.name.trim() ? t.name.trim().slice(0, 80) : rolle === 'superadmin' ? 'Superadmin' : 'Lehrkraft';
    return db.transaction(() => {
      let r = db.prepare('SELECT * FROM lehrkraefte WHERE sub = ?').get(t.sub);
      if (r && r.status === 'deaktiviert') return { fehler: 'deaktiviert' };
      if (!r) {
        const info = db
          .prepare("INSERT INTO lehrkraefte (email, name, schule, pw_hash, rolle, status, created_at, entschieden_at, sub) VALUES (?, ?, '', '!', ?, 'aktiv', ?, ?, ?)")
          .run(`${t.sub.replace(':', '-')}@portal.invalid`, name, rolle, iso(), iso(), t.sub);
        r = db.prepare('SELECT * FROM lehrkraefte WHERE id = ?').get(info.lastInsertRowid);
      } else {
        db.prepare("UPDATE lehrkraefte SET name = ?, rolle = ?, status = 'aktiv' WHERE id = ?").run(name, rolle, r.id);
      }
      // Kurse laut Token (Inhaberin und Mitlehrkraft); fehlende Kurse → kein Zugang mehr
      const ids = [];
      for (const k of t.kurse.filter((x) => x.rolle === 'lehrkraft')) {
        const kr = kursUpsert(k);
        ids.push(kr.id);
        db.prepare('INSERT OR IGNORE INTO kurs_lehrkraefte (kurs_id, lehrkraft_id) VALUES (?, ?)').run(kr.id, r.id);
      }
      const alt = db.prepare('SELECT kurs_id FROM kurs_lehrkraefte WHERE lehrkraft_id = ?').all(r.id);
      for (const a of alt) if (!ids.includes(a.kurs_id)) db.prepare('DELETE FROM kurs_lehrkraefte WHERE kurs_id = ? AND lehrkraft_id = ?').run(a.kurs_id, r.id);
      db.prepare('UPDATE lehrkraefte SET last_login_at = ? WHERE id = ?').run(iso(), r.id);
      return db.prepare('SELECT * FROM lehrkraefte WHERE id = ?').get(r.id);
    })();
  }

  /**
   * Schüler aus dem Token übernehmen: je Kurs eine Zeile (gleiche sub). Liefert die Zeile, mit der die Sitzung
   * beginnt (zuletzt aktiver zugänglicher Kurs bzw. der gewünschte), oder { fehler }.
   */
  function schuelerAnmelden(t, { kursWunsch } = {}) {
    const { name, key } = anzeigename(t.name, 'Schüler');
    return db.transaction(() => {
      const ids = [];
      for (const k of t.kurse.filter((x) => x.rolle === 'mitglied')) {
        const kr = kursUpsert(k);
        ids.push(kr.id);
        const r = db.prepare('SELECT * FROM schueler WHERE kurs_id = ? AND sub = ?').get(kr.id, t.sub);
        const n = freierName(kr.id, name, key, r ? r.id : null);
        if (!r) {
          db.prepare("INSERT INTO schueler (kurs_id, name, name_key, code, created_at, sub, zugang) VALUES (?, ?, ?, '', ?, ?, 1)").run(kr.id, n.name, n.key, iso(), t.sub);
        } else {
          db.prepare('UPDATE schueler SET name = ?, name_key = ?, zugang = 1 WHERE id = ?').run(n.name, n.key, r.id);
        }
      }
      db.prepare(`UPDATE schueler SET zugang = 0 WHERE sub = ? AND kurs_id NOT IN (${ids.map(() => '?').join(',') || 'NULL'})`).run(t.sub, ...ids);
      const zeilen = zugaenglich(t.sub);
      if (!zeilen.length) return { fehler: ids.length ? 'gesperrt' : 'keine_berechtigung' };
      const wunsch = kursWunsch ? zeilen.find((z) => z.portal_id === kursWunsch) : null;
      const r = wunsch || zeilen[0];
      db.prepare('UPDATE schueler SET last_active_at = ? WHERE id = ?').run(iso(), r.id);
      return db.prepare('SELECT * FROM schueler WHERE id = ?').get(r.id);
    })();
  }

  /** Name im Kurs eindeutig machen (UNIQUE kurs_id, name_key): „Lena S.“, „Lena S. 2“ … */
  function freierName(kursId, name, key, eigeneId) {
    const belegt = db.prepare('SELECT 1 FROM schueler WHERE kurs_id = ? AND name_key = ? AND id IS NOT ?');
    if (!belegt.get(kursId, key, eigeneId)) return { name, key };
    for (let i = 2; i < 1000; i++) {
      const n = `${name.slice(0, 26)} ${i}`;
      const k = n.toLocaleLowerCase('de-DE');
      if (!belegt.get(kursId, k, eigeneId)) return { name: n, key: k };
    }
    throw new Error('Kein freier Name.');
  }

  /** Zeilen eines Portal-Schülers in zugänglichen, nicht gesperrten Kursen (zuletzt aktiv zuerst). */
  function zugaenglich(sub) {
    return db
      .prepare(
        `SELECT s.*, k.name AS kurs_name, k.portal_id FROM schueler s JOIN kurse k ON k.id = s.kurs_id
         WHERE s.sub = ? AND s.zugang = 1 AND k.aktiv = 1 ORDER BY COALESCE(s.last_active_at, s.created_at) DESC, s.id DESC`
      )
      .all(sub);
  }

  /** Kurse eines angemeldeten Portal-Schülers (für den Kurswechsel). */
  function kurseVon(schuelerRow) {
    if (!schuelerRow.sub) return [];
    return zugaenglich(schuelerRow.sub).map((z) => ({ id: z.kurs_id, name: z.kurs_name, aktuell: z.id === schuelerRow.id }));
  }

  /** Kurs wechseln: Zeile derselben sub im gewünschten Kurs. */
  function kursWechseln(schuelerRow, kursId) {
    if (!schuelerRow.sub) throw new V.ForbiddenError('Nur für Anmeldungen über das Portal.');
    const z = zugaenglich(schuelerRow.sub).find((x) => x.kurs_id === kursId);
    if (!z) throw new V.NotFoundError('Kurs nicht gefunden.');
    db.prepare('UPDATE schueler SET last_active_at = ? WHERE id = ?').run(iso(), z.id);
    return db.prepare('SELECT * FROM schueler WHERE id = ?').get(z.id);
  }

  /* ---------- Verbund-API ---------- */

  /** Alle Daten eines Kontos (sub) bzw. eines Kurses (Kurs-ID) löschen. Idempotent. */
  function loeschen(b) {
    if (b && typeof b.sub === 'string') {
      if (!SUB.test(b.sub)) throw new V.ValidationError('sub ungültig.');
      return db.transaction(() => {
        let n = db.prepare('DELETE FROM schueler WHERE sub = ?').run(b.sub).changes;
        n += db.prepare('DELETE FROM lehrkraefte WHERE sub = ?').run(b.sub).changes;
        return n;
      })();
    }
    if (b && typeof b.kurs === 'string') {
      if (!KURS_ID.test(b.kurs)) throw new V.ValidationError('kurs ungültig.');
      return db.prepare('DELETE FROM kurse WHERE portal_id = ?').run(b.kurs).changes;
    }
    throw new V.ValidationError('sub oder kurs fehlt.');
  }

  /** Kennzahlen eines Portal-Kurses (keine Antworten, Lösungen oder Freitexte). null = unbekannt. */
  function uebersicht(kursId) {
    if (typeof kursId !== 'string' || !KURS_ID.test(kursId)) return null;
    const kr = db.prepare('SELECT * FROM kurse WHERE portal_id = ?').get(kursId);
    if (!kr) return null;
    const einst = kurse.einstellungen(kr.einstellungen);
    const welten = [...inhalte.katalog.welten.values()].filter((w) => einst.welten.includes(w.nr)).sort((a, b) => a.nr - b.nr);
    const max = welten.reduce((s, w) => s + w.maxPunkte, 0);
    const st = [...stand.staende(kr.id).values()].filter((e) => e.row.sub);
    const schueler = st.map((e) => {
      const ist = welten.reduce((s, w) => s + (e.level[w.nr] || 0), 0);
      return {
        sub: e.row.sub,
        punkte: e.gesamt,
        geloest: e.geloest,
        anteil: max ? Math.round(Math.min(1, ist / max) * 100) / 100 : 0,
        zuletzt: e.row.last_active_at || null
      };
    });
    return {
      kurs: kursId,
      stand: iso(),
      schueler,
      welten: welten.map((w) => ({
        nr: w.nr,
        titel: w.titel,
        anteil: st.length && w.maxPunkte ? Math.round((st.reduce((s, e) => s + Math.min(1, (e.level[w.nr] || 0) / w.maxPunkte), 0) / st.length) * 100) / 100 : 0
      }))
    };
  }

  /** Kurs umbenennen bzw. sperren/entsperren. Unbekannte Kurse werden bei der nächsten Anmeldung angelegt. */
  function kursAendern(kursId, b) {
    if (typeof kursId !== 'string' || !KURS_ID.test(kursId)) throw new V.ValidationError('Kurs-ID ungültig.');
    const body = b || {};
    const kr = db.prepare('SELECT * FROM kurse WHERE portal_id = ?').get(kursId);
    if (!kr) return { ok: true };
    if (typeof body.name === 'string' && body.name.trim()) db.prepare('UPDATE kurse SET name = ? WHERE id = ?').run(body.name.trim().slice(0, 80), kr.id);
    if (typeof body.aktiv === 'boolean') db.prepare('UPDATE kurse SET aktiv = ? WHERE id = ?').run(body.aktiv ? 1 : 0, kr.id);
    return { ok: true };
  }

  return { pruefeInhalt, lehrkraftAnmelden, schuelerAnmelden, kurseVon, kursWechseln, loeschen, uebersicht, kursAendern };
}

module.exports = { createVerbund, SUB, KURS_ID };
