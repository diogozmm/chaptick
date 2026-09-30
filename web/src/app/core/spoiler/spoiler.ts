import { Chapter, ChapterSummary, Checkpoint, Item, ItemType, SpoilerLevel } from '../content/content.models';

/**
 * The spoiler rules, kept pure so they can be tested without Angular. The central rule:
 * nothing from a chapter after the current one is ever loaded or shown.
 */

export const isUnlocked = (chapter: Pick<ChapterSummary, 'order'>, currentOrder: number): boolean =>
  chapter.order <= currentOrder;

/** Level 1 hides the name behind a tap; level 2 also asks for confirmation. */
export const isMasked = (level: SpoilerLevel): boolean => level > 0;
export const needsConfirmation = (level: SpoilerLevel): boolean => level === 2;

/** 1-based position among the chapter's items of the same type, for labels like "Hidden quest #2". */
export function maskOrdinal(chapter: Chapter, item: Item): number {
  return chapter.items.filter((i) => i.type === item.type).findIndex((i) => i.id === item.id) + 1;
}

export interface CheckpointAlert {
  checkpoint: Checkpoint;
  pending: number;
}

/**
 * The earliest point of no return in the chapter that still has pending items.
 * Powers "Before X, 3 items are still missing".
 */
export function nextCheckpointAlert(chapter: Chapter, done: ReadonlySet<string>): CheckpointAlert | null {
  const checkpoints = [...chapter.checkpoints].sort((a, b) => a.order - b.order);
  for (const checkpoint of checkpoints) {
    const pending = chapter.items.filter((i) => i.availableUntil === checkpoint.id && !done.has(i.id)).length;
    if (pending > 0) return { checkpoint, pending };
  }
  return null;
}

/**
 * Pending items whose deadline sits in a chapter before `beforeOrder`: what the player left
 * behind once they reached that chapter. Deadlines in chapters that are not loaded are
 * treated as still open, since they can only be in the future.
 */
export function expiredItems(chapters: readonly Chapter[], done: ReadonlySet<string>, beforeOrder: number): Item[] {
  const checkpointOrder = new Map<string, number>();
  for (const chapter of chapters) {
    for (const checkpoint of chapter.checkpoints) checkpointOrder.set(checkpoint.id, chapter.order);
  }
  return chapters
    .flatMap((c) => c.items)
    .filter((item) => {
      if (done.has(item.id) || item.availableUntil === null) return false;
      const order = checkpointOrder.get(item.availableUntil);
      return order !== undefined && order < beforeOrder;
    });
}

export interface Progress {
  done: number;
  total: number;
}

export function chapterProgress(chapter: Chapter, done: ReadonlySet<string>): Progress {
  return { done: chapter.items.filter((i) => done.has(i.id)).length, total: chapter.items.length };
}

export function groupByType(items: readonly Item[], order: readonly ItemType[]): { type: ItemType; items: Item[] }[] {
  return order.map((type) => ({ type, items: items.filter((i) => i.type === type) })).filter((g) => g.items.length > 0);
}

/** Items that moving from `fromOrder` to `toOrder` would leave behind, excluding ones already lost. */
export function newlyLeftBehind(
  chapters: readonly Chapter[],
  done: ReadonlySet<string>,
  fromOrder: number,
  toOrder: number,
): Item[] {
  const alreadyLost = new Set(expiredItems(chapters, done, fromOrder).map((i) => i.id));
  return expiredItems(chapters, done, toOrder).filter((i) => !alreadyLost.has(i.id));
}
