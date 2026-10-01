import { ChangeDetectionStrategy, Component, input } from '@angular/core';
import { RouterLink } from '@angular/router';

import { Icon } from '../icon/icon';

/**
 * Bottom bar of a detail page: previous and next entry around a main action. Sticky rather than
 * fixed, so it rests above the footer instead of covering it at the end of the page.
 */
@Component({
  selector: 'app-detail-bar',
  imports: [RouterLink, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="bar">
      @if (prev(); as link) {
        <a class="arrow" [routerLink]="link" [attr.aria-label]="prevLabel()"><app-icon name="chevron-left" /></a>
      } @else {
        <span class="arrow off" aria-hidden="true"><app-icon name="chevron-left" /></span>
      }
      <div class="main"><ng-content /></div>
      @if (next(); as link) {
        <a class="arrow" [routerLink]="link" [attr.aria-label]="nextLabel()"><app-icon name="chevron-right" /></a>
      } @else {
        <span class="arrow off" aria-hidden="true"><app-icon name="chevron-right" /></span>
      }
    </div>
  `,
  styles: `
    :host {
      position: sticky; bottom: 0; z-index: 5; margin: 0 -1rem; padding: 0.75rem 1rem calc(0.75rem + env(safe-area-inset-bottom));
      background: linear-gradient(transparent, var(--bg) 35%);
    }
    .bar {
      display: flex; align-items: center; gap: 0.5rem; padding: 0.4rem; border-radius: calc(var(--radius) + 0.4rem);
      background: var(--surface); border: 1px solid var(--border); box-shadow: 0 8px 24px rgb(0 0 0 / 0.12);
    }
    .main { flex: 1; min-width: 0; display: grid; }
    .arrow {
      flex: none; display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: var(--radius);
      color: var(--text); background: var(--surface-2); text-decoration: none;
    }
    .arrow:hover { color: var(--accent); }
    .arrow:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
    .arrow.off { color: var(--text-muted); opacity: 0.35; }
    .arrow app-icon { width: 1.25rem; height: 1.25rem; }
  `,
})
export class DetailBar {
  readonly prev = input<unknown[] | null>(null);
  readonly next = input<unknown[] | null>(null);
  readonly prevLabel = input.required<string>();
  readonly nextLabel = input.required<string>();
}
