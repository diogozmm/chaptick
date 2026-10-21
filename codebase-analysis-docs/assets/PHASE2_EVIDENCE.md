# Phase 2 evidence and continuation ledger

INDEX_VERSION: phase2-v1. Source-local architectural review. Hashes are SHA-256 of complete files, truncated to eight hex digits. Chunks identify relevant source ranges, not test execution. Large page templates were searched for architectural call sites/error UI rather than exhaustively reviewed.

| Source chunk / stable anchor | Architectural evidence |
| --- | --- |
| `CHUNK_ID = wrangler.jsonc#1-11#901ff326`<br>[[F:wrangler.jsonc#1-11#901ff326]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/main.ts#1-6#2341253f`<br>[[F:web/src/main.ts#1-6#2341253f]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/app.config.ts#1-48#1b1fe1f8`<br>[[F:web/src/app/app.config.ts#1-48#1b1fe1f8]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/app.ts#1-34#7cffa631`<br>[[F:web/src/app/app.ts#1-34#7cffa631]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/app.html#1-59#af16d33d`<br>[[F:web/src/app/app.html#1-59#af16d33d]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/app.routes.ts#1-44#e267f9dc`<br>[[F:web/src/app/app.routes.ts#1-44#e267f9dc]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/game/active-game.ts#1-58#db79bed7`<br>[[F:web/src/app/core/game/active-game.ts#1-58#db79bed7]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/content/content.service.ts#1-73#9f6c43a6`<br>[[F:web/src/app/core/content/content.service.ts#1-73#9f6c43a6]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/spoiler/chapter-access.ts#1-49#2984dc74`<br>[[F:web/src/app/core/spoiler/chapter-access.ts#1-49#2984dc74]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/progress/progress.store.ts#1-60#08adcc2a`<br>[[F:web/src/app/core/progress/progress.store.ts#1-60#08adcc2a]] | Store state and activation |
| `CHUNK_ID = web/src/app/core/progress/progress.store.ts#62-120#08adcc2a`<br>[[F:web/src/app/core/progress/progress.store.ts#62-120#08adcc2a]] | Mutations and transfer |
| `CHUNK_ID = web/src/app/core/progress/progress.store.ts#122-160#08adcc2a`<br>[[F:web/src/app/core/progress/progress.store.ts#122-160#08adcc2a]] | Optimistic persistence and queue |
| `CHUNK_ID = web/src/app/core/progress/progress.store.ts#162-202#08adcc2a`<br>[[F:web/src/app/core/progress/progress.store.ts#162-202#08adcc2a]] | Import parsing |
| `CHUNK_ID = web/src/app/core/progress/progress.repository.ts#1-33#510c21ae`<br>[[F:web/src/app/core/progress/progress.repository.ts#1-33#510c21ae]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/game/saved-games.ts#1-68#717ce3e9`<br>[[F:web/src/app/core/game/saved-games.ts#1-68#717ce3e9]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/search/global-search.ts#1-89#8f128d82`<br>[[F:web/src/app/core/search/global-search.ts#1-89#8f128d82]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/pages/home/home.ts#1-63#6f011515`<br>[[F:web/src/app/pages/home/home.ts#1-63#6f011515]] | Home setup |
| `CHUNK_ID = web/src/app/pages/home/home.ts#65-116#6f011515`<br>[[F:web/src/app/pages/home/home.ts#65-116#6f011515]] | Resume and global search |
| `CHUNK_ID = web/src/app/pages/home/home.ts#118-157#6f011515`<br>[[F:web/src/app/pages/home/home.ts#118-157#6f011515]] | Transfer confirmation |
| `CHUNK_ID = web/src/app/core/spoiler/reveal.service.ts#1-15#a59bed00`<br>[[F:web/src/app/core/spoiler/reveal.service.ts#1-15#a59bed00]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/spoiler/item-view.ts#1-59#7decc034`<br>[[F:web/src/app/core/spoiler/item-view.ts#1-59#7decc034]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/ui/spoiler-reveal/spoiler-reveal.ts#1-60#ccd40764`<br>[[F:web/src/app/ui/spoiler-reveal/spoiler-reveal.ts#1-60#ccd40764]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/spoiler/spoiler.ts#1-106#a8bfec27`<br>[[F:web/src/app/core/spoiler/spoiler.ts#1-106#a8bfec27]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/spoiler/deadlines.ts#1-50#ac968fe4`<br>[[F:web/src/app/core/spoiler/deadlines.ts#1-50#ac968fe4]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/search/search.ts#1-80#81af4074`<br>[[F:web/src/app/core/search/search.ts#1-80#81af4074]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/collections/collections.ts#1-84#b1061ea1`<br>[[F:web/src/app/core/collections/collections.ts#1-84#b1061ea1]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/route/route.ts#1-28#0a907cff`<br>[[F:web/src/app/core/route/route.ts#1-28#0a907cff]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/ui/advance-confirm/advance-confirm.ts#1-58#2ecb6b37`<br>[[F:web/src/app/ui/advance-confirm/advance-confirm.ts#1-58#2ecb6b37]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/ui/route-steps/route-steps.ts#1-74#168e55ff`<br>[[F:web/src/app/ui/route-steps/route-steps.ts#1-74#168e55ff]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/pwa/app-update.service.ts#1-59#3f7fc6a1`<br>[[F:web/src/app/core/pwa/app-update.service.ts#1-59#3f7fc6a1]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/progress/transfer.service.ts#1-53#5bf5a484`<br>[[F:web/src/app/core/progress/transfer.service.ts#1-53#5bf5a484]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/analytics.service.ts#1-33#0c4afc66`<br>[[F:web/src/app/core/analytics.service.ts#1-33#0c4afc66]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/i18n/lang.service.ts#1-41#ba519d52`<br>[[F:web/src/app/core/i18n/lang.service.ts#1-41#ba519d52]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/pages/entry/entry.ts#1-94#9eaa2033`<br>[[F:web/src/app/pages/entry/entry.ts#1-94#9eaa2033]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/pages/creature/creature.ts#1-57#dd004a2b`<br>[[F:web/src/app/pages/creature/creature.ts#1-57#dd004a2b]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/pages/plan/plan.ts#1-97#c5fe1300`<br>[[F:web/src/app/pages/plan/plan.ts#1-97#c5fe1300]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/compendium/compendium.ts#1-64#e4871ad6`<br>[[F:web/src/app/core/compendium/compendium.ts#1-64#e4871ad6]] | Index contracts |
| `CHUNK_ID = web/src/app/core/compendium/compendium.ts#65-131#e4871ad6`<br>[[F:web/src/app/core/compendium/compendium.ts#65-131#e4871ad6]] | Index construction and late name linking |
| `CHUNK_ID = web/src/app/core/compendium/compendium.ts#133-158#e4871ad6`<br>[[F:web/src/app/core/compendium/compendium.ts#133-158#e4871ad6]] | Entry search and category counts |
| `CHUNK_ID = web/src/app/pages/where/where.ts#1-52#b4433bd6`<br>[[F:web/src/app/pages/where/where.ts#1-52#b4433bd6]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/progress/progress.models.ts#1-31#7c470eb1`<br>[[F:web/src/app/core/progress/progress.models.ts#1-31#7c470eb1]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/progress/transfer-link.ts#1-54#f4d083dd`<br>[[F:web/src/app/core/progress/transfer-link.ts#1-54#f4d083dd]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/pages/backup/backup.ts#1-89#b867ff84`<br>[[F:web/src/app/pages/backup/backup.ts#1-89#b867ff84]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = scripts/content-validation.mjs#1-73#73079ad3`<br>[[F:scripts/content-validation.mjs#1-73#73079ad3]] | Discovery, schemas and legacy entity IDs |
| `CHUNK_ID = scripts/content-validation.mjs#75-115#73079ad3`<br>[[F:scripts/content-validation.mjs#75-115#73079ad3]] | Trophies and backward references |
| `CHUNK_ID = scripts/content-validation.mjs#117-162#73079ad3`<br>[[F:scripts/content-validation.mjs#117-162#73079ad3]] | Compendium and adventure references |
| `CHUNK_ID = scripts/content-validation.mjs#164-204#73079ad3`<br>[[F:scripts/content-validation.mjs#164-204#73079ad3]] | Checkpoint/registry invariants |
| `CHUNK_ID = scripts/content-validation.mjs#206-240#73079ad3`<br>[[F:scripts/content-validation.mjs#206-240#73079ad3]] | Validation orchestration |
| `CHUNK_ID = scripts/build-content.mjs#1-93#743fd6b7`<br>[[F:scripts/build-content.mjs#1-93#743fd6b7]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/angular.json#1-80#80bb5381`<br>[[F:web/angular.json#1-80#80bb5381]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = .github/workflows/ci.yml#1-53#5a791563`<br>[[F:.github/workflows/ci.yml#1-53#5a791563]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/content/content.models.ts#1-305#f9b077f9`<br>[[F:web/src/app/core/content/content.models.ts#1-305#f9b077f9]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/ngsw-config.json#1-56#b18c1ffe`<br>[[F:web/ngsw-config.json#1-56#b18c1ffe]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/public/_headers#1-16#55301e37`<br>[[F:web/public/_headers#1-16#55301e37]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/ui/how-it-works/how-it-works.ts#1-41#87abdc7e`<br>[[F:web/src/app/ui/how-it-works/how-it-works.ts#1-41#87abdc7e]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/e2e/offline.e2e.ts#1-40#841a8e9e`<br>[[F:web/e2e/offline.e2e.ts#1-40#841a8e9e]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/pwa/app-update.service.spec.ts#1-51#d7a4baba`<br>[[F:web/src/app/core/pwa/app-update.service.spec.ts#1-51#d7a4baba]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = docs/deploy.md#1-62#05b96177`<br>[[F:docs/deploy.md#1-62#05b96177]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/site.config.ts#1-71#a66d4ee2`<br>[[F:web/src/app/site.config.ts#1-71#a66d4ee2]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/ui/report-link/report-link.ts#1-70#750cfea3`<br>[[F:web/src/app/ui/report-link/report-link.ts#1-70#750cfea3]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/ui/name-fix/name-fix.ts#1-74#0e71b9b8`<br>[[F:web/src/app/ui/name-fix/name-fix.ts#1-74#0e71b9b8]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/pages/checklist/checklist.html#1-171#daa88fa0`<br>[[F:web/src/app/pages/checklist/checklist.html#1-171#daa88fa0]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/pages/item-detail/item-detail.html#1-131#d6b4a5d8`<br>[[F:web/src/app/pages/item-detail/item-detail.html#1-131#d6b4a5d8]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/pages/boss-detail/boss-detail.html#1-55#934dc570`<br>[[F:web/src/app/pages/boss-detail/boss-detail.html#1-55#934dc570]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/compendium/plan.ts#1-86#8236d6c9`<br>[[F:web/src/app/core/compendium/plan.ts#1-86#8236d6c9]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/pages/compendium/compendium.ts#1-170#c157defa`<br>[[F:web/src/app/pages/compendium/compendium.ts#1-170#c157defa]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/pages/search/search.ts#1-55#98fffab4`<br>[[F:web/src/app/pages/search/search.ts#1-55#98fffab4]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/e2e/library.e2e.ts#1-47#9bbd5bd3`<br>[[F:web/e2e/library.e2e.ts#1-47#9bbd5bd3]] | Component or configuration contract; see Phase 2 citations |
| `CHUNK_ID = web/src/app/core/i18n/transloco-http-loader.ts#1-13#2621dfc5`<br>[[F:web/src/app/core/i18n/transloco-http-loader.ts#1-13#2621dfc5]] | Component or configuration contract; see Phase 2 citations |

## Checks and scope

- Existing 50 Phase 1 anchors retained and checked against the current files.
- Phase 2 source anchors and next-read chunk hashes checked against the current files.
- Four Mermaid sources match the diagrams embedded in the master document.
- No application code or authored game content changed; no application tests executed.
- Source-derived failure consequences are distinguished from runtime hypotheses in section 2.6.

**Decisions/Findings:** architectural source evidence recorded. **Open Questions:** runtime hypotheses remain in the master state block. **Next Steps:** Phase 3 feature analysis.
