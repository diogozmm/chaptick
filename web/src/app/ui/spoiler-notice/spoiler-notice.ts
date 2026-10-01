import { ChangeDetectionStrategy, Component, inject, input, signal } from '@angular/core';
import { TranslocoPipe } from '@jsverse/transloco';

import { SpoilerLevel } from '../../core/content/content.models';
import { RevealService } from '../../core/spoiler/reveal.service';
import { needsConfirmation } from '../../core/spoiler/spoiler';
import { Icon } from '../icon/icon';

/**
 * One notice for everything a detail page keeps hidden, with a single reveal button. Level 2
 * asks for confirmation first, like the inline reveal in the checklist.
 */
@Component({
  selector: 'app-spoiler-notice',
  imports: [TranslocoPipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <app-icon name="eye-off" />
    <div class="body">
      <p>{{ message() }}</p>
      @if (confirming()) {
        <p class="confirm">{{ 'spoiler.confirm' | transloco }}</p>
        <div class="actions">
          <button type="button" class="button primary" (click)="reveal.reveal(itemId())">{{ 'spoiler.show' | transloco }}</button>
          <button type="button" class="button" (click)="confirming.set(false)">{{ 'common.cancel' | transloco }}</button>
        </div>
      } @else {
        <button type="button" class="button" (click)="tap()">{{ 'spoiler.reveal' | transloco }}</button>
      }
    </div>
  `,
  styles: `
    :host {
      display: flex; gap: 0.75rem; align-items: flex-start; padding: 1rem; border-radius: var(--radius);
      border: 1px dashed var(--border-strong); background: var(--surface);
    }
    :host > app-icon { flex: none; width: 1.35rem; height: 1.35rem; margin-top: 0.1rem; color: var(--text-muted); }
    .body { display: grid; gap: 0.6rem; justify-items: start; }
    p { margin: 0; }
    .confirm { font-weight: 600; }
    .actions { display: flex; flex-wrap: wrap; gap: 0.5rem; }
  `,
})
export class SpoilerNotice {
  protected readonly reveal = inject(RevealService);

  readonly itemId = input.required<string>();
  readonly level = input.required<SpoilerLevel>();
  readonly message = input.required<string>();

  protected readonly confirming = signal(false);

  protected tap(): void {
    if (needsConfirmation(this.level())) this.confirming.set(true);
    else this.reveal.reveal(this.itemId());
  }
}
