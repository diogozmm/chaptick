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
       t('+6 BP. Corna gives you an old photo; show it to Lila upstairs in the Mayor\'s Residence, then to the Mayor.',
         '+6 BP. A Corna entrega uma foto antiga; mostre à Lila no andar de cima da residência do prefeito e depois à prefeita.'),
       0, [D1])
c.item('quest', t("Businesswoman's Bodyguard"), t("Bose — Trino's Home", 'Bose — casa do Trino'), BREATHER,
       t('4 +2 BP. Escort Milano from the west exit to Ravennue Village within 10 minutes for the bonus. The timer pauses in scenes and Command Battles, but each turn costs 5 seconds; a forced fight waits on Ravennue Trail (the leader is weak to water).',
         '4 +2 BP. Escolte a Milano da saída oeste até Ravennue Village em até 10 minutos para o bônus. O cronômetro pausa em cenas e Command Battles, mas cada turno custa 5 segundos; uma luta obrigatória espera na Ravennue Trail (o líder é fraco contra água).'),
       0, [D1])
c.item('quest', t('Mine Mop Up'), t('Abandoned mine — front gate', 'Mina abandonada — portão da frente'), BREATHER,
       t('Talk to the officers at the gate, then clear every mystery machine inside until the game says they are all defeated. Grab the chest beyond the east exit: there is no way back in afterwards.',
         'Fale com os oficiais no portão e depois derrote todas as máquinas misteriosas lá dentro até o jogo avisar que acabaram. Pegue o baú depois da saída leste: depois não dá para voltar.'),
       0, [D1])

# Missables
c.item('missable', t('Bonus BP: win the fight on the deck', 'BP bônus: vencer a luta no convés'), t('Later in the chapter', 'Mais adiante no capítulo'), END,
       t('+5 BP. Losing still lets the story go on, so save first. Equip Grail Locket or a Proxy Puppet, keep Earth Guard up, blind them with Grand Stream, and when they start reviving each other finish them with an area art.',
         '+5 BP. Perder não impede a história de seguir, então salve antes. Equipe Grail Locket ou um Proxy Puppet, mantenha o Earth Guard, cegue-os com Grand Stream e, quando começarem a se reviver, finalize com uma art em área.'),
       2, [D2])

# Collectibles
c.item('collectible', t('Liberl News Issue 8'), t('Bose Market — Grocery Minuet'), BREATHER,
       t('The rebuilt market sells it.', 'O mercado reconstruído vende.'), 0, [D1])
c.item('collectible', t('Gambler Jack — Vol. 8'), t('Ravennue Village'), BREATHER,
       t('Talk to Louie.', 'Fale com o Louie.'), 0, [D1])
c.item('collectible', t('Gambler Jack — Vol. 9'), t('Haken Gate'), BREATHER,
       t('Talk to Carlos.', 'Fale com o Carlos.'), 0, [D1])
c.item('collectible', t('Fishing rod: Lakelord II', 'Vara de pesca: Lakelord II'), t("Bose — Kuwano's Home", 'Bose — casa do Kuwano'), BREATHER,
       t('Talk to Cecile, find her husband at Valleria Shore, then come back to her.', 'Fale com a Cecile, encontre o marido dela na Valleria Shore e volte a ela.'),
       0, [D1])
c.item('collectible', t('Research facility treasure chests (19)', 'Baús da instalação de pesquisa (19)'), t('Research facility', 'Instalação de pesquisa'), FACILITY,
       t('Several rooms open only with the three card keys you collect along the way, so backtrack once you have all of them (the monster chest needs the last key). Includes Green Cookie (eat it for the recipe) and a second pair of Night-Vision Goggles for the dark room.',
         'Várias salas só abrem com os três cartões de acesso que você pega pelo caminho, então volte quando tiver todos (o baú de monstros precisa do último). Inclui Green Cookie (coma para ganhar a receita) e um segundo par de Night-Vision Goggles para a sala escura.'),
       1, [D2])
c.item('collectible', t('Ship treasure chests (11)', 'Baús da nave (11)'), t('Later in the chapter', 'Mais adiante no capítulo'), END,
       t('Includes Spicy Meatballs (eat it for the recipe) and a monster chest on the stern\'s first level. You cannot come back here.',
         'Inclui Spicy Meatballs (coma para ganhar a receita) e um baú de monstros no primeiro nível da popa. Não dá para voltar aqui.'),
       2, [D2])

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
