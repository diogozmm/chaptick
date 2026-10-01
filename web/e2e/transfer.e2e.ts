import { expect, test } from '@playwright/test';

import { expectSaved, row } from './helpers';

test('exported progress restores on another device', async ({ page, browser }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await row(page, 'Book One').getByRole('checkbox').check();
  await expectSaved(page, 'sc-ch0-co-01');
  await page.goto('/');
  const [download] = await Promise.all([page.waitForEvent('download'), page.getByRole('button', { name: 'Export' }).click()]);
  const file = await download.path();

  const other = await browser.newContext({ locale: 'en-US' });
  const phone = await other.newPage();
  await phone.goto('/');
  await phone.locator('input[type=file]').setInputFiles(file);
  await phone.getByRole('button', { name: 'Replace' }).click();
  await expect(phone.getByRole('status')).toHaveText('Progress imported (1 game(s)).');
  await phone.goto('/sc/chapters/sc-ch0');
  await expect(row(phone, 'Book One').getByRole('checkbox')).toBeChecked();
  await other.close();
});

test('a wrong file is rejected and progress is kept', async ({ page }) => {
  await page.goto('/sc/chapters/sc-ch0');
  await row(page, 'Book One').getByRole('checkbox').check();
  await expectSaved(page, 'sc-ch0-co-01');
  await page.goto('/');
  await page.locator('input[type=file]').setInputFiles({ name: 'x.json', mimeType: 'application/json', buffer: Buffer.from('{}') });
  await page.getByRole('button', { name: 'Replace' }).click();
  await expect(page.getByRole('status')).toHaveText("That file isn't an exported progress file.");
  await page.goto('/sc/chapters/sc-ch0');
  await expect(row(page, 'Book One').getByRole('checkbox')).toBeChecked();
});
