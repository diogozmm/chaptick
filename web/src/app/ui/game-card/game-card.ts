import { ChangeDetectionStrategy, Component, computed, inject, input } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { CatalogGame } from '../../core/content/content.models';
import { SavedGames } from '../../core/game/saved-games';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { GameCover } from '../game-cover/game-cover';
import { Icon } from '../icon/icon';

/** A game in the library: cover, what it offers, size, and Start or Continue. */
@Component({
  selector: 'app-game-card',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, GameCover, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    @let g = game();
    @let gc = saved.cover(g.id);
    <a class="card game" [routerLink]="saved.link(g.id)">
      <app-game-cover class="cover" [cover]="gc.style" [text]="gc.text" />
      <span class="game-body">
        <span class="visually-hidden">{{ g.name | localize: lang.lang() }}</span>
        <span class="features">
          @for (t of saved.features(g.id); track t) {
            <span class="feature" [attr.data-feature]="t">{{ 'feature.' + t | transloco }}</span>
          }
        </span>
        <span class="muted small">{{ saved.k('home.counts', g.id) | transloco: { chapters: g.chapterCount, items: g.itemCount } }}</span>
        @if (started()) {
          <span class="badge">{{ 'home.inProgress' | transloco: { count: saved.doneCount(g.id) } }}</span>
        }
      </span>
      <span class="game-action">
        {{ (started() ? 'home.resume' : 'home.start') | transloco }}
        <app-icon name="chevron-right" />
      </span>
    </a>
  `,
  styles: `
    :host { display: grid; }
    .small { font-size: 0.8125rem; }
    .cover { margin: 0 -1.125rem; }
    .game {
      display: flex; flex-direction: column; gap: 0.5rem; padding: 0 1.125rem 0.9rem; overflow: hidden;
      text-decoration: none; color: var(--text); transition: border-color 0.2s, transform 0.2s var(--ease);
    }
    .game:hover { transform: translateY(-2px); border-color: var(--accent); }
    .game-body { flex: 1; display: grid; gap: 0.3rem; align-content: start; }
    .badge { justify-self: start; }
    .game-action { display: inline-flex; align-items: center; gap: 0.25rem; color: var(--accent); font-weight: 600; white-space: nowrap; }
    .features { display: flex; flex-wrap: wrap; gap: 0.3rem; }
    .feature {
      padding: 0.1rem 0.45rem; border-radius: 0.35rem; background: var(--surface-2); color: var(--text-muted);
      font: 600 0.68rem/1.5 var(--font-body); letter-spacing: 0.04em; text-transform: uppercase;
    }
    .feature[data-feature='compendium'] { background: var(--accent-soft); color: var(--text); }
  `,
})
export class GameCard {
  protected readonly saved = inject(SavedGames);
  protected readonly lang = inject(LangService);
  readonly game = input.required<CatalogGame>();
  protected readonly started = computed(() => this.saved.started(this.game().id));
}
