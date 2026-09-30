import { Injectable, inject, signal } from '@angular/core';
import { SwUpdate } from '@angular/service-worker';

/**
 * Tells the shell when a new app or content version is ready. Reloading is left to the player:
 * swapping versions mid-checklist would be jarring, and progress is already saved.
 */
@Injectable({ providedIn: 'root' })
export class AppUpdateService {
  private readonly updates = inject(SwUpdate);
  private readonly ready = signal(false);

  readonly updateReady = this.ready.asReadonly();

  constructor() {
    if (!this.updates.isEnabled) return;
    this.updates.versionUpdates.subscribe((event) => {
      if (event.type === 'VERSION_READY') this.ready.set(true);
    });
    // A broken cache can only be fixed by fetching everything again.
    this.updates.unrecoverable.subscribe(() => location.reload());
  }

  reload(): void {
    location.reload();
  }
}
