import { test } from 'node:test';
import assert from 'node:assert/strict';
import { cpSync, mkdtempSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { execFileSync } from 'node:child_process';
import { contentVersion } from '../scripts/content-version.mjs';

const fixture = new URL('./fixtures/valid/', import.meta.url);
const buildScript = new URL('../scripts/build-content.mjs', import.meta.url);

test('published versions change on content edits without touching the source version', () => {
  const temp = mkdtempSync(join(tmpdir(), 'content-build-'));
  try {
    const root = join(temp, 'source');
    const out = join(temp, 'output');
    cpSync(fixture, root, { recursive: true });
    const read = (path) => JSON.parse(readFileSync(path, 'utf8'));
    const build = () => {
      execFileSync(process.execPath, [buildScript.pathname, '--root', root, '--out', out]);
      return read(join(out, 'demo/manifest.json'));
    };
    const sourceVersion = read(join(root, 'demo/game.json')).dataVersion;
    const first = build();
    assert.ok(Number.isSafeInteger(first.game.dataVersion));
    assert.deepEqual(build(), first, 'identical rebuilds must not invalidate offline content');
    const chapterPath = join(root, 'demo/chapters/ch-00.json');
    const chapter = read(chapterPath);
    chapter.items[0].hint.pt = 'Uma instrução corrigida.';
    writeFileSync(chapterPath, JSON.stringify(chapter));
    const second = build();
    assert.notEqual(second.game.dataVersion, first.game.dataVersion);
    assert.equal(read(join(out, 'demo', second.chapters[0].file)).items[0].hint.pt, 'Uma instrução corrigida.');
    assert.equal(read(join(root, 'demo/game.json')).dataVersion, sourceVersion);
  } finally {
    rmSync(temp, { recursive: true, force: true });
  }
});

test('fingerprints ignore object key order but include metadata and ordered steps', () => {
  const game = { id: 'demo', dataVersion: 1 };
  const chapter = { order: 0, items: [{ steps: ['first', 'second'] }] };
  const version = contentVersion(game, [chapter]);
  assert.equal(contentVersion({ dataVersion: 1, id: 'demo' }, [chapter]), version);
  assert.notEqual(contentVersion({ ...game, name: { en: 'Updated' } }, [chapter]), version);
  assert.notEqual(contentVersion(game, [{ ...chapter, items: [{ steps: ['second', 'first'] }] }]), version);
});
