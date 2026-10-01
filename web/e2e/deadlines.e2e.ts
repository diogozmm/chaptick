import { expect, test } from '@playwright/test';

import { row, trackContent } from './helpers';

test('lists what can still be lost, most urgent first, without spoilers', async ({ page }) => {
  const fetched = trackContent(page);
  await page.goto('/sc/chapters/sc-ch0');
  await page.getByRole('link', { name: 'What can I still miss' }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'What can I still miss' })).toBeVisible();
  await expect(page.getByText('3 pending item(s) will be lost')).toBeVisible();

  const headings = page.getByRole('heading', { level: 2 });
  await expect(headings.nth(0)).toContainText('Next point of no return');
  await expect(headings.nth(0)).toContainText('Before: Leaving town');
  await expect(headings.nth(1)).toContainText('Before: End of prologue');
  // Masked items keep their mask here too; open-ended ones are not listed.
  await expect(page.locator('main')).not.toContainText(/Secret Name|Very Secret|Book One/);
  expect(fetched.filter((url) => /ch-[12]\.json/.test(url))).toEqual([]);

  // Ticking one off takes it out of the list.
  await row(page, 'Safe Quest').getByRole('checkbox').click();
  await expect(page.getByText('2 pending item(s) will be lost')).toBeVisible();
  await expect(headings.nth(0)).toContainText('Before: End of prologue');
});
