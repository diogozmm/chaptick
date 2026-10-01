import { expect, test } from '@playwright/test';

test('the arrows walk through the chapter in checklist order', async ({ page }) => {
  await page.goto('/sc/items/sc-ch0-q-01');
  await expect(page.getByRole('heading', { level: 1, name: 'Safe Quest' })).toBeVisible();
  await expect(page.getByText('Expires in this chapter')).toBeVisible();
  await expect(page.getByLabel('Previous item')).toHaveCount(0);

  await page.getByRole('link', { name: 'Next item' }).click();
  await expect(page).toHaveURL('/sc/items/sc-ch0-hq-01');
  await page.getByRole('link', { name: 'Next item' }).click();
  await expect(page).toHaveURL('/sc/items/sc-ch0-mi-01');
  await page.getByRole('link', { name: 'Next item' }).click();
  await expect(page).toHaveURL('/sc/items/sc-ch0-co-01');
  await expect(page.getByRole('link', { name: 'Next item' })).toHaveCount(0);
  await expect(page.getByText('No deadline')).toBeVisible();

  await page.getByRole('link', { name: 'Previous item' }).click();
  await expect(page).toHaveURL('/sc/items/sc-ch0-mi-01');
});

test('ticking an item keeps the arrows in place, and type filters narrow them', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await page.getByRole('button', { name: 'Hide done' }).click();
  await page.getByRole('button', { name: 'Quests', exact: true }).click();
  // Navigate inside the app: a full reload could race the filter's write to IndexedDB.
  await page.getByRole('link', { name: /Safe Quest/ }).click();
  await expect(page).toHaveURL('/sc/items/sc-ch0-q-01');
  await page.getByRole('button', { name: 'Mark as done' }).click();
  await expect(page.getByText('Done', { exact: true })).toBeVisible();
  // Only quests pass the filter, so there is nothing after this one.
  await expect(page.getByRole('link', { name: 'Next item' })).toHaveCount(0);
});

test('one notice hides everything a level 1 item would give away', async ({ page }) => {
  await page.goto('/sc/items/sc-ch0-hq-01');
  const main = page.locator('main');
  await expect(page.getByRole('heading', { level: 1, name: 'Hidden quest #1' })).toBeVisible();
  await expect(main).not.toContainText(/Secret Name|Secret Place|Secret hint|Sources/);
  await page.getByRole('button', { name: 'Reveal', exact: true }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Secret Name' })).toBeVisible();
  await expect(main).toContainText('Secret Place');
  await expect(main).toContainText('Secret hint');
  await expect(main).toContainText('Sources: e2e');
});

test('level 2 keeps the safe hint visible and asks before revealing', async ({ page }) => {
  await page.goto('/sc/items/sc-ch0-mi-01');
  const main = page.locator('main');
  await expect(main).toContainText('Safe hint');
  await expect(main).not.toContainText(/Very Secret|Hidden Place/);
  await page.getByRole('button', { name: 'Reveal', exact: true }).click();
  await expect(main).not.toContainText('Very Secret');
  await page.getByRole('button', { name: 'Show' }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Very Secret' })).toBeVisible();
});

test('a boss page shows its position and the bar never hides the content', async ({ page }) => {
  await page.goto('/sc/bosses/sc-ch0-bs-01');
  await expect(page.getByText('Boss 1 of 1')).toBeVisible();
  await expect(page.getByRole('link', { name: /Next boss|Previous boss/ })).toHaveCount(0);

  await page.goto('/sc/items/sc-ch0-co-01');
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
  const bar = await page.locator('app-detail-bar').boundingBox();
  const last = await page.locator('main app-route-steps li').last().boundingBox();
  expect(bar && last && last.y + last.height <= bar.y).toBe(true);
});

test('a quest lists its fights, masked, with a link to the strategy', async ({ page }) => {
  await page.goto('/sc/items/sc-ch0-q-01');
  const fight = page.getByRole('link', { name: /Boss #1/ });
  await expect(fight).toBeVisible();
  await expect(page.locator('main')).not.toContainText('Secret Boss');
  await fight.click();
  await expect(page).toHaveURL('/sc/bosses/sc-ch0-bs-01');
  await page.getByRole('button', { name: 'Reveal', exact: true }).click();
  await page.getByRole('button', { name: 'Show' }).click();
  await page.getByRole('link', { name: /Part of: Safe Quest/ }).click();
  await expect(page.getByRole('link', { name: /Secret Boss/ })).toBeVisible();
});
