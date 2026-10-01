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

  async put(progress: SavedProgress): Promise<void> {
    await (await this.open()).put('progress', progress);
  }
}
