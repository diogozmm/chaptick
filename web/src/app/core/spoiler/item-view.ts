import { Injectable, inject } from '@angular/core';
import { TranslocoService } from '@jsverse/transloco';

import { Chapter, Item, Localized } from '../content/content.models';
import { ContentService } from '../content/content.service';
import { RevealService } from './reveal.service';
import { chapterOrderOf, isMasked, maskOrdinal } from './spoiler';

export type Deadline =
  | { kind: 'checkpoint'; description: Localized }
  /** The checkpoint is in a chapter not unlocked yet: only its neutral label may be shown. */
  | { kind: 'chapter'; label: Localized }
  | { kind: 'none' };

/** How much of an item may be shown right now. Shared by every view of an item. */
@Injectable({ providedIn: 'root' })
export class ItemView {
  private readonly transloco = inject(TranslocoService);
  private readonly reveals = inject(RevealService);
  private readonly content = inject(ContentService);

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

  deadline(chapter: Chapter, item: Item): Deadline {
    const id = item.availableUntil;
    if (!id) return { kind: 'none' };
    const owner = chapter.checkpoints.some((c) => c.id === id) ? chapter : this.content.loaded().get(id.replace(/-cp-\d+$/, ''));
    const checkpoint = owner?.checkpoints.find((c) => c.id === id);
    if (checkpoint) return { kind: 'checkpoint', description: checkpoint.neutralDescription };
    const order = chapterOrderOf(id);
    const summary = this.content.manifest()?.chapters.find((c) => c.order === order);
    return summary ? { kind: 'chapter', label: summary.neutralLabel } : { kind: 'none' };
  }
}
