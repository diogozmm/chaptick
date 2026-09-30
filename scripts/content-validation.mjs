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
  for (const name of ['common', 'game', 'chapter']) {
    ajv.addSchema(readJson(new URL(`${name}.schema.json`, SCHEMA_DIR)), `${name}.schema.json`);
  }
  return { game: ajv.getSchema('game.schema.json'), chapter: ajv.getSchema('chapter.schema.json') };
}

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

  for (const entity of [...chapter.checkpoints, ...chapter.items]) {
    if (!entity.id.startsWith(`${chapter.id}-`)) errors.push(`${file}: "${entity.id}" does not belong to ${chapter.id}`);
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

function crossChapterErrors(chapters) {
  const errors = [];
  const seen = new Map();
  const checkpointChapterOrder = new Map();
  const orders = new Map();

  for (const { file, data } of chapters) {
    if (orders.has(data.order)) errors.push(`${file}: order ${data.order} already used by ${orders.get(data.order)}`);
    orders.set(data.order, file);
    for (const id of [data.id, ...data.checkpoints.map((c) => c.id), ...data.items.map((i) => i.id)]) {
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

  for (const { dir, game, chapters } of loadContent(root)) {
    errors.push(...schemaErrors(validators.game, game, `${dir}/game.json`));
    if (game.id !== dir) errors.push(`${dir}/game.json: id "${game.id}" should match folder "${dir}"`);

    const valid = chapters.filter(({ file, data }) => {
      const found = schemaErrors(validators.chapter, data, file);
      errors.push(...found);
      return found.length === 0;
    });
    for (const { file, data } of valid) errors.push(...chapterErrors(data, file, game.id));

    const cross = crossChapterErrors(valid);
    errors.push(...cross.errors);
    allIds.push(game.id, ...cross.ids);
  }

  const registry = readJson(join(root, 'id-registry.json'));
  errors.push(...registryErrors(allIds, registry, baseRegistry));
  return errors;
}
