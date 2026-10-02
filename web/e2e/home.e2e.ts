import { expect, test } from '@playwright/test';

import { expectSaved, pickChapter, row } from './helpers';

test('a first visit gets the introduction and every game; a returning player gets their games to continue', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('heading', { level: 1, name: 'Never miss a thing, chapter by chapter' })).toBeVisible();
  const pick = page.getByRole('region', { name: 'Pick a game' });
  await expect(pick.getByRole('link', { name: /E2E Game.*Start/ })).toBeVisible();
  await expect(pick.getByRole('link', { name: /Other Game.*Start/ })).toBeVisible();

  await page.goto('/sc/chapters/sc-ch0');
  await row(page, 'Book One').getByRole('checkbox').check();
  await expectSaved(page, 'sc-ch0-co-01');
  await pickChapter(page, 'zz', 'Opening');

  await page.goto('/');
  await expect(page.getByRole('heading', { name: 'Never miss a thing, chapter by chapter' })).toHaveCount(0);
  const continuing = page.getByRole('region', { name: 'Continue' });
  // Most recently played first.
  await expect(continuing.getByRole('link')).toHaveText([/Other Game.*Opening/, /E2E Game.*Prologue · 1 done/]);
  await continuing.getByRole('link', { name: /E2E Game/ }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Prologue' })).toBeVisible();
});

test('the home search finds games, and content of started games only up to where the player is', async ({ page }) => {
  await page.goto('/');
  const search = page.getByRole('searchbox', { name: /Search games/ });
  await search.fill('other');
  await expect(page).toHaveURL(/\?q=other/);
  await expect(page.getByRole('link', { name: /Other Game.*Start/ })).toBeVisible();

  await pickChapter(page, 'sc', 'Prologue');
  await page.goto('/');
  await search.fill('safe');
  const sc = page.getByRole('group', { name: 'E2E Game' });
  await expect(sc.getByRole('link', { name: /Safe Quest/ })).toBeVisible();
  await sc.getByRole('link', { name: /Safe Quest/ }).click();
  await expect(page).toHaveURL(/\/sc\/items\//);

  // A later chapter's content is never searched.
  await page.goto('/?q=future');
  await expect(page.getByText('Nothing found for "future".')).toBeVisible();
});

test('all games, by series, with filters', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('link', { name: /All games/ }).click();
  const library = page.getByRole('region', { name: 'All games' });
  const filters = library.getByRole('navigation', { name: 'Filter by series' });
  await expect(filters.getByRole('link', { name: 'All' })).toHaveAttribute('aria-current', 'true');

  await filters.getByRole('link', { name: 'Second series' }).click();
  await expect(page).toHaveURL(/\/games\?f=second-series$/);
  await expect(library.getByRole('heading', { level: 3 })).toHaveText(['Second series']);
  await expect(library.getByRole('link', { name: /Other Game/ })).toBeVisible();
  await expect(library.getByRole('link', { name: /E2E Game/ })).toHaveCount(0);

  await page.goBack();
  await expect(library.getByRole('heading', { level: 3 })).toHaveCount(3);
  await library.getByRole('region', { name: 'Demo series' }).getByRole('link', { name: 'See all' }).click();
  await expect(page).toHaveURL(/\/games\?f=demo-series$/);
  await expect(library.getByRole('heading', { level: 3 })).toHaveText(['Demo series']);
});
