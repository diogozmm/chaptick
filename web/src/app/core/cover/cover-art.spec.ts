import { COVER_WIDTH, coverShapes, coverTextLayout, fallbackCoverText } from './cover-art';

describe('cover art', () => {
  it('draws every motif inside the cover width', () => {
    for (const motif of ['orbits', 'waves', 'stripes'] as const) {
      const shapes = coverShapes(motif);
      expect(shapes.length).toBeGreaterThan(3);
      for (const shape of shapes) if (shape.kind === 'circle') expect(shape.cx).toBeLessThanOrEqual(COVER_WIDTH);
    }
  });

  it('falls back to stripes for an unknown motif', () => {
    expect(coverShapes('nope' as never)).toEqual(coverShapes('stripes'));
  });

  it('splits a name at the colon when a game has no cover text', () => {
    expect(fallbackCoverText('Ys X: Proud Nordics')).toEqual({ title: 'Ys X', subtitle: 'Proud Nordics' });
    expect(fallbackCoverText('Trails in the Sky')).toEqual({ title: 'Trails in the Sky' });
  });

  it('accounts for wider display fonts', () => {
    const title = { title: 'Trails in the Sky' };
    const cinzel = coverTextLayout(title, 'cinzel').titleSize;
    expect(cinzel).toBeLessThan(coverTextLayout(title).titleSize);
    // Cinzel's measured width is about 0.534 em per character on this title.
    expect(cinzel * 0.534 * title.title.length).toBeLessThanOrEqual(356);
  });

  it('shrinks long titles so they fit on one line', () => {
    expect(coverTextLayout({ title: 'Ys X' }).titleSize).toBe(46);
    const long = coverTextLayout({ title: 'Trails in the Sky', subtitle: '2nd Chapter' }).titleSize;
    expect(long).toBeLessThan(46);
    expect(long * 0.45 * 'Trails in the Sky'.length).toBeLessThanOrEqual(356);
  });
});
