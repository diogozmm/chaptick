"""Which trophy each checklist item counts toward, per game (trophy ids from content/<game>/game.json).

Applied by Chapter.write(), so regenerating a chapter keeps its tags. To retag existing chapter
files without regenerating them:  python3 trophies.py <gameId>
Rules match on English names; adding a field changes no id, so this is safe after publishing.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'content'


def _sc(item):
    en, kind = item['name']['en'], item['type']
    tags = []
    if kind in ('quest', 'hidden_quest'):
        tags += ['quest-master', 'a-rank-bracer']
    if en.startswith('Bonus BP'):
        tags.append('a-rank-bracer')
    if re.match(r'(Liberl News|Gambler Jack)', en):
        tags.append('book-master')
    if 'treasure chests' in en:
        tags.append('treasure-hunter')
    if en.startswith('Recipe'):
        tags.append('three-star-chef')
    return tags


def _ysx(item):
    # EX quests are left out: the guide does not say whether Proud's EX quests count.
    en, kind = item['name']['en'], item['type']
    tags = []
    if kind == 'quest' and not en.startswith('EX:'):
        tags.append('go-to-guy-and-gal')
    if 'character note' in en:
        tags.append('seashell-networker')
    if kind == 'collectible' and ('treasure' in en.lower() or 'chests' in en):
        tags.append('no-hewnstone-unturned')
    if en.startswith('Ship upgrades'):
        tags.append('all-decked-out')
    return tags


RULES = {'sc': _sc, 'ysx': _ysx}


def apply(game, data):
    rule = RULES.get(game)
    if not rule:
        return
    for item in data['items']:
        tags = rule(item)
        if tags:
            item['trophies'] = tags
        else:
            item.pop('trophies', None)


if __name__ == '__main__':
    game = sys.argv[1]
    for path in sorted((ROOT / game / 'chapters').glob('ch-*.json')):
        data = json.loads(path.read_text())
        apply(game, data)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
        print(f'{path.name}: {sum(1 for i in data["items"] if i.get("trophies"))} tagged')
