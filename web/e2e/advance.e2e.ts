import { expect, test } from '@playwright/test';

import { row, trackContent } from './helpers';

test('advancing warns about what is left behind without naming it first', async ({ page }) => {
  const fetched = trackContent(page);
  await page.goto('/sc/chapters');
  await page.getByRole('listitem').filter({ hasText: 'Chapter 1 — locked' }).getByRole('button', { name: "I'm here" }).click();

  const warning = page.locator('details').filter({ hasText: 'You will leave 3 item(s) behind' });
  await expect(warning).toBeVisible();
  await expect(warning.getByText('Safe Quest')).toBeHidden();

  await warning.locator('summary').click();
  // Ticked items leave this list by design, so click and assert the new count instead of check().
  await row(page, 'Safe Quest').getByRole('checkbox').click();
  await expect(page.getByText('You will leave 2 item(s) behind')).toBeVisible();
  expect(fetched.some((url) => url.endsWith('ch-1.json'))).toBe(false);

  await page.getByRole('button', { name: "Yes, I'm here" }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Chapter 1' })).toBeVisible();
  await expect(page.getByText('FUTURE QUEST 1')).toBeVisible();
  await expect(page.locator('details summary')).toHaveText('You left 2 item(s) behind');
  await expect(page.locator('body')).not.toContainText('FUTURE QUEST 2');
  expect(fetched.some((url) => url.endsWith('ch-2.json'))).toBe(false);
});

test('going back to an earlier chapter needs no confirmation', async ({ page }) => {
  await page.goto('/sc/chapters');
  await page.getByRole('listitem').filter({ hasText: 'Chapter 1 — locked' }).getByRole('button', { name: "I'm here" }).click();
  await page.getByRole('button', { name: "Yes, I'm here" }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Chapter 1' })).toBeVisible();
  await page.goto('/sc/chapters');
  await page.getByRole('listitem').filter({ hasText: 'Prologue' }).getByRole('button', { name: "I'm here" }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Prologue' })).toBeVisible();
});

test('a checklist moves on to the next chapter without going through "Where am I"', async ({ page }) => {
  const fetched = trackContent(page);
  await page.goto('/sc/chapters/sc-ch0');
  const next = page.getByRole('navigation', { name: 'Next chapter' });
  await next.getByRole('button', { name: "I've reached Chapter 1" }).click();
  await expect(next.getByText('You will leave 3 item(s) behind')).toBeVisible();
  expect(fetched.some((url) => url.endsWith('ch-1.json'))).toBe(false);

  // Cancelling keeps you where you are.
  await next.getByRole('button', { name: 'Cancel' }).click();
  await expect(next.getByRole('button', { name: "I've reached Chapter 1" })).toBeVisible();

  await next.getByRole('button', { name: "I've reached Chapter 1" }).click();
  await next.getByRole('button', { name: "Yes, I'm here" }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Chapter 1' })).toBeVisible();
  await expect(page.getByText('FUTURE QUEST 1')).toBeVisible();
  expect(fetched.some((url) => url.endsWith('ch-2.json'))).toBe(false);

  // From an earlier, already unlocked chapter the next one is a plain link.
  await page.goto('/sc/chapters/sc-ch0');
  await page.getByRole('navigation', { name: 'Next chapter' }).getByRole('link', { name: /Chapter 1/ }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Chapter 1' })).toBeVisible();
});
