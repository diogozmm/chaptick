# Deploy

The app is a static site on **Cloudflare Pages**. There is no server in Phase 1.

## One-time setup

1. Push this repository to GitHub.
2. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → pick the repository.
3. Build settings:

   | Setting | Value |
   | --- | --- |
   | Framework preset | None |
   | Build command | `npm ci && npm run content:build && cd web && npm ci && npx ng build` |
   | Build output directory | `web/dist/web/browser` |
   | Environment variable | `NODE_VERSION` = `24` |

4. Save. Every push to `main` deploys to production; every pull request gets its own preview URL.

There is no `404.html` in the output, so Pages serves `index.html` for unknown paths (SPA mode),
which is what deep links like `/sc/chapters/sc-ch0` need. Cache and security headers live in
`web/public/_headers`.

## Publishing a content correction

1. Edit `content/`, bump `dataVersion` in `content/sc/game.json`.
2. Merge the PR. The new `dataVersion` changes the chapter URLs (`?v=`), so installed apps fetch the
   corrected chapter instead of the cached one, and the service worker shows "A new version is ready".

## Optional settings (`web/src/app/site.config.ts`)

- `analytics`: Umami script URL and website id (Umami Cloud's free tier, or self-hosted). Leave `null`
  to disable. It is cookieless and set to honour Do Not Track, so no consent banner is needed.
- `donations`, `contactEmail`, `repoUrl`: empty values hide the related UI.
- `sources`, `contributors`, `supporters`: shown on the credits page.
