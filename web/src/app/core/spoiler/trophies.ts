import { Chapter, Trophy } from '../content/content.models';
import { expiredItems } from './spoiler';

export interface TrophyProgress {
  trophy: Trophy;
  done: number;
  total: number;
  /** Pending items whose deadline has already passed: the trophy may no longer be possible. */
  lost: number;
}

/**
 * How far each checklist trophy is, counting only the chapters passed in (the unlocked ones), so
 * the totals never reveal what lies ahead. Trophies tied to a whole collection are left out:
 * the collections screen already shows them.
 */
export function trophyProgress(
  trophies: readonly Trophy[],
  chapters: readonly Chapter[],
  done: ReadonlySet<string>,
  currentOrder: number,
): TrophyProgress[] {
  const items = chapters.flatMap((c) => c.items);
  const lost = new Set(expiredItems(chapters, done, currentOrder).map((i) => i.id));
  return trophies
    .filter((t) => !t.collection)
    .map((trophy) => {
      const counted = items.filter((i) => i.trophies?.includes(trophy.id));
      return {
        trophy,
        total: counted.length,
        done: counted.filter((i) => done.has(i.id)).length,
        lost: counted.filter((i) => lost.has(i.id)).length,
      };
    })
    .filter((p) => p.total > 0);
}
