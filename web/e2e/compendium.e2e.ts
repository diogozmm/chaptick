import { expect, test } from '@playwright/test';

import { expectSaved, pickChapter, trackContent } from './helpers';

test('the library marks and filters games by what they offer', async ({ page }) => {
  await page.goto('/');
  const library = page.getByRole('region', { name: 'Library' });
  const card = library.getByRole('link', { name: /Field Game/ });
  await expect(card).toContainText('Checklist');
  await expect(card).toContainText('Compendium');
  await expect(card).toContainText('2 areas · 2 tasks');

  await library.getByRole('navigation', { name: 'Filter by series' }).getByRole('link', { name: 'Compendium' }).click();
  await expect(page).toHaveURL(/\?t=compendium#library$/);
  await expect(library.getByRole('link', { name: /Field Game/ })).toBeVisible();
  await expect(library.getByRole('link', { name: /E2E Game/ })).toHaveCount(0);
});

test('an area game asks for the area, and its compendium only knows what is unlocked', async ({ page }) => {
  const fetched = trackContent(page);
  await page.goto('/cc');
  await expect(page.getByRole('heading', { level: 1, name: 'Which area have you reached?' })).toBeVisible();
  await page.getByRole('listitem').filter({ hasText: 'Area 1' }).getByRole('button', { name: "I'm here" }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Area 1' })).toBeVisible();

  // The checklist links to the compendium.
  await page.getByRole('link', { name: /Compendium/ }).first().click();
  await page.getByRole('searchbox', { name: 'Search items' }).fill('deep');
  await expect(page.getByText('0 item(s)')).toBeVisible();
  await page.getByRole('searchbox', { name: 'Search items' }).fill('herb');
  await page.getByRole('link', { name: /Bitter Herb/ }).click();

  await expect(page.getByRole('heading', { level: 1, name: 'Bitter Herb' })).toBeVisible();
  await expect(page.getByText('Town')).toBeVisible();
  await expect(page.locator('main')).not.toContainText('Cellar');
  await expect(page.getByRole('link', { name: 'Herb Tea' })).toBeVisible();
  expect(fetched.some((url) => /cc\/ch-1\.json/.test(url))).toBe(false);
});

test('reaching a later area adds its sources; creatures that give items have a detail page', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 2');
  await page.goto('/cc/entries/cc-bitter-herb');
  await expect(page.getByText('Cellar Market')).toBeVisible();
  await expect(page.getByText('Area 2 onwards')).toBeVisible();

  await page.goto('/cc/compendium?tab=creatures');
  await page.getByRole('button', { name: 'Only those that give items' }).click();
  await page.getByRole('link', { name: 'Grinning Scarecrow' }).click();
  await expect(page.getByText('Weak point: Weak to Light Attacks')).toBeVisible();
  await expect(page.getByText('Battle loot · Farm Common Loot')).toBeVisible();
  await page.getByText('Can also draw from Random Potions (1)').click();
  await expect(page.getByText('Chaos Potion')).toBeVisible();

  await page.goto('/cc/compendium?tab=creatures');
  await page.getByRole('link', { name: 'Cellar Thing' }).click();

  await expect(page.getByRole('heading', { level: 1, name: 'Cellar Thing' })).toBeVisible();
  const steal = page.getByRole('table');
  await expect(steal.getByRole('row', { name: /Bitter Herb.*Level 1.*25%/ })).toBeVisible();
  await steal.getByRole('link', { name: 'Bitter Herb' }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Bitter Herb' })).toBeVisible();
});

test('an area the player has not reached keeps its creatures out', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 1');
  await page.goto('/cc/creatures/cc-cr-cellar-thing');
  await expect(page.getByText("This isn't in the places you have reached yet.")).toBeVisible();
  await expect(page.locator('main')).not.toContainText('Cellar Thing');
});

test('a made recipe stays ticked', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 1');
  await page.goto('/cc/compendium?tab=crafts&c=cook');
  const tea = page.getByRole('checkbox', { name: 'Herb Tea' });
  await tea.check();
  await expectSaved(page, 'cc-cook-herb-tea');
  await page.goto('/cc/compendium?tab=crafts&c=cook');
  await expect(page.getByRole('checkbox', { name: 'Herb Tea' })).toBeChecked();
});

test('the season view shows what only this season has, last chances first, for reached areas only', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 1');
  await page.getByRole('link', { name: 'What does your season bring?' }).click();
  await expect(page.getByText('Pick your season to see what it brings.')).toBeVisible();

  await page.getByRole('button', { name: 'Summer (Harvest)' }).click();
  const only = page.getByRole('region', { name: /Only this season/ });
  await expect(only.getByRole('link')).toHaveText([/Glow Fish.*Night.*Last chance/, /Frost Eel.*Seasons: summer, autumn/]);
  await expect(page.locator('main')).not.toContainText('Moon Carp');

  await page.getByRole('button', { name: 'Spring (Rebirth)' }).click();
  await expect(page.getByText('Coming in Summer (Harvest) (2)')).toBeVisible();

  // Seeds show up in the season they can be planted, flagged when it is their last one.
  await page.getByRole('button', { name: 'Autumn (Witch)' }).click();
  const plant = page.getByRole('region', { name: /To plant now/ });
  await expect(plant.getByRole('link')).toHaveText([/Squash Seed.*Grows in 12 days.*Last season to plant it/]);

  // The season is remembered for the game.
  await page.goto('/cc/chapters/cc-ch0');
  await expect(page.getByRole('link', { name: 'This season: Autumn (Witch)' })).toBeVisible();
});

test('equipment shows its slot, stats and effect', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 1');
  await page.goto('/cc/compendium?c=equipment');
  await page.getByRole('link', { name: /Iron Sword \+2.*Weapon/ }).click();
  await expect(page.getByRole('heading', { level: 2, name: 'Equipment: Weapon' })).toBeVisible();
  await expect(page.getByRole('listitem').filter({ hasText: 'Attack +6' })).toBeVisible();
  await expect(page.getByText('+25% chance for Basic Attacks to add +1 Lethal point')).toBeVisible();
});

test('a shopping list sums what to gather and lets you make or buy each ingredient', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 1');
  await page.goto('/cc/entries/cc-iron-sword-2');
  await page.getByRole('link', { name: 'Shopping list' }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Iron Sword +2' })).toBeVisible();

  const gather = page.getByRole('region', { name: 'What to gather' });
  // Iron Bar has no other way to get it, so it is made from ore by default.
  await expect(gather.getByRole('listitem')).toHaveText([/1×\s*Bitter Herb/, /2×\s*Iron Ore/]);

  await page.getByRole('button', { name: 'One more' }).click();
  await expect(page).toHaveURL(/qty=2/);
  await expect(gather.getByRole('listitem')).toHaveText([/2×\s*Bitter Herb/, /4×\s*Iron Ore/]);

  await page.getByRole('button', { name: 'Get it ready-made' }).click();
  await expect(gather.getByRole('listitem')).toHaveText([/2×\s*Bitter Herb/, /4×\s*Iron Bar/]);

  // Ticked items move to the bottom.
  await gather.getByRole('checkbox', { name: /Bitter Herb/ }).check();
  await expect(gather.getByRole('listitem')).toHaveText([/4×\s*Iron Bar/, /2×\s*Bitter Herb/]);
});

test('villagers show what they love, and an item shows who likes it as a gift', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 1');
  await page.goto('/cc/compendium?tab=villagers');
  const ada = page.getByRole('region', { name: 'Ada' });
  await expect(ada.getByRole('link', { name: 'Herb Tea' })).toBeVisible();
  await ada.getByText('Hates (1)').click();
  await expect(ada.getByRole('link', { name: 'Iron Ore' })).toBeVisible();
  await expect(page.getByRole('region', { name: 'Bo' })).toContainText('follows the common tastes');

  await page.goto('/cc/entries/cc-bitter-herb');
  await expect(page.getByRole('region', { name: 'As a gift' })).toContainText('Likes: Ada');
  await expect(page.getByRole('region', { name: 'As a gift' })).toContainText('Everyone else: Dislike it (−6)');
  await page.goto('/cc/entries/cc-herb-tea');
  await expect(page.getByRole('region', { name: 'As a gift' })).toContainText('Everyone else: Like it (+5)');
  await page.goto('/cc/compendium?tab=crafts&c=process');
  await expect(page.getByText('2 hours · makes 2')).toBeVisible();
});

test('a name that differs in the game replaces ours on this device and can be sent in', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 1');
  await page.goto('/cc/entries/cc-bitter-herb');
  await page.getByRole('button', { name: 'Different name in your game?' }).click();
  await page.getByRole('textbox', { name: 'Name as your game shows it' }).fill('Bitterleaf');
  await page.getByRole('button', { name: 'Use this name' }).click();

  await expect(page.getByRole('heading', { level: 1, name: 'Bitterleaf' })).toBeVisible();
  await expect(page.getByText('Our name: Bitter Herb')).toBeVisible();
  const report = page.getByRole('link', { name: 'a GitHub issue' }).or(page.getByRole('link', { name: /GitHub/ }));
  await expect(report.first()).toHaveAttribute('href', /template=name-correction\.yml.*ingame=Bitterleaf/);

  // Search finds it by the player's name, and lists show it.
  await page.goto('/cc/compendium?q=bitterleaf');
  await expect(page.getByRole('link', { name: /Bitterleaf/ })).toBeVisible();

  await page.goto('/cc/entries/cc-bitter-herb');
  await page.getByRole('button', { name: 'Edit' }).click();
  await page.getByRole('button', { name: 'Back to "Bitter Herb"' }).click();
  await expect(page.getByRole('heading', { level: 1, name: 'Bitter Herb' })).toBeVisible();
});

test('the season calendar shows today, later this season and weekly events', async ({ page }) => {
  await pickChapter(page, 'cc', 'Area 1');
  await page.goto('/cc/compendium?tab=season');
  await page.getByRole('button', { name: 'Autumn (Witch)' }).click();
  const cal = page.getByRole('region', { name: 'Calendar' });
  await expect(cal.getByText('This season')).toBeVisible();
  await expect(cal).toContainText('Day 7');
  await expect(cal).not.toContainText('Carnival');
  await expect(cal).toContainText('Weekends');

  for (let i = 0; i < 7; i++) await cal.getByRole('button', { name: 'Next day' }).click();
  await expect(cal.getByText('Today, day 7')).toBeVisible();
  await expect(cal.locator('.today')).toContainText('Fishing Contest');
  await expect(cal).toContainText('Day 21 · in 14 day(s)');
  await expect(cal.locator('.today').getByRole('link', { name: 'Glow Fish' })).toBeVisible();

  await page.getByRole('button', { name: 'Winter (Death)' }).click();
  await expect(cal).toContainText('Carnival');
});
