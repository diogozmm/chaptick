import { Pipe, PipeTransform } from '@angular/core';

import { Lang, Localized, localize } from '../content/content.models';

/** `text | localize: lang()` — content text in the active language, falling back to English. */
@Pipe({ name: 'localize' })
export class LocalizePipe implements PipeTransform {
  transform(text: Localized, lang: Lang): string {
    return localize(text, lang);
  }
}
