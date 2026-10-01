import { ChangeDetectionStrategy, Component, computed, inject, resource, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { byChapter, FishEntry, fishBook, fishStats, rankAKey, recipeBook } from '../../core/collections/collections';
import { Chapter } from '../../core/content/content.models';
import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { Icon } from '../../ui/icon/icon';

type Tab = 'fish' | 'recipes';

/** Fishing log and recipe book, grouped by chapter and limited to what the unlocked chapters reveal. */
@Component({
  selector: 'app-collections',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './collections.html',
  styleUrl: './collections.scss',
})
export class Collections {
  private readonly access = inject(ChapterAccess);
  protected readonly game = inject(ActiveGame);
  protected readonly progress = inject(ProgressStore);
  protected readonly lang = inject(LangService);

  protected readonly tab = signal<Tab>('fish');
  protected readonly rankAKey = rankAKey;
  protected readonly current = this.access.current;

  private readonly chapters = resource({
    params: () => this.access.currentOrder(),
    loader: () => this.access.loadUnlocked(),
  });
  protected readonly ready = computed(() => this.chapters.hasValue());
  private readonly loaded = computed(() => (this.chapters.hasValue() ? this.chapters.value() : []));
  private readonly hideDone = computed(() => this.progress.preferences().hideDone);

  private readonly fish = computed(() => fishBook(this.loaded()));
  private readonly recipes = computed(() => recipeBook(this.loaded()));
  protected readonly fishStats = computed(() => fishStats(this.fish(), this.progress.done()));
  protected readonly recipeStats = computed(() => {
    const done = this.progress.done();
    return { learned: this.recipes().filter((e) => done.has(e.recipe.id)).length, total: this.recipes().length };
  });

  /** Done and total for the open tab, shown in the header. */
  protected readonly summary = computed(() => {
    const [done, total] = this.tab() === 'fish' ? [this.fishStats().caught, this.fishStats().known] : [this.recipeStats().learned, this.recipeStats().total];
    return { done, total, percent: total ? Math.round((done / total) * 100) : 0 };
  });

  protected readonly fishGroups = computed(() => this.groups(this.fish(), (e) => e.fish.id));
  protected readonly recipeGroups = computed(() => this.groups(this.recipes(), (e) => e.recipe.id));

  private groups<T extends { chapter: Chapter }>(entries: T[], id: (entry: T) => string) {
    const done = this.progress.done();
    return byChapter(entries).map((group) => {
      const doneCount = group.entries.filter((e) => done.has(id(e))).length;
      const visible = this.hideDone() ? group.entries.filter((e) => !done.has(id(e))) : group.entries;
      return { ...group, visible, done: doneCount, total: group.entries.length };
    });
  }

  /** The rank every spot shares, shown once by the name instead of under each spot. */
  protected sharedRank(entry: FishEntry): string | null {
    const [first, ...rest] = entry.spots;
    return first?.rank && rest.every((spot) => spot.rank === first.rank) ? first.rank : null;
  }

  protected toggleHideDone(): void {
    void this.progress.setPreferences({ hideDone: !this.hideDone() });
  }

  protected toggleCaught(entry: FishEntry): void {
    const caught = this.progress.done().has(entry.fish.id);
    // Unmarking a catch also clears its Rank A mark, which cannot exist without it.
    void this.progress.setDone(caught ? [entry.fish.id, rankAKey(entry.fish.id)] : [entry.fish.id], !caught);
  }

  protected toggleRankA(entry: FishEntry): void {
    const key = rankAKey(entry.fish.id);
    const on = !this.progress.done().has(key);
    // A Rank A catch is still a catch.
    void this.progress.setDone(on ? [entry.fish.id, key] : [key], on);
  }
}
