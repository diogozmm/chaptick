import { Chapter, ITEM_TYPES, Item, ItemType } from '../content/content.models';
import { chapterOrderOf, groupByType } from './spoiler';

/**
 * Where an item stands for the player, shown at the top of its detail page:
 * done, already lost, expiring in the current chapter, expiring later, or no deadline.
 */
export type ItemStatus = 'done' | 'left-behind' | 'this-chapter' | 'later' | 'none';

export function itemStatus(item: Item, done: ReadonlySet<string>, currentOrder: number): ItemStatus {
  if (done.has(item.id)) return 'done';
  if (item.availableUntil === null) return 'none';
  const order = chapterOrderOf(item.availableUntil);
  if (order === undefined) return 'none';
  if (order < currentOrder) return 'left-behind';
  return order === currentOrder ? 'this-chapter' : 'later';
}

/**
 * The chapter's items in checklist order (by type, then authoring order), honoring the type
 * filters when the item itself passes them. "Hide done" is ignored on purpose: ticking an item
 * must not make the arrows jump.
 */
export function checklistOrder(chapter: Chapter, filters: readonly ItemType[], itemId: string): Item[] {
  const filtered = filters.length ? chapter.items.filter((i) => filters.includes(i.type)) : chapter.items;
  const list = filtered.some((i) => i.id === itemId) ? filtered : chapter.items;
  return groupByType(list, ITEM_TYPES).flatMap((g) => g.items);
}

export function neighbours<T extends { id: string }>(list: readonly T[], id: string): { prev?: T; next?: T; index: number } {
  const index = list.findIndex((e) => e.id === id);
  return index < 0 ? { index } : { prev: list[index - 1], next: list[index + 1], index };
}

/** "guide: Neoseeker Ys X walkthrough, Chapter 5" → "Neoseeker Ys X walkthrough, Chapter 5". */
export const sourceLabel = (source: string): string => source.replace(/^guide:\s*/i, '');
