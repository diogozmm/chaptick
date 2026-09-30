import { ChangeDetectionStrategy, Component, computed, inject, input, resource } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { Chapter, ITEM_TYPES, Item, ItemType } from '../../core/content/content.models';
import { ContentService } from '../../core/content/content.service';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { chapterProgress, expiredItems, groupByType, nextCheckpointAlert } from '../../core/spoiler/spoiler';
import { ItemRow } from '../../ui/item-row/item-row';

@Component({
  selector: 'app-checklist',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, ItemRow],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './checklist.html',
  styleUrl: './checklist.scss',
})
export class Checklist {
  private readonly content = inject(ContentService);
  private readonly access = inject(ChapterAccess);
  protected readonly progress = inject(ProgressStore);
  protected readonly lang = inject(LangService);

  /** Bound from the route; the route guard already checked it is unlocked. */
  readonly chapterId = input.required<string>();

  protected readonly chapter = resource({
    params: () => this.access.unlockedChapter(this.chapterId()),
    loader: ({ params }) => this.content.loadChapter(params),
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
    return chapter ? nextCheckpointAlert(chapter, this.progress.done()) : null;
  });
  protected readonly leftBehind = computed<{ chapter: Chapter; item: Item }[]>(() => {
    const chapters = this.earlier.hasValue() ? this.earlier.value() : [];
    const lost = new Set(expiredItems(chapters, this.progress.done(), this.access.currentOrder()).map((i) => i.id));
    return chapters.flatMap((chapter) => chapter.items.filter((i) => lost.has(i.id)).map((item) => ({ chapter, item })));
  });
  protected readonly availableTypes = computed(() => ITEM_TYPES.filter((t) => this.loaded()?.items.some((i) => i.type === t)));
  protected readonly groups = computed(() => {
    const chapter = this.loaded();
    if (!chapter) return [];
    const { hideDone, filters } = this.progress.preferences();
    const done = this.progress.done();
    const visible = chapter.items.filter(
      (i) => (filters.length === 0 || filters.includes(i.type)) && !(hideDone && done.has(i.id)),
    );
    return groupByType(visible, ITEM_TYPES);
  });

  protected isFilterOn(type: ItemType): boolean {
    return this.progress.preferences().filters.includes(type);
  }

  protected toggleFilter(type: ItemType): void {
    const filters = this.progress.preferences().filters;
    void this.progress.setPreferences({
      filters: filters.includes(type) ? filters.filter((t) => t !== type) : [...filters, type],
    });
  }

  protected toggleHideDone(): void {
    void this.progress.setPreferences({ hideDone: !this.progress.preferences().hideDone });
  }
}
