import { Injectable, inject, signal } from '@angular/core';
import { TranslocoService } from '@jsverse/transloco';
import { firstValueFrom } from 'rxjs';

import { Lang } from '../content/content.models';

const STORAGE_KEY = 'bracer-notes.lang';

/** UI and content language. The choice is a per-device convenience, so storage failures are ignored. */
@Injectable({ providedIn: 'root' })
export class LangService {
  private readonly transloco = inject(TranslocoService);
  private readonly langSignal = signal<Lang>('en');

  readonly lang = this.langSignal.asReadonly();

  async init(): Promise<void> {
    await this.use(readStored() ?? (navigator.language.toLowerCase().startsWith('pt') ? 'pt' : 'en'));
  }

  async use(lang: Lang): Promise<void> {
    await firstValueFrom(this.transloco.load(lang));
    this.transloco.setActiveLang(lang);
    this.langSignal.set(lang);
    document.documentElement.lang = lang === 'pt' ? 'pt-BR' : 'en';
    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch {
      // Private mode or blocked storage: the language just won't be remembered.
    }
  }
}

function readStored(): Lang | null {
  try {
    const value = localStorage.getItem(STORAGE_KEY);
    return value === 'en' || value === 'pt' ? value : null;
  } catch {
    return null;
  }
}
