/* Algo Quest Lab – gemeinsame Hilfsfunktionen (kein Build, Vanilla JS, keine Inline-Skripte) */
'use strict';

const AQ = (() => {
  const SVG_NS = 'http://www.w3.org/2000/svg';

  /** DOM-Element erzeugen – Texte werden immer als Textknoten eingefügt (XSS-sicher). */
  function h(tag, attrs, ...children) {
    const el = document.createElement(tag);
    setAttrs(el, attrs);
    appendAll(el, children);
    return el;
  }

  /** SVG-Element erzeugen. */
  function s(tag, attrs, ...children) {
    const el = document.createElementNS(SVG_NS, tag);
    setAttrs(el, attrs);
    appendAll(el, children);
    return el;
  }

  function setAttrs(el, attrs) {
    if (!attrs) return;
    for (const [k, v] of Object.entries(attrs)) {
      if (v === null || v === undefined || v === false) continue;
      if (k === 'class') el.setAttribute('class', v);
      else if (k === 'style' && typeof v === 'object') {
        for (const [sk, sv] of Object.entries(v)) {
          if (sk.startsWith('--')) el.style.setProperty(sk, sv);
          else el.style[sk] = sv;
        }
      } else if (k === 'dataset') Object.assign(el.dataset, v);
      else if (k.startsWith('on') && typeof v === 'function') el.addEventListener(k.slice(2), v);
      else if (k === 'value') el.value = v;
      else if (k === 'checked' || k === 'selected' || k === 'disabled') el[k] = !!v;
      else el.setAttribute(k, v === true ? '' : String(v));
    }
  }

  function appendAll(el, children) {
    for (const c of children.flat(Infinity)) {
      if (c === null || c === undefined || c === false) continue;
      el.appendChild(c instanceof Node ? c : document.createTextNode(String(c)));
    }
  }

  function clear(el) {
    while (el.firstChild) el.removeChild(el.firstChild);
    return el;
  }

  function mount(el, ...children) {
    clear(el);
    appendAll(el, children);
    return el;
  }

  async function api(method, url, body) {
    const opts = { method, headers: { Accept: 'application/json' }, credentials: 'same-origin' };
    if (body !== undefined) {
      opts.headers['Content-Type'] = 'application/json';
      opts.body = JSON.stringify(body);
    }
    let res;
    try {
      res = await fetch(url, opts);
    } catch {
      const e = new Error('Keine Verbindung zum Server. Bitte prüfe das Netzwerk.');
      e.status = 0;
      throw e;
    }
    let data = null;
    const ct = res.headers.get('content-type') || '';
    if (ct.includes('application/json')) data = await res.json();
    if (!res.ok) {
      const err = new Error((data && data.error) || `Fehler ${res.status}`);
      err.status = res.status;
      err.data = data;
      err.details = data && data.details;
      throw err;
    }
    return data;
  }

  let toastTimer;
  function toast(msg, art = '') {
    let t = document.getElementById('toast');
    if (!t) {
      t = h('div', { id: 'toast', role: 'status', 'aria-live': 'polite' });
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.className = art === true ? 'err' : art || '';
    t.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => (t.hidden = true), art === true || art === 'err' ? 6000 : 3500);
  }

  function fmtDatum(iso) {
    if (!iso) return '–';
    const d = new Date(iso);
    if (Number.isNaN(d.getTime())) return iso;
    return d.toLocaleDateString('de-DE') + ' ' + d.toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' });
  }

  function progress(fraction, cls = '') {
    const pct = Math.round(Math.max(0, Math.min(1, fraction || 0)) * 100);
    return h('div', { class: 'progress ' + cls, role: 'progressbar', 'aria-valuenow': pct, 'aria-valuemin': 0, 'aria-valuemax': 100, 'aria-label': `${pct} Prozent` }, h('span', { style: { width: pct + '%' } }));
  }

  function prozent(x) {
    return Math.round((x || 0) * 100) + ' %';
  }

  function sterne(stufe) {
    return h('span', { class: 'sterne', 'aria-label': `Stufe ${stufe}`, title: `Stufe ${stufe}` }, '★'.repeat(stufe) + '☆'.repeat(Math.max(0, 3 - stufe)));
  }

  /** Bestätigungsdialog (Promise<boolean>). */
  function bestaetigen(titel, text, { ok = 'OK', abbrechen = 'Abbrechen', gefahr = false, eingabe = null } = {}) {
    return new Promise((resolve) => {
      const feld = eingabe ? h('input', { type: 'text', 'aria-label': eingabe.label || 'Bestätigung', autocomplete: 'off', placeholder: eingabe.platzhalter || '' }) : null;
      const okBtn = h('button', { class: 'btn ' + (gefahr ? 'danger' : ''), type: 'button' }, ok);
      const d = h(
        'dialog',
        { 'aria-labelledby': 'dlg-titel' },
        h('h2', { id: 'dlg-titel' }, titel),
        typeof text === 'string' ? h('p', null, text) : text,
        feld ? h('div', { class: 'field' }, h('label', null, eingabe.label), feld) : null,
        h('div', { class: 'btn-row' }, okBtn, h('button', { class: 'btn secondary', type: 'button', onclick: () => fertig(false) }, abbrechen))
      );
      function fertig(v) {
        d.close();
        d.remove();
        resolve(v);
      }
      okBtn.addEventListener('click', () => {
        if (feld) {
          if (eingabe.muss !== undefined && feld.value.trim() !== eingabe.muss) {
            feld.setAttribute('aria-invalid', 'true');
            feld.focus();
            toast('Die Eingabe stimmt nicht.', true);
            return;
          }
          return fertig(feld.value);
        }
        fertig(true);
      });
      d.addEventListener('cancel', (e) => {
        e.preventDefault();
        fertig(false);
      });
      document.body.appendChild(d);
      d.showModal();
      (feld || okBtn).focus();
    });
  }

  function download(url) {
    const a = h('a', { href: url, download: '' });
    document.body.appendChild(a);
    a.click();
    a.remove();
  }

  function readFile(file) {
    return new Promise((resolve, reject) => {
      const r = new FileReader();
      r.onload = () => resolve(String(r.result));
      r.onerror = () => reject(new Error('Datei konnte nicht gelesen werden.'));
      r.readAsText(file, 'utf-8');
    });
  }

  /** Mischen (Fisher-Yates). */
  function mische(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function speichere(key, wert) {
    try {
      localStorage.setItem(key, JSON.stringify(wert));
    } catch {
      /* egal */
    }
  }
  function lade(key, standard) {
    try {
      const v = JSON.parse(localStorage.getItem(key));
      return v === null || v === undefined ? standard : v;
    } catch {
      return standard;
    }
  }

  return { SVG_NS, h, s, clear, mount, api, toast, fmtDatum, progress, prozent, sterne, bestaetigen, download, readFile, mische, speichere, lade };
})();
