import { Routes } from '@angular/router';

import { unlockedChapterGuard } from './core/spoiler/chapter-access';

export const routes: Routes = [
  { path: '', loadComponent: () => import('./pages/home/home').then((m) => m.Home) },
  { path: 'sc/chapters', loadComponent: () => import('./pages/where/where').then((m) => m.Where) },
  {
    path: 'sc/chapters/:chapterId',
    canActivate: [unlockedChapterGuard],
    loadComponent: () => import('./pages/checklist/checklist').then((m) => m.Checklist),
  },
  {
    path: 'sc/items/:itemId',
    canActivate: [unlockedChapterGuard],
    loadComponent: () => import('./pages/item-detail/item-detail').then((m) => m.ItemDetail),
  },
  { path: '**', redirectTo: '' },
];
