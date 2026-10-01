import { CoverStyle, CoverText } from '../cover/cover-art';

/** Mirrors content/schema/*.schema.json. Keep both in sync. */
export type Lang = 'en' | 'pt';

export interface Localized {
  en: string;
  pt?: string;
}

export const ITEM_TYPES = ['quest', 'hidden_quest', 'missable', 'collectible'] as const;
export type ItemType = (typeof ITEM_TYPES)[number];
export type SpoilerLevel = 0 | 1 | 2;

export interface Trophy {
  id: string;
  /** Official English name. */
  name: string;
  description: Localized;
  /** Tied to a whole collection screen instead of checklist items. */
  collection?: 'fish' | 'recipes';
}

export interface Game {
  id: string;
  franchise: string;
  order?: number;
  name: Localized;
  platforms: string[];
  dataVersion: number;
  /** Trophies tied to what the app tracks; see content/schema/game.schema.json. */
  trophies?: Trophy[];
}

/** A game as listed in the library: counts only, nothing that could spoil. */
export interface CatalogGame {
  id: string;
  name: Localized;
  /** Text drawn on the library cover; derived from the name when missing. */
  cover?: CoverText;
  platforms: string[];
  chapterCount: number;
  itemCount: number;
}

export interface Franchise {
  id: string;
  name: Localized;
  description?: Localized;
  games: CatalogGame[];
  cover?: CoverStyle;
}

export interface Catalog {
  franchises: Franchise[];
}

/** What the manifest knows about a chapter: enough to show it locked, never its items. */
export interface ChapterSummary {
  id: string;
  order: number;
  neutralLabel: Localized;
  itemCount: number;
  file: string;
}

export interface Manifest {
  game: Game;
  /** How many fish and recipes the whole game has (counts only); missing in older builds. */
  collections?: { fish: number; recipes: number };
  chapters: ChapterSummary[];
}

export interface Checkpoint {
  id: string;
  order: number;
  neutralDescription: Localized;
}

export interface RouteStep {
  text: Localized;
}

export interface Item {
  id: string;
  type: ItemType;
  name: Localized;
  location: Localized;
  availableUntil: string | null;
  hint: Localized;
  spoilerLevel: SpoilerLevel;
  sources: string[];
  /** Ids of the game's trophies this item counts toward. */
  trophies?: string[];
  /** Route through the area; each stop can be ticked on its own. */
  steps?: RouteStep[];
}

export interface ItemText {
  itemId: string;
  text: Localized;
  author: string;
  license: string;
  approvedAt: string;
}

export interface Boss {
  id: string;
  name: Localized;
  location: Localized;
  /** Quest or missable this fight belongs to, if any. */
  relatedItem?: string;
  strategy: Localized;
  sources: string[];
}

export type FishRank = 'A' | 'B' | 'C';

export interface Fish {
  id: string;
  name: Localized;
  sources: string[];
}

/** A good spot in the chapter's region; may refer to a fish from an earlier chapter. */
export interface FishSpot {
  fishId: string;
  /** Best size rank here, for games that grade catches. */
  rank?: FishRank;
  where: Localized;
  /** Bait needed here, for games where bait decides the catch. */
  bait?: string;
}

export interface Recipe {
  id: string;
  kind: 'standard' | 'customized';
  name: Localized;
  source: Localized;
  sources: string[];
}

export interface Chapter {
  id: string;
  gameId: string;
  order: number;
  neutralLabel: Localized;
  checkpoints: Checkpoint[];
  items: Item[];
  itemTexts: ItemText[];
  bosses?: Boss[];
  fish?: Fish[];
  fishSpots?: FishSpot[];
  recipes?: Recipe[];
}

export const localize = (text: Localized, lang: Lang): string => (lang === 'pt' ? text.pt : undefined) ?? text.en;
