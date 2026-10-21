import { signal } from '@angular/core';
import { TestBed } from '@angular/core/testing';
import { TranslocoService } from '@jsverse/transloco';

import { Chapter, Item } from '../content/content.models';
import { ContentService } from '../content/content.service';
import { ActiveGame } from '../game/active-game';
import { ChapterAccess } from './chapter-access';
import { ItemView } from './item-view';

const item = (id: string, availableUntil: string | null): Item => ({
  id, type: 'quest', availableUntil, name: { en: id }, location: { en: '' }, hint: { en: '' }, spoilerLevel: 0, sources: [],
});
const chapter = (order: number, items: Item[]): Chapter => ({
  id: `t-ch${order}`, gameId: 't', order, neutralLabel: { en: `Chapter ${order}` }, itemTexts: [], items,
  checkpoints: [{ id: `t-ch${order}-cp-01`, order: 1, neutralDescription: { en: `description ${order}` } }],
});

describe('ItemView deadline', () => {
  const ch1 = chapter(1, [item('t-ch1-q-01', 't-ch2-cp-01')]);
  const ch2 = chapter(2, []);
  const currentOrder = signal(1);

  beforeEach(() => {
    currentOrder.set(1);
    TestBed.configureTestingModule({
      providers: [
        { provide: TranslocoService, useValue: {} },
        // Chapter 2 is cached although the player is in chapter 1, e.g. after moving back.
        { provide: ContentService, useValue: { loaded: () => new Map([[ch1.id, ch1], [ch2.id, ch2]]) } },
        { provide: ActiveGame, useValue: { manifest: () => ({ chapters: [ch1, ch2].map((c) => ({ order: c.order, neutralLabel: c.neutralLabel })) }) } },
        { provide: ChapterAccess, useValue: { currentOrder } },
      ],
    });
  });

  it('names only the chapter when the deadline is in one beyond the player, even if it is cached', () => {
    const deadline = TestBed.inject(ItemView).deadline(ch1, ch1.items[0]);
    expect(deadline).toEqual({ kind: 'chapter', label: { en: 'Chapter 2' } });
  });

  it('describes the checkpoint once its chapter is reached', () => {
    currentOrder.set(2);
    const deadline = TestBed.inject(ItemView).deadline(ch1, ch1.items[0]);
    expect(deadline).toEqual({ kind: 'checkpoint', description: { en: 'description 2' } });
  });
});
