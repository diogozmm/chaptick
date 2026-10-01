# Deploy

The app is a static site on **Cloudflare** (Workers static assets, or Pages). There is no server in Phase 1.

## One-time setup (Cloudflare Workers, static assets)

The app is served as static assets by a Worker with no server code. `wrangler.jsonc` at the repo root tells
Wrangler which folder to serve and turns on the single-page-app fallback, so deep links like
`/sc/chapters/sc-ch0` load the app instead of a 404.

1. Push this repository to GitHub.
2. Cloudflare dashboard → Workers & Pages → Create → Import a repository → pick the repository.
3. Settings:

   | Setting | Value |
   | --- | --- |
   | Project name | `chaptick` (must match `name` in `wrangler.jsonc`) |
   | Build command | `npm ci && npm run content:build && cd web && npm ci && npx ng build` |
   | Deploy command | `npx wrangler deploy` |
   | Root directory | `/` (the repository root, where `wrangler.jsonc` lives) |
   | Environment variable | `NODE_VERSION` = `24` |

4. Save. Every push to `main` deploys to production; pull requests get preview builds.

Cache and security headers live in `web/public/_headers`, which Workers static assets honour. Check a deploy with
`npx wrangler deploy --dry-run` (no login needed) or `npx wrangler dev` to serve the build locally.

### Alternative: Cloudflare Pages

Pages also works without `wrangler.jsonc`: same build command, output directory `web/dist/web/browser`. With no
`404.html` in the output, Pages serves `index.html` for unknown paths.

## Moving to a new domain

Browsers keep each address's saved data apart, so progress saved on `chaptick.diogo-zmm.workers.dev` is not
visible on a new domain. The app carries it over with a transfer link (the progress travels after the `#`, which
never reaches a server). To move:

1. Cloudflare dashboard → Workers & Pages → `chaptick` → Settings → Domains & Routes → add the custom domain.
   The same Worker now answers on both addresses; keep the `workers.dev` one enabled.
2. In `web/src/app/site.config.ts`, set `canonicalOrigin` to the new address, e.g. `'https://chaptick.app'`
   (no trailing slash).
3. In `web/src/index.html`, change the `og:image` URL to the new domain.
4. Deploy. Visits on the old address now show "Chaptick moved to …" with "Take my progress there": one tap opens
   the new address with the player's progress, and the new address asks before replacing anything.

Leave the old address running for a long while: players who come back months later still need it to move their
progress. Players can also move progress between devices any time with "Share a transfer link" in the library.

## Publishing a content correction

1. Edit `content/`, bump `dataVersion` in `content/sc/game.json`.
2. Merge the PR. The new `dataVersion` changes the chapter URLs (`?v=`), so installed apps fetch the
   corrected chapter instead of the cached one, and the service worker shows "A new version is ready".

## Optional settings (`web/src/app/site.config.ts`)

- `analytics`: Umami script URL and website id (Umami Cloud's free tier, or self-hosted). Leave `null`
  to disable. It is cookieless and set to honour Do Not Track, so no consent banner is needed.
- `donations`, `contactEmail`, `repoUrl`: empty values hide the related UI.
- `sources`, `contributors`, `supporters`: shown on the credits page.
