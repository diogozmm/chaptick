// Renders public/share.png, the 1200×630 preview shown when a Chaptick link is shared (WhatsApp,
// Discord, Reddit...). Original art only: the brand mark and the library covers from cover-art.ts.
// Run after changing the covers or the tagline:  node scripts/render-share-image.mjs
import { readFileSync } from 'node:fs';
import { chromium } from 'playwright';

import { COVER_FONTS, COVER_HEIGHT, COVER_WIDTH, DEFAULT_COVER, coverShapes, coverTextLayout, fallbackCoverText } from '../src/app/core/cover/cover-art.ts';

const root = new URL('../', import.meta.url);
// setContent pages cannot read local files, so the fonts are inlined.
const font = (path) => `data:font/woff2;base64,${readFileSync(new URL(path, root)).toString('base64')}`;
const franchises = JSON.parse(readFileSync(new URL('../content/franchises.json', root), 'utf8'));
const games = ['sc', 'ysx'].map((id) => JSON.parse(readFileSync(new URL(`../content/${id}/game.json`, root), 'utf8')));
const mark = readFileSync(new URL('public/icons/mark.svg', root), 'utf8');

function cover(game) {
  const text = game.cover ?? fallbackCoverText(game.name.en);
  const s = franchises.find((f) => f.id === game.franchise)?.cover ?? DEFAULT_COVER;
  const layout = coverTextLayout(text, s.font);
  const titleFont = COVER_FONTS[s.font ?? 'default'];
  const shapes = coverShapes(s.motif)
    .map((shape) => {
      const color = shape.accent ? s.accent : '#fff';
      return shape.kind === 'path'
        ? `<path d="${shape.d}" fill="none" stroke="${color}" stroke-width="${shape.width}" opacity="${shape.opacity}" stroke-linecap="round"/>`
        : `<circle cx="${shape.cx}" cy="${shape.cy}" r="${shape.r}" opacity="${shape.opacity}" fill="${shape.fill ? color : 'none'}" stroke="${shape.fill ? 'none' : color}" stroke-width="2"/>`;
    })
    .join('');
  return `<svg viewBox="0 0 ${COVER_WIDTH} ${COVER_HEIGHT}" preserveAspectRatio="xMidYMid slice">
    <defs><linearGradient id="g-${game.id}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${s.from}"/><stop offset="1" stop-color="${s.to}"/></linearGradient></defs>
    <rect width="${COVER_WIDTH}" height="${COVER_HEIGHT}" fill="url(#g-${game.id})"/>${shapes}
    <defs><linearGradient id="s-${game.id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0.35" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.5"/></linearGradient></defs>
    <rect width="${COVER_WIDTH}" height="${COVER_HEIGHT}" fill="url(#s-${game.id})"/>
    <text x="22" y="${layout.titleY}" class="title" font-size="${layout.titleSize}" font-family="${titleFont.family}" font-weight="${titleFont.weight}">${text.title}</text>
    ${text.subtitle ? `<text x="23" y="${layout.subtitleY}" class="subtitle">${text.subtitle}</text>` : ''}</svg>`;
}

const html = `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face { font-family: Fraunces; src: url(${font('node_modules/@fontsource-variable/fraunces/files/fraunces-latin-opsz-normal.woff2')}); font-weight: 100 900; }
@font-face { font-family: Cinzel; src: url(${font('node_modules/@fontsource/cinzel/files/cinzel-latin-700-normal.woff2')}); font-weight: 700; }
@font-face { font-family: 'Uncial Antiqua'; src: url(${font('node_modules/@fontsource/uncial-antiqua/files/uncial-antiqua-latin-400-normal.woff2')}); }
@font-face { font-family: 'Fraunces Variable'; src: url(${font('node_modules/@fontsource-variable/fraunces/files/fraunces-latin-opsz-normal.woff2')}); font-weight: 100 900; }
@font-face { font-family: Inter; src: url(${font('node_modules/@fontsource-variable/inter/files/inter-latin-wght-normal.woff2')}); font-weight: 100 900; }
html, body { margin: 0; }
body {
  width: 1200px; height: 630px; overflow: hidden; position: relative; font-family: Inter; color: #eef1f8;
  background: radial-gradient(900px 500px at 0% 0%, rgb(88 130 214 / 0.35), transparent 60%),
              radial-gradient(700px 500px at 100% 100%, rgb(88 130 214 / 0.14), transparent 60%), #0c1120;
}
.text { position: absolute; left: 80px; top: 92px; width: 580px; }
.brand { display: flex; align-items: center; gap: 22px; }
.brand svg { width: 92px; height: 92px; }
.name { font: 600 88px/1 Fraunces; letter-spacing: -1.5px; }
h1 { margin: 52px 0 0; font: 600 54px/1.12 Fraunces; letter-spacing: -0.5px; }
p { margin: 26px 0 0; font-size: 28px; line-height: 1.4; color: #aab4cc; }
.covers { position: absolute; right: 40px; top: 96px; width: 470px; }
.cover { width: 470px; border-radius: 22px; overflow: hidden; box-shadow: 0 30px 60px rgb(0 0 0 / 0.45); border: 1px solid rgb(255 255 255 / 0.12); }
.cover svg { display: block; width: 100%; aspect-ratio: ${COVER_WIDTH} / ${COVER_HEIGHT}; }
.cover:nth-child(1) { transform: rotate(-4deg); }
.cover:nth-child(2) { transform: rotate(3deg) translate(-10px, 36px); }
.title { fill: #fff; }
.subtitle { font: 600 15px/1 Inter; letter-spacing: 0.14em; text-transform: uppercase; fill: #fff; opacity: 0.85; }
</style></head><body>
  <div class="text">
    <div class="brand">${mark}<span class="name">Chaptick</span></div>
    <h1>Never miss a thing, chapter by chapter</h1>
    <p>Spoiler-free checklists of quests, missables and collectibles.</p>
  </div>
  <div class="covers">${games.map((g) => `<div class="cover">${cover(g)}</div>`).join('')}</div>
</body></html>`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
await page.setContent(html, { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: new URL('public/share.png', root).pathname });
await browser.close();
console.log('✓ public/share.png');
