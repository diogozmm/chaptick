import { ChangeDetectionStrategy, Component, computed, inject, resource, signal } from '@angular/core';
import { NgTemplateOutlet } from '@angular/common';
import { TranslocoPipe } from '@jsverse/transloco';

import { FishEntry, fishBook, fishStats, rankAKey, recipeBook } from '../../core/collections/collections';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { Icon } from '../../ui/icon/icon';

type Tab = 'fish' | 'recipes';

/** Fishing notebook and recipe book, limited to what the unlocked chapters reveal. */
@Component({
  selector: 'app-collections',
  imports: [NgTemplateOutlet, TranslocoPipe, LocalizePipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './collections.html',
  styleUrl: './collections.scss',
})
export class Collections {
  private readonly access = inject(ChapterAccess);
  protected readonly progress = inject(ProgressStore);
  protected readonly lang = inject(LangService);

  protected readonly tab = signal<Tab>('fish');
  protected readonly rankAKey = rankAKey;

  private readonly chapters = resource({
    params: () => this.access.currentOrder(),
    loader: () => this.access.loadUnlocked(),
  });
  private readonly loaded = computed(() => (this.chapters.hasValue() ? this.chapters.value() : []));

  protected readonly fish = computed(() => fishBook(this.loaded()));
  protected readonly fishStats = computed(() => fishStats(this.fish(), this.progress.done()));
  protected readonly recipes = computed(() => recipeBook(this.loaded()));
  protected readonly recipeStats = computed(() => {
    const done = this.progress.done();
    const { standard, customized } = this.recipes();
    const count = (list: { recipe: { id: string } }[]) => list.filter((e) => done.has(e.recipe.id)).length;
    return { standard: count(standard), standardTotal: standard.length, customized: count(customized), customizedTotal: customized.length };
  });

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
