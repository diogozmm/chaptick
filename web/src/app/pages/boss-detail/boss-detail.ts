import { ChangeDetectionStrategy, Component, computed, inject, input, resource } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { ContentService } from '../../core/content/content.service';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ChapterAccess, chapterIdOfItem } from '../../core/spoiler/chapter-access';
import { ItemView } from '../../core/spoiler/item-view';
import { RevealService } from '../../core/spoiler/reveal.service';
import { Icon } from '../../ui/icon/icon';
import { SpoilerReveal } from '../../ui/spoiler-reveal/spoiler-reveal';

/** Strategy for one fight. Everything but the neutral placeholder waits for an explicit reveal. */
@Component({
  selector: 'app-boss-detail',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, SpoilerReveal, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './boss-detail.html',
  styleUrl: './boss-detail.scss',
})
export class BossDetail {
  private readonly content = inject(ContentService);
  private readonly access = inject(ChapterAccess);
  protected readonly reveals = inject(RevealService);
  protected readonly view = inject(ItemView);
  protected readonly lang = inject(LangService);

  /** Bound from the route; the route guard already checked its chapter is unlocked. */
  readonly bossId = input.required<string>();

  protected readonly chapter = resource({
    params: () => this.access.unlockedChapter(chapterIdOfItem(this.bossId())),
    loader: ({ params }) => this.content.loadChapter(params),
  });

  protected readonly entry = computed(() => {
    if (!this.chapter.hasValue()) return undefined;
    const chapter = this.chapter.value();
    const bosses = chapter.bosses ?? [];
    const index = bosses.findIndex((b) => b.id === this.bossId());
    if (index < 0) return null;
    const boss = bosses[index];
    return { chapter, boss, n: index + 1, related: chapter.items.find((i) => i.id === boss.relatedItem) };
  });
}
