import { Injectable, computed, inject, signal } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';

import { ContentService } from '../content/content.service';
import { ProgressStore } from '../progress/progress.store';

/** The game whose pages are open. Everything game-specific (manifest, progress, links) follows it. */
@Injectable({ providedIn: 'root' })
export class ActiveGame {
  private readonly content = inject(ContentService);
  private readonly progress = inject(ProgressStore);
  private readonly idSignal = signal<string | null>(null);

  readonly id = this.idSignal.asReadonly();
  readonly manifest = computed(() => this.content.manifestOf(this.idSignal()));
  readonly game = computed(() => {
    const id = this.idSignal();
    return id ? this.content.game(id) : undefined;
  });

  /** Loads the game's manifest and saved progress. False when the game is not in the catalog. */
  async activate(gameId: string): Promise<boolean> {
    if (!this.content.game(gameId)) return false;
    if (this.idSignal() === gameId) return true;
    const manifest = await this.content.loadManifest(gameId);
    await this.progress.load(gameId, manifest.chapters[0]?.id ?? '');
    this.idSignal.set(gameId);
    return true;
  }

  /** Router link inside the active game, e.g. link('chapters', id) → ['/', 'sc', 'chapters', id]. */
  link(...segments: string[]): string[] {
    return ['/', this.idSignal() ?? '', ...segments];
  }
}

/** Opens the game named in the URL, or goes back to the library for an unknown one. */
export const gameGuard: CanActivateFn = async (route) =>
  (await inject(ActiveGame).activate(route.params['gameId'])) ? true : inject(Router).parseUrl('/');
