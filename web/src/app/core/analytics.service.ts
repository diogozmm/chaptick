import { Injectable } from '@angular/core';

import { SITE } from '../site.config';

type AnalyticsEvent = 'item_toggled' | 'chapter_advanced' | 'progress_exported' | 'progress_link_created' | 'progress_moved';

interface Umami {
  track(event: string, data?: Record<string, string | number>): void;
}

/**
 * Cookieless, aggregate analytics (Umami), so no consent banner is needed. Never send item ids
 * or anything that identifies a person. A no-op until `SITE.analytics` is configured.
 */
@Injectable({ providedIn: 'root' })
export class AnalyticsService {
  init(): void {
    const config = SITE.analytics;
    if (!config || !config.hosts.includes(location.hostname)) return;
    const script = document.createElement('script');
    script.defer = true;
    script.src = config.scriptUrl;
    script.dataset['websiteId'] = config.websiteId;
    script.dataset['doNotTrack'] = 'true';
    // Umami's own guard too: never count a visit on any other host.
    script.dataset['domains'] = config.hosts.join(',');
    document.head.appendChild(script);
  }

  track(event: AnalyticsEvent, data?: Record<string, string | number>): void {
    (window as { umami?: Umami }).umami?.track(event, data);
  }
}
