import { expect, test } from '@playwright/test';

import { expectSaved, row } from './helpers';

test('two tabs of the app keep each other\'s ticks and show them without a reload', async ({ context }) => {
  const first = await context.newPage();
  const second = await context.newPage();
  await first.goto('/sc/chapters/sc-ch0');
  await second.goto('/sc/chapters/sc-ch0');

  await row(first, 'Safe Quest').getByRole('checkbox').check();
  // The other tab picks the change up on its own...
  await expect(row(second, 'Safe Quest').getByRole('checkbox')).toBeChecked();

  // ...and what it ticks next is added to the first tab's, not written over it.
  await row(second, 'Book One').getByRole('checkbox').check();
  await expect(row(first, 'Book One').getByRole('checkbox')).toBeChecked();
  await expectSaved(second, 'sc-ch0-q-01');
  await expectSaved(second, 'sc-ch0-co-01');
  await second.reload();
  await expect(row(second, 'Safe Quest').getByRole('checkbox')).toBeChecked();
  await expect(row(second, 'Book One').getByRole('checkbox')).toBeChecked();
});
