import { Chapter } from '../content/content.models';
import { byChapter, fishBook, fishStats, rankAKey, recipeBook } from './collections';

const chapter = (order: number, extra: Partial<Chapter>): Chapter => ({
  id: `t-ch${order}`,
  gameId: 't',
  order,
  neutralLabel: { en: `Chapter ${order}` },
  checkpoints: [],
  items: [],
  itemTexts: [],
  ...extra,
});

const ch1 = chapter(1, {
  fish: [{ id: 't-ch1-fi-01', name: { en: 'Crab' }, sources: ['t'] }],
  fishSpots: [{ fishId: 't-ch1-fi-01', rank: 'B', where: { en: 'Harbor' } }],
  recipes: [{ id: 't-ch1-re-01', kind: 'standard', name: { en: 'Soup' }, source: { en: 'Inn' }, sources: ['t'] }],
});
const ch2 = chapter(2, {
  fish: [{ id: 't-ch2-fi-01', name: { en: 'Carp' }, sources: ['t'] }],
  fishSpots: [
    { fishId: 't-ch1-fi-01', rank: 'A', where: { en: 'Pond' } },
    { fishId: 't-ch2-fi-01', rank: 'C', where: { en: 'River' } },
  ],
  recipes: [{ id: 't-ch2-re-01', kind: 'customized', name: { en: 'Feast' }, source: { en: 'Cook soup' }, sources: ['t'] }],
});

describe('collections', () => {
  it('only knows what the given chapters reveal', () => {
    const early = fishBook([ch1]);
    expect(early.map((e) => e.fish.id)).toEqual(['t-ch1-fi-01']);
    expect(early[0].bestRank).toBe('B');
    expect(early[0].spots.map((s) => s.where.en)).toEqual(['Harbor']);
  });

  it('upgrades the best rank and sorts spots once a later region unlocks', () => {
    const crab = fishBook([ch2, ch1]).find((e) => e.fish.id === 't-ch1-fi-01')!;
    expect(crab.bestRank).toBe('A');
    expect(crab.spots.map((s) => s.where.en)).toEqual(['Pond', 'Harbor']);
    expect(crab.chapter.id).toBe('t-ch1');
  });

  it('counts catches and Rank A only for fish that can reach A', () => {
    const book = fishBook([ch1, ch2]);
    const done = new Set(['t-ch1-fi-01', rankAKey('t-ch1-fi-01'), 't-ch2-fi-01']);
    expect(fishStats(book, done)).toEqual({ caught: 2, known: 2, rankA: 1, rankAKnown: 1 });
  });

  it('works for games without ranks, keeping the bait', () => {
    const unranked = chapter(1, {
      fish: [{ id: 't-ch1-fi-01', name: { en: 'Herring' }, sources: ['t'] }],
      fishSpots: [{ fishId: 't-ch1-fi-01', where: { en: 'Docks' }, bait: 'Fishing Bait S' }],
    });
    const [entry] = fishBook([unranked]);
    expect(entry.bestRank).toBeNull();
    expect(entry.spots[0].bait).toBe('Fishing Bait S');
    expect(fishStats([entry], new Set()).rankAKnown).toBe(0);
  });

  it('lists every recipe in chapter order', () => {
    expect(recipeBook([ch2, ch1]).map((e) => e.recipe.id)).toEqual(['t-ch1-re-01', 't-ch2-re-01']);
  });

  it('groups entries by the chapter that reveals them', () => {
    const groups = byChapter(fishBook([ch2, ch1]));
    expect(groups.map((g) => [g.chapter.id, g.entries.map((e) => e.fish.id)])).toEqual([
      ['t-ch1', ['t-ch1-fi-01']],
      ['t-ch2', ['t-ch2-fi-01']],
    ]);
  });
});
