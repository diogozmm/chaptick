import { expect, test } from '@playwright/test';

import { trackContent } from './helpers';

test('search finds route steps and keeps masked text out', async ({ page }) => {
  const fetched = trackContent(page);
  await page.goto('/sc/chapters/sc-ch0');
  await page.getByRole('link', { name: 'Search', exact: true }).click();
  const box = page.getByRole('searchbox', { name: 'Search the chapters you have reached' });

  await box.fill('shelf');
  const result = page.getByRole('link', { name: /Book One/ });
  await expect(result).toContainText('Route:');
  await expect(result).toContainText('Left shelf');

  // A masked name is never searched...
  await box.fill('secret');
  await expect(page.getByText('0 result(s)')).toBeVisible();
  // ...but a level 2 item's safe hint is, and the result keeps the mask.
  await box.fill('safe hint');
  await expect(page.getByRole('link', { name: /Missable #1/ })).toBeVisible();
  await expect(page.locator('main')).not.toContainText('Very Secret');
  expect(fetched.filter((url) => /ch-[12]\.json/.test(url))).toEqual([]);

  // Back from a result returns to the same search.
  await page.getByRole('link', { name: /Missable #1/ }).click();
  await expect(page).toHaveURL('/sc/items/sc-ch0-mi-01');
  await page.goBack();
  await expect(box).toHaveValue('safe hint');
});
