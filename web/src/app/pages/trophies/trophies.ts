import { ChangeDetectionStrategy, Component, computed, inject, resource } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { trophyProgress } from '../../core/spoiler/trophies';
import { Icon } from '../../ui/icon/icon';

/** How far each trophy is, counting only the chapters the player has reached. */
@Component({
  selector: 'app-trophies',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './trophies.html',
  styleUrl: './trophies.scss',
})
export class Trophies {
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
  protected readonly rows = computed(() =>
    trophyProgress(
      this.game.manifest()?.game.trophies ?? [],
      this.chapters.hasValue() ? this.chapters.value() : [],
      this.progress.done(),
      this.access.currentOrder(),
    ),
  );
  /** Trophies for a whole fish or recipe collection live on the collections screen. */
  protected readonly collections = computed(() => (this.game.manifest()?.game.trophies ?? []).filter((t) => t.collection));

  protected readonly collectionNames = computed(() => this.collections().map((t) => t.name).join(' · '));

  protected percent(done: number, total: number): number {
    return total === 0 ? 0 : Math.round((done / total) * 100);
  }
}
