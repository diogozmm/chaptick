import { ChangeDetectionStrategy, Component, computed, inject, input, signal } from '@angular/core';
import { TranslocoPipe } from '@jsverse/transloco';

import { SpoilerLevel } from '../../core/content/content.models';
import { RevealService } from '../../core/spoiler/reveal.service';
import { isMasked, needsConfirmation } from '../../core/spoiler/spoiler';

/**
 * Shows its content directly for spoiler level 0. Level 1 shows `placeholder` until tapped;
 * level 2 also asks for confirmation. Revealing is shared by every view of the same item.
 */
@Component({
  selector: 'app-spoiler-reveal',
  imports: [TranslocoPipe],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    @if (visible()) {
      <ng-content />
    } @else if (confirming()) {
      <span class="confirm" role="group" [attr.aria-label]="'spoiler.confirm' | transloco">
        <span>{{ 'spoiler.confirm' | transloco }}</span>
        <button type="button" class="link" (click)="reveal.reveal(itemId())">{{ 'spoiler.show' | transloco }}</button>
        <button type="button" class="link" (click)="confirming.set(false)">{{ 'common.cancel' | transloco }}</button>
      </span>
    } @else {
      <button type="button" class="masked" (click)="tap()">
        <span class="label">{{ placeholder() }}</span>
        <span class="cue">{{ 'spoiler.tapToReveal' | transloco }}</span>
      </button>
    }
  `,
  styles: `
    .masked {
      all: unset; cursor: pointer; display: inline-flex; flex-wrap: wrap; align-items: center; gap: 0.25rem 0.5rem;
      font: inherit; color: var(--text);
    }
    .masked:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 4px; }
    .label { text-decoration: underline dashed var(--text-muted); text-underline-offset: 4px; }
    .cue {
      font: 600 0.6875rem/1 var(--font-body); letter-spacing: 0.06em; text-transform: uppercase;
      padding: 0.3rem 0.5rem; border-radius: 999px; color: var(--accent); background: var(--accent-soft);
    }
    .confirm { display: inline-flex; flex-wrap: wrap; gap: 0 0.75rem; align-items: center; font-size: 0.9375rem; font-weight: 500; }
  `,
})
export class SpoilerReveal {
  protected readonly reveal = inject(RevealService);

  readonly itemId = input.required<string>();
  readonly level = input.required<SpoilerLevel>();
  readonly placeholder = input.required<string>();

  protected readonly confirming = signal(false);
  protected readonly visible = computed(() => !isMasked(this.level()) || this.reveal.isRevealed(this.itemId()));

  protected tap(): void {
    if (needsConfirmation(this.level())) this.confirming.set(true);
    else this.reveal.reveal(this.itemId());
  }
}
