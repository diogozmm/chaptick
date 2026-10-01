import { ChangeDetectionStrategy, Component, computed, inject, resource, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { NgTemplateOutlet } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { map } from 'rxjs';
import { TranslocoPipe } from '@jsverse/transloco';

import { ContentService } from '../../core/content/content.service';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { SavedProgress } from '../../core/progress/progress.models';
import { ProgressImportError, ProgressStore, parseExport } from '../../core/progress/progress.store';
import { TransferService } from '../../core/progress/transfer.service';
import { chapterProgress, nextCheckpointAlert } from '../../core/spoiler/spoiler';
import { SITE } from '../../site.config';
import { Icon } from '../../ui/icon/icon';
import { GameCover } from '../../ui/game-cover/game-cover';
import { ScrollHints } from '../../ui/scroll-hints/scroll-hints';
import { fallbackCoverText } from '../../core/cover/cover-art';
import { localize } from '../../core/content/content.models';

type TransferStatus = { kind: 'ok' | 'error'; key: string; count?: number } | null;

/** Progress carried by the transfer link that opened the page, waiting for "replace my progress?". */
interface PendingImport {
  text: string;
  games: string;
}

/**
 * The library. Returning players see their games first (the last one played, then the others);
 * below, every franchise is a row of covers, and a filter (?f=<franchise>) shows one franchise as a
 * grid. Backup and transfer live on their own page; a transfer link still lands here.
 */
@Component({
  selector: 'app-home',
  imports: [RouterLink, NgTemplateOutlet, TranslocoPipe, LocalizePipe, Icon, GameCover, ScrollHints],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home {
  protected readonly content = inject(ContentService);
  protected readonly lang = inject(LangService);
  private readonly progress = inject(ProgressStore);
  private readonly transfer = inject(TransferService);
  protected readonly suggestUrl = SITE.repoUrl ? `${SITE.repoUrl}/issues` : '';

  private readonly saved = resource({ loader: () => this.progress.listSaved() });
  private readonly savedByGame = computed(
    () => new Map<string, SavedProgress>((this.saved.hasValue() ? this.saved.value() : []).map((p) => [p.gameId, p])),
  );
  protected readonly franchises = computed(() => this.content.catalog()?.franchises ?? []);
  protected readonly hasProgress = computed(() => this.savedByGame().size > 0);

  /** The franchise filter from ?f=, ignored when it names no franchise. */
  private readonly filterParam = toSignal(inject(ActivatedRoute).queryParamMap.pipe(map((p) => p.get('f'))));
  protected readonly filter = computed(() => this.franchises().find((f) => f.id === this.filterParam()) ?? null);
  protected readonly shown = computed(() => {
    const only = this.filter();
    return only ? [only] : this.franchises();
  });

  /** Started games other than the most recent one, newest first, with their current chapter. */
  protected readonly others = resource({
    params: () => (this.saved.hasValue() ? this.saved.value() : []).filter((p) => this.content.game(p.gameId)).slice(1),
    loader: ({ params }) =>
      Promise.all(
        params.map(async (saved) => {
          const manifest = await this.content.loadManifest(saved.gameId);
          const chapter = manifest.chapters.find((c) => c.id === saved.currentChapter) ?? manifest.chapters[0];
          return { gameId: saved.gameId, game: this.content.game(saved.gameId)!, chapter };
        }),
      ),
  });

  /** The most recently played game that is still in the catalog, with its current chapter. */
  protected readonly recent = resource({
    params: () => (this.saved.hasValue() ? this.saved.value() : []).find((p) => this.content.game(p.gameId)),
    loader: async ({ params: saved }) => {
      const manifest = await this.content.loadManifest(saved.gameId);
      const summary = manifest.chapters.find((c) => c.id === saved.currentChapter) ?? manifest.chapters[0];
      // The current chapter is unlocked for that game by definition, so loading it spoils nothing.
      const chapter = await this.content.loadChapter(saved.gameId, summary);
      const done = new Set(saved.doneItems);
      const stats = chapterProgress(chapter, done);
      return {
        gameId: saved.gameId,
        game: this.content.game(saved.gameId)!,
        summary,
        stats,
        percent: stats.total ? Math.round((stats.done / stats.total) * 100) : 0,
        alert: nextCheckpointAlert(chapter, done),
      };
    },
  });

  /** Ticked items of a saved game (route steps and Rank A marks are not counted twice). */
  protected doneCount(gameId: string): number {
    return this.savedByGame().get(gameId)?.doneItems.filter((id) => !id.includes('#')).length ?? 0;
  }

  /** Cover colors come from the franchise; the text from the game, or its name. */
  protected cover(gameId: string) {
    const game = this.content.game(gameId);
    return {
      style: this.content.franchiseOf(gameId)?.cover,
      text: game?.cover ?? fallbackCoverText(game ? localize(game.name, 'en') : gameId),
    };
  }

  protected started(gameId: string): boolean {
    return this.savedByGame().has(gameId);
  }

  /** A started game resumes at its current chapter; a new one opens "Where am I?" first. */
  protected gameLink(gameId: string): string[] {
    const saved = this.savedByGame().get(gameId);
    return saved ? ['/', gameId, 'chapters', saved.currentChapter] : ['/', gameId, 'chapters'];
  }

  protected readonly pendingImport = signal<PendingImport | null>(null);
  protected readonly status = signal<TransferStatus>(null);

  constructor() {
    void this.receiveLink();
  }

  /** A transfer link opened this page: show what it carries and ask before replacing anything. */
  private async receiveLink(): Promise<void> {
    try {
      const text = await this.transfer.takeIncoming();
      if (text !== null) this.pendingImport.set({ text, games: this.gameNames(text) });
    } catch (error) {
      const reason = error instanceof ProgressImportError ? error.reason : 'wrong-format';
      this.status.set({ kind: 'error', key: `transfer.error.${reason}` });
    }
  }

  /** "Trails in the Sky 2nd Chapter, Ys X: Proud Nordics" for the games in an exported file. */
  private gameNames(text: string): string {
    const lang = this.lang.lang();
    return parseExport(text)
      .map((g) => this.content.game(g.gameId))
      .filter((g) => g !== undefined)
      .map((g) => localize(g.name, lang))
      .join(', ');
  }

  protected async confirmImport(): Promise<void> {
    const pending = this.pendingImport();
    this.pendingImport.set(null);
    if (pending === null) return;
    try {
      const count = await this.progress.importJson(pending.text);
      this.status.set({ kind: 'ok', key: 'transfer.imported', count });
      this.saved.reload();
    } catch (error) {
      const reason = error instanceof ProgressImportError ? error.reason : 'wrong-format';
      this.status.set({ kind: 'error', key: `transfer.error.${reason}` });
    }
  }
}
