# Trails in the Sky 1st Chapter (2025 remake) — rewritten in our own words from the Neoseeker
# walkthrough (facts only). The game locks each region once the story moves on, so chests,
# books and recipes expire when you leave their region; quests expire at the story beats the
# guide warns about. Chest contents and numbers come from fc_chests.py.
# Once published, never reorder or remove anything: ids are derived from order.
import re

from fc_chests import CHESTS
from lib import Chapter, t

G = 'fc'
NEO = lambda page: f'guide: Neoseeker FC walkthrough, {page}'
CH = {}

# Checkpoints that close a region live in the chapter where they happen; earlier chapters point
# to them by id (they are created further down, in this order).
VERTE = 'fc-ch1-cp-01'      # crossing Verte Bridge: no return to Rolent
KRONE = 'fc-ch2-cp-01'      # Krone Pass checkpoint: no return to Bose
KALDIA = 'fc-ch3-cp-01'     # border permit at Air-Letten: no return to Ruan
SANKTHEIM = 'fc-ch4-cp-01'  # border permit at Sanktheim Gate: no return to Zeiss


def region_cp(created, expected):
    """The region-closing checkpoints are referenced by id before they exist: keep them in sync."""
    if created != expected:
        raise SystemExit(f'checkpoint id drifted: {created} != {expected}')


def chapter(order, en, pt):
    CH[order] = Chapter(order, en, pt, game=G)
    return CH[order]


def qty(name):
    return re.sub(r' x ?(\d)', r' ×\1', name)


def chests(c, area, nums, until, hint, sources, title=None):
    """One entry per area; every chest is a route step, in the guide's order."""
    steps = []
    for n in nums:
        item, floor, battle = CHESTS[n]
        item = qty(item)
        en, pt = (f'{floor} — {item}', f'{floor} — {item}') if floor else (item, item)
        if battle:
            foes = ', '.join(qty(b.strip()) for b in battle.split(',') if b.strip())
            en += f' (monster chest: {foes})'
            pt += f' (baú de monstros: {foes})'
        steps.append(t(en, pt))
    n = len(nums)
    name = t(f'{title[0]} ({n})', f'{title[1]} ({n})') if title else t(f'{area[0]} treasure chests ({n})', f'Baús de {area[1]} ({n})')
    c.item('collectible', name, t(*area), until, t(*hint), 0, sources, steps=steps)


def quest(c, name, where, until, hint, sources, hidden=False):
    c.item('hidden_quest' if hidden else 'quest', t(name), t(*where), until, t(*hint), 0, sources)


def bonus(c, name, where, until, hint, sources):
    """Bonus BP from a story choice: level 1, since the choice can hint at the story."""
    c.item('missable', t(f'Bonus BP: {name[0]}', f'BP bônus: {name[1]}'), t(*where), until, t(*hint), 1, sources)


def book(c, name, where, until, hint, sources):
    c.item('collectible', t(name), t(*where), until, t(*hint), 0, sources)


def recipes(c, region, rows, until, hint, sources):
    steps = [t(f'{name} — {en}', f'{name} — {pt}') for name, en, pt in rows]
    n = len(rows)
    c.item('collectible', t(f'Recipes: {region[0]} ({n})', f'Receitas: {region[1]} ({n})'), t(*region), until, t(*hint), 0, sources, steps=steps)


def dish(c, name, en, pt, kind='standard'):
    c.recipe(name, t(en, pt), kind=kind, sources=[NEO('Recipe List')])


EAT = ('Eat each dish once to learn its recipe.', 'Coma cada prato uma vez para aprender a receita.')

# ======================================================================== Prologue
c = chapter(0, 'Prologue', 'Prólogo')
D1, D2, D3 = NEO('Prologue - Day 1'), NEO('Prologue - Day 2'), NEO('Prologue - Day 3')
P_ESMELAS = c.cp('Entering Esmelas Tower for the first time', 'Entrar na Esmelas Tower pela primeira vez')
P_PERZEL = c.cp('The night patrol at Perzel Farm', 'A patrulha noturna na Perzel Farm')
P_REPORTERS = c.cp("Starting the reporters' escort (talk to Verne at Hotel Rolent)", 'Começar a escolta dos repórteres (falar com o Verne no Hotel Rolent)')
P_ROBBERY = c.cp('Wrapping up the robbery investigation with Scherazard', 'Encerrar a investigação do roubo com a Scherazard')
P_END = c.cp('The event marker deep in Mistwald (end of the Prologue)', 'O marcador de evento no fundo de Mistwald (fim do Prólogo)')

quest(c, 'Shiny Stone Search', ('Rolent — Carl, behind the Orbal Factory', 'Rolent — Carl, atrás da Orbal Factory'), P_PERZEL,
      ('2 BP. Check the steam from the drain cover near Rinon\'s General Goods, then take the sewer entrance behind the chapel and find the shiny stone. Eat the Drill Meatballs you get for the recipe.',
       '2 BP. Veja o vapor saindo do bueiro perto da Rinon\'s General Goods, depois entre no esgoto pelos fundos da capela e ache a pedra brilhante. Coma as Drill Meatballs que você ganha para aprender a receita.'), [D2])
quest(c, 'Milch Monster', ('Milch Main Road — middle of the road', 'Milch Main Road — meio da estrada'), P_PERZEL,
      ('3 BP. Weak to fire. It explodes when it dies, so keep the party out of range for the last hit.',
       '3 BP. Fraco contra fogo. Ele explode ao morrer, então deixe a equipe fora do alcance no golpe final.'), [D2])
quest(c, 'Malga Mushroom', ('Rolent Landing Port — Orvid', 'Rolent Landing Port — Orvid'), P_REPORTERS,
      ('3 BP. The glowing Firefly Mushroom is near the Silver Earrings chest at the northeast end of Malga Trail; picking it starts a fight.',
       '3 BP. O Firefly Mushroom brilhante fica perto do baú das Silver Earrings, no extremo nordeste da Malga Trail; pegá-lo começa uma luta.'), [D3])
quest(c, 'Streetlight Switch', ("Rolent — Freddy at the Orbment Shop", 'Rolent — Freddy na loja de orbments'), P_REPORTERS,
      ('3 (+1) BP. The broken light is in the middle of Milch Main Road. For the bonus, let Joshua fight and have Estelle enter the code: the 3rd option (544818). Rewards Impede 2.',
       '3 (+1) BP. A luz quebrada fica no meio da Milch Main Road. Para o bônus, deixe o Joshua lutar e faça a Estelle digitar o código: a 3ª opção (544818). Dá Impede 2.'), [D3])
quest(c, 'Medicinal Material', ('Rolent Chapel — Father Divine', 'Capela de Rolent — Father Divine'), P_REPORTERS,
      ('3 BP. Bring a Bear Claw (southeast end of Mistwald) and Monster Powder (Killer Hornets in Mistwald). Mistwald only has four Bear Claws: don\'t cook them all.',
       '3 BP. Leve uma Bear Claw (extremo sudeste de Mistwald) e Monster Powder (Killer Hornets em Mistwald). Mistwald só tem quatro Bear Claws: não cozinhe todas.'), [D2, D3])
quest(c, 'Troop Training', ('Verte Bridge — Chief Warrant Officer Ashton', 'Verte Bridge — Chief Warrant Officer Ashton'), P_REPORTERS,
      ('2 (+2) BP. Win the training fight against two soldiers for the bonus; save first. Their attacks lower Defense: Estelle\'s Morale helps.',
       '2 (+2) BP. Vença a luta de treino contra dois soldados para o bônus; salve antes. Os ataques deles reduzem a defesa: o Morale da Estelle ajuda.'), [D3])
quest(c, 'Catch that Cat!', ('Rolent — Ida at the café', 'Rolent — Ida no café'), P_REPORTERS,
      ('2 BP. Short deadline: do it right away. The cat isn\'t marked: look between the clock tower, near Elger Arms & Guards, by Hotel Rolent, then upstairs in the chapel.',
       '2 BP. Prazo curto: faça na hora. O gato não aparece no mapa: procure entre a torre do relógio, perto da Elger Arms & Guards, junto ao Hotel Rolent e, por fim, no andar de cima da capela.'), [D3])
quest(c, 'Elize Hwy Monster', ('Elize Highway — the bridge', 'Elize Highway — a ponte'), P_END,
      ('4 BP. It blocks the bridge to your next destination, so you can\'t skip it. Wear Sleep protection; weak to fire.',
       '4 BP. Ele bloqueia a ponte para o próximo destino, então não dá para pular. Use proteção contra Sleep; fraco contra fogo.'), [D3])
bonus(c, ('storming into Esmelas Tower', 'entrar na Esmelas Tower'), ('Esmelas Tower — entrance', 'Esmelas Tower — entrada'), P_ESMELAS,
      ('+1 BP (Child Rescue). The choice comes right as you enter: pick the 2nd option, storming in together with Joshua.',
       '+1 BP (Child Rescue). A escolha aparece logo ao entrar: escolha a 2ª opção, entrar junto com o Joshua.'), [D1])
bonus(c, ('sneaking up on the crop thief', 'chegar de surpresa no ladrão de plantações'), ('Perzel Farm', 'Perzel Farm'), P_PERZEL,
      ('+2 BP (Perzel Pest Control). After the stables and the greenhouse, sneak up behind the monster without entering its line of sight, and examine it. Save first.',
       '+2 BP (Perzel Pest Control). Depois do estábulo e da estufa, chegue por trás do monstro sem entrar no campo de visão dele e examine-o. Salve antes.'), [D2])
bonus(c, ('the four robbery questions', 'as quatro perguntas do roubo'), ("Rolent — Mayor's Residence", 'Rolent — residência do prefeito'), P_ROBBERY,
      ('+4 BP (Mayoral Robbery), one per right answer: 2nd, 2nd, 3rd, 4th.',
       '+4 BP (Mayoral Robbery), um por resposta certa: 2ª, 2ª, 3ª, 4ª.'), [D3])
bonus(c, ('the choice in Mistwald', 'a escolha em Mistwald'), ('Mistwald — southeast end', 'Mistwald — extremo sudeste'), P_END,
      ('+1 BP (Mayoral Robbery). Pick the 2nd option during the event. The boss right after is much harder than in the original: bring Earth Guard.',
       '+1 BP (Mayoral Robbery). Escolha a 2ª opção durante o evento. O chefe logo depois é bem mais difícil que no original: leve Earth Guard.'), [D3])
book(c, 'Carnelia Vol. 1', ('Rolent — northwest house, upstairs', 'Rolent — casa a noroeste, andar de cima'), VERTE,
     ('Talk to Rhett. The Carnelia volumes are traded together for Estelle and Joshua\'s best weapons late in the game. A missed volume can later be bought, at a high price.',
      'Fale com o Rhett. Os volumes de Carnelia são trocados juntos pelas melhores armas da Estelle e do Joshua no fim do jogo. Um volume perdido pode ser comprado depois, por um preço alto.'), [D1])
book(c, "Luke's Diary", ('Rolent — northwest house, ground floor', 'Rolent — casa a noroeste, térreo'), VERTE,
     ('Read the diary on the table in Luke\'s room.', 'Leia o diário sobre a mesa do quarto do Luke.'), [D1])
book(c, 'Liberl News Issue 1', ("Rolent — Rinon's General Goods", "Rolent — Rinon's General Goods"), None,
     ('Bought during a story scene: you can\'t miss it.', 'Comprado durante uma cena da história: não tem como perder.'), [D1])
recipes(c, ('Rolent region', 'região de Rolent'), [
    ('Maple Cookie', "story scene at Rinon's General Goods", "cena da história na Rinon's General Goods"),
    ('Wholesome Pasta', 'Abend Bar', 'Abend Bar'),
    ('Fried Potatoes', 'Abend Bar', 'Abend Bar'),
    ('Flowery Soda', 'Abend Bar', 'Abend Bar'),
    ("Carmine's Eye", 'Abend Bar', 'Abend Bar'),
    ('Drill Meatballs', 'Shiny Stone Search reward', 'recompensa da Shiny Stone Search'),
    ('Dreamy Shell Bake', 'chest on Esmelas Tower 3F', 'baú no 3F da Esmelas Tower'),
    ('Salad Sandwich', 'Emily at Gurune Gate', 'Emily no Gurune Gate'),
], VERTE, EAT, [D1, D2])
S_ROL = [D2]
chests(c, ('Rolent Sewers', 'Rolent Sewers'), [2, 3], VERTE,
       ('The first dungeon, during Retrieval Training.', 'A primeira dungeon, durante a Retrieval Training.'), [D1])
chests(c, ('Elize Highway', 'Elize Highway'), [1, 15, 16, 17, 18], VERTE,
       ('A hidden cave west of the Droplet of Life is a great early grinding spot.', 'Uma caverna escondida a oeste do Droplet of Life é um ótimo lugar para treinar cedo.'), [D1] + S_ROL)
chests(c, ('Esmelas Tower', 'Esmelas Tower'), [6, 7, 8, 9, 10, 11, 12, 13, 14], VERTE,
       ('Both monster chests hold Wind Trappers that are very hard before level 8 and explode when defeated. You come back here in the story, so they can wait.',
        'Os dois baús de monstros têm Wind Trappers muito difíceis antes do nível 8, que explodem ao serem derrotados. Você volta aqui na história, então eles podem esperar.'), S_ROL)
chests(c, ('Mistwald', 'Mistwald'), [19, 20, 21, 22], VERTE,
       ('Black Bangle and Beast Hide Jumpsuit are big early upgrades, with no monster chests.', 'Black Bangle e Beast Hide Jumpsuit são grandes melhorias no começo, sem baús de monstros.'), S_ROL)
chests(c, ('Malga Trail', 'Malga Trail'), [4, 5, 23, 24, 25, 26], VERTE,
       ('The side path that Joshua blocks on Day 1 opens on Day 2.', 'O caminho lateral que o Joshua bloqueia no Dia 1 abre no Dia 2.'), [D1] + S_ROL)
chests(c, ('Milch Main Road', 'Milch Main Road'), [27, 28, 29, 30, 31, 32], VERTE,
       ('One monster chest with Lily Movers. A Shining Pom can spawn near the first Rhinocider.', 'Um baú de monstros com Lily Movers. Um Shining Pom pode aparecer perto do primeiro Rhinocider.'), S_ROL)
c.boss(t('Pine Plant+'), t('Milch Main Road'),
       t('Weak to fire. It explodes on defeat (up to 800 damage on high difficulties): keep the party away for the final blow.',
         'Fraco contra fogo. Explode ao ser derrotado (até 800 de dano nas dificuldades altas): mantenha a equipe longe no golpe final.'),
       related='fc-ch0-q-02', sources=[D2])
c.boss(t('Great Crop Muncher'), t('Perzel Farm'),
       t('Teaches Overdrive: turn it on and chain Brave Attacks. Fire arts work well; it powers up by eating its apple.',
         'Ensina o Overdrive: ative e encadeie Brave Attacks. Arts de fogo funcionam bem; ele fica mais forte comendo a maçã.'), sources=[D2])
c.boss(t('Royal Army soldiers', 'Soldados do Royal Army'), t('Verte Bridge'),
       t('Their hits lower Defense; Estelle\'s Morale counters it, and Overdrive ends the fight fast.',
         'Os golpes deles reduzem a defesa; o Morale da Estelle compensa, e o Overdrive encerra a luta rápido.'), related='fc-ch0-q-06', sources=[D3])
c.boss(t('Emeronecider'), t('Elize Highway'),
       t('Tanky but weak to fire. Spread out (its hits splash) and wear Sleep protection.',
         'Resistente, mas fraco contra fogo. Espalhe a equipe (os golpes atingem em área) e use proteção contra Sleep.'), related='fc-ch0-q-08', sources=[D3])
c.boss(t('Josette and the bandits', 'Josette e os bandidos'), t('Mistwald'),
       t('Much harder than the original. Bring Earth Guard, take out the bandits first with Schera\'s wind arts, impede Josette\'s casts and dispel her Rage buff with Anti-Sept or Joshua\'s Sever.',
         'Bem mais difícil que no original. Leve Earth Guard, derrube os bandidos primeiro com as arts de vento da Schera, interrompa as conjurações da Josette e remova o buff de Rage com Anti-Sept ou o Sever do Joshua.'),
       sources=[D3])

# ======================================================================== Chapter 1
c = chapter(1, 'Chapter 1', 'Capítulo 1')
BOSE, HAKEN, VAL = NEO('Chapter 1 - Bose'), NEO('Chapter 1 - Haken Gate'), NEO('Chapter 1 - Valleria Shore')
region_cp(c.cp('Crossing Verte Bridge into the Bose region (no return to Rolent)', 'Atravessar a Verte Bridge para a região de Bose (sem volta para Rolent)'), VERTE)
EISEN = c.cp('Passing the soldiers on East Bose Highway into Eisen Road', 'Passar pelos soldados na East Bose Highway rumo à Eisen Road')
RAVENNUE = c.cp('Heading to Ravennue Village to follow the airliner lead', 'Ir para Ravennue Village atrás da pista do airliner')
MINE = c.cp('The clearing in the Abandoned Mine (boss fight)', 'A clareira da Abandoned Mine (luta contra chefe)')
VALLERIA = c.cp('Talking to Sophina at the Kingfisher Inn (stuck at Valleria Shore)', 'Falar com a Sophina na Kingfisher Inn (preso em Valleria Shore)')
END1 = c.cp('Leaving the Sky Pirate Stronghold (end of Chapter 1)', 'Sair do Sky Pirate Stronghold (fim do Capítulo 1)')
quest(c, 'Divine Delivery', ('Rolent Chapel, then Bose Chapel', 'Capela de Rolent e depois capela de Bose'), EISEN,
      ('2 BP. Short deadline. Pick up the letter from Father Divine BEFORE crossing Verte Bridge, then give it to Father Holstein in the Bose chapel.',
       '2 BP. Prazo curto. Pegue a carta com o Father Divine ANTES de atravessar a Verte Bridge e entregue ao Father Holstein na capela de Bose.'), [BOSE])
quest(c, "Elissa's Entreaty", ('Rolent — Elissa at Abend Bar', 'Rolent — Elissa no Abend Bar'), VERTE,
      ('2 (+2) BP. Not on the board, new in the remake. At Perzel Farm check every green marker; pick the 1st option at the strawberries and the 2nd at the cow for the bonus. Eat the Sunshine Mille Crepe for its recipe.',
       '2 (+2) BP. Não aparece no quadro, nova no remake. Na Perzel Farm, examine todos os marcadores verdes; escolha a 1ª opção nos morangos e a 2ª na vaca para o bônus. Coma o Sunshine Mille Crepe para aprender a receita.'), [BOSE], hidden=True)
quest(c, 'Mountain Monster', ('Ravennue Trail', 'Ravennue Trail'), EISEN,
      ('4 BP. Short deadline. Its Fate Saber can K.O. instantly: bring Deathblow protection (Grail Ring, Crest Charm). It is slow and easy to stun.',
       '4 BP. Prazo curto. O Fate Saber dele pode derrubar na hora: leve proteção contra Deathblow (Grail Ring, Crest Charm). Ele é lento e fácil de atordoar.'), [BOSE])
quest(c, 'Culinary Collection', ('Bose — Gwen at Restaurant Anterose', 'Bose — Gwen no Restaurant Anterose'), EISEN,
      ('3 BP. Bring 5 Monster Tenders, dropped by Limera and Hresvelgr (start of Eisen Road, or the hidden cave on West Bose Highway). Rewards the Royal Omelette recipe.',
       '3 BP. Leve 5 Monster Tenders, que caem de Limera e Hresvelgr (início da Eisen Road ou a caverna escondida da West Bose Highway). Dá a receita do Royal Omelette.'), [BOSE])
quest(c, 'Amber Alarm', ('Amberl Tower', 'Amberl Tower'), RAVENNUE,
      ('4 BP. Not on the board: it starts when you enter Amberl Tower. Reach 5F, approach the center, then leave the tower.',
       '4 BP. Não aparece no quadro: começa quando você entra na Amberl Tower. Suba até o 5F, aproxime-se do centro e depois saia da torre.'), [HAKEN], hidden=True)
quest(c, 'Claw Cure', ('Bose Market — Spence', 'Bose Market — Spence'), RAVENNUE,
      ('4 BP. Appears after Divine Delivery. Bring two Bear Claws from Nebel Valley: near the end of the west path (after its quest monster) and beside the Thelas Balm chest.',
       '4 BP. Aparece depois da Divine Delivery. Leve duas Bear Claws de Nebel Valley: perto do fim do caminho oeste (depois do monstro da quest) e ao lado do baú do Thelas Balm.'), [HAKEN])
quest(c, 'Escort Escapade', ('Bose — Hart at Frieden Hotel', 'Bose — Hart no Frieden Hotel'), RAVENNUE,
      ('4 (+1) BP. Walk Hart to Krone Trail; if he falls it\'s game over, so avoid fights. Choose "A frontal assault!" (1st option) for the bonus.',
       '4 (+1) BP. Leve o Hart até a Krone Trail; se ele cair é game over, então evite lutas. Escolha "A frontal assault!" (1ª opção) para o bônus.'), [HAKEN])
quest(c, 'E Bose Hwy Monster', ('East Bose Highway', 'East Bose Highway'), RAVENNUE,
      ('4 BP. Poisonous scorpions; the leader calls more.', '4 BP. Escorpiões venenosos; o líder chama mais.'), [HAKEN])
quest(c, 'Nebel Valley Monster', ('Nebel Valley', 'Nebel Valley'), RAVENNUE,
      ('5 BP. Kill the Boiled Eggers from a distance (they explode) and wear Flame Zippos against Freeze.',
       '5 BP. Derrube os Boiled Eggers à distância (eles explodem) e use Flame Zippos contra Freeze.'), [HAKEN])
quest(c, 'W Bose Hwy Monster', ('West Bose Highway', 'West Bose Highway'), RAVENNUE,
      ('4 BP. The toughest of this set: spread out, keep Earth Guard up and protect against Mute, Seal and Blind.',
       '4 BP. O mais difícil deste grupo: espalhe a equipe, mantenha o Earth Guard e se proteja de Mute, Seal e Blind.'), [HAKEN])
quest(c, 'Battle Backup', ('Nebel Valley', 'Nebel Valley'), VALLERIA,
      ('4 BP. New in the remake. Help Anelace in Nebel Valley; Flame Zippos recommended. Later, Sting at the Bose guild gives Proxy Puppet S ×2.',
       '4 BP. Nova no remake. Ajude a Anelace em Nebel Valley; Flame Zippos recomendados. Depois, o Sting na guilda de Bose dá Proxy Puppet S ×2.'), [VAL])
quest(c, 'Ansel Path Monster', ('New Ansel Path', 'New Ansel Path'), VALLERIA,
      ('5 BP. It blocks the way to Valleria Shore, so you can\'t skip it. The turtles shrug off physical hits: use arts and step out of the red circles.',
       '5 BP. Ele bloqueia o caminho para Valleria Shore, então não dá para pular. As tartarugas aguentam golpes físicos: use arts e saia dos círculos vermelhos.'), [VAL])
bonus(c, ('the answer on the airliner deck', 'a resposta no convés do airliner'), ('Abandoned Mine — the airliner', 'Abandoned Mine — o airliner'), VALLERIA,
      ('+3 BP (Missing Airliner). Outside on the airliner, pick the 5th option: their hideout is somewhere special.',
       '+3 BP (Missing Airliner). No lado de fora do airliner, escolha a 5ª opção: o esconderijo deles fica num lugar especial.'), [HAKEN])
c.item('missable', t('Examine the vacuum cleaner', 'Examinar o aspirador de pó'), t('Sky Pirate Stronghold — second floor, northwest', 'Sky Pirate Stronghold — segundo andar, noroeste'), END1,
       t('Examining it gives the Black Notebook, needed for the hidden quest Black Notebook in Chapter 2.',
         'Examiná-lo dá o Black Notebook, necessário para a quest escondida Black Notebook no Capítulo 2.'), 0, [VAL])
book(c, 'Carnelia Vol. 2', ('Verte Bridge — Private Harold', 'Verte Bridge — Private Harold'), VERTE,
     ('He stands by the gate: talk to him before going through.', 'Ele fica junto ao portão: fale com ele antes de passar.'), [BOSE])
book(c, 'Liberl News Issue 2', ("Rolent — Rinon's General Goods", "Rolent — Rinon's General Goods"), VERTE,
     ('Buy it before leaving Rolent.', 'Compre antes de sair de Rolent.'), [BOSE])
book(c, 'Carnelia Vol. 3', ('Haken Gate — Marco in the rest area', 'Haken Gate — Marco na área de descanso'), RAVENNUE,
     ('Talk to him before entering the main building and examining the far door.', 'Fale com ele antes de entrar no prédio principal e examinar a porta do fundo.'), [HAKEN])
book(c, 'Carnelia Vol. 4', ('Bose Market — Libro', 'Bose Market — Libro'), VALLERIA,
     ('Talk to him before heading to Valleria Shore. Grocery Minuet sells missed volumes, at a high price.',
      'Fale com ele antes de ir para Valleria Shore. A Grocery Minuet vende volumes perdidos, por um preço alto.'), [VAL])
book(c, 'Liberl News Issue 3', ('Bose Market — Grocery Minuet', 'Bose Market — Grocery Minuet'), KRONE,
     ('Buy it before leaving the Bose region.', 'Compre antes de sair da região de Bose.'), [VAL])
book(c, 'Hundred Days War - A True Account', ('Valleria Shore', 'Valleria Shore'), None,
     ('Received in a story scene: you can\'t miss it.', 'Recebido numa cena da história: não tem como perder.'), [VAL])
recipes(c, ('Bose region', 'região de Bose'), [
    ('Sunshine Mille Crepe', "Elissa's Entreaty reward (Rolent)", "recompensa da Elissa's Entreaty (Rolent)"),
    ('Fullmouth Soup', 'Kirsche Bar', 'Kirsche Bar'),
    ('Red Tail Soup', 'Kirsche Bar', 'Kirsche Bar'),
    ('Astonishing Cheese Risotto', 'Kirsche Bar', 'Kirsche Bar'),
    ('Sweet Castella', "Caterina's Shop, Bose Market", "Caterina's Shop, Bose Market"),
    ('Flowery Jelly', "Caterina's Shop, Bose Market", "Caterina's Shop, Bose Market"),
    ('Beast Steak', 'chest on Ravennue Trail', 'baú na Ravennue Trail'),
    ('Royal Omelette', 'Culinary Collection reward', 'recompensa da Culinary Collection'),
    ('Cursed Fried Eyeballs', 'chest on Krone Trail', 'baú na Krone Trail'),
    ('Heaven-and-Hell Stew', 'have some stew at Whemler Hut (2nd option)', 'aceite o ensopado na Whemler Hut (2ª opção)'),
    ('Kasagin Tempura', 'The Kingfisher Inn', 'The Kingfisher Inn'),
    ('Miso-Simmered Carp', 'The Kingfisher Inn', 'The Kingfisher Inn'),
    ('Grilled Rockfish Skewer', 'The Kingfisher Inn', 'The Kingfisher Inn'),
    ('Salmon Meunière', 'The Kingfisher Inn', 'The Kingfisher Inn'),
    ('Grilled Rainbow Trout', 'The Kingfisher Inn', 'The Kingfisher Inn'),
    ('Apple Ice Cream', 'The Moonlight Path, Ravennue Village', 'The Moonlight Path, Ravennue Village'),
    ('Fresh-Squeezed Juice', 'The Moonlight Path, Ravennue Village', 'The Moonlight Path, Ravennue Village'),
], KRONE, EAT, [BOSE, HAKEN])
S_BOSE = [BOSE]
chests(c, ('East Bose Highway', 'East Bose Highway'), [33, 34, 35], KRONE,
       ('Two of the three can be opened before the story event midway along the road.', 'Dois dos três podem ser abertos antes do evento da história no meio da estrada.'), S_BOSE)
chests(c, ('West Bose Highway', 'West Bose Highway'), [36, 37, 38, 39, 40], KRONE,
       ('The monster chest holds Katars, an upgrade for Joshua. A hidden cave in the southwest is a farming spot.', 'O baú de monstros tem Katars, uma melhoria para o Joshua. Uma caverna escondida no sudoeste serve para farmar.'), S_BOSE)
chests(c, ('Ravennue Trail', 'Ravennue Trail'), [41, 42, 43, 44, 45, 46, 47], KRONE,
       ('Four chests before the quest marker (approaching it starts the boss fight), three after it.', 'Quatro baús antes do marcador da quest (chegar perto começa a luta), três depois.'), S_BOSE)
chests(c, ('Krone Trail (Bose side)', 'Krone Trail (lado de Bose)'), [48, 49, 50], KRONE,
       ('Includes the Cursed Fried Eyeballs dish. Reach the western checkpoint to unlock fast travel.', 'Inclui o prato Cursed Fried Eyeballs. Chegue ao posto a oeste para liberar a viagem rápida.'), S_BOSE)
chests(c, ('Nebel Valley', 'Nebel Valley'), [51, 52, 53], KRONE,
       ('Many enemies freeze: wear Flame Zippos. Picking up a Bear Claw early skips a fun line in a later quest.', 'Muitos inimigos congelam: use Flame Zippos. Pegar uma Bear Claw cedo pula uma fala divertida de uma quest futura.'), S_BOSE)
chests(c, ('New Ansel Path', 'New Ansel Path'), [54, 55], KRONE,
       ('Evasive enemies: Hit quartz on the field leader helps.', 'Inimigos evasivos: quartzo Hit no líder de campo ajuda.'), S_BOSE)
chests(c, ('Amberl Tower', 'Amberl Tower'), [56, 57, 58, 59, 60, 61, 62, 63], KRONE,
       ('Both monster chests hold Ground Trappers that explode on defeat; they are very weak to wind (Aero Storm).', 'Os dois baús de monstros têm Ground Trappers que explodem ao serem derrotados; eles são muito fracos contra vento (Aero Storm).'), S_BOSE)
chests(c, ('Eisen Road', 'Eisen Road'), [64, 65], KRONE,
       ('Limera reflect arts and call Hresvelgr; both drop the Monster Tenders for Culinary Collection.', 'Limeras refletem arts e chamam Hresvelgr; os dois deixam cair os Monster Tenders da Culinary Collection.'), [HAKEN])
chests(c, ('Abandoned Mine', 'Abandoned Mine'), [66, 67], MINE,
       ('One-time visit. Take the right path for both chests before heading toward the story event.', 'Visita única. Pegue o caminho da direita para os dois baús antes de ir ao evento da história.'), [HAKEN])
chests(c, ('Sky Pirate Stronghold', 'Sky Pirate Stronghold'), list(range(68, 78)), END1,
       ('One-time dungeon. The last chest holds the Jeweled Ring for the Ring Robbery quest, and the vacuum cleaner on the second floor starts a hidden quest.',
        'Dungeon de visita única. O último baú tem o Jeweled Ring da quest Ring Robbery, e o aspirador de pó do segundo andar começa uma quest escondida.'), [VAL])
c.boss(t('Fate Spinner'), t('Ravennue Trail'),
       t('Its Fate Saber can K.O. instantly: wear Deathblow protection or keep revives ready. It is slow, so delay and Overdrive can lock it down.',
         'O Fate Saber pode derrubar na hora: use proteção contra Deathblow ou deixe itens de reviver prontos. Ele é lento, então atraso e Overdrive podem travá-lo.'),
       related='fc-ch1-q-02', sources=S_BOSE)
c.boss(t('King Scorpion+'), t('East Bose Highway'),
       t('Easy: poisonous scorpions and more of them over time.', 'Fácil: escorpiões venenosos, e mais deles com o tempo.'), related='fc-ch1-q-06', sources=[HAKEN])
c.boss(t('Master Cryon'), t('Nebel Valley'),
       t('Kill the Boiled Eggers from range (they explode), wear Flame Zippos against Diamond Dust\'s Freeze, and dispel its Rage near the end.',
         'Derrube os Boiled Eggers à distância (eles explodem), use Flame Zippos contra o Freeze do Diamond Dust e remova o Rage dele perto do fim.'),
       related='fc-ch1-q-07', sources=[HAKEN])
c.boss(t('Thunder Quake'), t('West Bose Highway'),
       t('Fast and tanky. Spread out against its area attacks, keep Earth Guard up, protect against Mute, Seal and Blind, and Sever its Rage.',
         'Rápido e resistente. Espalhe a equipe contra os ataques em área, mantenha o Earth Guard, se proteja de Mute, Seal e Blind e use o Sever no Rage.'),
       related='fc-ch1-q-08', sources=[HAKEN])
c.boss(t('Kyle and the sky pirates', 'Kyle e os piratas do céu'), t('Abandoned Mine'),
       t('Grenades hit in small areas: spread out and cast Earth Guard. Clear the three pirates first; Kyle is tanky and can Burn or Blind.',
         'As granadas acertam pequenas áreas: espalhe a equipe e use Earth Guard. Derrube os três piratas primeiro; o Kyle é resistente e pode causar Burn ou Blind.'),
       sources=[HAKEN])
c.boss(t('Big the Yeti'), t('Nebel Valley'),
       t('Wear Flame Zippos against its Ice Breath and dispel its Rage with Sever or Anti-Sept. Sylphen Wing helps.',
         'Use Flame Zippos contra o Ice Breath e remova o Rage com Sever ou Anti-Sept. Sylphen Wing ajuda.'), related='fc-ch1-q-09', sources=[VAL])
c.boss(t('Diamond Turtle'), t('New Ansel Path'),
       t('Very high physical defense: use arts and magic crafts, and step out of the red circles. At low HP it reflects one art.',
         'Defesa física altíssima: use arts e crafts mágicos e saia dos círculos vermelhos. Com pouco HP, reflete uma art.'), related='fc-ch1-q-10', sources=[VAL])
c.boss(t('The Capua family', 'A família Capua'), t('Sky Pirate Stronghold'),
       t('Harder than the Prologue boss and you can\'t go back to town: bring La Tear, Earth Guard and Clock Up EX. Focus one sibling at a time near 33% HP so they don\'t Rage together, and leave the tanky Don for last.',
         'Mais difícil que o chefe do Prólogo e não dá para voltar à cidade: leve La Tear, Earth Guard e Clock Up EX. Foque um irmão por vez perto de 33% do HP para que não entrem em Rage juntos, e deixe o Don, mais resistente, por último.'),
       sources=[VAL])

# ======================================================================== Chapter 2
c = chapter(2, 'Chapter 2', 'Capítulo 2')
MAN, RUAN, ACAD = NEO('Chapter 2 - Manoria Village'), NEO('Chapter 2 - Ruan'), NEO('Chapter 2 - Jenis Royal Academy')
region_cp(c.cp('Reaching the Krone Pass checkpoint (no return to Bose)', 'Chegar ao posto da Krone Pass (sem volta para Bose)'), KRONE)
REACH_RUAN = c.cp('Arriving in Ruan with Kloe', 'Chegar a Ruan com a Kloe')
ORPHANAGE = c.cp('Investigating the burnt Mercia Orphanage', 'Investigar o Mercia Orphanage incendiado')
WAREHOUSE = c.cp('The fight in the South Block warehouse', 'A luta no depósito do South Block')
ACADEMY = c.cp("Going to the headmaster's office at Jenis Royal Academy", 'Ir à sala do diretor na Jenis Royal Academy')
EVE = c.cp("Returning to the headmaster's office on the eve of the festival", 'Voltar à sala do diretor na véspera do festival')
ALBA = c.cp('Guiding Professor Alba at the school festival', 'Guiar o Professor Alba no festival da escola')
MANORIA = c.cp('The event at The White Magnolia in Manoria (Agate joins)', 'O evento na The White Magnolia em Manoria (o Agate entra)')
END2 = c.cp('The last event of Chapter 2', 'O último evento do Capítulo 2')
quest(c, 'Ring Robbery', ('Bose — Lana, southeast corner', 'Bose — Lana, canto sudeste'), KRONE,
      ('3 BP. Needs the Jeweled Ring from the last chest of the Sky Pirate Stronghold; return it to Lana.',
       '3 BP. Precisa do Jeweled Ring do último baú do Sky Pirate Stronghold; devolva à Lana.'), [MAN])
quest(c, 'Black Notebook', ('Haken Gate — underground cells', 'Haken Gate — celas subterrâneas'), KRONE,
      ('5 BP. Only if you examined the vacuum cleaner in the Sky Pirate Stronghold: bring the notebook to the guards.',
       '5 BP. Só se você examinou o aspirador de pó no Sky Pirate Stronghold: leve o caderno aos guardas.'), [MAN], hidden=True)
quest(c, 'Lighthouse Labor', ('Varenne Lighthouse — Vogt', 'Varenne Lighthouse — Vogt'), ORPHANAGE,
      ('4 BP. Not on the board: talk to Vogt outside the lighthouse and clear the four Red Shumocks inside.',
       '4 BP. Não aparece no quadro: fale com o Vogt do lado de fora do farol e derrote os quatro Red Shumocks lá dentro.'), [MAN], hidden=True)
quest(c, 'Seaside Way Monster', ('Gull Seaside Way', 'Gull Seaside Way'), REACH_RUAN,
      ('4 BP. It blocks the road to Ruan, so you can\'t skip it. Disable the weaker mobs with Chaos Brand first.',
       '4 BP. Ele bloqueia a estrada para Ruan, então não dá para pular. Desative os inimigos menores com Chaos Brand primeiro.'), [MAN])
quest(c, 'Key Keeping', ('Ruan — Harg at the port', 'Ruan — Harg no porto'), ORPHANAGE,
      ('2 BP. The key is in the water by the plank bridge east of Aqua Rossa Bar. Check the rods upstairs in the bar, borrow the Progressive Rod from Squaro and fish it out.',
       '2 BP. A chave está na água junto à ponte de tábuas a leste do Aqua Rossa Bar. Veja as varas no andar de cima do bar, pegue a Progressive Rod emprestada com o Squaro e pesque a chave.'), [RUAN])
quest(c, 'Aina Cswy Monster', ('Aina Causeway — outside Sapphirl Tower', 'Aina Causeway — em frente à Sapphirl Tower'), ORPHANAGE,
      ('4 BP. The crabs reflect physical hits until stunned: use arts and wear Mute protection. Drops Prototype Zero for Prototype Pursuit.',
       '4 BP. Os caranguejos refletem golpes físicos até serem atordoados: use arts e proteção contra Mute. Deixa cair o Prototype Zero da Prototype Pursuit.'), [RUAN])
quest(c, 'Prototype Pursuit', ('Ruan — Karl at Joan Arms & Guards', 'Ruan — Karl na Joan Arms & Guards'), ORPHANAGE,
      ('3 BP. Hand over Prototype Zero (from the Aina Cswy Monster). Rewards Seal Blade.',
       '3 BP. Entregue o Prototype Zero (do Aina Cswy Monster). Dá a Seal Blade.'), [RUAN])
quest(c, 'Maintenance Mail', ("Ruan — Tobias at Granate's Orbal Factory", "Ruan — Tobias na Granate's Orbal Factory"), ACADEMY,
      ('4 BP. Short deadline. Take the bag to Vogt at the top of Varenne Lighthouse. Bring Azelia Rosè (Primo, casino) and Salty Anchovies (Fiore\'s, Manoria) too for a Work Helmet and a Victory Headband.',
       '4 BP. Prazo curto. Leve a bolsa ao Vogt no alto do Varenne Lighthouse. Leve também Azelia Rosè (Primo, cassino) e Salty Anchovies (Fiore\'s, Manoria) para ganhar um Work Helmet e um Victory Headband.'), [ACAD])
quest(c, 'Map Mystery', ('Ruan Chapel — Jimmy', 'Capela de Ruan — Jimmy'), ACADEMY,
      ('3 (+2) BP. Short deadline. The treasure is in a barrel on the small beach by Gull Seaside Way\'s east wall (Skull Dagger + map fragment). The bonus needs Jimmy saved earlier on Gull Seaside Way.',
       '3 (+2) BP. Prazo curto. O tesouro está num barril na prainha junto à parede leste da Gull Seaside Way (Skull Dagger + fragmento de mapa). O bônus exige ter salvado o Jimmy antes na Gull Seaside Way.'), [ACAD, MAN])
quest(c, 'Exploration Escort', ('Manoria Village — Amelia at the north entrance', 'Manoria Village — Amelia na entrada norte'), ACADEMY,
      ('5 BP. Short deadline. Go to the north end of Krone Trail, win the fight, then escort Orvid back to Manoria.',
       '5 BP. Prazo curto. Vá ao extremo norte da Krone Trail, vença a luta e escolte o Orvid de volta a Manoria.'), [ACAD])
quest(c, 'Delicate Diplomacy', ('Air-Letten', 'Air-Letten'), ACADEMY,
      ('3 (+2) BP. Short deadline. Agree on the balcony, then in the cafeteria answer 2nd, either, 1st, 2nd for the bonus.',
       '3 (+2) BP. Prazo curto. Aceite na varanda e, na cafeteria, responda 2ª, qualquer uma, 1ª, 2ª para o bônus.'), [ACAD])
quest(c, 'Candelabrum Clues', ("Ruan — Gilbert at the Mayor's Residence", 'Ruan — Gilbert na residência do prefeito'), ACADEMY,
      ('7 BP. Short deadline. Check the plaque at Ruan Lighthouse, the roulette table upstairs in the casino, the forklift at the port and the crane near the bar, then talk to Harg.',
       '7 BP. Prazo curto. Examine a placa do farol de Ruan, a roleta no andar de cima do cassino, a empilhadeira do porto e o guindaste perto do bar, depois fale com o Harg.'), [ACAD])
quest(c, 'Seaside Way Monster 2', ('Gull Seaside Way', 'Gull Seaside Way'), MANORIA,
      ('5 BP. It blocks the way to Manoria, so you can\'t skip it. Use arts against Seal and Blind; Knight Ammonites explode when defeated.',
       '5 BP. Ele bloqueia o caminho para Manoria, então não dá para pular. Use arts contra Seal e Blind; os Knight Ammonites explodem ao serem derrotados.'), [ACAD])
c.item('missable', t('Save Jimmy on Gull Seaside Way', 'Salvar o Jimmy na Gull Seaside Way'), t('Gull Seaside Way — alcove on the beach', 'Gull Seaside Way — reentrância na praia'), REACH_RUAN,
       t('A side event on the way to Ruan (three Sharkagators). Saving him unlocks +2 BP in the Map Mystery quest later.',
         'Um evento opcional a caminho de Ruan (três Sharkagators). Salvá-lo libera +2 BP na quest Map Mystery depois.'), 0, [MAN])
bonus(c, ('the questions at the orphanage', 'as perguntas no orfanato'), ('Mercia Orphanage; Manoria Village', 'Mercia Orphanage; Manoria Village'), WAREHOUSE,
      ('+4 BP (Orphanage Investigation). After examining every clue, pick the 2nd option (someone started the fire?); later at The White Magnolia, pick the 3rd (the thugs?!).',
       '+4 BP (Orphanage Investigation). Depois de examinar todas as pistas, escolha a 2ª opção (alguém começou o fogo?); depois, na The White Magnolia, escolha a 3ª (os bandidos?!).'), [RUAN])
bonus(c, ('the festival preparations', 'os preparativos do festival'), ('Jenis Royal Academy', 'Jenis Royal Academy'), EVE,
      ('+5 BP (A Festival Favor), via the blue markers: Logan\'s three books (+1), Janitor Parkes\'s three decoration spots (+1) and clearing the old schoolhouse (+3). Pick up its three U-Materials first.',
       '+5 BP (A Festival Favor), pelos marcadores azuis: os três livros do Logan (+1), os três lugares de decoração do zelador Parkes (+1) e limpar a escola antiga (+3). Pegue antes os três U-Materials de lá.'), [ACAD])
book(c, 'Liberl News Issue 4', ('Bose Market — Grocery Minuet', 'Bose Market — Grocery Minuet'), KRONE,
     ('Buy it before leaving Bose for good.', 'Compre antes de sair de Bose de vez.'), [MAN])
book(c, 'Ruan Economic History 1', ("Jenis Royal Academy — boys' locker room (clubhouse)", 'Jenis Royal Academy — vestiário masculino (clube)'), EVE,
     ('One of Logan\'s three books for the festival preparations.', 'Um dos três livros do Logan nos preparativos do festival.'), [ACAD])
book(c, 'Ruan Economic History 2', ('Jenis Royal Academy — faculty lounge, main building', 'Jenis Royal Academy — sala dos professores, prédio principal'), EVE,
     ('The book by Ms. Millia.', 'O livro perto da Ms. Millia.'), [ACAD])
book(c, 'Ruan Economic History 3', ("Jenis Royal Academy — boys' dorm, 1F southwest room", 'Jenis Royal Academy — dormitório masculino, sala sudoeste do 1F'), EVE,
     ('On the desk.', 'Sobre a escrivaninha.'), [ACAD])
book(c, 'Carnelia Vol. 5', ('Ruan — Matilda by the hotel bridge', 'Ruan — Matilda junto à ponte do hotel'), KALDIA,
     ('Available after the festival. If missed, O\'Neil Duty-Free Shop sells it later.', 'Disponível depois do festival. Se perder, a O\'Neil Duty-Free Shop vende depois.'), [ACAD])
book(c, 'Liberl News Issue 5', ("Ruan — O'Neil Duty-Free Shop", "Ruan — O'Neil Duty-Free Shop"), KALDIA,
     ('Buy it before leaving the Ruan region.', 'Compre antes de sair da região de Ruan.'), [RUAN])
recipes(c, ('Ruan region', 'região de Ruan'), [
    ('Morning-Picked Herbal Tea', 'The White Magnolia, Manoria', 'The White Magnolia, Manoria'),
    ('Stubborn Paella', 'The White Magnolia, Manoria', 'The White Magnolia, Manoria'),
    ('Azelia Rosè', 'Lavantar Casino & Bar', 'Lavantar Casino & Bar'),
    ('Steamed Roe in Sake', 'Aqua Rossa Bar', 'Aqua Rossa Bar'),
    ('Healthy Rice Porridge', 'Aqua Rossa Bar', 'Aqua Rossa Bar'),
    ('Blazing Fried Chicken', 'chest on Sapphirl Tower 5F', 'baú no 5F da Sapphirl Tower'),
    ('Salt-Crusted Small Fish', 'Air-Letten cafeteria', 'cafeteria de Air-Letten'),
    ('Jenis Lunch', 'Jenis Royal Academy cafeteria', 'cafeteria da Jenis Royal Academy'),
], KALDIA, EAT, [MAN, RUAN, ACAD])
recipes(c, ('school festival stalls', 'barracas do festival'), [
    ('Coffee Ice Cream', 'Frozen Sweets Fleuret', 'Frozen Sweets Fleuret'),
    ('Orange Ice Cream', 'Frozen Sweets Fleuret', 'Frozen Sweets Fleuret'),
    ('Crunchy Popcorn', 'Pop Step', 'Pop Step'),
    ('Rainbow Jelly Beans', 'Fortissimo Candies', 'Fortissimo Candies'),
    ('Royal Crepe', 'Crepe Shop Nagomi', 'Crepe Shop Nagomi'),
], ALBA, ('The stalls only exist on festival day: buy and eat each dish before moving the story on.',
          'As barracas só existem no dia do festival: compre e coma cada prato antes de avançar a história.'), [ACAD])
S_RUAN = [MAN]
chests(c, ('Krone Trail (Ruan side)', 'Krone Trail (lado de Ruan)'), [78, 79, 80], KALDIA,
       ('Same monsters as the Bose side, at a higher level.', 'Os mesmos monstros do lado de Bose, em nível mais alto.'), S_RUAN)
chests(c, ('Manoria Byroad', 'Manoria Byroad'), [81, 82, 83, 84, 85], KALDIA,
       ('The monster chest with Military Boots swarms you with Stove Plants: Joshua\'s Black Fang (level 21) clears them.', 'O baú de monstros com as Military Boots cerca você de Stove Plants: o Black Fang do Joshua (nível 21) resolve.'), S_RUAN)
chests(c, ('Gull Seaside Way', 'Gull Seaside Way'), list(range(86, 95)), KALDIA,
       ('Shining Poms appear on the beaches. The Skull Dagger barrel by the east wall belongs to the Map Mystery quest.', 'Shining Poms aparecem nas praias. O barril da Skull Dagger junto à parede leste é da quest Map Mystery.'), S_RUAN)
chests(c, ('Vista Forest Road', 'Vista Forest Road'), [95, 96, 97, 98], KALDIA,
       ('Evasive enemies; one monster chest.', 'Inimigos evasivos; um baú de monstros.'), S_RUAN)
chests(c, ('Aina Causeway', 'Aina Causeway'), [99, 100, 101], KALDIA,
       ('The hidden cave of the region is to the south, near Air-Letten.', 'A caverna escondida da região fica ao sul, perto de Air-Letten.'), [RUAN])
chests(c, ('Sapphirl Tower', 'Sapphirl Tower'), list(range(102, 109)), KALDIA,
       ('The north path from 2F has both monster chests (Aqua Trappers, weak to earth); the south path leads to the rest and the roof. Includes Kloe\'s Flamberge.',
        'O caminho norte a partir do 2F tem os dois baús de monstros (Aqua Trappers, fracos contra terra); o caminho sul leva aos outros e ao terraço. Inclui a Flamberge da Kloe.'), [RUAN])
c.boss(t('Jabba'), t('Gull Seaside Way'),
       t('Two halves: disable the weaker mobs with Chaos Brand and clear them, then focus the Jabba.',
         'Duas metades: desative os inimigos menores com Chaos Brand e derrube-os, depois foque o Jabba.'), related='fc-ch2-q-02', sources=[MAN])
c.boss(t('Helm Cancer+'), t('Aina Causeway'),
       t('They reflect physical hits until stunned: use arts, Chaos Brand the small ones and step out of Blue Impact. Wear Mute protection.',
         'Eles refletem golpes físicos até serem atordoados: use arts, aplique Chaos Brand nos pequenos e saia do Blue Impact. Use proteção contra Mute.'),
       related='fc-ch2-q-04', sources=[RUAN])
c.boss(t('The Ravens', 'Os Ravens'), t('Ruan — South Block warehouse', 'Ruan — depósito do South Block'),
       t('Six foes; the three named ones support and revive the grunts. Joshua\'s Protect works well here. At low HP they Rage and gain an instant-K.O. attack: Resurgence and Kloe\'s healing S-Craft are your safety net.',
         'Seis inimigos; os três com nome dão suporte e revivem os capangas. O Protect do Joshua funciona bem aqui. Com pouco HP eles entram em Rage e ganham um ataque de KO instantâneo: Resurgence e o S-Craft de cura da Kloe são sua rede de segurança.'),
       sources=[RUAN])
c.boss(t('Jabba King'), t('Gull Seaside Way'),
       t('Its escorts scale to your level. Kloe\'s water arts hit hard; arts beat its Seal and Blind, and Knight Ammonites explode when defeated.',
         'Os acompanhantes acompanham o seu nível. As arts de água da Kloe batem forte; arts contornam o Seal e o Blind, e os Knight Ammonites explodem ao serem derrotados.'),
       related='fc-ch2-q-11', sources=[ACAD])
c.boss(t('Black-clad soldiers', 'Soldados de preto'), t('Varenne Lighthouse — top', 'Varenne Lighthouse — topo'),
       t('Very fast: Clock Up EX helps. The claw soldier\'s sweep hits hard, so spread out, and don\'t push both into Rage at once.',
         'Muito rápidos: Clock Up EX ajuda. A varrida do soldado com garras bate forte, então espalhe a equipe e não leve os dois ao Rage juntos.'), sources=[ACAD])
c.boss(t('Fango and Bronco', 'Fango e Bronco'), t("Ruan — Mayor's Residence", 'Ruan — residência do prefeito'),
       t('When one wolf falls, its Death Throes greatly buffs the other: damage both evenly and finish them together, dispelling with Anti-Sept or Sever. Stay out of their fire and ice circles.',
         'Quando um lobo cai, o Death Throes dele fortalece muito o outro: distribua o dano e termine os dois juntos, removendo buffs com Anti-Sept ou Sever. Fique fora dos círculos de fogo e gelo.'),
       sources=[ACAD])

# ======================================================================== Chapter 3
c = chapter(3, 'Chapter 3', 'Capítulo 3')
ZEISS, ELMO, LEIS = NEO('Chapter 3 - Zeiss'), NEO('Chapter 3 - Elmo Village'), NEO('Chapter 3 - Leiston Fortress')
region_cp(c.cp('Requesting the border permit at Air-Letten (no return to Ruan)', 'Pedir a permissão de fronteira em Air-Letten (sem volta para Ruan)'), KALDIA)
PUMP = c.cp('Examining the pump shed in Elmo Village', 'Examinar a casa da bomba em Elmo Village')
FACTORY = c.cp('Reaching the 3rd-floor workshop during the factory incident', 'Chegar à oficina do 3º andar durante o incidente na fábrica')
TOWER = c.cp('The fight at the Carnelia Tower entrance', 'A luta na entrada da Carnelia Tower')
REPORT = c.cp('Reporting at the guild after visiting Leiston Fortress', 'Relatar na guilda depois de visitar a Leiston Fortress')
AIRSHIP = c.cp('Telling Chief Murdock you are ready (airship to Leiston)', 'Dizer ao Chief Murdock que você está pronto (airship para Leiston)')
END3 = c.cp('Examining the boat at Leiston Fortress (end of Chapter 3)', 'Examinar o barco na Leiston Fortress (fim do Capítulo 3)')
quest(c, 'Looking for Librarian', ('Zeiss Central Factory — Constance, 2F library', 'Zeiss Central Factory — Constance, biblioteca do 2F'), PUMP,
      ('3 BP. Recover three books: 3F Design Room (steel table), 4F Laboratory (table) and 4F Clinic (drawer). It starts the Overtime chain.',
       '3 BP. Recupere três livros: sala de projetos do 3F (mesa de aço), laboratório do 4F (mesa) e clínica do 4F (gaveta). Começa a sequência Overtime.'), [ZEISS])
quest(c, 'Present for Parents', ('Zeiss — Russell Home', 'Zeiss — Russell Home'), PUMP,
      ('4 BP. Not on the board, new in the remake. Check the mailbox, then Tita\'s desk (3rd option). Visit the chapel plaque and Ray in the 4F Laboratory, and defeat the pink Creepy Sheep in southwest Tratt Plains for its wool.',
       '4 BP. Não aparece no quadro, nova no remake. Veja a caixa de correio e depois a mesa da Tita (3ª opção). Visite a placa da capela e o Ray no laboratório do 4F, e derrote a Creepy Sheep rosa no sudoeste das Tratt Plains para pegar a lã.'), [ELMO], hidden=True)
quest(c, 'Product Piloting', ('Zeiss Central Factory — Terry, 4F laboratory', 'Zeiss Central Factory — Terry, laboratório do 4F'), PUMP,
      ('4 (+2) BP. Wear the Strega-α on Estelle and visit at least four of Air-Letten, Wolf Fort, Sanktheim Gate, Leiston Fortress and Elmo Village (fast travel counts).',
       '4 (+2) BP. Equipe as Strega-α na Estelle e visite pelo menos quatro entre Air-Letten, Wolf Fort, Sanktheim Gate, Leiston Fortress e Elmo Village (viagem rápida conta).'), [ELMO])
quest(c, 'Stopping Smoking', ('Zeiss Central Factory — Dr. Miriam, 4F clinic', 'Zeiss Central Factory — Dr. Miriam, clínica do 4F'), PUMP,
      ('4 BP. Give Antoine fresh milk, ask Travis (5F) about the cigarettes, talk to Chief Murdock (2F), take the Back Room Key from the desk and check his desk in the back room.',
       '4 BP. Dê leite fresco ao Antoine, pergunte ao Travis (5F) sobre os cigarros, fale com o Chief Murdock (2F), pegue a Back Room Key na mesa e examine a mesa dele na sala dos fundos.'), [ELMO])
quest(c, 'Fresher Flavors', ('Zeiss — Ben at Forgel Bar', 'Zeiss — Ben no Forgel Bar'), PUMP,
      ('3 BP. Pick an Acerbic Tomato from the plants in the 4F laboratory greenhouse and show it to Ben. Rewards Acerbic Tomato Sandwich.',
       '3 BP. Pegue um Acerbic Tomato das plantas na estufa do laboratório do 4F e mostre ao Ben. Dá o Acerbic Tomato Sandwich.'), [ELMO])
quest(c, 'Tratt Plains Monster', ('Tratt Plains Road', 'Tratt Plains Road'), PUMP,
      ('4 BP. Tanky against physical hits but weak to arts and most ailments; it shields itself at low HP.',
       '4 BP. Aguenta golpes físicos, mas é fraco contra arts e quase todos os efeitos; ele se protege com pouco HP.'), [ELMO])
quest(c, 'Cargo Car', ('Tratt Plains Road — the stranded cargo car', 'Tratt Plains Road — o carro de carga parado'), PUMP,
      ('4 BP. Talk to Wong and beat the Armored Rabbits. Unlocks Roadside Repair.', '4 BP. Fale com o Wong e derrote os Armored Rabbits. Libera a Roadside Repair.'), [ELMO])
quest(c, 'Roadside Repair', ('Tratt Plains Road — Wong', 'Tratt Plains Road — Wong'), PUMP,
      ('5 BP. Talk to Prometheus (3F), read the Orbal Automobile entry on the 5F computer, get the Drive Orbment from Rudi in Kaldia Tunnel and bring it to Wong.',
       '5 BP. Fale com o Prometheus (3F), leia a entrada do Orbal Automobile no computador do 5F, pegue o Drive Orbment com o Rudi no Kaldia Tunnel e leve ao Wong.'), [ELMO])
quest(c, 'Cupid on Cue', ('Wolf Fort — Private Brahm', 'Wolf Fort — Private Brahm'), PUMP,
      ('2 (+4) BP. Not on the board. Deliver his letter to Fey (factory B1F) with a gift: the Wool Knit Cap from Bell Station gives the full +4; Work Gloves or a Seasonal Tart give +2.',
       '2 (+4) BP. Não aparece no quadro. Entregue a carta dele à Fey (B1F da fábrica) com um presente: o Wool Knit Cap da Bell Station dá os +4; Work Gloves ou uma Seasonal Tart dão +2.'), [ELMO], hidden=True)
quest(c, 'Ritter Rd Monster', ('Ritter Roadway — where the road splits', 'Ritter Roadway — onde a estrada se divide'), PUMP,
      ('5 BP. Clear the small snakes with area attacks and bring poison protection.', '5 BP. Derrube as cobras pequenas com ataques em área e leve proteção contra veneno.'), [ELMO])
quest(c, 'Overtime', ('Elmo Village — stone by the hot springs', 'Elmo Village — pedra junto às fontes termais'), PUMP,
      ('3 BP. After Looking for Librarian. Take The Erbe Woodpecker back to Constance.', '3 BP. Depois da Looking for Librarian. Devolva The Erbe Woodpecker à Constance.'), [ELMO])
quest(c, 'Over-Overtime', ('Tratt Plains Road — the four stone pillars near Carnelia Tower', 'Tratt Plains Road — os quatro pilares de pedra perto da Carnelia Tower'), PUMP,
      ("4 BP. Examine the central pillar for Hertz's Adventure Vol. 2 and return it.", "4 BP. Examine o pilar do centro para pegar Hertz's Adventure Vol. 2 e devolva."), [ELMO])
quest(c, 'Over-Over-Overtime', ('Sanktheim Gate — top floor', 'Sanktheim Gate — último andar'), PUMP,
      ('4 BP. The book 31 Cypress Trees is on a barrel (with an Impede 3).', '4 BP. O livro 31 Cypress Trees está sobre um barril (com um Impede 3).'), [ELMO])
quest(c, 'Ritter Rd Monster 2', ('Ritter Roadway', 'Ritter Roadway'), AIRSHIP,
      ('6 BP. Short deadline. Defeating the leader buffs the other wolves and it can revive them: bring Anti-Sept All. You can wait until Agate and Tita rejoin, but it expires once you board the airship for Leiston.',
       '6 BP. Prazo curto. Derrotar o líder fortalece os outros lobos, e ele pode revivê-los: leve Anti-Sept All. Dá para esperar o Agate e a Tita voltarem, mas a quest expira quando você embarca no airship para Leiston.'), [LEIS])
bonus(c, ('the smoke canisters', 'os botijões de fumaça'), ('Zeiss Central Factory — emergency stairs', 'Zeiss Central Factory — escada de emergência'), FACTORY,
      ('+5 BP (Factory Incident): examine all five smoke canisters (blue markers), +1 each, before going to the 3F workshop.',
       '+5 BP (Factory Incident): examine os cinco botijões de fumaça (marcadores azuis), +1 cada, antes de ir à oficina do 3F.'), [LEIS])
bonus(c, ('the answer at Carnelia Tower', 'a resposta na Carnelia Tower'), ('Carnelia Tower — entrance', 'Carnelia Tower — entrada'), TOWER,
      ('+3 BP (Factory Incident). After the fight at the entrance, pick the 3rd option.', '+3 BP (Factory Incident). Depois da luta na entrada, escolha a 3ª opção.'), [LEIS])
bonus(c, ('the answer at the Zeiss guild', 'a resposta na guilda de Zeiss'), ('Zeiss — Bracer Guild', 'Zeiss — Bracer Guild'), REPORT,
      ('+3 BP (Vanished Professor). Back at the guild after Leiston Fortress, pick the 3rd option.', '+3 BP (Vanished Professor). De volta à guilda depois da Leiston Fortress, escolha a 3ª opção.'), [LEIS])
bonus(c, ('sneaking into Leiston Fortress', 'entrar escondido na Leiston Fortress'), ('Leiston Fortress', 'Leiston Fortress'), END3,
      ('+3 BP (Vanished Professor). Get past the alerted guards without being seen (slip by on the left, watching their sight on the minimap). Save first.',
       '+3 BP (Vanished Professor). Passe pelos guardas em alerta sem ser visto (vá pela esquerda, observando a visão deles no minimapa). Salve antes.'), [LEIS])
book(c, 'Carnelia Vol. 6', ('Jenis Royal Academy — Violet, clubhouse 2F', 'Jenis Royal Academy — Violet, 2º andar do clube'), KALDIA,
     ('Before leaving Ruan at the start of the chapter. Bell Station in Zeiss sells it if missed.', 'Antes de sair de Ruan, no começo do capítulo. A Bell Station em Zeiss vende se você perder.'), [ZEISS])
book(c, 'Liberl News Issue 6', ("Ruan — O'Neil Duty-Free Shop", "Ruan — O'Neil Duty-Free Shop"), KALDIA,
     ('Buy it before leaving Ruan at the start of the chapter.', 'Compre antes de sair de Ruan, no começo do capítulo.'), [ZEISS])
book(c, "Hertz's Adventure Vol. 1", ('Zeiss Central Factory — 2F library bookshelf', 'Zeiss Central Factory — estante da biblioteca do 2F'), PUMP,
     ('Examine the bookshelf.', 'Examine a estante.'), [ZEISS])
book(c, 'Crystal Optical Theory', ('Zeiss Central Factory', 'Zeiss Central Factory'), PUMP,
     ('Part of Looking for Librarian.', 'Parte da Looking for Librarian.'), [ZEISS])
book(c, "Tomorrow's Cooking", ('Zeiss Central Factory', 'Zeiss Central Factory'), PUMP,
     ('Part of Looking for Librarian. Reading it in the notebook teaches Portable Bouillabaisse.', 'Parte da Looking for Librarian. Lê-lo no caderno ensina o Portable Bouillabaisse.'), [ZEISS])
book(c, 'Cat Talk for Dummies', ('Zeiss Central Factory', 'Zeiss Central Factory'), PUMP,
     ('Part of Looking for Librarian.', 'Parte da Looking for Librarian.'), [ZEISS])
book(c, 'The Erbe Woodpecker', ('Elmo Village — hot springs', 'Elmo Village — fontes termais'), PUMP,
     ('Found during Overtime.', 'Encontrado durante a Overtime.'), [ELMO])
book(c, "Hertz's Adventure Vol. 2", ('Tratt Plains Road — stone pillars', 'Tratt Plains Road — pilares de pedra'), PUMP,
     ('Found during Over-Overtime.', 'Encontrado durante a Over-Overtime.'), [ELMO])
book(c, '31 Cypress Trees', ('Sanktheim Gate — top floor', 'Sanktheim Gate — último andar'), PUMP,
     ('Found during Over-Over-Overtime.', 'Encontrado durante a Over-Over-Overtime.'), [ELMO])
book(c, 'Carnelia Vol. 7', ('Wolf Fort — Bruno', 'Wolf Fort — Bruno'), SANKTHEIM,
     ('After the factory incident. Bell Station sells it if missed.', 'Depois do incidente na fábrica. A Bell Station vende se você perder.'), [LEIS])
book(c, 'Liberl News Issue 7', ('Zeiss — Bell Station', 'Zeiss — Bell Station'), SANKTHEIM,
     ('Buy it before leaving the Zeiss region.', 'Compre antes de sair da região de Zeiss.'), [LEIS])
recipes(c, ('Zeiss region', 'região de Zeiss'), [
    ('Spiral Pasta', 'Forgel Bar', 'Forgel Bar'),
    ('Black Pepper Soup', 'Forgel Bar', 'Forgel Bar'),
    ('Seasonal Tart', 'Forgel Bar', 'Forgel Bar'),
    ('Portable Bouillabaisse', "read Tomorrow's Cooking in the notebook", "leia Tomorrow's Cooking no caderno"),
    ('Acerbic Tomato Sandwich', 'Fresher Flavors reward', 'recompensa da Fresher Flavors'),
    ("Meat Lover's Hot Pot", 'Sanktheim Gate cafeteria', 'cafeteria do Sanktheim Gate'),
    ('Infernal Fried Eggs', 'chest on Carnelia Tower 5F', 'baú no 5F da Carnelia Tower'),
    ('Soft-Boiled Hot Spring Egg', 'Autumn Souvenirs, Elmo Village', 'Autumn Souvenirs, Elmo Village'),
    ('Fruit Milk', 'Maple Leaf Inn diner (after the pump is fixed)', 'restaurante da Maple Leaf Inn (depois do conserto da bomba)'),
    ('Special Eggnog', 'Maple Leaf Inn diner', 'restaurante da Maple Leaf Inn'),
    ('Monster Fish Sashimi', 'Maple Leaf Inn diner', 'restaurante da Maple Leaf Inn'),
    ('Wild Veggie Hot Pot', 'Maple Leaf Inn diner', 'restaurante da Maple Leaf Inn'),
], SANKTHEIM, EAT, [ZEISS, ELMO])
chests(c, ('Kaldia Tunnel', 'Kaldia Tunnel'), list(range(109, 116)), SANKTHEIM,
       ('Combo Attacks and Full Burst are introduced here.', 'Combo Attacks e Full Burst são apresentados aqui.'), [ZEISS])
chests(c, ('Kaldia Limestone Cave', 'Kaldia Limestone Cave'), list(range(116, 125)), SANKTHEIM,
       ('Optional and stronger than you at first; you return in the story. Pengus fall to Confuse and Deathblow; the two monster chests give Tita\'s G-Impact and the Black Coat.',
        'Opcional e mais forte que você no começo; você volta na história. Os Pengus caem com Confuse e Deathblow; os dois baús de monstros dão o G-Impact da Tita e o Black Coat.'), [ZEISS])
chests(c, ('Tratt Plains Road', 'Tratt Plains Road'), list(range(125, 138)), SANKTHEIM,
       ('Includes Wolf Fort and the hidden cave on the east side; the Shining Pom of the region spawns here.', 'Inclui o Wolf Fort e a caverna escondida no lado leste; o Shining Pom da região aparece aqui.'), [ELMO])
chests(c, ('Carnelia Tower', 'Carnelia Tower'), list(range(138, 146)), SANKTHEIM,
       ('On 2F each staircase leads to a chest; only the middle one goes up. The Trappers are weak to water and explode.', 'No 2F cada escada leva a um baú; só a do meio sobe. Os Trappers são fracos contra água e explodem.'), [ELMO])
chests(c, ('Ritter Roadway', 'Ritter Roadway'), list(range(146, 151)), SANKTHEIM,
       ('Follow the road to the end of Soldat Army Road; also touch Sanktheim Gate for fast travel.', 'Siga a estrada até o fim da Soldat Army Road; passe também pelo Sanktheim Gate para a viagem rápida.'), [ELMO])
c.boss(t('Rhinoking'), t('Tratt Plains Road'),
       t('A huge HP sponge for physical parties: use arts and ailments (Blind, Confuse, Sleep). It shields itself and Rages at low HP.',
         'Uma esponja de HP para equipes físicas: use arts e efeitos (Blind, Confuse, Sleep). Ele se protege e entra em Rage com pouco HP.'),
       related='fc-ch3-q-05', sources=[ELMO])
c.boss(t('Mercury Viper'), t('Ritter Roadway'),
       t('Wipe the small snakes with one area attack and bring poison protection (or Tita\'s Vital Cannon to cleanse).',
         'Derrube as cobras pequenas com um ataque em área e leve proteção contra veneno (ou o Vital Cannon da Tita para curar).'),
       related='fc-ch3-q-08', sources=[ELMO])
c.boss(t('Black-clad soldiers', 'Soldados de preto'), t('Carnelia Tower — roof', 'Carnelia Tower — terraço'),
       t('Seal, Poison and Deathblow; they Rage below half HP. Chaos Brand works, and Agate and Joshua\'s S-Crafts finish them, but brace for Rage.',
         'Seal, Poison e Deathblow; entram em Rage abaixo da metade do HP. Chaos Brand funciona, e os S-Crafts do Agate e do Joshua finalizam, mas prepare-se para o Rage.'), sources=[LEIS])
c.boss(t('King Pengu'), t('Kaldia Limestone Cave'),
       t('Wear Confuse protection and spread out against Tuna Missile. Chaos Brand stops its worst moves; near the end it calls guards and a huge area attack.',
         'Use proteção contra Confuse e espalhe a equipe contra o Tuna Missile. Chaos Brand impede os piores golpes; perto do fim ele chama guardas e um ataque em área enorme.'), sources=[LEIS])
c.boss(t('Bloody Saber'), t('Ritter Roadway'),
       t('Defeating it buffs the remaining wolves and it can revive them all: clear the wolves first or dispel with Anti-Sept All. Joshua\'s Evil Eye confuses the pack.',
         'Derrotá-lo fortalece os lobos restantes, e ele pode reviver todos: derrube os lobos primeiro ou remova os buffs com Anti-Sept All. O Evil Eye do Joshua confunde a matilha.'),
       related='fc-ch3-q-12', sources=[LEIS])

# ======================================================================== Final Chapter
c = chapter(4, 'Final Chapter', 'Capítulo Final')
GRAN, SEW, VILLA, FINAL = NEO('Final Chapter - Grancel'), NEO('Final Chapter - Grancel Sewers'), NEO('Final Chapter - Erbe Royal Villa'), NEO('Final Chapter - Final Dungeon')
region_cp(c.cp('Requesting the border permit at Sanktheim Gate (no return to Zeiss)', 'Pedir a permissão de fronteira no Sanktheim Gate (sem volta para Zeiss)'), SANKTHEIM)
GUILD = c.cp('Arriving at the Grancel Bracer Guild', 'Chegar à Bracer Guild de Grancel')
PROFILES = c.cp('Reading the profiles at the Liberl News Service', 'Ler os perfis no Liberl News Service')
CATHEDRAL = c.cp('Sneaking to the cathedral at night', 'Ir escondido até a catedral à noite')
FINAL_MATCH = c.cp('Talking to the Usher for the Grand Arena final', 'Falar com o Usher para a final da Grand Arena')
OPERATION = c.cp('Starting the operation with Elnan (point of no return)', 'Começar a operação com o Elnan (ponto sem volta)')
NOON = c.cp('Waiting until noon at the North Block sewer door', 'Esperar até o meio-dia na porta do esgoto do North Block')
KEEP = c.cp('The battles in the Royal Keep', 'As batalhas no Royal Keep')
FINAL_DOOR = c.cp('Opening the giant door on the bottom level of the Sealed Area', 'Abrir a porta gigante no nível mais baixo da Sealed Area')
ENDING = c.cp('Resting on the East Block benches (the ending)', 'Descansar nos bancos do East Block (o final)')
quest(c, 'Wayside Wallet', ('Grancel — Anton or Ricky at the Edel Department Store', 'Grancel — Anton ou Ricky na Edel Department Store'), FINAL_MATCH,
      ('5 BP. New in the remake. Talk to Culetti (Sunnybell Inn), Armand or Ellie (South Block) and Private Barranco (Gurune Gate), then bring the wallet back.',
       '5 BP. Nova no remake. Fale com o Culetti (Sunnybell Inn), o Armand ou a Ellie (South Block) e o Private Barranco (Gurune Gate), depois devolva a carteira.'), [GRAN])
quest(c, 'Child Custody', ('Grancel — tourist couple outside the cathedral', 'Grancel — casal de turistas em frente à catedral'), FINAL_MATCH,
      ("5 BP. New in the remake. Check the castle entrance, talk to Grant (East Block), see the scene at the Landing Port and finish at the Fisherman's Guild.",
       "5 BP. Nova no remake. Vá à entrada do castelo, fale com o Grant (East Block), veja a cena no Landing Port e termine na Fisherman's Guild."), [SEW])
quest(c, 'W Block Sewers Monster', ('Grancel Sewers — W. Block', 'Grancel Sewers — W. Block'), FINAL_MATCH,
      ("8 BP. Use Zin's Taunt to pull the crowd and clear it with wind arts. The same sewers hold Chewy Spare Ribs, the last recipe.",
       '8 BP. Use o Taunt do Zin para atrair o grupo e derrube-o com arts de vento. O mesmo esgoto tem as Chewy Spare Ribs, a última receita.'), [SEW])
quest(c, 'Myriad Monsters', ('Grancel — Elnan at the Bracer Guild', 'Grancel — Elnan na Bracer Guild'), FINAL_MATCH,
      ('6 BP. New in the remake. Clear the monsters marked on his map; the boss then appears near the hidden cave. Use area attacks so it can\'t keep reviving the Millipede Balls.',
       '6 BP. Nova no remake. Derrote os monstros marcados no mapa dele; o chefe aparece em seguida perto da caverna escondida. Use ataques em área para ele não ficar revivendo as Millipede Balls.'), [SEW])
quest(c, 'E Block Sewers Monster', ('Grancel Sewers — E. Block', 'Grancel Sewers — E. Block'), FINAL_MATCH,
      ('8 BP. In the first rooms downstairs. Freeze protection makes it easy; its Pearl Mirror reflects one attack.',
       '8 BP. Nas primeiras salas do andar de baixo. Proteção contra Freeze facilita; o Pearl Mirror dele reflete um ataque.'), [SEW])
quest(c, 'Embassy Emergency', ('Grancel Castle — lounge', 'Grancel Castle — salão'), ENDING,
      ('3 BP. After the final battle: meet Olivier in the castle lounge, read the request at the guild, then return to the lounge and watch the fireworks.',
       '3 BP. Depois da batalha final: encontre o Olivier no salão do castelo, leia o pedido na guilda, volte ao salão e veja os fogos.'), [FINAL])
bonus(c, ('the answer at the Grancel guild', 'a resposta na guilda de Grancel'), ('Grancel — Bracer Guild', 'Grancel — Bracer Guild'), GUILD,
      ('+1 BP (Royal Message). Pick the 3rd option: the letter of introduction won\'t work?', '+1 BP (Royal Message). Escolha a 3ª opção: a carta de apresentação não vai funcionar?'), [GRAN])
bonus(c, ('the name at the Liberl News Service', 'o nome no Liberl News Service'), ('Grancel — Liberl News Service', 'Grancel — Liberl News Service'), PROFILES,
      ('+2 BP (Royal Message). After reading the profiles, pick the 3rd option.', '+2 BP (Royal Message). Depois de ler os perfis, escolha a 3ª opção.'), [SEW])
bonus(c, ('reaching the cathedral unseen', 'chegar à catedral sem ser visto'), ('Grancel — at night', 'Grancel — à noite'), CATHEDRAL,
      ('+5 BP (Royal Message). Reach the cathedral without being caught once. Detour to the landing port first for Carnelia Vol. 10. Save first.',
       '+5 BP (Royal Message). Chegue à catedral sem ser pego nenhuma vez. Passe antes no porto para pegar o Carnelia Vol. 10. Salve antes.'), [SEW])
bonus(c, ('the two answers at the Liberl News Service', 'as duas respostas no Liberl News Service'), ('Grancel — Liberl News Service', 'Grancel — Liberl News Service'), OPERATION,
      ('+4 BP (Hostage Rescue). Upstairs, pick the 2nd option both times.', '+4 BP (Hostage Rescue). No andar de cima, escolha a 2ª opção nas duas vezes.'), [VILLA])
bonus(c, ('the battles in the Royal Keep', 'as batalhas no Royal Keep'), ('Grancel Castle — Royal Keep', 'Grancel Castle — Royal Keep'), KEEP,
      ('+5 BP (Save the Queen): don\'t defeat the Duke in the first fight (+2; keep area attacks off him and skip Burst), then win the last fight (+3).',
       '+5 BP (Save the Queen): não derrote o Duque na primeira luta (+2; mantenha os ataques em área longe dele e não use Burst), depois vença a última luta (+3).'), [VILLA])
c.item('missable', t('Trade the Carnelia volumes for the ultimate weapons', 'Trocar os volumes de Carnelia pelas armas definitivas'), t('Grancel — Baral at Baral Coffee House', 'Grancel — Baral no Baral Coffee House'), OPERATION,
       t('With all 11 volumes, Baral trades them for Estelle and Joshua\'s strongest weapons. Missed volumes 8–11 are sold at the Edel Department Store.',
         'Com os 11 volumes, o Baral troca pelas armas mais fortes da Estelle e do Joshua. Os volumes 8 a 11 perdidos são vendidos na Edel Department Store.'), 0, [VILLA])
book(c, 'Carnelia Vol. 8', ('Air-Letten — Private Otto', 'Air-Letten — Private Otto'), SANKTHEIM,
     ('At the start of the chapter, before leaving Zeiss.', 'No começo do capítulo, antes de sair de Zeiss.'), [GRAN])
book(c, 'Carnelia Vol. 9', ('Gurune Gate — Private Selbourne, upstairs', 'Gurune Gate — Private Selbourne, andar de cima'), OPERATION,
     ('East of Kirsche Avenue.', 'A leste da Kirsche Avenue.'), [GRAN])
book(c, 'Carnelia Vol. 10', ('Grancel — Ralph at the landing port', 'Grancel — Ralph no porto'), CATHEDRAL,
     ('During the night sneak to the cathedral (blue marker).', 'Durante a ida escondida até a catedral à noite (marcador azul).'), [SEW])
book(c, 'Carnelia Vol. 11', ('Grancel — Anton by the Edel Department Store', 'Grancel — Anton perto da Edel Department Store'), FINAL_MATCH,
     ('Talk to him and Marsha each time she walks by; on her third pass, he hands it over.', 'Fale com ele e com a Marsha cada vez que ela passar; na terceira passagem, ele entrega o livro.'), [SEW])
book(c, 'Liberl News Issue 8', ('Grancel — Edel Department Store, General Goods', 'Grancel — Edel Department Store, General Goods'), OPERATION,
     ('Buy it before the point of no return.', 'Compre antes do ponto sem volta.'), [GRAN])
book(c, 'Liberl News Issue 9', ('Grancel — Edel Department Store, General Goods', 'Grancel — Edel Department Store, General Goods'), OPERATION,
     ('Out on Day 5, before the point of no return.', 'Sai no Dia 5, antes do ponto sem volta.'), [VILLA])
book(c, 'Liberl News - Special Edition', ('Grancel — Edel Department Store, General Goods', 'Grancel — Edel Department Store, General Goods'), ENDING,
     ('After the final battle, before resting on the benches.', 'Depois da batalha final, antes de descansar nos bancos.'), [FINAL])
recipes(c, ('Grancel', 'Grancel'), [
    ('Gorgeous Crepe', "Nonna's Crepe Shop, South Block", "Nonna's Crepe Shop, South Block"),
    ('Concentrated Espresso', 'Baral Coffee House, West Block', 'Baral Coffee House, West Block'),
    ('Artisan Rice Curry', 'Baral Coffee House, West Block', 'Baral Coffee House, West Block'),
    ('Mixed Cocktail', 'Sunnybell Inn, South Block', 'Sunnybell Inn, South Block'),
    ('Refreshing Pie', 'Sunnybell Inn, South Block', 'Sunnybell Inn, South Block'),
    ('Hearty Bouillabaisse', 'Sunnybell Inn, South Block', 'Sunnybell Inn, South Block'),
    ('Special Ice Cream', "Sorbet's Ice Cream Shop, East Block", "Sorbet's Ice Cream Shop, East Block"),
    ('Chewy Spare Ribs', 'chest in the W. Block sewers', 'baú no esgoto do W. Block'),
], OPERATION, EAT, [GRAN, SEW])
chests(c, ('Kirsche Avenue', 'Kirsche Avenue'), [151, 152, 153, 154], OPERATION,
       ('Gurune Gate, to the east, has Carnelia Vol. 9.', 'O Gurune Gate, a leste, tem o Carnelia Vol. 9.'), [GRAN])
chests(c, ('Erbe Scenic Route', 'Erbe Scenic Route'), [155, 156, 157, 158, 159], OPERATION,
       ('Easier if you come before the story escort. The hidden cave is behind the bushes at the Sapphirl Monument.', 'Mais fácil se você vier antes da escolta da história. A caverna escondida fica atrás dos arbustos no Sapphirl Monument.'), [GRAN])
chests(c, ('Grancel Sewers — W. Block', 'Grancel Sewers — W. Block'), [160, 161, 162, 163, 164], OPERATION,
       ('Includes Chewy Spare Ribs, the last standard recipe.', 'Inclui as Chewy Spare Ribs, a última receita padrão.'), [SEW])
chests(c, ('Grancel Sewers — E. Block', 'Grancel Sewers — E. Block'), [165, 166, 167, 168], OPERATION,
       ('A switch deeper in opens a shortcut to the W. Block.', 'Um interruptor mais ao fundo abre um atalho para o W. Block.'), [SEW])
chests(c, ('Grancel Sewers — N. Block', 'Grancel Sewers — N. Block'), [169, 170, 171, 172], NOON,
       ('One-time visit. The monster chest holds the Cloak quartz.', 'Visita única. O baú de monstros tem o quartzo Cloak.'), [VILLA])
SEALED = ('Many chests are locked behind fights and hold the strongest gear for the rest of the party. Check the minimap legend: the chest icon disappears once a floor is cleared.',
          'Muitos baús ficam atrás de lutas e têm o melhor equipamento para o resto da equipe. Veja a legenda do minimapa: o ícone de baú some quando o andar está limpo.')
chests(c, ('Sealed Area — 1st Level', 'Sealed Area — 1º nível'), list(range(173, 184)), FINAL_DOOR, SEALED, [FINAL])
chests(c, ('Sealed Area — 2nd Level', 'Sealed Area — 2º nível'), list(range(184, 193)), FINAL_DOOR,
       ('The Berserker chest is reached from this level by an elevator up to a corner of the 1st Level.', 'O baú do Berserker é alcançado a partir deste nível, por um elevador até um canto do 1º nível.'), [FINAL])
chests(c, ('Sealed Area — 3rd Level', 'Sealed Area — 3º nível'), list(range(193, 200)), FINAL_DOOR,
       ("Thor's Hammer on the 2nd Level is reached from here. You should be at 199 of 212 before the elevator down.", 'O Thor\'s Hammer do 2º nível é alcançado daqui. Você deve estar com 199 de 212 antes do elevador para baixo.'), [FINAL])
chests(c, ('Sealed Area — 4th Level', 'Sealed Area — 4º nível'), list(range(200, 213)), FINAL_DOOR,
       ('Take the left (east) path first, then the west path down. Opening the last one gives Treasure Hunter if none were missed.', 'Pegue primeiro o caminho da esquerda (leste), depois o oeste descendo. Abrir o último dá o Treasure Hunter se nenhum ficou para trás.'), [FINAL])
c.boss(t('The Ravens', 'Os Ravens'), t('Grand Arena'),
       t('A pushover by now: burst them down with area arts or S-Crafts right after stunning them.',
         'Fácil a esta altura: derrube com arts em área ou S-Crafts logo depois de atordoá-los.'), sources=[GRAN])
c.boss(t('Zvryu Dryu'), t('Grancel Sewers — W. Block'),
       t("One of the easiest fights: Zin's Taunt draws everything, and wind arts plus a Full Burst wipe the crowd.",
         'Uma das lutas mais fáceis: o Taunt do Zin atrai todos, e arts de vento com um Full Burst limpam o grupo.'),
       related='fc-ch4-q-03', sources=[SEW])
c.boss(t('The Grancel bracers', 'Os bracers de Grancel'), t('Grand Arena — semi-final', 'Grand Arena — semifinal'),
       t("Have Zin bait them with Taunt (and Sylphen Wing), dispel buffs with Anti-Sept All and burst them when stunned. Kurt can revive the others: don't leave him for last.",
         'Faça o Zin atraí-los com Taunt (e Sylphen Wing), remova buffs com Anti-Sept All e ataque com tudo quando atordoados. O Kurt pode reviver os outros: não o deixe por último.'),
       sources=[SEW])
c.boss(t('Hide Spinner'), t('Grancel outskirts', 'Arredores de Grancel'),
       t('It spends its turns reviving and buffing the Millipede Balls: keep up area attacks and Burst.',
         'Ele gasta os turnos revivendo e fortalecendo as Millipede Balls: mantenha os ataques em área e o Burst.'),
       related='fc-ch4-q-04', sources=[SEW])
c.boss(t('Dangle Bone'), t('Grancel Sewers — E. Block', 'Grancel Sewers — E. Block'),
       t('Freeze protection is the key; Pearl Mirror reflects one attack or art, and it calls more Bone Fish.',
         'Proteção contra Freeze é o essencial; o Pearl Mirror reflete um ataque ou art, e ele chama mais Bone Fish.'),
       related='fc-ch4-q-05', sources=[SEW])
c.boss(t('The arena final', 'A final da arena'), t('Grand Arena — final', 'Grand Arena — final'),
       t('The commander debuffs and splits into a weak copy (stun or defeat it for the notebook). Bait with Zin, keep buffs up and use area attacks; the soldiers can revive each other with balms.',
         'O comandante aplica debuffs e se divide numa cópia fraca (atordoe ou derrote para o caderno). Atraia com o Zin, mantenha os buffs e use ataques em área; os soldados podem se reviver com balms.'),
       sources=[SEW])
c.boss(t('Captain Amalthea'), t('Grancel Castle', 'Grancel Castle'),
       t('She drains EP/CP and inflicts Poison, Seal, Deathblow and Mute. Use Sylphen Wing or Kloe\'s Weiss Aura and keep Kloe\'s S-Break as a panic button.',
         'Ela drena EP/CP e causa Poison, Seal, Deathblow e Mute. Use Sylphen Wing ou o Weiss Aura da Kloe e guarde o S-Break da Kloe como botão de emergência.'),
       sources=[VILLA])
c.boss(t('The Duke and his guards', 'O Duque e os guardas'), t('Grancel Castle — Royal Keep', 'Grancel Castle — Royal Keep'),
       t('For the bonus, don\'t defeat the Duke: lure the soldiers away from him, aim area attacks elsewhere and skip Burst. Recover CP before the last enemy falls: the next fight is very hard.',
         'Para o bônus, não derrote o Duque: afaste os soldados dele, mire os ataques em área em outro lugar e não use Burst. Recupere CP antes de o último inimigo cair: a próxima luta é muito difícil.'),
       sources=[VILLA])
c.boss(t('Captain Amalthea (rematch)', 'Captain Amalthea (revanche)'), t('Sealed Area — 2nd Level', 'Sealed Area — 2º nível'),
       t('Same as before, with two Gandor+ that call minions; your best party handles it.', 'Igual à anterior, com dois Gandor+ que chamam ajudantes; sua melhor equipe resolve.'), sources=[FINAL])
c.boss(t('The colonel', 'O coronel'), t('Sealed Area — bottom level', 'Sealed Area — nível mais baixo'),
       t('His crafts hit small areas, so spread out; his S-Craft hits one target, so just revive. Heal HP and EP before the last blow: the next fight starts as you end this one.',
         'Os crafts dele acertam áreas pequenas, então espalhe a equipe; o S-Craft acerta um alvo só, então basta reviver. Recupere HP e EP antes do golpe final: a próxima luta começa assim que esta termina.'),
       sources=[FINAL])
c.boss(t('The final battle', 'A batalha final'), t('Sealed Area — beyond the giant door', 'Sealed Area — além da porta gigante'),
       t('Several phases. Impede the side units\' casts and dispel the boss\'s Rage-like boosts at once. Later, block its single-target nuke with Earth Wall and impede its long area cast; from a third of its HP it stays enraged, so dispel and push through.',
         'Várias fases. Interrompa as conjurações das unidades laterais e remova na hora os reforços parecidos com Rage. Depois, bloqueie o ataque forte de alvo único com Earth Wall e interrompa a conjuração longa em área; a partir de um terço do HP ele fica em Rage até o fim, então remova os buffs e insista.'),
       sources=[FINAL])

# ======================================================================== Recipe book (Collections)
for order, rows in {
    0: ['Maple Cookie', 'Wholesome Pasta', 'Fried Potatoes', 'Flowery Soda', "Carmine's Eye", 'Drill Meatballs', 'Dreamy Shell Bake', 'Salad Sandwich'],
    1: ['Sunshine Mille Crepe', 'Fullmouth Soup', 'Red Tail Soup', 'Astonishing Cheese Risotto', 'Sweet Castella', 'Flowery Jelly', 'Beast Steak',
        'Royal Omelette', 'Cursed Fried Eyeballs', 'Heaven-and-Hell Stew', 'Kasagin Tempura', 'Miso-Simmered Carp', 'Grilled Rockfish Skewer',
        'Salmon Meunière', 'Grilled Rainbow Trout', 'Apple Ice Cream', 'Fresh-Squeezed Juice'],
    2: ['Morning-Picked Herbal Tea', 'Stubborn Paella', 'Azelia Rosè', 'Steamed Roe in Sake', 'Healthy Rice Porridge', 'Blazing Fried Chicken',
        'Salt-Crusted Small Fish', 'Jenis Lunch', 'Coffee Ice Cream', 'Orange Ice Cream', 'Crunchy Popcorn', 'Rainbow Jelly Beans', 'Royal Crepe'],
    3: ['Spiral Pasta', 'Black Pepper Soup', 'Seasonal Tart', 'Portable Bouillabaisse', 'Acerbic Tomato Sandwich', "Meat Lover's Hot Pot",
        'Infernal Fried Eggs', 'Soft-Boiled Hot Spring Egg', 'Fruit Milk', 'Special Eggnog', 'Monster Fish Sashimi', 'Wild Veggie Hot Pot'],
    4: ['Gorgeous Crepe', 'Concentrated Espresso', 'Artisan Rice Curry', 'Mixed Cocktail', 'Refreshing Pie', 'Hearty Bouillabaisse',
        'Special Ice Cream', 'Chewy Spare Ribs'],
}.items():
    for name in rows:
        dish(CH[order], name, 'Eat it once; the checklist entry for its region says where to get it.',
             'Coma uma vez; a entrada da região no checklist diz onde conseguir.')

for order, rows in {
    0: [('Energy Smoothie', 'Estelle', "Carmine's Eye"), ('Potato Salad Sandwich', 'Joshua', 'Salad Sandwich')],
    1: [('Apple Compote', 'Estelle', 'Apple Ice Cream'), ('Fried Salmon', 'Joshua', 'Salmon Meunière')],
    2: [('Cheesy Chicken Burger', 'Estelle', 'Blazing Fried Chicken'), ('Colorful Fruit Punch', 'Joshua', 'Azelia Rosè')],
    3: [('Fluffy Pancakes', 'Estelle', 'Seasonal Tart'), ('Demi-glace Omelette Rice', 'Joshua', 'Infernal Fried Eggs')],
    4: [('Brown Sugar Syrup Parfait', 'Joshua', 'Special Ice Cream'), ('Hearty Baked Curry Doria', 'Estelle', 'Artisan Rice Curry')],
}.items():
    for name, cook, base in rows:
        dish(CH[order], name, f'Have {cook} cook {base}.', f'Peça para {"a" if cook == "Estelle" else "o"} {cook} cozinhar {base}.', kind='customized')

for c in CH.values():
    c.write()
