import { expect, test } from '@playwright/test';

import { expectSaved, row, trackContent } from './helpers';

test('the library groups games by franchise', async ({ page }) => {
  await page.goto('/games');
  const library = page.getByRole('region', { name: 'All games' });
  await expect(library.getByRole('heading', { level: 3, name: 'Demo series' })).toBeVisible();
  await expect(library.getByRole('heading', { level: 3, name: 'Second series' })).toBeVisible();
  await expect(library.getByRole('link', { name: /Other Game/ })).toBeVisible();
  await expect(library.getByText('Games for this series are on the way.')).toBeVisible();
  await expect(library.getByText('More games and series coming')).toBeVisible();
});

test('each game keeps its own progress and content', async ({ page }) => {
  const fetched = trackContent(page);
  await page.goto('/sc/chapters/sc-ch0');
  await row(page, 'Book One').getByRole('checkbox').check();
  await expectSaved(page, 'sc-ch0-co-01');

  await page.goto('/zz/chapters/zz-ch0');
  await expect(page.getByRole('heading', { level: 1, name: 'Opening' })).toBeVisible();
  await expect(page.getByText('0 of 1 done')).toBeVisible();
  await expect(page.locator('main')).not.toContainText('Book One');

  await page.goto('/');
  await expect(page.getByRole('region', { name: 'Continue' }).getByRole('link', { name: /E2E Game.*Prologue · 1 done/ })).toBeVisible();
  await page.goto('/games');
  await expect(page.getByRole('link', { name: /E2E Game.*In progress · 1 done.*Continue/ })).toBeVisible();
  expect(fetched.filter((url) => url.startsWith('/content/zz/') && url.includes('sc-'))).toEqual([]);
});

test('an unknown game goes back to the library', async ({ page }) => {
  await page.goto('/nope/chapters');
  await expect(page).toHaveURL('/');
});

test('analytics never load outside the production host', async ({ page }) => {
  const external: string[] = [];
  page.on('request', (req) => {
    if (!req.url().startsWith('http://127.0.0.1')) external.push(req.url());
  });
  await page.goto('/');
  await page.getByRole('link', { name: /Start|Continue/ }).first().click();
  await page.waitForLoadState('networkidle');
  expect(external).toEqual([]);
});
