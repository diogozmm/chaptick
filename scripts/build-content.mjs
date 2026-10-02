#!/usr/bin/env node
// Validates content/ and writes the static files the app serves:
//   <out>/catalog.json          franchises and their games, counts only (the library screen)
//   <out>/<game>/manifest.json  counts only, never names, so locked chapters stay spoiler-free
//   <out>/<game>/ch-<order>.json one file per chapter, fetched only once it is unlocked
import { mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { parseArgs } from 'node:util';
import { loadContent, loadFranchises, validateContent } from './content-validation.mjs';

const { values } = parseArgs({
  options: { root: { type: 'string', default: 'content' }, out: { type: 'string', default: 'web/public/content' } },
});

const errors = validateContent(values.root);
if (errors.length > 0) {
  console.error(errors.map((e) => `✗ ${e}`).join('\n'));
  process.exit(1);
}

rmSync(values.out, { recursive: true, force: true });
mkdirSync(values.out, { recursive: true });
const games = loadContent(values.root);

/** What a game offers, read from its content: a checklist when it has items, a compendium when it
 * has entries, crafts or creatures. Derived here so it can never go stale. */
const featuresOf = (chapters) => {
  const has = (key) => chapters.some(({ data }) => (data[key] ?? []).length > 0);
  return [
    ...(has('items') ? ['checklist'] : []),
    ...(['entries', 'crafts', 'creatures', 'villagers', 'events'].some(has) ? ['compendium'] : []),
  ];
};

const catalog = {
  franchises: loadFranchises(values.root).map((franchise) => ({
    ...franchise,
    games: games
      .filter(({ game }) => game.franchise === franchise.id)
      .sort((a, b) => (a.game.order ?? 0) - (b.game.order ?? 0))
      .map(({ game, chapters }) => ({
        id: game.id,
        name: game.name,
        cover: game.cover,
        platforms: game.platforms,
        features: featuresOf(chapters),
        progressTerm: game.progressTerm,
        chapterCount: chapters.length,
        itemCount: chapters.reduce((sum, c) => sum + c.data.items.length, 0),
      })),
  })),
};
writeFileSync(join(values.out, 'catalog.json'), JSON.stringify(catalog));

for (const { game, chapters } of games) {
  const outDir = join(values.out, game.id);
  mkdirSync(outDir, { recursive: true });

  const sorted = chapters.map((c) => c.data).sort((a, b) => a.order - b.order);
  const manifest = {
    game,
    features: featuresOf(chapters),
    // Totals only (no names), so screens can hide a collection a game doesn't have.
    collections: {
      fish: sorted.reduce((sum, c) => sum + (c.fish ?? []).length, 0),
      recipes: sorted.reduce((sum, c) => sum + (c.recipes ?? []).length, 0),
    },
    deadlines: sorted.reduce((sum, c) => sum + c.items.filter((i) => i.availableUntil !== null).length, 0),
    compendium: {
      entries: sorted.reduce((sum, c) => sum + (c.entries ?? []).length, 0),
      crafts: sorted.reduce((sum, c) => sum + (c.crafts ?? []).length, 0),
      creatures: sorted.reduce((sum, c) => sum + (c.creatures ?? []).length, 0),
      // Ways to get things that depend on the in-game season, so screens can offer a season view.
      seasonal: sorted.reduce(
        (sum, c) =>
          sum +
          [...(c.entries ?? []).flatMap((e) => e.sources), ...(c.entrySources ?? [])].filter((s) => s.seasons?.length).length +
          (c.events ?? []).length,
        0,
      ),
    },
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
