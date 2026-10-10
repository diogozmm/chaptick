# Structured item instructions

## Content contract

`content/schema/chapter.schema.json` validates the optional `Item.guidance` object. The TypeScript counterpart is `ItemGuidance` in `web/src/app/core/content/content.models.ts`.

| Field | Meaning | Shape |
| --- | --- | --- |
| `overview` | General explanation, without repeating categorized information | Localized text |
| `requirements` | Prerequisites such as a party member or friendship threshold | Localized text array |
| `preparation` | Equipment or supplies to prepare before starting | Localized text array |
| `warnings` | Deadlines, failure conditions, irreversible consequences | Localized text array |
| `rewards` | Rewards and their bonus conditions | Localized text array |
| `optional` | Actions that are not required to complete the item | Localized text array |
| `alternatives` | Conditional paths; each has `condition` and `instructions` | Array of objects |

Localized text requires `en`; `pt` is supported and should be supplied when authoring bilingual content. Omit unused fields; empty guidance objects, empty lists and unknown fields are invalid.

`hint` remains required as the checklist summary and fallback for older clients. Keep it consistent with guidance, and keep level-2 hints safe without revealing the item. Guidance is explicit data: the application does not guess categories from punctuation or English/Portuguese labels.

## Progress and visibility

Only the existing top-level `steps` array contributes to route completion. Its persisted keys are `<itemId>#step-<n>`, with one-based positions. Never reorder or remove published steps to move advice into another category. All migrated step arrays and item IDs remain unchanged.

Optional actions and alternative branches have no checkboxes and do not block completion. `availableUntil` still controls the actual deadline logic; a warning is explanatory text, not a replacement for the checkpoint reference.

`web/src/app/pages/item-detail/item-detail.html` shows guidance only when both the hint and the item name may be shown. Before revealing a level-2 item, the safe legacy hint remains visible and all guidance stays hidden. Items without guidance retain the existing hint presentation.

`web/src/app/ui/item-guidance/item-guidance.ts` renders overview, warnings, requirements and preparation before the route, with optional actions, rewards and conditional paths after it. All text uses Angular interpolation, not HTML parsing.

## Authoring

`Chapter.item(..., guidance=...)` in `scripts/authoring/lib.py` accepts explicit structured guidance. FC's quest and bonus helpers forward this argument. WTE's task, treasure-map and adventure builders populate guidance directly from their structured source data. Keep the JSON and its authoring source synchronized.

Example, alongside the existing `hint` and optional top-level `steps`:

```json
{
  "guidance": {
    "requirements": [{ "en": "Kloe must be in the party.", "pt": "Kloe precisa estar na equipe." }],
    "preparation": [{ "en": "Equip Freeze protection.", "pt": "Equipe proteção contra Freeze." }],
    "rewards": [{ "en": "+4 BP.", "pt": "+4 BP." }],
    "alternatives": [
      {
        "condition": { "en": "With Agate", "pt": "Com Agate" },
        "instructions": [{ "en": "Choose the first option.", "pt": "Escolha a primeira opção." }]
      }
    ]
  }
}
```

## Validation

- Root: `npm run test:content` and `npm run content:build` validate the schema and generate automatic cache revisions.
- In `web/`: `npm run e2e -- e2e/guidance.e2e.ts e2e/detail.e2e.ts e2e/route.e2e.ts` verifies rendering, language switching, spoiler gates, progress and legacy fallback.
- `web/e2e/a11y.e2e.ts` checks accessibility in both themes; `npm run e2e:content-update` exercises the real service worker across content deployments.

Future content can adopt guidance incrementally. Short, unambiguous legacy hints do not need artificial categorization.

## Remaining-hint review

The second editorial pass reviewed all 277 items that still used only `hint`. It added guidance to 112: FC 28, SC 31, WTE 1, Ys X 52. The catalog now has 315 structured entries; 165 retain concise directions, simple acquisition conditions, or supplementary navigation notes for existing step lists.

The additions separate one-time-visit warnings, monster-chest preparation, bonus conditions, fallback purchases and rewards. Ys X's Red Crest uses conditional branches rather than additional required steps. WTE's marriage entry separates the warning about consuming the daily gift from its overview.

This pass only added guidance. Existing hints, step arrays, item IDs, deadlines, sources and previously authored guidance were preserved. A read-only regeneration of the affected Python authoring sources was compared against the chapter JSON, including WTE's marriage builder. Both languages remain present; there is no runtime categorization of text.
