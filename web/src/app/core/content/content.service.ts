import { HttpClient } from '@angular/common/http';
import { Injectable, inject, signal } from '@angular/core';
import { firstValueFrom } from 'rxjs';

import { Catalog, CatalogGame, Chapter, ChapterSummary, Franchise, Manifest } from './content.models';

const BASE = '/content';

/**
 * Loads game data for any game in the catalog. Chapter files are fetched one by one and only
 * when asked for, so a locked chapter never reaches the browser (not even the network tab or
 * the SW cache). Callers ask only for unlocked chapters; see `ChapterAccess`.
 */
@Injectable({ providedIn: 'root' })
export class ContentService {
  private readonly http = inject(HttpClient);
  private readonly manifests = new Map<string, Promise<Manifest>>();
  private readonly chapters = new Map<string, Promise<Chapter>>();
  private readonly catalogSignal = signal<Catalog | null>(null);
  private readonly manifestsSignal = signal<ReadonlyMap<string, Manifest>>(new Map());
  private readonly loadedSignal = signal<ReadonlyMap<string, Chapter>>(new Map());

  readonly catalog = this.catalogSignal.asReadonly();
  /** Chapters already fetched, by chapter id. Only unlocked chapters are ever fetched, so everything here is safe to show. */
  readonly loaded = this.loadedSignal.asReadonly();

  async loadCatalog(): Promise<Catalog> {
    const catalog = await firstValueFrom(this.http.get<Catalog>(`${BASE}/catalog.json`));
    this.catalogSignal.set(catalog);
    return catalog;
  }

  game(gameId: string): CatalogGame | undefined {
    return this.catalog()?.franchises.flatMap((f) => f.games).find((g) => g.id === gameId);
  }

  franchiseOf(gameId: string): Franchise | undefined {
    return this.catalog()?.franchises.find((f) => f.games.some((g) => g.id === gameId));
  }

  manifestOf(gameId: string | null): Manifest | undefined {
    return gameId ? this.manifestsSignal().get(gameId) : undefined;
  }

  loadManifest(gameId: string): Promise<Manifest> {
    let pending = this.manifests.get(gameId);
    if (!pending) {
      pending = firstValueFrom(this.http.get<Manifest>(`${BASE}/${gameId}/manifest.json`)).then((manifest) => {
        manifest.chapters.sort((a, b) => a.order - b.order);
        this.manifestsSignal.update((map) => new Map(map).set(gameId, manifest));
        return manifest;
      });
      pending.catch(() => this.manifests.delete(gameId));
      this.manifests.set(gameId, pending);
    }
    return pending;
  }

  loadChapter(gameId: string, summary: ChapterSummary): Promise<Chapter> {
    let pending = this.chapters.get(summary.id);
    if (!pending) {
      // The data version busts the offline cache whenever a correction is published.
      const version = this.manifestOf(gameId)?.game.dataVersion ?? 0;
      pending = firstValueFrom(this.http.get<Chapter>(`${BASE}/${gameId}/${summary.file}?v=${version}`));
      pending.then(
        (chapter) => this.loadedSignal.update((map) => new Map(map).set(chapter.id, chapter)),
        () => this.chapters.delete(summary.id),
      );
      this.chapters.set(summary.id, pending);
    }
    return pending;
  }
}
