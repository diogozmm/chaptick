import { ChangeDetectionStrategy, Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { ActiveGame } from '../../core/game/active-game';
import { Icon } from '../icon/icon';

const STORAGE_KEY = 'chaptick.howItWorks';

/**
 * The few rules worth knowing before the first checklist, shown until dismissed. Remembered per
 * browser only: if storage is unavailable the card simply shows again, which is harmless.
 */
@Component({
  selector: 'app-how-it-works',
  imports: [RouterLink, TranslocoPipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './how-it-works.html',
  styleUrl: './how-it-works.scss',
})
export class HowItWorks {
  protected readonly game = inject(ActiveGame);
  protected readonly open = signal(!readSeen());

  protected dismiss(): void {
    this.open.set(false);
    try {
      localStorage.setItem(STORAGE_KEY, '1');
    } catch {
      // Private mode or blocked storage: it just shows again next time.
    }
  }
}

function readSeen(): boolean {
  try {
    return localStorage.getItem(STORAGE_KEY) === '1';
  } catch {
    return false;
  }
}
