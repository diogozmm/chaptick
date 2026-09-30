import { ChangeDetectionStrategy, Component, computed, inject, input } from '@angular/core';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { Chapter, Item } from '../../core/content/content.models';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';
import { ItemView } from '../../core/spoiler/item-view';
import { Icon } from '../icon/icon';
import { SpoilerReveal } from '../spoiler-reveal/spoiler-reveal';

/** One checklist entry: checkbox, masked name, deadline, hint and a link to the details. */
@Component({
  selector: 'app-item-row',
  imports: [RouterLink, TranslocoPipe, LocalizePipe, SpoilerReveal, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './item-row.html',
  styleUrl: './item-row.scss',
  host: { '[class.done]': 'done()', '[attr.data-type]': 'item().type' },
})
export class ItemRow {
  protected readonly progress = inject(ProgressStore);
  protected readonly view = inject(ItemView);
  protected readonly lang = inject(LangService);

  /** The chapter the item belongs to. */
  readonly chapter = input.required<Chapter>();
  readonly item = input.required<Item>();

  protected readonly done = computed(() => this.progress.done().has(this.item().id));
  protected readonly deadline = computed(() => this.view.deadline(this.chapter(), this.item()));
}
