/* Algo Quest Lab – Beamer-Board: Top 15, Weltfortschritt des Kurses, letzte Erfolge. Aktualisiert sich alle 60 s. */
'use strict';
(() => {
  const { h, mount, api, progress } = AQ;
  const app = document.getElementById('app');
  const code = decodeURIComponent(location.pathname.split('/').filter(Boolean)[1] || '');

  function zeit(iso) {
    const d = new Date(iso);
    return d.toLocaleDateString('de-DE', { day: '2-digit', month: '2-digit' }) + ' ' + d.toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' });
  }

  async function lade() {
    try {
      const b = await api('GET', `/api/board/${encodeURIComponent(code)}`);
      document.title = `Board – ${b.kurs.name}`;
      mount(
        app,
        h('div', { class: 'row' }, h('div', { class: 'brand-mark', 'aria-hidden': 'true' }, 'AQ'), h('h1', null, `Algo Quest – ${b.kurs.name}`), h('span', { class: 'right muted' }, `${b.schueler} Abenteurer · aktualisiert ${new Date().toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' })}`)),
        h(
          'div',
          { class: 'board-grid' },
          h(
            'section',
            { class: 'board-card' },
            h('h2', null, '🏆 Top 15'),
            b.liste.length
              ? h('table', { class: 'board-liste' }, h('tbody', null, b.liste.map((r) => h('tr', null, h('td', { class: 'platz' }, r.platz <= 3 ? ['🥇', '🥈', '🥉'][r.platz - 1] : String(r.platz)), h('td', null, r.name), h('td', { class: 'p' }, `${r.punkte}`), h('td', { class: 'p' }, `🏅 ${r.abzeichen}`)))))
              : h('p', null, 'Noch keine Punkte – los geht’s!')
          ),
          h(
            'div',
            null,
            h('section', { class: 'board-card' }, h('h2', null, '🗺️ Fortschritt des Kurses'), b.welten.map((w) => {
              const el = h('div', { class: 'board-welt' }, h('div', { class: 'row' }, h('span', null, `Welt ${w.nr}: ${w.titel}`), h('strong', { class: 'right' }, Math.round(w.anteil * 100) + ' %')), progress(w.anteil, 'welt'));
              el.style.setProperty('--welt', w.farbe);
              return el;
            })),
            h('div', { class: 'spacer' }),
            h('section', { class: 'board-card' }, h('h2', null, '✨ Letzte Erfolge'), b.erfolge.length ? b.erfolge.map((e) => h('div', { class: 'board-erfolg' }, e.text, ' ', h('span', { class: 'zeit' }, zeit(e.at)))) : h('p', null, 'Noch keine Erfolge.'))
          )
        )
      );
    } catch (e) {
      mount(app, h('h1', null, 'Beamer-Board'), h('p', null, e.status === 404 ? 'Für diesen Kurs ist kein Beamer-Board aktiviert.' : e.message));
    }
  }
  lade();
  setInterval(lade, 60000);
})();
