# Phase 3 evidence and continuation ledger

INDEX_VERSION: phase3-v1. This ledger records feature source contracts and inspected test evidence. SHA-256 hashes cover the whole file; ranges locate the relevant unit. Small files are anchored whole; large templates/test groups have semantic chunks. Source inspection does not imply test execution. Previously traced shared services are reused from Phase 2.

| CHUNK_ID / stable anchor | Feature evidence |
| --- | --- |
| `CHUNK_ID = web/src/app/app.routes.ts#1-44#e267f9dc`<br>[[F:web/src/app/app.routes.ts#1-44#e267f9dc]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/checklist/checklist.ts#1-150#650d02a5`<br>[[F:web/src/app/pages/checklist/checklist.ts#1-150#650d02a5]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/where/where.ts#1-52#b4433bd6`<br>[[F:web/src/app/pages/where/where.ts#1-52#b4433bd6]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/spoiler/chapter-access.ts#1-49#2984dc74`<br>[[F:web/src/app/core/spoiler/chapter-access.ts#1-49#2984dc74]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/progress/progress.models.ts#1-31#7c470eb1`<br>[[F:web/src/app/core/progress/progress.models.ts#1-31#7c470eb1]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/route/route.ts#1-28#0a907cff`<br>[[F:web/src/app/core/route/route.ts#1-28#0a907cff]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/collections/collections.ts#1-84#b1061ea1`<br>[[F:web/src/app/core/collections/collections.ts#1-84#b1061ea1]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/game/saved-games.ts#1-68#717ce3e9`<br>[[F:web/src/app/core/game/saved-games.ts#1-68#717ce3e9]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/spoiler/reveal.service.ts#1-15#a59bed00`<br>[[F:web/src/app/core/spoiler/reveal.service.ts#1-15#a59bed00]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/season-calendar/season-calendar.ts#1-43#afd6fb60`<br>[[F:web/src/app/ui/season-calendar/season-calendar.ts#1-43#afd6fb60]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/home/home.ts#1-157#6f011515`<br>[[F:web/src/app/pages/home/home.ts#1-157#6f011515]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/home/home.html#1-56#948ebd7a`<br>[[F:web/src/app/pages/home/home.html#1-56#948ebd7a]] | Import confirmation, introduction and game search |
| `CHUNK_ID = web/src/app/pages/home/home.html#57-134#948ebd7a`<br>[[F:web/src/app/pages/home/home.html#57-134#948ebd7a]] | Content result labels and show-more behavior |
| `CHUNK_ID = web/src/app/pages/home/home.html#135-189#948ebd7a`<br>[[F:web/src/app/pages/home/home.html#135-189#948ebd7a]] | Resume summaries and initial game grid |
| `CHUNK_ID = web/src/app/pages/library/library.ts#1-55#5876287f`<br>[[F:web/src/app/pages/library/library.ts#1-55#5876287f]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/library/library.html#1-79#aaefeca9`<br>[[F:web/src/app/pages/library/library.html#1-79#aaefeca9]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/game-card/game-card.ts#1-65#eb30a6c2`<br>[[F:web/src/app/ui/game-card/game-card.ts#1-65#eb30a6c2]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/progress/progress.store.ts#1-60#08adcc2a`<br>[[F:web/src/app/core/progress/progress.store.ts#1-60#08adcc2a]] | Active state and load |
| `CHUNK_ID = web/src/app/core/progress/progress.store.ts#62-120#08adcc2a`<br>[[F:web/src/app/core/progress/progress.store.ts#62-120#08adcc2a]] | Mutations and exports/import |
| `CHUNK_ID = web/src/app/core/progress/progress.store.ts#122-160#08adcc2a`<br>[[F:web/src/app/core/progress/progress.store.ts#122-160#08adcc2a]] | Queue and storage retention |
| `CHUNK_ID = web/src/app/core/progress/progress.store.ts#162-202#08adcc2a`<br>[[F:web/src/app/core/progress/progress.store.ts#162-202#08adcc2a]] | Parser and initial-pick predicate |
| `CHUNK_ID = web/e2e/home.e2e.ts#1-64#fd3f84cf`<br>[[F:web/e2e/home.e2e.ts#1-64#fd3f84cf]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/library.e2e.ts#1-47#9bbd5bd3`<br>[[F:web/e2e/library.e2e.ts#1-47#9bbd5bd3]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/where/where.html#1-73#c259abf7`<br>[[F:web/src/app/pages/where/where.html#1-73#c259abf7]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/advance-confirm/advance-confirm.ts#1-58#2ecb6b37`<br>[[F:web/src/app/ui/advance-confirm/advance-confirm.ts#1-58#2ecb6b37]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/advance-confirm/advance-confirm.html#1-18#ac58a00a`<br>[[F:web/src/app/ui/advance-confirm/advance-confirm.html#1-18#ac58a00a]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/spoiler/spoiler.ts#1-106#a8bfec27`<br>[[F:web/src/app/core/spoiler/spoiler.ts#1-106#a8bfec27]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/how-it-works/how-it-works.ts#1-41#87abdc7e`<br>[[F:web/src/app/ui/how-it-works/how-it-works.ts#1-41#87abdc7e]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/onboarding.e2e.ts#1-33#6a54fd9d`<br>[[F:web/e2e/onboarding.e2e.ts#1-33#6a54fd9d]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/advance.e2e.ts#1-62#edf573f5`<br>[[F:web/e2e/advance.e2e.ts#1-62#edf573f5]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = scripts/authoring/trophies.py#1-90#2a15c270`<br>[[F:scripts/authoring/trophies.py#1-90#2a15c270]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/checklist/checklist.html#1-83#daa88fa0`<br>[[F:web/src/app/pages/checklist/checklist.html#1-83#daa88fa0]] | Counts, capabilities, alerts and earlier items |
| `CHUNK_ID = web/src/app/pages/checklist/checklist.html#84-144#daa88fa0`<br>[[F:web/src/app/pages/checklist/checklist.html#84-144#daa88fa0]] | Filters, item groups and boss section |
| `CHUNK_ID = web/src/app/pages/checklist/checklist.html#145-171#daa88fa0`<br>[[F:web/src/app/pages/checklist/checklist.html#145-171#daa88fa0]] | Advance action and fetch error states |
| `CHUNK_ID = web/src/app/ui/item-row/item-row.ts#1-44#e75ac379`<br>[[F:web/src/app/ui/item-row/item-row.ts#1-44#e75ac379]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/item-row/item-row.html#1-50#df909570`<br>[[F:web/src/app/ui/item-row/item-row.html#1-50#df909570]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/route-steps/route-steps.ts#1-74#168e55ff`<br>[[F:web/src/app/ui/route-steps/route-steps.ts#1-74#168e55ff]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/spoiler/item-view.ts#1-59#7decc034`<br>[[F:web/src/app/core/spoiler/item-view.ts#1-59#7decc034]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = scripts/authoring/lib.py#1-110#f6aff8c5`<br>[[F:scripts/authoring/lib.py#1-110#f6aff8c5]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/checklist.e2e.ts#1-85#9382e083`<br>[[F:web/e2e/checklist.e2e.ts#1-85#9382e083]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/route.e2e.ts#1-26#ee24e987`<br>[[F:web/e2e/route.e2e.ts#1-26#ee24e987]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/trophies.e2e.ts#1-28#b8340eeb`<br>[[F:web/e2e/trophies.e2e.ts#1-28#b8340eeb]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/spoiler/deadlines.ts#1-50#ac968fe4`<br>[[F:web/src/app/core/spoiler/deadlines.ts#1-50#ac968fe4]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/spoiler/item-status.ts#1-36#afce8e20`<br>[[F:web/src/app/core/spoiler/item-status.ts#1-36#afce8e20]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/deadlines/deadlines.ts#1-45#cdb3f30a`<br>[[F:web/src/app/pages/deadlines/deadlines.ts#1-45#cdb3f30a]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/deadlines/deadlines.html#1-42#6d86c5fb`<br>[[F:web/src/app/pages/deadlines/deadlines.html#1-42#6d86c5fb]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/deadlines.e2e.ts#1-24#01574569`<br>[[F:web/e2e/deadlines.e2e.ts#1-24#01574569]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/item-detail/item-detail.ts#1-93#0cef4109`<br>[[F:web/src/app/pages/item-detail/item-detail.ts#1-93#0cef4109]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/item-detail/item-detail.html#1-65#d6b4a5d8`<br>[[F:web/src/app/pages/item-detail/item-detail.html#1-65#d6b4a5d8]] | Masks, facts, hints and trophy metadata |
| `CHUNK_ID = web/src/app/pages/item-detail/item-detail.html#66-131#d6b4a5d8`<br>[[F:web/src/app/pages/item-detail/item-detail.html#66-131#d6b4a5d8]] | Routes, bosses, community text, sources and navigation |
| `CHUNK_ID = web/src/app/pages/boss-detail/boss-detail.ts#1-58#15f54fbf`<br>[[F:web/src/app/pages/boss-detail/boss-detail.ts#1-58#15f54fbf]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/boss-detail/boss-detail.html#1-55#934dc570`<br>[[F:web/src/app/pages/boss-detail/boss-detail.html#1-55#934dc570]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = scripts/content-validation.mjs#48-115#73079ad3`<br>[[F:scripts/content-validation.mjs#48-115#73079ad3]] | Identity, trophy and boss/fish reference checks |
| `CHUNK_ID = scripts/content-validation.mjs#117-162#73079ad3`<br>[[F:scripts/content-validation.mjs#117-162#73079ad3]] | Compendium and adventure reference checks |
| `CHUNK_ID = scripts/content-validation.mjs#164-240#73079ad3`<br>[[F:scripts/content-validation.mjs#164-240#73079ad3]] | Checkpoint/history validation and orchestration |
| `CHUNK_ID = web/e2e/detail.e2e.ts#1-95#d642f8dd`<br>[[F:web/e2e/detail.e2e.ts#1-95#d642f8dd]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/collections.e2e.ts#1-80#40909e82`<br>[[F:web/e2e/collections.e2e.ts#1-80#40909e82]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/collections/collections.ts#1-97#96827ab3`<br>[[F:web/src/app/pages/collections/collections.ts#1-97#96827ab3]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/collections/collections.html#1-57#a947108c`<br>[[F:web/src/app/pages/collections/collections.html#1-57#a947108c]] | Totals, tabs and trophies |
| `CHUNK_ID = web/src/app/pages/collections/collections.html#58-125#a947108c`<br>[[F:web/src/app/pages/collections/collections.html#58-125#a947108c]] | Fish/rank flags and spots |
| `CHUNK_ID = web/src/app/pages/collections/collections.html#126-164#a947108c`<br>[[F:web/src/app/pages/collections/collections.html#126-164#a947108c]] | Recipe completion and empty states |
| `CHUNK_ID = web/src/app/core/search/search.ts#1-80#81af4074`<br>[[F:web/src/app/core/search/search.ts#1-80#81af4074]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/search/global-search.ts#1-89#8f128d82`<br>[[F:web/src/app/core/search/global-search.ts#1-89#8f128d82]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/search/search.ts#1-55#98fffab4`<br>[[F:web/src/app/pages/search/search.ts#1-55#98fffab4]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/search/search.html#1-44#ab162ccb`<br>[[F:web/src/app/pages/search/search.html#1-44#ab162ccb]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/compendium/compendium.ts#1-158#e4871ad6`<br>[[F:web/src/app/core/compendium/compendium.ts#1-158#e4871ad6]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/compendium/compendium.ts#1-170#c157defa`<br>[[F:web/src/app/pages/compendium/compendium.ts#1-170#c157defa]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/fixtures/content/sc/chapters/ch-00.json#1-194#5c3797ad`<br>[[F:web/e2e/fixtures/content/sc/chapters/ch-00.json#1-194#5c3797ad]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/search.e2e.ts#1-30#bf3c6116`<br>[[F:web/e2e/search.e2e.ts#1-30#bf3c6116]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/compendium/compendium.spec.ts#1-82#693e8f4d`<br>[[F:web/src/app/core/compendium/compendium.spec.ts#1-82#693e8f4d]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/compendium/compendium.html#1-75#8b568638`<br>[[F:web/src/app/pages/compendium/compendium.html#1-75#8b568638]] | Entry browse/query/category/results |
| `CHUNK_ID = web/src/app/pages/compendium/compendium.html#76-147#8b568638`<br>[[F:web/src/app/pages/compendium/compendium.html#76-147#8b568638]] | Craft tracking, ingredients and plans |
| `CHUNK_ID = web/src/app/pages/compendium/compendium.html#148-215#8b568638`<br>[[F:web/src/app/pages/compendium/compendium.html#148-215#8b568638]] | Villagers, gifts and adventures |
| `CHUNK_ID = web/src/app/pages/compendium/compendium.html#216-318#8b568638`<br>[[F:web/src/app/pages/compendium/compendium.html#216-318#8b568638]] | Seasons, calendar and planting |
| `CHUNK_ID = web/src/app/pages/compendium/compendium.html#319-390#8b568638`<br>[[F:web/src/app/pages/compendium/compendium.html#319-390#8b568638]] | Creature masks, seasonal row and gift links |
| `CHUNK_ID = web/src/app/pages/entry/entry.ts#1-94#9eaa2033`<br>[[F:web/src/app/pages/entry/entry.ts#1-94#9eaa2033]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/entry/entry.html#1-76#6e3b1447`<br>[[F:web/src/app/pages/entry/entry.html#1-76#6e3b1447]] | Names, equipment and planting |
| `CHUNK_ID = web/src/app/pages/entry/entry.html#77-143#6e3b1447`<br>[[F:web/src/app/pages/entry/entry.html#77-143#6e3b1447]] | Acquisition, madeBy and usedIn links |
| `CHUNK_ID = web/src/app/pages/entry/entry.html#144-186#6e3b1447`<br>[[F:web/src/app/pages/entry/entry.html#144-186#6e3b1447]] | Gifts, creatures, wiki and missing entry |
| `CHUNK_ID = web/e2e/compendium.e2e.ts#1-79#ff155b55`<br>[[F:web/e2e/compendium.e2e.ts#1-79#ff155b55]] | Capabilities, reached data, creatures and made flags |
| `CHUNK_ID = web/e2e/compendium.e2e.ts#81-133#ff155b55`<br>[[F:web/e2e/compendium.e2e.ts#81-133#ff155b55]] | Seasons, equipment and planner |
| `CHUNK_ID = web/e2e/compendium.e2e.ts#135-204#ff155b55`<br>[[F:web/e2e/compendium.e2e.ts#135-204#ff155b55]] | Gifts, names, calendar and friendship |
| `CHUNK_ID = web/src/app/pages/plan/plan.ts#1-97#c5fe1300`<br>[[F:web/src/app/pages/plan/plan.ts#1-97#c5fe1300]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/plan/plan.html#1-99#1674abd6`<br>[[F:web/src/app/pages/plan/plan.html#1-99#1674abd6]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/compendium/plan.ts#1-86#8236d6c9`<br>[[F:web/src/app/core/compendium/plan.ts#1-86#8236d6c9]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/compendium/plan.spec.ts#1-63#419684ee`<br>[[F:web/src/app/core/compendium/plan.spec.ts#1-63#419684ee]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/creature/creature.html#1-38#e3538e60`<br>[[F:web/src/app/pages/creature/creature.html#1-38#e3538e60]] | Heading-only reveal, editor, notes and places |
| `CHUNK_ID = web/src/app/pages/creature/creature.html#39-105#e3538e60`<br>[[F:web/src/app/pages/creature/creature.html#39-105#e3538e60]] | Steal and encounter rewards |
| `CHUNK_ID = web/src/app/pages/creature/creature.html#106-155#e3538e60`<br>[[F:web/src/app/pages/creature/creature.html#106-155#e3538e60]] | Loot pools and not-found/loading states |
| `CHUNK_ID = web/src/app/pages/creature/creature.ts#1-57#dd004a2b`<br>[[F:web/src/app/pages/creature/creature.ts#1-57#dd004a2b]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/name-fix/name-fix.ts#1-74#0e71b9b8`<br>[[F:web/src/app/ui/name-fix/name-fix.ts#1-74#0e71b9b8]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/compendium/seasons.ts#1-90#24b2b832`<br>[[F:web/src/app/core/compendium/seasons.ts#1-90#24b2b832]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/season-calendar/season-calendar.html#1-73#26f01f52`<br>[[F:web/src/app/ui/season-calendar/season-calendar.html#1-73#26f01f52]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = scripts/build-content.mjs#1-93#743fd6b7`<br>[[F:scripts/build-content.mjs#1-93#743fd6b7]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/compendium/seasons.spec.ts#1-71#90595acb`<br>[[F:web/src/app/core/compendium/seasons.spec.ts#1-71#90595acb]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/content/content.models.ts#1-305#f9b077f9`<br>[[F:web/src/app/core/content/content.models.ts#1-305#f9b077f9]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/app.ts#1-34#7cffa631`<br>[[F:web/src/app/app.ts#1-34#7cffa631]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/i18n/lang.service.ts#1-41#ba519d52`<br>[[F:web/src/app/core/i18n/lang.service.ts#1-41#ba519d52]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/i18n/game-name.pipe.ts#1-14#127e51c8`<br>[[F:web/src/app/core/i18n/game-name.pipe.ts#1-14#127e51c8]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/i18n/original.pipe.ts#1-14#9a02a13f`<br>[[F:web/src/app/core/i18n/original.pipe.ts#1-14#9a02a13f]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/name-fix/name-fix.html#1-37#cd54f48b`<br>[[F:web/src/app/ui/name-fix/name-fix.html#1-37#cd54f48b]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/ui/report-link/report-link.ts#1-70#750cfea3`<br>[[F:web/src/app/ui/report-link/report-link.ts#1-70#750cfea3]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/progress/progress.store.spec.ts#1-88#da683cb8`<br>[[F:web/src/app/core/progress/progress.store.spec.ts#1-88#da683cb8]] | Picking, names, persistence and per-game isolation |
| `CHUNK_ID = web/src/app/core/progress/progress.store.spec.ts#90-142#da683cb8`<br>[[F:web/src/app/core/progress/progress.store.spec.ts#90-142#da683cb8]] | Round trips, format failures and storage retention |
| `CHUNK_ID = web/src/app/core/progress/progress.repository.ts#1-33#510c21ae`<br>[[F:web/src/app/core/progress/progress.repository.ts#1-33#510c21ae]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/progress/transfer.service.ts#1-53#5bf5a484`<br>[[F:web/src/app/core/progress/transfer.service.ts#1-53#5bf5a484]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/progress/transfer-link.ts#1-54#f4d083dd`<br>[[F:web/src/app/core/progress/transfer-link.ts#1-54#f4d083dd]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/backup/backup.ts#1-89#b867ff84`<br>[[F:web/src/app/pages/backup/backup.ts#1-89#b867ff84]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/backup/backup.html#1-40#233e896c`<br>[[F:web/src/app/pages/backup/backup.html#1-40#233e896c]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/app.html#1-59#af16d33d`<br>[[F:web/src/app/app.html#1-59#af16d33d]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/site.config.ts#1-71#a66d4ee2`<br>[[F:web/src/app/site.config.ts#1-71#a66d4ee2]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/transfer.e2e.ts#1-34#2bfe3f96`<br>[[F:web/e2e/transfer.e2e.ts#1-34#2bfe3f96]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/transfer-link.e2e.ts#1-40#433f8d2e`<br>[[F:web/e2e/transfer-link.e2e.ts#1-40#433f8d2e]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/offline.e2e.ts#1-40#841a8e9e`<br>[[F:web/e2e/offline.e2e.ts#1-40#841a8e9e]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/e2e/a11y.e2e.ts#1-17#47bbf202`<br>[[F:web/e2e/a11y.e2e.ts#1-17#47bbf202]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/app.config.ts#1-48#1b1fe1f8`<br>[[F:web/src/app/app.config.ts#1-48#1b1fe1f8]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/ngsw-config.json#1-56#b18c1ffe`<br>[[F:web/ngsw-config.json#1-56#b18c1ffe]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/pwa/app-update.service.ts#1-59#3f7fc6a1`<br>[[F:web/src/app/core/pwa/app-update.service.ts#1-59#3f7fc6a1]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/credits/credits.ts#1-61#744a49f6`<br>[[F:web/src/app/pages/credits/credits.ts#1-61#744a49f6]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/pages/privacy/privacy.ts#1-26#a0b82e9d`<br>[[F:web/src/app/pages/privacy/privacy.ts#1-26#a0b82e9d]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = web/src/app/core/pwa/app-update.service.spec.ts#1-51#d7a4baba`<br>[[F:web/src/app/core/pwa/app-update.service.spec.ts#1-51#d7a4baba]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = content/franchises.json#1-55#e3bbe919`<br>[[F:content/franchises.json#1-55#e3bbe919]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = scripts/authoring/wte-ids.json#1-85#6520c44d`<br>[[F:scripts/authoring/wte-ids.json#1-85#6520c44d]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = CONTRIBUTING.md#1-58#a34991a3`<br>[[F:CONTRIBUTING.md#1-58#a34991a3]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = docs/deploy.md#1-62#05b96177`<br>[[F:docs/deploy.md#1-62#05b96177]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = scripts/validate-content.mjs#1-28#62ee223c`<br>[[F:scripts/validate-content.mjs#1-28#62ee223c]] | Feature contract / regression source cited in Phase 3 |
| `CHUNK_ID = scripts/authoring/wte.py#1-45#9e89cd08`<br>[[F:scripts/authoring/wte.py#1-45#9e89cd08]] | Generator source prerequisites and stale stateless-ID comment |
| `CHUNK_ID = scripts/authoring/wte.py#1089-1150#9e89cd08`<br>[[F:scripts/authoring/wte.py#1089-1150#9e89cd08]] | Build placement, dependency settlement and stable checklist allocation |
| `CHUNK_ID = scripts/authoring/wte.py#1220-1282#9e89cd08`<br>[[F:scripts/authoring/wte.py#1220-1282#9e89cd08]] | Reference pruning and source/report output |
| `CHUNK_ID = tests/content-validation.test.mjs#1-126#19ba1aae`<br>[[F:tests/content-validation.test.mjs#1-126#19ba1aae]] | Feature contract / regression source cited in Phase 3 |

## Source-data spot checks

- Parsed the authored chapters to count creature spoiler levels: all 113 current WTE creatures are level 0; other authored games have no creature records. This limits current impact of the creature-detail mask gap, not the behavior of the template.
- Parsed checklist levels: SC contains two level-2 items; other authored games contain none at this snapshot.
- Inspected fixture `web/e2e/fixtures/content/sc/chapters/ch-00.json`: `sc-ch0-mi-01` is level 2 with name “Very Secret” and safe hint “Safe hint.” The proposed home-search regression is documented but not executed.

The data-file anchors below identify the snapshots used for the field-count checks, not a full content or game-fact review.

- [[F:content/wte/chapters/ch-00.json#1-12#a30d7591]]
- [[F:content/wte/chapters/ch-01.json#1-12#dfe78cb3]]
- [[F:content/wte/chapters/ch-02.json#1-12#80e862fc]]
- [[F:content/wte/chapters/ch-03.json#1-12#5ae25ded]]
- [[F:content/wte/chapters/ch-04.json#1-12#6a30a24b]]
- [[F:content/sc/chapters/ch-00.json#1-12#04f5c7ff]]
- [[F:content/sc/chapters/ch-01.json#1-12#424b4c75]]
- [[F:content/sc/chapters/ch-02.json#1-12#923e82c3]]
- [[F:content/sc/chapters/ch-03.json#1-12#f9b703f5]]
- [[F:content/sc/chapters/ch-04.json#1-12#975778bd]]
- [[F:content/sc/chapters/ch-05.json#1-12#c11ad30c]]
- [[F:content/sc/chapters/ch-06.json#1-12#eff47f0f]]
- [[F:content/sc/chapters/ch-07.json#1-12#5fd059c6]]

**Decisions/Findings:** all routed feature families and their principal shared behaviors are documented. **Open Questions:** source-confirmed discrepancies still require coding-task regressions; no tests were run. **Next Steps:** Phase 4 risk consolidation.
