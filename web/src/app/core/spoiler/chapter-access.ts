import { Injectable, computed, inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';

import { Chapter, ChapterSummary } from '../content/content.models';
import { ContentService } from '../content/content.service';
import { ProgressStore } from '../progress/progress.store';
import { isUnlocked } from './spoiler';

/** Joins the manifest with the player's current chapter to decide what may be loaded. */
@Injectable({ providedIn: 'root' })
export class ChapterAccess {
  private readonly content = inject(ContentService);
  private readonly progress = inject(ProgressStore);

  readonly chapters = computed(() => this.content.manifest()?.chapters ?? []);
  readonly current = computed<ChapterSummary | undefined>(() => {
    const chapters = this.chapters();
    return chapters.find((c) => c.id === this.progress.currentChapter()) ?? chapters[0];
  });
  readonly currentOrder = computed(() => this.current()?.order ?? 0);
  readonly unlocked = computed(() => this.chapters().filter((c) => isUnlocked(c, this.currentOrder())));

  /** Every chapter up to the current one, for rules that look across chapters. */
  loadUnlocked(): Promise<Chapter[]> {
    return Promise.all(this.unlocked().map((summary) => this.content.loadChapter(summary)));
  }

  /** The chapter if the player may see it, otherwise undefined. */
  unlockedChapter(chapterId: string): ChapterSummary | undefined {
    const summary = this.content.summary(chapterId);
    return summary && isUnlocked(summary, this.currentOrder()) ? summary : undefined;
  }
}

/** Item ids start with their chapter id: `sc-ch3-hq-02` belongs to `sc-ch3`. */
export const chapterIdOfItem = (itemId: string): string => itemId.match(/^[a-z0-9]+-ch\d+/)?.[0] ?? '';

/** Blocks a pasted link to a locked chapter, item or boss instead of loading it. */
export const unlockedChapterGuard: CanActivateFn = (route) => {
  const chapterId = route.params['chapterId'] ?? chapterIdOfItem(route.params['itemId'] ?? route.params['bossId'] ?? '');
  return inject(ChapterAccess).unlockedChapter(chapterId) ? true : inject(Router).parseUrl('/sc/chapters');
};
