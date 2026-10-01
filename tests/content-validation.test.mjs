import { test } from 'node:test';
import assert from 'node:assert/strict';
import { cpSync, mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { validateContent } from '../scripts/content-validation.mjs';

const FIXTURE = new URL('./fixtures/valid/', import.meta.url).pathname;
const CH0 = 'demo/chapters/ch-00.json';

/** Copies the valid fixture, lets `mutate` edit one JSON file, and validates the copy. */
function validateWith(file, mutate, options) {
  const root = mkdtempSync(join(tmpdir(), 'content-'));
  cpSync(FIXTURE, root, { recursive: true });
  if (file) {
    const path = join(root, file);
    const data = JSON.parse(readFileSync(path, 'utf8'));
    writeFileSync(path, JSON.stringify(mutate(data) ?? data));
  }
  return validateContent(root, options);
}

const expectError = (errors, fragment) =>
  assert.ok(errors.some((e) => e.includes(fragment)), `expected "${fragment}" in:\n${errors.join('\n')}`);

test('valid fixture passes', () => {
  assert.deepEqual(validateWith(), []);
});

test('real content passes', () => {
  assert.deepEqual(validateContent(new URL('../content/', import.meta.url).pathname), []);
});

test('rejects schema violations', () => {
  expectError(validateWith(CH0, (d) => void (d.items[0].spoilerLevel = 3)), 'must be equal to one of the allowed values');
});

test('rejects duplicate ids across chapters', () => {
  const errors = validateWith('demo/chapters/ch-01.json', (d) => {
    d.items.push({ ...d.items[0], id: 'demo-ch1-hq-01' });
  });
  expectError(errors, 'duplicate id "demo-ch1-hq-01"');
});

test('rejects unknown checkpoint', () => {
  expectError(validateWith(CH0, (d) => void (d.items[0].availableUntil = 'demo-ch0-cp-09')), 'does not exist');
});

test('rejects checkpoint from an earlier chapter', () => {
  const errors = validateWith('demo/chapters/ch-01.json', (d) => void (d.items[0].availableUntil = 'demo-ch0-cp-01'));
  expectError(errors, 'earlier chapter');
});

test('rejects type code that does not match the type', () => {
  expectError(validateWith(CH0, (d) => void (d.items[0].type = 'collectible')), 'uses code "q"');
});

test('rejects item placed in the wrong chapter file', () => {
  expectError(validateWith(CH0, (d) => void (d.items[0].id = 'demo-ch1-q-05')), 'does not belong to demo-ch0');
});

test('rejects unregistered ids', () => {
  const errors = validateWith('id-registry.json', (r) => r.filter((id) => id !== 'demo-ch0-q-01'));
  expectError(errors, '"demo-ch0-q-01" is used in content but not registered');
});

test('rejects ids removed from the registry', () => {
  const errors = validateWith(null, null, { baseRegistry: ['demo', 'retired-id'] });
  expectError(errors, '"retired-id" was removed');
});

test('rejects community text for an item of another chapter', () => {
  expectError(validateWith(CH0, (d) => void (d.itemTexts[0].itemId = 'demo-ch1-hq-01')), 'not an item of this chapter');
});

test('rejects a fish spot for a fish from a later chapter', () => {
  const errors = validateWith(CH0, (d) => void (d.fishSpots = [{ fishId: 'demo-ch1-fi-01', rank: 'B', where: { en: 'Town' } }]));
  expectError(errors, 'from a later chapter');
});

test('rejects a boss linked to an unknown item', () => {
  expectError(validateWith('demo/chapters/ch-01.json', (d) => void (d.bosses[0].relatedItem = 'demo-ch1-q-99')), 'refers to unknown');
});

test('rejects unregistered boss, fish and recipe ids', () => {
  const errors = validateWith('id-registry.json', (r) => r.filter((id) => !id.includes('-bs-')));
  expectError(errors, '"demo-ch1-bs-01" is used in content but not registered');
});

test('rejects a game from an unknown franchise', () => {
  expectError(validateWith('demo/game.json', (g) => void (g.franchise = 'nope')), 'unknown franchise "nope"');
});

test('rejects duplicate franchises', () => {
  expectError(validateWith('franchises.json', (f) => [...f, f[0]]), 'duplicate franchise');
});
