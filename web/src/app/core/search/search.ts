import { Chapter, Item, Lang, localize } from '../content/content.models';

export type MatchField = 'name' | 'location' | 'step' | 'hint';

export interface SearchHit {
  chapter: Chapter;
  item: Item;
  field: MatchField;
  /** The matching text, cut around the match for long hints. */
  text: string;
  /** Where the first query word sits in `text`, for highlighting. */
  start: number;
  length: number;
}

/** What may be searched right now: the same rules that decide what is shown. */
export interface SearchVisibility {
  name(item: Item): boolean;
  hint(item: Item): boolean;
}

const FIELD_ORDER: MatchField[] = ['name', 'location', 'step', 'hint'];
const MAX_HITS = 60;
const SNIPPET = 70;

/** Lower case without accents, so "oland" finds "Öland" and "acao" finds "ação". */
export const normalize = (text: string): string =>
  text.normalize('NFD').replace(/\p{Diacritic}/gu, '').toLowerCase();

/**
 * Finds items whose visible text contains every word of the query. Only the chapters passed in
 * are searched (callers pass the unlocked ones), and masked text is never searched, so a result
 * can never reveal what the player chose not to see. Name matches come first, then location,
 * route steps and hints; each group in chapter order.
 */
export function searchItems(chapters: readonly Chapter[], query: string, lang: Lang, visible: SearchVisibility): SearchHit[] {
  const words = normalize(query).split(/\s+/).filter((w) => w.length > 0);
  if (words.join('').length < 2) return [];
  const hits: (SearchHit & { rank: number; order: number })[] = [];

  for (const chapter of chapters) {
    for (const item of chapter.items) {
      const fields: [MatchField, string][] = [];
      if (visible.name(item)) {
        fields.push(['name', localize(item.name, lang)], ['location', localize(item.location, lang)]);
        // The game may show the English name even to a Portuguese reader.
        if (item.name.en !== localize(item.name, lang)) fields.push(['name', item.name.en]);
      }
      if (visible.hint(item)) {
        for (const step of item.steps ?? []) fields.push(['step', localize(step.text, lang)]);
        fields.push(['hint', localize(item.hint, lang)]);
      }
      if (fields.length === 0) continue;
      const all = normalize(fields.map(([, text]) => text).join(' '));
      if (!words.every((w) => all.includes(w))) continue;

      // Report the most telling field that holds the first word.
      const best = [...fields]
        .sort((a, b) => FIELD_ORDER.indexOf(a[0]) - FIELD_ORDER.indexOf(b[0]))
        .find(([, text]) => normalize(text).includes(words[0]));
      if (!best) continue;
      const [field, full] = best;
      const at = normalize(full).indexOf(words[0]);
      const from = field === 'hint' ? Math.max(0, at - SNIPPET / 2) : 0;
      const cut = field === 'hint' && full.length > from + SNIPPET * 2;
      const text = (from > 0 ? '…' : '') + full.slice(from, cut ? from + SNIPPET * 2 : undefined) + (cut ? '…' : '');
      hits.push({
        chapter, item, field, text,
        start: at - from + (from > 0 ? 1 : 0),
        length: words[0].length,
        rank: FIELD_ORDER.indexOf(field),
        order: chapter.order,
      });
    }
  }
  return hits
    .sort((a, b) => a.rank - b.rank || a.order - b.order)
    .slice(0, MAX_HITS)
    .map(({ rank: _rank, order: _order, ...hit }) => hit);
}
