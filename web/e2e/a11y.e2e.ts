import AxeBuilder from '@axe-core/playwright';
import { expect, test } from '@playwright/test';

const PAGES = ['/', '/sc/chapters', '/sc/chapters/sc-ch0', '/sc/items/sc-ch0-co-01', '/credits', '/privacy'];

for (const colorScheme of ['dark', 'light'] as const) {
  for (const path of PAGES) {
    test(`no WCAG A/AA violations on ${path} (${colorScheme})`, async ({ page }) => {
      // Entrance animations fade content in; axe must measure the final colors, not a mid-fade frame.
      await page.emulateMedia({ colorScheme, reducedMotion: 'reduce' });
      await page.goto(path);
      await expect(page.locator('main h1')).toBeVisible();
      const { violations } = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
      expect(violations.map((v) => `${v.id}: ${v.nodes.map((n) => n.target).join(' | ')}`)).toEqual([]);
    });
  }
}
