import { ChangeDetectionStrategy, Component, computed, inject, input, output, resource } from '@angular/core';
import { Router } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { AnalyticsService } from '../../core/analytics.service';
import { ChapterSummary } from '../../core/content/content.models';
import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { newlyLeftBehind } from '../../core/spoiler/spoiler';
import { Icon } from '../icon/icon';
import { ItemRow } from '../item-row/item-row';

/**
 * Confirms moving forward to a locked chapter, listing what would be left behind first.
 * Shared by "Where am I" and the "next chapter" button at the end of a checklist.
 */
@Component({
  selector: 'app-advance-confirm',
  imports: [TranslocoPipe, LocalizePipe, ItemRow, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './advance-confirm.html',
  styleUrl: './advance-confirm.scss',
})
export class AdvanceConfirm {
  private readonly access = inject(ChapterAccess);
  private readonly progress = inject(ProgressStore);
  protected readonly game = inject(ActiveGame);
  private readonly router = inject(Router);
  private readonly analytics = inject(AnalyticsService);
  protected readonly lang = inject(LangService);

  readonly target = input.required<ChapterSummary>();
  readonly cancelled = output<void>();

  private readonly chapters = resource({
    params: () => this.access.currentOrder(),
    loader: () => this.access.loadUnlocked(),
  });

  /** Recomputed as the player ticks items off right here, before confirming. */
  protected readonly leftBehind = computed(() => {
    const chapters = this.chapters.hasValue() ? this.chapters.value() : [];
    const lost = new Set(
      newlyLeftBehind(chapters, this.progress.done(), this.access.currentOrder(), this.target().order).map((i) => i.id),
    );
    return chapters.flatMap((chapter) => chapter.items.filter((i) => lost.has(i.id)).map((item) => ({ chapter, item })));
  });

  protected async confirm(): Promise<void> {
    const target = this.target();
    this.analytics.track('chapter_advanced', { order: target.order });
    await this.progress.setChapter(target.id);
    await this.router.navigate(this.game.link('chapters', target.id));
  }
}
