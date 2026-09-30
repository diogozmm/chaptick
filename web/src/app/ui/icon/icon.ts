import { ChangeDetectionStrategy, Component, computed, inject, input } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';

import { ICONS, IconName } from './icons';

/** Decorative by default (aria-hidden): pair it with visible text or an aria-label on the control. */
@Component({
  selector: 'app-icon',
  changeDetection: ChangeDetectionStrategy.OnPush,
  host: { 'aria-hidden': 'true', '[innerHTML]': 'svg()' },
  template: '',
  styles: `
    :host { display: inline-flex; flex: none; width: 1.25em; height: 1.25em; }
    :host ::ng-deep svg { width: 100%; height: 100%; }
  `,
})
export class Icon {
  private readonly sanitizer = inject(DomSanitizer);

  readonly name = input.required<IconName>();
  readonly strokeWidth = input(2);

  // The markup is a compile-time constant from icons.ts, never user input, so bypassing is safe.
  protected readonly svg = computed(() =>
    this.sanitizer.bypassSecurityTrustHtml(
      `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" ` +
        `stroke-width="${this.strokeWidth()}" stroke-linecap="round" stroke-linejoin="round">${ICONS[this.name()]}</svg>`,
    ),
  );
}
