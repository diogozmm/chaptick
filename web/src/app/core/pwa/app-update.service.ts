import { DestroyRef, Injectable, inject, signal } from '@angular/core';
import { NavigationStart, Router } from '@angular/router';
import { SwUpdate } from '@angular/service-worker';
import { filter } from 'rxjs';

/** How often a visible app looks for a new version. Only ngsw.json is fetched. */
const CHECK_EVERY_MS = 30 * 60 * 1000;

/**
 * Keeps players on the latest version. The service worker only looks for updates when the page
 * loads, and an installed app resumed from the background never reloads, so this also checks when
 * the app comes back to the foreground and every half hour.
 *
 * A ready update is applied at the next in-app navigation, as a normal page load of the screen the
 * player asked for: nothing is swapped mid-screen, and progress is already saved on every tap.
 * The banner still offers to reload right away.
 */
@Injectable({ providedIn: 'root' })
export class AppUpdateService {
  private readonly updates = inject(SwUpdate);
  private readonly router = inject(Router);
  private readonly ready = signal(false);

  readonly updateReady = this.ready.asReadonly();

  constructor() {
    if (!this.updates.isEnabled) return;
    this.updates.versionUpdates.subscribe((event) => {
      if (event.type === 'VERSION_READY') this.ready.set(true);
    });
    // A broken cache can only be fixed by fetching everything again.
    this.updates.unrecoverable.subscribe(() => location.reload());

    this.router.events.pipe(filter((e) => e instanceof NavigationStart)).subscribe((event) => {
      // Back/forward already moved the history: replace, so the next "back" still works.
      if (this.ready()) this.load(event.url, event.navigationTrigger === 'popstate');
    });

    const check = () => {
      if (document.visibilityState === 'visible') void this.updates.checkForUpdate().catch(() => undefined);
    };
    document.addEventListener('visibilitychange', check);
    const timer = setInterval(check, CHECK_EVERY_MS);
    inject(DestroyRef).onDestroy(() => {
      document.removeEventListener('visibilitychange', check);
      clearInterval(timer);
    });
  }

  reload(): void {
    location.reload();
  }

  /** A full page load of `url`, which picks up the new version. */
  protected load(url: string, replace: boolean): void {
    if (replace) location.replace(url);
    else location.assign(url);
  }
}
