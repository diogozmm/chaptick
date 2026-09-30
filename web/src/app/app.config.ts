import { provideHttpClient, withFetch } from '@angular/common/http';
import { ApplicationConfig, inject, isDevMode, provideAppInitializer, provideBrowserGlobalErrorListeners } from '@angular/core';
import { provideRouter, withComponentInputBinding, withInMemoryScrolling } from '@angular/router';
import { provideServiceWorker } from '@angular/service-worker';
import { provideTransloco } from '@jsverse/transloco';

import { routes } from './app.routes';
import { AnalyticsService } from './core/analytics.service';
import { ContentService } from './core/content/content.service';
import { LangService } from './core/i18n/lang.service';
import { TranslocoHttpLoader } from './core/i18n/transloco-http-loader';
import { ProgressStore } from './core/progress/progress.store';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideHttpClient(withFetch()),
    provideRouter(
      routes,
      withComponentInputBinding(),
      withInMemoryScrolling({ anchorScrolling: 'enabled', scrollPositionRestoration: 'enabled' }),
    ),
    // Offline-first: the app shell is prefetched, chapters are cached as they unlock.
    provideServiceWorker('ngsw-worker.js', {
      enabled: !isDevMode(),
      registrationStrategy: 'registerWhenStable:30000',
    }),
    provideTransloco({
      config: {
        availableLangs: ['en', 'pt'],
        defaultLang: 'en',
        fallbackLang: 'en',
        reRenderOnLangChange: true,
        prodMode: !isDevMode(),
      },
      loader: TranslocoHttpLoader,
    }),
    // Guards need the manifest and the current chapter before the first navigation.
    provideAppInitializer(async () => {
      const content = inject(ContentService);
      const progress = inject(ProgressStore);
      const lang = inject(LangService);
      inject(AnalyticsService).init();
      const [manifest] = await Promise.all([content.loadManifest(), lang.init()]);
      await progress.load(manifest.chapters[0]?.id ?? '');
    }),
  ],
};
