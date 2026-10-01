import { Chapter, Item } from '../content/content.models';
import { deadlineGroups } from './deadlines';

const item = (id: string, availableUntil: string | null): Item => ({
  id, type: 'quest', availableUntil, name: { en: id }, location: { en: '' }, hint: { en: '' }, spoilerLevel: 0, sources: [],
});
const chapter = (order: number, items: Item[], checkpoints: number[] = []): Chapter => ({
  id: `t-ch${order}`, gameId: 't', order, neutralLabel: { en: `Chapter ${order}` }, itemTexts: [], items,
  checkpoints: checkpoints.map((n) => ({ id: `t-ch${order}-cp-0${n}`, order: n, neutralDescription: { en: `cp ${order}.${n}` } })),
});

describe('deadline groups', () => {
  const ch1 = chapter(1, [item('t-ch1-q-01', 't-ch1-cp-01'), item('t-ch1-q-02', 't-ch2-cp-02'), item('t-ch1-q-03', 't-ch5-cp-01')], [1]);
  const ch2 = chapter(2, [item('t-ch2-q-01', 't-ch2-cp-02'), item('t-ch2-q-02', 't-ch2-cp-01'), item('t-ch2-q-03', null)], [1, 2]);

  it('orders what can still be lost by deadline, skipping done, open-ended and lost items', () => {
    const groups = deadlineGroups([ch2, ch1], new Set(['t-ch2-q-01']), 2);
    expect(groups.map((g) => [g.key, g.entries.map((e) => e.item.id)])).toEqual([
      ['t-ch2-cp-01', ['t-ch2-q-02']],
      ['t-ch2-cp-02', ['t-ch1-q-02']],
      ['chapter-5', ['t-ch1-q-03']],
    ]);
  });

  it('never names a checkpoint of a chapter that is not loaded', () => {
    const later = deadlineGroups([ch1], new Set(), 1).find((g) => g.chapterOrder === 5)!;
    expect(later.kind).toBe('chapter');
    expect('checkpoint' in later).toBe(false);
  });

  it('keeps the chapter each item comes from', () => {
    const [first] = deadlineGroups([ch1, ch2], new Set(), 1);
    expect(first.entries[0].chapter.id).toBe('t-ch1');
  });
});
