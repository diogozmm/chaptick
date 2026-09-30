import { ChangeDetectionStrategy, Component } from '@angular/core';
import { TranslocoPipe } from '@jsverse/transloco';

import { SITE } from '../../site.config';

@Component({
  selector: 'app-credits',
  imports: [TranslocoPipe],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <h1>{{ 'credits.title' | transloco }}</h1>

    <section>
      <h2>{{ 'credits.sources' | transloco }}</h2>
      <p class="muted">{{ 'credits.sourcesIntro' | transloco }}</p>
      <ul>
        @for (source of site.sources; track source.url) {
          <li><a [href]="source.url" rel="noopener" target="_blank">{{ source.name }}</a> — {{ source.authors }}</li>
        }
      </ul>
    </section>

    @if (site.contributors.length > 0) {
      <section>
        <h2>{{ 'credits.contributors' | transloco }}</h2>
        <p>{{ site.contributors.join(', ') }}</p>
      </section>
    }

    <section id="support">
      <h2>{{ 'credits.support' | transloco }}</h2>
      <p>{{ 'credits.supportIntro' | transloco }}</p>
      @if (site.donations.length > 0) {
        <ul class="donations">
          @for (link of site.donations; track link.url) {
            <li><a class="button" [href]="link.url" rel="noopener" target="_blank">{{ link.label }}</a></li>
          }
        </ul>
      }
      @if (site.supporters.length > 0) {
        <p class="muted">{{ 'credits.thanks' | transloco }} {{ site.supporters.join(', ') }}</p>
      }
    </section>

    <section>
      <h2>{{ 'credits.licenses' | transloco }}</h2>
      <p>{{ 'credits.licensesText' | transloco }}</p>
      @if (site.repoUrl) {
        <p><a [href]="site.repoUrl" rel="noopener" target="_blank">{{ 'credits.repo' | transloco }}</a></p>
      }
    </section>
  `,
  styles: `
    h2 { font-size: 1.1rem; margin: 1.5rem 0 0.5rem; }
    ul { padding-left: 1.25rem; }
    .donations { list-style: none; padding: 0; display: flex; flex-wrap: wrap; gap: 0.5rem; }
  `,
})
export class Credits {
  protected readonly site = SITE;
}
