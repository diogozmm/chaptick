import { Chapter, Craft, Entry } from '../content/content.models';
import { compendiumIndex } from './compendium';
import { craftYield, madeByDefault, planCraft, planTotals } from './plan';

const entry = (id: string, kind: 'shop' | 'craft' | 'process' = 'shop'): Entry => ({
  id, name: { en: id }, category: 'materials', sources: [{ kind, where: { en: 'Somewhere' } }],
});
const craft = (id: string, makes: string, ingredients: [string, number][], name = makes): Craft => ({
  id, name: { en: name }, kind: 'craft', group: { en: 'Bench' }, makes,
  ingredients: ingredients.map(([entryId, qty]) => ({ entryId, name: { en: entryId }, qty })),
});

const area: Chapter = {
  id: 'zz-ch0', gameId: 'zz', order: 0, neutralLabel: { en: 'Area 1' }, checkpoints: [], items: [], itemTexts: [],
  entries: [
    entry('ore'), entry('wood'), entry('bar', 'process'), entry('plank'), entry('sword', 'craft'), entry('path', 'craft'),
  ],
  crafts: [
    craft('c-bar', 'bar', [['ore', 2]]),
    craft('c-plank', 'plank', [['wood', 3]]),
    craft('c-sword', 'sword', [['bar', 3], ['plank', 1]]),
    craft('c-path', 'path', [['plank', 1]], '10x path'),
  ],
};
const index = compendiumIndex([area]);
const sword = index.crafts.find((c) => c.craft.id === 'c-sword')!;

describe('plan', () => {
  it('makes an ingredient by default only when there is no other way to get it', () => {
    expect(madeByDefault(index, 'bar')).toBe(true);
    expect(madeByDefault(index, 'plank')).toBe(false);
    expect(madeByDefault(index, 'ore')).toBe(false);
  });

  it('expands made ingredients and sums what to gather', () => {
    const plan = planCraft(index, sword, 2);
    expect(plan.runs).toBe(2);
    const bar = plan.children.find((c) => c.entryId === 'bar')!;
    expect([bar.qty, bar.runs, bar.children[0].qty]).toEqual([6, 6, 12]);
    expect(planTotals(plan).map((t) => [t.entryId, t.qty])).toEqual([['ore', 12], ['plank', 2]]);
  });

  it('lets the player choose to make or buy any ingredient that has a recipe', () => {
    const made = planCraft(index, sword, 1, new Map([['plank', true], ['bar', false]]));
    expect(planTotals(made).map((t) => [t.entryId, t.qty])).toEqual([['bar', 3], ['wood', 3]]);
  });

  it('runs batch recipes only as often as needed', () => {
    const path = index.crafts.find((c) => c.craft.id === 'c-path')!;
    expect(craftYield(path.craft)).toBe(10);
    expect(planCraft(index, path, 25).runs).toBe(3);
  });

  it('uses a recipe\'s declared yield, e.g. a processor that makes two', () => {
    expect(craftYield({ ...area.crafts![0], yield: 2 })).toBe(2);
  });

  it('stops instead of looping on recipes that lead back to themselves', () => {
    const loop = compendiumIndex([{ ...area, crafts: [craft('c-a', 'ore', [['bar', 1]]), craft('c-b', 'bar', [['ore', 1]])] }]);
    const plan = planCraft(loop, loop.crafts[0], 1, new Map([['bar', true], ['ore', true]]));
    expect(plan.children[0].children[0].craft).toBeUndefined();
  });
});
