import { Chapter, Craft, Creature, Entry, EntryCategory, Lang, Source, localize } from '../content/content.models';
import { normalize } from '../search/search';

/** A way to get an entry, with the chapter or area where it applies. */
export interface PlacedSource {
  source: Source;
  chapter: Chapter;
}

export interface IndexedEntry {
  entry: Entry;
  /** Where it first becomes obtainable. */
  chapter: Chapter;
  /** Every known way to get it, earliest chapter first. */
  sources: PlacedSource[];
}

export interface IndexedCraft {
  craft: Craft;
  chapter: Chapter;
}

export interface IndexedCreature {
  creature: Creature;
  chapter: Chapter;
}

/** Everything the reached chapters say about one game's compendium, linked both ways. */
export interface CompendiumIndex {
  entries: Map<string, IndexedEntry>;
  crafts: IndexedCraft[];
  creatures: IndexedCreature[];
  /** Crafts that make an entry. */
  madeBy: Map<string, IndexedCraft[]>;
  /** Crafts that use an entry as an ingredient. */
  usedIn: Map<string, IndexedCraft[]>;
  /** Creatures that give an entry. */
  givenBy: Map<string, IndexedCreature[]>;
}

const push = <K, V>(map: Map<K, V[]>, key: K, value: V): void => {
  const list = map.get(key);
  if (list) list.push(value);
  else map.set(key, [value]);
};

/**
 * Builds the compendium from the chapters passed in, which callers limit to the unlocked ones: a
 * later source, craft or creature simply isn't there yet. Links only point backwards in content, so
 * nothing here can name something from a chapter that was not passed.
 */
export function compendiumIndex(chapters: readonly Chapter[]): CompendiumIndex {
  const sorted = [...chapters].sort((a, b) => a.order - b.order);
  const index: CompendiumIndex = {
    entries: new Map(), crafts: [], creatures: [], madeBy: new Map(), usedIn: new Map(), givenBy: new Map(),
  };
  for (const chapter of sorted) {
    for (const entry of chapter.entries ?? []) {
      index.entries.set(entry.id, { entry, chapter, sources: entry.sources.map((source) => ({ source, chapter })) });
    }
    for (const { entryId, ...source } of chapter.entrySources ?? []) {
      index.entries.get(entryId)?.sources.push({ source, chapter });
    }
    for (const craft of chapter.crafts ?? []) {
      const placed = { craft, chapter };
      index.crafts.push(placed);
      if (craft.makes) push(index.madeBy, craft.makes, placed);
      for (const ingredient of craft.ingredients) if (ingredient.entryId) push(index.usedIn, ingredient.entryId, placed);
    }
    for (const creature of chapter.creatures ?? []) {
      const placed = { creature, chapter };
      index.creatures.push(placed);
      const given = new Set((creature.rewards ?? []).flatMap((r) => r.items).flatMap((i) => (i.entryId ? [i.entryId] : [])));
      for (const entryId of given) push(index.givenBy, entryId, placed);
    }
  }
  return index;
}

/**
 * Entries whose name (in the reader's language or in English, as the game may show either) holds
 * every word of the query, optionally in one category. Names starting with the query come first,
 * then alphabetical. An empty query lists the category (or nothing).
 */
export function findEntries(
  index: CompendiumIndex,
  query: string,
  lang: Lang,
  category: EntryCategory | null = null,
): IndexedEntry[] {
  const words = normalize(query).split(/\s+/).filter((w) => w.length > 0);
  if (words.length === 0 && !category) return [];
  const name = (e: IndexedEntry) => normalize(localize(e.entry.name, lang));
  const both = (e: IndexedEntry) => `${name(e)} ${normalize(e.entry.name.en)}`;
  return [...index.entries.values()]
    .filter((e) => (!category || e.entry.category === category) && words.every((w) => both(e).includes(w)))
    .map((e) => ({ e, starts: words.length > 0 && (name(e).startsWith(words[0]) || normalize(e.entry.name.en).startsWith(words[0])) }))
    .sort((a, b) => Number(b.starts) - Number(a.starts) || name(a.e).localeCompare(name(b.e)))
    .map(({ e }) => e);
}

/** How many entries each category has, in the order categories are listed. */
export function categoryCounts(index: CompendiumIndex): Map<EntryCategory, number> {
  const counts = new Map<EntryCategory, number>();
  for (const { entry } of index.entries.values()) counts.set(entry.category, (counts.get(entry.category) ?? 0) + 1);
  return counts;
}
