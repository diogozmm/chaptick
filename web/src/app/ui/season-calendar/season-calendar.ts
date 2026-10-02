import { ChangeDetectionStrategy, Component, computed, inject, input } from '@angular/core';
import { NgTemplateOutlet } from '@angular/common';
import { RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { calendar } from '../../core/compendium/seasons';
import { GameEvent, Season } from '../../core/content/content.models';
import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { ProgressStore } from '../../core/progress/progress.store';

const MAX_DAY = 28;

/**
 * The season's calendar: what happens today, later this season and every week. The player sets
 * the day of the season (kept per game); without it, the whole season is listed.
 */
@Component({
  selector: 'app-season-calendar',
  imports: [RouterLink, NgTemplateOutlet, TranslocoPipe, LocalizePipe],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './season-calendar.html',
  styleUrl: './season-calendar.scss',
})
export class SeasonCalendar {
  private readonly progress = inject(ProgressStore);
  protected readonly game = inject(ActiveGame);
  protected readonly lang = inject(LangService);

  readonly events = input.required<readonly GameEvent[]>();
  readonly season = input.required<Season>();

  protected readonly maxDay = MAX_DAY;
  protected readonly day = computed(() => this.progress.preferences().day ?? null);
  protected readonly calendarNow = computed(() =>
    this.events().length ? calendar(this.events(), this.season(), this.day()) : null,
  );

  protected setDay(day: number | null): void {
    void this.progress.setPreferences({ day: day === null ? undefined : Math.min(MAX_DAY, Math.max(1, day)) });
  }
}
