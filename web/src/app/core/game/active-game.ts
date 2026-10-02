import { Injectable, computed, inject, signal } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';

import { GameFeature, ProgressTerm } from '../content/content.models';
import { ContentService } from '../content/content.service';
import { termKey } from '../i18n/terms';
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

  readonly term = computed<ProgressTerm>(() => this.manifest()?.game.progressTerm ?? 'chapter');
  readonly features = computed<GameFeature[]>(() => this.manifest()?.features ?? ['checklist']);
  readonly hasChecklist = computed(() => this.features().includes('checklist'));
  readonly hasCompendium = computed(() => this.features().includes('compendium'));
  /** Only games with fish or recipes to collect, or with deadlines, show those screens. */
  readonly hasCollections = computed(() => {
    const c = this.manifest()?.collections;
    return !c || c.fish + c.recipes > 0;
  });
  readonly hasSeasons = computed(() => (this.manifest()?.compendium?.seasonal ?? 0) > 0);
  readonly hasDeadlines = computed(() => (this.manifest()?.deadlines ?? 1) > 0);

  /** The i18n key worded for this game's progress term (chapters or areas). */
  k(key: string): string {
    return termKey(key, this.term());
  }

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
