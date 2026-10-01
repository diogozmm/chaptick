import { expect, test } from '@playwright/test';

import { trackContent } from './helpers';

test('a first visit picks any chapter directly, with no "left behind" warning', async ({ page }) => {
  const fetched = trackContent(page);
  await page.goto('/');
  await expect(page.getByRole('list', { name: 'How it works' })).toContainText("Tell us which chapter you're in");

  await page.getByRole('link', { name: /E2E Game.*Start/ }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Which chapter are you in?' })).toBeVisible();
  await page.getByRole('listitem').filter({ hasText: 'Chapter 1' }).getByRole('button', { name: "I'm here" }).click();

  await expect(page.getByRole('heading', { level: 1, name: 'Chapter 1' })).toBeVisible();
  expect(fetched.some((url) => url.endsWith('ch-2.json'))).toBe(false);

  // Once picked, "Where am I" is back to its usual view.
  await page.goto('/sc/chapters');
  await expect(page.getByText('You are here')).toBeVisible();
  await expect(page.getByText('Chapter 2 — locked')).toBeVisible();
});

test('"How it works" shows on the first checklist until dismissed', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  const card = page.getByRole('region', { name: 'How it works' });
  await expect(card).toContainText('stay hidden until you tap to reveal');
  await card.getByRole('button', { name: 'Got it' }).click();
  await expect(card).toBeHidden();

  await page.reload();
  await expect(page.getByRole('heading', { level: 1, name: 'Prologue' })).toBeVisible();
  await expect(page.getByRole('region', { name: 'How it works' })).toHaveCount(0);
});
