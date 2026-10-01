import { provideHttpClient, withFetch } from '@angular/common/http';
import { ApplicationConfig, inject, isDevMode, provideAppInitializer, provideBrowserGlobalErrorListeners } from '@angular/core';
import { provideRouter, withComponentInputBinding, withInMemoryScrolling, withRouterConfig } from '@angular/router';
import { provideServiceWorker } from '@angular/service-worker';
import { provideTransloco } from '@jsverse/transloco';

import { routes } from './app.routes';
import { AnalyticsService } from './core/analytics.service';
import { ContentService } from './core/content/content.service';
import { LangService } from './core/i18n/lang.service';
import { TranslocoHttpLoader } from './core/i18n/transloco-http-loader';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideHttpClient(withFetch()),
    provideRouter(
      routes,
      withComponentInputBinding(),
      withInMemoryScrolling({ anchorScrolling: 'enabled', scrollPositionRestoration: 'enabled' }),
      // Child pages also see the :gameId of their parent route.
      withRouterConfig({ paramsInheritanceStrategy: 'always' }),
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
    // The library needs the catalog before the first navigation; each game loads on demand.
    provideAppInitializer(async () => {
      inject(AnalyticsService).init();
      await Promise.all([inject(ContentService).loadCatalog(), inject(LangService).init()]);
    }),
  ],
};
