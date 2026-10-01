import { expect, test } from '@playwright/test';

import { expectSaved, row, rowById, trackContent } from './helpers';

test('reaches a chapter checklist in at most two taps, then resumes in one', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('link', { name: /E2E Game.*Start/ }).click();
  await page.getByRole('link', { name: 'Prologue' }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Prologue' })).toBeVisible();

  await page.goto('/');
  await page.getByRole('link', { name: 'Continue: Prologue' }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Prologue' })).toBeVisible();
});

test('keeps ticked items after a reload', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await row(page, 'Safe Quest').getByRole('checkbox').check();
  await expect(page.getByText('1 of 4 done')).toBeVisible();
  await expectSaved(page, 'sc-ch0-q-01');

  await page.reload();
  await expect(row(page, 'Safe Quest').getByRole('checkbox')).toBeChecked();
});

test('warns about the next point of no return', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await expect(page.getByRole('status')).toContainText('Before "Leaving town", 1 item(s) are still missing.');
  await row(page, 'Safe Quest').getByRole('checkbox').check();
  await expect(page.getByRole('status')).toContainText('Before "End of prologue", 2 item(s) are still missing.');
});

test('level 1 hides name, location and hint until tapped', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  const hidden = rowById(page, 'sc-ch0-hq-01');
  await expect(hidden).toContainText('Hidden quest #1');
  await expect(hidden).not.toContainText(/Secret Name|Secret Place|Secret hint/);

  await hidden.getByRole('button', { name: /Hidden quest #1/ }).click();
  await expect(hidden).toContainText('Secret Name');
  await expect(hidden).toContainText('Secret Place');
  await expect(hidden).toContainText('Secret hint');
});

test('level 2 shows only the hint and asks before revealing', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  const missable = rowById(page, 'sc-ch0-mi-01');
  await expect(missable).toContainText('Missable #1');
  await expect(missable).toContainText('Safe hint');
  await expect(missable).not.toContainText(/Very Secret|Hidden Place/);

  await missable.getByRole('button', { name: /Missable #1/ }).click();
  await expect(missable).not.toContainText('Very Secret');
  await missable.getByRole('button', { name: 'Show' }).click();
  await expect(missable).toContainText('Very Secret');
});

test('item details respect the mask and show community texts', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await row(page, 'Book One').getByRole('link').click();
  await expect(page.getByRole('heading', { level: 1, name: 'Book One' })).toBeVisible();
  await expect(page.getByText('A community description.')).toBeVisible();
  await page.getByRole('button', { name: 'Mark as done' }).click();
  await expect(page.getByRole('button', { name: 'Mark as not done' })).toBeVisible();

  await page.goto('/sc/items/sc-ch0-hq-01');
  await expect(page.locator('main')).not.toContainText(/Secret Name|Secret Place|Secret hint/);
});

test('never fetches or shows a locked chapter, even from a pasted link', async ({ page }) => {
  const fetched = trackContent(page);
  for (const path of ['/', '/sc/chapters', '/sc/chapters/sc-ch0', '/sc/items/sc-ch0-q-01']) {
    await page.goto(path);
    await expect(page.locator('main h1')).toBeVisible();
  }
  for (const locked of ['/sc/chapters/sc-ch1', '/sc/items/sc-ch2-q-01']) {
    await page.goto(locked);
    await expect(page).toHaveURL('/sc/chapters');
  }
  await expect(page.getByText('Chapter 1 — locked')).toBeVisible();
  await expect(page.locator('body')).not.toContainText('FUTURE');
  expect(fetched.filter((url) => /ch-[12]\.json/.test(url))).toEqual([]);
});
