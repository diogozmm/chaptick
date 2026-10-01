import { ChangeDetectionStrategy, Component, computed, inject, input, linkedSignal } from '@angular/core';
import { TranslocoPipe } from '@jsverse/transloco';

import { Item } from '../../core/content/content.models';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { routeProgress, stepChange, stepKey } from '../../core/route/route';
import { Icon } from '../icon/icon';

/** A route through an area: each stop has its own checkbox, and the last one completes the item. */
@Component({
  selector: 'app-route-steps',
  imports: [TranslocoPipe, LocalizePipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    @let p = progress();
    <button type="button" class="toggle" [attr.aria-expanded]="open()" [attr.aria-controls]="listId()" (click)="open.set(!open())">
      <app-icon name="map-pin" />
      {{ 'route.title' | transloco }} · {{ p.done }}/{{ p.total }}
      <app-icon class="chevron" [class.up]="open()" name="chevron-right" />
    </button>
    @if (open()) {
      <ol class="steps" [id]="listId()">
        @for (step of item().steps; track $index) {
          @let key = stepKey(item().id, $index);
          <li [class.done]="store.done().has(key)">
            <label>
              <input type="checkbox" class="checkbox" [checked]="store.done().has(key)" (change)="toggle($index)" />
              <span>{{ step.text | localize: lang.lang() }}</span>
            </label>
          </li>
        }
      </ol>
    }
  `,
  styles: `
    :host { display: grid; gap: 0.4rem; }
    .toggle {
      justify-self: start; display: inline-flex; align-items: center; gap: 0.35rem; min-height: 2.5rem; padding: 0 0.75rem;
      border-radius: 999px; border: 1px solid var(--border); background: var(--surface-2); color: var(--text);
      font: 600 0.8125rem/1 var(--font-body); cursor: pointer;
    }
    .toggle app-icon { width: 0.95rem; height: 0.95rem; }
    .chevron { transition: transform 0.2s; }
    .chevron.up { transform: rotate(90deg); }
    .steps { list-style: none; margin: 0; padding: 0; display: grid; gap: 0.15rem; counter-reset: step; }
    .steps label { display: flex; align-items: flex-start; gap: 0.6rem; min-height: 2.75rem; padding: 0.35rem 0; cursor: pointer; font-size: 0.9rem; line-height: 1.45; }
    .steps .checkbox { width: 1.35rem; height: 1.35rem; margin-top: 0.05rem; }
    .steps li.done span { color: var(--text-muted); text-decoration: line-through; }
  `,
})
export class RouteSteps {
  protected readonly store = inject(ProgressStore);
  protected readonly lang = inject(LangService);
  protected readonly stepKey = stepKey;

  readonly item = input.required<Item>();
  /** Start expanded (detail page) or collapsed (checklist row). */
  readonly expanded = input(false);

  protected readonly open = linkedSignal(() => this.expanded());
  protected readonly progress = computed(() => routeProgress(this.item(), this.store.done()));
  protected readonly listId = computed(() => `route-${this.item().id}`);

  protected toggle(index: number): void {
    const change = stepChange(this.item(), index, this.store.done());
    void this.store.setDone(change.ids, change.done);
  }
}
