import { ChangeDetectionStrategy, Component, inject, input } from '@angular/core';
import { TranslocoPipe } from '@jsverse/transloco';
import { ItemGuidance as Guidance } from '../../core/content/content.models';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';

/** Parent applies spoiler visibility. These sections are informational, never progress controls. */
@Component({
  selector: 'app-item-guidance',
  imports: [TranslocoPipe, LocalizePipe],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    @let g = guidance();
    @let l = lang.lang();
    @if (position() === 'before' && g.overview) {
      <section class="card">
        <h2>{{ 'item.instructions' | transloco }}</h2>
        <p>{{ g.overview | localize: l }}</p>
      </section>
    }
    @for (key of position() === 'before' ? before : after; track key) {
      @if (g[key]; as lines) {
        <section class="card" [class.warning]="key === 'warnings'">
          <h2>{{ 'guidance.' + key | transloco }}</h2>
          <ul>
            @for (line of lines; track $index) { <li>{{ line | localize: l }}</li> }
          </ul>
        </section>
      }
    }
    @if (position() === 'after' && g.alternatives) {
      <section class="card alternatives">
        <h2>{{ 'guidance.alternatives' | transloco }}</h2>
        @for (branch of g.alternatives; track $index) {
          <section class="branch">
            <h3>{{ branch.condition | localize: l }}</h3>
            <ul>
              @for (line of branch.instructions; track $index) { <li>{{ line | localize: l }}</li> }
            </ul>
          </section>
        }
      </section>
    }
  `,
  styles: `
    :host { display: grid; gap: 1rem; }
    :host:empty { display: none; }
    .card { display: grid; gap: 0.75rem; }
    h2 { font-size: 1.2rem; }
    h3 { margin: 0; font: 600 1rem/1.5 var(--font-body); }
    p, ul { margin: 0; line-height: 1.75; white-space: pre-line; overflow-wrap: anywhere; }
    ul { padding-inline-start: 1.25rem; display: grid; gap: 0.5rem; }
    .warning { border-inline-start: 3px solid var(--warn-text); }
    .warning h2 { color: var(--warn-text); }
    .branch { display: grid; gap: 0.5rem; }
    .branch + .branch { padding-top: 0.75rem; border-top: 1px solid var(--border); }
  `,
})
export class ItemGuidance {
  protected readonly lang = inject(LangService);
  protected readonly before = ['warnings', 'requirements', 'preparation'] as const;
  protected readonly after = ['optional', 'rewards'] as const;
  readonly guidance = input.required<Guidance>();
  readonly position = input<'before' | 'after'>('before');
}
