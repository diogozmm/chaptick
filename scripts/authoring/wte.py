# Welcome to Elderfield — built from pages saved by hand (never fetched by a script):
#   the Welcome to Elderfield Wiki (wiki.gg, CC BY-SA 4.0): Items/*, Crafting, Cooking, Forging,
#   Treasure and an Special:Export of the enemy pages;
#   the Neoseeker task guides (Beginner, General, Job Board, Long-Term).
# Facts only, as structured data (kind of source, place, shop, station); flavor text is not copied.
#
# Progress is by area, not story chapter: each "chapter" file is an area group, in the order the
# game opens them (confirmed by a player). Everything is placed in the earliest area where it can
# be obtained, so nothing from a later area shows up early.
#
# Checklist items (tasks, treasure maps) are append-only like every other game: ids follow the
# order below, so new tasks may only be added at the end of their area's list. Compendium ids
# (entries, crafts, creatures) are slugs of the official name: they hold no progress.
#
# Usage: python3 scripts/authoring/wte.py [folder with the saved pages]
import glob
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import wte_pt as PT
import wte_tasks_pt as TASKS
from lib import ROOT, t

PT.TASK_NAMES.update(TASKS.TASK_NAMES)

G = 'wte'
PAGES = Path(sys.argv[1] if len(sys.argv) > 1 else Path.home() / 'Downloads' / 'Elderfield')
WIKI = 'wiki: Welcome to Elderfield Wiki (wiki.gg, CC BY-SA 4.0)'
NEO = 'guide: Neoseeker Welcome to Elderfield'

# Area names, in the order the game opens them. A player chose to show them, locked ones included.
LABELS = [
    t('Town, Farm & Lakefront', 'Cidade, Fazenda e Beira do Lago'),
    t('Mall, Mines & Sewers', 'Shopping, Minas e Esgotos'),
    t('Old Woods & Catacombs', 'Bosque Antigo e Catacumbas'),
    t('Mall Basement & Sealed Passage', 'Subsolo do Shopping e Passagem Selada'),
    t('Deep Woods & Deep Catacombs', 'Floresta Profunda e Catacumbas Profundas'),
]

# Place names → area index. Checked longest first, so "Deep Catacombs" wins over "Catacombs".
PLACES = {
    0: ['Farm Path', 'Farmhouse', 'Farm', 'Workshop', 'Lakefront', 'Ranch', 'Town', 'TownSouth', "Klaus's House",
        'Library', 'Greystone Estates', 'Elderfield High', 'Classroom', 'Laundry', 'Saloon', 'General Store',
        'Fancy House', 'Art Gallery', 'Music Store', 'Park', 'Apartment', 'Home', 'Basement', 'Farming Shop',
        'Seed Shop', 'Ranch Shop', 'Nursery', 'Pet Shop', 'Farmer Hans', 'Old Man Crawford', 'Chef Elroy',
        'Fisherman Herb', 'Abandoned Building', 'Job Board', 'Bait Shop', 'Lemonade Stand'],
    1: ['Mall', 'Mall Outside', 'Mall Floor', 'Mall Mines', 'Mine 1', 'Mine F', 'Beginner Mines', 'Mines', 'Sewers',
        'Food Cart', 'Grocery Store', 'Snack Shop', 'Vending Machine', 'Mining Shop', 'Mall Rat', 'Soggy Slice',
        'Garbage', 'Rooftop', 'Office'],
    2: ['Old Woods', 'Campsite', 'Catacombs', 'Shrine', 'Woodsman', 'Mill', 'Cabin', 'Clearing', 'Professor Dayton'],
    3: ['Deep Mall', 'Mall BF', 'Sealed Passage', 'Mall basement'],
    4: ['Deep Woods', 'DeepWoods', 'Deep Catacombs', 'Hidden Manor', 'Deep Woods Village', 'Eternal Lantern', 'Daeus'],
}
_PLACE_RE = sorted(((p, a) for a, ps in PLACES.items() for p in ps), key=lambda x: -len(x[0]))


def areas_in(text):
    """Every area a text mentions, matching the longest place names first."""
    found, rest = set(), text
    for place, area in _PLACE_RE:
        pattern = r'\b' + re.escape(place) + r'\b'
        if re.search(pattern, rest):
            found.add(area)
            rest = re.sub(pattern, ' ', rest)
    return found


# --- HTML tables --------------------------------------------------------------------------------
class _Tables(HTMLParser):
    """Top-level tables with the heading each sits under; images become their alt text."""

    def __init__(self):
        super().__init__()
        self.tables, self.cur, self.row, self.cell, self.depth = [], None, None, None, 0
        self.head, self.inh, self.htext = '', None, []

    def handle_starttag(self, tag, attrs):
        if tag in ('h2', 'h3', 'h4') and self.depth == 0:
            self.inh, self.htext = tag, []
        if tag == 'table':
            self.depth += 1
            if self.depth == 1:
                self.cur = {'head': self.head, 'rows': []}
        if self.depth == 1:
            if tag == 'tr':
                self.row = []
            if tag in ('td', 'th'):
                self.cell = []
            if tag == 'br' and self.cell is not None:
                self.cell.append(' / ')

    def handle_endtag(self, tag):
        if tag == self.inh:
            self.head = re.sub(r'\s+', ' ', ''.join(self.htext)).replace('[edit | edit source]', '').strip()
            self.inh = None
        if self.depth == 1:
            if tag in ('td', 'th') and self.cell is not None:
                self.row.append(re.sub(r'\s+', ' ', ''.join(self.cell)).strip())
                self.cell = None
            if tag == 'tr' and self.row is not None:
                self.cur['rows'].append(self.row)
                self.row = None
        if tag == 'table':
            if self.depth == 1:
                self.tables.append(self.cur)
            self.depth -= 1

    def handle_data(self, data):
        if self.inh:
            self.htext.append(data)
        if self.cell is not None:
            self.cell.append(data)


def tables(name):
    parser = _Tables()
    parser.feed((PAGES / name).read_text(encoding='utf-8'))
    for table in parser.tables:
        header = None
        for row in table['rows']:
            if row and row[0] in ('Name', 'Item'):
                header = row
                continue
            if header and len(row) == len(header):
                yield table['head'], dict(zip(header, row))


def slug(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def clean_name(name):
    name = name.split(' / ')[-1] if name.startswith('File:') else name
    name = re.sub(r'^File:\S+\.png\s*', '', name)
    return re.sub(r'\s+', ' ', name.strip(' /')).strip()


# --- Sources ------------------------------------------------------------------------------------
# Each "How to obtain" cell runs several facts together; they are split on the phrases that start one.
STARTS = (r'Found or received:|Purchase from|Possible loot|Possible pickup|Possible result|Possible reward|'
          r'Possible drop|Possible small-crystal|Possible large-crystal|Fishing:|Foraging|Forage from|Craft at|'
          r'Craft \d|Cook via|Cook in|Prepare at|(?<!: )Process |(?<!: )Age |Collect from|Chop |(?<!: )(?<!at )(?<!in )Mine |'
          r'Harvest from|Reward for|Reward from|Reward or|Given by|(?<!: )Received|Found in|Loot from|A drop|Dropped|'
          r'(?<!: )Complet|Obtained during|'
          r'Starts pre-placed|Fishing treasure|Convert another|(?<!\()Tier \d')

KINDS = [  # (kind, pattern on the start of a fact)
    ('found', r'Found or received:|Found in|Starts pre-placed|Received'),
    ('shop', r'Purchase from'),
    ('loot', r'Possible loot|Possible pickup|Loot from|Fishing treasure|Tier \d'),
    ('random', r'Possible result|Possible reward|Possible small-crystal|Possible large-crystal|Possible drop'),
    ('fish', r'Fishing:'),
    ('forage', r'Foraging|Forage from'),
    ('craft', r'Craft|Prepare at|Convert another'),
    ('cook', r'Cook'),
    ('process', r'Process |Age '),
    ('gather', r'Collect from|Chop |Mine |Harvest from'),
    ('task', r'Reward for|Reward from|Reward or|Given by|Complet|Obtained during'),
    ('drop', r'A drop|Dropped'),
]
NOT_OBTAINABLE = re.compile(r'Not obtainable|No normal', re.I)


def tidy(text):
    text = re.sub(r'\s+', ' ', text).strip(' ;,.')
    text = re.sub(r'; availability may require progression or a shop unlock', ' (after an unlock)', text)
    text = re.sub(r'\(relative weight (\d+)(?:, maximum quantity (\d+))?\)', '', text)
    return text.strip(' ;,.')


# The game's four seasons; the pumpkin is the "mascot of the Season of the Witch".
SEASONS = {'Rebirth': 'spring', 'Harvest': 'summer', 'Witch': 'autumn', 'Death': 'winter'}


def parse_sources(cell):
    """Facts of one "How to obtain" cell as [{kind, where, area}]; area is None when no place is named."""
    out = []
    parts = re.split(r'(?=' + STARTS + ')', cell)
    for part in parts:
        part = part.strip()
        if not part or NOT_OBTAINABLE.search(part):
            continue
        kind = next((k for k, p in KINDS if re.match(p, part)), 'other')
        where = tidy(re.sub(r'^(Found or received:|Purchase from( the)?|Possible loot:?( in)?|Possible pickup( at)?|'
                            r'Fishing:|Foraging|Craft at( the)?|Cook via Cooking:|Cook in an? |Loot from|Given by|'
                            r'Reward (for|from|or loot during)( completing)?( the)?)\s*', '', part))
        source = {'kind': kind, 'where': where.strip('() ') if kind == 'forage' else where}
        if kind == 'fish':
            found = [s for name, s in SEASONS.items() if re.search(rf'\b{name}\b', where)]
            if found:
                source['seasons'] = found
            if re.search(r'nighttime', where):
                source['time'] = 'night'
            elif re.search(r'daytime', where):
                source['time'] = 'day'
        areas = areas_in(part)
        source['area'] = max(areas) if areas else None
        out.append(source)
    return out


# --- Entries (the item index) ------------------------------------------------------------------
CATEGORY_FILES = {
    'materials': 'Items:Materials', 'gems': 'Items:Gems', 'metals': 'Items:Metals', 'fish': 'Items:Fish',
    'crops': 'Items:Crops', 'seeds': 'Items:Seeds', 'food': 'Items:Food', 'potions': 'Items:Potions',
    'tools': 'Items:Tools and Utility',
}


def load_entries():
    entries = {}
    for category, prefix in CATEGORY_FILES.items():
        page = f'{prefix} - Welcome to Elderfield Wiki.html'
        for _, row in tables(page):
            name = clean_name(row['Name'])
            if not name or name in entries:
                continue
            sources = parse_sources(row.get('Location / How to Obtain', ''))
            if not sources:
                continue
            sell = row.get('Sell Price', '').split(' / ')[0].strip()
            entries[name] = {'name': name, 'category': category, 'sell': sell if re.match(r'^\d+g$', sell) else None,
                             'sources': sources}
    return entries


FORAGE_SEASONS = {'Spring': 'spring', 'Summer': 'summer', 'Autumn': 'autumn', 'Winter': 'winter'}


def add_foraging(entries):
    """The Foraging page lists every spot (and season) a forageable shows up in; item pages often
    miss them. One source per place, so each lands in its own area."""
    for head, row in tables('Foraging - Welcome to Elderfield Wiki.html'):
        name = clean_name(re.sub(r'\[[^\]]*\]', '', row['Name']))
        if name not in entries:
            continue
        season = FORAGE_SEASONS.get(head)
        known = {s['where'] for s in entries[name]['sources'] if s['kind'] == 'forage'}
        for place in [p.strip() for p in row.get('Location', '').split(',') if p.strip()]:
            if place in known:
                continue
            areas = areas_in(place)
            source = {'kind': 'forage', 'where': place, 'area': max(areas) if areas else None}
            if season:
                source['seasons'] = [season]
            entries[name]['sources'].append(source)


# --- Crafts (Crafting, Cooking, Forging) --------------------------------------------------------
def ingredients(cell):
    found = re.findall(r'(\d+)x\s+(?:\[[^\]]*\]\s*)?([A-Za-z][A-Za-z\'\- ]+?)(?=\s+\d+x|\s*/|\s*$)', cell)
    return [{'name': clean_name(n), 'qty': int(q)} for q, n in found]


def load_crafts():
    crafts = []
    pages = [('Crafting', 'craft'), ('Cooking', 'cook'), ('Forging', 'forge')]
    for page, kind in pages:
        for group, row in tables(f'{page} - Welcome to Elderfield Wiki.html'):
            name = clean_name(re.sub(r'\[[^\]]*\]', '', row.get('Name') or row.get('Item', '')))
            ing = ingredients(row.get('Ingredients', ''))
            if not name or not ing:
                continue
            unlock = tidy(row.get('How to Obtain') or row.get('Recipe Source') or '')
            crafts.append({'name': name.split(' x')[0].strip(), 'kind': kind, 'group': group, 'ingredients': ing,
                           'unlock': '' if unlock.lower() == 'placeholder' else unlock})
    return crafts


# --- Creatures (enemy pages export) -------------------------------------------------------------
CREATURE_AREAS = {'Town and Farm': 0, 'Mall': 1, 'Sewers': 1, 'Mines': 1, 'The Old Woods': 2, 'Catacombs': 2,
                  'Mall BF': 3, 'Sealed Passage': 3, 'The Deep Woods': 4, 'Deep Catacombs': 4}


def load_creatures():
    xml = next(PAGES.glob('*.xml')).read_text(encoding='utf-8')
    creatures = []
    for title, text in re.findall(r'<title>(.*?)</title>.*?<text[^>]*>(.*?)</text>', xml, re.S):
        text = html.unescape(text)
        name = html.unescape(title).replace(' (Enemy)', '').strip('"')
        cats = re.findall(r'\[\[Category:(.+?) enemies\]\]', text)
        areas = [CREATURE_AREAS[c] for c in cats if c in CREATURE_AREAS]
        if not areas:
            continue  # seasonal events and special encounters: no place to look for them
        locs = re.search(r'! Locations\n\| (.+)', text)
        where = [re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]+)\]\]', r'\1', l).strip()
                 for l in (locs.group(1).split('<br>') if locs else [])]
        rewards = []
        steal = re.search(r'=== Stealable items ===(.*?)(?:<!--|\n==)', text, re.S)
        if steal:
            for variant, item, chance in re.findall(r'\| ([^|\n]+?) \|\| .*?\[\[([^\]|]+)\]\] \|\| (\d+%)', steal.group(1)):
                rewards.append({'how': 'steal', 'items': [item], 'chance': chance, 'variant': variant.strip()})
        for row in re.findall(r'\n\| ([^\n]*?) \|\| ([^\n]*?) \|\| [^\n]*? \|\| ([^\n]*Items received:[^\n]*)', text):
            situation, when, results = row
            got = re.search(r"'''Items received:'''(.*?)(?:<br>|$)", results)
            needs = re.search(r"'''Required or removed:'''(.*?)(?:<br>|$)", results)
            reward = {'how': 'event', 'items': re.findall(r'Item sprite\|([^|}]+)', got.group(1)), 'situation': situation.strip()}
            if when.strip() and when.strip() != 'During the listed interaction':
                reward['when'] = when.strip()
            if needs:
                reward['gives'] = re.findall(r'Item sprite\|([^|}]+)', needs.group(1))
            rewards.append(reward)
        unique = []
        for reward in rewards:
            if reward not in unique:
                unique.append(reward)
        rewards = unique
        where = [w for w in where if w and 'No normal encounter' not in w]
        creatures.append({'name': name, 'area': min(areas), 'where': where or [c for c in cats if c in CREATURE_AREAS],
                          'rewards': rewards})
    return sorted(creatures, key=lambda c: c['name'])


# --- Tasks (Neoseeker) --------------------------------------------------------------------------
def strip_tags(s):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()


def load_tasks():
    tasks = []
    for path in sorted(PAGES.glob('*Tasks*Neoseeker.html')):
        page = path.read_text(encoding='utf-8')
        page = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', page, flags=re.S)
        heads = list(re.finditer(r'<h2[^>]*>(.*?)</h2>', page, re.S))
        for i, head in enumerate(heads):
            body = page[head.end(): heads[i + 1].start() if i + 1 < len(heads) else len(page)]
            giver = re.search(r'<b>Task giver:</b>(.*?)<b>Location:</b>(.*?)</p>', body, re.S)
            if not giver:
                continue
            name = strip_tags(head.group(1))
            req = re.search(r'<b>Requirements:</b>(.*?)</p>', body, re.S)
            obj = re.search(r'<h3[^>]*>(?:<span[^>]*>)?Objectives(?:</span>)?</h3>(.*?)(?:<h[23]|<p><b>Reward|$)', body, re.S)
            objectives = [strip_tags(li) for li in re.findall(r'<li>(.*?)</li>', obj.group(1), re.S)] if obj else []
            objectives = [o.rstrip('.') for o in objectives if not re.match(r'speak to .+ to claim', o, re.I)]
            reward = re.search(r'<b>Reward:</b>(.*?)</p>', body, re.S)
            fails = re.search(r'<b>fails ([^<]+)</b>', body)
            text = ' '.join([strip_tags(giver.group(2)), strip_tags(req.group(1)) if req else '', *objectives])
            areas = areas_in(text)
            tasks.append({
                'name': name, 'giver': strip_tags(giver.group(1)), 'location': strip_tags(giver.group(2)),
                'objectives': objectives, 'reward': strip_tags(reward.group(1)) if reward else '',
                'fails': strip_tags(fails.group(1)) if fails else '', 'area': max(areas) if areas else 0,
                'page': path.name.split(' - ')[1] if ' - ' in path.name else path.stem,
            })
    return tasks


def load_treasure():
    maps = []
    parser = _Tables()
    parser.feed((PAGES / 'Treasure - Welcome to Elderfield Wiki.html').read_text(encoding='utf-8'))
    for table in parser.tables:
        rows = table['rows']
        if not rows or rows[0][0] != 'Treasure Maps':
            continue
        for row in rows[1:]:
            name, _, how, loot, where = (row + [''] * 5)[:5]
            if not re.match(r'^Treasure Map \d+$', name):
                continue  # the wiki's own notes to editors
            areas = areas_in(how + ' ' + where)
            maps.append({'name': name, 'how': how, 'loot': re.sub(r'\[[^\]]*\]\s*', '', loot), 'where': where,
                         'area': max(areas) if areas else 0})
    return maps


# --- Placement ----------------------------------------------------------------------------------
def place(entries, crafts, tasks=()):
    """Area of every entry: the earliest of its sources. Task rewards take the task's area; made-only
    items take the latest area among their ingredients, resolved repeatedly until nothing changes."""
    by_name = {c['name']: c for c in crafts}
    task_area = {task['name'].lower(): task['area'] for task in tasks}
    for e in entries.values():
        for s in e['sources']:
            named = [task_area[n.lower()] for n in re.findall(r'"([^"]+)"', s['where']) if n.lower() in task_area]
            if s['area'] is None and named:
                s['area'] = max(named)
        known = [s['area'] for s in e['sources'] if s['area'] is not None]
        e['area'] = min(known) if known else None
    # Processed goods name what they are made from ("Age Wine (Grape) in a Cask"): they inherit it.
    names = sorted(entries, key=len, reverse=True)

    def inputs(name, e):
        text, found = ' '.join(s['where'] for s in e['sources']), []
        for other in names:
            if other != name and re.search(r'(?<![\w(])' + re.escape(other) + r'(?![\w)])', text):
                found.append(other)
                text = text.replace(other, ' ')
        return found

    for _ in range(10):
        changed = False
        for name, e in entries.items():
            if e['area'] is not None:
                continue
            craft = by_name.get(name)
            used = [i['name'] for i in craft['ingredients'] if i['name'] in entries] if craft else inputs(name, e)
            areas = [entries[n]['area'] for n in used]
            if areas and None not in areas:
                e['area'] = max(areas)
                changed = True
        if not changed:
            break
    for c in crafts:
        areas = [entries[i['name']]['area'] for i in c['ingredients'] if i['name'] in entries]
        areas = [a for a in areas if a is not None] + list(areas_in(c['unlock']))
        c['area'] = max(areas) if areas else 0
    unplaced = sorted(n for n, e in entries.items() if e['area'] is None)
    for name in unplaced:
        entries[name]['area'] = 0
    return unplaced


# --- Output -------------------------------------------------------------------------------------
KIND_LABEL = {'craft': 'Crafting', 'cook': 'Cooking', 'forge': 'Forge'}



GROUPS = {
    'Utility': 'Utilidades', 'Scarecrows': 'Espantalhos', 'Decorative': 'Decoração', 'Large Objects': 'Objetos grandes',
    'Witching Mortar': 'Pilão de Bruxaria', 'Prep Table': 'Mesa de Preparo', 'Compost Bin': 'Composteira', 'God Forge': 'Forja Divina',
    'Materials': 'Materiais', 'Shelters': 'Abrigos', 'General': 'Geral', 'Blessings': 'Bênçãos', 'Flasks': 'Frascos',
    "Tinker's Desk": 'Mesa do Inventor', 'Basic Ingredients': 'Ingredientes básicos', 'Cooking Pot': 'Panela', 'Juicer': 'Espremedor',
    'Oven': 'Forno', 'Coffee Maker': 'Cafeteira', 'Weapons': 'Armas', 'Armor': 'Armaduras', 'Accessories': 'Acessórios',
}
KEY_ITEMS = {
    'Skull of the Deep': 'Crânio das Profundezas', 'Skull of the Lost': 'Crânio dos Perdidos', 'Skull of the Dark': 'Crânio das Trevas',
    'Skull of the Mall': 'Crânio do Shopping', 'Skull of the Woods': 'Crânio da Floresta', 'Lost Supplies': 'Suprimentos Perdidos',
    'Essence of Daeus': 'Essência de Daeus', 'Essence of Delvek': 'Essência de Delvek', 'Damp Nails': 'Pregos Úmidos',
    'Living Soul': 'Alma Viva', 'Gold Coin of Death': 'Moeda de Ouro da Morte', 'New Doll': 'Boneca Nova',
    'Palewood Branch': 'Galho de Madeira Pálida',
}
PT.WORDS.update(KEY_ITEMS)
WHEN = {
    'the required item is available': 'com o item pedido em mãos',
    'an earlier stage of this interaction is complete': 'depois da etapa anterior da conversa',
    'Sophia Apology ≥ 2': 'Desculpas da Sophia ≥ 2',
}


def both(en, pt):
    return t(en, pt if pt and pt != en else None)


def localized_source(source, names):
    out = {k: v for k, v in source.items() if k not in ('area', 'where')}
    return {'kind': out.pop('kind'), 'where': both(source['where'], PT.source_pt(source['where'], names)), **out}


def creature_reward(reward, known_ids):
    """One way a creature gives items: stolen in battle (with chance), or at an event."""
    item = lambda n: {**({'entryId': known_ids[n]} if n in known_ids else {}), 'name': PT.t2(n)}
    out = {'how': reward['how'], 'items': [item(n) for n in reward['items']]}
    if reward.get('chance'):
        out['chance'] = reward['chance']
    if reward.get('variant'):
        out['variant'] = both(reward['variant'], PT.terms_pt(reward['variant'].replace('Level', 'Nível')))
    if reward.get('situation'):
        out['situation'] = both(reward['situation'], PT.place_pt(reward['situation']))
    if reward.get('when'):
        when = re.sub(r'\{\{Item sprite\|([^|}]+)[^}]*\}\} is active', r'\1 is active', reward['when'])
        pt = WHEN.get(when) or re.sub(r'^(.+) is active$', lambda m: f'com {PT.tr(m[1]) or m[1]} em andamento', when)
        out['when'] = both(when, pt)
    if reward.get('gives'):
        out['gives'] = [item(n) for n in reward['gives']]
    return out


def task_item(task, next_id):
    lines = TASKS.LINES
    steps_en = '; '.join(task['objectives'])
    steps_pt = '; '.join(lines.get(o, o) for o in task['objectives'])
    hint_en = f'Objectives: {steps_en}' if steps_en else 'Talk to the task giver to start it'
    hint_pt = f'Objetivos: {steps_pt}' if steps_pt else 'Fale com quem dá a tarefa para começar'
    if task['reward']:
        reward_en = TASKS.REWARD_EN.get(task['reward'], task['reward']).rstrip('.')
        hint_en += f'. Reward: {reward_en}'
        hint_pt += f". Recompensa: {lines.get(task['reward'], task['reward']).rstrip('.')}"
    if task['fails']:
        failed = task['fails'].removesuffix('.')
        hint_en += f'. Careful: accepting it fails {failed}'
        hint_pt += f'. Atenção: aceitar esta faz falhar a tarefa {TASKS.TASK_NAMES.get(failed, failed)}'
    kind = 'missable' if task['fails'] else 'quest'
    location_pt = f"{PT.place_pt(task['giver'])} — {lines.get(task['location'], task['location'])}"
    return {'id': next_id('mi' if kind == 'missable' else 'q'), 'type': kind,
            'name': t(task['name'], TASKS.TASK_NAMES.get(task['name'])),
            'location': both(f"{task['giver']} — {task['location']}", location_pt), 'availableUntil': None,
            'hint': t(hint_en + '.', hint_pt + '.'), 'spoilerLevel': 0, 'sources': [f"{NEO}: {task['page']}"]}


def map_item(m, next_id):
    n = int(m['name'].split()[-1])
    (how_en, how_pt), where = TASKS.MAPS[n]
    loot = [(q, name.strip()) for q, name in re.findall(r'(\d+)x ([^,]+?)(?:,|\.?$)', m['loot'])]
    loot_en = ', '.join(f'{q}× {name}' for q, name in loot)
    loot_pt = ', '.join(f'{q}× {PT.tr(name) or name}' for q, name in loot)
    hint_en, hint_pt = f'How to get it: {how_en}', f'Como conseguir: {how_pt}'
    if loot:
        hint_en += f' Inside: {loot_en}.'
        hint_pt += f' Conteúdo: {loot_pt}.'
    return {'id': next_id('co'), 'type': 'collectible', 'name': t(m['name'], f'Mapa do Tesouro {n}'),
            'location': t(*where) if where else t('Marked on the map', 'Indicado no mapa'), 'availableUntil': None,
            'hint': t(hint_en, hint_pt), 'spoilerLevel': 1, 'sources': [f'{WIKI}: Treasure']}


def build():
    entries, crafts, tasks = load_entries(), load_crafts(), load_tasks()
    add_foraging(entries)
    unplaced = place(entries, crafts, tasks)
    creatures, maps = load_creatures(), load_treasure()
    known_ids = {name: f'{G}-{slug(name)}' for name in entries}

    chapters = []
    names = set(entries) | {c['name'] for c in crafts} | {i['name'] for c in crafts for i in c['ingredients']}
    for order in range(len(LABELS)):
        ch_id = f'{G}-ch{order}'
        items, counters = [], {}

        def next_id(code):
            counters[code] = counters.get(code, 0) + 1
            return f'{ch_id}-{code}-{counters[code]:02d}'

        for task in [x for x in tasks if x['area'] == order]:
            items.append(task_item(task, next_id))
        for m in [x for x in maps if x['area'] == order]:
            items.append(map_item(m, next_id))

        ch_entries, extra = [], []
        for name, e in sorted(entries.items()):
            mine = [s for s in e['sources'] if (s['area'] if s['area'] is not None else e['area']) == order]
            if not mine and e['area'] != order:
                continue
            clean = [localized_source(s, names) for s in mine]
            if e['area'] == order:
                entry = {'id': known_ids[name], 'name': PT.t2(name), 'category': e['category'], 'sources': clean}
                if e['sell']:
                    entry['sell'] = e['sell']
                ch_entries.append(entry)
            else:
                extra.extend({'entryId': known_ids[name], **s} for s in clean)

        ch_crafts = []
        for c in [x for x in crafts if x['area'] == order]:
            craft = {'id': f"{G}-{c['kind']}-{slug(c['name'])}", 'name': PT.t2(c['name']), 'kind': c['kind'],
                     'group': t(c['group'], GROUPS.get(c['group'])), 'ingredients': [
                         {**({'entryId': known_ids[i['name']]} if i['name'] in known_ids else {}),
                          'name': PT.t2(i['name']), 'qty': i['qty']} for i in c['ingredients']]}
            if c['name'] in known_ids:
                craft['makes'] = known_ids[c['name']]
            if c['unlock']:
                unlock = c['unlock'].rstrip(' /.')
                craft['unlock'] = both(unlock, TASKS.UNLOCKS.get(c['unlock']) or TASKS.UNLOCKS.get(unlock)
                                       or PT.source_pt(unlock, names))
            ch_crafts.append(craft)

        ch_creatures = []
        for c in [x for x in creatures if x['area'] == order]:
            # Creatures are shown by name (a player asked not to mask them).
            creature = {'id': f"{G}-cr-{slug(c['name'])}", 'name': t(c['name'], PT.CREATURES.get(c['name'])),
                        'where': [both(w, PT.place_pt(w)) for w in c['where']], 'spoilerLevel': 0}
            if c['rewards']:
                creature['rewards'] = [creature_reward(r, known_ids) for r in c['rewards']]
            ch_creatures.append(creature)

        chapter = {'id': ch_id, 'gameId': G, 'order': order, 'neutralLabel': LABELS[order], 'checkpoints': [],
                   'items': items, 'itemTexts': [], 'entries': ch_entries}
        if extra:
            chapter['entrySources'] = extra
        if ch_crafts:
            chapter['crafts'] = ch_crafts
        if ch_creatures:
            chapter['creatures'] = ch_creatures
        chapters.append(chapter)

    # Crafts may name ingredients that only exist further ahead; keep references pointing backwards.
    area_of = {known_ids[n]: e['area'] for n, e in entries.items()}
    for ch in chapters:
        for c in ch.get('crafts', []):
            for i in c['ingredients']:
                if 'entryId' in i and area_of[i['entryId']] > ch['order']:
                    del i['entryId']
            if 'makes' in c and area_of[c['makes']] > ch['order']:
                del c['makes']
        for c in ch.get('creatures', []):
            for r in c.get('rewards', []):
                for i in [*r['items'], *r.get('gives', [])]:
                    if 'entryId' in i and area_of[i['entryId']] > ch['order']:
                        del i['entryId']

    out = ROOT / G / 'chapters'
    out.mkdir(parents=True, exist_ok=True)
    for ch in chapters:
        (out / f"ch-{ch['order']:02d}.json").write_text(json.dumps(ch, ensure_ascii=False, indent=2) + '\n')

    registry_path = ROOT / 'id-registry.json'
    registry = json.loads(registry_path.read_text())
    ids = [G] + [i['id'] for ch in chapters for i in [{'id': ch['id']}, *ch['items']]]
    added = [i for i in ids if i not in registry]
    registry_path.write_text(json.dumps(registry + added, indent=2) + '\n')

    print(f"entries {len(entries)}, crafts {len(crafts)}, creatures {len(creatures)}, tasks {len(tasks)}, "
          f"treasure maps {len(maps)}; ids registered: {len(added)}")
    for ch in chapters:
        print(f"  {ch['id']}: {len(ch['items'])} items, {len(ch['entries'])} entries, "
              f"{len(ch.get('entrySources', []))} later sources, {len(ch.get('crafts', []))} crafts, "
              f"{len(ch.get('creatures', []))} creatures")
    if unplaced:
        # Shown from area 1 on: better visible a little early than missing. Listed for a player to check.
        report = Path(__file__).with_name('wte-unplaced.txt')
        report.write_text('\n'.join(unplaced) + '\n')
        print(f'  {len(unplaced)} entries name no place; put in area 1 and listed in {report.name}')


if __name__ == '__main__':
    build()
