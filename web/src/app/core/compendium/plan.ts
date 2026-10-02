import { Craft, Localized } from '../content/content.models';
import { CompendiumIndex, IndexedCraft } from './compendium';

/** One line of a plan: something to have, and how many; made from `children` when it is crafted. */
export interface PlanNode {
  name: Localized;
  entryId?: string;
  qty: number;
  /** The recipe used to make it, when it is made rather than gathered. */
  craft?: IndexedCraft;
  /** How many times that recipe runs (a recipe may make several at once). */
  runs: number;
  /** Whether a recipe for it is known, so the player can choose to make it. */
  makeable: boolean;
  children: PlanNode[];
}

export interface PlanTotal {
  name: Localized;
  entryId?: string;
  qty: number;
}

const MAX_DEPTH = 8;
const MADE_KINDS = new Set(['craft', 'cook', 'process']);

/** How many a recipe makes at once: its yield, or the batch in its name ("10x Tile Path" makes ten). */
export const craftYield = (craft: Craft): number => craft.yield ?? Number(/^(\d+)x /.exec(craft.name.en)?.[1] ?? 1);

/**
 * Whether an ingredient is made by default: only when a recipe for it is known and there is no
 * other way to get it (no shop, spot, drop…). The player can switch any ingredient either way.
 */
export function madeByDefault(index: CompendiumIndex, entryId: string): boolean {
  const entry = index.entries.get(entryId);
  if (!entry || !index.madeBy.has(entryId)) return false;
  return entry.sources.every((s) => MADE_KINDS.has(s.source.kind));
}

/**
 * The tree of what it takes to make `qty` of a recipe, from the reached content only. `choice`
 * overrides the default per ingredient (true: make it, false: get it ready-made). Recipes that
 * lead back to themselves stop there instead of looping.
 */
export function planCraft(
  index: CompendiumIndex,
  craft: IndexedCraft,
  qty: number,
  choice: ReadonlyMap<string, boolean> = new Map(),
): PlanNode {
  const build = (c: IndexedCraft, need: number, depth: number, path: ReadonlySet<string>): PlanNode => {
    const runs = Math.ceil(need / craftYield(c.craft));
    const children = c.craft.ingredients.map((ingredient) => {
      const want = ingredient.qty * runs;
      const recipe = ingredient.entryId ? index.madeBy.get(ingredient.entryId)?.[0] : undefined;
      const makeable = !!recipe && !path.has(recipe.craft.id) && depth < MAX_DEPTH;
      const make = makeable && (choice.get(ingredient.entryId!) ?? madeByDefault(index, ingredient.entryId!));
      if (make) {
        const node = build(recipe!, want, depth + 1, new Set([...path, recipe!.craft.id]));
        return { ...node, name: ingredient.name, entryId: ingredient.entryId, qty: want };
      }
      return { name: ingredient.name, entryId: ingredient.entryId, qty: want, runs: 0, makeable, children: [] };
    });
    return { name: c.craft.name, entryId: c.craft.makes, qty: need, craft: c, runs, makeable: true, children };
  };
  return build(craft, qty, 0, new Set([craft.craft.id]));
}

/** Everything to gather for a plan, summed across the tree: its leaves. */
export function planTotals(root: PlanNode): PlanTotal[] {
  const totals = new Map<string, PlanTotal>();
  const walk = (node: PlanNode) => {
    for (const child of node.children) {
      if (child.craft) {
        walk(child);
        continue;
      }
      const key = child.entryId ?? child.name.en;
      const total = totals.get(key);
      if (total) total.qty += child.qty;
      else totals.set(key, { name: child.name, entryId: child.entryId, qty: child.qty });
    }
  };
  walk(root);
  return [...totals.values()].sort((a, b) => a.name.en.localeCompare(b.name.en));
}
