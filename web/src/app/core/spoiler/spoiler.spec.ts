import { Chapter, Item, ITEM_TYPES } from '../content/content.models';
import {
  chapterProgress,
  expiredItems,
  groupByType,
  isUnlocked,
  maskOrdinal,
  newlyLeftBehind,
  nextCheckpointAlert,
} from './spoiler';

const item = (id: string, type: Item['type'], availableUntil: string | null): Item => ({
  id,
  type,
  availableUntil,
  name: { en: id },
  location: { en: 'somewhere' },
  hint: { en: 'hint' },
  spoilerLevel: 0,
  sources: ['test'],
});

const chapter = (order: number, items: Item[], checkpoints = [1, 2]): Chapter => ({
  id: `t-ch${order}`,
  gameId: 't',
  order,
  neutralLabel: { en: `Chapter ${order}` },
  checkpoints: checkpoints.map((n) => ({ id: `t-ch${order}-cp-0${n}`, order: n, neutralDescription: { en: `cp ${n}` } })),
  items,
  itemTexts: [],
});

describe('spoiler rules', () => {
  const ch0 = chapter(0, [
    item('t-ch0-q-01', 'quest', 't-ch0-cp-01'),
    item('t-ch0-hq-01', 'hidden_quest', 't-ch0-cp-02'),
    item('t-ch0-hq-02', 'hidden_quest', 't-ch0-cp-02'),
    item('t-ch0-co-01', 'collectible', null),
    item('t-ch0-mi-01', 'missable', 't-ch1-cp-01'),
  ]);
  const ch1 = chapter(1, [item('t-ch1-q-01', 'quest', 't-ch1-cp-01')]);

  it('unlocks the current chapter and the ones before it only', () => {
    expect(isUnlocked({ order: 0 }, 1)).toBe(true);
    expect(isUnlocked({ order: 1 }, 1)).toBe(true);
    expect(isUnlocked({ order: 2 }, 1)).toBe(false);
  });

  it('numbers masked items within their type', () => {
    expect(maskOrdinal(ch0, ch0.items[2])).toBe(2);
    expect(maskOrdinal(ch0, ch0.items[0])).toBe(1);
  });

  it('alerts on the earliest checkpoint that still has pending items', () => {
    expect(nextCheckpointAlert(ch0, new Set())).toEqual({ checkpoint: ch0.checkpoints[0], pending: 1 });
    expect(nextCheckpointAlert(ch0, new Set(['t-ch0-q-01']))).toEqual({ checkpoint: ch0.checkpoints[1], pending: 2 });
  });

  it('has no alert once every deadline in the chapter is cleared', () => {
    expect(nextCheckpointAlert(ch0, new Set(['t-ch0-q-01', 't-ch0-hq-01', 't-ch0-hq-02']))).toBeNull();
  });

  it('lists items left behind in earlier chapters, ignoring open-ended and future deadlines', () => {
    const left = expiredItems([ch0, ch1], new Set(['t-ch0-hq-01']), 1).map((i) => i.id);
    expect(left).toEqual(['t-ch0-q-01', 't-ch0-hq-02']);
  });

  it('keeps items whose deadline is in a chapter that is not loaded', () => {
    expect(expiredItems([ch0], new Set(), 5).map((i) => i.id)).not.toContain('t-ch0-mi-01');
  });

  it('counts chapter progress', () => {
    expect(chapterProgress(ch0, new Set(['t-ch0-q-01', 'unknown-id']))).toEqual({ done: 1, total: 5 });
  });

  it('groups by type in display order and drops empty groups', () => {
    expect(groupByType(ch0.items, ITEM_TYPES).map((g) => g.type)).toEqual([
      'quest',
      'hidden_quest',
      'missable',
      'collectible',
    ]);
    expect(groupByType(ch1.items, ITEM_TYPES).map((g) => g.type)).toEqual(['quest']);
  });

  it('counts only what an advance newly leaves behind', () => {
    const done = new Set(['t-ch0-hq-01']);
    // Moving 0 → 1 loses the chapter 0 deadlines; 1 → 2 loses only chapter 1 ones.
    expect(newlyLeftBehind([ch0, ch1], done, 0, 1).map((i) => i.id)).toEqual(['t-ch0-q-01', 't-ch0-hq-02']);
    expect(newlyLeftBehind([ch0, ch1], done, 1, 2).map((i) => i.id)).toEqual(['t-ch0-mi-01', 't-ch1-q-01']);
  });

  it('leaves nothing behind when moving backwards', () => {
    expect(newlyLeftBehind([ch0, ch1], new Set(), 1, 0)).toEqual([]);
  });
});
