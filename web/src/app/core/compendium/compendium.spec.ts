import { Chapter } from '../content/content.models';
import { categoryCounts, compendiumIndex, findEntries } from './compendium';

const chapter = (order: number, extra: Partial<Chapter>): Chapter => ({
  id: `zz-ch${order}`, gameId: 'zz', order, neutralLabel: { en: `Area ${order + 1}` },
  checkpoints: [], items: [], itemTexts: [], ...extra,
});

const area1 = chapter(0, {
  entries: [
    { id: 'zz-bitter-herb', name: { en: 'Bitter Herb' }, category: 'materials', sources: [{ kind: 'forage', where: { en: 'Town' } }] },
    { id: 'zz-herb-tea', name: { en: 'Herb Tea', pt: 'Chá de Ervas' }, category: 'food', sources: [{ kind: 'cook', where: { en: 'Kettle' } }] },
  ],
  crafts: [{
    id: 'zz-cook-herb-tea', name: { en: 'Herb Tea' }, kind: 'cook', group: { en: 'Kettle' }, makes: 'zz-herb-tea',
    ingredients: [{ entryId: 'zz-bitter-herb', name: { en: 'Bitter Herb' }, qty: 2 }],
  }],
});
area1.commonGifts = { likes: [{ name: { en: 'Herb Tea' } }], neutral: [{ entryId: 'zz-bitter-herb', name: { en: 'Bitter Herb' } }] };
area1.villagers = [{ id: 'zz-vl-ada', name: { en: 'Ada' }, gifts: { loves: [{ entryId: 'zz-herb-tea', name: { en: 'Herb Tea' } }], hates: [{ name: { en: 'Rock' } }] } }];
const area2 = chapter(1, {
  entries: [{ id: 'zz-bone', name: { en: 'Bone' }, category: 'materials', sources: [{ kind: 'loot', where: { en: 'Crypt' } }] }],
  entrySources: [{ entryId: 'zz-bitter-herb', kind: 'shop', where: { en: 'Crypt Market' } }],
  creatures: [{
    id: 'zz-cr-ghoul', name: { en: 'Ghoul' }, where: [{ en: 'Crypt' }], spoilerLevel: 0,
    rewards: [{ how: 'steal', items: [{ entryId: 'zz-bitter-herb', name: { en: 'Bitter Herb' } }], chance: '25%' }],
  }],
});

describe('compendium', () => {
  it('joins later sources onto earlier entries, in chapter order', () => {
    const index = compendiumIndex([area2, area1]);
    const herb = index.entries.get('zz-bitter-herb')!;
    expect(herb.chapter.order).toBe(0);
    expect(herb.sources.map((s) => [s.source.where.en, s.chapter.order])).toEqual([['Town', 0], ['Crypt Market', 1]]);
  });

  it('only knows what the chapters passed in reveal', () => {
    const index = compendiumIndex([area1]);
    expect(index.entries.has('zz-bone')).toBe(false);
    expect(index.entries.get('zz-bitter-herb')!.sources).toHaveLength(1);
    expect(index.givenBy.size).toBe(0);
  });

  it('links crafts and creatures both ways', () => {
    const index = compendiumIndex([area1, area2]);
    expect(index.madeBy.get('zz-herb-tea')!.map((c) => c.craft.id)).toEqual(['zz-cook-herb-tea']);
    expect(index.usedIn.get('zz-bitter-herb')!.map((c) => c.craft.id)).toEqual(['zz-cook-herb-tea']);
    expect(index.givenBy.get('zz-bitter-herb')!.map((c) => c.creature.id)).toEqual(['zz-cr-ghoul']);
  });

  it('links what a creature or villager gives by name once that item is reached', () => {
    const later = chapter(1, { entries: [{ id: 'zz-rock', name: { en: 'Rock' }, category: 'materials', sources: [{ kind: 'gather', where: { en: 'Pit' } }] }] });
    expect(compendiumIndex([area1]).gifts.has('zz-rock')).toBe(false);
    const index = compendiumIndex([area1, later]);
    expect(index.gifts.get('zz-rock')!.map((g) => g.reaction)).toEqual(['hates']);
    expect(index.villagers[0].gifts.hates![0].entryId).toBe('zz-rock');
  });

  it('knows how each villager reacts to an item', () => {
    const index = compendiumIndex([area1]);
    expect(index.villagers.map((v) => v.id)).toEqual(['zz-vl-ada']);
    expect(index.gifts.get('zz-herb-tea')!.map((g) => [g.villager.id, g.reaction])).toEqual([['zz-vl-ada', 'loves']]);
    // Common lists are linked by name too.
    expect(index.commonGift.get('zz-herb-tea')).toBe('likes');
    expect(index.commonGift.get('zz-bitter-herb')).toBe('neutral');
  });

  it('finds by every word, names starting with the query first, ignoring accents and case', () => {
    const index = compendiumIndex([area1, area2]);
    expect(findEntries(index, 'herb', 'en').map((e) => e.entry.id)).toEqual(['zz-herb-tea', 'zz-bitter-herb']);
    expect(findEntries(index, 'HÉRB tea', 'en').map((e) => e.entry.id)).toEqual(['zz-herb-tea']);
    // In Portuguese both names are searched: the game may show either.
    expect(findEntries(index, 'chá', 'pt').map((e) => e.entry.id)).toEqual(['zz-herb-tea']);
    expect(findEntries(index, 'herb tea', 'pt').map((e) => e.entry.id)).toEqual(['zz-herb-tea']);
    // The player's own name finds it too, and comes first.
    expect(findEntries(index, 'cha mate', 'pt', null, { 'zz-herb-tea': 'Chá Mate' }).map((e) => e.entry.id)).toEqual(['zz-herb-tea']);
    expect(findEntries(index, '', 'en')).toEqual([]);
    expect(findEntries(index, '', 'en', 'materials').map((e) => e.entry.id)).toEqual(['zz-bitter-herb', 'zz-bone']);
    expect(categoryCounts(index).get('materials')).toBe(2);
  });
});
