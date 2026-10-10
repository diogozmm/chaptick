// Isolated deployments for the real-service-worker regression test.
import { cpSync, mkdirSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { execFileSync } from 'node:child_process';

const base = new URL('./.content/update/', import.meta.url);
const source = new URL('source/', base);
rmSync(base, { recursive: true, force: true });
mkdirSync(base, { recursive: true });
cpSync(new URL('./fixtures/content/', import.meta.url), source, { recursive: true });
const build = (version) => execFileSync(process.execPath, [
  new URL('../../scripts/build-content.mjs', import.meta.url).pathname,
  '--root', source.pathname, '--out', new URL(version + '/', base).pathname,
], { stdio: 'inherit' });
build('before');
const path = new URL('sc/chapters/ch-00.json', source);
const chapter = JSON.parse(readFileSync(path, 'utf8'));
const item = chapter.items.find((i) => i.id === 'sc-ch0-co-01');
item.hint.en = 'Updated instructions from the new deployment.';
item.steps[0].text.en = 'Updated left shelf instruction';
writeFileSync(path, JSON.stringify(chapter));
// Intentionally keep game.json's dataVersion unchanged.
build('after');
