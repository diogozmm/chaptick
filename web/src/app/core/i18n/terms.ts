import { ProgressTerm } from '../content/content.models';

/**
 * Texts that name a chapter, with an "area" wording under `area.` in the i18n files. Games split
 * by areas (opened in order) read those instead, e.g. "Which area have you reached?".
 */
const AREA_KEYS = new Set([
  'where.title', 'where.intro', 'where.locked', 'where.pickTitle', 'where.pickIntro', 'where.confirmAdvance',
  'checklist.eyebrow', 'checklist.empty', 'checklist.nextChapter', 'checklist.advanceTo',
  'home.whereAmI', 'home.counts', 'home.pickChapter', 'search.label', 'search.hint', 'howItWorks.tick',
]);

export const termKey = (key: string, term: ProgressTerm | undefined): string =>
  term === 'area' && AREA_KEYS.has(key) ? `area.${key}` : key;
