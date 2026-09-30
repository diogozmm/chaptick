# bracer-notes

> Working title. Unofficial, spoiler-safe companion for **Trails in the Sky 2nd Chapter**.

Tell it which chapter you are in and see only what you can't miss up to that point:
quests, hidden quests, missables and collectibles, with a warning before each point of no return.

- Works offline on your phone, next to the console.
- No account. Progress stays on your device (export/import to move it).
- Content is locked by chapter, so future chapters never show up by accident.

## Repository

| Path | What |
| --- | --- |
| `content/` | Game data, one JSON file per chapter, validated by `content/schema/` |
| `content/id-registry.json` | Every id ever used. Append-only: saved progress points at these ids |
| `scripts/` | `validate-content.mjs` (CI) and `build-content.mjs` (writes `web/public/content/`) |
| `web/` | Angular PWA |

```sh
npm install
npm run content:validate   # schema, ids, checkpoints, append-only registry
npm run content:build      # writes web/public/content/
npm run test:content

cd web
npm install
npx ng serve               # http://localhost:4200
npx ng test --watch=false
npx playwright test        # e2e on a production build with fixture content
```

Deploy: see [docs/deploy.md](docs/deploy.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Please never write item or character names in issue or PR titles; use the item id.

## Licenses

- Code: [MIT](LICENSE)
- Content (`content/`): [CC BY-SA 4.0](LICENSE-CONTENT)

## Support

Donations keep hosting running: <!-- TODO: GitHub Sponsors / Ko-fi / Pix links -->

---

Fan project, unofficial and not affiliated with Nihon Falcom or its publishers. All trademarks belong to their owners.
