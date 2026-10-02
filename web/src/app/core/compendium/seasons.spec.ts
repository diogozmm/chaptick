import { Chapter } from '../content/content.models';
import { compendiumIndex } from './compendium';
import { hasSeasons, nextSeason, seasonView } from './seasons';

const area = (order: number, extra: Partial<Chapter>): Chapter => ({
  id: `zz-ch${order}`, gameId: 'zz', order, neutralLabel: { en: `Area ${order + 1}` },
  checkpoints: [], items: [], itemTexts: [], ...extra,
});
const fish = (id: string, seasons?: ('spring' | 'summer' | 'autumn' | 'winter')[]) => ({
  id, name: { en: id }, category: 'fish' as const, sources: [{ kind: 'fish' as const, where: { en: 'Lake' }, ...(seasons ? { seasons } : {}) }],
});

const lake = area(0, {
  entries: [
    fish('carp', ['autumn', 'winter']), fish('eel'), fish('perch', ['summer']), fish('koi', ['winter']),
    { id: 'berry', name: { en: 'berry' }, category: 'crops', sources: [
      { kind: 'forage', where: { en: 'Town' }, seasons: ['autumn'] }, { kind: 'shop', where: { en: 'Store' } }] },
  ],
});
const woods = area(1, { entries: [fish('ghost', ['autumn'])] });
const seed = (id: string, seasons: ('spring' | 'summer' | 'autumn' | 'winter')[]) => ({
  id, name: { en: id }, category: 'seeds' as const, sources: [{ kind: 'shop' as const, where: { en: 'Store' } }],
  grow: { seasons, days: 8, harvests: 1, yield: '1' },
});
const farm = area(0, { entries: [seed('wheat', ['spring', 'summer', 'autumn']), seed('squash', ['autumn']), seed('soulfruit', ['spring', 'summer', 'autumn', 'winter'])] });

describe('seasons', () => {
  it('wraps the year around', () => {
    expect(nextSeason('winter')).toBe('spring');
  });

  it('splits what only this season has, what it also has, and what comes next', () => {
    const view = seasonView(compendiumIndex([lake]), 'autumn');
    expect(view.only.map((e) => [e.entry.entry.id, e.lastChance])).toEqual([['carp', false]]);
    expect(view.also.map((e) => e.entry.entry.id)).toEqual(['berry']);
    expect(view.coming.map((e) => e.entry.entry.id)).toEqual(['koi']);
  });

  it('marks the last chance before a fish goes away for the next season', () => {
    const view = seasonView(compendiumIndex([lake]), 'summer');
    expect(view.only.map((e) => [e.entry.entry.id, e.lastChance])).toEqual([['perch', true]]);
  });

  it('lists what can be planted now: last chances first, all-year seeds last', () => {
    const view = seasonView(compendiumIndex([farm]), 'autumn');
    expect(view.plant.map((p) => [p.entry.entry.id, p.lastChance])).toEqual([['squash', true], ['wheat', true], ['soulfruit', false]]);
    expect(seasonView(compendiumIndex([farm]), 'winter').plant.map((p) => p.entry.entry.id)).toEqual(['soulfruit']);
  });

  it('only knows the areas passed in', () => {
    expect(seasonView(compendiumIndex([lake]), 'autumn').only.some((e) => e.entry.entry.id === 'ghost')).toBe(false);
    // Last chances come first: the ghost fish is autumn-only, the carp stays into winter.
    expect(seasonView(compendiumIndex([lake, woods]), 'autumn').only.map((e) => e.entry.entry.id)).toEqual(['ghost', 'carp']);
    expect(hasSeasons(compendiumIndex([area(0, { entries: [fish('eel')] })]))).toBe(false);
  });
});
