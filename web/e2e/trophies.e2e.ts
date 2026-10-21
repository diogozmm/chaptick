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

test('the trophies page counts what is done in the chapters reached', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await page.getByRole('link', { name: 'Trophy progress' }).click();
  const quests = page.getByRole('listitem').filter({ hasText: 'Questmaster' });
  await expect(quests).toContainText('0/2');
  // Collection trophies are not counted here; they point to the collections screen.
  await expect(page.getByRole('listitem').filter({ hasText: 'Angler' })).toHaveCount(0);
  await expect(page.getByRole('link', { name: /Fish and recipe trophies/ })).toBeVisible();

  await page.goBack();
  await row(page, 'Safe Quest').getByRole('checkbox').check();
  await page.getByRole('link', { name: 'Trophy progress' }).click();
  await expect(quests).toContainText('1/2');
});

test('a trophy lists what is missing, behind the same masks, and ticking it there updates the count', async ({ page }) => {
  await page.goto('/sc/trophies');
  const quests = page.locator('li.trophy').filter({ hasText: 'Questmaster' });
  await expect(quests).toContainText('0/2');
  await quests.getByText('What is missing (2)').click();
  await expect(row(quests, 'Safe Quest')).toBeVisible();
  // The hidden quest stays behind its mask here too.
  await expect(quests).not.toContainText('Secret Name');
  await expect(quests.getByRole('button', { name: /Hidden quest #1/ })).toBeVisible();

  // The ticked item leaves this list by design, so click and assert the count instead of check().
  await row(quests, 'Safe Quest').getByRole('checkbox').click();
  await expect(quests).toContainText('1/2');
  await expect(quests.getByText('What is missing (1)')).toBeVisible();
  await expect(row(quests, 'Safe Quest')).toHaveCount(0);
});
