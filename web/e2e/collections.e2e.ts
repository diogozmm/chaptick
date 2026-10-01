import { expect, test } from '@playwright/test';

import { trackContent } from './helpers';

test('bosses stay masked and out of progress until revealed', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await expect(page.getByText('0 of 4 done')).toBeVisible();
  const section = page.locator('details.bosses');
  await section.locator('summary').click();
  await expect(section).toContainText('Boss #1');
  await expect(section).toContainText('Part of: Safe Quest');
  await expect(section).not.toContainText('Secret Boss');

  await section.getByRole('link', { name: 'Strategy for boss #1' }).click();
  await expect(page.locator('main')).not.toContainText(/Secret Boss|Boss Lair|Secret strategy/);
  await page.getByRole('button', { name: /Boss #1/ }).click();
  await page.getByRole('button', { name: 'Show' }).click();
  await expect(page.locator('main')).toContainText('Secret Boss');
  await expect(page.locator('main')).toContainText('Boss Lair');
  await expect(page.locator('main')).toContainText('Secret strategy text.');
});

test('collections only show what unlocked chapters reveal', async ({ page }) => {
  const fetched = trackContent(page);
  await page.goto('/');
  await page.getByRole('link', { name: 'Collections' }).first().click();
  await expect(page.getByRole('heading', { level: 1, name: 'Collections' })).toBeVisible();
  await expect(page.getByText('Silver Fish')).toBeVisible();
  await expect(page.getByText('Town pier')).toBeVisible();
  await page.getByRole('tab', { name: 'Recipes' }).click();
  await expect(page.getByText('Town Stew', { exact: true })).toBeVisible();
  await expect(page.getByText('Hero Stew')).toBeVisible();
  await expect(page.locator('body')).not.toContainText('FUTURE');
  expect(fetched.filter((url) => /ch-[12]\.json/.test(url))).toEqual([]);
});

test('a Rank A catch also counts as caught and survives a reload', async ({ page }) => {
  await page.goto('/sc/collections');
  const row = page.locator('li.row').filter({ hasText: 'Silver Fish' });
  await row.getByRole('button', { name: 'Caught at Rank A' }).click();
  await expect(row.getByRole('checkbox')).toBeChecked();
  await expect(page.locator('.stats')).toContainText('1/1 caught');
  await expect(page.locator('.stats')).toContainText('1/1 Rank A');

  await expect
    .poll(() =>
      page.evaluate(
        () =>
          new Promise<string[]>((resolve) => {
            const open = indexedDB.open('bracer-notes');
            open.onsuccess = () => {
              const get = open.result.transaction('progress').objectStore('progress').get('sc');
              get.onsuccess = () => resolve(get.result?.doneItems ?? []);
            };
          }),
      ),
    )
    .toEqual(expect.arrayContaining(['sc-ch0-fi-01', 'sc-ch0-fi-01#rank-a']));
  await page.reload();
  await expect(row.getByRole('button', { name: 'Caught at Rank A' })).toHaveAttribute('aria-pressed', 'true');

  // Unmarking the catch clears Rank A too.
  await row.getByRole('checkbox').uncheck();
  await expect(row.getByRole('button', { name: 'Caught at Rank A' })).toHaveAttribute('aria-pressed', 'false');
});

test('a pasted link to a locked boss redirects', async ({ page }) => {
  await page.goto('/sc/bosses/sc-ch1-bs-01');
  await expect(page).toHaveURL('/sc/chapters');
});
