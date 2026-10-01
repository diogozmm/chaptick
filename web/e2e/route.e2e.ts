import { expect, test } from '@playwright/test';

import { expectSaved, row } from './helpers';

test('finishing every step of a route completes the item', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  const book = row(page, 'Book One');
  await book.getByRole('button', { name: /Route · 0\/2/ }).click();
  await book.getByRole('checkbox', { name: 'Left shelf' }).check();
  await expect(book.getByRole('button', { name: /Route · 1\/2/ })).toBeVisible();
  await expect(book.getByRole('checkbox').first()).not.toBeChecked();

  await book.getByRole('checkbox', { name: 'Right shelf' }).check();
  await expect(book.getByRole('checkbox').first()).toBeChecked();
  await expect(page.getByText('1 of 4 done')).toBeVisible();
  await expectSaved(page, 'sc-ch0-co-01');

  // Unticking the item clears its route too.
  await book.getByRole('checkbox').first().uncheck();
  await expect(book.getByRole('button', { name: /Route · 0\/2/ })).toBeVisible();
});

test('the route is open on the item page', async ({ page }) => {
  await page.goto('/sc/items/sc-ch0-co-01');
  await expect(page.getByRole('checkbox', { name: 'Left shelf' })).toBeVisible();
});
