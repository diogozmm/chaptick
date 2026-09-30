import { HttpClient } from '@angular/common/http';
import { Injectable, inject, signal } from '@angular/core';
import { firstValueFrom } from 'rxjs';

import { Chapter, ChapterSummary, Manifest } from './content.models';

export const GAME_ID = 'sc';
const BASE = `/content/${GAME_ID}`;

/**
 * Loads game data. Chapter files are fetched one by one and only when asked for, so a
 * locked chapter never reaches the browser (not even the network tab or the SW cache).
 * Callers are responsible for asking only for unlocked chapters; see `ChapterAccess`.
 */
@Injectable({ providedIn: 'root' })
export class ContentService {
  private readonly http = inject(HttpClient);
  private readonly chapters = new Map<string, Promise<Chapter>>();
  private readonly manifestSignal = signal<Manifest | null>(null);

  readonly manifest = this.manifestSignal.asReadonly();

  async loadManifest(): Promise<Manifest> {
    const manifest = await firstValueFrom(this.http.get<Manifest>(`${BASE}/manifest.json`));
    manifest.chapters.sort((a, b) => a.order - b.order);
    this.manifestSignal.set(manifest);
    return manifest;
  }

  summary(chapterId: string): ChapterSummary | undefined {
    return this.manifest()?.chapters.find((c) => c.id === chapterId);
  }

  loadChapter(summary: ChapterSummary): Promise<Chapter> {
    let pending = this.chapters.get(summary.id);
    if (!pending) {
      // The data version busts the offline cache whenever a correction is published.
      const url = `${BASE}/${summary.file}?v=${this.manifest()?.game.dataVersion ?? 0}`;
      pending = firstValueFrom(this.http.get<Chapter>(url));
      pending.catch(() => this.chapters.delete(summary.id));
      this.chapters.set(summary.id, pending);
    }
    return pending;
  }
}
