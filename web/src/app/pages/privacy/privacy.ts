import { ChangeDetectionStrategy, Component } from '@angular/core';
import { TranslocoPipe } from '@jsverse/transloco';

import { SITE } from '../../site.config';

/** Mirrors PRIVACY.md in the repository. */
@Component({
  selector: 'app-privacy',
  imports: [TranslocoPipe],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <h1>{{ 'privacy.title' | transloco }}</h1>
    <ul class="stack-sm">
      <li>{{ 'privacy.progress' | transloco }}</li>
      <li>{{ 'privacy.analytics' | transloco }}</li>
      <li>{{ 'privacy.suggestions' | transloco }}</li>
    </ul>
    @if (contactEmail) {
      <p>{{ 'privacy.contact' | transloco }} <a [href]="'mailto:' + contactEmail">{{ contactEmail }}</a></p>
    }
  `,
  styles: `ul { padding-left: 1.25rem; }`,
})
export class Privacy {
  protected readonly contactEmail = SITE.contactEmail;
}
