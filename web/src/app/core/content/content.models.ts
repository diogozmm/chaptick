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

/** What a game is split into for spoiler locking: story chapters, or areas opened in order. */
export type ProgressTerm = 'chapter' | 'area';

/** What a game offers, derived from its content at build time. */
export type GameFeature = 'checklist' | 'compendium';

export interface Game {
  id: string;
  franchise: string;
  order?: number;
  name: Localized;
  platforms: string[];
  dataVersion: number;
  progressTerm?: ProgressTerm;
  /** Game patch the content was checked against. */
  gameVersion?: string;
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
  /** Missing in older builds: treated as a checklist. */
  features?: GameFeature[];
  progressTerm?: ProgressTerm;
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
  features?: GameFeature[];
  /** Compendium totals (counts only). */
  compendium?: { entries: number; crafts: number; creatures: number; seasonal?: number };
  /** How many items have a deadline, so games without any can hide the deadlines screen. */
  deadlines?: number;
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

export const ENTRY_CATEGORIES = ['materials', 'gems', 'metals', 'fish', 'crops', 'seeds', 'food', 'potions', 'tools', 'equipment'] as const;
export type EntryCategory = (typeof ENTRY_CATEGORIES)[number];
export const SOURCE_KINDS = [
  'found', 'shop', 'forage', 'fish', 'gather', 'loot', 'random', 'task', 'drop', 'craft', 'cook', 'process', 'other',
] as const;
export type SourceKind = (typeof SOURCE_KINDS)[number];
export type Season = 'spring' | 'summer' | 'autumn' | 'winter';
export type GearSlot = 'weapon' | 'offhand' | 'head' | 'body' | 'legs' | 'feet';

/** One way to get a compendium entry: places, shops and stations, as the game names them. */
export interface Source {
  kind: SourceKind;
  where: Localized;
  seasons?: Season[];
  time?: 'day' | 'night';
}

/** Compendium: something you can get, listed in the chapter or area where it first becomes obtainable. */
export interface Entry {
  id: string;
  name: Localized;
  category: EntryCategory;
  sell?: string;
  sources: Source[];
  /** For equipment: where it goes, what it changes and any special effect. */
  gear?: { slot: GearSlot; stats?: Localized; bonuses?: Localized; effect?: Localized };
  /** For seeds: when they can be planted and how they grow. */
  grow?: { seasons: Season[]; days: number | null; harvests: number; yield: string; crop?: string };
}

/** A further way to get an earlier entry, only known from this chapter or area on. */
export interface EntrySource extends Source {
  entryId: string;
}

export type CraftKind = 'craft' | 'cook' | 'forge';

export interface Craft {
  id: string;
  name: Localized;
  kind: CraftKind;
  /** The station or section it is made at. */
  group: Localized;
  /** `entryId` is missing when the ingredient is not in the compendium (or not reached yet). */
  ingredients: { entryId?: string; name: Localized; qty: number }[];
  makes?: string;
  unlock?: Localized;
  /** Chance the recipe works, when below 100%. */
  success?: string;
}

/** An item a creature hands over; linked when it is in the compendium. */
export interface RewardItem {
  entryId?: string;
  name: Localized;
}

/**
 * How a creature gives items: stolen in battle (with a chance), at a fight or meeting, from a
 * battle loot pool, or as what winning that fight can give.
 */
export interface CreatureReward {
  how: 'steal' | 'event' | 'loot' | 'victory';
  /** The loot pool's name. */
  pool?: Localized;
  /** Shared pools this one can also draw from. */
  also?: { name: Localized; items: RewardItem[] }[];
  items: RewardItem[];
  chance?: string;
  /** Which version of the creature, for steals. */
  variant?: Localized;
  situation?: Localized;
  /** A condition, e.g. a task in progress. */
  when?: Localized;
  /** Items handed over in exchange. */
  gives?: RewardItem[];
}

export interface Creature {
  id: string;
  name: Localized;
  where: Localized[];
  spoilerLevel: SpoilerLevel;
  /** Weak points and the damage it deals. */
  notes?: Localized;
  rewards?: CreatureReward[];
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
  entries?: Entry[];
  entrySources?: EntrySource[];
  crafts?: Craft[];
  creatures?: Creature[];
}

export const localize = (text: Localized, lang: Lang): string => (lang === 'pt' ? text.pt : undefined) ?? text.en;
