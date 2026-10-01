import { Chapter, Fish, FishRank, Recipe } from '../content/content.models';

/**
 * Fishing notebook and recipe book, built only from the chapters passed in. Callers pass the
 * unlocked chapters, so spots and dishes from later regions never show up early.
 */

/** Rank A catches are tracked next to the "caught" mark, in the same done set. */
export const rankAKey = (fishId: string): string => `${fishId}#rank-a`;

const RANK_ORDER: Record<FishRank, number> = { A: 0, B: 1, C: 2 };

export interface FishEntry {
  fish: Fish;
  chapter: Chapter;
  bestRank: FishRank;
  spots: { rank: FishRank; where: Chapter['neutralLabel'] }[];
}

export function fishBook(chapters: readonly Chapter[]): FishEntry[] {
  const sorted = [...chapters].sort((a, b) => a.order - b.order);
  const entries = new Map<string, FishEntry>();
  for (const chapter of sorted) {
    for (const fish of chapter.fish ?? []) entries.set(fish.id, { fish, chapter, bestRank: 'C', spots: [] });
  }
  for (const chapter of sorted) {
    for (const spot of chapter.fishSpots ?? []) entries.get(spot.fishId)?.spots.push({ rank: spot.rank, where: spot.where });
  }
  for (const entry of entries.values()) {
    entry.spots.sort((a, b) => RANK_ORDER[a.rank] - RANK_ORDER[b.rank]);
    entry.bestRank = entry.spots[0]?.rank ?? 'C';
  }
  return [...entries.values()];
}

export interface RecipeEntry {
  recipe: Recipe;
  chapter: Chapter;
}

export function recipeBook(chapters: readonly Chapter[]): { standard: RecipeEntry[]; customized: RecipeEntry[] } {
  const all = [...chapters]
    .sort((a, b) => a.order - b.order)
    .flatMap((chapter) => (chapter.recipes ?? []).map((recipe) => ({ recipe, chapter })));
  return {
    standard: all.filter((e) => e.recipe.kind === 'standard'),
    customized: all.filter((e) => e.recipe.kind === 'customized'),
  };
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
