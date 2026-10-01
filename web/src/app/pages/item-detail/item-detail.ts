import { ChangeDetectionStrategy, Component, computed, inject, input, resource } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { Item } from '../../core/content/content.models';
import { ContentService } from '../../core/content/content.service';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ChapterAccess, chapterIdOfItem } from '../../core/spoiler/chapter-access';
import { ItemView } from '../../core/spoiler/item-view';
import { Icon } from '../../ui/icon/icon';
import { TYPE_ICON } from '../../ui/item-type';
import { itemChange } from '../../core/route/route';
import { RouteSteps } from '../../ui/route-steps/route-steps';
import { SpoilerReveal } from '../../ui/spoiler-reveal/spoiler-reveal';

@Component({
  selector: 'app-item-detail',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, SpoilerReveal, Icon, RouteSteps],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './item-detail.html',
  styleUrl: './item-detail.scss',
})
export class ItemDetail {
  private readonly content = inject(ContentService);
  private readonly access = inject(ChapterAccess);
  protected readonly progress = inject(ProgressStore);
  protected readonly view = inject(ItemView);
  protected readonly lang = inject(LangService);
  protected readonly typeIcon = TYPE_ICON;

  /** Bound from the route; the route guard already checked its chapter is unlocked. */
  readonly itemId = input.required<string>();

  protected readonly chapter = resource({
    params: () => this.access.unlockedChapter(chapterIdOfItem(this.itemId())),
    loader: ({ params }) => this.content.loadChapter(params),
  });

  protected toggle(item: Item): void {
    const change = itemChange(item, this.progress.done());
    void this.progress.setDone(change.ids, change.done);
  }

  protected readonly entry = computed(() => {
    if (!this.chapter.hasValue()) return undefined;
    const chapter = this.chapter.value();
    const item = chapter.items.find((i) => i.id === this.itemId());
    if (!item) return null;
    return {
      chapter,
      item,
      deadline: this.view.deadline(chapter, item),
      texts: chapter.itemTexts.filter((t) => t.itemId === item.id),
    };
  });
}
