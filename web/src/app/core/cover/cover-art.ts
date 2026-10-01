/**
 * Original cover art for the library: a gradient, an abstract motif per franchise and the game's
 * name set in type, so the game is recognisable at a glance. No logos or other game assets. Kept free of Angular so scripts/render-share-image.mjs can draw the
 * same covers into the share image.
 */

export type CoverMotif = 'orbits' | 'waves' | 'stripes';
export type CoverFontId = 'cinzel' | 'uncial-antiqua';

export interface CoverStyle {
  motif: CoverMotif;
  from: string;
  to: string;
  accent: string;
  /** Display font for the title; the app's serif when missing. */
  font?: CoverFontId;
}

/**
 * Title fonts (SIL Open Font License, self-hosted through Fontsource). `width` is a safe average
 * glyph width in em, measured on the real titles, used to shrink long titles to one line.
 */
export const COVER_FONTS: Record<CoverFontId | 'default', { family: string; weight: number; width: number }> = {
  cinzel: { family: 'Cinzel', weight: 700, width: 0.56 },
  'uncial-antiqua': { family: 'Uncial Antiqua', weight: 400, width: 0.6 },
  default: { family: 'Fraunces Variable', weight: 600, width: 0.45 },
};

/** The game's name split for the cover, e.g. "Trails in the Sky" / "2nd Chapter". */
export interface CoverText {
  title: string;
  subtitle?: string;
}

export type CoverShape =
  | { kind: 'path'; d: string; width: number; opacity: number; accent?: boolean }
  | { kind: 'circle'; cx: number; cy: number; r: number; fill: boolean; opacity: number; accent?: boolean };

export const COVER_WIDTH = 400;
export const COVER_HEIGHT = 150;

/** Used for a franchise without its own cover colors: a calm slate. */
export const DEFAULT_COVER: CoverStyle = { motif: 'stripes', from: '#25304a', to: '#4a5a7d', accent: '#e9b949' };

function wave(y: number, amplitude: number, length: number): string {
  let d = `M -${length} ${y}`;
  for (let x = -length; x < COVER_WIDTH + length; x += length) d += ` q ${length / 2} ${-amplitude} ${length} 0`;
  return d;
}

const MOTIFS: Record<CoverMotif, CoverShape[]> = {
  // Orbits and stars: a sky crossed by paths.
  orbits: [
    { kind: 'circle', cx: 318, cy: 44, r: 48, fill: false, opacity: 0.35, accent: true },
    { kind: 'path', d: 'M -40 120 C 40 20 200 -10 440 20', width: 1.5, opacity: 0.35 },
    { kind: 'path', d: 'M -40 150 C 60 40 260 10 440 60', width: 2.5, opacity: 0.5, accent: true },
    { kind: 'path', d: 'M -40 175 C 80 70 280 40 440 100', width: 1.5, opacity: 0.3 },
    ...[[60, 40, 2.4], [120, 22, 1.6], [196, 52, 1.3], [262, 18, 2], [372, 92, 1.5], [28, 88, 1.5], [150, 96, 1.2]].map(
      ([cx, cy, r]): CoverShape => ({ kind: 'circle', cx, cy, r, fill: true, opacity: 0.7 }),
    ),
  ],
  // Swell and a low sun: open sea.
  waves: [
    { kind: 'circle', cx: 330, cy: 42, r: 24, fill: true, opacity: 0.6, accent: true },
    { kind: 'path', d: wave(78, 10, 48), width: 1.5, opacity: 0.25 },
    { kind: 'path', d: wave(100, 12, 56), width: 2.5, opacity: 0.45, accent: true },
    { kind: 'path', d: wave(124, 12, 64), width: 1.5, opacity: 0.3 },
    { kind: 'path', d: wave(146, 14, 72), width: 1.5, opacity: 0.2 },
  ],
  stripes: Array.from({ length: 14 }, (_, i): CoverShape => ({
    kind: 'path',
    d: `M ${i * 36 - 150} ${COVER_HEIGHT + 10} L ${i * 36} -10`,
    width: 1.5,
    opacity: i % 3 === 0 ? 0.35 : 0.15,
    accent: i % 3 === 0,
  })),
};

export const coverShapes = (motif: CoverMotif): CoverShape[] => MOTIFS[motif] ?? MOTIFS.stripes;

/** A game without cover text of its own: "Ys X: Proud Nordics" → "Ys X" / "Proud Nordics". */
export function fallbackCoverText(name: string): CoverText {
  const [title, ...rest] = name.split(':');
  return rest.length ? { title: title.trim(), subtitle: rest.join(':').trim() } : { title: name };
}

/** Where the text goes and how big: the title shrinks so a long one still fits on one line. */
export function coverTextLayout(text: CoverText, font?: CoverFontId): { titleSize: number; titleY: number; subtitleY: number } {
  const width = COVER_FONTS[font ?? 'default'].width;
  const titleSize = Math.min(46, Math.floor(350 / (text.title.length * width)));
  return text.subtitle ? { titleSize, titleY: 106, subtitleY: 132 } : { titleSize, titleY: 128, subtitleY: 0 };
}
