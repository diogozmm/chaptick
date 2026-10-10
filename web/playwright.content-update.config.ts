import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  testMatch: 'content-update.update.ts',
  workers: 1,
  timeout: 60_000,
  retries: 0,
  use: {
    ...devices['Pixel 7'],
    baseURL: 'http://127.0.0.1:4311',
    locale: 'en-US',
    serviceWorkers: 'allow',
    trace: 'retain-on-failure',
  },
  webServer: {
    command: 'node e2e/prepare-content-update.mjs && npx ng build && CONTENT_UPDATE_TEST=1 PORT=4311 node e2e/serve.mjs',
    url: 'http://127.0.0.1:4311',
    reuseExistingServer: false,
    timeout: 180_000,
  },
});
