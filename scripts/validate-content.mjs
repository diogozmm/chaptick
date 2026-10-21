#!/usr/bin/env node
// Usage: node scripts/validate-content.mjs [--root content] [--base origin/main]
// --base compares id-registry.json and the route steps against that git ref, so ids can never be
// removed and published steps can only grow at the end.
import { execFileSync } from 'node:child_process';
import { parseArgs } from 'node:util';
import { validateContent } from './content-validation.mjs';

const { values } = parseArgs({
  options: { root: { type: 'string', default: 'content' }, base: { type: 'string', default: 'origin/main' } },
});

function readBaseRegistry(ref, root) {
  try {
    const raw = execFileSync('git', ['show', `${ref}:${root}/id-registry.json`], { stdio: ['ignore', 'pipe', 'ignore'] });
    return JSON.parse(raw.toString());
  } catch {
    console.warn(`warning: ${ref}:${root}/id-registry.json not found; skipping append-only check`);
    return undefined;
  }
}

/** English text of every published route step, by item id, read from the chapter files at `ref`. */
function readBaseSteps(ref, root) {
  try {
    const git = (...args) => execFileSync('git', args, { stdio: ['ignore', 'pipe', 'ignore'], maxBuffer: 64 * 1024 * 1024 }).toString();
    const files = git('ls-tree', '-r', '--name-only', ref, `${root}/`).split('\n').filter((f) => /\/chapters\/ch-\d+\.json$/.test(f));
    if (files.length === 0) throw new Error('no chapters');
    const steps = new Map();
    for (const file of files) {
      for (const item of JSON.parse(git('show', `${ref}:${file}`)).items ?? []) {
        if (item.steps?.length) steps.set(item.id, item.steps.map((step) => step.text.en));
      }
    }
    return steps;
  } catch {
    console.warn(`warning: chapters at ${ref} not found; skipping the route step check`);
    return undefined;
  }
}

const errors = validateContent(values.root, {
  baseRegistry: readBaseRegistry(values.base, values.root),
  baseSteps: readBaseSteps(values.base, values.root),
});
if (errors.length > 0) {
  console.error(errors.map((e) => `✗ ${e}`).join('\n'));
  console.error(`\n${errors.length} content error(s).`);
  process.exit(1);
}
console.log('✓ content is valid');
