import { Chapter, Item } from '../content/content.models';
import { normalize, searchItems } from './search';

const item = (id: string, name: string, extra: Partial<Item> = {}): Item => ({
  id, type: 'collectible', availableUntil: null, name: { en: name }, location: { en: `${name} area` },
  hint: { en: 'A long hint about nothing in particular, then the Hidden Lever near the end of a very long sentence.' },
  spoilerLevel: 0, sources: [], ...extra,
});
const chapter = (order: number, items: Item[]): Chapter => ({
  id: `t-ch${order}`, gameId: 't', order, neutralLabel: { en: `Chapter ${order}` }, checkpoints: [], itemTexts: [], items,
});

const all = { name: () => true, hint: () => true };

describe('search', () => {
  const ch1 = chapter(1, [
    item('t-ch1-co-01', 'Termina Island treasure chests', { steps: [{ text: { en: 'East side — Gale Boots' } }] }),
    item('t-ch1-co-02', 'Öland Island chests'),
  ]);
  const ch2 = chapter(2, [item('t-ch2-q-01', 'Gale Hunt'), item('t-ch2-hq-01', 'Secret Gale', { spoilerLevel: 1 })]);

  it('finds route steps, ignoring case and accents', () => {
    const [hit] = searchItems([ch1], 'gale boots', 'en', all);
    expect(hit.item.id).toBe('t-ch1-co-01');
    expect(hit.field).toBe('step');
    expect(hit.text.slice(hit.start, hit.start + hit.length)).toBe('Gale');
    expect(searchItems([ch1], 'oland', 'en', all).map((h) => h.item.id)).toEqual(['t-ch1-co-02']);
    expect(normalize('Öland Ação')).toBe('oland acao');
  });

  it('ranks name matches before route steps', () => {
    expect(searchItems([ch1, ch2], 'gale', 'en', all).map((h) => [h.item.id, h.field])).toEqual([
      ['t-ch2-q-01', 'name'],
      ['t-ch2-hq-01', 'name'],
      ['t-ch1-co-01', 'step'],
    ]);
  });

  it('never searches what is masked', () => {
    const masked = { name: (i: Item) => i.spoilerLevel === 0, hint: (i: Item) => i.spoilerLevel !== 1 };
    expect(searchItems([ch2], 'secret', 'en', masked)).toEqual([]);
  });

  it('cuts long hints around the match', () => {
    const [hit] = searchItems([ch1], 'lever', 'en', all);
    expect(hit.field).toBe('hint');
    expect(hit.text.startsWith('…')).toBe(true);
    expect(hit.text.slice(hit.start, hit.start + hit.length)).toBe('Lever');
  });

  it('waits for at least two characters', () => {
    expect(searchItems([ch1], 'g', 'en', all)).toEqual([]);
  });
});
