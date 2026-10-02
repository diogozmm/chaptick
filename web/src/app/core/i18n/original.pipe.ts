import { Pipe, PipeTransform } from '@angular/core';

import { Lang, Localized } from '../content/content.models';

/**
 * The English name when the reader sees a translation of it, so a player whose game shows the
 * English name (or a different official translation) still recognizes it. Empty otherwise.
 */
@Pipe({ name: 'original' })
export class OriginalPipe implements PipeTransform {
  transform(text: Localized | undefined, lang: Lang): string {
    return text && lang !== 'en' && text.pt && text.pt !== text.en ? text.en : '';
  }
}
