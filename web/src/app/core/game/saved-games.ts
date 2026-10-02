import { Injectable, computed, inject, resource, signal } from '@angular/core';

import { GameFeature, localize } from '../content/content.models';
import { ContentService } from '../content/content.service';
import { fallbackCoverText } from '../cover/cover-art';
import { termKey } from '../i18n/terms';
import { SavedProgress } from '../progress/progress.models';
import { ProgressStore, needsChapterPick } from '../progress/progress.store';

/**
 * The games saved on this device and what the library shows for each (link, cover, counts).
 * Shared by the home page and the full library; call `reload()` when a page opens, since progress
 * changes while playing.
 */
@Injectable({ providedIn: 'root' })
export class SavedGames {
  private readonly content = inject(ContentService);
  private readonly progress = inject(ProgressStore);
  private readonly tick = signal(0);

  readonly saved = resource({ params: () => this.tick(), loader: () => this.progress.listSaved() });
  /** Saved games still in the catalog, most recently played first. */
  readonly list = computed<SavedProgress[]>(() =>
    (this.saved.hasValue() ? this.saved.value() : []).filter((p) => this.content.game(p.gameId)),
  );
  readonly byGame = computed(() => new Map(this.list().map((p) => [p.gameId, p])));

  reload(): void {
    this.tick.update((n) => n + 1);
  }

  started(gameId: string): boolean {
    return this.byGame().has(gameId);
  }

  /** Ticked items of a saved game (route steps and Rank A marks are not counted twice). */
  doneCount(gameId: string): number {
    return this.byGame().get(gameId)?.doneItems.filter((id) => !id.includes('#')).length ?? 0;
  }

  features(gameId: string): GameFeature[] {
    return this.content.game(gameId)?.features ?? ['checklist'];
  }

  /** An i18n key worded for the game's progress term (chapters or areas). */
  k(key: string, gameId: string): string {
    return termKey(key, this.content.game(gameId)?.progressTerm);
  }

  /** Cover colors come from the franchise; the text from the game, or its name. */
  cover(gameId: string) {
    const game = this.content.game(gameId);
    return {
      style: this.content.franchiseOf(gameId)?.cover,
      text: game?.cover ?? fallbackCoverText(game ? localize(game.name, 'en') : gameId),
    };
  }

  /**
   * A started game resumes at its current chapter (or its compendium, when it has no checklist);
   * a new one opens "Where am I?" first.
   */
  link(gameId: string): string[] {
    const saved = this.byGame().get(gameId);
    if (!saved || needsChapterPick(saved)) return ['/', gameId, 'chapters'];
    return this.features(gameId).includes('checklist') ? ['/', gameId, 'chapters', saved.currentChapter] : ['/', gameId, 'compendium'];
  }
}
