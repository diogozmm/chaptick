import { GameEvent, Season } from '../content/content.models';
import { CompendiumIndex, IndexedEntry, PlacedSource } from './compendium';

export const SEASONS: Season[] = ['spring', 'summer', 'autumn', 'winter'];
export const nextSeason = (season: Season): Season => SEASONS[(SEASONS.indexOf(season) + 1) % SEASONS.length];

export interface SeasonalEntry {
  entry: IndexedEntry;
  /** The ways to get it in the season asked about. */
  sources: PlacedSource[];
  /** Every season it can be had in, when every way to get it depends on the season. */
  seasons: Season[];
  /** It cannot be had next season: get it now or wait for it to come back around. */
  lastChance: boolean;
}

export interface Plantable {
  entry: IndexedEntry;
  /** It cannot be planted next season. */
  lastChance: boolean;
  /** Plantable all year. */
  anytime: boolean;
}

export interface SeasonView {
  /** Seeds that can be planted now, last chances first. */
  plant: Plantable[];
  /** Only obtainable in some seasons, this one included. */
  only: SeasonalEntry[];
  /** Obtainable any time, but some ways only work this season (e.g. foraging spots). */
  also: SeasonalEntry[];
  /** Only obtainable in some seasons, starting next season. */
  coming: SeasonalEntry[];
}

/** Whether a game's reached content says anything about seasons at all. */
export const hasSeasons = (index: CompendiumIndex): boolean =>
  index.events.length > 0 || [...index.entries.values()].some((e) => e.entry.grow || e.sources.some((s) => s.source.seasons?.length));

export interface Calendar {
  /** Events on the given day (empty when no day is set). */
  today: GameEvent[];
  /** Dated events later this season (or all of them, when no day is set), soonest first. */
  upcoming: { event: GameEvent; day: number }[];
  weekly: GameEvent[];
}

/** What the season holds, around the player's day when they set one. */
export function calendar(events: readonly GameEvent[], season: Season, day: number | null): Calendar {
  const dated = events.filter((e) => e.days && (!e.season || e.season === season));
  const today = day ? dated.filter((e) => e.days!.includes(day)) : [];
  const upcoming = dated
    .flatMap((event) => event.days!.filter((d) => !day || d > day).map((d) => ({ event, day: d })))
    .sort((a, b) => a.day - b.day);
  return { today, upcoming, weekly: events.filter((e) => e.weekly) };
}

/**
 * What a season changes, from the reached chapters (or areas) only. An entry counts as seasonal
 * when every way to get it is tied to a season; names come first in alphabetical order.
 */
export function seasonView(index: CompendiumIndex, season: Season): SeasonView {
  const next = nextSeason(season);
  const view: SeasonView = { plant: [], only: [], also: [], coming: [] };
  for (const entry of index.entries.values()) {
    const seasonal = entry.sources.filter((s) => s.source.seasons?.length);
    if (seasonal.length === 0) continue;
    const strict = seasonal.length === entry.sources.length;
    const seasons = SEASONS.filter((x) => seasonal.some((s) => s.source.seasons!.includes(x)));
    const now = seasonal.filter((s) => s.source.seasons!.includes(season));
    if (now.length > 0) {
      const item = { entry, sources: now, seasons: strict ? seasons : [], lastChance: strict && !seasons.includes(next) };
      (strict ? view.only : view.also).push(item);
    } else if (strict && seasons.includes(next)) {
      view.coming.push({ entry, sources: seasonal.filter((s) => s.source.seasons!.includes(next)), seasons, lastChance: false });
    }
  }
  for (const entry of index.entries.values()) {
    const seasons = entry.entry.grow?.seasons;
    if (!seasons?.includes(season)) continue;
    view.plant.push({ entry, lastChance: !seasons.includes(next), anytime: seasons.length === SEASONS.length });
  }
  view.plant.sort((a, b) => Number(b.lastChance) - Number(a.lastChance) || Number(a.anytime) - Number(b.anytime)
    || a.entry.entry.name.en.localeCompare(b.entry.entry.name.en));
  const byName = (a: SeasonalEntry, b: SeasonalEntry) => a.entry.entry.name.en.localeCompare(b.entry.entry.name.en);
  view.only.sort((a, b) => Number(b.lastChance) - Number(a.lastChance) || byName(a, b));
  view.also.sort(byName);
  view.coming.sort(byName);
  return view;
}
