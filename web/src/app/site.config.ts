/**
 * Public, non-secret settings. Everything here ships to the browser and lives in a public repo.
 * Empty values hide the matching UI, so the app works before they are filled in.
 */
export const SITE = {
  repoUrl: 'https://github.com/diogozmm/chaptick',
  contactEmail: 'diogo.zmm@outlook.com',
  donations: [] as { label: string; url: string }[], // e.g. GitHub Sponsors, Ko-fi, Pix/Apoia.se
  /**
   * The address the app should live at, e.g. 'https://chaptick.app' once a domain is bought. Empty
   * for now. When set, visits on any other address (like the workers.dev one) show a banner that
   * carries the player's progress over, since browsers keep each address's data apart.
   * See docs/deploy.md, "Moving to a new domain".
   */
  canonicalOrigin: '',
  /**
   * Cookieless Umami. Null disables analytics entirely. It only runs on `hosts`, so local
   * development and the e2e tests never load it or count as visits: add the new host here when
   * the site moves to its own domain.
   */
  analytics: {
    scriptUrl: 'https://cloud.umami.is/script.js',
    websiteId: '72d5d9cc-0ead-43cf-8565-c133dc8da961',
    hosts: ['chaptick.diogo-zmm.workers.dev'],
  } as { scriptUrl: string; websiteId: string; hosts: string[] } | null,

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
    {
      name: 'Neoseeker — Ys X: Nordics and Proud Nordics Walkthrough',
      authors: 'Neoseeker guide team',
      url: 'https://www.neoseeker.com/ys-x-nordics/walkthrough',
    },
    {
      name: 'GameFAQs — Ys X: Nordics Guide and Walkthrough',
      authors: 'shockinblue',
      url: 'https://gamefaqs.gamespot.com/ps5/390326-ys-x-nordics/faqs/80939',
    },
  ],
  /** Nicknames of approved community contributors. */
  contributors: [] as string[],
  /** Supporters who asked to be credited. */
  supporters: [] as string[],
};
