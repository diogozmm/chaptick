import { ChangeDetectionStrategy, Component, computed, inject, input, resource } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { compendiumIndex } from '../../core/compendium/compendium';
import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { OriginalPipe } from '../../core/i18n/original.pipe';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { Icon } from '../../ui/icon/icon';
import { SpoilerReveal } from '../../ui/spoiler-reveal/spoiler-reveal';

/**
 * One creature: where it shows up and exactly what it gives (stolen in battle with its chance, or
 * handed over at a fight or meeting, with any condition and what you give in exchange). Only
 * creatures from reached chapters (or areas) are found.
 */
@Component({
  selector: 'app-creature',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, OriginalPipe, Icon, SpoilerReveal],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './creature.html',
  styleUrl: './creature.scss',
})
export class CreatureDetail {
  private readonly access = inject(ChapterAccess);
  protected readonly game = inject(ActiveGame);
  protected readonly lang = inject(LangService);

  readonly creatureId = input.required<string>();

  private readonly chapters = resource({
    params: () => this.access.currentOrder(),
    loader: () => this.access.loadUnlocked(),
  });
  protected readonly ready = computed(() => this.chapters.hasValue());
  private readonly index = computed(() => compendiumIndex(this.chapters.hasValue() ? this.chapters.value() : []));
  protected readonly found = computed(() => {
    const creatures = this.index().creatures;
    const at = creatures.findIndex((c) => c.creature.id === this.creatureId());
    return at < 0 ? null : { ...creatures[at], n: at + 1 };
  });
  protected readonly steals = computed(() => (this.found()?.creature.rewards ?? []).filter((r) => r.how === 'steal'));
  protected readonly events = computed(() => (this.found()?.creature.rewards ?? []).filter((r) => r.how === 'event'));
  /** Battle loot pools first, then what winning the fight gives. */
  protected readonly loot = computed(() =>
    (this.found()?.creature.rewards ?? [])
      .filter((r) => r.how === 'loot' || r.how === 'victory')
      .sort((a, b) => Number(a.how === 'victory') - Number(b.how === 'victory')),
  );
}
