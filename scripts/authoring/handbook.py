"""Combat Handbook entries of Trails in the Sky 2nd Chapter, one checklist item per chapter.

The enemy list (battle-notes.json: chapter order -> [name, level]) comes from the guide's Battle
Notes page, 410 entries in all. Chapters 8 and 9 build the item through `add(chapter)`; the older
chapter files were edited by hand after they were generated, so `python3 handbook.py` appends the
item to their JSON directly (idempotent, ids and registry untouched apart from the new id).
"""
import json
import re
import sys
from pathlib import Path

from lib import ROOT, src, t

DATA = json.loads((Path(__file__).with_name('battle-notes.json')).read_text())
LABELS = {
    0: ('Le Locle', 'Le Locle'), 1: ('Ruan', 'Ruan'), 2: ('Zeiss', 'Zeiss'), 3: ('Grancel', 'Grancel'), 4: ('Rolent', 'Rolent'),
    5: ('Bose', 'Bose'), 6: ('Chapter 6', 'Capítulo 6'), 7: ('Chapter 7', 'Capítulo 7'), 8: ('all of Liberl', 'todo Liberl'),
    9: ('Liber Ark', 'Liber Ark'),
}
SOURCE = src('Battle Notes')


def fields(order):
    """Everything a handbook item holds, as the JSON dict minus its id."""
    entries = DATA[str(order)]
    en, pt = LABELS[order]
    name = t(f'Combat Handbook: {en} ({len(entries)})', f'Combat Handbook: {pt} ({len(entries)})')
    hint = t(f'Record all {len(entries)} enemies of this chapter in the Combat Handbook, then tick them here.',
             f'Registre os {len(entries)} inimigos deste capítulo no Combat Handbook e marque-os aqui.')
    guidance = {
        'overview': t('The list names every enemy of the chapter, some of which give the story away, so it stays hidden until you open it. '
                      'Fill the handbook before moving on: some enemies cannot be met again. Do not forget the Shining Poms and their Shining Pom+ versions.',
                      'A lista traz todos os inimigos do capítulo, alguns dos quais entregam a história, por isso ela fica escondida até você abri-la. '
                      'Preencha o handbook antes de seguir adiante: alguns inimigos não voltam a aparecer. Não esqueça dos Shining Poms e das versões Shining Pom+.'),
    }
    return {
        'type': 'collectible', 'name': name, 'location': t('Combat Handbook, in the camp menu', 'Combat Handbook, no menu de acampamento'),
        'availableUntil': None, 'hint': hint, 'spoilerLevel': 2, 'sources': [SOURCE],
        'steps': [{'text': t(f'{n} (Lv. {lv})')} for n, lv in entries], 'guidance': guidance, 'trophies': ['battle-master'],
    }


def add(chapter):
    """For a chapter built by its own script: call after the other items so the id comes last."""
    f = fields(chapter.order)
    return chapter.item('collectible', f['name'], f['location'], None, f['hint'], f['spoilerLevel'], f['sources'],
                        steps=[s['text'] for s in f['steps']], trophies=f['trophies'], guidance=f['guidance'])


def append_to_json(order, game='sc'):
    path = ROOT / game / 'chapters' / f'ch-{order:02d}.json'
    data = json.loads(path.read_text())
    f = fields(order)
    if any(i['name']['en'].startswith('Combat Handbook') for i in data['items']):
        return False
    last = max((int(m.group(1)) for i in data['items'] if (m := re.fullmatch(rf'{game}-ch{order}-co-(\d+)', i['id']))), default=0)
    item = {'id': f'{game}-ch{order}-co-{last + 1:02d}', **f}
    data['items'].append(item)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    registry_path = ROOT / 'id-registry.json'
    registry = json.loads(registry_path.read_text())
    if item['id'] not in registry:
        registry.append(item['id'])
        registry_path.write_text(json.dumps(registry, indent=2) + '\n')
    print(f'{path.name}: added {item["id"]} ({len(f["steps"])} entries)')
    return True


if __name__ == '__main__':
    for order in range(8):
        append_to_json(order)
