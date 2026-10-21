"""Bracer quest corrections for Trails in the Sky 2nd Chapter (Neoseeker Bracer Quests).

The page lists 87 quests and 452 BP in total, while Rank A needs 450, so a missing 5 BP quest can
cost the A-Rank Bracer trophy. Chapters 5 and 6 were edited by hand after they were generated, so
their JSON is the source and this script patches it. Ids and steps are untouched. Idempotent.

  * Mine Mop Up (chapter 6) never said it gives 6 BP.
  * Ravennue Trail Monster (chapter 5, 5 BP) was missing. The page gives no route for it, so the
    item says what is confirmed and where to look.
"""
import json

from lib import ROOT, src, t

SOURCE = src('Bracer Quests')


def load(order):
    path = ROOT / 'sc' / 'chapters' / f'ch-{order:02d}.json'
    return path, json.loads(path.read_text())


path, ch6 = load(6)
mop_up = next(i for i in ch6['items'] if i['name']['en'] == 'Mine Mop Up')
if 'BP' not in mop_up['hint']['en']:
    mop_up['hint'] = {k: f'{prefix} {mop_up["hint"][k]}' for k, prefix in (('en', 'Reward: +6 BP.'), ('pt', 'Recompensa: +6 BP.'))}
    mop_up['guidance']['rewards'] = [t('+6 BP.', '+6 BP.')]
    mop_up['sources'].append(SOURCE)
path.write_text(json.dumps(ch6, ensure_ascii=False, indent=2) + '\n')

path, ch5 = load(5)
if not any(i['name']['en'] == 'Ravennue Trail Monster' for i in ch5['items']):
    ch5['items'].append({
        'id': 'sc-ch5-q-07', 'type': 'quest', 'name': t('Ravennue Trail Monster'),
        'location': t('Bose region — Ravennue Trail', 'Região de Bose — Ravennue Trail'),
        'availableUntil': None,
        'hint': t('Reward: +5 BP. A monster request listed for this chapter in the Bracer Notebook. No route is confirmed yet, so check the notebook in the game.',
                  'Recompensa: +5 BP. Um pedido de monstro listado neste capítulo no Bracer Notebook. Ainda não há rota confirmada, então confira o caderno no jogo.'),
        'spoilerLevel': 0, 'sources': [SOURCE],
        'guidance': {
            'rewards': [t('+5 BP.', '+5 BP.')],
            'overview': t('A monster request listed for this chapter in the Bracer Notebook. No route is confirmed yet, so check the notebook in the game.',
                          'Um pedido de monstro listado neste capítulo no Bracer Notebook. Ainda não há rota confirmada, então confira o caderno no jogo.'),
            'warnings': [t('Rank A needs 450 of the 452 BP in the game, so skipping a 5 BP request puts the A-Rank Bracer trophy at risk.',
                           'O Rank A exige 450 dos 452 BP do jogo, então pular um pedido de 5 BP coloca o troféu A-Rank Bracer em risco.')],
        },
        'trophies': ['quest-master', 'a-rank-bracer'],
    })
path.write_text(json.dumps(ch5, ensure_ascii=False, indent=2) + '\n')

registry_path = ROOT / 'id-registry.json'
registry = json.loads(registry_path.read_text())
if 'sc-ch5-q-07' not in registry:
    registry_path.write_text(json.dumps(registry + ['sc-ch5-q-07'], indent=2) + '\n')
print('quests patched')
