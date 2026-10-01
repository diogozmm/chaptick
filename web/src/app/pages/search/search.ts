import { ChangeDetectionStrategy, Component, computed, inject, input, resource } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { SearchHit, searchItems } from '../../core/search/search';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { ItemView } from '../../core/spoiler/item-view';
import { Icon } from '../../ui/icon/icon';
import { TYPE_ICON } from '../../ui/item-type';

/** Search the unlocked chapters: names, places, route steps and hints, never anything masked. */
@Component({
  selector: 'app-search',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './search.html',
  styleUrl: './search.scss',
})
export class Search {
  private readonly access = inject(ChapterAccess);
  private readonly router = inject(Router);
  protected readonly view = inject(ItemView);
  protected readonly lang = inject(LangService);
  protected readonly game = inject(ActiveGame);
  protected readonly typeIcon = TYPE_ICON;

  /** Kept in the URL (?q=), so "back" from a result returns to the same search. */
  readonly q = input<string | undefined>();
  protected readonly query = computed(() => this.q() ?? '');

  private readonly chapters = resource({
    params: () => this.access.currentOrder(),
    loader: () => this.access.loadUnlocked(),
  });

  protected readonly hits = computed(() =>
    searchItems(this.chapters.hasValue() ? this.chapters.value() : [], this.query(), this.lang.lang(), {
      name: (item) => this.view.showLocation(item),
      hint: (item) => this.view.showHint(item),
    }),
  );
  protected readonly searching = computed(() => this.query().trim().length >= 2 && this.chapters.hasValue());

  protected setQuery(value: string): void {
    void this.router.navigate([], { queryParams: { q: value || null }, replaceUrl: true });
  }

  protected parts(hit: SearchHit): [string, string, string] {
    const { text, start, length } = hit;
    return [text.slice(0, start), text.slice(start, start + length), text.slice(start + length)];
  }
}
