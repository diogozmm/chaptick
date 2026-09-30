import { Injectable, inject } from '@angular/core';
import { TranslocoService } from '@jsverse/transloco';

import { Chapter, Item } from '../content/content.models';
import { RevealService } from './reveal.service';
import { isMasked, maskOrdinal } from './spoiler';

/** How much of an item may be shown right now. Shared by every view of an item. */
@Injectable({ providedIn: 'root' })
export class ItemView {
  private readonly transloco = inject(TranslocoService);
  private readonly reveals = inject(RevealService);

  /** "Hidden quest #2": what a masked item is called until revealed. */
  placeholder(chapter: Chapter, item: Item): string {
    return this.transloco.translate(`type.one.${item.type}`, { n: maskOrdinal(chapter, item) });
  }

  /** Location can give away as much as the name, so it follows the same mask. */
  showLocation(item: Item): boolean {
    return !isMasked(item.spoilerLevel) || this.reveals.isRevealed(item.id);
  }

  /**
   * Level 2 hints are written to be safe on their own; level 1 hints may name what the mask
   * hides. Community texts inherit the item's level, so they follow this rule too.
   */
  showHint(item: Item): boolean {
    return item.spoilerLevel !== 1 || this.reveals.isRevealed(item.id);
  }
}
