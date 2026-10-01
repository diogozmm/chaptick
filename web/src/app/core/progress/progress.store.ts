import { Injectable, computed, inject, signal } from '@angular/core';

import { AnalyticsService } from '../analytics.service';
import { DEFAULT_PREFERENCES, PROGRESS_SCHEMA_VERSION, Preferences, SavedProgress } from './progress.models';
import { ProgressRepository } from './progress.repository';

export type ImportFailure = 'invalid-json' | 'wrong-format' | 'newer-version';

export class ProgressImportError extends Error {
  constructor(readonly reason: ImportFailure) {
    super(`Progress import failed: ${reason}`);
  }
}

/** Exported file: every game saved on this device. */
interface ExportFile {
  schemaVersion: number;
  app: 'chaptick';
  games: SavedProgress[];
}

/** Progress of the active game, plus device-wide export/import. One record per game. */
@Injectable({ providedIn: 'root' })
export class ProgressStore {
  private readonly repository = inject(ProgressRepository);
  private readonly analytics = inject(AnalyticsService);
  private readonly state = signal<SavedProgress | null>(null);
  private saving: Promise<void> = Promise.resolve();
  private persistenceAsked = false;

  readonly progress = this.state.asReadonly();
  readonly currentChapter = computed(() => this.state()?.currentChapter ?? '');
  readonly done = computed(() => new Set(this.state()?.doneItems ?? []));
  readonly preferences = computed(() => this.state()?.preferences ?? DEFAULT_PREFERENCES);
  /** A first visit: nothing ticked and no chapter picked yet, so "Where am I" asks instead of warning. */
  readonly needsChapterPick = computed(() => {
    const p = this.state();
    return !!p && needsChapterPick(p);
  });

  /**
   * Switches to a game's saved progress, or starts it at `firstChapterId` on a first visit. A
   * first visit is saved right away so the library can offer "Continue" for it.
   */
  async load(gameId: string, firstChapterId: string): Promise<void> {
    await this.saving;
    const saved = await this.repository.get(gameId);
    if (saved) {
      this.state.set(saved);
      return;
    }
    const fresh = this.fresh(gameId, firstChapterId);
    this.state.set(fresh);
    await this.persist(fresh);
  }

  /** Every game saved on this device, most recently played first. */
  async listSaved(): Promise<SavedProgress[]> {
    await this.saving;
    return (await this.repository.getAll()).sort((a, b) => b.updatedAt.localeCompare(a.updatedAt));
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
    return this.update(() => ({ currentChapter: chapterId, chapterChosen: true }));
  }

  setPreferences(change: Partial<Preferences>): Promise<void> {
    return this.update((p) => ({ preferences: { ...p.preferences, ...change } }));
  }

  /** Every saved game as one file. `compact` drops the indentation, for transfer links. */
  async exportJson(compact = false): Promise<string> {
    const file: ExportFile = { schemaVersion: PROGRESS_SCHEMA_VERSION, app: 'chaptick', games: await this.listSaved() };
    return JSON.stringify(file, null, compact ? undefined : 2);
  }

  /**
   * Replaces the saved progress of every game in the file and returns how many games it had.
   * Also accepts the older single-game export. Unknown item ids are kept: the file may come
   * from newer content.
   */
  async importJson(text: string): Promise<number> {
    const games = parseExport(text);
    this.askToKeepStorage();
    for (const game of games) this.persist(game);
    await this.saving;
    const active = games.find((g) => g.gameId === this.state()?.gameId);
    if (active) this.state.set(active);
    return games.length;
  }

  private update(change: (current: SavedProgress) => Partial<SavedProgress>): Promise<void> {
    const current = this.state();
    if (!current) throw new Error('ProgressStore used before load()');
    const next = { ...current, ...change(current), updatedAt: new Date().toISOString() };
    this.state.set(next);
    this.askToKeepStorage();
    return this.persist(next);
  }

  /**
   * Asks the browser not to evict saved progress (e.g. Safari clears sites left unvisited for a
   * week). Done once, on the first real change rather than on page load, because Firefox shows a
   * prompt. Best effort: the browser may refuse, and progress is saved either way.
   */
  private askToKeepStorage(): void {
    if (this.persistenceAsked) return;
    this.persistenceAsked = true;
    const storage = typeof navigator === 'undefined' ? undefined : navigator.storage;
    if (!storage?.persist) return;
    void storage
      .persisted()
      .then((kept) => kept || storage.persist())
      .catch(() => undefined);
  }

  // Writes are chained so a slow write can never land after a newer one.
  private persist(progress: SavedProgress): Promise<void> {
    this.saving = this.saving.then(() => this.repository.put(progress));
    return this.saving;
  }

  private fresh(gameId: string, firstChapterId: string): SavedProgress {
    return {
      schemaVersion: PROGRESS_SCHEMA_VERSION,
      gameId,
      currentChapter: firstChapterId,
      doneItems: [],
      preferences: DEFAULT_PREFERENCES,
      updatedAt: new Date().toISOString(),
    };
  }
}

/** Reads an exported file (or a transfer link's contents) without saving anything. */
export function parseExport(text: string): SavedProgress[] {
  let data: unknown;
  try {
    data = JSON.parse(text);
  } catch {
    throw new ProgressImportError('invalid-json');
  }
  if (!isRecord(data) || typeof data['schemaVersion'] !== 'number') throw new ProgressImportError('wrong-format');
  if (data['schemaVersion'] > PROGRESS_SCHEMA_VERSION) throw new ProgressImportError('newer-version');
  const records = Array.isArray(data['games']) ? data['games'] : [data];
  if (records.length === 0) throw new ProgressImportError('wrong-format');
  return records.map(parseGame);
}

function parseGame(data: unknown): SavedProgress {
  if (!isRecord(data)) throw new ProgressImportError('wrong-format');
  if (typeof data['schemaVersion'] === 'number' && data['schemaVersion'] > PROGRESS_SCHEMA_VERSION) {
    throw new ProgressImportError('newer-version');
  }
  const { gameId, currentChapter, doneItems, preferences, updatedAt, chapterChosen } = data;
  const validItems = Array.isArray(doneItems) && doneItems.every((id) => typeof id === 'string');
  if (typeof gameId !== 'string' || typeof currentChapter !== 'string' || !validItems) {
    throw new ProgressImportError('wrong-format');
  }
  return {
    schemaVersion: PROGRESS_SCHEMA_VERSION,
    gameId,
    currentChapter,
    doneItems: [...new Set(doneItems as string[])],
    preferences: { ...DEFAULT_PREFERENCES, ...(isRecord(preferences) ? preferences : {}) },
    updatedAt: typeof updatedAt === 'string' ? updatedAt : new Date().toISOString(),
    ...(chapterChosen === true ? { chapterChosen } : {}),
  };
}

/** True until the player picks a chapter or ticks anything (older saves count as picked once ticked). */
export const needsChapterPick = (p: SavedProgress): boolean => !p.chapterChosen && p.doneItems.length === 0;

const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === 'object' && value !== null && !Array.isArray(value);
