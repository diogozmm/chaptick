"""Tiny helpers to author chapter files. Output is plain JSON validated by content/schema."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'content'


def t(en, pt=None):
    return {'en': en, 'pt': pt} if pt else {'en': en}


def src(page):
    return f'guide: Neoseeker SC walkthrough, {page}'


class Chapter:
    def __init__(self, order, en, pt):
        self.order = order
        self.id = f'sc-ch{order}'
        self.data = {'id': self.id, 'gameId': 'sc', 'order': order, 'neutralLabel': t(en, pt),
                     'checkpoints': [], 'items': [], 'itemTexts': []}
        self.counters = {}

    def cp(self, en, pt):
        n = len(self.data['checkpoints']) + 1
        cid = f'{self.id}-cp-{n:02d}'
        self.data['checkpoints'].append({'id': cid, 'order': n, 'neutralDescription': t(en, pt)})
        return cid

    def item(self, type_, name, location, until, hint, level=0, sources=()):
        code = {'quest': 'q', 'hidden_quest': 'hq', 'missable': 'mi', 'collectible': 'co'}[type_]
        self.counters[code] = self.counters.get(code, 0) + 1
        iid = f'{self.id}-{code}-{self.counters[code]:02d}'
        self.data['items'].append({'id': iid, 'type': type_, 'name': name, 'location': location,
                                   'availableUntil': until, 'hint': hint, 'spoilerLevel': level,
                                   'sources': list(sources)})
        return iid

    def write(self):
        path = ROOT / 'sc' / 'chapters' / f'ch-{self.order:02d}.json'
        path.write_text(json.dumps(self.data, ensure_ascii=False, indent=2) + '\n')
        registry_path = ROOT / 'id-registry.json'
        registry = json.loads(registry_path.read_text())
        ids = [self.id] + [c['id'] for c in self.data['checkpoints']] + [i['id'] for i in self.data['items']]
        registry += [i for i in ids if i not in registry]
        registry_path.write_text(json.dumps(registry, indent=2) + '\n')
        print(f'{path.name}: {len(self.data["checkpoints"])} checkpoints, {len(self.data["items"])} items')
