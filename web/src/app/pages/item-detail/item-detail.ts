import { ChangeDetectionStrategy, Component, computed, inject, input, resource } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { Item, localize } from '../../core/content/content.models';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ActiveGame } from '../../core/game/active-game';
import { ChapterAccess, chapterIdOfItem } from '../../core/spoiler/chapter-access';
import { checklistOrder, itemStatus, neighbours, sourceLabel } from '../../core/spoiler/item-status';
import { ItemView } from '../../core/spoiler/item-view';
import { RevealService } from '../../core/spoiler/reveal.service';
import { DetailBar } from '../../ui/detail-bar/detail-bar';
import { ReportLink } from '../../ui/report-link/report-link';
import { Icon } from '../../ui/icon/icon';
import { IconName } from '../../ui/icon/icons';
import { TYPE_ICON } from '../../ui/item-type';
import { itemChange, routeProgress } from '../../core/route/route';
import { RouteSteps } from '../../ui/route-steps/route-steps';
import { SpoilerNotice } from '../../ui/spoiler-notice/spoiler-notice';

const STATUS_ICON: Record<ReturnType<typeof itemStatus>, IconName> = {
  done: 'circle-check',
  'left-behind': 'hourglass',
  'this-chapter': 'triangle-alert',
  later: 'flag',
  none: 'compass',
};

@Component({
  selector: 'app-item-detail',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, Icon, RouteSteps, SpoilerNotice, DetailBar, ReportLink],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './item-detail.html',
  styleUrl: './item-detail.scss',
})
export class ItemDetail {
  private readonly access = inject(ChapterAccess);
  protected readonly progress = inject(ProgressStore);
  protected readonly view = inject(ItemView);
  protected readonly reveals = inject(RevealService);
  protected readonly lang = inject(LangService);
  protected readonly game = inject(ActiveGame);
  protected readonly typeIcon = TYPE_ICON;
  protected readonly statusIcon = STATUS_ICON;
  protected readonly sourceLabel = sourceLabel;

  /** Bound from the route; the route guard already checked its chapter is unlocked. */
  readonly itemId = input.required<string>();

  protected readonly chapter = resource({
    params: () => this.access.unlockedChapter(chapterIdOfItem(this.itemId())),
    loader: ({ params }) => this.access.loadChapter(params),
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
    const done = this.progress.done();
    const lang = this.lang.lang();
    const showName = this.view.showLocation(item);
    const showHint = this.view.showHint(item);
    const order = checklistOrder(chapter, this.progress.preferences().filters, item.id);
    const { prev, next } = neighbours(order, item.id);
    return {
      chapter,
      item,
      showName,
      showHint,
      // Chest groups are named after their area: repeating the area as the location adds nothing.
      showLocation: showName && !localize(item.name, lang).startsWith(localize(item.location, lang)),
      // Source pages are named after places, so they wait for the whole item to be visible.
      showSources: showName && showHint && item.sources.length > 0,
      hiddenMessage: item.spoilerLevel === 1 ? 'spoiler.hiddenItem' : 'spoiler.hiddenName',
      status: itemStatus(item, done, this.access.currentOrder()),
      deadline: this.view.deadline(chapter, item),
      route: item.steps?.length ? routeProgress(item, done) : null,
      texts: chapter.itemTexts.filter((t) => t.itemId === item.id),
      // Fights that belong to this item, numbered like in the chapter's boss list.
      bosses: (chapter.bosses ?? []).map((boss, i) => ({ boss, n: i + 1 })).filter((e) => e.boss.relatedItem === item.id),
      prev: prev ? this.game.link('items', prev.id) : null,
      next: next ? this.game.link('items', next.id) : null,
    };
  });
}
