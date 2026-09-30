# Chapter 2 — rewritten in our own words from the Neoseeker walkthrough (facts only).
# Once published, never reorder or remove items: ids are derived from order.
from lib import Chapter, src, t

RUAN = src('Chapter 2 - Ruan')
ZEISS = src('Chapter 2 - Zeiss')
WOLF = src('Chapter 2 - Wolf Fort')
CH3 = src('Chapter 3 - Zeiss')
LEAVE_ZEISS = 'sc-ch3-cp-01'  # boarding the airliner from Zeiss to Grancel, early in Chapter 3

c = Chapter(2, 'Chapter 2', 'Capítulo 2')
LEAVE_RUAN = c.cp('Boarding the airliner out of Ruan', 'Embarcar no airliner saindo de Ruan')
FORT = c.cp('Going near the fort at the east end of Tratt Plains Road (red story marker)',
            'Chegar perto do forte no extremo leste da Tratt Plains Road (marcador vermelho)')
CAVE = c.cp('Entering the cave behind the wooden gate north of Elmo Village',
            'Entrar na caverna atrás do portão de madeira ao norte de Elmo Village')
END = c.cp('The last event marker of Chapter 2', 'O último marcador de evento do Capítulo 2')

# Quests
c.item('quest', t('Election Office Outrage'), t('Ruan — Hotel Blanche'), LEAVE_RUAN,
       t('+5 BP. Starts after talking to Nial and Dorothy downstairs; you stay inside the hotel until it ends. Ask everything until no new topics appear. Final answers: 6th, 2nd, 2nd, 2nd.',
         '+5 BP. Começa depois de falar com Nial e Dorothy no andar de baixo; você fica preso no hotel até terminar. Pergunte tudo até não surgirem assuntos novos. Respostas finais: 6ª, 2ª, 2ª, 2ª.'),
       1, [RUAN])
c.item('quest', t('Winners Wanted'), t('Ruan — Lavantar Bar & Casino'), LEAVE_RUAN,
       t('+4 BP. A wrong pick fails it. With Scherazard: Estelle 1st, 1st; Olivier 1st, 2nd; Scherazard 2nd. With Agate: Agate 1st, 1st; Olivier 1st, 2nd; Estelle 2nd.',
         '+4 BP. Uma escolha errada faz falhar. Com Scherazard: Estelle 1ª, 1ª; Olivier 1ª, 2ª; Scherazard 2ª. Com Agate: Agate 1ª, 1ª; Olivier 1ª, 2ª; Estelle 2ª.'),
       0, [RUAN])
c.item('quest', t('Stolen Sign'), t('Zeiss'), LEAVE_ZEISS,
       t('+4 BP. Ask Kilika about it. Cards: back of the clock tower in the plaza; the terminal in the factory 5F (Central Factory → All Orbal Technology → Bracer Guild Sign); under the three chimneys behind Forgel Bar; then talk to Fey by the conveyor on B1F.',
         '+4 BP. Pergunte à Kilika. Cartões: atrás da torre do relógio na praça; o terminal no 5F da fábrica (Central Factory → All Orbal Technology → Bracer Guild Sign); sob as três chaminés atrás do Forgel Bar; depois fale com a Fey na esteira do B1F.'),
       0, [ZEISS])
c.item('quest', t('Firearm Field Test'), t('Zeiss Central Factory — 3F', 'Zeiss Central Factory — 3º andar'), LEAVE_ZEISS,
       t('3 +2 BP. Karl gives Olivier a gun. Win 15 Command Battles on Tratt Plains Road with it equipped (10 is the minimum) before reporting back.',
         '3 +2 BP. O Karl dá uma arma ao Olivier. Vença 15 Command Battles na Tratt Plains Road com ela equipada (o mínimo é 10) antes de voltar.'),
       0, [ZEISS, CH3])
c.item('quest', t('Drill Duty'), t('Leiston Fortress — end of Soldat Army Road', 'Leiston Fortress — fim da Soldat Army Road'), FORT,
       t('3 +2 BP. Three rounds with no healing in between; you must win the last one for the bonus.',
         '3 +2 BP. Três rodadas sem cura entre elas; é preciso vencer a última para ganhar o bônus.'),
       0, [ZEISS])
c.item('quest', t('Kaldia Tunnel Monster'), t('Kaldia Tunnel'), LEAVE_ZEISS,
       t('+3 BP. Whale frogs swallow allies: hit the frog three times to free them.',
         '+3 BP. Os sapos-baleia engolem aliados: acerte o sapo três vezes para libertá-los.'),
       0, [ZEISS])
c.item('quest', t('Tratt Plains Monster'), t('Tratt Plains Road — east, before the fort path', 'Tratt Plains Road — leste, antes do caminho do forte'), LEAVE_ZEISS,
       t('+3 BP. Lots of ailments: debuff immunity makes it manageable. Do not wander into the fort by accident.',
         '+3 BP. Muitos efeitos negativos: imunidade a debuffs deixa a luta administrável. Cuidado para não entrar no forte sem querer.'),
       0, [ZEISS])
c.item('quest', t('Probe for Parts'), t('Zeiss Central Factory — ground floor', 'Zeiss Central Factory — térreo'), LEAVE_ZEISS,
       t('3 +2 BP. Find all 8 parts: 3 in the 3F Workshop, 4 in the 4F Laboratory and 1 by the cat in the 4F Clinic.',
         '3 +2 BP. Encontre as 8 peças: 3 na oficina do 3F, 4 no laboratório do 4F e 1 perto do gato na clínica do 4F.'),
       1, [WOLF])
c.item('quest', t('Vanquish the Voyeurs'), t('Elmo Village — Maple Leaf Inn'), CAVE,
       t('+4 BP. Equip Confuse and Sleep protection before talking to Mao.',
         '+4 BP. Equipe proteção contra Confuse e Sleep antes de falar com a Mao.'),
       1, [WOLF])
c.item('quest', t('Tratt Plains Monster 2'), t('Tratt Plains Road — southwest cliff fishing spot', 'Tratt Plains Road — pesqueiro no penhasco a sudoeste'), LEAVE_ZEISS,
       t('+3 BP. A swarm that drains EP and blinds: wind arts and big S-Crafts clear it fast.',
         '+3 BP. Um enxame que drena EP e cega: arts de vento e S-Crafts fortes resolvem rápido.'),
       1, [WOLF])
c.item('quest', t('Army Road Monster'), t('Soldat Army Road — near Leiston Fortress', 'Soldat Army Road — perto da Leiston Fortress'), LEAVE_ZEISS,
       t('+3 BP. Hits very hard: stack HP and keep buffs up.', '+3 BP. Bate muito forte: aumente o HP e mantenha os buffs.'),
       1, [WOLF])

# Missables
c.item('missable', t('Bonus BP: talk to Rudi in Kaldia Tunnel', 'BP bônus: falar com o Rudi no Kaldia Tunnel'), t('Kaldia Tunnel — near the factory exit', 'Kaldia Tunnel — perto da saída da fábrica'), FORT,
       t('+3 BP just for talking to him.', '+3 BP só por conversar com ele.'), 0, [ZEISS])
c.item('missable', t('Bonus BP: question in the storeroom', 'BP bônus: pergunta no depósito'), t('Sanktheim Gate'), CAVE,
       t('+3 BP. In the scene with Warrant Officer Talbot, pick the 3rd option.',
         '+3 BP. Na cena com o Warrant Officer Talbot, escolha a 3ª opção.'),
       1, [WOLF])
c.item('missable', t("Bonus BP: question in the professor's office", 'BP bônus: pergunta na sala do professor'), t('Zeiss Central Factory — 5F', 'Zeiss Central Factory — 5º andar'), CAVE,
       t('+2 BP. When asked where to go, pick the 3rd option.', '+2 BP. Quando perguntarem para onde ir, escolha a 3ª opção.'),
       1, [WOLF])

# Collectibles
c.item('collectible', t('Gambler Jack — Vol. 3'), t('Airliner to Zeiss', 'Airliner para Zeiss'), None,
       t('Talk to Olivier a second time after his scene on board. If you miss it, Bell Station in Zeiss sells a copy in Chapter 3.',
         'Fale com o Olivier uma segunda vez depois da cena dele a bordo. Se perder, a Bell Station em Zeiss vende uma cópia no Capítulo 3.'),
       0, [RUAN, CH3])
c.item('collectible', t('Liberl News Issue 3'), t('Zeiss — Bell Station'), LEAVE_ZEISS,
       t('Sold at Bell Station.', 'Vendido na Bell Station.'), 0, [ZEISS])
c.item('collectible', t('Recipes: Zeiss (4)', 'Receitas: Zeiss (4)'), t('Zeiss'), LEAVE_ZEISS,
       t("Magma Wings, Acerbic Tomato Sandwich (Ben also gives one) and Fruit Kingdom at Forgel Bar; Mysterious Paste at Priam's Drink Shop outside the factory.",
         "Magma Wings, Acerbic Tomato Sandwich (o Ben também dá um) e Fruit Kingdom no Forgel Bar; Mysterious Paste na Priam's Drink Shop, do lado de fora da fábrica."),
       0, [ZEISS])
c.item('collectible', t('Recipe: Golden Risotto', 'Receita: Golden Risotto'), t('Sanktheim Gate — cafeteria'), LEAVE_ZEISS,
       t('Take the northeast branch of Ritter Roadway.', 'Siga pelo ramo nordeste da Ritter Roadway.'), 0, [ZEISS])
c.item('collectible', t('Recipes: Elmo Village (3)', 'Receitas: Elmo Village (3)'), t('Elmo Village — Maple Leaf Inn'), LEAVE_ZEISS,
       t('Continental Eggs, Passionate Egg Roll and Top-Rated Shake.', 'Continental Eggs, Passionate Egg Roll e Top-Rated Shake.'), 0, [ZEISS])
c.item('collectible', t('Bunny Medal'), t('Elmo Village — Autumn Souvenirs'), LEAVE_ZEISS,
       t('2nd of the 5 animal medals.', '2ª das 5 medalhas de animais.'), 0, [ZEISS])
c.item('collectible', t('Ritter Roadway treasure chests (3)', 'Baús da Ritter Roadway (3)'), t('Ritter Roadway'), LEAVE_ZEISS,
       t('Along both branches of the road.', 'Ao longo dos dois ramos da estrada.'), 0, [ZEISS])
c.item('collectible', t('Soldat Army Road treasure chests (4)', 'Baús da Soldat Army Road (4)'), t('Soldat Army Road'), LEAVE_ZEISS,
       t('Includes a monster chest with grasshoppers. Break the wall midway along the road to open a hidden water cave.',
         'Inclui um baú de monstros com gafanhotos. Quebre a parede no meio da estrada para abrir uma caverna com água escondida.'),
       0, [ZEISS])
c.item('collectible', t('Kaldia Tunnel treasure chests (6)', 'Baús do Kaldia Tunnel (6)'), t('Kaldia Tunnel'), LEAVE_ZEISS,
       t('Reached from the basement of Zeiss Central Factory.', 'Acesso pelo subsolo da Zeiss Central Factory.'), 0, [ZEISS])
c.item('collectible', t('Tratt Plains Road treasure chests (13)', 'Baús da Tratt Plains Road (13)'), t('Tratt Plains Road'), LEAVE_ZEISS,
       t('One holds the Pisces Heart fishing rod (east side). Includes a monster chest with sheep and mantises.',
         'Um guarda a vara de pesca Pisces Heart (lado leste). Inclui um baú de monstros com ovelhas e louva-a-deus.'),
       0, [ZEISS])
c.item('collectible', t('Carnelia Tower treasure chests (15)', 'Baús da Carnelia Tower (15)'), t('Carnelia Tower'), LEAVE_ZEISS,
       t('Optional tower northeast of Tratt Plains Road. The top-floor monster chest has five Fire Trappers: water arts, and keep away when they explode.',
         'Torre opcional a nordeste da Tratt Plains Road. O baú de monstros do último andar tem cinco Fire Trappers: use arts de água e se afaste quando explodirem.'),
       0, [ZEISS])
c.item('collectible', t('Hot spring cave treasure chests (9)', 'Baús da caverna das fontes termais (9)'), t('Cave north of Elmo Village', 'Caverna ao norte de Elmo Village'), END,
       t('Includes Septium Jelly Beans (eat it for the recipe) and a monster chest. The last two chests are down the side branch near the end, not the path to the healing device.',
         'Inclui Septium Jelly Beans (coma para ganhar a receita) e um baú de monstros. Os dois últimos baús ficam no desvio perto do fim, não no caminho do dispositivo de cura.'),
       1, [WOLF])

c.write()
