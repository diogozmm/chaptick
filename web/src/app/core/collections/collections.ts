import { Chapter, Fish, FishRank, Recipe } from '../content/content.models';

/**
 * Fishing notebook and recipe book, built only from the chapters passed in. Callers pass the
 * unlocked chapters, so spots and dishes from later regions never show up early.
 */

/** Rank A catches are tracked next to the "caught" mark, in the same done set. */
export const rankAKey = (fishId: string): string => `${fishId}#rank-a`;

const RANK_ORDER: Record<FishRank, number> = { A: 0, B: 1, C: 2 };
const rankOrder = (rank?: FishRank): number => (rank ? RANK_ORDER[rank] : 3);

export interface FishEntry {
  fish: Fish;
  chapter: Chapter;
  /** Null for games without catch ranks. */
  bestRank: FishRank | null;
  spots: { rank?: FishRank; where: Chapter['neutralLabel']; bait?: string }[];
}

export function fishBook(chapters: readonly Chapter[]): FishEntry[] {
  const sorted = [...chapters].sort((a, b) => a.order - b.order);
  const entries = new Map<string, FishEntry>();
  for (const chapter of sorted) {
    for (const fish of chapter.fish ?? []) entries.set(fish.id, { fish, chapter, bestRank: null, spots: [] });
  }
  for (const chapter of sorted) {
    for (const spot of chapter.fishSpots ?? []) {
      entries.get(spot.fishId)?.spots.push({ rank: spot.rank, where: spot.where, bait: spot.bait });
    }
  }
  for (const entry of entries.values()) {
    // Ranked spots first, best rank first; unranked spots keep their chapter order.
    entry.spots.sort((a, b) => rankOrder(a.rank) - rankOrder(b.rank));
    entry.bestRank = entry.spots[0]?.rank ?? null;
  }
  return [...entries.values()];
}

export interface RecipeEntry {
  recipe: Recipe;
  chapter: Chapter;
}

/** Every dish in chapter order; customized dishes stay in the list with their own label. */
export function recipeBook(chapters: readonly Chapter[]): RecipeEntry[] {
  return [...chapters]
    .sort((a, b) => a.order - b.order)
    .flatMap((chapter) => (chapter.recipes ?? []).map((recipe) => ({ recipe, chapter })));
}

export interface ChapterGroup<T> {
  chapter: Chapter;
  entries: T[];
}

/** Groups entries under the chapter that first reveals them, keeping chapter order. */
export function byChapter<T extends { chapter: Chapter }>(entries: readonly T[]): ChapterGroup<T>[] {
  const groups = new Map<string, ChapterGroup<T>>();
  for (const entry of entries) {
    const group = groups.get(entry.chapter.id) ?? { chapter: entry.chapter, entries: [] };
    group.entries.push(entry);
    groups.set(entry.chapter.id, group);
  }
  return [...groups.values()].sort((a, b) => a.chapter.order - b.chapter.order);
}

export interface FishStats {
  caught: number;
  known: number;
  rankA: number;
  rankAKnown: number;
}

export function fishStats(entries: readonly FishEntry[], done: ReadonlySet<string>): FishStats {
  const withA = entries.filter((e) => e.bestRank === 'A');
  return {
    caught: entries.filter((e) => done.has(e.fish.id)).length,
    known: entries.length,
    rankA: withA.filter((e) => done.has(rankAKey(e.fish.id))).length,
    rankAKnown: withA.length,
  };
}
