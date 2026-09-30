import { ChangeDetectionStrategy, Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { ContentService } from '../../core/content/content.service';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressImportError, ProgressStore } from '../../core/progress/progress.store';
import { ChapterAccess } from '../../core/spoiler/chapter-access';

type TransferStatus = { kind: 'ok' | 'error'; key: string } | null;

@Component({
  selector: 'app-home',
  imports: [RouterLink, TranslocoPipe, LocalizePipe],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home {
  protected readonly content = inject(ContentService);
  protected readonly access = inject(ChapterAccess);
  protected readonly lang = inject(LangService);
  private readonly progress = inject(ProgressStore);

  /** File contents waiting for "replace my progress?" confirmation. */
  protected readonly pendingImport = signal<string | null>(null);
  protected readonly status = signal<TransferStatus>(null);

  protected exportProgress(): void {
    const blob = new Blob([this.progress.exportJson()], { type: 'application/json' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `bracer-notes-progress-${new Date().toISOString().slice(0, 10)}.json`;
    link.click();
    URL.revokeObjectURL(link.href);
    this.status.set({ kind: 'ok', key: 'transfer.exported' });
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
