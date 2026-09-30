import { ChangeDetectionStrategy, Component, computed, inject, signal } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { Chapter, ChapterSummary } from '../../core/content/content.models';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { isUnlocked, newlyLeftBehind } from '../../core/spoiler/spoiler';
import { ItemRow } from '../../ui/item-row/item-row';

interface PendingAdvance {
  target: ChapterSummary;
  chapters: Chapter[];
}

/** "Where am I": pick the current chapter. Moving forward is always explicit and confirmed. */
@Component({
  selector: 'app-where',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, ItemRow],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './where.html',
  styleUrl: './where.scss',
})
export class Where {
  protected readonly access = inject(ChapterAccess);
  protected readonly lang = inject(LangService);
  private readonly progress = inject(ProgressStore);
  private readonly router = inject(Router);

  protected readonly pending = signal<PendingAdvance | null>(null);

  /** Recomputed as the player ticks items off right here, before confirming. */
  protected readonly leftBehind = computed(() => {
    const pending = this.pending();
    if (!pending) return [];
    const lost = newlyLeftBehind(pending.chapters, this.progress.done(), this.access.currentOrder(), pending.target.order);
    const ids = new Set(lost.map((i) => i.id));
    return pending.chapters.flatMap((chapter) => chapter.items.filter((i) => ids.has(i.id)).map((item) => ({ chapter, item })));
  });

  protected isUnlocked(chapter: ChapterSummary): boolean {
    return isUnlocked(chapter, this.access.currentOrder());
  }

  protected async askToAdvance(target: ChapterSummary): Promise<void> {
    this.pending.set({ target, chapters: await this.access.loadUnlocked() });
  }

  protected async choose(chapter: ChapterSummary): Promise<void> {
    await this.progress.setChapter(chapter.id);
    this.pending.set(null);
    await this.router.navigate(['/sc/chapters', chapter.id]);
  }
}
