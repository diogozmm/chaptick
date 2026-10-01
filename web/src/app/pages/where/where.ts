import { ChangeDetectionStrategy, Component, inject, signal } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { ChapterSummary } from '../../core/content/content.models';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ActiveGame } from '../../core/game/active-game';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { isUnlocked } from '../../core/spoiler/spoiler';
import { Icon } from '../../ui/icon/icon';
import { AdvanceConfirm } from '../../ui/advance-confirm/advance-confirm';

/** "Where am I": pick the current chapter. Moving forward is always explicit and confirmed. */
@Component({
  selector: 'app-where',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, AdvanceConfirm, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './where.html',
  styleUrl: './where.scss',
})
export class Where {
  protected readonly access = inject(ChapterAccess);
  protected readonly lang = inject(LangService);
  protected readonly game = inject(ActiveGame);
  private readonly progress = inject(ProgressStore);
  private readonly router = inject(Router);

  /** The locked chapter whose confirmation is open. */
  protected readonly pending = signal<ChapterSummary | null>(null);

  protected isUnlocked(chapter: ChapterSummary): boolean {
    return isUnlocked(chapter, this.access.currentOrder());
  }

  /** Going back to an unlocked chapter needs no confirmation; moving forward goes through AdvanceConfirm. */
  protected async choose(chapter: ChapterSummary): Promise<void> {
    await this.progress.setChapter(chapter.id);
    this.pending.set(null);
    await this.router.navigate(this.game.link('chapters', chapter.id));
  }
}
