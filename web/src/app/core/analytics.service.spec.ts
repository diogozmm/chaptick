import { TestBed } from '@angular/core/testing';

import { SITE } from '../site.config';
import { AnalyticsService } from './analytics.service';

describe('AnalyticsService', () => {
  const original = SITE.analytics;
  const script = () => document.head.querySelector('script[data-website-id]');
  afterEach(() => {
    SITE.analytics = original;
    script()?.remove();
  });

  it('never loads off the production host (local development, tests)', () => {
    TestBed.inject(AnalyticsService).init();
    expect(script()).toBeNull();
  });

  it('loads cookieless Umami on its host, honouring Do Not Track', () => {
    SITE.analytics = { ...original!, hosts: [location.hostname] };
    TestBed.inject(AnalyticsService).init();
    const tag = script() as HTMLScriptElement;
    expect(tag.src).toBe('https://cloud.umami.is/script.js');
    expect(tag.dataset['doNotTrack']).toBe('true');
    expect(tag.dataset['domains']).toBe(location.hostname);
  });
});
