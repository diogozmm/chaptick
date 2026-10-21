# Historical Phase 2 continuation state

## STATE BLOCK

```yaml
INDEX_VERSION: phase2-v1
PHASE_STATUS: Phases 1–2 complete; Phases 3–6 pending
FILE_MAP_SUMMARY: top 50 baseline priorities in codebase-analysis-docs/assets/FILE_INDEX.md
PHASE2_EVIDENCE: codebase-analysis-docs/assets/PHASE2_EVIDENCE.md
HISTORICAL_STATE: codebase-analysis-docs/assets/PHASE1_STATE.md
COMPLETED:
  - Runtime component map and static content build boundary
  - Chapter read, progress write, global search and transfer flows
  - State ownership, caching, updates, integrations and error handling
  - Four Mermaid diagrams and source-anchored architectural findings
OPEN_QUESTIONS:
  - Same-session same-order game switches with reused aggregate components
  - Storage-failure UX, partial import recovery and reload during pending writes
  - Full feature-level masking after backward progression
  - Detailed authoring/schema constraints and remaining feature edge cases
KNOWN_RISKS:
  - Registry validation excludes compendium entities
  - Rejected save promise blocks subsequent queued persistence
  - Loaded chapters persist after backward selection
  - ItemView.deadline can use a cached checkpoint beyond current order
  - Aggregate resource keys omit explicit active-game identity
  - Import preference values lack nested type validation
GLOSSARY_DELTA:
  - reached-content index: derived graph built from permitted chapter payloads
  - synthetic completion ID: step or rank marker stored alongside entity IDs
  - freshness/performance caches: independent SW policies for metadata/chapter data
  - optimistic persistence: signal update precedes durable write completion
VALIDATION: source tracing and documentation checks; application tests not run
```

### NEXT_READ_QUEUE

Proceed with Phase 3 when requested. Inspect complete feature entry points, templates and corresponding tests; retain Phase 2 architecture as the shared context. Initial chunks follow; continue on function/template boundaries.

- `web/src/app/pages/library/library.ts#1-55#5876287f`
- `web/src/app/pages/where/where.html#1-73#c259abf7`
- `web/src/app/pages/checklist/checklist.html#1-80#daa88fa0`
- `web/src/app/pages/item-detail/item-detail.ts#1-80#0cef4109`
- `web/src/app/pages/boss-detail/boss-detail.ts#1-58#15f54fbf`
- `web/src/app/ui/item-row/item-row.ts#1-44#e75ac379`
- `web/src/app/pages/deadlines/deadlines.ts#1-45#cdb3f30a`
- `web/src/app/pages/compendium/compendium.html#1-80#8b568638`
- `web/src/app/ui/season-calendar/season-calendar.ts#1-43#afd6fb60`
- `web/src/app/core/progress/progress.store.spec.ts#1-80#da683cb8`
- `tests/content-validation.test.mjs#1-80#19ba1aae`
- `scripts/authoring/lib.py#1-80#f6aff8c5`

