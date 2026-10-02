import { Routes } from '@angular/router';

import { gameGuard } from './core/game/active-game';
import { unlockedChapterGuard } from './core/spoiler/chapter-access';

export const routes: Routes = [
  { path: '', loadComponent: () => import('./pages/home/home').then((m) => m.Home) },
  { path: 'credits', loadComponent: () => import('./pages/credits/credits').then((m) => m.Credits) },
  { path: 'backup', loadComponent: () => import('./pages/backup/backup').then((m) => m.Backup) },
  { path: 'privacy', loadComponent: () => import('./pages/privacy/privacy').then((m) => m.Privacy) },
  {
    // Every game lives under its own id: /sc/chapters, /sc/items/..., and later other games.
    path: ':gameId',
    canActivate: [gameGuard],
    children: [
      { path: '', pathMatch: 'full', redirectTo: 'chapters' },
      { path: 'chapters', loadComponent: () => import('./pages/where/where').then((m) => m.Where) },
      {
        path: 'chapters/:chapterId',
        canActivate: [unlockedChapterGuard],
        loadComponent: () => import('./pages/checklist/checklist').then((m) => m.Checklist),
      },
      {
        path: 'items/:itemId',
        canActivate: [unlockedChapterGuard],
        loadComponent: () => import('./pages/item-detail/item-detail').then((m) => m.ItemDetail),
      },
      {
        path: 'bosses/:bossId',
        canActivate: [unlockedChapterGuard],
        loadComponent: () => import('./pages/boss-detail/boss-detail').then((m) => m.BossDetail),
      },
      { path: 'search', loadComponent: () => import('./pages/search/search').then((m) => m.Search) },
      { path: 'deadlines', loadComponent: () => import('./pages/deadlines/deadlines').then((m) => m.Deadlines) },
      { path: 'compendium', loadComponent: () => import('./pages/compendium/compendium').then((m) => m.Compendium) },
      { path: 'creatures/:creatureId', loadComponent: () => import('./pages/creature/creature').then((m) => m.CreatureDetail) },
      { path: 'entries/:entryId', loadComponent: () => import('./pages/entry/entry').then((m) => m.EntryDetail) },
      { path: 'collections', loadComponent: () => import('./pages/collections/collections').then((m) => m.Collections) },
    ],
  },
  { path: '**', redirectTo: '' },
];
