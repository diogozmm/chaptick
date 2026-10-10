import { Item } from '../content/content.models';

/** Steps are tracked next to items in the same done set: `<itemId>#step-<n>`, 1-based. */
export const stepKey = (itemId: string, index: number): string => `${itemId}#step-${index + 1}`;

export const stepKeys = (item: Item): string[] => (item.steps ?? []).map((_, i) => stepKey(item.id, i));

/** Whole-item completion also covers steps added by a later content revision. */
export const stepDone = (item: Item, index: number, done: ReadonlySet<string>): boolean =>
  done.has(item.id) || done.has(stepKey(item.id, index));

export function routeProgress(item: Item, done: ReadonlySet<string>): { done: number; total: number } {
  const keys = stepKeys(item);
  return { done: done.has(item.id) ? keys.length : keys.filter((k) => done.has(k)).length, total: keys.length };
}

/**
 * Ids to set when a step changes: finishing the last step completes the item, and unticking a
 * step reopens it.
 */
export function stepChange(item: Item, index: number, done: ReadonlySet<string>): { ids: string[]; done: boolean; alsoDone?: string[] } {
  const key = stepKey(item.id, index);
  if (done.has(item.id)) {
    // Materialize implied completion before reopening one step, in the same saved update.
    return { ids: [key, item.id], done: false, alsoDone: stepKeys(item).filter((k) => k !== key) };
  }
  if (done.has(key)) return { ids: [key, item.id], done: false };
  const others = stepKeys(item).filter((k) => k !== key);
  const completes = others.every((k) => done.has(k));
  return { ids: completes ? [key, item.id] : [key], done: true };
}

/** Ticking the whole item ticks every step; unticking it clears them. */
export function itemChange(item: Item, done: ReadonlySet<string>): { ids: string[]; done: boolean } {
  return { ids: [item.id, ...stepKeys(item)], done: !done.has(item.id) };
}
