# Contributing

Thanks for helping players not miss anything!

## Spoiler rule (most important)

Issue and PR **titles** must use only the item id, never its name:

- ✅ `fix sc-ch3-hq-02 location`
- ❌ `fix <character name>'s hidden quest`

Descriptions may contain spoilers, but open with a line saying which chapter they cover.

## Fixing or adding data

1. Edit the chapter file in `content/sc/chapters/`.
2. New ids go at the **end** of `content/id-registry.json`. Never remove or reuse an id, even for deleted items:
   people's saved progress points at them.
3. Id format: `<game>-ch<order>-<type>-<nn>`, with type `q` (quest), `hq` (hidden quest), `mi` (missable), `co` (collectible),
   and `cp` for checkpoints. Example: `sc-ch3-hq-02`.
4. Fill `sources` with where the fact came from (`wiki: <page>`, `guide: <name>`, `verified in game`).
5. Run `npm run content:validate` before opening the PR.

`spoilerLevel`:

- `0`: name and location are safe.
- `1`: the name reveals something (a new character, say). The app hides it behind a tap.
- `2`: only the hint is shown; everything else needs tap + confirmation.

Checkpoint descriptions and hints must be neutral: describe the moment, not what happens.

## Text you write

Write in your own words. Do not copy from guides or other sites. Text from the Fandom wiki may be adapted
if you cite the page (same CC BY-SA 4.0 license). By contributing you license your content under CC BY-SA 4.0.

## No game assets

No screenshots, art, icons or music.
