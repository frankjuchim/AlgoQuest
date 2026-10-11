// Rendert Lab-Blöcke (struktogramm, baum, reihung, adt, tabelle, klassenkarte, code …) als PNG – mit dem Renderer des Labs
// (public/static/js/render.js), damit Bilder in den Erklärvideos genauso aussehen wie im Lab. Aufgerufen von video_folien.py.
// Aufruf: node werkzeuge/video_bilder.js <spec.json> <ausgabeordner>
//   spec.json: { "name": {block}, ... }  → <ausgabeordner>/<name>.png
const path = require('node:path');
const fs = require('node:fs');
const { chromium } = require(require('node:path').join(__dirname, '..', 'node_modules', 'playwright-core'));
const APP = path.join(__dirname, '..', 'public');
function chromiumPfad() {
  if (process.env.CHROMIUM_PATH) return process.env.CHROMIUM_PATH;
  const basis = process.env.PLAYWRIGHT_BROWSERS_PATH || '/opt/pw-browsers';
  for (const d of fs.readdirSync(basis).filter((x) => /^chromium-\d+$/.test(x)).sort().reverse()) {
    const p = path.join(basis, d, 'chrome-linux', 'chrome');
    if (fs.existsSync(p)) return p;
  }
  return undefined;
}

(async () => {
  const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const aus = path.resolve(process.argv[3]);
  fs.mkdirSync(aus, { recursive: true });
  const html = `<!doctype html><html lang="de"><head><meta charset="utf-8">
  <link rel="stylesheet" href="file://${APP}/static/css/style.css">
  <style>body{background:#fff;margin:0;padding:12px} #x{display:inline-block;max-width:900px;font-size:20px} #x .card{box-shadow:none} #x .sg{min-width:0}</style></head>
  <body><div id="x"></div>
  <script src="file://${APP}/static/js/common.js"></script>
  <script src="file://${APP}/static/js/shared/baum.js"></script>
  <script src="file://${APP}/static/js/render.js"></script></body></html>`;
  const datei = path.join(aus, '_render.html');
  fs.writeFileSync(datei, html);
  const b = await chromium.launch({ executablePath: chromiumPfad() });
  const p = await b.newPage({ viewport: { width: 1000, height: 800 }, deviceScaleFactor: 3 });
  const fehler = [];
  p.on('pageerror', (e) => fehler.push(String(e)));
  await p.goto('file://' + datei);
  for (const [name, block] of Object.entries(spec)) {
    const breite = block._breite || null;
    await p.evaluate(([block, breite]) => {
      const x = document.getElementById('x');
      x.replaceChildren();
      x.style.width = breite ? breite + 'px' : '';
      const b = { ...block };
      delete b._breite;
      x.append(AQR.bloecke([b], null));
    }, [block, breite]);
    await p.waitForTimeout(50);
    await p.locator('#x').screenshot({ path: path.join(aus, name + '.png'), omitBackground: false });
  }
  fs.unlinkSync(datei);
  await b.close();
  if (fehler.length) { console.error(fehler.join('\n')); process.exit(1); }
  console.log(Object.keys(spec).length + ' Bild(er) in ' + aus);
})();
