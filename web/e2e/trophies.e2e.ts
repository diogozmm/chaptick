import { expect, test } from '@playwright/test';

import { row, rowById } from './helpers';

test('items show the trophy they count toward, behind the same mask as the hint', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await expect(row(page, 'Safe Quest')).toContainText('Questmaster');
  const hidden = rowById(page, 'sc-ch0-hq-01');
  await expect(hidden).not.toContainText('Questmaster');
  await hidden.getByRole('button', { name: /Hidden quest #1/ }).click();
  await expect(hidden).toContainText('Questmaster');

  // The "Trophies" filter keeps only items that count toward one.
  await page.getByRole('button', { name: 'Trophies' }).click();
  await expect(page.locator('app-item-row')).toHaveCount(2);
  await expect(page.locator('main')).not.toContainText('Book One');

  await page.goto('/sc/items/sc-ch0-q-01');
  await expect(page.getByText('Counts toward the trophy')).toBeVisible();
  await expect(page.getByText('Finish every quest.')).toBeVisible();
});

test('a collection trophy shows on its tab', async ({ page }) => {
  await page.goto('/sc/collections');
  await expect(page.getByText('Angler')).toBeVisible();
  await page.getByRole('tab', { name: /Recipes/ }).click();
  await expect(page.getByText('Angler')).toHaveCount(0);
});
