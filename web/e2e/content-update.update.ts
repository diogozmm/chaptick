import { expect, test } from '@playwright/test';
import { expectSaved } from './helpers';

test('a content-only deployment refreshes cached instructions and keeps progress offline', async ({ page, context, request }) => {
  await page.goto('/sc/items/sc-ch0-co-01');
  await page.evaluate(async () => { await navigator.serviceWorker.ready; });
  await page.reload();
  await expect.poll(() => page.evaluate(() => Boolean(navigator.serviceWorker.controller))).toBe(true);
  const firstStep = page.getByRole('checkbox', { name: 'Left shelf', exact: true });
  await expect(firstStep).toBeVisible();
  await firstStep.check();
  await expectSaved(page, 'sc-ch0-co-01#step-1');

  // A real offline reload proves the old chapter is in the Angular worker cache.
  await context.setOffline(true);
  await page.reload();
  await expect(firstStep).toBeChecked();
  await expect(page.getByRole('checkbox', { name: 'Right shelf', exact: true })).not.toBeChecked();
  await context.setOffline(false);

  const previous = await (await request.get('/content/sc/manifest.json')).json();
  expect((await request.post('/__test/deploy-after')).ok()).toBe(true);
  const next = await (await request.get('/content/sc/manifest.json')).json();
  expect(next.game.dataVersion).not.toBe(previous.game.dataVersion);

  // Same app shell and service worker, new content only. No cache clearing or storage reset.
  await page.reload();
  await expect(page.getByText('Updated instructions from the new deployment.', { exact: true })).toBeVisible();
  await expect(page.getByText('New structured reward.', { exact: true })).toBeVisible();
  const updatedStep = page.getByRole('checkbox', { name: 'Updated left shelf instruction', exact: true });
  await expect(updatedStep).toBeChecked();
  await expect(page.getByRole('checkbox', { name: 'Right shelf', exact: true })).not.toBeChecked();
  await expectSaved(page, 'sc-ch0-co-01#step-1');

  const cachedUrls = await page.evaluate(async () => {
    const urls: string[] = [];
    for (const name of await caches.keys()) {
      for (const req of await (await caches.open(name)).keys()) urls.push(req.url);
    }
    return urls;
  });
  for (const version of [previous.game.dataVersion, next.game.dataVersion]) {
    expect(cachedUrls.some((url) => url.endsWith(`/content/sc/ch-0.json?v=${version}`))).toBe(true);
  }
  expect(cachedUrls.some((url) => /\/content\/sc\/ch-[12]\.json/.test(url))).toBe(false);

  await context.setOffline(true);
  await page.reload();
  await expect(updatedStep).toBeChecked();
  await expect(page.getByText('Updated instructions from the new deployment.', { exact: true })).toBeVisible();
  await expectSaved(page, 'sc-ch0-co-01#step-1');
});
