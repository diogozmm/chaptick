# FILE INDEX — phase3-v1

Tracked baseline: 258 files. Phases 2–3 retained the same source inventory and top-50 priorities; additional read evidence is recorded in `codebase-analysis-docs/assets/PHASE2_EVIDENCE.md` and `codebase-analysis-docs/assets/PHASE3_EVIDENCE.md`. SHA-256 first eight hex digits; lines count physical byte lines (not meaningful for binary assets). P0 backbone, P1 important feature/config/test, P2 supporting, P3 lockfiles/binaries. Indexing does not imply semantic review. Generated/vendor files excluded through Git inventory.

| # | PRIORITY | PATH | TYPE | LINES | HASH8 | NOTES |
| --- | --- | --- | --- | ---: | --- | --- |
| 1 | P0 | `README.md` | docs | 52 | `42920d8c` | First-read backbone |
| 2 | P0 | `package.json` | code/config | 14 | `a41dda20` | First-read backbone |
| 3 | P0 | `web/package.json` | code/config | 44 | `b7871879` | First-read backbone |
| 4 | P0 | `web/src/main.ts` | code/config | 6 | `2341253f` | First-read backbone |
| 5 | P0 | `web/src/app/app.config.ts` | code/config | 48 | `1b1fe1f8` | First-read backbone |
| 6 | P0 | `web/src/app/app.routes.ts` | code/config | 44 | `e267f9dc` | First-read backbone |
| 7 | P0 | `web/src/app/core/content/content.models.ts` | code/config | 305 | `f9b077f9` | First-read backbone |
| 8 | P0 | `web/src/app/core/content/content.service.ts` | code/config | 73 | `9f6c43a6` | First-read backbone |
| 9 | P0 | `web/src/app/core/game/active-game.ts` | code/config | 58 | `db79bed7` | First-read backbone |
| 10 | P0 | `web/src/app/core/spoiler/chapter-access.ts` | code/config | 49 | `2984dc74` | First-read backbone |
| 11 | P0 | `web/src/app/core/progress/progress.models.ts` | code/config | 31 | `7c470eb1` | First-read backbone |
| 12 | P0 | `web/src/app/core/progress/progress.repository.ts` | code/config | 33 | `510c21ae` | First-read backbone |
| 13 | P0 | `web/src/app/core/progress/progress.store.ts` | code/config | 202 | `08adcc2a` | First-read backbone |
| 14 | P0 | `scripts/build-content.mjs` | code/config | 93 | `743fd6b7` | First-read backbone |
| 15 | P0 | `scripts/content-validation.mjs` | code/config | 240 | `73079ad3` | First-read backbone |
| 16 | P0 | `scripts/validate-content.mjs` | code/config | 28 | `62ee223c` | First-read backbone |
| 17 | P0 | `content/schema/chapter.schema.json` | content | 1088 | `cf8fdc18` | First-read backbone |
| 18 | P0 | `content/schema/common.schema.json` | content | 16 | `bb963e28` | First-read backbone |
| 19 | P0 | `content/schema/game.schema.json` | content | 105 | `7eca35d3` | First-read backbone |
| 20 | P0 | `content/id-registry.json` | content | 915 | `dbaf17d4` | First-read backbone |
| 21 | P1 | `web/src/app/pages/home/home.ts` | code/config | 157 | `6f011515` | Phase 1 feature evidence / Phase 2 queue |
| 22 | P1 | `web/src/app/pages/checklist/checklist.ts` | code/config | 150 | `650d02a5` | Phase 1 feature evidence / Phase 2 queue |
| 23 | P1 | `web/src/app/pages/compendium/compendium.ts` | code/config | 170 | `c157defa` | Phase 1 feature evidence / Phase 2 queue |
| 24 | P1 | `web/src/app/pages/plan/plan.ts` | code/config | 97 | `c5fe1300` | Phase 1 feature evidence / Phase 2 queue |
| 25 | P1 | `web/src/app/pages/collections/collections.ts` | code/config | 97 | `96827ab3` | Phase 1 feature evidence / Phase 2 queue |
| 26 | P1 | `web/src/app/core/spoiler/spoiler.ts` | code/config | 106 | `a8bfec27` | Phase 1 feature evidence / Phase 2 queue |
| 27 | P1 | `web/src/app/core/spoiler/item-view.ts` | code/config | 59 | `7decc034` | Phase 1 feature evidence / Phase 2 queue |
| 28 | P1 | `web/src/app/core/search/global-search.ts` | code/config | 89 | `8f128d82` | Phase 1 feature evidence / Phase 2 queue |
| 29 | P1 | `web/src/app/core/compendium/compendium.ts` | code/config | 158 | `e4871ad6` | Phase 1 feature evidence / Phase 2 queue |
| 30 | P1 | `web/src/app/core/compendium/plan.ts` | code/config | 86 | `8236d6c9` | Phase 1 feature evidence / Phase 2 queue |
| 31 | P1 | `web/src/app/core/compendium/seasons.ts` | code/config | 90 | `24b2b832` | Phase 1 feature evidence / Phase 2 queue |
| 32 | P1 | `web/src/app/core/progress/transfer.service.ts` | code/config | 53 | `5bf5a484` | Phase 1 feature evidence / Phase 2 queue |
| 33 | P1 | `web/src/app/core/progress/transfer-link.ts` | code/config | 54 | `f4d083dd` | Phase 1 feature evidence / Phase 2 queue |
| 34 | P1 | `web/src/app/core/analytics.service.ts` | code/config | 33 | `0c4afc66` | Phase 1 feature evidence / Phase 2 queue |
| 35 | P1 | `web/src/app/site.config.ts` | code/config | 71 | `a66d4ee2` | Phase 1 feature evidence / Phase 2 queue |
| 36 | P1 | `web/ngsw-config.json` | code/config | 56 | `b18c1ffe` | Phase 1 feature evidence / Phase 2 queue |
| 37 | P1 | `wrangler.jsonc` | code/config | 11 | `901ff326` | Phase 1 feature evidence / Phase 2 queue |
| 38 | P1 | `.github/workflows/ci.yml` | code/config | 53 | `5a791563` | Phase 1 feature evidence / Phase 2 queue |
| 39 | P1 | `web/playwright.config.ts` | code/config | 27 | `f006e389` | Phase 1 feature evidence / Phase 2 queue |
| 40 | P1 | `web/e2e/checklist.e2e.ts` | test | 85 | `9382e083` | Phase 1 feature evidence / Phase 2 queue |
| 41 | P1 | `web/e2e/compendium.e2e.ts` | test | 204 | `ff155b55` | Phase 1 feature evidence / Phase 2 queue |
| 42 | P1 | `web/e2e/offline.e2e.ts` | test | 40 | `841a8e9e` | Phase 1 feature evidence / Phase 2 queue |
| 43 | P1 | `tests/content-validation.test.mjs` | test | 126 | `19ba1aae` | Phase 1 feature evidence / Phase 2 queue |
| 44 | P1 | `CONTRIBUTING.md` | docs | 58 | `a34991a3` | Phase 1 feature evidence / Phase 2 queue |
| 45 | P1 | `docs/deploy.md` | docs | 62 | `05b96177` | Phase 1 feature evidence / Phase 2 queue |
| 46 | P1 | `content/fc/game.json` | content | 75 | `1d89d81b` | Phase 1 feature evidence / Phase 2 queue |
| 47 | P1 | `content/sc/game.json` | content | 67 | `2ee650e1` | Phase 1 feature evidence / Phase 2 queue |
| 48 | P1 | `content/wte/game.json` | content | 16 | `ced64b9e` | Phase 1 feature evidence / Phase 2 queue |
| 49 | P1 | `content/ysx/game.json` | content | 67 | `b1aa6cf1` | Phase 1 feature evidence / Phase 2 queue |
| 50 | P1 | `scripts/authoring/lib.py` | code/config | 110 | `f6aff8c5` | Phase 1 feature evidence / Phase 2 queue |
| 51 | P2 | `.github/ISSUE_TEMPLATE/item-correction.yml` | code/config | 21 | `c76ea861` | Inventory only; not necessarily read |
| 52 | P2 | `.github/ISSUE_TEMPLATE/name-correction.yml` | code/config | 24 | `42f41423` | Inventory only; not necessarily read |
| 53 | P2 | `.gitignore` | code/config | 10 | `05dc6460` | Inventory only; not necessarily read |
| 54 | P2 | `LICENSE` | code/config | 21 | `e8ce4307` | Inventory only; not necessarily read |
| 55 | P2 | `LICENSE-CONTENT` | code/config | 13 | `504444f3` | Inventory only; not necessarily read |
| 56 | P2 | `PRIVACY.md` | docs | 7 | `2c8d8382` | Inventory only; not necessarily read |
| 57 | P2 | `THIRD_PARTY_NOTICES.md` | docs | 55 | `5d8b7826` | Inventory only; not necessarily read |
| 58 | P2 | `content/fc/chapters/ch-00.json` | content | 1067 | `6580ec30` | Inventory only; not necessarily read |
| 59 | P2 | `content/fc/chapters/ch-01.json` | content | 1600 | `79a7f8ea` | Inventory only; not necessarily read |
| 60 | P2 | `content/fc/chapters/ch-02.json` | content | 1401 | `10f3d0b5` | Inventory only; not necessarily read |
| 61 | P2 | `content/fc/chapters/ch-03.json` | content | 1523 | `4a856711` | Inventory only; not necessarily read |
| 62 | P2 | `content/fc/chapters/ch-04.json` | content | 1564 | `17efa9f3` | Inventory only; not necessarily read |
| 63 | P2 | `content/franchises.json` | content | 55 | `e3bbe919` | Inventory only; not necessarily read |
| 64 | P2 | `content/sc/chapters/ch-00.json` | content | 699 | `04f5c7ff` | Inventory only; not necessarily read |
| 65 | P2 | `content/sc/chapters/ch-01.json` | content | 1366 | `424b4c75` | Inventory only; not necessarily read |
| 66 | P2 | `content/sc/chapters/ch-02.json` | content | 1449 | `923e82c3` | Inventory only; not necessarily read |
| 67 | P2 | `content/sc/chapters/ch-03.json` | content | 1262 | `f9b703f5` | Inventory only; not necessarily read |
| 68 | P2 | `content/sc/chapters/ch-04.json` | content | 1175 | `975778bd` | Inventory only; not necessarily read |
| 69 | P2 | `content/sc/chapters/ch-05.json` | content | 1228 | `c11ad30c` | Inventory only; not necessarily read |
| 70 | P2 | `content/sc/chapters/ch-06.json` | content | 548 | `eff47f0f` | Inventory only; not necessarily read |
| 71 | P2 | `content/sc/chapters/ch-07.json` | content | 726 | `5fd059c6` | Inventory only; not necessarily read |
| 72 | P2 | `content/schema/franchises.schema.json` | content | 66 | `a0722952` | Inventory only; not necessarily read |
| 73 | P2 | `content/wte/chapters/ch-00.json` | content | 32543 | `a30d7591` | Inventory only; not necessarily read |
| 74 | P2 | `content/wte/chapters/ch-01.json` | content | 11135 | `dfe78cb3` | Inventory only; not necessarily read |
| 75 | P2 | `content/wte/chapters/ch-02.json` | content | 18739 | `80e862fc` | Inventory only; not necessarily read |
| 76 | P2 | `content/wte/chapters/ch-03.json` | content | 2247 | `5ae25ded` | Inventory only; not necessarily read |
| 77 | P2 | `content/wte/chapters/ch-04.json` | content | 10222 | `6a30a24b` | Inventory only; not necessarily read |
| 78 | P2 | `content/ysx/chapters/ch-00.json` | content | 32 | `adffe556` | Inventory only; not necessarily read |
| 79 | P2 | `content/ysx/chapters/ch-01.json` | content | 71 | `36a5271c` | Inventory only; not necessarily read |
| 80 | P2 | `content/ysx/chapters/ch-02.json` | content | 211 | `bcf7d31a` | Inventory only; not necessarily read |
| 81 | P2 | `content/ysx/chapters/ch-03.json` | content | 399 | `00658f48` | Inventory only; not necessarily read |
| 82 | P2 | `content/ysx/chapters/ch-04.json` | content | 890 | `ced432d6` | Inventory only; not necessarily read |
| 83 | P2 | `content/ysx/chapters/ch-05.json` | content | 1481 | `92d7bbbc` | Inventory only; not necessarily read |
| 84 | P2 | `content/ysx/chapters/ch-06.json` | content | 856 | `cb622044` | Inventory only; not necessarily read |
| 85 | P2 | `content/ysx/chapters/ch-07.json` | content | 641 | `bef49a5e` | Inventory only; not necessarily read |
| 86 | P2 | `content/ysx/chapters/ch-08.json` | content | 358 | `f8d74667` | Inventory only; not necessarily read |
| 87 | P2 | `content/ysx/chapters/ch-09.json` | content | 824 | `b4baddcf` | Inventory only; not necessarily read |
| 88 | P2 | `content/ysx/chapters/ch-10.json` | content | 884 | `2e2b5a5f` | Inventory only; not necessarily read |
| 89 | P2 | `content/ysx/chapters/ch-11.json` | content | 84 | `3c8e2329` | Inventory only; not necessarily read |
| 90 | P3 | `package-lock.json` | code/config | 90 | `2fc478b7` | Inventory only; not necessarily read |
| 91 | P2 | `scripts/authoring/ch0.py` | code/config | 61 | `6acac105` | Inventory only; not necessarily read |
| 92 | P2 | `scripts/authoring/ch1.py` | code/config | 241 | `ccbce44b` | Inventory only; not necessarily read |
| 93 | P2 | `scripts/authoring/ch2.py` | code/config | 238 | `decd01d9` | Inventory only; not necessarily read |
| 94 | P2 | `scripts/authoring/ch3.py` | code/config | 224 | `53081e3d` | Inventory only; not necessarily read |
| 95 | P2 | `scripts/authoring/ch4.py` | code/config | 225 | `467ff059` | Inventory only; not necessarily read |
| 96 | P2 | `scripts/authoring/ch5.py` | code/config | 217 | `d45f1a24` | Inventory only; not necessarily read |
| 97 | P2 | `scripts/authoring/ch6.py` | code/config | 111 | `5d1a92a7` | Inventory only; not necessarily read |
| 98 | P2 | `scripts/authoring/ch7.py` | code/config | 132 | `fe4a3c6b` | Inventory only; not necessarily read |
| 99 | P2 | `scripts/authoring/fc.py` | code/config | 726 | `f758aa58` | Inventory only; not necessarily read |
| 100 | P2 | `scripts/authoring/fc_chests.py` | code/config | 216 | `cb3706bb` | Inventory only; not necessarily read |
| 101 | P2 | `scripts/authoring/trophies.py` | code/config | 90 | `2a15c270` | Inventory only; not necessarily read |
| 102 | P2 | `scripts/authoring/wte-ids.json` | code/config | 85 | `6520c44d` | Inventory only; not necessarily read |
| 103 | P2 | `scripts/authoring/wte-unplaced.txt` | code/config | 237 | `ad6c7eb1` | Inventory only; not necessarily read |
| 104 | P2 | `scripts/authoring/wte.py` | code/config | 1282 | `9e89cd08` | Inventory only; not necessarily read |
| 105 | P2 | `scripts/authoring/wte_pt.py` | code/config | 826 | `6d8bdc10` | Inventory only; not necessarily read |
| 106 | P2 | `scripts/authoring/wte_tasks_pt.py` | code/config | 299 | `7f13ac94` | Inventory only; not necessarily read |
| 107 | P2 | `scripts/authoring/ysx.py` | code/config | 1057 | `ff5f1848` | Inventory only; not necessarily read |
| 108 | P2 | `tests/fixtures/valid/demo/chapters/ch-00.json` | test | 20 | `3e61b153` | Inventory only; not necessarily read |
| 109 | P2 | `tests/fixtures/valid/demo/chapters/ch-01.json` | test | 91 | `feda8e63` | Inventory only; not necessarily read |
| 110 | P2 | `tests/fixtures/valid/demo/game.json` | test | 1 | `3bd4d3c2` | Inventory only; not necessarily read |
| 111 | P2 | `tests/fixtures/valid/franchises.json` | test | 1 | `5fffba84` | Inventory only; not necessarily read |
| 112 | P2 | `tests/fixtures/valid/id-registry.json` | test | 1 | `c64efdc1` | Inventory only; not necessarily read |
| 113 | P2 | `web/.editorconfig` | code/config | 17 | `d62fd282` | Inventory only; not necessarily read |
| 114 | P2 | `web/.gitignore` | code/config | 47 | `dcb19492` | Inventory only; not necessarily read |
| 115 | P2 | `web/.prettierrc` | code/config | 12 | `8cd4a640` | Inventory only; not necessarily read |
| 116 | P2 | `web/angular.json` | code/config | 80 | `80bb5381` | Inventory only; not necessarily read |
| 117 | P2 | `web/e2e/a11y.e2e.ts` | test | 17 | `47bbf202` | Inventory only; not necessarily read |
| 118 | P2 | `web/e2e/advance.e2e.ts` | test | 62 | `edf573f5` | Inventory only; not necessarily read |
| 119 | P2 | `web/e2e/collections.e2e.ts` | test | 80 | `40909e82` | Inventory only; not necessarily read |
| 120 | P2 | `web/e2e/deadlines.e2e.ts` | test | 24 | `01574569` | Inventory only; not necessarily read |
| 121 | P2 | `web/e2e/detail.e2e.ts` | test | 95 | `d642f8dd` | Inventory only; not necessarily read |
| 122 | P2 | `web/e2e/fixtures/content/cc/chapters/ch-00.json` | test | 458 | `b6bf7c49` | Inventory only; not necessarily read |
| 123 | P2 | `web/e2e/fixtures/content/cc/chapters/ch-01.json` | test | 105 | `b8db8073` | Inventory only; not necessarily read |
| 124 | P2 | `web/e2e/fixtures/content/cc/game.json` | test | 11 | `8ff3e314` | Inventory only; not necessarily read |
| 125 | P2 | `web/e2e/fixtures/content/franchises.json` | test | 23 | `c854b658` | Inventory only; not necessarily read |
| 126 | P2 | `web/e2e/fixtures/content/id-registry.json` | test | 32 | `9c930e51` | Inventory only; not necessarily read |
| 127 | P2 | `web/e2e/fixtures/content/sc/chapters/ch-00.json` | test | 194 | `5c3797ad` | Inventory only; not necessarily read |
| 128 | P2 | `web/e2e/fixtures/content/sc/chapters/ch-01.json` | test | 74 | `a4f9ca2c` | Inventory only; not necessarily read |
| 129 | P2 | `web/e2e/fixtures/content/sc/chapters/ch-02.json` | test | 9 | `108c2d74` | Inventory only; not necessarily read |
| 130 | P2 | `web/e2e/fixtures/content/sc/game.json` | test | 27 | `0df1f71b` | Inventory only; not necessarily read |
| 131 | P2 | `web/e2e/fixtures/content/zz/chapters/ch-00.json` | test | 45 | `731363c1` | Inventory only; not necessarily read |
| 132 | P2 | `web/e2e/fixtures/content/zz/game.json` | test | 9 | `ff8a5df2` | Inventory only; not necessarily read |
| 133 | P2 | `web/e2e/helpers.ts` | test | 43 | `7774511a` | Inventory only; not necessarily read |
| 134 | P2 | `web/e2e/home.e2e.ts` | test | 64 | `fd3f84cf` | Inventory only; not necessarily read |
| 135 | P2 | `web/e2e/library.e2e.ts` | test | 47 | `9bbd5bd3` | Inventory only; not necessarily read |
| 136 | P2 | `web/e2e/onboarding.e2e.ts` | test | 33 | `6a54fd9d` | Inventory only; not necessarily read |
| 137 | P2 | `web/e2e/route.e2e.ts` | test | 26 | `ee24e987` | Inventory only; not necessarily read |
| 138 | P2 | `web/e2e/search.e2e.ts` | test | 30 | `bf3c6116` | Inventory only; not necessarily read |
| 139 | P2 | `web/e2e/serve.mjs` | test | 30 | `016af588` | Inventory only; not necessarily read |
| 140 | P2 | `web/e2e/transfer-link.e2e.ts` | test | 40 | `433f8d2e` | Inventory only; not necessarily read |
| 141 | P2 | `web/e2e/transfer.e2e.ts` | test | 34 | `2bfe3f96` | Inventory only; not necessarily read |
| 142 | P2 | `web/e2e/trophies.e2e.ts` | test | 28 | `b8340eeb` | Inventory only; not necessarily read |
| 143 | P3 | `web/package-lock.json` | code/config | 7073 | `06b666ae` | Inventory only; not necessarily read |
| 144 | P2 | `web/public/_headers` | code/config | 16 | `55301e37` | Inventory only; not necessarily read |
| 145 | P2 | `web/public/i18n/en.json` | code/config | 522 | `0ed44dae` | Inventory only; not necessarily read |
| 146 | P2 | `web/public/i18n/pt.json` | code/config | 522 | `299e16cd` | Inventory only; not necessarily read |
| 147 | P3 | `web/public/icons/apple-touch-icon.png` | code/config | 13 | `b64457f0` | Inventory only; not necessarily read |
| 148 | P3 | `web/public/icons/icon-192.png` | code/config | 42 | `52f5c01b` | Inventory only; not necessarily read |
| 149 | P3 | `web/public/icons/icon-512.png` | code/config | 92 | `d39caeaa` | Inventory only; not necessarily read |
| 150 | P2 | `web/public/icons/mark.svg` | code/config | 7 | `459d5f12` | Inventory only; not necessarily read |
| 151 | P3 | `web/public/icons/maskable-512.png` | code/config | 45 | `1d441a20` | Inventory only; not necessarily read |
| 152 | P2 | `web/public/manifest.webmanifest` | code/config | 15 | `14b7826a` | Inventory only; not necessarily read |
| 153 | P3 | `web/public/share.png` | code/config | 2046 | `77e28ed4` | Inventory only; not necessarily read |
| 154 | P2 | `web/scripts/render-share-image.mjs` | code/config | 78 | `e157c47f` | Inventory only; not necessarily read |
| 155 | P2 | `web/src/app/app.html` | code/config | 59 | `af16d33d` | Inventory only; not necessarily read |
| 156 | P2 | `web/src/app/app.scss` | code/config | 39 | `de30def9` | Inventory only; not necessarily read |
| 157 | P2 | `web/src/app/app.ts` | code/config | 34 | `7cffa631` | Inventory only; not necessarily read |
| 158 | P2 | `web/src/app/core/analytics.service.spec.ts` | test | 27 | `be2897f3` | Inventory only; not necessarily read |
| 159 | P2 | `web/src/app/core/collections/collections.spec.ts` | test | 72 | `9fd9714a` | Inventory only; not necessarily read |
| 160 | P2 | `web/src/app/core/collections/collections.ts` | code/config | 84 | `b1061ea1` | Inventory only; not necessarily read |
| 161 | P2 | `web/src/app/core/compendium/compendium.spec.ts` | test | 82 | `693e8f4d` | Inventory only; not necessarily read |
| 162 | P2 | `web/src/app/core/compendium/plan.spec.ts` | test | 63 | `419684ee` | Inventory only; not necessarily read |
| 163 | P2 | `web/src/app/core/compendium/seasons.spec.ts` | test | 71 | `90595acb` | Inventory only; not necessarily read |
| 164 | P2 | `web/src/app/core/cover/cover-art.spec.ts` | test | 35 | `090a3d82` | Inventory only; not necessarily read |
| 165 | P2 | `web/src/app/core/cover/cover-art.ts` | code/config | 102 | `86196617` | Inventory only; not necessarily read |
| 166 | P2 | `web/src/app/core/game/saved-games.ts` | code/config | 68 | `717ce3e9` | Inventory only; not necessarily read |
| 167 | P2 | `web/src/app/core/i18n/game-name.pipe.ts` | code/config | 14 | `127e51c8` | Inventory only; not necessarily read |
| 168 | P2 | `web/src/app/core/i18n/lang.service.ts` | code/config | 41 | `ba519d52` | Inventory only; not necessarily read |
| 169 | P2 | `web/src/app/core/i18n/localize.pipe.ts` | code/config | 11 | `398b3ef4` | Inventory only; not necessarily read |
| 170 | P2 | `web/src/app/core/i18n/original.pipe.ts` | code/config | 14 | `9a02a13f` | Inventory only; not necessarily read |
| 171 | P2 | `web/src/app/core/i18n/terms.ts` | code/config | 14 | `bd9c50d3` | Inventory only; not necessarily read |
| 172 | P2 | `web/src/app/core/i18n/transloco-http-loader.ts` | code/config | 13 | `2621dfc5` | Inventory only; not necessarily read |
| 173 | P2 | `web/src/app/core/progress/progress.store.spec.ts` | test | 142 | `da683cb8` | Inventory only; not necessarily read |
| 174 | P2 | `web/src/app/core/progress/transfer-link.spec.ts` | test | 34 | `5c282aab` | Inventory only; not necessarily read |
| 175 | P2 | `web/src/app/core/progress/transfer.service.spec.ts` | test | 33 | `85c766f1` | Inventory only; not necessarily read |
| 176 | P2 | `web/src/app/core/pwa/app-update.service.spec.ts` | test | 51 | `d7a4baba` | Inventory only; not necessarily read |
| 177 | P2 | `web/src/app/core/pwa/app-update.service.ts` | code/config | 59 | `3f7fc6a1` | Inventory only; not necessarily read |
| 178 | P2 | `web/src/app/core/route/route.spec.ts` | test | 43 | `0da009a8` | Inventory only; not necessarily read |
| 179 | P2 | `web/src/app/core/route/route.ts` | code/config | 28 | `0a907cff` | Inventory only; not necessarily read |
| 180 | P2 | `web/src/app/core/search/global-search.spec.ts` | test | 48 | `346d48e7` | Inventory only; not necessarily read |
| 181 | P2 | `web/src/app/core/search/search.spec.ts` | test | 54 | `b6ae61d2` | Inventory only; not necessarily read |
| 182 | P2 | `web/src/app/core/search/search.ts` | code/config | 80 | `81af4074` | Inventory only; not necessarily read |
| 183 | P2 | `web/src/app/core/spoiler/deadlines.spec.ts` | test | 35 | `769855d5` | Inventory only; not necessarily read |
| 184 | P2 | `web/src/app/core/spoiler/deadlines.ts` | code/config | 50 | `ac968fe4` | Inventory only; not necessarily read |
| 185 | P2 | `web/src/app/core/spoiler/item-status.spec.ts` | test | 43 | `49205b46` | Inventory only; not necessarily read |
| 186 | P2 | `web/src/app/core/spoiler/item-status.ts` | code/config | 36 | `afce8e20` | Inventory only; not necessarily read |
| 187 | P2 | `web/src/app/core/spoiler/reveal.service.ts` | code/config | 15 | `a59bed00` | Inventory only; not necessarily read |
| 188 | P2 | `web/src/app/core/spoiler/spoiler.spec.ts` | test | 116 | `2a446f93` | Inventory only; not necessarily read |
| 189 | P2 | `web/src/app/pages/backup/backup.html` | code/config | 40 | `233e896c` | Inventory only; not necessarily read |
| 190 | P2 | `web/src/app/pages/backup/backup.scss` | code/config | 12 | `fa681e37` | Inventory only; not necessarily read |
| 191 | P2 | `web/src/app/pages/backup/backup.ts` | code/config | 89 | `b867ff84` | Inventory only; not necessarily read |
| 192 | P2 | `web/src/app/pages/boss-detail/boss-detail.html` | code/config | 55 | `934dc570` | Inventory only; not necessarily read |
| 193 | P2 | `web/src/app/pages/boss-detail/boss-detail.scss` | code/config | 28 | `6c71c96e` | Inventory only; not necessarily read |
| 194 | P2 | `web/src/app/pages/boss-detail/boss-detail.ts` | code/config | 58 | `15f54fbf` | Inventory only; not necessarily read |
| 195 | P2 | `web/src/app/pages/checklist/checklist.html` | code/config | 171 | `daa88fa0` | Inventory only; not necessarily read |
| 196 | P2 | `web/src/app/pages/checklist/checklist.scss` | code/config | 82 | `f4901b4e` | Inventory only; not necessarily read |
| 197 | P2 | `web/src/app/pages/collections/collections.html` | code/config | 164 | `a947108c` | Inventory only; not necessarily read |
| 198 | P2 | `web/src/app/pages/collections/collections.scss` | code/config | 67 | `13c71218` | Inventory only; not necessarily read |
| 199 | P2 | `web/src/app/pages/compendium/compendium.html` | code/config | 390 | `8b568638` | Inventory only; not necessarily read |
| 200 | P2 | `web/src/app/pages/compendium/compendium.scss` | code/config | 114 | `568171fc` | Inventory only; not necessarily read |
| 201 | P2 | `web/src/app/pages/creature/creature.html` | code/config | 155 | `e3538e60` | Inventory only; not necessarily read |
| 202 | P2 | `web/src/app/pages/creature/creature.scss` | code/config | 35 | `c4585c96` | Inventory only; not necessarily read |
| 203 | P2 | `web/src/app/pages/creature/creature.ts` | code/config | 57 | `dd004a2b` | Inventory only; not necessarily read |
| 204 | P2 | `web/src/app/pages/credits/credits.ts` | code/config | 61 | `744a49f6` | Inventory only; not necessarily read |
| 205 | P2 | `web/src/app/pages/deadlines/deadlines.html` | code/config | 42 | `6d86c5fb` | Inventory only; not necessarily read |
| 206 | P2 | `web/src/app/pages/deadlines/deadlines.scss` | code/config | 14 | `f2fc417b` | Inventory only; not necessarily read |
| 207 | P2 | `web/src/app/pages/deadlines/deadlines.ts` | code/config | 45 | `cdb3f30a` | Inventory only; not necessarily read |
| 208 | P2 | `web/src/app/pages/entry/entry.html` | code/config | 186 | `6e3b1447` | Inventory only; not necessarily read |
| 209 | P2 | `web/src/app/pages/entry/entry.scss` | code/config | 42 | `92e66291` | Inventory only; not necessarily read |
| 210 | P2 | `web/src/app/pages/entry/entry.ts` | code/config | 94 | `9eaa2033` | Inventory only; not necessarily read |
| 211 | P2 | `web/src/app/pages/home/home.html` | code/config | 189 | `948ebd7a` | Inventory only; not necessarily read |
| 212 | P2 | `web/src/app/pages/home/home.scss` | code/config | 69 | `397e7152` | Inventory only; not necessarily read |
| 213 | P2 | `web/src/app/pages/item-detail/item-detail.html` | code/config | 131 | `d6b4a5d8` | Inventory only; not necessarily read |
| 214 | P2 | `web/src/app/pages/item-detail/item-detail.scss` | code/config | 60 | `99e5a8b3` | Inventory only; not necessarily read |
| 215 | P2 | `web/src/app/pages/item-detail/item-detail.ts` | code/config | 93 | `0cef4109` | Inventory only; not necessarily read |
| 216 | P2 | `web/src/app/pages/library/library.html` | code/config | 79 | `aaefeca9` | Inventory only; not necessarily read |
| 217 | P2 | `web/src/app/pages/library/library.scss` | code/config | 48 | `d95c1841` | Inventory only; not necessarily read |
| 218 | P2 | `web/src/app/pages/library/library.ts` | code/config | 55 | `5876287f` | Inventory only; not necessarily read |
| 219 | P2 | `web/src/app/pages/plan/plan.html` | code/config | 99 | `1674abd6` | Inventory only; not necessarily read |
| 220 | P2 | `web/src/app/pages/plan/plan.scss` | code/config | 39 | `94ebd539` | Inventory only; not necessarily read |
| 221 | P2 | `web/src/app/pages/privacy/privacy.ts` | code/config | 26 | `a0b82e9d` | Inventory only; not necessarily read |
| 222 | P2 | `web/src/app/pages/search/search.html` | code/config | 44 | `ab162ccb` | Inventory only; not necessarily read |
| 223 | P2 | `web/src/app/pages/search/search.scss` | code/config | 30 | `0325dca6` | Inventory only; not necessarily read |
| 224 | P2 | `web/src/app/pages/search/search.ts` | code/config | 55 | `98fffab4` | Inventory only; not necessarily read |
| 225 | P2 | `web/src/app/pages/where/where.html` | code/config | 73 | `c259abf7` | Inventory only; not necessarily read |
| 226 | P2 | `web/src/app/pages/where/where.scss` | code/config | 32 | `e624a23c` | Inventory only; not necessarily read |
| 227 | P2 | `web/src/app/pages/where/where.ts` | code/config | 52 | `b4433bd6` | Inventory only; not necessarily read |
| 228 | P2 | `web/src/app/ui/advance-confirm/advance-confirm.html` | code/config | 18 | `ac58a00a` | Inventory only; not necessarily read |
| 229 | P2 | `web/src/app/ui/advance-confirm/advance-confirm.scss` | code/config | 10 | `f4368bda` | Inventory only; not necessarily read |
| 230 | P2 | `web/src/app/ui/advance-confirm/advance-confirm.ts` | code/config | 58 | `2ecb6b37` | Inventory only; not necessarily read |
| 231 | P2 | `web/src/app/ui/detail-bar/detail-bar.ts` | code/config | 54 | `0767e5e3` | Inventory only; not necessarily read |
| 232 | P2 | `web/src/app/ui/game-card/game-card.ts` | code/config | 65 | `eb30a6c2` | Inventory only; not necessarily read |
| 233 | P2 | `web/src/app/ui/game-cover/game-cover.ts` | code/config | 71 | `15216953` | Inventory only; not necessarily read |
| 234 | P2 | `web/src/app/ui/how-it-works/how-it-works.html` | code/config | 17 | `2d50b241` | Inventory only; not necessarily read |
| 235 | P2 | `web/src/app/ui/how-it-works/how-it-works.scss` | code/config | 7 | `437fa1dd` | Inventory only; not necessarily read |
| 236 | P2 | `web/src/app/ui/how-it-works/how-it-works.ts` | code/config | 41 | `87abdc7e` | Inventory only; not necessarily read |
| 237 | P2 | `web/src/app/ui/icon/icon.ts` | code/config | 30 | `47330380` | Inventory only; not necessarily read |
| 238 | P2 | `web/src/app/ui/icon/icons.ts` | code/config | 31 | `4d5267c0` | Inventory only; not necessarily read |
| 239 | P2 | `web/src/app/ui/item-row/item-row.html` | code/config | 50 | `df909570` | Inventory only; not necessarily read |
| 240 | P2 | `web/src/app/ui/item-row/item-row.scss` | code/config | 30 | `8cb2acc1` | Inventory only; not necessarily read |
| 241 | P2 | `web/src/app/ui/item-row/item-row.ts` | code/config | 44 | `e75ac379` | Inventory only; not necessarily read |
| 242 | P2 | `web/src/app/ui/item-type.ts` | code/config | 10 | `f21bbc1a` | Inventory only; not necessarily read |
| 243 | P2 | `web/src/app/ui/name-fix/name-fix.html` | code/config | 37 | `cd54f48b` | Inventory only; not necessarily read |
| 244 | P2 | `web/src/app/ui/name-fix/name-fix.scss` | code/config | 17 | `14042948` | Inventory only; not necessarily read |
| 245 | P2 | `web/src/app/ui/name-fix/name-fix.ts` | code/config | 74 | `0e71b9b8` | Inventory only; not necessarily read |
| 246 | P2 | `web/src/app/ui/report-link/report-link.ts` | code/config | 70 | `750cfea3` | Inventory only; not necessarily read |
| 247 | P2 | `web/src/app/ui/route-steps/route-steps.ts` | code/config | 74 | `168e55ff` | Inventory only; not necessarily read |
| 248 | P2 | `web/src/app/ui/scroll-hints/scroll-hints.ts` | code/config | 37 | `9453be89` | Inventory only; not necessarily read |
| 249 | P2 | `web/src/app/ui/season-calendar/season-calendar.html` | code/config | 73 | `26f01f52` | Inventory only; not necessarily read |
| 250 | P2 | `web/src/app/ui/season-calendar/season-calendar.scss` | code/config | 28 | `382a96a6` | Inventory only; not necessarily read |
| 251 | P2 | `web/src/app/ui/season-calendar/season-calendar.ts` | code/config | 43 | `afd6fb60` | Inventory only; not necessarily read |
| 252 | P2 | `web/src/app/ui/spoiler-notice/spoiler-notice.ts` | code/config | 57 | `5d77732c` | Inventory only; not necessarily read |
| 253 | P2 | `web/src/app/ui/spoiler-reveal/spoiler-reveal.ts` | code/config | 60 | `ccd40764` | Inventory only; not necessarily read |
| 254 | P2 | `web/src/index.html` | code/config | 29 | `ba0871cd` | Inventory only; not necessarily read |
| 255 | P2 | `web/src/styles.scss` | code/config | 180 | `0100eb07` | Inventory only; not necessarily read |
| 256 | P2 | `web/tsconfig.app.json` | code/config | 14 | `12e2786b` | Inventory only; not necessarily read |
| 257 | P2 | `web/tsconfig.json` | code/config | 32 | `e73b50ac` | Inventory only; not necessarily read |
| 258 | P2 | `web/tsconfig.spec.json` | test | 14 | `958fd251` | Inventory only; not necessarily read |

Decisions/Findings: prioritize source contracts and runtime entry points.

Open Questions: behavioral details of inventory-only files.

Next Steps: follow master document read queue.
