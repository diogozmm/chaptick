import { TestBed } from '@angular/core/testing';

import { compendiumIndex } from '../compendium/compendium';
import { Chapter } from '../content/content.models';
import { GlobalSearch, ReachedGame } from './global-search';

const area = (order: number, extra: Partial<Chapter>): Chapter => ({
  id: `zz-ch${order}`, gameId: 'zz', order, neutralLabel: { en: `Area ${order + 1}` }, checkpoints: [], items: [], itemTexts: [], ...extra,
});
const reached = (chapters: Chapter[], names: Record<string, string> = {}): ReachedGame => ({
  gameId: 'zz', game: { id: 'zz', name: { en: 'Zed' }, platforms: [], chapterCount: 2, itemCount: 1 }, chapters,
  index: compendiumIndex(chapters), names,
});

const town = area(0, {
  items: [
    { id: 'zz-ch0-q-01', type: 'quest', name: { en: 'Fence Task' }, location: { en: 'Farm' }, availableUntil: null, hint: { en: 'Fix it' }, spoilerLevel: 0, sources: [] },
    { id: 'zz-ch0-hq-01', type: 'hidden_quest', name: { en: 'Secret Fence' }, location: { en: 'Barn' }, availableUntil: null, hint: { en: 'Shh' }, spoilerLevel: 1, sources: [] },
  ],
  entries: [{ id: 'zz-fence-post', name: { en: 'Fence Post', pt: 'Mourão' }, category: 'materials', sources: [{ kind: 'shop', where: { en: 'Store' } }] }],
  creatures: [{ id: 'zz-cr-fence-ghost', name: { en: 'Fence Ghost' }, where: [], spoilerLevel: 0 }],
  villagers: [{ id: 'zz-vl-fenna', name: { en: 'Fenna' }, gifts: {} }],
});

describe('GlobalSearch', () => {
  const search = () => TestBed.inject(GlobalSearch);

  it('finds tasks, items, creatures and villagers in what was reached, never masked names', () => {
    const results = search().search(reached([town]), 'fen', 'en');
    expect(results.items.map((h) => h.item.id)).toEqual(['zz-ch0-q-01']);
    expect(results.related).toEqual([]);
    expect(results.entries.map((e) => e.entry.id)).toEqual(['zz-fence-post']);
    expect(results.creatures.map((c) => c.creature.id)).toEqual(['zz-cr-fence-ghost']);
    expect(results.villagers.map((v) => v.id)).toEqual(['zz-vl-fenna']);
    expect(results.total).toBe(4);
  });

  it('lists items that only match in a hint after everything matched by name', () => {
    const results = search().search(reached([town]), 'fix', 'en');
    expect(results.items).toEqual([]);
    expect(results.related.map((h) => h.item.id)).toEqual(['zz-ch0-q-01']);
  });

  it('matches the player\'s own names and both languages', () => {
    expect(search().search(reached([town]), 'mourao', 'pt').entries.length).toBe(1);
    expect(search().search(reached([town], { 'zz-fence-post': 'Estaca' }), 'estaca', 'pt').entries.length).toBe(1);
  });
});
