#!/usr/bin/env node
// Usage: node scripts/validate-content.mjs [--root content] [--base origin/main]
// --base compares id-registry.json against that git ref so ids can never be removed.
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

const errors = validateContent(values.root, { baseRegistry: readBaseRegistry(values.base, values.root) });
if (errors.length > 0) {
  console.error(errors.map((e) => `✗ ${e}`).join('\n'));
  console.error(`\n${errors.length} content error(s).`);
  process.exit(1);
}
console.log('✓ content is valid');
