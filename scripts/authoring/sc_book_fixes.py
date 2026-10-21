"""Book List corrections for Trails in the Sky 2nd Chapter (Neoseeker Book List).

Volume 10 needs Kloe in the party, and most Gambler Jack volumes can be bought later if the first
chance was missed. Text only: ids and steps are untouched. Idempotent.
"""
import json

from lib import ROOT, src, t

SOURCE = src('Book List')
FALLBACK = {
    'sc-ch0-co-09': (1, "O'Neil Duty-Free Shop in Chapter 1", "a O'Neil Duty-Free Shop no Capítulo 1", '1,000', '1.000'),
    'sc-ch4-co-04': (6, "Rinon's General Goods in Chapter 5", "a Rinon's General Goods no Capítulo 5", '6,000', '6.000'),
    'sc-ch5-co-02': (7, 'Grocery Minuet in Chapter 6', 'a Grocery Minuet no Capítulo 6', '7,000', '7.000'),
    'sc-ch6-co-02': (8, 'Dalmore Company in Grancel in Chapter 8', 'a Dalmore Company, em Grancel, no Capítulo 8', '16,000', '16.000'),
    'sc-ch6-co-03': (9, 'Dalmore Company in Grancel in Chapter 8', 'a Dalmore Company, em Grancel, no Capítulo 8', '18,000', '18.000'),
    'sc-ch7-co-03': (10, 'Dalmore Company in Grancel in Chapter 8', 'a Dalmore Company, em Grancel, no Capítulo 8', '20,000', '20.000'),
}
KLOE = t('Kloe must be in the party.', 'A Kloe precisa estar na equipe.')


def patch(order):
    path = ROOT / 'sc' / 'chapters' / f'ch-{order:02d}.json'
    data = json.loads(path.read_text())
    for it in data['items']:
        if it['id'] not in FALLBACK:
            continue
        _, where_en, where_pt, price_en, price_pt = FALLBACK[it['id']]
        sentence = t(f'If you miss it, {where_en} sells it for {price_en} mira.', f'Se perder, {where_pt} vende por {price_pt} mira.')
        if 'sells it for' in it['hint']['en']:
            continue
        original = dict(it['hint'])
        it['hint'] = {k: f'{original[k]} {sentence[k]}' for k in ('en', 'pt')}
        if it['id'] == 'sc-ch7-co-03':
            it['hint'] = {k: f'{KLOE[k]} {it["hint"][k]}' for k in ('en', 'pt')}
        guidance = it.get('guidance')
        if guidance:
            guidance.setdefault('optional', []).append(sentence)
        elif it['id'] == 'sc-ch7-co-03':
            it['guidance'] = {'overview': original, 'requirements': [KLOE], 'optional': [sentence]}
        if SOURCE not in it['sources']:
            it['sources'].append(SOURCE)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


for order in range(8):
    patch(order)
print('book hints patched')
