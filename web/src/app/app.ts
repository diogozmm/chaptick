import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { LangService } from './core/i18n/lang.service';
import { AppUpdateService } from './core/pwa/app-update.service';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, TranslocoPipe],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './app.html',
  styleUrl: './app.scss',
})
export class App {
  protected readonly lang = inject(LangService);
  protected readonly update = inject(AppUpdateService);

  protected toggleLang(): void {
    void this.lang.use(this.lang.lang() === 'pt' ? 'en' : 'pt');
  }
}
