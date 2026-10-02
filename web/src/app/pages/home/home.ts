import { ChangeDetectionStrategy, Component, computed, inject, input, resource, signal } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { CatalogGame, localize } from '../../core/content/content.models';
import { ContentService } from '../../core/content/content.service';
import { SavedGames } from '../../core/game/saved-games';
import { GameNamePipe } from '../../core/i18n/game-name.pipe';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressImportError, ProgressStore, needsChapterPick, parseExport } from '../../core/progress/progress.store';
import { TransferService } from '../../core/progress/transfer.service';
import { GlobalSearch } from '../../core/search/global-search';
import { normalize } from '../../core/search/search';
import { chapterProgress, nextCheckpointAlert } from '../../core/spoiler/spoiler';
import { GameCard } from '../../ui/game-card/game-card';
import { GameCover } from '../../ui/game-cover/game-cover';
import { Icon } from '../../ui/icon/icon';

type TransferStatus = { kind: 'ok' | 'error'; key: string; count?: number } | null;

/** Progress carried by the transfer link that opened the page, waiting for "replace my progress?". */
interface PendingImport {
  text: string;
  games: string;
}

const MIN_QUERY = 2;

/**
 * Home: one search box for games and for what the player's started games hold (only up to where
 * they are), then their games to continue. A first visit gets the introduction and every game
 * instead. The full library, by series, lives at /games.
 */
@Component({
  selector: 'app-home',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, GameNamePipe, Icon, GameCover, GameCard],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home {
  protected readonly content = inject(ContentService);
  protected readonly lang = inject(LangService);
  protected readonly saved = inject(SavedGames);
  private readonly progress = inject(ProgressStore);
  private readonly transfer = inject(TransferService);
  private readonly router = inject(Router);
  private readonly globalSearch = inject(GlobalSearch);

  /** The search, kept in the URL (?q=) so "back" from a result returns to it. */
  readonly q = input<string | undefined>();
  protected readonly query = computed(() => (this.q() ?? '').trim());
  protected readonly searching = computed(() => this.query().length >= MIN_QUERY);

  protected readonly allGames = computed<CatalogGame[]>(() => (this.content.catalog()?.franchises ?? []).flatMap((f) => f.games));
  protected readonly hasProgress = computed(() => this.saved.list().length > 0);

  constructor() {
    this.saved.reload();
    void this.receiveLink();
  }

  /** Each started game with where the player is, how far, and the next point of no return. */
  protected readonly continuing = resource({
    params: () => this.saved.list(),
    loader: ({ params }) =>
      Promise.all(
        params.map(async (saved) => {
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
            picking: needsChapterPick(saved),
          };
        }),
      ),
  });

  /** Games whose name holds every word of the query, in either language. */
  protected readonly gameHits = computed(() => {
    const words = normalize(this.query()).split(/\s+/).filter((w) => w);
    if (!this.searching()) return [];
    const lang = this.lang.lang();
    return this.allGames().filter((g) => {
      const text = normalize(`${localize(g.name, lang)} ${g.name.en}`);
      return words.every((w) => text.includes(w));
    });
  });

  /** Reached content of every started game, loaded once the player starts typing. */
  private readonly reached = resource({
    params: () => (this.searching() ? this.saved.list() : undefined),
    loader: ({ params }) => this.globalSearch.reached(params),
  });
  protected readonly loadingContent = computed(() => this.searching() && this.reached.isLoading());
  protected readonly contentHits = computed(() => {
    if (!this.searching() || !this.reached.hasValue()) return [];
    const lang = this.lang.lang();
    return this.reached.value().map((g) => this.globalSearch.search(g, this.query(), lang)).filter((r) => r.total > 0);
  });
  protected readonly nothingFound = computed(
    () => this.searching() && !this.loadingContent() && this.gameHits().length === 0 && this.contentHits().length === 0,
  );
  protected readonly names = computed(() => new Map(this.saved.list().map((p) => [p.gameId, p.preferences.names ?? {}])));

  protected setQuery(value: string): void {
    void this.router.navigate([], { queryParams: { q: value || null }, replaceUrl: true });
  }

  protected readonly pendingImport = signal<PendingImport | null>(null);
  protected readonly status = signal<TransferStatus>(null);

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
