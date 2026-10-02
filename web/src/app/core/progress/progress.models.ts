import { ItemType, Season } from '../content/content.models';

export const PROGRESS_SCHEMA_VERSION = 1;

export interface Preferences {
  hideDone: boolean;
  /** Item types to show; empty means all. */
  filters: ItemType[];
  /** Only items that count toward a trophy. Optional, so older saves and exports stay valid. */
  trophiesOnly?: boolean;
  /** The in-game season the player is in, for games whose content depends on it. */
  season?: Season;
}

/** Saved on the device only. Exported as-is, so changes need a schemaVersion bump and a migration. */
export interface SavedProgress {
  schemaVersion: number;
  gameId: string;
  currentChapter: string;
  doneItems: string[];
  preferences: Preferences;
  updatedAt: string;
  /** Set once the player has said where they are. Optional, so older saves and exports stay valid. */
  chapterChosen?: boolean;
}

export const DEFAULT_PREFERENCES: Preferences = { hideDone: false, filters: [] };
