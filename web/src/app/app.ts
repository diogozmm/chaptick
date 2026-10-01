import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { LangService } from './core/i18n/lang.service';
import { AppUpdateService } from './core/pwa/app-update.service';
import { Icon } from './ui/icon/icon';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive, TranslocoPipe, Icon],
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
