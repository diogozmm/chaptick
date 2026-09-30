import { expect, test } from '@playwright/test';

test.use({ serviceWorkers: 'allow' });

test('works offline after the first visit', async ({ page, context }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await page.evaluate(async () => {
    await navigator.serviceWorker.ready;
  });
  // The first load happened before the worker took control; this one goes through it and fills the cache.
  await page.reload();
  await expect.poll(() => page.evaluate(() => Boolean(navigator.serviceWorker.controller))).toBe(true);
  await expect(page.getByText('Safe Quest')).toBeVisible();

  await context.setOffline(true);
  await page.reload();
  await expect(page.getByRole('heading', { level: 1, name: 'Prologue' })).toBeVisible();
  await expect(page.getByText('Safe Quest')).toBeVisible();
  await page.getByRole('link', { name: /Where am I/ }).click();
  await expect(page.getByText('Chapter 1 — locked')).toBeVisible();
});

test('locked chapters never land in the offline cache', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await page.evaluate(async () => {
    await navigator.serviceWorker.ready;
  });
  await page.reload();
  await expect(page.getByText('Safe Quest')).toBeVisible();

  const cached = await page.evaluate(async () => {
    const urls: string[] = [];
    for (const name of await caches.keys()) {
      for (const req of await (await caches.open(name)).keys()) urls.push(new URL(req.url).pathname);
    }
    return urls;
  });
  expect(cached.some((url) => url.endsWith('ch-0.json'))).toBe(true);
  expect(cached.filter((url) => /ch-[12]\.json/.test(url))).toEqual([]);
});
