import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import Ajv2020 from 'ajv/dist/2020.js';
import addFormats from 'ajv-formats';

const TYPE_CODES = { quest: 'q', hidden_quest: 'hq', missable: 'mi', collectible: 'co' };
const SCHEMA_DIR = new URL('../content/schema/', import.meta.url);

const readJson = (path) => JSON.parse(readFileSync(path, 'utf8'));

function createValidators() {
  const ajv = new Ajv2020({ allErrors: true });
  addFormats(ajv);
  for (const name of ['common', 'game', 'chapter', 'franchises']) {
    ajv.addSchema(readJson(new URL(`${name}.schema.json`, SCHEMA_DIR)), `${name}.schema.json`);
  }
  return {
    game: ajv.getSchema('game.schema.json'),
    chapter: ajv.getSchema('chapter.schema.json'),
    franchises: ajv.getSchema('franchises.schema.json'),
  };
}

/** The franchise list at the content root. */
export const loadFranchises = (root) => readJson(join(root, 'franchises.json'));

/** Loads every game under `root` as { game, chapters: [{ file, data }] }. */
export function loadContent(root) {
  return readdirSync(root, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && entry.name !== 'schema')
    .map((entry) => {
      const dir = join(root, entry.name);
      const chaptersDir = join(dir, 'chapters');
      const files = existsSync(chaptersDir) ? readdirSync(chaptersDir).filter((f) => f.endsWith('.json')).sort() : [];
      return {
        dir: entry.name,
        game: readJson(join(dir, 'game.json')),
        chapters: files.map((file) => ({ file: join(entry.name, 'chapters', file), data: readJson(join(chaptersDir, file)) })),
      };
    });
}

function schemaErrors(validate, data, file) {
  if (validate(data)) return [];
  return validate.errors.map((e) => `${file}: ${e.instancePath || '/'} ${e.message}`);
}

function chapterErrors(chapter, file, gameId) {
  const errors = [];
  const expectedId = `${gameId}-ch${chapter.order}`;
  if (chapter.gameId !== gameId) errors.push(`${file}: gameId "${chapter.gameId}" should be "${gameId}"`);
  if (chapter.id !== expectedId) errors.push(`${file}: chapter id "${chapter.id}" should be "${expectedId}"`);

  for (const id of [...chapter.checkpoints.map((c) => c.id), ...entityIds(chapter)]) {
    if (!id.startsWith(`${chapter.id}-`)) errors.push(`${file}: "${id}" does not belong to ${chapter.id}`);
  }
  for (const item of chapter.items) {
    const code = item.id.split('-').at(-2);
    if (code !== TYPE_CODES[item.type]) errors.push(`${file}: "${item.id}" uses code "${code}" but type is ${item.type}`);
  }
  const itemIds = new Set(chapter.items.map((i) => i.id));
  for (const text of chapter.itemTexts) {
    // Texts ship in the item's own chapter file so they never leak ahead of it.
    if (!itemIds.has(text.itemId)) errors.push(`${file}: itemText points to "${text.itemId}", not an item of this chapter`);
  }
  return errors;
}

/** Every id a chapter defines besides its checkpoints: items, bosses, fish and recipes. */
const entityIds = (chapter) =>
  [chapter.items, chapter.bosses, chapter.fish, chapter.recipes].flatMap((list) => (list ?? []).map((e) => e.id));

/** References that may point to the same chapter or an earlier one, never a later one. */
/** Trophy ids are unique per game, and items only point to trophies their game declares. */
function trophyErrors(game, chapters, dir) {
  const errors = [];
  const ids = new Set();
  for (const { id } of game.trophies ?? []) {
    if (ids.has(id)) errors.push(`${dir}/game.json: duplicate trophy "${id}"`);
    ids.add(id);
  }
  for (const { file, data } of chapters) {
    for (const item of data.items) {
      for (const trophy of item.trophies ?? []) {
        if (!ids.has(trophy)) errors.push(`${file}: "${item.id}" counts toward unknown trophy "${trophy}"`);
      }
    }
  }
  return errors;
}

function backReferenceErrors(chapters) {
  const errors = [];
  const orderOf = new Map();
  for (const { data } of chapters) {
    for (const i of data.items) orderOf.set(i.id, data.order);
    for (const f of data.fish ?? []) orderOf.set(f.id, data.order);
  }
  for (const { file, data } of chapters) {
    const refs = [
      ...(data.bosses ?? []).filter((b) => b.relatedItem).map((b) => [b.id, b.relatedItem]),
      ...(data.fishSpots ?? []).map((s) => [`fish spot "${s.where.en}"`, s.fishId]),
    ];
    for (const [from, to] of refs) {
      const order = orderOf.get(to);
      if (order === undefined) errors.push(`${file}: ${from} refers to unknown "${to}"`);
      else if (order > data.order) errors.push(`${file}: ${from} refers to "${to}" from a later chapter`);
    }
  }
  return errors;
}

/**
 * Compendium ids (entries, crafts, creatures) are unique per game, and every reference to an entry
 * points to the same chapter or an earlier one, so an unlocked file never names something ahead.
 */
function compendiumErrors(chapters) {
  const errors = [];
  const orderOf = new Map();
  for (const { file, data } of chapters) {
    for (const e of [...(data.entries ?? []), ...(data.crafts ?? []), ...(data.creatures ?? []), ...(data.villagers ?? []), ...(data.events ?? [])]) {
      if (orderOf.has(e.id)) errors.push(`${file}: duplicate compendium id "${e.id}"`);
      orderOf.set(e.id, data.order);
    }
  }
  const entryIds = new Set(chapters.flatMap(({ data }) => (data.entries ?? []).map((e) => e.id)));
  for (const { file, data } of chapters) {
    const refs = [
      ...(data.entrySources ?? []).map((s) => ['a later source', s.entryId]),
      ...(data.entries ?? []).filter((e) => e.grow?.crop).map((e) => [`seed "${e.id}"`, e.grow.crop]),
      ...(data.events ?? []).flatMap((e) => (e.related ?? []).filter((i) => i.entryId).map((i) => [`event "${e.id}"`, i.entryId])),
      ...Object.values(data.commonGifts ?? {}).flat().filter((g) => g.entryId).map((g) => ['common gifts', g.entryId]),
      ...(data.villagers ?? []).flatMap((v) =>
        Object.values(v.gifts).flat().filter((g) => g.entryId).map((g) => [`villager "${v.id}"`, g.entryId]),
      ),
      ...(data.crafts ?? []).flatMap((c) => [
        ...c.ingredients.filter((i) => i.entryId).map((i) => [`craft "${c.id}"`, i.entryId]),
        ...(c.makes ? [[`craft "${c.id}"`, c.makes]] : []),
      ]),
      ...(data.creatures ?? []).flatMap((c) =>
        (c.rewards ?? [])
          .flatMap((r) => [...r.items, ...(r.gives ?? []), ...(r.also ?? []).flatMap((a) => a.items)])
          .filter((i) => i.entryId)
          .map((i) => [`creature "${c.id}"`, i.entryId]),
      ),
    ];
    for (const [from, to] of refs) {
      if (!entryIds.has(to)) errors.push(`${file}: ${from} refers to unknown entry "${to}"`);
      else if (orderOf.get(to) > data.order) errors.push(`${file}: ${from} refers to "${to}" from a later chapter`);
    }
  }
  return errors;
}

function crossChapterErrors(chapters) {
  const errors = [];
  const seen = new Map();
  const checkpointChapterOrder = new Map();
  const orders = new Map();

  for (const { file, data } of chapters) {
    if (orders.has(data.order)) errors.push(`${file}: order ${data.order} already used by ${orders.get(data.order)}`);
    orders.set(data.order, file);
    for (const id of [data.id, ...data.checkpoints.map((c) => c.id), ...entityIds(data)]) {
      if (seen.has(id)) errors.push(`${file}: duplicate id "${id}" (also in ${seen.get(id)})`);
      seen.set(id, file);
    }
    for (const cp of data.checkpoints) checkpointChapterOrder.set(cp.id, data.order);
  }

  for (const { file, data } of chapters) {
    for (const item of data.items) {
      if (item.availableUntil === null) continue;
      const cpOrder = checkpointChapterOrder.get(item.availableUntil);
      if (cpOrder === undefined) errors.push(`${file}: "${item.id}" availableUntil "${item.availableUntil}" does not exist`);
      else if (cpOrder < data.order) errors.push(`${file}: "${item.id}" expires at a checkpoint of an earlier chapter`);
    }
  }
  return { errors, ids: [...seen.keys()] };
}

function registryErrors(ids, registry, baseRegistry) {
  const errors = [];
  const registered = new Set(registry);
  if (registered.size !== registry.length) errors.push('id-registry.json: contains duplicates');
  for (const id of ids) {
    if (!registered.has(id)) errors.push(`id-registry.json: "${id}" is used in content but not registered`);
  }
  // Saved progress points at these ids, so a registered id may never disappear or be reused.
  for (const id of baseRegistry ?? []) {
    if (!registered.has(id)) errors.push(`id-registry.json: "${id}" was removed; ids are append-only`);
  }
  return errors;
}

/** Returns a list of human-readable errors; empty means the content is publishable. */
export function validateContent(root, { baseRegistry } = {}) {
  const validators = createValidators();
  const errors = [];
  const allIds = [];

  const franchises = loadFranchises(root);
  errors.push(...schemaErrors(validators.franchises, franchises, 'franchises.json'));
  const franchiseIds = new Set();
  for (const { id } of Array.isArray(franchises) ? franchises : []) {
    if (franchiseIds.has(id)) errors.push(`franchises.json: duplicate franchise "${id}"`);
    franchiseIds.add(id);
  }

  for (const { dir, game, chapters } of loadContent(root)) {
    errors.push(...schemaErrors(validators.game, game, `${dir}/game.json`));
    if (game.id !== dir) errors.push(`${dir}/game.json: id "${game.id}" should match folder "${dir}"`);
    if (!franchiseIds.has(game.franchise)) errors.push(`${dir}/game.json: unknown franchise "${game.franchise}"`);

    const valid = chapters.filter(({ file, data }) => {
      const found = schemaErrors(validators.chapter, data, file);
      errors.push(...found);
      return found.length === 0;
    });
    for (const { file, data } of valid) errors.push(...chapterErrors(data, file, game.id));
    errors.push(...trophyErrors(game, valid, dir));

    const cross = crossChapterErrors(valid);
    errors.push(...cross.errors, ...backReferenceErrors(valid), ...compendiumErrors(valid));
    allIds.push(game.id, ...cross.ids);
  }

  const registry = readJson(join(root, 'id-registry.json'));
  errors.push(...registryErrors(allIds, registry, baseRegistry));
  return errors;
}
