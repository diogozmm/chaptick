import { Injectable } from '@angular/core';
import { DBSchema, IDBPDatabase, openDB } from 'idb';

import { SavedProgress } from './progress.models';

interface ProgressDb extends DBSchema {
  progress: { key: string; value: SavedProgress };
}

/** One record per game in IndexedDB. No server ever sees it. */
@Injectable({ providedIn: 'root' })
export class ProgressRepository {
  private db?: Promise<IDBPDatabase<ProgressDb>>;

  private open(): Promise<IDBPDatabase<ProgressDb>> {
    this.db ??= openDB<ProgressDb>('chaptick', 1, {
      upgrade: (db) => db.createObjectStore('progress', { keyPath: 'gameId' }),
    });
    return this.db;
  }

  async get(gameId: string): Promise<SavedProgress | undefined> {
    return (await this.open()).get('progress', gameId);
  }

  async getAll(): Promise<SavedProgress[]> {
    return (await this.open()).getAll('progress');
  }

  async put(progress: SavedProgress): Promise<void> {
    await (await this.open()).put('progress', progress);
  }

  /**
   * Reads, changes and writes one game's record in a single transaction. Two tabs of the app can
   * be open on the same record, and each only knows what it loaded: changing the stored record
   * (not a copy from memory) keeps one tab from overwriting the other's changes.
   */
  async update(gameId: string, change: (stored: SavedProgress | undefined) => SavedProgress): Promise<SavedProgress> {
    const tx = (await this.open()).transaction('progress', 'readwrite');
    const next = change(await tx.store.get(gameId));
    await tx.store.put(next);
    await tx.done;
    return next;
  }
}
