import { Chapter, Trophy } from '../content/content.models';
import { routeProgress } from '../route/route';
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
      // Items made of steps that are each one thing to collect count step by step.
      const unit = (i: Chapter['items'][number]) =>
        trophy.countBy === 'steps' && i.steps?.length ? routeProgress(i, done) : { done: done.has(i.id) ? 1 : 0, total: 1 };
      return {
        trophy,
        total: counted.reduce((n, i) => n + unit(i).total, 0),
        done: counted.reduce((n, i) => n + unit(i).done, 0),
        lost: counted.filter((i) => lost.has(i.id)).reduce((n, i) => n + unit(i).total - unit(i).done, 0),
      };
    })
    .filter((p) => p.total > 0);
}
