import { expect, test } from '@playwright/test';

import { expectSaved, pickChapter, trackContent } from './helpers';

test('the library marks and filters games by what they offer', async ({ page }) => {
  await page.goto('/');
  const library = page.getByRole('region', { name: 'Library' });
  const card = library.getByRole('link', { name: /Field Game/ });
  await expect(card).toContainText('Checklist');
  await expect(card).toContainText('Compendium');
  await expect(card).toContainText('2 areas · 2 tasks');

  await library.getByRole('navigation', { name: 'Filter by series' }).getByRole('link', { name: 'Compendium' }).click();
  await expect(page).toHaveURL(/\?t=compendium#library$/);
  await expect(library.getByRole('link', { name: /Field Game/ })).toBeVisible();
  await expect(library.getByRole('link', { name: /E2E Game/ })).toHaveCount(0);
});

test('an area game asks for the area, and its compendium only knows what is unlocked', async ({ page }) => {
  const fetched = trackContent(page);
  await page.goto('/cc');
  await expect(page.getByRole('heading', { level: 1, name: 'Which area have you reached?' })).toBeVisible();
  await page.getByRole('listitem').filter({ hasText: 'Area 1' }).getByRole('button', { name: "I'm here" }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Area 1' })).toBeVisible();

  // The checklist links to the compendium.
  await page.getByRole('link', { name: /Compendium/ }).first().click();
  await page.getByRole('searchbox', { name: 'Search items' }).fill('ore');
  await expect(page.getByText('0 item(s)')).toBeVisible();
  await page.getByRole('searchbox', { name: 'Search items' }).fill('herb');
  await page.getByRole('link', { name: /Bitter Herb/ }).click();

  await expect(page.getByRole('heading', { level: 1, name: 'Bitter Herb' })).toBeVisible();
  await expect(page.getByText('Town')).toBeVisible();
  await expect(page.locator('main')).not.toContainText('Cellar');
  await expect(page.getByRole('link', { name: 'Herb Tea' })).toBeVisible();
  expect(fetched.some((url) => /cc\/ch-1\.json/.test(url))).toBe(false);
});

test('reaching a later area adds its sources; creatures that give items have a detail page', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 2');
  await page.goto('/cc/entries/cc-bitter-herb');
  await expect(page.getByText('Cellar Market')).toBeVisible();
  await expect(page.getByText('Area 2 onwards')).toBeVisible();

  await page.goto('/cc/compendium?tab=creatures');
  await expect(page.getByText('Grinning Scarecrow')).toBeVisible();
  await page.getByRole('button', { name: 'Only those that give items' }).click();
  await expect(page.getByText('Grinning Scarecrow')).toBeHidden();
  await page.getByRole('link', { name: 'Cellar Thing' }).click();

  await expect(page.getByRole('heading', { level: 1, name: 'Cellar Thing' })).toBeVisible();
  const steal = page.getByRole('table');
  await expect(steal.getByRole('row', { name: /Bitter Herb.*Level 1.*25%/ })).toBeVisible();
  await steal.getByRole('link', { name: 'Bitter Herb' }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Bitter Herb' })).toBeVisible();
});

test('an area the player has not reached keeps its creatures out', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 1');
  await page.goto('/cc/creatures/cc-cr-cellar-thing');
  await expect(page.getByText("This isn't in the places you have reached yet.")).toBeVisible();
  await expect(page.locator('main')).not.toContainText('Cellar Thing');
});

test('a made recipe stays ticked', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 1');
  await page.goto('/cc/compendium?tab=crafts&c=cook');
  const tea = page.getByRole('checkbox', { name: 'Herb Tea' });
  await tea.check();
  await expectSaved(page, 'cc-cook-herb-tea');
  await page.goto('/cc/compendium?tab=crafts&c=cook');
  await expect(page.getByRole('checkbox', { name: 'Herb Tea' })).toBeChecked();
});
