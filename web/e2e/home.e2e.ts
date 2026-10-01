import { expect, test } from '@playwright/test';

import { expectSaved, row } from './helpers';

test('a first visit gets the introduction; a returning player gets their games first', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('heading', { level: 1, name: 'Never miss a thing, chapter by chapter' })).toBeVisible();

  await page.goto('/sc/chapters/sc-ch0');
  await row(page, 'Book One').getByRole('checkbox').check();
  await expectSaved(page, 'sc-ch0-co-01');
  await page.goto('/zz/chapters/zz-ch0');
  await expect(page.getByRole('heading', { level: 1, name: 'Opening' })).toBeVisible();

  await page.goto('/');
  await expect(page.getByRole('heading', { name: 'Never miss a thing, chapter by chapter' })).toHaveCount(0);
  // The last game played is the big card; the other one is listed right below it.
  await expect(page.getByRole('link', { name: 'Continue: Opening' })).toBeVisible();
  const others = page.getByRole('region', { name: 'Your other games' });
  await expect(others.getByRole('link', { name: /E2E Game.*Prologue · 1 done/ })).toBeVisible();
});

test('the library filters by series, and "See all" opens one series', async ({ page }) => {
  await page.goto('/');
  const library = page.getByRole('region', { name: 'Library' });
  const filters = library.getByRole('navigation', { name: 'Filter by series' });
  await expect(filters.getByRole('link', { name: 'All' })).toHaveAttribute('aria-current', 'true');

  await filters.getByRole('link', { name: 'Second series' }).click();
  await expect(page).toHaveURL(/\?f=second-series#library$/);
  await expect(library.getByRole('heading', { level: 3 })).toHaveText(['Second series']);
  await expect(library.getByRole('link', { name: /Other Game/ })).toBeVisible();
  await expect(library.getByRole('link', { name: /E2E Game/ })).toHaveCount(0);

  await page.goBack();
  await expect(library.getByRole('heading', { level: 3 })).toHaveCount(3);
  await library.getByRole('region', { name: 'Demo series' }).getByRole('link', { name: 'See all' }).click();
  await expect(page).toHaveURL(/\?f=demo-series#library$/);
  await expect(library.getByRole('heading', { level: 3 })).toHaveText(['Demo series']);
});
