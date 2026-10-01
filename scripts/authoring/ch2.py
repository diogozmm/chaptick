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

# ---------------------------------------------------------------- bosses
c.boss(t('Neptune Frog'), t('Kaldia Tunnel'),
       t('The frogs swallow allies (three hits free them) and the swallower then repeats a short-delay area attack. Remove one Whale Frog before it swallows anyone, free allies first, then grind the rest down: no crippling ailments here.',
         'Os sapos engolem aliados (três golpes os libertam) e quem engoliu repete um ataque em área de pouco atraso. Derrube um Whale Frog antes que engula alguém, liberte os aliados primeiro e depois desgaste o resto: não há efeitos incapacitantes aqui.'),
       related='sc-ch2-q-06', sources=[ZEISS])
c.boss(t('Lt. Colonel Cid'), t('Leiston Fortress — final round', 'Leiston Fortress — última rodada'),
       t('Radiant Cleave hits a line for heavy damage: keep everyone high on HP. Always impede his arts; his Sylpharion gives his side arts reflect. Take out the soldiers, then Belc, then Cid. Strip his Rage Boost buffs, and after Indomitable Will finish him with S-Breaks.',
         'O Radiant Cleave atinge uma linha com muito dano: mantenha todos com HP alto. Interrompa sempre as arts dele; o Sylpharion dele dá reflexo de arts ao grupo. Derrube os soldados, depois o Belc e por fim o Cid. Remova os buffs do Rage Boost e, depois do Indomitable Will, finalize com S-Breaks.'),
       related='sc-ch2-q-05', sources=[ZEISS])
c.boss(t('Mantrap ×3'), t('Tratt Plains Road — east', 'Tratt Plains Road — leste'),
       t('A flood of ailments and stat downs, plus a swallow: debuff immunity (Sylphen Guard or Sylpharion) is close to mandatory. Free swallowed allies with three hits and keep healing.',
         'Uma enxurrada de efeitos e reduções de atributos, mais um ataque que engole: imunidade a debuffs (Sylphen Guard ou Sylpharion) é quase obrigatória. Liberte aliados engolidos com três golpes e mantenha a cura.'),
       related='sc-ch2-q-07', sources=[ZEISS])
c.boss(t('Big Creepy Sheep'), t('Elmo Village'),
       t('Phase one is six sheep inflicting Sleep, Blind and Confuse: be protected and use the time to buff and shield. In phase two the big sheep hits harder with the same ailments; Earth Wall blocks its attacks. Burst it when stunned.',
         'A primeira fase são seis ovelhas que causam Sleep, Blind e Confuse: esteja protegido e use o tempo para buffs e escudos. Na segunda fase, a ovelha grande bate mais forte com os mesmos efeitos; o Earth Wall bloqueia os ataques dela. Ataque forte quando atordoar.'),
       related='sc-ch2-q-09', sources=[WOLF])
c.boss(t('Ya-Kah ×8'), t('Tratt Plains Road — southwest cliff', 'Tratt Plains Road — penhasco a sudoeste'),
       t('Low HP, but they drain EP and CP, blind you and call more of their kind. Sweep them early with wind arts (Aero Storm, Grand Stream) or big S-Crafts.',
         'Pouco HP, mas drenam EP e CP, cegam e chamam mais da espécie. Varra-os cedo com arts de vento (Aero Storm, Grand Stream) ou S-Crafts fortes.'),
       related='sc-ch2-q-10', sources=[WOLF])
c.boss(t('Mustang Saber'), t('Soldat Army Road — near Leiston Fortress', 'Soldat Army Road — perto da Leiston Fortress'),
       t('No gimmick, just very high damage and a blinding zone. Stack HP and use Zodiac, debuff immunity and Foresight.',
         'Sem truques, só dano muito alto e uma zona que cega. Aumente o HP e use Zodiac, imunidade a debuffs e Foresight.'),
       related='sc-ch2-q-11', sources=[WOLF])
c.boss(t('Abyss Worms'), t('Hot spring cave — depths', 'Caverna das fontes termais — fundo'),
       t('The worms answer almost every hit, Chain and Burst included, with Earth-Shaker (heavy party damage and delay); counters do not trigger it. First kill the Parasite Primas without touching the worms, then take the worms one or two at a time with wind arts. Avoid area attacks that hit several worms.',
         'As minhocas respondem a quase todo golpe, inclusive Chain e Burst, com o Earth-Shaker (muito dano na equipe e atraso); contra-ataques não ativam. Primeiro derrube os Parasite Primas sem tocar nelas; depois pegue uma ou duas por vez com arts de vento. Evite ataques em área que acertem várias.'),
       sources=[WOLF])

# ---------------------------------------------------------------- fishing
CRAB, ANGEL, KASAGO, BLACKFISH, SEABASS, TROUT, CLAUDINE, EEL, OCTOPUS = (f'sc-ch1-fi-{n:02d}' for n in range(1, 10))
NEW = {}
for name in ['Kasagin', 'Yamany', 'Tiger Rockfish', 'Liberl Carp', 'Valleria Bass', 'Rainbow Trout', 'Carp',
             'Rockeater', 'Salmon', 'Snakehead', 'Mahi-Mahi']:
    NEW[name] = c.fish(name, sources=[CH3])
SW = t('Tratt Plains Road — southwest corner by the cliff', 'Tratt Plains Road — canto sudoeste, junto ao penhasco')
c.spot(CRAB, 'A', t('Tratt Plains Road — northeast and east ponds', 'Tratt Plains Road — lagos nordeste e leste'))
c.spot(ANGEL, 'A', SW)
c.spot(KASAGO, 'A', SW)
c.spot(BLACKFISH, 'A', SW)
c.spot(SEABASS, 'A', SW)
c.spot(CLAUDINE, 'B', SW)
c.spot(OCTOPUS, 'B', SW)
c.spot(TROUT, 'B', t('Leiston Fortress — outside', 'Leiston Fortress — lado de fora'))
c.spot(EEL, 'C', t('Elmo Village — Maple Leaf Inn courtyard', 'Elmo Village — pátio da Maple Leaf Inn'))
c.spot(NEW['Kasagin'], 'A', t('Tratt Plains Road — pond near Elmo Village; Leiston Fortress — outside', 'Tratt Plains Road — lago perto de Elmo Village; Leiston Fortress — lado de fora'))
c.spot(NEW['Yamany'], 'A', t('Kaldia Tunnel — bridge at the midpoint', 'Kaldia Tunnel — ponte no meio do caminho'))
c.spot(NEW['Tiger Rockfish'], 'B', t('Kaldia Tunnel bridge; Soldat Army Road water cave', 'Ponte do Kaldia Tunnel; caverna com água da Soldat Army Road'))
c.spot(NEW['Liberl Carp'], 'C', t('Tratt Plains Road ponds; Soldat Army Road water cave', 'Lagos da Tratt Plains Road; caverna com água da Soldat Army Road'))
c.spot(NEW['Valleria Bass'], 'C', t('Soldat Army Road water cave; Tratt Plains Road ponds', 'Caverna com água da Soldat Army Road; lagos da Tratt Plains Road'))
c.spot(NEW['Rainbow Trout'], 'C', t('Soldat Army Road water cave', 'Caverna com água da Soldat Army Road'))
c.spot(NEW['Carp'], 'B', t('Maple Leaf Inn courtyard; Tratt Plains Road ponds', 'Pátio da Maple Leaf Inn; lagos da Tratt Plains Road'))
c.spot(NEW['Rockeater'], 'B', t('Leiston Fortress — outside', 'Leiston Fortress — lado de fora'))
c.spot(NEW['Salmon'], 'B', t('Tratt Plains Road southwest corner; Leiston Fortress — outside', 'Canto sudoeste da Tratt Plains Road; Leiston Fortress — lado de fora'))
c.spot(NEW['Snakehead'], 'C', t('Tratt Plains Road — northeast and east ponds', 'Tratt Plains Road — lagos nordeste e leste'))
c.spot(NEW['Mahi-Mahi'], 'B', SW)

# ---------------------------------------------------------------- recipes
c.recipe('Magma Wings', t('Forgel Bar, Zeiss'), sources=[ZEISS])
c.recipe('Acerbic Tomato Sandwich', t('Forgel Bar, Zeiss (Ben also gives one)', 'Forgel Bar, Zeiss (o Ben também dá um)'), sources=[ZEISS])
c.recipe('Fruit Kingdom', t('Forgel Bar, Zeiss'), sources=[ZEISS])
c.recipe('Mysterious Paste', t("Priam's Drink Shop, outside Zeiss Central Factory", "Priam's Drink Shop, do lado de fora da Zeiss Central Factory"), sources=[ZEISS])
c.recipe('Golden Risotto', t('Sanktheim Gate cafeteria', 'Cafeteria do Sanktheim Gate'), sources=[ZEISS])
c.recipe('Continental Eggs', t('Maple Leaf Inn, Elmo Village'), sources=[ZEISS])
c.recipe('Passionate Egg Roll', t('Maple Leaf Inn, Elmo Village'), sources=[ZEISS])
c.recipe('Top-Rated Shake', t('Maple Leaf Inn, Elmo Village'), sources=[ZEISS])
c.recipe('Septium Jelly Beans', t('Treasure chest in the hot spring cave', 'Baú na caverna das fontes termais'), sources=[WOLF])
c.recipe('Ham & Egg Feast', t('Have Estelle cook Herb Sandwich', 'A Estelle cozinha Herb Sandwich'), 'customized', sources=[RUAN])
c.recipe('Breeze Basil Pasta', t('Have Scherazard cook Sea Breeze Soup (needs her in the party)', 'A Scherazard cozinha Sea Breeze Soup (precisa dela na equipe)'), 'customized', sources=[RUAN])
c.recipe('Thunderous Potato Soup', t('Have Agate cook Toasty Potato Wedges (needs him in the party)', 'O Agate cozinha Toasty Potato Wedges (precisa dele na equipe)'), 'customized', sources=[RUAN])

c.write()
