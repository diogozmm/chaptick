import { ChangeDetectionStrategy, Component, computed, inject, input, linkedSignal } from '@angular/core';
import { TranslocoPipe } from '@jsverse/transloco';

import { Item } from '../../core/content/content.models';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { routeProgress, stepChange, stepDone } from '../../core/route/route';
import { Icon } from '../icon/icon';

/** A route through an area: each stop has its own checkbox, and the last one completes the item. */
@Component({
  selector: 'app-route-steps',
  imports: [TranslocoPipe, LocalizePipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  host: { '[class.detailed]': '!collapsible()' },
  template: `
    @let p = progress();
    @if (collapsible()) {
      <button type="button" class="toggle" [attr.aria-expanded]="open()" [attr.aria-controls]="listId()" (click)="open.set(!open())">
        <app-icon name="map-pin" />
        {{ 'route.title' | transloco }} · {{ p.done }}/{{ p.total }}
        <app-icon class="chevron" [class.up]="open()" name="chevron-right" />
      </button>
    }
    @if (open() || !collapsible()) {
      <ol class="steps" [id]="listId()">
        @for (step of item().steps; track $index) {
          @let done = stepDone(item(), $index, store.done());
          <li [class.done]="done">
            <label>
              @if (!collapsible()) {
                <span class="step-number" aria-hidden="true">{{ $index + 1 }}</span>
              }
              <input type="checkbox" class="checkbox" [checked]="done" (change)="toggle($index)" />
              <span class="step-text">{{ step.text | localize: lang.lang() }}</span>
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
    .steps li.done .step-text { color: var(--text-muted); text-decoration: line-through; }
    :host(.detailed) .steps { gap: 0.75rem; }
    :host(.detailed) li { border: 1px solid var(--border); border-radius: var(--radius); background: var(--surface); }
    :host(.detailed) label {
      display: grid; grid-template-columns: 2rem minmax(0, 1fr) 1.35rem; gap: 0.75rem;
      padding: 1rem; font-size: 1rem; line-height: 1.65;
    }
    .step-number {
      display: grid; place-items: center; width: 2rem; height: 2rem; border-radius: 50%;
      background: var(--accent-soft); color: var(--accent); font: 600 0.8125rem/1 var(--font-body);
      font-variant-numeric: tabular-nums;
    }
    :host(.detailed) .step-text { grid-column: 2; grid-row: 1; overflow-wrap: anywhere; }
    :host(.detailed) .checkbox { grid-column: 3; grid-row: 1; margin-top: 0.3rem; }
    :host(.detailed) li:focus-within { outline: 2px solid var(--accent); outline-offset: 3px; }
    :host(.detailed) li.done { background: var(--surface-2); }
    :host(.detailed) li.done .step-text { text-decoration: none; }
    @media (hover: hover) { :host(.detailed) li:hover { border-color: var(--border-strong); } }
    @media (max-width: 380px) {
      :host(.detailed) label { grid-template-columns: 1.75rem minmax(0, 1fr) 1.35rem; padding: 0.875rem; gap: 0.5rem; }
      .step-number { width: 1.75rem; height: 1.75rem; }
    }
  `,
})
export class RouteSteps {
  protected readonly store = inject(ProgressStore);
  protected readonly lang = inject(LangService);
  protected readonly stepDone = stepDone;

  readonly item = input.required<Item>();
  /** Start expanded (detail page) or collapsed (checklist row). */
  readonly expanded = input(false);
  /** False on the detail page, where the route is the main content and always open. */
  readonly collapsible = input(true);

  protected readonly open = linkedSignal(() => this.expanded());
  protected readonly progress = computed(() => routeProgress(this.item(), this.store.done()));
  protected readonly listId = computed(() => `route-${this.item().id}`);

  protected toggle(index: number): void {
    const change = stepChange(this.item(), index, this.store.done());
    void this.store.setDone(change.ids, change.done, change.alsoDone);
  }
}
