/** Mirrors content/schema/*.schema.json. Keep both in sync. */
export type Lang = 'en' | 'pt';

export interface Localized {
  en: string;
  pt?: string;
}

export const ITEM_TYPES = ['quest', 'hidden_quest', 'missable', 'collectible'] as const;
export type ItemType = (typeof ITEM_TYPES)[number];
export type SpoilerLevel = 0 | 1 | 2;

export interface Game {
  id: string;
  name: Localized;
  platforms: string[];
  dataVersion: number;
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
  chapters: ChapterSummary[];
}

export interface Checkpoint {
  id: string;
  order: number;
  neutralDescription: Localized;
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
  rank: FishRank;
  where: Localized;
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
