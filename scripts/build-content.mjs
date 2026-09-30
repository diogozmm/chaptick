#!/usr/bin/env node
// Validates content/ and writes the static files the app serves:
//   <out>/<game>/manifest.json  counts only, never names, so locked chapters stay spoiler-free
//   <out>/<game>/ch-<order>.json one file per chapter, fetched only once it is unlocked
import { mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { parseArgs } from 'node:util';
import { loadContent, validateContent } from './content-validation.mjs';

const { values } = parseArgs({
  options: { root: { type: 'string', default: 'content' }, out: { type: 'string', default: 'web/public/content' } },
});

const errors = validateContent(values.root);
if (errors.length > 0) {
  console.error(errors.map((e) => `✗ ${e}`).join('\n'));
  process.exit(1);
}

rmSync(values.out, { recursive: true, force: true });
for (const { game, chapters } of loadContent(values.root)) {
  const outDir = join(values.out, game.id);
  mkdirSync(outDir, { recursive: true });

  const sorted = chapters.map((c) => c.data).sort((a, b) => a.order - b.order);
  const manifest = {
    game,
    chapters: sorted.map(({ id, order, neutralLabel, items }) => ({
      id,
      order,
      neutralLabel,
      itemCount: items.length,
      file: `ch-${order}.json`,
    })),
  };
  writeFileSync(join(outDir, 'manifest.json'), JSON.stringify(manifest));
  for (const chapter of sorted) writeFileSync(join(outDir, `ch-${chapter.order}.json`), JSON.stringify(chapter));
  console.log(`✓ ${game.id}: ${sorted.length} chapter(s), data v${game.dataVersion}`);
}
