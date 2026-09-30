import 'fake-indexeddb/auto';
import { TestBed } from '@angular/core/testing';

import { ProgressImportError, ProgressStore } from './progress.store';
import { ProgressRepository } from './progress.repository';

describe('ProgressStore', () => {
  let store: ProgressStore;

  beforeEach(async () => {
    indexedDB = new IDBFactory();
    TestBed.configureTestingModule({});
    store = TestBed.inject(ProgressStore);
    await store.load('sc-ch0');
  });

  it('starts at the first chapter on a first visit', () => {
    expect(store.currentChapter()).toBe('sc-ch0');
    expect(store.done().size).toBe(0);
  });

  it('persists toggles and chapter changes across reloads', async () => {
    await store.toggle('sc-ch0-co-01');
    await store.toggle('sc-ch0-co-02');
    await store.toggle('sc-ch0-co-01');
    await store.setChapter('sc-ch1');

    const reloaded = TestBed.runInInjectionContext(() => new ProgressStore());
    await reloaded.load('sc-ch0');
    expect([...reloaded.done()]).toEqual(['sc-ch0-co-02']);
    expect(reloaded.currentChapter()).toBe('sc-ch1');
  });

  it('round-trips export and import, keeping unknown ids', async () => {
    await store.toggle('sc-ch9-hq-01');
    await store.setPreferences({ hideDone: true });
    const exported = store.exportJson();

    await store.toggle('sc-ch9-hq-01');
    await store.importJson(exported);

    expect(store.done().has('sc-ch9-hq-01')).toBe(true);
    expect(store.preferences().hideDone).toBe(true);
    expect((await TestBed.inject(ProgressRepository).get('sc'))?.doneItems).toEqual(['sc-ch9-hq-01']);
  });

  it.each([
    ['not json', 'invalid-json'],
    ['[]', 'wrong-format'],
    ['{"schemaVersion":1,"gameId":"other","currentChapter":"x","doneItems":[]}', 'wrong-game'],
    ['{"schemaVersion":99,"gameId":"sc","currentChapter":"x","doneItems":[]}', 'newer-version'],
    ['{"schemaVersion":1,"gameId":"sc","currentChapter":"x","doneItems":[1]}', 'wrong-format'],
  ])('rejects %s as %s without touching progress', async (text, reason) => {
    await store.toggle('sc-ch0-co-01');
    await expect(store.importJson(text)).rejects.toThrow(new ProgressImportError(reason as never).message);
    expect(store.done().has('sc-ch0-co-01')).toBe(true);
  });
});
