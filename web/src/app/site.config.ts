/**
 * Public, non-secret settings. Everything here ships to the browser and lives in a public repo.
 * Empty values hide the matching UI, so the app works before they are filled in.
 */
export const SITE = {
  repoUrl: 'https://github.com/diogozmm/chaptick',
  contactEmail: 'diogo.zmm@outlook.com',
  donations: [] as { label: string; url: string }[], // e.g. GitHub Sponsors, Ko-fi, Pix/Apoia.se
  /** Cookieless Umami. Null disables analytics entirely. */
  analytics: null as { scriptUrl: string; websiteId: string } | null,

  /** Guides and wikis the data was checked against. Keep in sync with `sources` in content/. */
  sources: [
    {
      name: 'Neoseeker — Trails in the Sky 2nd Chapter Walkthrough',
      authors: 'Zoelius, BlazingMeat',
      url: 'https://www.neoseeker.com/trails-in-the-sky-2nd-chapter/walkthrough',
    },
    {
      name: 'GameFAQs — Trails in the Sky 2nd Chapter Guide and Walkthrough',
      authors: 'shockinblue',
      url: 'https://gamefaqs.gamespot.com/ps5/605493-trails-in-the-sky-2nd-chapter/faqs/82698',
    },
  ],
  /** Nicknames of approved community contributors. */
  contributors: [] as string[],
  /** Supporters who asked to be credited. */
  supporters: [] as string[],
};
