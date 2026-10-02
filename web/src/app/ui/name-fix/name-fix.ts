import { ChangeDetectionStrategy, Component, computed, inject, input, signal } from '@angular/core';
import { TranslocoPipe } from '@jsverse/transloco';

import { Localized, localize } from '../../core/content/content.models';
import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { ProgressStore } from '../../core/progress/progress.store';
import { SITE } from '../../site.config';
import { Icon } from '../icon/icon';

/**
 * "The name is different in my game": the player types the name their game shows. It replaces
 * ours right away on this device (saved with their progress, so backups keep it), and they can
 * send it in so the content gets fixed for everyone.
 */
@Component({
  selector: 'app-name-fix',
  imports: [TranslocoPipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './name-fix.html',
  styleUrl: './name-fix.scss',
})
export class NameFix {
  private readonly progress = inject(ProgressStore);
  private readonly active = inject(ActiveGame);
  protected readonly lang = inject(LangService);

  readonly entryId = input.required<string>();
  readonly name = input.required<Localized>();

  protected readonly open = signal(false);
  protected readonly draft = signal('');
  protected readonly saved = computed(() => this.progress.preferences().names?.[this.entryId()] ?? '');
  protected readonly ours = computed(() => localize(this.name(), this.lang.lang()));

  protected start(): void {
    this.draft.set(this.saved() || this.ours());
    this.open.set(true);
  }

  protected async save(): Promise<void> {
    const value = this.draft().trim();
    await this.progress.setName(this.entryId(), value === this.ours() ? '' : value);
    this.open.set(false);
  }

  protected async reset(): Promise<void> {
    await this.progress.setName(this.entryId(), '');
    this.open.set(false);
  }

  private readonly version = computed(() => {
    const game = this.active.manifest()?.game;
    return game ? `${game.id} data v${game.dataVersion}` : '';
  });

  /** A prefilled report of the name the player typed (GitHub issue form, or e-mail). */
  protected readonly issueUrl = computed(() => {
    if (!SITE.repoUrl || !this.saved()) return '';
    const params = new URLSearchParams({
      template: 'name-correction.yml', title: `name ${this.entryId()}`, item: this.entryId(), english: this.name().en,
      shown: this.ours(), ingame: this.saved(), language: this.lang.lang() === 'pt' ? 'pt-BR' : 'en', version: this.version(),
    });
    return `${SITE.repoUrl}/issues/new?${params}`;
  });
  protected readonly mailUrl = computed(() => {
    if (!SITE.contactEmail || !this.saved()) return '';
    const subject = encodeURIComponent(`Chaptick: name ${this.entryId()}`);
    const body = encodeURIComponent(
      `Entry: ${this.entryId()}\nEnglish: ${this.name().en}\nApp shows: ${this.ours()}\nIn my game: ${this.saved()}\nData: ${this.version()}\n`,
    );
    return `mailto:${SITE.contactEmail}?subject=${subject}&body=${body}`;
  });
}
