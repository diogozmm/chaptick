import { Page, expect } from '@playwright/test';

/** Records every content file the page asks for, to prove locked chapters are never fetched. */
export function trackContent(page: Page): string[] {
  const urls: string[] = [];
  page.on('request', (req) => {
    const path = new URL(req.url()).pathname;
    if (path.startsWith('/content/')) urls.push(path);
  });
  return urls;
}

/** Progress writes are async; wait until IndexedDB has them before reloading. */
export async function expectSaved(page: Page, itemId: string, saved = true): Promise<void> {
  await expect
    .poll(() =>
      page.evaluate(
        (id) =>
          new Promise<boolean>((resolve) => {
            const open = indexedDB.open('bracer-notes');
            open.onsuccess = () => {
              const get = open.result.transaction('progress').objectStore('progress').get('sc');
              get.onsuccess = () => resolve(Boolean(get.result?.doneItems.includes(id)));
            };
          }),
        itemId,
      ),
    )
    .toBe(saved);
}

export const row = (page: Page, text: string | RegExp) => page.locator('app-item-row').filter({ hasText: text });

/** A checklist row found by item id, so it still matches after its name is revealed. */
export const rowById = (page: Page, itemId: string) =>
  page.locator('app-item-row').filter({ has: page.locator(`[id="name-${itemId}"]`) });
