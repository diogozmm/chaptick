# Chapter 6 — rewritten in our own words from the GameFAQs walkthrough by shockinblue (facts only).
# Story-heavy chapter: places and fights after the first day use neutral wording and spoiler level 1.
# Once published, never reorder or remove items: ids are derived from order.
from lib import Chapter, gf, t

D1 = gf('Chapter 6 - Day 1')
D2 = gf('Chapter 6 - Day 2')

c = Chapter(6, 'Chapter 6', 'Capítulo 6')
BREATHER = c.cp('Choosing to take a breather at The Kingfisher Inn', 'Escolher fazer uma pausa na The Kingfisher Inn')
FACILITY = c.cp('The final fight inside the research facility', 'A luta final dentro da instalação de pesquisa')
END = c.cp('The last event marker of Chapter 6', 'O último marcador de evento do Capítulo 6')

# Quests
c.item('quest', t('Distant Days'), t('Bose — Kirsche Bar'), BREATHER,
       t('Reward: +6 BP. Show the old photo in this order.', 'Recompensa: +6 BP. Mostre a foto antiga nesta ordem.'),
       0, [D1], steps=[
           t('Get the old photo from Corna.', 'Pegue a foto antiga com Corna.'),
           t('Show it to Lila upstairs in the Mayor’s Residence.', 'Mostre a foto a Lila no andar de cima da residência do prefeito.'),
           t('Show it to the Mayor.', 'Mostre a foto ao prefeito.'),
       ], guidance={'rewards': [{'en': '+6 BP.', 'pt': '+6 BP.'}],
        'overview': {'en': 'Show the old photo in this order.', 'pt': 'Mostre a foto antiga nesta ordem.'}})
c.item('quest', t("Businesswoman's Bodyguard"), t("Bose — Trino's Home", 'Bose — casa do Trino'), BREATHER,
       t('BP: 4 (+2 bonus). Escort Milano from the west exit to Ravennue Village in under 10 minutes for the bonus.\nTimer: pauses during scenes and Command Battles, but each turn adds 5 seconds.\nForced fight: on Ravennue Trail; the leader is weak to water.', 'BP: 4 (+2 de bônus). Escolte Milano da saída oeste até Ravennue Village em menos de 10 minutos para receber o bônus.\nCronômetro: pausa nas cenas e nas Command Battles, mas cada turno custa 5 segundos.\nLuta obrigatória: em Ravennue Trail; o líder é fraco contra água.'),
       0, [D1], guidance={'rewards': [{'en': 'BP: 4 (+2 bonus).', 'pt': 'BP: 4 (+2 de bônus).'}],
        'overview': {'en': 'Escort Milano from the west exit to Ravennue Village in under 10 minutes for '
                           'the bonus.\n'
                           'Timer: pauses during scenes and Command Battles, but each turn adds 5 '
                           'seconds.\n'
                           'Forced fight: on Ravennue Trail; the leader is weak to water.',
                     'pt': 'Escolte Milano da saída oeste até Ravennue Village em menos de 10 minutos '
                           'para receber o bônus.\n'
                           'Cronômetro: pausa nas cenas e nas Command Battles, mas cada turno custa 5 '
                           'segundos.\n'
                           'Luta obrigatória: em Ravennue Trail; o líder é fraco contra água.'}})
c.item('quest', t('Mine Mop Up'), t('Abandoned mine — front gate', 'Mina abandonada — portão da frente'), BREATHER,
       t('One-time visit: collect the chest beyond the east exit before leaving.', 'Visita única: recolha o baú depois da saída leste antes de ir embora.'),
       0, [D1], steps=[
           t('Talk to the officers at the gate.', 'Fale com os oficiais no portão.'),
           t('Defeat every mystery machine inside until the game confirms they are all defeated.', 'Derrote todas as máquinas misteriosas lá dentro até o jogo confirmar que todas foram vencidas.'),
           t('Collect the chest beyond the east exit; you cannot return afterwards.', 'Recolha o baú depois da saída leste; depois disso, não será possível voltar.'),
       ])

# Missables
c.item('missable', t('Bonus BP: win the fight on the deck', 'BP bônus: vencer a luta no convés'), t('Later in the chapter', 'Mais adiante no capítulo'), END,
       t('Bonus: +5 BP. Save first: losing lets the story continue but costs the bonus.\nPreparation: equip Grail Locket or a Proxy Puppet.\nDuring the fight:\n• Keep Earth Guard active.\n• Use Grand Stream to inflict Blind.\n• When they start reviving each other, finish them with an area art.', 'Bônus: +5 BP. Salve antes: perder permite continuar a história, mas custa o bônus.\nPreparação: equipe Grail Locket ou Proxy Puppet.\nDurante a luta:\n• Mantenha Earth Guard ativo.\n• Use Grand Stream para causar Blind.\n• Quando começarem a reviver uns aos outros, finalize com uma art em área.'),
       2, [D2], guidance={'rewards': [{'en': 'Bonus: +5 BP.', 'pt': 'Bônus: +5 BP.'}],
        'overview': {'en': 'Save first: losing lets the story continue but costs the bonus.\n'
                           'Preparation: equip Grail Locket or a Proxy Puppet.\n'
                           'During the fight:\n'
                           '• Keep Earth Guard active.\n'
                           '• Use Grand Stream to inflict Blind.\n'
                           '• When they start reviving each other, finish them with an area art.',
                     'pt': 'Salve antes: perder permite continuar a história, mas custa o bônus.\n'
                           'Preparação: equipe Grail Locket ou Proxy Puppet.\n'
                           'Durante a luta:\n'
                           '• Mantenha Earth Guard ativo.\n'
                           '• Use Grand Stream para causar Blind.\n'
                           '• Quando começarem a reviver uns aos outros, finalize com uma art em área.'}})

# Collectibles
c.item('collectible', t('Liberl News Issue 8'), t('Bose Market — Grocery Minuet'), BREATHER,
       t('The rebuilt market sells it.', 'O mercado reconstruído vende.'), 0, [D1])
c.item('collectible', t('Gambler Jack — Vol. 8'), t('Ravennue Village'), BREATHER,
       t('Talk to Louie.', 'Fale com o Louie.'), 0, [D1])
c.item('collectible', t('Gambler Jack — Vol. 9'), t('Haken Gate'), BREATHER,
       t('Talk to Carlos.', 'Fale com o Carlos.'), 0, [D1])
c.item('collectible', t('Fishing rod: Lakelord II', 'Vara de pesca: Lakelord II'), t("Bose — Kuwano's Home", 'Bose — casa do Kuwano'), BREATHER,
       t('Follow Cecile’s request to obtain Lakelord II.', 'Siga o pedido de Cecile para obter Lakelord II.'),
       0, [D1], steps=[
           t('Talk to Cecile.', 'Fale com Cecile.'),
           t('Find her husband at Valleria Shore.', 'Encontre o marido dela em Valleria Shore.'),
           t('Return to Cecile.', 'Volte para falar com Cecile.'),
       ])
c.item('collectible', t('Research facility treasure chests (19)', 'Baús da instalação de pesquisa (19)'), t('Research facility', 'Instalação de pesquisa'), FACILITY,
       t('Several rooms open only with the three card keys you collect along the way, so backtrack once you have all of them (the monster chest needs the last key).\nIncludes Green Cookie (eat it for the recipe) and a second pair of Night-Vision Goggles for the dark room.', 'Várias salas só abrem com os três cartões de acesso que você pega pelo caminho, então volte quando tiver todos (o baú de monstros precisa do último).\nInclui Green Cookie (coma para ganhar a receita) e um segundo par de Night-Vision Goggles para a sala escura.'),
       1, [D2])
c.item('collectible', t('Ship treasure chests (11)', 'Baús da nave (11)'), t('Later in the chapter', 'Mais adiante no capítulo'), END,
       t('Includes Spicy Meatballs (eat it for the recipe) and a monster chest on the stern\'s first level. You cannot come back here.',
         'Inclui Spicy Meatballs (coma para ganhar a receita) e um baú de monstros no primeiro nível da popa. Não dá para voltar aqui.'),
       2, [D2])

# ---------------------------------------------------------------- routes (append-only once published)
c.set_steps('sc-ch6-co-05', [
    t('1F, east hallway, south door — Droplet of Defense', '1F, corredor leste, porta sul — Droplet of Defense'),
    t('1F, all the way north — Droplet of Spirit', '1F, todo o caminho ao norte — Droplet of Spirit'),
    t('1F, right hallway, last door on the right — Tearal Balm ×2', '1F, corredor da direita, última porta à direita — Tearal Balm ×2'),
    t('1F, next room, right door — Droplet of Strength', '1F, sala seguinte, porta da direita — Droplet of Strength'),
    t('2F, left door in the first room — EP Charge III ×2', '2F, porta da esquerda na primeira sala — EP Charge III ×2'),
    t('2F, second hallway, first door on the left — Night-Vision Goggles', '2F, segundo corredor, primeira porta à esquerda — Night-Vision Goggles'),
    t('2F, south exit, then left — Droplet of Life', '2F, saída sul e depois à esquerda — Droplet of Life'),
    t('2F dark room, along the right wall to the south door — Ebony Shoes+', '2F, sala escura, pela parede da direita até a porta sul — Ebony Shoes+'),
    t('2F, door at the end that needs the second key — Star Rabbits+', '2F, porta no fim que pede o segundo cartão — Star Rabbits+'),
    t('3F, outdoors — Green Cookie', '3F, área externa — Green Cookie'),
    t('3F, southern hallway, door on the left — All Sepith ×300', '3F, corredor sul, porta à esquerda — All Sepith ×300'),
    t('3F, room at the end (3 chests) — Ebony Suit+, Droplet of Magic, Zeram Powder', '3F, sala no fim (3 baús) — Ebony Suit+, Droplet of Magic, Zeram Powder'),
    t('With all keys: 1F, door to the north — All Sepith ×300', 'Com todos os cartões: 1F, porta ao norte — All Sepith ×300'),
    t('1F, door next to the room with the large machine — Misty Veil+', '1F, porta ao lado da sala com a máquina grande — Misty Veil+'),
    t('2F, door right of the elevator — All Sepith ×300', '2F, porta à direita do elevador — All Sepith ×300'),
    t('2F, door on the left side of the dark room — All Sepith ×300', '2F, porta no lado esquerdo da sala escura — All Sepith ×300'),
    t('3F, the hallway door you skipped — monster chest: Chronograph', '3F, a porta do corredor que você pulou — baú de monstros: Chronograph'),
], source=D2)
c.set_steps('sc-ch6-co-06', [
    t('Starting area, room on the left — Spicy Meatballs', 'Área inicial, sala à esquerda — Spicy Meatballs'),
    t('Next room — Tearal Balm', 'Sala seguinte — Tearal Balm'),
    t('North hallway, third room — EP Charge III', 'Corredor norte, terceira sala — EP Charge III'),
    t('Next level: first door on the left, upstairs, second door (3 chests) — Tearal Balm, Zeram Capsule, U-Material+', 'Nível seguinte: primeira porta à esquerda, andar de cima, segunda porta (3 baús) — Tearal Balm, Zeram Capsule, U-Material+'),
    t('Door across the hall to the north, upstairs, door on the right — Athelas Balm ×2', 'Porta do outro lado do corredor ao norte, andar de cima, porta à direita — Athelas Balm ×2'),
    t('Rear section, first level: middle room of the north hallway — Droplet of Life', 'Seção traseira, primeiro nível: sala do meio do corredor norte — Droplet of Life'),
    t('Southernmost hallway, center door — monster chest: Seven-Ring Staff', 'Corredor mais ao sul, porta central — baú de monstros: Seven-Ring Staff'),
    t('Rear section, second level: first room of the north hallway — EP Charge III', 'Seção traseira, segundo nível: primeira sala do corredor norte — EP Charge III'),
    t('Southernmost hallway, middle room — All Sepith ×300', 'Corredor mais ao sul, sala do meio — All Sepith ×300'),
], source=D2)

# ---------------------------------------------------------------- bosses
c.boss(t('Hide Spinner'), t('Ravennue Trail'),
       t('Part of the timed escort: blast the seven Millipede Balls with S-Crafts, then finish the leader with water arts. You should still have most of the clock left.',
         'Parte da escolta com tempo: destrua as sete Millipede Balls com S-Crafts e finalize o líder com arts de água. Ainda deve sobrar boa parte do tempo.'),
       related='sc-ch6-q-02', sources=[D1])
c.boss(t('Three duels in the facility', 'Três duelos na instalação'), t('Research facility', 'Instalação de pesquisa'),
       t('Three familiar fighters, one per floor, each with escort machines. All of them survive one lethal hit, so save an S-Break. Bring Sleep and Seal protection for the second, and expect the third to strip your buffs and steal bonuses.',
         'Três lutadores conhecidos, um por andar, cada um com máquinas de escolta. Todos sobrevivem a um golpe letal, então guarde um S-Break. Leve proteção contra Sleep e Seal para o segundo, e espere que o terceiro remova seus buffs e roube bônus.'),
       sources=[D2])
c.boss(t('Doppelrunner ×3'), t('Research facility — top floor', 'Instalação de pesquisa — último andar'),
       t('They spread out, so bring wide area arts. Each Rage Boost is followed by an S-Break that hits everyone, poisons and strips buffs: be ready to answer with your own S-Crafts, three times in a row.',
         'Eles se espalham, então leve arts de área ampla. Cada Rage Boost vem seguido de um S-Break que atinge todos, envenena e remove buffs: esteja pronto para responder com seus S-Crafts, três vezes seguidas.'),
       sources=[D2])
c.boss(t('Battle on the deck', 'Batalha no convés'), t('Later in the chapter', 'Mais adiante no capítulo'),
       t('See the bonus BP item: blind them with Grand Stream, shield up, and use area arts once they start reviving each other. Their counters still hurt while blinded.',
         'Veja o item de BP bônus: cegue-os com Grand Stream, use escudos e arts em área quando começarem a se reviver. Os contra-ataques ainda doem mesmo com eles cegos.'),
       related='sc-ch6-mi-01', sources=[D2])
c.boss(t('Pale Apache'), t('Later in the chapter', 'Mais adiante no capítulo'),
       t('Weak to wind and water. Resist Burn from its grenade, and watch for the charged line cannon that lowers stats.',
         'Fraco contra vento e água. Resista ao Burn da granada e fique atento ao canhão em linha carregado, que reduz atributos.'),
       sources=[D2])

# ---------------------------------------------------------------- recipes
c.recipe('Green Cookie', t('Treasure chest in the research facility', 'Baú na instalação de pesquisa'), sources=[D2])
c.recipe('Spicy Meatballs', t('Treasure chest later in the chapter', 'Baú mais adiante no capítulo'), sources=[D2])

c.write()
