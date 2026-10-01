import { ChangeDetectionStrategy, Component, computed, inject, resource, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { AnalyticsService } from '../../core/analytics.service';
import { ContentService } from '../../core/content/content.service';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressImportError, ProgressStore } from '../../core/progress/progress.store';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { chapterProgress, nextCheckpointAlert } from '../../core/spoiler/spoiler';
import { Icon } from '../../ui/icon/icon';

type TransferStatus = { kind: 'ok' | 'error'; key: string } | null;

@Component({
  selector: 'app-home',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home {
  protected readonly content = inject(ContentService);
  protected readonly access = inject(ChapterAccess);
  protected readonly lang = inject(LangService);
  private readonly progress = inject(ProgressStore);
  private readonly contentService = inject(ContentService);
  private readonly analytics = inject(AnalyticsService);

  /** The current chapter is always unlocked, so loading it here never leaks anything. */
  private readonly currentChapter = resource({
    params: () => this.access.current(),
    loader: ({ params }) => this.contentService.loadChapter(params),
  });
  protected readonly summary = computed(() => {
    if (!this.currentChapter.hasValue()) return null;
    const chapter = this.currentChapter.value();
    const stats = chapterProgress(chapter, this.progress.done());
    return {
      ...stats,
      percent: stats.total ? Math.round((stats.done / stats.total) * 100) : 0,
      alert: nextCheckpointAlert(chapter, this.progress.done()),
    };
  });

  /** File contents waiting for "replace my progress?" confirmation. */
  protected readonly pendingImport = signal<string | null>(null);
  protected readonly status = signal<TransferStatus>(null);

  protected exportProgress(): void {
    const blob = new Blob([this.progress.exportJson()], { type: 'application/json' });
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
      await this.progress.importJson(text);
      this.status.set({ kind: 'ok', key: 'transfer.imported' });
    } catch (error) {
      const reason = error instanceof ProgressImportError ? error.reason : 'wrong-format';
      this.status.set({ kind: 'error', key: `transfer.error.${reason}` });
    }
  }
}
