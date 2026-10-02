import { Pipe, PipeTransform } from '@angular/core';

import { Lang, Localized, localize } from '../content/content.models';

/**
 * `name | gameName: id : names : lang` — the name the player saved for this entry (as their game
 * shows it), or ours in their language. `names` comes from the saved progress.
 */
@Pipe({ name: 'gameName' })
export class GameNamePipe implements PipeTransform {
  transform(text: Localized, id: string | undefined, names: Record<string, string> | undefined, lang: Lang): string {
    return (id && names?.[id]) || localize(text, lang);
  }
}
