import { expect, test } from '@playwright/test';

import { row } from './helpers';

test('a transfer link carries progress to a fresh browser', async ({ browser, baseURL }) => {
  // Device A: tick something, then copy the link (no share sheet, so it goes to the clipboard).
  const a = await browser.newContext({ permissions: ['clipboard-read', 'clipboard-write'] });
  const pageA = await a.newPage();
  await pageA.addInitScript(() => Object.defineProperty(navigator, 'share', { value: undefined }));
  await pageA.goto('/sc/chapters/sc-ch0');
  await row(pageA, 'Safe Quest').getByRole('checkbox').check();
  await pageA.getByRole('link', { name: 'Chaptick' }).click();
  await pageA.getByRole('link', { name: 'Back up or move your progress' }).click();
  await pageA.getByRole('button', { name: 'Copy a transfer link' }).click();
  await expect(pageA.getByText('Link copied. Open it on the other device.')).toBeVisible();
  const link = await pageA.evaluate(() => navigator.clipboard.readText());
  expect(link.startsWith(`${baseURL}/#transfer=z`)).toBe(true);
  await a.close();

  // Device B: nothing saved yet. Opening the link asks first, then imports.
  const b = await browser.newContext();
  const pageB = await b.newPage();
  await pageB.goto(link);
  const dialog = pageB.getByRole('alertdialog', { name: 'Progress from a link' });
  await expect(dialog).toContainText('E2E Game');
  // The data leaves the address bar before anything else happens.
  await expect(pageB).toHaveURL(`${baseURL}/`);
  await dialog.getByRole('button', { name: 'Replace' }).click();
  await expect(pageB.getByText('Progress imported (1 game(s)).')).toBeVisible();

  await pageB.goto('/sc/chapters/sc-ch0');
  await expect(row(pageB, 'Safe Quest').getByRole('checkbox')).toBeChecked();
  await b.close();
});

test('a cut link is refused without touching saved progress', async ({ page }) => {
  await page.goto('/#transfer=zH4sIAAAA');
  await expect(page.getByText("That file isn't an exported progress file.")).toBeVisible();
  await expect(page.getByRole('alertdialog')).toHaveCount(0);
});
