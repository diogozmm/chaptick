# Historical Phase 1 continuation state

## STATE BLOCK

```yaml
INDEX_VERSION: phase1-v1
PHASE_STATUS: Phase 1 complete; Phases 2–6 pending
FILE_MAP_SUMMARY: first 50 prioritized entries in codebase-analysis-docs/assets/FILE_INDEX.md
COMPLETED:
  - Tracked-file inventory and language/config/test classification
  - Bootstrap, content-loading, progression and storage backbone scan
  - Feature/business-purpose overview and interaction summary
  - Source-derived game coverage counts and selected E2E evidence
OPEN_QUESTIONS:
  - Are resource keys sufficient when switching games at the same chapter order?
  - Do all search/detail consumers preserve masking and access after moving backward?
  - How do storage errors and partial multi-game imports recover?
  - How are SW updates, cache eviction and offline failures surfaced?
  - Which schema cross-references and authoring workflows constrain extensions?
KNOWN_RISKS:
  - README scope is stale; SC examples are not universal
  - IDs and save/content versions are compatibility boundaries
  - Low-level fetch helpers trust callers for spoiler access
  - Device/origin-local progress needs explicit transfer
  - Python authoring may replace existing content collections
GLOSSARY_DELTA:
  - franchise, chapter/area, manifest, checkpoint, item, entry, craft
  - collection, spoiler level, progress, data version
VALIDATION: documentation references and inventory only; app tests not run
```

### NEXT_READ_QUEUE

Proceed only when Phase 2 is requested. Read bounded chunks around named functions; use `PATH#START-END#HASH8` labels for continuation notes. Read queue focuses on unresolved interactions rather than repeating the whole initial scan:

- `web/src/app/app.ts#1-34#7cffa631` — start here, then continue on function boundaries.
- `web/src/app/core/game/saved-games.ts#1-68#717ce3e9` — start here, then continue on function boundaries.
- `web/src/app/core/spoiler/spoiler.ts#1-80#a8bfec27` — start here, then continue on function boundaries.
- `web/src/app/core/spoiler/item-view.ts#1-59#7decc034` — start here, then continue on function boundaries.
- `web/src/app/core/spoiler/reveal.service.ts#1-15#a59bed00` — start here, then continue on function boundaries.
- `web/src/app/core/search/global-search.ts#1-80#8f128d82` — start here, then continue on function boundaries.
- `web/src/app/core/compendium/compendium.ts#1-80#e4871ad6` — start here, then continue on function boundaries.
- `web/src/app/core/compendium/plan.ts#1-80#8236d6c9` — start here, then continue on function boundaries.
- `web/src/app/core/pwa/app-update.service.ts#1-59#3f7fc6a1` — start here, then continue on function boundaries.
- `scripts/content-validation.mjs#1-80#73079ad3` — start here, then continue on function boundaries.
- `web/e2e/offline.e2e.ts#1-40#841a8e9e` — start here, then continue on function boundaries.

