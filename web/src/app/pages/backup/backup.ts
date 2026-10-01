import { ChangeDetectionStrategy, Component, inject, resource, signal } from '@angular/core';
import { TranslocoPipe, TranslocoService } from '@jsverse/transloco';

import { AnalyticsService } from '../../core/analytics.service';
import { ProgressImportError, ProgressStore } from '../../core/progress/progress.store';
import { TransferService } from '../../core/progress/transfer.service';
import { Icon } from '../../ui/icon/icon';

type Status = { kind: 'ok' | 'error'; key: string; count?: number } | null;

/** Backup and transfer: a transfer link, or an exported file with every game on this device. */
@Component({
  selector: 'app-backup',
  imports: [TranslocoPipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './backup.html',
  styleUrl: './backup.scss',
})
export class Backup {
  private readonly progress = inject(ProgressStore);
  private readonly analytics = inject(AnalyticsService);
  private readonly transfer = inject(TransferService);
  private readonly transloco = inject(TranslocoService);
  protected readonly canShare = typeof navigator !== 'undefined' && typeof navigator.share === 'function';

  private readonly saved = resource({ loader: () => this.progress.listSaved() });
  /** File contents waiting for "replace my progress?". */
  protected readonly pendingFile = signal<string | null>(null);
  protected readonly status = signal<Status>(null);

  /** Shares (phones) or copies a link that opens Chaptick elsewhere with this device's progress. */
  protected async shareLink(): Promise<void> {
    this.status.set(null);
    if (!(this.saved.hasValue() && this.saved.value().length > 0)) {
      this.status.set({ kind: 'error', key: 'transfer.nothingToShare' });
      return;
    }
    const url = await this.transfer.createLink();
    if (this.canShare) {
      try {
        await navigator.share({ title: 'Chaptick', text: this.transloco.translate('transfer.shareText'), url });
        return;
      } catch (error) {
        if (error instanceof DOMException && error.name === 'AbortError') return;
        // Sharing is unavailable here after all: fall back to the clipboard.
      }
    }
    try {
      await navigator.clipboard.writeText(url);
      this.status.set({ kind: 'ok', key: 'transfer.linkCopied' });
    } catch {
      this.status.set({ kind: 'error', key: 'transfer.linkFailed' });
    }
  }

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
    this.pendingFile.set(await file.text());
  }

  protected async confirmImport(): Promise<void> {
    const text = this.pendingFile();
    this.pendingFile.set(null);
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
