import { ChangeDetectionStrategy, Component, computed, effect, inject, input, resource, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { Boss, Chapter, ITEM_TYPES, Item, ItemType, localize } from '../../core/content/content.models';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ActiveGame } from '../../core/game/active-game';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { ItemView } from '../../core/spoiler/item-view';
import { carriedOver, chapterProgress, expiredItems, groupByType, nextCheckpointAlert } from '../../core/spoiler/spoiler';
import { Icon } from '../../ui/icon/icon';
import { ItemRow } from '../../ui/item-row/item-row';
import { SpoilerReveal } from '../../ui/spoiler-reveal/spoiler-reveal';
import { AdvanceConfirm } from '../../ui/advance-confirm/advance-confirm';
import { TYPE_ICON } from '../../ui/item-type';

@Component({
  selector: 'app-checklist',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, ItemRow, Icon, SpoilerReveal, AdvanceConfirm],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './checklist.html',
  styleUrl: './checklist.scss',
})
export class Checklist {
  private readonly access = inject(ChapterAccess);
  protected readonly progress = inject(ProgressStore);
  protected readonly lang = inject(LangService);
  protected readonly game = inject(ActiveGame);
  protected readonly view = inject(ItemView);

  /** Bound from the route; the route guard already checked it is unlocked. */
  readonly chapterId = input.required<string>();

  protected readonly chapter = resource({
    params: () => this.access.unlockedChapter(this.chapterId()),
    loader: ({ params }) => this.access.loadChapter(params),
  });

  /** Earlier chapters, loaded only for the current chapter's "left behind" section. */
  private readonly earlier = resource({
    params: () => {
      const current = this.access.current();
      return current?.id === this.chapterId() && current.order > 0 ? current.order : undefined;
    },
    loader: async ({ params }) => (await this.access.loadUnlocked()).filter((c) => c.order < params),
  });

  private readonly loaded = computed(() => (this.chapter.hasValue() ? this.chapter.value() : undefined));
  protected readonly stats = computed(() => {
    const chapter = this.loaded();
    return chapter ? chapterProgress(chapter, this.progress.done()) : { done: 0, total: 0 };
  });
  protected readonly alert = computed(() => {
    const chapter = this.loaded();
    const carried = this.carried().map((e) => e.item);
    return chapter ? nextCheckpointAlert(chapter, this.progress.done(), carried) : null;
  });
  /** Earlier items whose deadline is still ahead: easy to forget once the chapter changes. */
  protected readonly carried = computed<{ chapter: Chapter; item: Item }[]>(() => {
    const chapters = this.earlier.hasValue() ? this.earlier.value() : [];
    const open = new Set(carriedOver(chapters, this.progress.done(), this.access.currentOrder()).map((i) => i.id));
    return chapters.flatMap((chapter) => chapter.items.filter((i) => open.has(i.id)).map((item) => ({ chapter, item })));
  });
  protected readonly leftBehind = computed<{ chapter: Chapter; item: Item }[]>(() => {
    const chapters = this.earlier.hasValue() ? this.earlier.value() : [];
    const lost = new Set(expiredItems(chapters, this.progress.done(), this.access.currentOrder()).map((i) => i.id));
    return chapters.flatMap((chapter) => chapter.items.filter((i) => lost.has(i.id)).map((item) => ({ chapter, item })));
  });
  protected readonly typeIcon = TYPE_ICON;
  protected readonly percent = computed(() => {
    const { done, total } = this.stats();
    return total ? Math.round((done / total) * 100) : 0;
  });
  /** Done/total per type over the whole chapter, ignoring filters. */
  protected readonly typeStats = computed(() => {
    const items = this.loaded()?.items ?? [];
    const done = this.progress.done();
    return new Map(
      ITEM_TYPES.map((type) => {
        const ofType = items.filter((i) => i.type === type);
        return [type, { done: ofType.filter((i) => done.has(i.id)).length, total: ofType.length }] as const;
      }),
    );
  });
  protected readonly availableTypes = computed(() => ITEM_TYPES.filter((t) => (this.typeStats().get(t)?.total ?? 0) > 0));
  protected readonly groups = computed(() => {
    const chapter = this.loaded();
    if (!chapter) return [];
    const { hideDone, filters, trophiesOnly } = this.progress.preferences();
    const done = this.progress.done();
    const visible = chapter.items.filter(
      (i) =>
        (filters.length === 0 || filters.includes(i.type)) &&
        !(hideDone && done.has(i.id)) &&
        !(trophiesOnly && this.hasTrophies() && !i.trophies?.length),
    );
    return groupByType(visible, ITEM_TYPES);
  });

  protected readonly bosses = computed(() => this.loaded()?.bosses ?? []);

  /** The chapter after this one: a plain link when already unlocked, a confirmed advance otherwise. */
  protected readonly next = computed(() => {
    const chapters = this.access.chapters();
    const index = chapters.findIndex((c) => c.id === this.chapterId());
    const next = index >= 0 ? chapters[index + 1] : undefined;
    return next ? { chapter: next, unlocked: next.order <= this.access.currentOrder() } : null;
  });
  protected readonly advancing = signal(false);

  constructor() {
    // A different chapter starts with the confirmation closed.
    effect(() => {
      this.chapterId();
      this.advancing.set(false);
    });
  }

  /** The quest a fight belongs to, named only as far as that quest's own mask allows. */
  protected relatedLabel(chapter: Chapter, boss: Boss): string | null {
    const item = chapter.items.find((i) => i.id === boss.relatedItem);
    if (!item) return null;
    return this.view.showLocation(item) ? localize(item.name, this.lang.lang()) : this.view.placeholder(chapter, item);
  }

  protected isFilterOn(type: ItemType): boolean {
    return this.progress.preferences().filters.includes(type);
  }

  protected toggleFilter(type: ItemType): void {
    const filters = this.progress.preferences().filters;
    void this.progress.setPreferences({
      filters: filters.includes(type) ? filters.filter((t) => t !== type) : [...filters, type],
    });
  }

  /** The "Trophies" filter only exists for games whose trophies are mapped. */
  protected readonly hasTrophies = computed(() => (this.game.manifest()?.game.trophies?.length ?? 0) > 0);

  protected toggleTrophiesOnly(): void {
    void this.progress.setPreferences({ trophiesOnly: !this.progress.preferences().trophiesOnly });
  }

  protected toggleHideDone(): void {
    void this.progress.setPreferences({ hideDone: !this.progress.preferences().hideDone });
  }
}
