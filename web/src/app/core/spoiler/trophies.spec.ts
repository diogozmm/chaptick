import { Chapter, Item, Trophy } from '../content/content.models';
import { trophyProgress } from './trophies';

const item = (id: string, trophies: string[] | undefined, availableUntil: string | null = null): Item => ({
  id, type: 'quest', availableUntil, name: { en: id }, location: { en: '' }, hint: { en: '' }, spoilerLevel: 0, sources: [], trophies,
});
const chapter = (order: number, items: Item[]): Chapter => ({
  id: `t-ch${order}`, gameId: 't', order, neutralLabel: { en: `Chapter ${order}` }, itemTexts: [], items,
  checkpoints: [{ id: `t-ch${order}-cp-01`, order: 1, neutralDescription: { en: 'cp' } }],
});
const trophy = (id: string, collection?: 'fish' | 'recipes'): Trophy => ({ id, name: id, description: { en: id }, collection });

describe('trophy progress', () => {
  const ch1 = chapter(1, [item('t-ch1-q-01', ['quests'], 't-ch1-cp-01'), item('t-ch1-q-02', ['quests', 'books']), item('t-ch1-q-03', undefined)]);
  const ch2 = chapter(2, [item('t-ch2-q-01', ['quests'])]);

  it('counts done and total items per trophy, ignoring items that count toward none', () => {
    const [quests, books] = trophyProgress([trophy('quests'), trophy('books')], [ch1, ch2], new Set(['t-ch1-q-02']), 2);
    expect([quests.total, quests.done]).toEqual([3, 1]);
    expect([books.total, books.done]).toEqual([1, 1]);
  });

  it('flags pending items whose deadline already passed', () => {
    const [quests] = trophyProgress([trophy('quests')], [ch1, ch2], new Set(), 2);
    expect(quests.lost).toBe(1);
    expect(trophyProgress([trophy('quests')], [ch1, ch2], new Set(['t-ch1-q-01']), 2)[0].lost).toBe(0);
  });

  it('only counts the chapters it is given and skips collection and empty trophies', () => {
    const result = trophyProgress([trophy('quests'), trophy('fish', 'fish'), trophy('other')], [ch1], new Set(), 1);
    expect(result.map((p) => [p.trophy.id, p.total])).toEqual([['quests', 2]]);
  });

  it('counts route steps instead of items for trophies that ask for it', () => {
    const entries = { ...item('t-ch1-co-01', ['notes']), steps: [{ text: { en: 'a' } }, { text: { en: 'b' } }, { text: { en: 'c' } }] };
    const plain = item('t-ch1-co-02', ['notes']);
    const chapters = [chapter(1, [entries, plain])];
    const counted = { ...trophy('notes'), countBy: 'steps' as const };
    const done = new Set(['t-ch1-co-01#step-1', 't-ch1-co-01#step-2']);
    const [p] = trophyProgress([counted], chapters, done, 1);
    expect([p.done, p.total]).toEqual([2, 4]);
    // Finishing the whole item counts every step, and without the option it is one item again.
    expect(trophyProgress([counted], chapters, new Set(['t-ch1-co-01']), 1)[0].done).toBe(3);
    expect(trophyProgress([trophy('notes')], chapters, done, 1)[0].total).toBe(2);
  });

  it('lists the items still to do, those already missed first', () => {
    const [quests] = trophyProgress([trophy('quests')], [ch1, ch2], new Set(['t-ch1-q-02']), 2);
    expect(quests.pending.map((p) => p.item.id)).toEqual(['t-ch1-q-01', 't-ch2-q-01']);
    const later = chapter(2, [item('t-ch2-q-01', ['quests']), item('t-ch2-q-02', ['quests'], 't-ch1-cp-01')]);
    const result = trophyProgress([trophy('quests')], [ch1, later], new Set(), 2)[0];
    // Done items are not listed and the missed ones (deadline in chapter 1) come before the rest.
    expect(result.pending.map((p) => p.item.id)).toEqual(['t-ch1-q-01', 't-ch2-q-02', 't-ch1-q-02', 't-ch2-q-01']);
    expect(result.pending[0].chapter.id).toBe('t-ch1');
  });
});
