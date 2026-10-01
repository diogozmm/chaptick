import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { LangService } from './core/i18n/lang.service';
import { ActiveGame } from './core/game/active-game';
import { AppUpdateService } from './core/pwa/app-update.service';
import { TransferService } from './core/progress/transfer.service';
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
  protected readonly game = inject(ActiveGame);
  protected readonly transfer = inject(TransferService);
  protected readonly movedHost = this.transfer.movedTo ? new URL(this.transfer.movedTo).host : '';

  protected toggleLang(): void {
    void this.lang.use(this.lang.lang() === 'pt' ? 'en' : 'pt');
  }
}
