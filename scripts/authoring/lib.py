"""Tiny helpers to author chapter files. Output is plain JSON validated by content/schema."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'content'


def t(en, pt=None):
    return {'en': en, 'pt': pt} if pt else {'en': en}


def src(page):
    return f'guide: Neoseeker SC walkthrough, {page}'


def gf(page):
    return f'guide: GameFAQs SC walkthrough by shockinblue, {page}'


class Chapter:
    def __init__(self, order, en, pt):
        self.order = order
        self.id = f'sc-ch{order}'
        self.data = {'id': self.id, 'gameId': 'sc', 'order': order, 'neutralLabel': t(en, pt),
                     'checkpoints': [], 'items': [], 'itemTexts': []}
        self.counters = {}

    @classmethod
    def load(cls, order):
        """Extends a chapter file written by hand, keeping its existing ids untouched."""
        c = cls.__new__(cls)
        c.order, c.id = order, f'sc-ch{order}'
        c.data = json.loads((ROOT / 'sc' / 'chapters' / f'ch-{order:02d}.json').read_text())
        for key in ('bosses', 'fish', 'fishSpots', 'recipes'):
            c.data[key] = []
        c.counters = {}
        return c

    def _next(self, code):
        self.counters[code] = self.counters.get(code, 0) + 1
        return f'{self.id}-{code}-{self.counters[code]:02d}'

    def boss(self, name, location, strategy, related=None, sources=()):
        boss = {'id': self._next('bs'), 'name': name, 'location': location, 'strategy': strategy, 'sources': list(sources)}
        if related:
            boss['relatedItem'] = related
        self.data.setdefault('bosses', []).append(boss)

    def fish(self, name, sources=()):
        fid = self._next('fi')
        self.data.setdefault('fish', []).append({'id': fid, 'name': t(name), 'sources': list(sources)})
        return fid

    def spot(self, fish_id, rank, where):
        self.data.setdefault('fishSpots', []).append({'fishId': fish_id, 'rank': rank, 'where': where})

    def recipe(self, name, source, kind='standard', sources=()):
        self.data.setdefault('recipes', []).append(
            {'id': self._next('re'), 'kind': kind, 'name': t(name), 'source': source, 'sources': list(sources)})

    def cp(self, en, pt, order=None):
        """Ids follow creation order (never reuse them); `order` places a checkpoint added later
        between existing ones on the story timeline."""
        n = len(self.data['checkpoints']) + 1
        cid = f'{self.id}-cp-{n:02d}'
        self.data['checkpoints'].append({'id': cid, 'order': order or n, 'neutralDescription': t(en, pt)})
        return cid

    def item(self, type_, name, location, until, hint, level=0, sources=(), steps=None):
        code = {'quest': 'q', 'hidden_quest': 'hq', 'missable': 'mi', 'collectible': 'co'}[type_]
        iid = self._next(code)
        item = {'id': iid, 'type': type_, 'name': name, 'location': location, 'availableUntil': until,
                'hint': hint, 'spoilerLevel': level, 'sources': list(sources)}
        if steps:
            item['steps'] = [{'text': s} for s in steps]
        self.data['items'].append(item)
        return iid

    def set_steps(self, item_id, steps, source=None):
        """Adds a route to an existing item (used for hand-written chapters). Append-only once published."""
        item = next(i for i in self.data['items'] if i['id'] == item_id)
        item['steps'] = [{'text': s} for s in steps]
        if source and source not in item['sources']:
            item['sources'].append(source)

    def write(self):
        path = ROOT / 'sc' / 'chapters' / f'ch-{self.order:02d}.json'
        path.write_text(json.dumps(self.data, ensure_ascii=False, indent=2) + '\n')
        registry_path = ROOT / 'id-registry.json'
        registry = json.loads(registry_path.read_text())
        extra = [e['id'] for key in ('bosses', 'fish', 'recipes') for e in self.data.get(key, [])]
        ids = [self.id] + [c['id'] for c in self.data['checkpoints']] + [i['id'] for i in self.data['items']] + extra
        registry += [i for i in ids if i not in registry]
        registry_path.write_text(json.dumps(registry, indent=2) + '\n')
        d = self.data
        print(f'{path.name}: {len(d["checkpoints"])} checkpoints, {len(d["items"])} items, '
              f'{len(d.get("bosses", []))} bosses, {len(d.get("fish", []))} fish, '
              f'{len(d.get("fishSpots", []))} spots, {len(d.get("recipes", []))} recipes')
