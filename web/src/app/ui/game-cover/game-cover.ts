import { ChangeDetectionStrategy, Component, computed, input } from '@angular/core';

import { COVER_FONTS, COVER_HEIGHT, COVER_WIDTH, CoverStyle, CoverText, DEFAULT_COVER, coverShapes, coverTextLayout } from '../../core/cover/cover-art';

let nextId = 0;

/** A game's cover in the library: original art and its name in type (see cover-art.ts). The card names the game for screen readers, so this is decorative. */
@Component({
  selector: 'app-game-cover',
  changeDetection: ChangeDetectionStrategy.OnPush,
  host: { 'aria-hidden': 'true' },
  template: `
    @let s = style();
    <svg [attr.viewBox]="viewBox" preserveAspectRatio="xMidYMid slice" focusable="false">
      <defs>
        <linearGradient [attr.id]="gradientId" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" [attr.stop-color]="s.from" />
          <stop offset="1" [attr.stop-color]="s.to" />
        </linearGradient>
        <linearGradient [attr.id]="scrimId" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0.35" stop-color="#000" stop-opacity="0" />
          <stop offset="1" stop-color="#000" stop-opacity="0.5" />
        </linearGradient>
      </defs>
      <rect [attr.width]="width" [attr.height]="height" [attr.fill]="'url(#' + gradientId + ')'" />
      @for (shape of shapes(); track $index) {
        @if (shape.kind === 'path') {
          <path [attr.d]="shape.d" fill="none" [attr.stroke]="shape.accent ? s.accent : '#fff'" [attr.stroke-width]="shape.width"
            [attr.opacity]="shape.opacity" stroke-linecap="round" />
        } @else {
          <circle [attr.cx]="shape.cx" [attr.cy]="shape.cy" [attr.r]="shape.r" [attr.opacity]="shape.opacity"
            [attr.fill]="shape.fill ? (shape.accent ? s.accent : '#fff') : 'none'"
            [attr.stroke]="shape.fill ? 'none' : shape.accent ? s.accent : '#fff'" stroke-width="2" />
        }
      }
      <!-- Darkens the bottom so the name always reads, whatever the motif behind it. -->
      <rect [attr.width]="width" [attr.height]="height" [attr.fill]="'url(#' + scrimId + ')'" />
      @let t = text();
      @let layout = textLayout();
      <text x="22" [attr.y]="layout.titleY" class="title" [attr.font-size]="layout.titleSize" [style.font-family]="titleFont().family"
        [attr.font-weight]="titleFont().weight">{{ t.title }}</text>
      @if (t.subtitle) {
        <text x="23" [attr.y]="layout.subtitleY" class="subtitle">{{ t.subtitle }}</text>
      }
    </svg>
  `,
  styles: `
    :host { display: block; aspect-ratio: 400 / 150; overflow: hidden; }
    svg { display: block; width: 100%; height: 100%; }
    .title { fill: #fff; }
    .subtitle { font: 600 15px/1 var(--font-body); letter-spacing: 0.14em; text-transform: uppercase; fill: #fff; opacity: 0.85; }
  `,
})
export class GameCover {
  readonly cover = input<CoverStyle | undefined>();
  readonly text = input.required<CoverText>();

  protected readonly width = COVER_WIDTH;
  protected readonly height = COVER_HEIGHT;
  protected readonly viewBox = `0 0 ${COVER_WIDTH} ${COVER_HEIGHT}`;
  private readonly uid = nextId++;
  protected readonly gradientId = `cover-gradient-${this.uid}`;
  protected readonly scrimId = `cover-scrim-${this.uid}`;
  protected readonly textLayout = computed(() => coverTextLayout(this.text(), this.style().font));
  protected readonly titleFont = computed(() => {
    const font = COVER_FONTS[this.style().font ?? 'default'];
    return { family: `'${font.family}', var(--font-display)`, weight: font.weight };
  });
  protected readonly style = computed(() => this.cover() ?? DEFAULT_COVER);
  protected readonly shapes = computed(() => coverShapes(this.style().motif));
}
