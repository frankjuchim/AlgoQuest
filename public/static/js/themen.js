/* Algo Quest Lab – Themenübersicht (/themen): Welten mit Leveln, Arbeitsblättern (PDF), Boss, Trainingsplatz und
 * Warm-up; Querschnitte nach Aufgabentyp und nach Fallen P1–P10. Öffentlich, ohne Lösungen. */
(() => {
  const { h, api, mount } = AQ;
  const ziel = document.getElementById('themen-inhalt');

  const dsText = (ds) => (!ds || !ds.length ? '' : ds.length === 1 ? `DS ${ds[0]}` : `DS ${ds.join(', ')}`);
  const dsSpanne = (ds) => (!ds ? '' : ds[0] === ds[1] ? `DS ${ds[0]}` : `DS ${ds[0]}–${ds[1]}`);
  // Schüler üben im Lab; eine angemeldete Lehrkraft landet in der Aufgaben-Vorschau (mit Lösungen) der Welt
  let lehrkraft = false;
  const levelLink = (l) => (lehrkraft ? `/lehrer#/vorschau/welt/${l.welt}` : `/spiel#/level/${encodeURIComponent(l.id)}`);
  const pdf = (url, text) => (url ? h('a', { class: 'pdf', href: url, target: '_blank', rel: 'noopener' }, text) : h('span', null, text));

  function einleitung(d) {
    return h(
      'section',
      { class: 'card' },
      h('h1', null, 'Themen und Arbeitsblätter'),
      h('p', null, 'Alles, was in der Einheit „Algorithmik und Datenstrukturen“ fürs Abitur wichtig ist – sortiert nach den sieben Welten. Zu jedem Thema gibt es ein Arbeitsblatt (PDF) und ein Level im Lab mit automatisch geprüften Aufgaben im Abitur-Stil.'),
      h(
        'ol',
        { class: 'schritte' },
        h('li', null, h('b', null, '1. Thema wählen'), 'Unten nach Welt, nach Aufgabentyp (z. B. Tracetabelle) oder nach deinen Fallen P1–P10 suchen.'),
        h('li', null, h('b', null, '2. Arbeitsblatt lesen'), 'Infoteile und Beispiele im PDF durcharbeiten, Aufgaben auf Papier lösen – wie im Abitur.'),
        h('li', null, h('b', null, '3. Im Lab üben'), '„Üben →“ öffnet das passende Level (Anmeldung mit Name und persönlichem Code). Ohne Tipp und Fehlversuch gibt es die meisten Punkte.'),
        h('li', null, h('b', null, '4. Boss als Abi-Probe'), 'Je Welt ein Online-Boss im Lab (auf Zeit, Auswertung mit Erklärungen) und ein Papier-Boss als PDF – handschriftlich in 60 Minuten wie im Abitur.'),
        h('li', null, h('b', null, '5. Dranbleiben'), 'Trainingsplatz (Zufallsaufgaben) und Warm-up-Karten – im Lab mit Lösungen (Leitner) oder als PDF für 10 Minuten auf Papier.')
      ),
      d.werkzeugkarten
        ? h('p', { class: 'callout gold' }, h('strong', null, 'Immer dabei: '), pdf(d.werkzeugkarten.url, d.werkzeugkarten.titel), ' – Abi-Check vor der Abgabe, Zeitbudget, Struktogramm- und Klassendiagramm-Notation.')
        : null
    );
  }

  function weltKarte(w) {
    const kopf = h(
      'div',
      { class: 'welt-kopf' },
      h('div', { class: 'welt-nr', 'aria-hidden': 'true' }, String(w.nr)),
      h('div', { class: 'grow' }, h('h2', null, `Welt ${w.nr} – ${w.titel}`), h('div', { class: 'meta' }, [dsSpanne(w.ds), `${w.levels.length} Level`, `${w.aufgaben} Aufgaben`].filter(Boolean).join(' · ')))
    );
    const tabelle = h(
      'div',
      { class: 'scroll-x' },
      h(
        'table',
        { class: 'liste levels' },
        h('thead', null, h('tr', null, h('th', null, 'Level'), h('th', null, 'Thema'), h('th', { class: 'hide-sm' }, 'DS'), h('th', null, 'Arbeitsblatt'), h('th', null, 'Lab'))),
        h(
          'tbody',
          null,
          w.levels.map((l) =>
            h(
              'tr',
              null,
              h('td', { class: 'lvl-nr' }, l.nr),
              h('td', null, l.titel, l.ide ? h('div', { class: 'muted klein' }, 'Online-IDE: ', l.ide) : null),
              h('td', { class: 'hide-sm klein ds' }, dsText(l.ds)),
              h('td', { class: 'klein ab' }, l.abBlatt && l.abBlatt.url ? pdf(l.abBlatt.url, l.ab) : l.ab || '–'),
              h('td', { class: 'lab' }, h('a', { href: levelLink(l), 'aria-label': `Level ${l.nr} üben` }, 'Üben →'), h('span', { class: 'muted klein' }, ` ${l.aufgaben} Aufgaben`))
            )
          )
        )
      )
    );
    const abs = w.arbeitsblaetter.length
      ? h('div', null, h('h3', null, 'Arbeitsblätter (PDF)'), h('ul', { class: 'ab-liste' }, w.arbeitsblaetter.map((a) => h('li', null, pdf(a.url, `AB ${a.nr}: ${a.titel}`), a.ds.length ? h('span', { class: 'muted klein' }, ` · ${dsText(a.ds)}`) : null))))
      : null;
    const symbol = { boss: '⚔️', probeklausur: '📝', warmup: '🔥' };
    const weitere = w.weitere && w.weitere.length
      ? h('div', null, h('h3', null, 'Training auf Papier (PDF)'), h('ul', { class: 'ab-liste' }, w.weitere.map((x) => h('li', null, `${symbol[x.art] || '📄'} `, x.url ? h('a', { href: x.url, target: '_blank', rel: 'noopener' }, x.titel) : x.titel))))
      : null;
    const extras = h(
      'div',
      { class: 'extras' },
      w.boss ? h('span', { class: 'pill gold' }, `⚔️ Online-Boss im Lab: ${w.boss.titel} (${w.boss.anzahl} Aufgaben, ${w.boss.dauerMin} min)`) : null,
      w.training.length ? h('span', { class: 'pill green', title: w.training.join(' · ') }, `🎯 Trainingsplatz: ${w.training.length} Aufgabenarten`) : null,
      w.warmup ? h('span', { class: 'pill' }, `🔥 ${w.warmup} Warm-up-Karten im Lab`) : null
    );
    return h('section', { class: 'welt-karte', id: `welt-${w.nr}`, style: { '--welt': w.farbe } }, kopf, h('div', { class: 'welt-inhalt' }, tabelle, abs, weitere, extras));
  }

  /** „Kür: Zugbuch und Initiative – Spielmodule“ → „Zugbuch und Initiative“ */
  const kurztitel = (t) => t.replace(/^Kür:\s*/, '').split(/[:–]/)[0].trim();

  function ortLinks(orte, welten) {
    const farbe = new Map(welten.map((w) => [w.nr, w.farbe]));
    return h(
      'div',
      { class: 'ort-links' },
      orte.map((o) =>
        h('a', { href: levelLink(o), title: `Level ${o.nr} – ${o.titel}` }, h('span', { class: 'pill', style: { borderLeft: `4px solid ${farbe.get(o.welt) || '#1f4e79'}` } }, `${o.nr} ${kurztitel(o.titel)}`, h('span', { class: 'muted' }, ` ×${o.anzahl}`)))
      )
    );
  }

  function aufgabentypen(d) {
    return h(
      'section',
      { class: 'card' },
      h('p', { class: 'muted' }, 'Die Abiturklassiker quer durch alle Welten – mit der Zahl passender Lab-Aufgaben je Level. Ein Klick öffnet das Level.'),
      h(
        'div',
        { class: 'scroll-x' },
        h(
          'table',
          { class: 'liste' },
          h('thead', null, h('tr', null, h('th', null, 'Aufgabentyp'), h('th', { class: 'num' }, 'Aufgaben'), h('th', null, 'Wo üben?'))),
          h('tbody', null, d.kategorien.map((k) => h('tr', null, h('td', null, h('strong', null, k.kategorie)), h('td', { class: 'num' }, String(k.anzahl)), h('td', null, ortLinks(k.orte, d.welten)))))
        )
      )
    );
  }

  function fallen(d) {
    return h(
      'section',
      { class: 'card' },
      h('p', { class: 'muted' }, 'Die zehn häufigsten Punktverluste im Abitur. In deinem Profil im Lab siehst du unter „Deine Fallen“, wo du noch Fehlversuche hast – hier findest du die passenden Level dazu.'),
      h(
        'div',
        { class: 'scroll-x' },
        h(
          'table',
          { class: 'liste' },
          h('thead', null, h('tr', null, h('th', null, 'Falle'), h('th', { class: 'num' }, 'Aufgaben'), h('th', null, 'Wo üben?'))),
          h(
            'tbody',
            null,
            d.fallen.map((f) => h('tr', null, h('td', null, h('strong', null, `${f.p} ${f.titel}`), h('div', { class: 'muted klein' }, f.text)), h('td', { class: 'num' }, String(f.anzahl)), h('td', null, ortLinks(f.orte, d.welten))))
          )
        )
      )
    );
  }

  async function start() {
    try {
      const sitzung = await api('GET', '/api/sitzung');
      lehrkraft = !sitzung.schueler && !!sitzung.lehrkraft;
      if (!sitzung.schueler) {
        const z = document.getElementById('zum-lab');
        z.textContent = sitzung.lehrkraft ? '▶ Lehrkraft-Bereich' : '▶ Anmelden';
        z.href = sitzung.lehrkraft ? '/lehrer' : '/';
      }
    } catch {
      /* Navigation bleibt beim Standard */
    }
    let d;
    try {
      d = await api('GET', '/api/themen');
    } catch (e) {
      mount(ziel, h('p', { class: 'callout warn' }, 'Die Übersicht konnte nicht geladen werden: ', e.message));
      return;
    }
    mount(
      ziel,
      einleitung(d),
      h('nav', { class: 'card chips', 'aria-label': 'Sprung zur Welt' }, h('strong', null, 'Welten: '), d.welten.map((w) => h('a', { href: `#welt-${w.nr}`, class: 'pill', style: { borderLeft: `4px solid ${w.farbe}` } }, `${w.nr} ${w.titel.replace(/^(Der|Die|Das)\s+/, '')}`))),
      h('h2', { class: 'abschnitt', id: 'welten' }, '🗺️ Nach Welten'),
      d.welten.map(weltKarte),
      h('h2', { class: 'abschnitt', id: 'aufgabentypen' }, '🧩 Nach Aufgabentyp'),
      aufgabentypen(d),
      h('h2', { class: 'abschnitt', id: 'fallen' }, '⚠️ Nach Fallen P1–P10'),
      fallen(d)
    );
    if (location.hash) {
      const el = document.getElementById(location.hash.slice(1));
      if (el) el.scrollIntoView();
    }
  }

  start();
})();
