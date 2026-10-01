import { DestroyRef, Directive, ElementRef, afterNextRender, inject, signal } from '@angular/core';

/**
 * On a horizontally scrolling element, tracks whether there is more content before or after the
 * visible part, so the page only shows the arrows that do something.
 */
@Directive({
  selector: '[appScrollHints]',
  exportAs: 'scrollHints',
  host: { '(scroll)': 'update()' },
})
export class ScrollHints {
  private readonly element = inject<ElementRef<HTMLElement>>(ElementRef).nativeElement;
  readonly canBack = signal(false);
  readonly canForward = signal(false);

  constructor() {
    const destroyRef = inject(DestroyRef);
    afterNextRender(() => {
      const observer = new ResizeObserver(() => this.update());
      observer.observe(this.element);
      destroyRef.onDestroy(() => observer.disconnect());
      this.update();
    });
  }

  protected update(): void {
    const { scrollLeft, scrollWidth, clientWidth } = this.element;
    this.canBack.set(scrollLeft > 4);
    this.canForward.set(scrollLeft + clientWidth < scrollWidth - 4);
  }

  /** One screenful at a time. */
  scroll(direction: 1 | -1): void {
    this.element.scrollBy({ left: direction * this.element.clientWidth * 0.9, behavior: 'smooth' });
  }
}
