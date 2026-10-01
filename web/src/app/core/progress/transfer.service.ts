import { Injectable, inject } from '@angular/core';

import { AnalyticsService } from '../analytics.service';
import { SITE } from '../../site.config';
import { ProgressStore } from './progress.store';
import { decodeTransfer, encodeTransfer, transferLink, transferToken } from './transfer-link';

/** Transfer links (another device) and the move to the canonical address (a new domain). */
@Injectable({ providedIn: 'root' })
export class TransferService {
  private readonly progress = inject(ProgressStore);
  private readonly analytics = inject(AnalyticsService);

  /** The canonical address when this visit is on another one, else null. */
  readonly movedTo: string | null =
    SITE.canonicalOrigin && typeof location !== 'undefined' && location.origin !== SITE.canonicalOrigin
      ? SITE.canonicalOrigin
      : null;

  /** A link that opens the app at `origin` with every saved game on this device. */
  async createLink(origin = location.origin): Promise<string> {
    this.analytics.track('progress_link_created');
    return transferLink(origin, await encodeTransfer(await this.progress.exportJson(true)));
  }

  private incoming: string | null = null;

  /**
   * Runs before the router starts (app initializer): keeps the token of a transfer link and removes
   * it from the address bar, so it is not bookmarked, shared again or imported twice.
   */
  captureIncoming(): void {
    const token = transferToken(location.hash);
    if (!token) return;
    this.incoming = token;
    history.replaceState(history.state, '', location.pathname + location.search);
  }

  /** The file carried by the link this page was opened with, once; null when there is none. */
  async takeIncoming(): Promise<string | null> {
    const token = this.incoming;
    this.incoming = null;
    return token ? decodeTransfer(token) : null;
  }

  /** Opens the canonical address, carrying this device's progress when there is any. */
  async moveToCanonical(): Promise<void> {
    if (!this.movedTo) return;
    const saved = await this.progress.listSaved();
    this.analytics.track('progress_moved', { games: saved.length });
    location.assign(saved.length ? await this.createLink(this.movedTo) : this.movedTo);
  }
}
