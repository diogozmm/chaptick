"""Corrections to the Trails in the Sky 2nd Chapter chests, from the Neoseeker Treasure List (566 chests).

Chapters 1 to 7 were edited by hand after they were generated, so their JSON is the source and this
script patches it. It is idempotent. Published ids and step positions are untouched: steps are only
reworded in place or added at the end, items are only renamed or added after the last one.

  * Chapter 5: the Amberl Tower has 23 chests, not 22 (Star Rabbits was missing).
  * Chapter 6: the abandoned mine has one more chest, open only during "Mine Mop Up".
  * Chapter 7: the four tower counts are exact (the "~" came from an approximate source), and the
    chests that were described only as "a room with 5 chests" now list what they hold.

With these the chests add up to the game's 566: 29 + 55 + 50 + 34 + 55 + 71 + 31 + 110 + 0 + 131.
"""
import json
import re

from lib import ROOT, src, t

TREASURE = src('Treasure List')


def load(order):
    path = ROOT / 'sc' / 'chapters' / f'ch-{order:02d}.json'
    return path, json.loads(path.read_text())


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def item(data, item_id):
    return next(i for i in data['items'] if i['id'] == item_id)


def add_source(it):
    if TREASURE not in it['sources']:
        it['sources'].append(TREASURE)


def register(ids):
    path = ROOT / 'id-registry.json'
    registry = json.loads(path.read_text())
    new = [i for i in ids if i not in registry]
    if new:
        path.write_text(json.dumps(registry + new, indent=2) + '\n')


def reword(it, number, en, pt):
    step = it['steps'][number - 1]['text']
    step['en'], step['pt'] = en, pt


# Chapter 5 — Amberl Tower
path, ch5 = load(5)
amberl = item(ch5, 'sc-ch5-co-09')
amberl['name'] = {k: re.sub(r'\(\d+\)', '(23)', v) for k, v in amberl['name'].items()}
star = t("The third chest in the guide's order, right after Buster Gear — Star Rabbits (shoes)",
         'O terceiro baú na ordem do guia, logo depois do Buster Gear — Star Rabbits (sapatos)')
if not any(s['text']['en'] == star['en'] for s in amberl['steps']):
    amberl['steps'].append({'text': star})
add_source(amberl)
save(path, ch5)

# Chapter 6 — one more chest in the abandoned mine
path, ch6 = load(6)
if not any(i['id'] == 'sc-ch6-co-08' for i in ch6['items']):
    mop_up = next(i for i in ch6['items'] if i['name']['en'] == 'Mine Mop Up')
    ch6['items'].append({
        'id': 'sc-ch6-co-08', 'type': 'collectible',
        'name': t('Abandoned mine treasure chests (1)', 'Baú da mina abandonada (1)'),
        'location': t('Abandoned mine — beyond the east exit', 'Mina abandonada — depois da saída leste'),
        'availableUntil': mop_up['availableUntil'],
        'hint': t('One chest that only opens during "Mine Mop Up". The mine is not visited again afterwards.',
                  'Um baú que só abre durante "Mine Mop Up". A mina não é visitada de novo depois.'),
        'spoilerLevel': 0, 'sources': [TREASURE],
        'steps': [{'text': t('Beyond the east exit — EP Charge III', 'Depois da saída leste — EP Charge III')}],
        'trophies': ['treasure-hunter'],
    })
save(path, ch6)

# Chapter 7 — exact counts and the contents of the unlisted rooms
path, ch7 = load(7)
for item_id in ('sc-ch7-co-08', 'sc-ch7-co-09', 'sc-ch7-co-10', 'sc-ch7-co-11'):
    it = item(ch7, item_id)
    it['name'] = {k: v.replace('~', '') for k, v in it['name'].items()}
    add_source(it)
esmelas = item(ch7, 'sc-ch7-co-08')
reword(esmelas, 5, '3rd level, left fork: teleporter up to a room with 5 chests — EP Charge III, U-Material+, Regina Girders, All Sepith ×300, Tearal Balm',
       '3º nível, bifurcação esquerda: teletransporte até uma sala com 5 baús — EP Charge III, U-Material+, Regina Girders, All Sepith ×300, Tearal Balm')
reword(esmelas, 6, '3rd level, right fork then north: teleporter to another room with 5 chests — EP Charge IV, Blue Falcon, All Sepith ×300, Athelas Balm ×2, Tear All Balm',
       '3º nível, bifurcação direita e depois norte: teletransporte até outra sala com 5 baús — EP Charge IV, Blue Falcon, All Sepith ×300, Athelas Balm ×2, Tear All Balm')
carnelia = item(ch7, 'sc-ch7-co-09')
reword(carnelia, 1, '1st level, seven chests right ahead — Zeram Powder, EP Charge III ×2, All Sepith ×300, U-Material+ ×2, Tearal Balm, Athelas Balm ×2',
       '1º nível, sete baús logo à frente — Zeram Powder, EP Charge III ×2, All Sepith ×300, U-Material+ ×2, Tearal Balm, Athelas Balm ×2')
save(path, ch7)

register(['sc-ch6-co-08'])
print('sc chests patched')
