import { defineConfig, devices } from '@playwright/test';

const PORT = 4310;

export default defineConfig({
  testDir: './e2e',
  testMatch: '**/*.e2e.ts',
  fullyParallel: true,
  forbidOnly: Boolean(process.env['CI']),
  retries: process.env['CI'] ? 1 : 0,
  reporter: 'list',
  use: {
    baseURL: `http://127.0.0.1:${PORT}`,
    locale: 'en-US',
    trace: 'on-first-retry',
    serviceWorkers: 'block',
  },
  // Mobile first: the app is used on a phone next to the console.
  projects: [{ name: 'mobile', use: { ...devices['Pixel 7'] } }],
  webServer: {
    command:
      'node ../scripts/build-content.mjs --root e2e/fixtures/content --out e2e/.content && npx ng build && node e2e/serve.mjs',
    url: `http://127.0.0.1:${PORT}`,
    reuseExistingServer: !process.env['CI'],
    timeout: 180_000,
  },
});
