import { ChangeDetectionStrategy, Component, computed, inject, input, resource } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { TranslocoPipe, TranslocoService } from '@jsverse/transloco';
import { NgTemplateOutlet } from '@angular/common';

import { categoryCounts, compendiumIndex, findEntries, IndexedCraft } from '../../core/compendium/compendium';
import { hasSeasons, nextSeason, SEASONS, seasonView } from '../../core/compendium/seasons';
import { Chapter, CraftKind, Creature, ENTRY_CATEGORIES, EntryCategory, Localized, Season, SourceKind, localize } from '../../core/content/content.models';
import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { OriginalPipe } from '../../core/i18n/original.pipe';
import { GameNamePipe } from '../../core/i18n/game-name.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { normalize } from '../../core/search/search';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { Icon } from '../../ui/icon/icon';
import { SpoilerReveal } from '../../ui/spoiler-reveal/spoiler-reveal';
import { SeasonCalendar } from '../../ui/season-calendar/season-calendar';

type Tab = 'items' | 'crafts' | 'creatures' | 'season' | 'villagers';
const TABS: Tab[] = ['items', 'crafts', 'creatures', 'season', 'villagers'];
const CRAFT_KINDS: CraftKind[] = ['craft', 'cook', 'forge', 'process'];
const MAX_LIST = 80;

/**
 * Compendium: where to get things, what makes what, and the creatures met so far. Built only from
 * the unlocked chapters (or areas), like everything else. State lives in the URL (?tab=, ?q=, ?c=),
 * so "back" from an entry returns to the same list.
 */
@Component({
  selector: 'app-compendium',
  imports: [RouterLink, NgTemplateOutlet, TranslocoPipe, LocalizePipe, OriginalPipe, GameNamePipe, Icon, SpoilerReveal, SeasonCalendar],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './compendium.html',
  styleUrl: './compendium.scss',
})
export class Compendium {
  private readonly access = inject(ChapterAccess);
  private readonly router = inject(Router);
  private readonly transloco = inject(TranslocoService);
  protected readonly game = inject(ActiveGame);
  protected readonly progress = inject(ProgressStore);
  protected readonly lang = inject(LangService);
  protected readonly names = computed(() => this.progress.preferences().names);

  readonly tab = input<string | undefined>();
  readonly q = input<string | undefined>();
  /** Category (items tab) or craft kind (crafts tab). */
  readonly c = input<string | undefined>();

  /** The season tab only for games whose reached content depends on the season. */
  protected readonly tabs = computed(() =>
    TABS.filter((t) => (t !== 'season' || this.seasonal()) && (t !== 'villagers' || this.index().villagers.length > 0)),
  );
  protected readonly villagers = computed(() => this.index().villagers);
  protected readonly commonGifts = computed(() => this.index().commonGifts);
  protected readonly friendship = computed(() => this.index().friendship);
  protected adventureName(itemId: string): Localized | null {
    return this.index().items.get(itemId)?.name ?? null;
  }
  protected readonly reactions = ['likes', 'neutral', 'hates'] as const;
  protected readonly categories = ENTRY_CATEGORIES;
  protected readonly craftKinds = CRAFT_KINDS;
  protected readonly current = computed<Tab>(() => (TABS as string[]).includes(this.tab() ?? '') ? (this.tab() as Tab) : 'items');
  protected readonly query = computed(() => this.q() ?? '');
  protected readonly here = this.access.current;

  private readonly chapters = resource({
    params: () => this.access.currentOrder(),
    loader: () => this.access.loadUnlocked(),
  });
  protected readonly ready = computed(() => this.chapters.hasValue());
  private readonly index = computed(() => compendiumIndex(this.chapters.hasValue() ? this.chapters.value() : []));
  protected readonly counts = computed(() => categoryCounts(this.index()));

  protected readonly seasonal = computed(() => hasSeasons(this.index()));
  protected readonly seasons = SEASONS;
  /** The player's in-game season, remembered per game. */
  protected readonly season = computed(() => this.progress.preferences().season ?? null);
  protected readonly next = computed(() => (this.season() ? nextSeason(this.season()!) : null));
  protected readonly seasonNow = computed(() => (this.season() ? seasonView(this.index(), this.season()!) : null));

  protected seasonNames(seasons: Season[]): string {
    return seasons.map((s) => this.transloco.translate(`compendium.seasonShort.${s}`)).join(', ');
  }

  protected readonly events = computed(() => this.index().events);

  protected setSeason(season: Season): void {
    void this.progress.setPreferences({ season });
  }

  protected sourceIcon(kind: SourceKind): 'fish' | 'compass' | 'map-pin' {
    return kind === 'fish' ? 'fish' : kind === 'forage' ? 'compass' : 'map-pin';
  }

  protected readonly category = computed<EntryCategory | null>(() =>
    (ENTRY_CATEGORIES as readonly string[]).includes(this.c() ?? '') ? (this.c() as EntryCategory) : null,
  );
  private readonly found = computed(() => findEntries(this.index(), this.query(), this.lang.lang(), this.category(), this.names()));
  protected readonly entries = computed(() => this.found().slice(0, MAX_LIST));
  protected readonly moreEntries = computed(() => Math.max(0, this.found().length - MAX_LIST));
  protected readonly listing = computed(() => this.query().trim().length > 0 || this.category() !== null);

  protected readonly craftKind = computed<CraftKind>(() =>
    (CRAFT_KINDS as string[]).includes(this.c() ?? '') ? (this.c() as CraftKind) : 'craft',
  );
  /** Crafts of the chosen kind matching the query, grouped by station or section. */
  protected readonly craftGroups = computed(() => {
    const words = normalize(this.query()).split(/\s+/).filter((w) => w.length > 0);
    const lang = this.lang.lang();
    // Names in the reader's language and in English: the game may show either.
    const names = (text: Localized) => `${localize(text, lang)} ${text.en}`;
    const matches = (c: IndexedCraft) => {
      const text = normalize([names(c.craft.name), ...c.craft.ingredients.map((i) => names(i.name))].join(' '));
      return words.every((w) => text.includes(w));
    };
    const groups = new Map<string, { label: Localized; crafts: IndexedCraft[] }>();
    for (const c of this.index().crafts) {
      if (c.craft.kind !== this.craftKind() || !matches(c)) continue;
      const group = groups.get(c.craft.group.en) ?? { label: c.craft.group, crafts: [] };
      group.crafts.push(c);
      groups.set(c.craft.group.en, group);
    }
    return [...groups].map(([key, group]) => ({ key, ...group }));
  });
  protected readonly craftCounts = computed(() => {
    const counts = new Map<CraftKind, number>();
    for (const { craft } of this.index().crafts) counts.set(craft.kind, (counts.get(craft.kind) ?? 0) + 1);
    return counts;
  });

  /** Only creatures that give items (?c=gives on the creatures tab). */
  protected readonly givingOnly = computed(() => this.current() === 'creatures' && this.c() === 'gives');

  protected whereList(creature: Creature): string {
    return creature.where.map((w) => localize(w, this.lang.lang())).join(' · ');
  }

  /** Creatures by the chapter or area they are first met in, numbered for their placeholders. */
  protected readonly creatureGroups = computed(() => {
    const groups = new Map<string, { chapter: Chapter; creatures: { n: number; creature: Creature }[] }>();
    let n = 0;
    for (const { creature, chapter } of this.index().creatures) {
      if (this.givingOnly() && !creature.rewards?.length) continue;
      const group = groups.get(chapter.id) ?? { chapter, creatures: [] };
      group.creatures.push({ n: ++n, creature });
      groups.set(chapter.id, group);
    }
    return [...groups.values()];
  });

  protected entryName(entryId: string): string | null {
    const found = this.index().entries.get(entryId);
    return found ? localize(found.entry.name, this.lang.lang()) : null;
  }

  protected go(params: { tab?: Tab; q?: string | null; c?: string | null }): void {
    const next = { tab: this.current(), q: this.q() ?? null, c: this.c() ?? null, ...params };
    void this.router.navigate([], {
      queryParams: { tab: next.tab === 'items' ? null : next.tab, q: next.q || null, c: next.c || null },
      replaceUrl: true,
    });
  }

  protected switchTab(tab: Tab): void {
    this.go({ tab, q: null, c: null });
  }
}
