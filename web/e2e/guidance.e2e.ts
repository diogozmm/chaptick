import { expect, test } from '@playwright/test';
import { expectSaved } from './helpers';

test('separates guidance and keeps optional actions and branches out of completion', async ({ page }) => {
  await page.goto('/sc/items/sc-ch0-q-01');
  for (const name of ['Requirements', 'Before you start', 'Important', 'Rewards', 'Optional', 'Choose the applicable path']) {
    await expect(page.getByRole('heading', { name, exact: true })).toBeVisible();
  }
  await expect(page.getByRole('heading', { name: 'With Agate', exact: true })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'With Scherazard', exact: true })).toBeVisible();
  await expect(page.locator('app-item-guidance input')).toHaveCount(0);
  await page.getByRole('button', { name: 'Mark as done', exact: true }).click();
  await expectSaved(page, 'sc-ch0-q-01');
  await page.reload();
  await expect(page.getByText('Done', { exact: true })).toBeVisible();
  await page.getByRole('button', { name: 'Mudar para português' }).click();
  await expect(page.getByRole('heading', { name: 'Antes de começar', exact: true })).toBeVisible();
  await expect(page.getByText('Equipe proteção contra Freeze.')).toBeVisible();
});

for (const level of [1, 2]) {
  test(`structured details stay hidden until level ${level} is revealed`, async ({ page }) => {
    await page.goto(`/sc/items/${level === 1 ? 'sc-ch0-hq-01' : 'sc-ch0-mi-01'}`);
    await expect(page.locator('main')).not.toContainText(/Secret reward|Secret equipment/);
    if (level === 2) await expect(page.getByText('Safe hint', { exact: true })).toBeVisible();
    await page.getByRole('button', { name: 'Reveal', exact: true }).click();
    if (level === 2) {
      await expect(page.locator('main')).not.toContainText('Secret reward');
      await page.getByRole('button', { name: 'Show', exact: true }).click();
    }
    await expect(page.getByText('Secret reward', { exact: true })).toBeVisible();
  });
}
