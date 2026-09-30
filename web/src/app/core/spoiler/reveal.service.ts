import { Injectable, signal } from '@angular/core';

/** Items the player chose to reveal. Session only: a reload hides them again. */
@Injectable({ providedIn: 'root' })
export class RevealService {
  private readonly revealed = signal<ReadonlySet<string>>(new Set());

  isRevealed(itemId: string): boolean {
    return this.revealed().has(itemId);
  }

  reveal(itemId: string): void {
    this.revealed.update((set) => new Set(set).add(itemId));
  }
}
