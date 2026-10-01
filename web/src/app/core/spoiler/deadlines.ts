import { Chapter, Checkpoint, Item } from '../content/content.models';
import { chapterOrderOf } from './spoiler';

export interface DeadlineEntry {
  chapter: Chapter;
  item: Item;
}

/**
 * Pending items that can still be done but will be lost, grouped by when they are lost:
 * - a checkpoint of a loaded (unlocked) chapter, shown with its neutral description;
 * - a later, locked chapter, whose checkpoints must not be shown: only the chapter is named.
 */
export type DeadlineGroup =
  | { kind: 'checkpoint'; key: string; chapterOrder: number; checkpoint: Checkpoint; entries: DeadlineEntry[] }
  | { kind: 'chapter'; key: string; chapterOrder: number; entries: DeadlineEntry[] };

/**
 * "What can I still miss": every pending item with a deadline in the current chapter or later,
 * earliest deadline first. Items already left behind are not here (the checklist lists those).
 * Only the chapters passed in are read, and callers pass the unlocked ones.
 */
export function deadlineGroups(chapters: readonly Chapter[], done: ReadonlySet<string>, currentOrder: number): DeadlineGroup[] {
  const checkpoints = new Map<string, { checkpoint: Checkpoint; chapterOrder: number }>();
  for (const chapter of chapters) {
    for (const checkpoint of chapter.checkpoints) checkpoints.set(checkpoint.id, { checkpoint, chapterOrder: chapter.order });
  }
  const groups = new Map<string, DeadlineGroup>();
  for (const chapter of [...chapters].sort((a, b) => a.order - b.order)) {
    for (const item of chapter.items) {
      const until = item.availableUntil;
      if (until === null || done.has(item.id)) continue;
      const known = checkpoints.get(until);
      const chapterOrder = known?.chapterOrder ?? chapterOrderOf(until);
      if (chapterOrder === undefined || chapterOrder < currentOrder) continue;
      const key = known ? until : `chapter-${chapterOrder}`;
      if (!groups.has(key)) {
        groups.set(
          key,
          known
            ? { kind: 'checkpoint', key, chapterOrder, checkpoint: known.checkpoint, entries: [] }
            : { kind: 'chapter', key, chapterOrder, entries: [] },
        );
      }
      groups.get(key)!.entries.push({ chapter, item });
    }
  }
  const rank = (g: DeadlineGroup) => (g.kind === 'checkpoint' ? g.checkpoint.order : Number.MAX_SAFE_INTEGER);
  return [...groups.values()].sort((a, b) => a.chapterOrder - b.chapterOrder || rank(a) - rank(b));
}
