import { ChangeDetectionStrategy, Component, computed, inject, input, resource, signal } from '@angular/core';
import { NgTemplateOutlet } from '@angular/common';
import { Router, RouterLink } from '@angular/router';
import { TranslocoPipe } from '@jsverse/transloco';

import { compendiumIndex } from '../../core/compendium/compendium';
import { craftYield, PlanNode, planCraft, planTotals } from '../../core/compendium/plan';
import { ActiveGame } from '../../core/game/active-game';
import { LangService } from '../../core/i18n/lang.service';
import { LocalizePipe } from '../../core/i18n/localize.pipe';
import { OriginalPipe } from '../../core/i18n/original.pipe';
import { ChapterAccess } from '../../core/spoiler/chapter-access';
import { Icon } from '../../ui/icon/icon';

const MAX_QTY = 99;

/**
 * Shopping list for a recipe: everything to gather, summed, and the steps to make it. Ingredients
 * that have a recipe can be switched between "make it" and "get it ready-made". Only what the
 * reached chapters (or areas) reveal is used.
 */
@Component({
  selector: 'app-plan',
  imports: [RouterLink, NgTemplateOutlet, TranslocoPipe, LocalizePipe, OriginalPipe, Icon],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './plan.html',
  styleUrl: './plan.scss',
})
export class Plan {
  private readonly access = inject(ChapterAccess);
  private readonly router = inject(Router);
  protected readonly game = inject(ActiveGame);
  protected readonly lang = inject(LangService);

  readonly craftId = input.required<string>();
  /** How many to make, kept in the URL (?qty=). */
  readonly qty = input<string | undefined>();

  private readonly chapters = resource({
    params: () => this.access.currentOrder(),
    loader: () => this.access.loadUnlocked(),
  });
  protected readonly ready = computed(() => this.chapters.hasValue());
  private readonly index = computed(() => compendiumIndex(this.chapters.hasValue() ? this.chapters.value() : []));
  protected readonly craft = computed(() => this.index().crafts.find((c) => c.craft.id === this.craftId()) ?? null);
  protected readonly amount = computed(() => Math.min(MAX_QTY, Math.max(1, Number.parseInt(this.qty() ?? '1', 10) || 1)));
  protected readonly perRun = computed(() => (this.craft() ? craftYield(this.craft()!.craft) : 1));

  /** The player's make-or-get choices per ingredient; the default applies to the others. */
  private readonly choice = signal<ReadonlyMap<string, boolean>>(new Map());
  /** Ingredients the player already has, ticked off the list (for this visit only). */
  protected readonly have = signal<ReadonlySet<string>>(new Set());

  protected readonly plan = computed(() => {
    const craft = this.craft();
    return craft ? planCraft(this.index(), craft, this.amount(), this.choice()) : null;
  });
  protected readonly totals = computed(() => {
    const plan = this.plan();
    if (!plan) return [];
    const have = this.have();
    const key = (t: { entryId?: string; name: { en: string } }) => t.entryId ?? t.name.en;
    return planTotals(plan)
      .map((t) => ({ ...t, key: key(t), had: have.has(key(t)) }))
      .sort((a, b) => Number(a.had) - Number(b.had));
  });

  /** The first ways to get an ingredient, as a hint under its name. */
  protected ways(entryId: string | undefined): { kind: string; where: string }[] {
    const found = entryId ? this.index().entries.get(entryId) : undefined;
    const lang = this.lang.lang();
    return (found?.sources ?? []).slice(0, 2).map((s) => ({ kind: s.source.kind, where: s.source.where[lang] ?? s.source.where.en }));
  }

  protected setAmount(value: number): void {
    const qty = Math.min(MAX_QTY, Math.max(1, value));
    void this.router.navigate([], { queryParams: { qty: qty === 1 ? null : qty }, replaceUrl: true });
  }

  protected toggleMake(node: PlanNode): void {
    if (!node.entryId) return;
    const next = new Map(this.choice());
    next.set(node.entryId, !node.craft);
    this.choice.set(next);
  }

  protected toggleHave(key: string): void {
    const next = new Set(this.have());
    if (next.has(key)) next.delete(key);
    else next.add(key);
    this.have.set(next);
  }
}
