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
    await store.load('sc', 'sc-ch0');
  });

  it('starts at the first chapter on a first visit', () => {
    expect(store.currentChapter()).toBe('sc-ch0');
    expect(store.done().size).toBe(0);
  });

  it('asks for the chapter on a first visit, until one is picked or anything is ticked', async () => {
    expect(store.needsChapterPick()).toBe(true);
    await store.setChapter('sc-ch0');
    expect(store.needsChapterPick()).toBe(false);

    await store.load('ysx', 'ysx-ch0');
    expect(store.needsChapterPick()).toBe(true);
    await store.toggle('ysx-ch0-q-01');
    expect(store.needsChapterPick()).toBe(false);
  });

  it('keeps the picked chapter through export and import', async () => {
    await store.setChapter('sc-ch1');
    const json = await store.exportJson();
    indexedDB = new IDBFactory();
    const fresh = TestBed.runInInjectionContext(() => new ProgressStore());
    await fresh.load('sc', 'sc-ch0');
    await fresh.importJson(json);
    expect(fresh.needsChapterPick()).toBe(false);
  });

  it('persists toggles and chapter changes across reloads', async () => {
    await store.toggle('sc-ch0-co-01');
    await store.toggle('sc-ch0-co-02');
    await store.toggle('sc-ch0-co-01');
    await store.setChapter('sc-ch1');

    const reloaded = TestBed.runInInjectionContext(() => new ProgressStore());
    await reloaded.load('sc', 'sc-ch0');
    expect([...reloaded.done()]).toEqual(['sc-ch0-co-02']);
    expect(reloaded.currentChapter()).toBe('sc-ch1');
  });

  it('keeps each game separate', async () => {
    await store.toggle('sc-ch0-co-01');
    await store.load('other', 'other-ch0');
    expect(store.done().size).toBe(0);
    await store.toggle('other-ch0-co-01');
    await store.load('sc', 'sc-ch0');
    expect([...store.done()]).toEqual(['sc-ch0-co-01']);
  });

  it('lists saved games, most recent first', async () => {
    await store.toggle('sc-ch0-co-01');
    await store.load('other', 'other-ch0');
    await store.toggle('other-ch0-co-01');
    expect((await store.listSaved()).map((p) => p.gameId)).toEqual(['other', 'sc']);
  });

  it('sets several ids at once without duplicates', async () => {
    await store.setDone(['a', 'a#rank-a'], true);
    await store.setDone(['a#rank-a'], true);
    expect([...store.done()]).toEqual(['a', 'a#rank-a']);
    await store.setDone(['a#rank-a'], false);
    expect([...store.done()]).toEqual(['a']);
  });

  it('round-trips every game through export and import, keeping unknown ids', async () => {
    await store.toggle('sc-ch9-hq-01');
    await store.setPreferences({ hideDone: true });
    await store.load('other', 'other-ch0');
    await store.toggle('other-ch0-co-01');
    const exported = await store.exportJson();

    indexedDB = new IDBFactory();
    TestBed.resetTestingModule();
    const fresh = TestBed.inject(ProgressStore);
    await fresh.load('sc', 'sc-ch0');
    expect(await fresh.importJson(exported)).toBe(2);

    expect(fresh.done().has('sc-ch9-hq-01')).toBe(true);
    expect(fresh.preferences().hideDone).toBe(true);
    expect((await TestBed.inject(ProgressRepository).get('other'))?.doneItems).toEqual(['other-ch0-co-01']);
  });

  it('still accepts the older single-game export', async () => {
    const legacy = '{"schemaVersion":1,"gameId":"sc","currentChapter":"sc-ch2","doneItems":["sc-ch0-co-01"]}';
    expect(await store.importJson(legacy)).toBe(1);
    expect(store.currentChapter()).toBe('sc-ch2');
  });

  it.each([
    ['not json', 'invalid-json'],
    ['[]', 'wrong-format'],
    ['{"schemaVersion":1,"app":"chaptick","games":[]}', 'wrong-format'],
    ['{"schemaVersion":99,"gameId":"sc","currentChapter":"x","doneItems":[]}', 'newer-version'],
    ['{"schemaVersion":1,"gameId":"sc","currentChapter":"x","doneItems":[1]}', 'wrong-format'],
  ])('rejects %s as %s without touching progress', async (text, reason) => {
    await store.toggle('sc-ch0-co-01');
    await expect(store.importJson(text)).rejects.toThrow(new ProgressImportError(reason as never).message);
    expect(store.done().has('sc-ch0-co-01')).toBe(true);
  });

  it('asks once to keep storage, on the first change rather than on load', async () => {
    const persist = vi.fn().mockResolvedValue(true);
    const persisted = vi.fn().mockResolvedValue(false);
    vi.stubGlobal('navigator', { ...navigator, storage: { persist, persisted } });
    try {
      const fresh = TestBed.runInInjectionContext(() => new ProgressStore());
      await fresh.load('sc', 'sc-ch0');
      expect(persisted).not.toHaveBeenCalled();

      await fresh.toggle('sc-ch0-co-01');
      await fresh.toggle('sc-ch0-co-02');
      await vi.waitFor(() => expect(persist).toHaveBeenCalledTimes(1));
      expect(persisted).toHaveBeenCalledTimes(1);
    } finally {
      vi.unstubAllGlobals();
    }
  });
});
