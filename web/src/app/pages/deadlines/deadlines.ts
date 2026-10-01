import { ChangeDetectionStrategy, Component, computed, inject, resource } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { Localized } from '../../core/content/content.models';
import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { deadlineGroups } from '../../core/spoiler/deadlines';
import { Icon } from '../../ui/icon/icon';
import { ItemRow } from '../../ui/item-row/item-row';

/** "What can I still miss": every pending item with a deadline, across the unlocked chapters, most urgent first. */
@Component({
  selector: 'app-deadlines',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, Icon, ItemRow],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './deadlines.html',
  styleUrl: './deadlines.scss',
})
export class Deadlines {
  private readonly access = inject(ChapterAccess);
  private readonly progress = inject(ProgressStore);
  protected readonly game = inject(ActiveGame);
  protected readonly lang = inject(LangService);
  protected readonly current = this.access.current;

  private readonly chapters = resource({
    params: () => this.access.currentOrder(),
    loader: () => this.access.loadUnlocked(),
  });

  protected readonly ready = computed(() => this.chapters.hasValue());
  protected readonly groups = computed(() =>
    deadlineGroups(this.chapters.hasValue() ? this.chapters.value() : [], this.progress.done(), this.access.currentOrder()),
  );
  protected readonly total = computed(() => this.groups().reduce((sum, g) => sum + g.entries.length, 0));

  /** A locked chapter is only named by its neutral label, like on "Where am I". */
  protected chapterLabel(order: number): Localized {
    return this.access.chapters().find((c) => c.order === order)?.neutralLabel ?? { en: `Chapter ${order}` };
  }
}
