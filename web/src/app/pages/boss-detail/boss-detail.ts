import { ChangeDetectionStrategy, Component, computed, inject, input, resource } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ActiveGame } from '../../core/game/active-game';
import { ChapterAccess, chapterIdOfItem } from '../../core/spoiler/chapter-access';
import { neighbours, sourceLabel } from '../../core/spoiler/item-status';
import { ItemView } from '../../core/spoiler/item-view';
import { RevealService } from '../../core/spoiler/reveal.service';
import { DetailBar } from '../../ui/detail-bar/detail-bar';
import { Icon } from '../../ui/icon/icon';
import { SpoilerNotice } from '../../ui/spoiler-notice/spoiler-notice';

/** Strategy for one fight. Everything but the neutral placeholder waits for an explicit reveal. */
@Component({
  selector: 'app-boss-detail',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, Icon, SpoilerNotice, DetailBar],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './boss-detail.html',
  styleUrl: './boss-detail.scss',
})
export class BossDetail {
  private readonly access = inject(ChapterAccess);
  protected readonly reveals = inject(RevealService);
  protected readonly view = inject(ItemView);
  protected readonly lang = inject(LangService);
  protected readonly game = inject(ActiveGame);
  protected readonly sourceLabel = sourceLabel;

  /** Bound from the route; the route guard already checked its chapter is unlocked. */
  readonly bossId = input.required<string>();

  protected readonly chapter = resource({
    params: () => this.access.unlockedChapter(chapterIdOfItem(this.bossId())),
    loader: ({ params }) => this.access.loadChapter(params),
  });

  protected readonly entry = computed(() => {
    if (!this.chapter.hasValue()) return undefined;
    const chapter = this.chapter.value();
    const bosses = chapter.bosses ?? [];
    const { prev, next, index } = neighbours(bosses, this.bossId());
    if (index < 0) return null;
    const boss = bosses[index];
    return {
      chapter,
      boss,
      n: index + 1,
      total: bosses.length,
      related: chapter.items.find((i) => i.id === boss.relatedItem),
      prev: prev ? this.game.link('bosses', prev.id) : null,
      next: next ? this.game.link('bosses', next.id) : null,
    };
  });
}
