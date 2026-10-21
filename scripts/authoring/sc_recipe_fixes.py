"""Customized dishes missing from Trails in the Sky 2nd Chapter (Neoseeker Recipe List: 17 in all).

The chapter files were edited by hand after they were generated, so their JSON is the source and
this script patches it. Each dish is added after the last recipe of the chapter where its cook and
base dish are both available, so published ids do not change. Idempotent.
"""
import json
import re

from lib import ROOT, src, t

SOURCE = src('Recipe List')
COOKS = {
    'Estelle': ('Estelle', 'A Estelle'), 'Joshua': ('Joshua', 'O Joshua'), 'Scherazard': ('Scherazard', 'A Scherazard'),
    'Agate': ('Agate', 'O Agate'), 'Tita': ('Tita', 'A Tita'), 'Zin': ('Zin', 'O Zin'),
}
# chapter, dish, cook, base dish
MISSING = [
    (5, 'Exotic Fizz', 'Scherazard', 'Mighty Juice'),
    (5, 'Tiger Dragon Stir-Fry', 'Zin', 'Three-Egg Rice Porridge'),
    (6, 'Draconic Meatballs', 'Agate', 'Spicy Meatballs'),
    (6, 'Pom Pom Cookie', 'Tita', 'Green Cookie'),
    (7, 'Homemade Seafood Risotto', 'Estelle', 'Platinum Risotto'),
    (7, 'Plump Salisbury Steak', 'Joshua', "Victor's Steak"),
]

added = []
for order in sorted({m[0] for m in MISSING}):
    path = ROOT / 'sc' / 'chapters' / f'ch-{order:02d}.json'
    data = json.loads(path.read_text())
    recipes = data.setdefault('recipes', [])
    last = max((int(m.group(1)) for r in recipes if (m := re.fullmatch(rf'sc-ch{order}-re-(\d+)', r['id']))), default=0)
    for chapter, dish, cook, base in MISSING:
        if chapter != order or any(r['name']['en'] == dish for r in recipes):
            continue
        last += 1
        en, pt = COOKS[cook]
        recipes.append({
            'id': f'sc-ch{order}-re-{last:02d}', 'kind': 'customized', 'name': t(dish),
            'source': t(f'Have {en} cook {base}', f'{pt} cozinha {base}'), 'sources': [SOURCE],
        })
        added.append(recipes[-1]['id'])
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

registry_path = ROOT / 'id-registry.json'
registry = json.loads(registry_path.read_text())
new = [i for i in added if i not in registry]
if new:
    registry_path.write_text(json.dumps(registry + new, indent=2) + '\n')
print('recipes added:', added)
