import { Injectable, computed, inject, signal } from '@angular/core';

import { AnalyticsService } from '../analytics.service';
import { GAME_ID } from '../content/content.service';
import { DEFAULT_PREFERENCES, PROGRESS_SCHEMA_VERSION, Preferences, SavedProgress } from './progress.models';
import { ProgressRepository } from './progress.repository';

export type ImportFailure = 'invalid-json' | 'wrong-format' | 'wrong-game' | 'newer-version';

export class ProgressImportError extends Error {
  constructor(readonly reason: ImportFailure) {
    super(`Progress import failed: ${reason}`);
  }
}

@Injectable({ providedIn: 'root' })
export class ProgressStore {
  private readonly repository = inject(ProgressRepository);
  private readonly analytics = inject(AnalyticsService);
  private readonly state = signal<SavedProgress | null>(null);
  private saving: Promise<void> = Promise.resolve();

  readonly progress = this.state.asReadonly();
  readonly currentChapter = computed(() => this.state()?.currentChapter ?? '');
  readonly done = computed(() => new Set(this.state()?.doneItems ?? []));
  readonly preferences = computed(() => this.state()?.preferences ?? DEFAULT_PREFERENCES);

  /** Loads saved progress, or starts at `firstChapterId` on a first visit. */
  async load(firstChapterId: string): Promise<void> {
    const saved = await this.repository.get(GAME_ID);
    this.state.set(saved ?? this.fresh(firstChapterId));
  }

  toggle(itemId: string): Promise<void> {
    this.analytics.track('item_toggled', { state: this.done().has(itemId) ? 'undone' : 'done' });
    return this.update((p) => ({
      doneItems: p.doneItems.includes(itemId) ? p.doneItems.filter((id) => id !== itemId) : [...p.doneItems, itemId],
    }));
  }

  /** Idempotent: marks every id as done (or not), e.g. a Rank A catch also counts as caught. */
  setDone(ids: readonly string[], done: boolean): Promise<void> {
    return this.update((p) => {
      const set = new Set(p.doneItems);
      for (const id of ids) {
        if (done) set.add(id);
        else set.delete(id);
      }
      return { doneItems: [...set] };
    });
  }

  setChapter(chapterId: string): Promise<void> {
    return this.update(() => ({ currentChapter: chapterId }));
  }

  setPreferences(change: Partial<Preferences>): Promise<void> {
    return this.update((p) => ({ preferences: { ...p.preferences, ...change } }));
  }

  exportJson(): string {
    return JSON.stringify(this.state(), null, 2);
  }

  /** Replaces progress with an exported file. Unknown item ids are kept: the file may come from newer content. */
  async importJson(text: string): Promise<void> {
    const imported = parseProgress(text);
    this.state.set(imported);
    await this.persist(imported);
  }

  private update(change: (current: SavedProgress) => Partial<SavedProgress>): Promise<void> {
    const current = this.state();
    if (!current) throw new Error('ProgressStore used before load()');
    const next = { ...current, ...change(current), updatedAt: new Date().toISOString() };
    this.state.set(next);
    return this.persist(next);
  }

  // Writes are chained so a slow write can never land after a newer one.
  private persist(progress: SavedProgress): Promise<void> {
    this.saving = this.saving.then(() => this.repository.put(progress));
    return this.saving;
  }

  private fresh(firstChapterId: string): SavedProgress {
    return {
      schemaVersion: PROGRESS_SCHEMA_VERSION,
      gameId: GAME_ID,
      currentChapter: firstChapterId,
      doneItems: [],
      preferences: DEFAULT_PREFERENCES,
      updatedAt: new Date().toISOString(),
    };
  }
}

function parseProgress(text: string): SavedProgress {
  let data: unknown;
  try {
    data = JSON.parse(text);
  } catch {
    throw new ProgressImportError('invalid-json');
  }
  if (!isRecord(data) || typeof data['schemaVersion'] !== 'number') throw new ProgressImportError('wrong-format');
  if (data['schemaVersion'] > PROGRESS_SCHEMA_VERSION) throw new ProgressImportError('newer-version');
  if (data['gameId'] !== GAME_ID) throw new ProgressImportError('wrong-game');

  const { currentChapter, doneItems, preferences } = data;
  const validItems = Array.isArray(doneItems) && doneItems.every((id) => typeof id === 'string');
  if (typeof currentChapter !== 'string' || !validItems) throw new ProgressImportError('wrong-format');

  return {
    schemaVersion: PROGRESS_SCHEMA_VERSION,
    gameId: GAME_ID,
    currentChapter,
    doneItems: [...new Set(doneItems as string[])],
    preferences: { ...DEFAULT_PREFERENCES, ...(isRecord(preferences) ? preferences : {}) },
    updatedAt: new Date().toISOString(),
  };
}

const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === 'object' && value !== null && !Array.isArray(value);
