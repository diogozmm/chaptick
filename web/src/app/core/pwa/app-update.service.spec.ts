import { TestBed } from '@angular/core/testing';
import { NavigationStart, Router } from '@angular/router';
import { SwUpdate, VersionEvent } from '@angular/service-worker';
import { Subject } from 'rxjs';

import { AppUpdateService } from './app-update.service';

describe('AppUpdateService', () => {
  const versionUpdates = new Subject<VersionEvent>();
  const routerEvents = new Subject<unknown>();
  const checkForUpdate = vi.fn().mockResolvedValue(false);
  let service: AppUpdateService;
  let load: ReturnType<typeof vi.fn>;

  beforeEach(() => {
    checkForUpdate.mockClear();
    TestBed.configureTestingModule({
      providers: [
        { provide: SwUpdate, useValue: { isEnabled: true, versionUpdates, unrecoverable: new Subject(), checkForUpdate } },
        { provide: Router, useValue: { events: routerEvents } },
      ],
    });
    service = TestBed.inject(AppUpdateService);
    load = vi.fn();
    (service as unknown as { load: typeof load }).load = load;
  });

  const ready = () =>
    versionUpdates.next({ type: 'VERSION_READY', currentVersion: { hash: 'a' }, latestVersion: { hash: 'b' } });

  it('keeps navigating in the app until a new version is ready', () => {
    routerEvents.next(new NavigationStart(1, '/sc/chapters'));
    expect(load).not.toHaveBeenCalled();

    ready();
    expect(service.updateReady()).toBe(true);
    routerEvents.next(new NavigationStart(2, '/sc/chapters/sc-ch1'));
    expect(load).toHaveBeenCalledWith('/sc/chapters/sc-ch1', false);
  });

  it('replaces the history entry on back/forward', () => {
    ready();
    routerEvents.next(new NavigationStart(3, '/sc/chapters', 'popstate'));
    expect(load).toHaveBeenCalledWith('/sc/chapters', true);
  });

  it('looks for a new version when the app comes back to the foreground', () => {
    document.dispatchEvent(new Event('visibilitychange'));
    expect(checkForUpdate).toHaveBeenCalledTimes(1);
  });
});
