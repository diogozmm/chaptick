import { ChangeDetectionStrategy, Component, computed, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { GameFeature } from '../../core/content/content.models';
import { ContentService } from '../../core/content/content.service';
import { SavedGames } from '../../core/game/saved-games';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { SITE } from '../../site.config';
import { GameCard } from '../../ui/game-card/game-card';
import { Icon } from '../../ui/icon/icon';
import { ScrollHints } from '../../ui/scroll-hints/scroll-hints';

/**
 * Every game: one row of covers per series, filtered by series (?f=) or by what a game offers
 * (?t=checklist|compendium). A series filter shows that series as a grid.
 */
@Component({
  selector: 'app-library',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, Icon, ScrollHints, GameCard],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './library.html',
  styleUrl: './library.scss',
})
export class Library {
  private readonly content = inject(ContentService);
  protected readonly lang = inject(LangService);
  protected readonly suggestUrl = SITE.repoUrl ? `${SITE.repoUrl}/issues` : '';

  constructor() {
    inject(SavedGames).reload();
  }

  protected readonly franchises = computed(() => this.content.catalog()?.franchises ?? []);
  private readonly params = toSignal(inject(ActivatedRoute).queryParamMap);
  protected readonly filter = computed(() => this.franchises().find((f) => f.id === this.params()?.get('f')) ?? null);
  protected readonly featureFilter = computed<GameFeature | null>(() => {
    const t = this.params()?.get('t');
    return t === 'checklist' || t === 'compendium' ? t : null;
  });
  protected readonly gameFeatures: GameFeature[] = ['checklist', 'compendium'];
  /** Series to show, each with only the games the feature filter lets through; empty ones drop out. */
  protected readonly shown = computed(() => {
    const only = this.filter();
    const feature = this.featureFilter();
    const series = only ? [only] : this.franchises();
    if (!feature) return series;
    return series
      .map((f) => ({ ...f, games: f.games.filter((g) => (g.features ?? ['checklist']).includes(feature)) }))
      .filter((f) => f.games.length > 0);
  });
  protected readonly filtered = computed(() => this.filter() !== null || this.featureFilter() !== null);
}
