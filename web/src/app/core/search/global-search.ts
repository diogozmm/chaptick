import { Injectable, inject } from '@angular/core';

import { CompendiumIndex, IndexedCreature, IndexedEntry, compendiumIndex, findEntries } from '../compendium/compendium';
import { CatalogGame, Chapter, Lang, Villager, localize } from '../content/content.models';
import { ContentService } from '../content/content.service';
import { SavedProgress } from '../progress/progress.models';
import { RevealService } from '../spoiler/reveal.service';
import { isMasked } from '../spoiler/spoiler';
import { SearchHit, normalize, searchItems } from './search';

/** A started game's chapters (or areas) the player has reached: the only ones search may read. */
export interface ReachedGame {
  gameId: string;
  game: CatalogGame;
  chapters: Chapter[];
  index: CompendiumIndex;
  names: Record<string, string>;
}

export interface GameResults {
  gameId: string;
  game: CatalogGame;
  /** Tasks and checklist items whose name matches. */
  items: SearchHit[];
  /** Tasks and checklist items that only match in their place or hint: less telling, listed last. */
  related: SearchHit[];
  entries: IndexedEntry[];
  creatures: IndexedCreature[];
  villagers: Villager[];
  total: number;
}

const PER_KIND = 4;

/** Loads, for every started game, the chapters up to the saved one, never further. */
@Injectable({ providedIn: 'root' })
export class GlobalSearch {
  private readonly content = inject(ContentService);
  private readonly reveals = inject(RevealService);

  async reached(saved: readonly SavedProgress[]): Promise<ReachedGame[]> {
    const games = await Promise.all(
      saved.map(async (progress) => {
        const game = this.content.game(progress.gameId);
        if (!game) return null;
        const manifest = await this.content.loadManifest(progress.gameId);
        const current = manifest.chapters.find((c) => c.id === progress.currentChapter) ?? manifest.chapters[0];
        if (!current) return null;
        const unlocked = manifest.chapters.filter((c) => c.order <= current.order);
        const chapters = await Promise.all(unlocked.map((c) => this.content.loadChapter(progress.gameId, c)));
        return { gameId: progress.gameId, game, chapters, index: compendiumIndex(chapters), names: progress.preferences.names ?? {} };
      }),
    );
    return games.filter((g) => g !== null);
  }

  /** What a query finds in one reached game. Masked names are never searched (unless revealed). */
  search(reached: ReachedGame, query: string, lang: Lang): GameResults {
    const visible = (id: string, level: 0 | 1 | 2) => !isMasked(level) || this.reveals.isRevealed(id);
    const items = searchItems(reached.chapters, query, lang, {
      name: (item) => visible(item.id, item.spoilerLevel),
      hint: (item) => item.spoilerLevel !== 1 || this.reveals.isRevealed(item.id),
    });
    const entries = findEntries(reached.index, query, lang, null, reached.names);
    const words = normalize(query).split(/\s+/).filter((w) => w);
    const matches = (...names: string[]) => {
      const text = normalize(names.join(' '));
      return words.length > 0 && words.every((w) => text.includes(w));
    };
    const creatures = reached.index.creatures.filter(
      ({ creature }) =>
        visible(creature.id, creature.spoilerLevel) &&
        matches(reached.names[creature.id] ?? '', localize(creature.name, lang), creature.name.en),
    );
    const villagers = reached.index.villagers.filter((v) => matches(localize(v.name, lang), v.name.en));
    const named = items.filter((h) => h.field === 'name');
    const related = items.filter((h) => h.field !== 'name');
    return {
      gameId: reached.gameId,
      game: reached.game,
      items: named.slice(0, PER_KIND),
      related: related.slice(0, Math.max(0, PER_KIND - named.length)),
      entries: entries.slice(0, PER_KIND),
      creatures: creatures.slice(0, PER_KIND),
      villagers: villagers.slice(0, PER_KIND),
      total: items.length + entries.length + creatures.length + villagers.length,
    };
  }
}
