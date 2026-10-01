import { Chapter, Item } from '../content/content.models';
import { checklistOrder, itemStatus, neighbours, sourceLabel } from './item-status';

const item = (id: string, type: Item['type'], availableUntil: string | null = null): Item => ({
  id, type, availableUntil, name: { en: id }, location: { en: '' }, hint: { en: '' }, spoilerLevel: 0, sources: [],
});

const chapter: Chapter = {
  id: 't-ch2', gameId: 't', order: 2, neutralLabel: { en: 'Chapter 2' }, checkpoints: [], itemTexts: [],
  items: [item('t-ch2-co-01', 'collectible'), item('t-ch2-q-01', 'quest'), item('t-ch2-mi-01', 'missable'), item('t-ch2-q-02', 'quest')],
};

describe('item status', () => {
  it('tells done, lost, urgent, later and open-ended items apart', () => {
    const done = new Set(['t-ch2-q-09']);
    expect(itemStatus(item('t-ch2-q-09', 'quest', 't-ch2-cp-01'), done, 2)).toBe('done');
    expect(itemStatus(item('a', 'quest', 't-ch1-cp-01'), done, 2)).toBe('left-behind');
    expect(itemStatus(item('b', 'quest', 't-ch2-cp-01'), done, 2)).toBe('this-chapter');
    expect(itemStatus(item('c', 'quest', 't-ch7-cp-03'), done, 2)).toBe('later');
    expect(itemStatus(item('d', 'quest'), done, 2)).toBe('none');
  });
});

describe('checklist order', () => {
  it('follows type order, then authoring order', () => {
    expect(checklistOrder(chapter, [], 't-ch2-q-01').map((i) => i.id)).toEqual(['t-ch2-q-01', 't-ch2-q-02', 't-ch2-mi-01', 't-ch2-co-01']);
  });

  it('honors type filters, unless the item itself is filtered out', () => {
    expect(checklistOrder(chapter, ['quest'], 't-ch2-q-02').map((i) => i.id)).toEqual(['t-ch2-q-01', 't-ch2-q-02']);
    expect(checklistOrder(chapter, ['quest'], 't-ch2-co-01')).toHaveLength(4);
  });

  it('finds the neighbours without wrapping around', () => {
    const list = checklistOrder(chapter, [], 't-ch2-q-01');
    expect(neighbours(list, 't-ch2-q-01')).toMatchObject({ prev: undefined, next: { id: 't-ch2-q-02' }, index: 0 });
    expect(neighbours(list, 't-ch2-co-01')).toMatchObject({ prev: { id: 't-ch2-mi-01' }, next: undefined, index: 3 });
  });

  it('cleans source labels', () => {
    expect(sourceLabel('guide: Neoseeker Ys X walkthrough, Chapter 5')).toBe('Neoseeker Ys X walkthrough, Chapter 5');
  });
});
