import { ChangeDetectionStrategy, Component, computed, inject, input, resource } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { compendiumIndex, PlacedSource } from '../../core/compendium/compendium';
import { SOURCE_KINDS, SourceKind, localize } from '../../core/content/content.models';
import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { OriginalPipe } from '../../core/i18n/original.pipe';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { SITE } from '../../site.config';
import { Icon } from '../../ui/icon/icon';
import { SpoilerReveal } from '../../ui/spoiler-reveal/spoiler-reveal';

/**
 * One compendium entry: every way to get it in the reached chapters (or areas), what makes it,
 * what it goes into and which creatures give it. An entry from further ahead is simply not found,
 * since only unlocked files are loaded.
 */
@Component({
  selector: 'app-entry',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, OriginalPipe, Icon, SpoilerReveal],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './entry.html',
  styleUrl: './entry.scss',
})
export class EntryDetail {
  private readonly access = inject(ChapterAccess);
  protected readonly game = inject(ActiveGame);
  protected readonly lang = inject(LangService);

  readonly entryId = input.required<string>();

  private readonly chapters = resource({
    params: () => this.access.currentOrder(),
    loader: () => this.access.loadUnlocked(),
  });
  protected readonly ready = computed(() => this.chapters.hasValue());
  private readonly index = computed(() => compendiumIndex(this.chapters.hasValue() ? this.chapters.value() : []));
  protected readonly found = computed(() => this.index().entries.get(this.entryId()));

  /** Sources grouped by kind, in a fixed order: places first, making things last. */
  protected readonly ways = computed(() => {
    const groups = new Map<SourceKind, PlacedSource[]>();
    for (const placed of this.found()?.sources ?? []) {
      const list = groups.get(placed.source.kind) ?? [];
      list.push(placed);
      groups.set(placed.source.kind, list);
    }
    return SOURCE_KINDS.filter((k) => groups.has(k)).map((kind) => ({ kind, sources: groups.get(kind)! }));
  });
  /** The entry's page on the game's wiki, where the facts come from. */
  protected readonly wikiUrl = computed(() => {
    const base = SITE.wikis[this.game.id() ?? ''];
    const found = this.found();
    return base && found ? base + encodeURIComponent(found.entry.name.en.replace(/ /g, '_')) : null;
  });
  protected statList(stats: string): string[] {
    return stats.split(';').map((s) => s.trim()).filter((s) => s);
  }

  protected cropName(entryId: string): string | null {
    const crop = this.index().entries.get(entryId);
    return crop ? localize(crop.entry.name, this.lang.lang()) : null;
  }

  protected readonly madeBy = computed(() => this.index().madeBy.get(this.entryId()) ?? []);
  protected readonly usedIn = computed(() => this.index().usedIn.get(this.entryId()) ?? []);
  protected readonly givenBy = computed(() => this.index().givenBy.get(this.entryId()) ?? []);
  protected readonly creatureNumber = computed(() => new Map(this.index().creatures.map((c, i) => [c.creature.id, i + 1])));

  protected readonly kindIcon: Record<SourceKind, 'map-pin' | 'gem' | 'fish' | 'sparkles' | 'flag' | 'utensils-crossed' | 'scroll-text' | 'swords' | 'compass'> = {
    found: 'map-pin', shop: 'gem', forage: 'compass', fish: 'fish', gather: 'compass', loot: 'sparkles',
    random: 'sparkles', task: 'flag', drop: 'swords', craft: 'scroll-text', cook: 'utensils-crossed',
    process: 'scroll-text', other: 'map-pin',
  };
}
