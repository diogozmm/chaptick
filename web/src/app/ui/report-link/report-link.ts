import { ChangeDetectionStrategy, Component, computed, inject, input } from '@angular/core';
import { TranslocoPipe } from '@jsverse/transloco';

import { ActiveGame } from '../../core/game/active-game';
import { SITE } from '../../site.config';
import { Icon } from '../icon/icon';

/**
 * "Report a mistake": a GitHub issue form or an e-mail, prefilled with the entry's id and the
 * game's data version. Only the id travels, never a name, so the report itself spoils nothing.
 * Hidden when neither a repository nor a contact e-mail is configured.
 */
@Component({
  selector: 'app-report-link',
  imports: [TranslocoPipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    @if (issueUrl() || mailUrl()) {
      <p class="report">
        <app-icon name="flag" />
        <span>
          {{ 'report.question' | transloco }}
          @if (issueUrl(); as url) {
            <a [href]="url" target="_blank" rel="noopener">{{ 'report.github' | transloco }}</a>
          }
          @if (issueUrl() && mailUrl()) {
            {{ 'report.or' | transloco }}
          }
          @if (mailUrl(); as url) {
            <a [href]="url">{{ 'report.email' | transloco }}</a>
          }
        </span>
      </p>
    }
  `,
  styles: `
    .report { display: flex; gap: 0.4rem; align-items: flex-start; margin: 0; font-size: 0.8125rem; color: var(--text-muted); }
    .report app-icon { flex: none; width: 0.9rem; height: 0.9rem; margin-top: 0.15rem; }
    a { color: var(--accent); }
  `,
})
export class ReportLink {
  private readonly active = inject(ActiveGame);

  /** Item or boss id, e.g. sc-ch3-hq-02. */
  readonly entryId = input.required<string>();

  private readonly version = computed(() => {
    const game = this.active.manifest()?.game;
    return game ? `${game.id} data v${game.dataVersion}` : '';
  });

  protected readonly issueUrl = computed(() => {
    if (!SITE.repoUrl) return '';
    const params = new URLSearchParams({
      template: 'item-correction.yml',
      title: `fix ${this.entryId()}`,
      item: this.entryId(),
      version: this.version(),
    });
    return `${SITE.repoUrl}/issues/new?${params}`;
  });

  protected readonly mailUrl = computed(() => {
    if (!SITE.contactEmail) return '';
    const subject = encodeURIComponent(`Chaptick: fix ${this.entryId()}`);
    const body = encodeURIComponent(`Item: ${this.entryId()}\nData: ${this.version()}\n\nWhat is wrong:\n\nSource:\n`);
    return `mailto:${SITE.contactEmail}?subject=${subject}&body=${body}`;
  });
}
