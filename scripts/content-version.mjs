import { createHash } from 'node:crypto';

// Object key order is not content; array order is (notably positional route steps).
const canonical = (value) => {
  if (Array.isArray(value)) return value.map(canonical);
  if (value !== null && typeof value === 'object') {
    return Object.fromEntries(Object.keys(value).sort().map((key) => [key, canonical(value[key])]));
  }
  return value;
};

/** Opaque, deterministic cache version. 48 bits fit exactly in JS and older numeric clients. */
export function contentVersion(game, chapters) {
  const content = canonical({ game, chapters: [...chapters].sort((a, b) => a.order - b.order) });
  return Number.parseInt(createHash('sha256').update(JSON.stringify(content)).digest('hex').slice(0, 12), 16) + 1;
}
