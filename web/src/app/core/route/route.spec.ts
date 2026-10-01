import { Item } from '../content/content.models';
import { itemChange, routeProgress, stepChange, stepKey } from './route';

const item: Item = {
  id: 't-ch0-co-01',
  type: 'collectible',
  name: { en: 'Chests (3)' },
  location: { en: 'Cave' },
  availableUntil: null,
  hint: { en: 'h' },
  spoilerLevel: 0,
  sources: ['t'],
  steps: [{ text: { en: 'a' } }, { text: { en: 'b' } }, { text: { en: 'c' } }],
};

describe('route steps', () => {
  it('uses 1-based keys next to the item id', () => {
    expect(stepKey(item.id, 0)).toBe('t-ch0-co-01#step-1');
  });

  it('counts finished steps', () => {
    expect(routeProgress(item, new Set([stepKey(item.id, 1)]))).toEqual({ done: 1, total: 3 });
  });

  it('completes the item with the last step', () => {
    const done = new Set([stepKey(item.id, 0), stepKey(item.id, 2)]);
    expect(stepChange(item, 1, done)).toEqual({ ids: [stepKey(item.id, 1), item.id], done: true });
    expect(stepChange(item, 1, new Set())).toEqual({ ids: [stepKey(item.id, 1)], done: true });
  });

  it('reopens the item when a step is unticked', () => {
    const done = new Set([item.id, stepKey(item.id, 0)]);
    expect(stepChange(item, 0, done)).toEqual({ ids: [stepKey(item.id, 0), item.id], done: false });
  });

  it('ticks or clears every step with the item', () => {
    expect(itemChange(item, new Set())).toEqual({
      ids: [item.id, stepKey(item.id, 0), stepKey(item.id, 1), stepKey(item.id, 2)],
      done: true,
    });
    expect(itemChange(item, new Set([item.id])).done).toBe(false);
  });
});
