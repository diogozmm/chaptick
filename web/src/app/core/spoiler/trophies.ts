import { Chapter, Item, Trophy } from '../content/content.models';
import { routeProgress } from '../route/route';
import { expiredItems } from './spoiler';

export interface TrophyProgress {
  trophy: Trophy;
  done: number;
  total: number;
  /** Pending items whose deadline has already passed: the trophy may no longer be possible. */
  lost: number;
  /** The items still to do, those already missed first, in the order of the chapters. */
  pending: { chapter: Chapter; item: Item }[];
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
  const lost = new Set(expiredItems(chapters, done, currentOrder).map((i) => i.id));
  return trophies
    .filter((t) => !t.collection)
    .map((trophy) => {
      const counted = chapters.flatMap((chapter) =>
        chapter.items.filter((i) => i.trophies?.includes(trophy.id)).map((item) => ({ chapter, item })),
      );
      // Items made of steps that are each one thing to collect count step by step.
      const unit = (i: Item) =>
        trophy.countBy === 'steps' && i.steps?.length ? routeProgress(i, done) : { done: done.has(i.id) ? 1 : 0, total: 1 };
      const pending = counted.filter(({ item }) => !done.has(item.id));
      return {
        trophy,
        total: counted.reduce((n, { item }) => n + unit(item).total, 0),
        done: counted.reduce((n, { item }) => n + unit(item).done, 0),
        lost: counted.filter(({ item }) => lost.has(item.id)).reduce((n, { item }) => n + unit(item).total - unit(item).done, 0),
        pending: [...pending.filter(({ item }) => lost.has(item.id)), ...pending.filter(({ item }) => !lost.has(item.id))],
      };
    })
    .filter((p) => p.total > 0);
}
