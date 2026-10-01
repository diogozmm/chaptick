import { ChangeDetectionStrategy, Component, computed, inject, resource, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { AnalyticsService } from '../../core/analytics.service';
import { ContentService } from '../../core/content/content.service';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { SavedProgress } from '../../core/progress/progress.models';
import { ProgressImportError, ProgressStore } from '../../core/progress/progress.store';
import { chapterProgress, nextCheckpointAlert } from '../../core/spoiler/spoiler';
import { SITE } from '../../site.config';
import { Icon } from '../../ui/icon/icon';
import { GameCover } from '../../ui/game-cover/game-cover';
import { fallbackCoverText } from '../../core/cover/cover-art';
import { localize } from '../../core/content/content.models';

type TransferStatus = { kind: 'ok' | 'error'; key: string; count?: number } | null;

/** The library: continue the last game, browse franchises and games, move progress between devices. */
@Component({
  selector: 'app-home',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, Icon, GameCover],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home {
  protected readonly content = inject(ContentService);
  protected readonly lang = inject(LangService);
  private readonly progress = inject(ProgressStore);
  private readonly analytics = inject(AnalyticsService);
  protected readonly suggestUrl = SITE.repoUrl ? `${SITE.repoUrl}/issues` : '';

  private readonly saved = resource({ loader: () => this.progress.listSaved() });
  private readonly savedByGame = computed(
    () => new Map<string, SavedProgress>((this.saved.hasValue() ? this.saved.value() : []).map((p) => [p.gameId, p])),
  );
  protected readonly franchises = computed(() => this.content.catalog()?.franchises ?? []);

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

  /** File contents waiting for "replace my progress?" confirmation. */
  protected readonly pendingImport = signal<string | null>(null);
  protected readonly status = signal<TransferStatus>(null);

  protected async exportProgress(): Promise<void> {
    const blob = new Blob([await this.progress.exportJson()], { type: 'application/json' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `chaptick-progress-${new Date().toISOString().slice(0, 10)}.json`;
    link.click();
    URL.revokeObjectURL(link.href);
    this.status.set({ kind: 'ok', key: 'transfer.exported' });
    this.analytics.track('progress_exported');
  }

  protected async pickFile(event: Event): Promise<void> {
    const input = event.target as HTMLInputElement;
    const file = input.files?.[0];
    input.value = ''; // lets the same file be picked again
    if (!file) return;
    this.status.set(null);
    this.pendingImport.set(await file.text());
  }

  protected async confirmImport(): Promise<void> {
    const text = this.pendingImport();
    this.pendingImport.set(null);
    if (text === null) return;
    try {
      const count = await this.progress.importJson(text);
      this.status.set({ kind: 'ok', key: 'transfer.imported', count });
      this.saved.reload();
    } catch (error) {
      const reason = error instanceof ProgressImportError ? error.reason : 'wrong-format';
      this.status.set({ kind: 'error', key: `transfer.error.${reason}` });
    }
  }
}
