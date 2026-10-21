# Final Chapter — rewritten in our own words from the Neoseeker walkthrough (facts only).
# Chests are numbered by the guide's running count (436 to 566; 435 are found before this chapter).
# Once published, never reorder or remove items: ids are derived from order.
import json

from handbook import add as add_handbook
from lib import ROOT, Chapter, src, t

PART1 = src('Final Chapter - Part 1')
PART2 = src('Final Chapter - Part 2')
PART3 = src('Final Chapter - Part 3')
DUNGEON = src('Final Chapter - Final Dungeon')
BOSS = src('Final Chapter - Final Boss')

c = Chapter(9, 'Final Chapter', 'Capítulo Final')
GLORIOUS = c.cp('Unlocking the last prison barrier aboard the Glorious (you cannot go back inside)',
                'Destravar a última barreira da prisão a bordo do Glorious (não dá mais para voltar lá dentro)')
TOP = c.cp('Stepping into the last elevator at the top of the Axis Pillar (the final point of no return)',
           'Entrar no último elevador no topo do Axis Pillar (o último ponto sem volta)')

# Chest number -> (item, kind, note). kind is 'monster' (note = the fight) or 'place' (note = the building).
CHESTS = {
    436: ('Argem Gem', '', ''),
    437: ('Nohval Gem', '', ''),
    438: ('Brave Staff', 'monster', 'Phenomenon+ x3'),
    439: ('Zeram Powder', '', ''),
    440: ('Elixir of Defense', '', ''),
    441: ('Tear All Balm', '', ''),
    442: ('All Sepith x300', '', ''),
    443: ('Dominion', '', ''),
    444: ('Elixir of Strength', '', ''),
    445: ('All Sepith x300', '', ''),
    446: ('EP Charge IV', '', ''),
    447: ('U-Material+ x2', '', ''),
    448: ('Seal II', '', ''),
    449: ('All Sepith x300', 'place', 'Residence 1'),
    450: ('Elixir of Life', 'place', 'Residence 1'),
    451: ('Briareus', 'place', 'Residence 2'),
    452: ('Goldia Gem', 'place', 'City Hall'),
    453: ('Athelas Balm EX', 'place', 'City Hall'),
    454: ('Elixir of Spirit', 'place', 'Tavern'),
    455: ('Zeram Powder', 'place', 'Tavern'),
    456: ('U-Material+ x2', 'place', 'Tavern'),
    457: ('Elixir of Magic', 'place', 'Residence 4'),
    458: ('Aura Fencer', 'monster', 'Ebony Scale+, Ebony Scale x2'),
    459: ('All Sepith x300', '', ''),
    460: ('Hermes Wings', '', ''),
    461: ('Zeram Capsule', '', ''),
    462: ('Elixir of Magic', '', ''),
    463: ('Leigong Gem', '', ''),
    464: ('Persedia', '', ''),
    465: ('Beastking Blade', '', ''),
    466: ('Ω Craft', '', ''),
    467: ('Mars Gem', '', ''),
    468: ('All Sepith x300', '', ''),
    469: ('Ancient Steak', '', ''),
    470: ('Elixir of Strength', '', ''),
    471: ('Tear All Balm', '', ''),
    472: ('EP Charge IV', '', ''),
    473: ('U-Material+ x2', '', ''),
    474: ('Athelas Balm EX', '', ''),
    475: ('S-Tablet x3', '', ''),
    476: ('Dark Messiah', '', ''),
    477: ('Elixir of Life', '', ''),
    478: ('All Sepith x300', '', ''),
    479: ('U-Material+ x2', '', ''),
    480: ('Zeram Powder', '', ''),
    481: ('Aurelia Dress', '', ''),
    482: ('Curia Balm x3', '', ''),
    483: ('Jagd Girders', '', ''),
    484: ('Rievelder', '', ''),
    485: ('All Sepith x300', '', ''),
    486: ('Grail Locket', 'monster', 'Leor Gun-EZ+ x2'),
    487: ('U-Material+ x2', '', ''),
    488: ('Curia Balm x3', '', ''),
    489: ('Seven-Star Sword', '', ''),
    490: ('Elixir of Life', '', ''),
    491: ('U-Material+ x2', '', ''),
    492: ('Poison II', '', ''),
    493: ('All Sepith x300', '', ''),
    494: ('U-Material+ x2', '', ''),
    495: ('Tear All Balm', '', ''),
    496: ('EP Charge IV', '', ''),
    497: ('Athelas Balm EX', '', ''),
    498: ('Jagdpanther', '', ''),
    499: ('Curia Balm x3', '', ''),
    500: ('Elixir of Life', '', ''),
    501: ('Burn II', '', ''),
    502: ('All Sepith x300', '', ''),
    503: ('U-Material+ x2', '', ''),
    504: ('Rosencrantz', '', ''),
    505: ('S-Tablet x3', '', ''),
    506: ('Security Card', '', ''),
    507: ('Elixir of Life', '', ''),
    508: ('All Sepith x300', '', ''),
    509: ('Tear All Balm', '', ''),
    510: ('EP Charge IV', '', ''),
    511: ('U-Material+ x2', '', ''),
    512: ('Athelas Balm EX', '', ''),
    513: ('All Sepith x300', '', ''),
    514: ('Rakan Gem', '', ''),
    515: ('Zeram Powder', '', ''),
    516: ('Benten Gem', '', ''),
    517: ('Tear All Balm', '', ''),
    518: ('Elixir of Spirit', '', ''),
    519: ('EP Charge IV', '', ''),
    520: ('Elixir of Life', '', ''),
    521: ('Athelas Balm EX', '', ''),
    522: ('Prometheus', 'monster', 'Cyrus Grey+ x4'),
    523: ('Elixir of Defense', '', ''),
    524: ('S-Tablet x3', '', ''),
    525: ('Zeram Capsule', '', ''),
    526: ('Blind II', '', ''),
    527: ('U-Material+ x3', '', ''),
    528: ('Curia Balm x3', '', ''),
    529: ('Gaia Suit', 'monster', 'Master Trapper, Dark Zone x2'),
    530: ('Tear All Balm', '', ''),
    531: ('Elixir of Life', '', ''),
    532: ('EP Charge IV', '', ''),
    533: ('U-Material+ x3', '', ''),
    534: ('Athelas Balm EX', '', ''),
    535: ('Parthenon Gear', 'monster', 'Master Trapper x2, D-G Diver'),
    536: ('All Sepith x300', '', ''),
    537: ('Elixir of Strength', '', ''),
    538: ('Zeram Powder', '', ''),
    539: ('Mute II', '', ''),
    540: ('U-Material+ x3', '', ''),
    541: ('Curia Balm x3', '', ''),
    542: ('Spiegels', 'monster', 'Master Trapper, Arti-Pearl x2'),
    543: ('Tear All Balm', '', ''),
    544: ('Elixir of Magic', '', ''),
    545: ('EP Charge IV', '', ''),
    546: ('All Sepith x300', '', ''),
    547: ('Elixir of Defense', '', ''),
    548: ('Athelas Balm EX', '', ''),
    549: ('Jormungandr', '', ''),
    550: ('Tear All Balm', '', ''),
    551: ('U-Material+ x3', '', ''),
    552: ('EP Charge IV', '', ''),
    553: ('Zeram Capsule', '', ''),
    554: ('Athelas Balm EX', '', ''),
    555: ('Barbarossa Plating', 'monster', 'Master Trapper x2, Arti-Pearl, Fortune Coin, Knuckle Spider x2'),
    556: ('Tear All Balm', '', ''),
    557: ('EP Charge IV', '', ''),
    558: ('Athelas Balm EX', '', ''),
    559: ('Elixir of Life', '', ''),
    560: ('Tear All Balm', '', ''),
    561: ('All Sepith x300', '', ''),
    562: ('Elixir of Spirit', '', ''),
    563: ('U-Material+ x3', '', ''),
    564: ('Sieglinde Plating', 'monster', 'Master Trapper x4'),
    565: ('EP Charge IV', '', ''),
    566: ('Athelas Balm EX x4', '', ''),
}


def chest_steps(first, last):
    steps = []
    for n in range(first, last + 1):
        name, kind, note = CHESTS[n]
        if kind == 'monster':
            steps.append(t(f'#{n} — {name} (monster chest: fight {note})', f'#{n} — {name} (baú de monstros: luta contra {note})'))
        elif kind == 'place':
            steps.append(t(f'#{n} — {name} ({note})', f'#{n} — {name} ({note})'))
        else:
            steps.append(t(f'#{n} — {name}'))
    return steps


def chests(name, loc, until, first, last, overview, sources, warnings=None):
    """A group of consecutive chests as one item with one route step per chest."""
    guidance = {'overview': t(*overview)}
    if warnings:
        guidance['warnings'] = [t(*w) for w in warnings]
    monsters = [f'{CHESTS[n][0]} ({CHESTS[n][2]})' for n in range(first, last + 1) if CHESTS[n][1] == 'monster']
    hint_en = f'Chests #{first} to #{last}. {overview[0]}'
    hint_pt = f'Baús #{first} a #{last}. {overview[1]}'
    if monsters:
        hint_en += ' Monster chests: ' + '; '.join(monsters) + '.'
        hint_pt += ' Baús de monstros: ' + '; '.join(monsters) + '.'
    return c.item('collectible', name, loc, until, t(hint_en, hint_pt), 0, sources, steps=chest_steps(first, last), guidance=guidance)


# ------------------------------------------------------------------ Books, recipes, crafting
c.item('collectible', t('Liberl News Issue 11'), t('Arseille — cafeteria', 'Arseille — cafeteria'), TOP,
       t('Sold at the cafeteria counter. It is the last book you need for the Book Master trophy, so buy it before going up the pillar.',
         'Vendido no balcão da cafeteria. É o último livro para o troféu Book Master, então compre antes de subir o pilar.'),
       0, [PART1])
c.item('collectible', t('Recipes: the last three (3)', 'Receitas: as três últimas (3)'), t('Arseille, Cradle and Factoria', 'Arseille, Cradle e Factoria'), TOP,
       t('The final standard recipes, one per district. With them you reach 70 of 70.', 'As últimas receitas padrão, uma por distrito. Com elas você chega a 70 de 70.'),
       0, [PART1, PART2], steps=[
           t('Bitter Omelet — buy at the Arseille cafeteria.', 'Bitter Omelet — compre na cafeteria da Arseille.'),
           t('Resurrection Jelly — Residential District, terminal in Residence 1: "Check new recipes".', 'Resurrection Jelly — Residential District, terminal na Residence 1: "Check new recipes".'),
           t('Ancient Steak — treasure chest in the Industrial District, near the Glorious (chest #469).', 'Ancient Steak — baú no Industrial District, perto do Glorious (baú #469).'),
       ])
c.item('collectible', t('Customized dishes: Final Chapter (4)', 'Pratos customizados: Final Chapter (4)'), t('Arseille — kitchen', 'Arseille — cozinha'), TOP,
       t('Have the right cook make each new recipe once. Finishing the whole notebook earns Three-Star Chef and Peculiar Chef.',
         'Peça ao cozinheiro certo para fazer cada receita nova uma vez. Completar todo o caderno rende Three-Star Chef e Peculiar Chef.'),
       0, [PART1, PART2], steps=[
           t('Flamboyant Candy Lei — Olivier cooks Aurora Beans.', 'Flamboyant Candy Lei — Olivier cozinha Aurora Beans.'),
           t("Mom's Omelet & Chicken Rice — Estelle cooks Bitter Omelet.", "Mom's Omelet & Chicken Rice — Estelle cozinha Bitter Omelet."),
           t('Compote Jelly — Joshua cooks Resurrection Jelly.', 'Compote Jelly — Joshua cozinha Resurrection Jelly.'),
           t('Bustling Meatloaf — Kloe cooks Ancient Steak.', 'Bustling Meatloaf — Kloe cozinha Ancient Steak.'),
       ])
c.item('collectible', t('Zemurian Ore weapons (3)', 'Armas de Zemurian Ore (3)'), t('Arseille — Factory, B2F', 'Arseille — Factory, B2F'), TOP,
       t('Get the Data Crystal Z from the terminal in the Tavern, bring it to Professor Russell, then forge your three ores into the weapons you want. This earns the Ultimate Artificer trophy.',
         'Pegue o Data Crystal Z no terminal da Tavern, leve-o ao professor Russell e forje seus três minérios nas armas que quiser. Isso rende o troféu Ultimate Artificer.'),
       0, [PART1], steps=[
           t('Residential District, Tavern terminal: Data Crystal Z.', 'Residential District, terminal da Tavern: Data Crystal Z.'),
           t('Residence 1 terminal, "Verify Crystals": Zemurian Ore.', 'Terminal da Residence 1, "Verify Crystals": Zemurian Ore.'),
           t('Give the Data Crystal Z to Professor Russell in the Factory (B2F).', 'Entregue o Data Crystal Z ao professor Russell na Factory (B2F).'),
           t('Forge three weapons from Zemurian Ore.', 'Forje três armas com Zemurian Ore.'),
       ], guidance={
           'overview': t('A first playthrough gives exactly three ores.', 'Um primeiro jogo dá exatamente três minérios.'),
           'warnings': [t('Josette, Julia and Mueller join later, so you may want to save ore for their weapons.',
                                          'Josette, Julia e Mueller entram depois, então talvez valha guardar minério para as armas deles.')],
           'optional': [t('On New Game+ Professor Russell trades extra ore for 10 U-Material+ each.',
                          'No New Game+ o professor Russell troca minério extra por 10 U-Material+ cada.')]})
c.item('collectible', t('Gem quartz: all 14 (and True Gems)', 'Quartzos Gem: todos os 14 (e True Gems)'), t('Online Shop terminal at each Halo Rail station', 'Terminal Online Shop em cada estação do Halo Rail'), TOP,
       t('Connect each station with Emergency Mode, then synthesize its Gems at the Online Shop. Three Gems plus U-Material+ make the True version.',
         'Conecte cada estação com Emergency Mode e sintetize as Gems dela no Online Shop. Três Gems mais U-Material+ fazem a versão True.'),
       0, [PART1, PART2, PART3], steps=[
           t('West Calmare Station (Park District): Amberl, Sapphirl, Carnelia and Esmelas Gems.', 'West Calmare Station (Park District): Amberl, Sapphirl, Carnelia e Esmelas Gems.'),
           t('Cradle Station No. 35: Nohval, Goldia and Argem Gems.', 'Cradle Station No. 35: Nohval, Goldia e Argem Gems.'),
           t('Factoria Station No. 7: Rakan, Benten, Mars and Leigong Gems.', 'Factoria Station No. 7: Rakan, Benten, Mars e Leigong Gems.'),
           t('Axis Pillar Station: Hades, Deus and Odin Gems.', 'Axis Pillar Station: Hades, Deus e Odin Gems.'),
       ], guidance={
           'overview': t('Each Gem takes 2,500 to 3,000 of one sepith type. One True Gem of each kind costs roughly 25,000 of each sepith, so start farming early.',
                         'Cada Gem custa de 2.500 a 3.000 de um tipo de sepith. Uma True Gem de cada tipo custa cerca de 25.000 de cada sepith, então comece o farm cedo.')})

# ------------------------------------------------------------------ Treasure chests
chests(t('Park District tunnel treasure chests (9)', 'Baús do túnel do Park District (9)'),
       t('Liber Ark Underground Tunnel 1', 'Liber Ark Underground Tunnel 1'), TOP, 436, 444,
       ('The tunnel ends in a mandatory fight against Phenomenon+ and its helpers.', 'O túnel termina numa luta obrigatória contra Phenomenon+ e seus ajudantes.'), [PART1])
chests(t('Residential District treasure chests (13)', 'Baús do Residential District (13)'),
       t('Residential District (Cradle)', 'Residential District (Cradle)'), TOP, 445, 457,
       ('Enter the buildings for more chests. Be at 457 before moving on.', 'Entre nos prédios para achar mais baús. Esteja em 457 antes de seguir adiante.'), [PART1])
chests(t('Industrial tunnel and Factoria treasure chests (13)', 'Baús do túnel industrial e de Factoria (13)'),
       t('Liber Ark Underground Tunnel 2 and Industrial District', 'Liber Ark Underground Tunnel 2 e Industrial District'), TOP, 458, 470,
       ('Near the end of the tunnel is a mandatory fight against Ebony Scale+ and Brute Angler. The last two chests are by the Glorious, one with a recipe.',
        'Perto do fim do túnel há uma luta obrigatória contra Ebony Scale+ e Brute Angler. Os dois últimos baús ficam perto do Glorious, um deles com uma receita.'), [PART2])
chests(t('Glorious treasure chests (36)', 'Baús do Glorious (36)'),
       t('The Glorious — Stern and Bow', 'The Glorious — Stern e Bow'), GLORIOUS, 471, 506,
       ('This is the last visit to the ship. Stern 1st level, Stern 2nd level (two rooms of six, one with a monster chest), Bow 1st level (side room of three plus six upstairs), the prison and the Security Card chest.',
        'Esta é a última visita ao navio. Stern 1º nível, Stern 2º nível (duas salas de seis, uma com baú de monstros), Bow 1º nível (sala lateral com três mais seis no andar de cima), a prisão e o baú do Security Card.'),
       [PART3], warnings=[
           ('Open No. 2 and No. 4 in the prison first for the last two chests; unlocking No. 1 closes the ship for good.',
            'Abra primeiro as barreiras No. 2 e No. 4 na prisão para pegar os dois últimos baús; destravar a No. 1 fecha o navio para sempre.'),
           ('You should be at 506 chests and 369 of 410 battle entries before unlocking No. 1.',
            'Você deve estar com 506 baús e 369 de 410 entradas de batalha antes de destravar a No. 1.')])
chests(t('Underground tunnel treasure chests (16)', 'Baús do túnel subterrâneo (16)'),
       t('Liber Ark Underground Tunnel 3', 'Liber Ark Underground Tunnel 3'), TOP, 507, 522,
       ('Reached through Factoria Station No. 7 after entering the password at the terminal. Expect a mandatory fight against eight Cyrus Grey+ near the end.',
        'Alcançado pela Factoria Station No. 7 depois de digitar a senha no terminal. Espere uma luta obrigatória contra oito Cyrus Grey+ perto do fim.'), [PART3])
chests(t('Axis Pillar treasure chests, floors 1 to 3 (19)', 'Baús do Axis Pillar, andares 1 a 3 (19)'),
       t('Axis Pillar — 1F to 3F', 'Axis Pillar — 1º ao 3º andar'), TOP, 523, 541,
       ('1F has seven chests with a monster chest at the fork on the right. 2F has eight in the wide room after the first boss. 3F has four before the second boss.',
        'O 1º andar tem sete baús, com um baú de monstros na bifurcação da direita. O 2º tem oito na sala larga depois do primeiro boss. O 3º tem quatro antes do segundo boss.'),
       [DUNGEON])
chests(t('Axis Pillar treasure chests, floors 4 to 6 (25)', 'Baús do Axis Pillar, andares 4 a 6 (25)'),
       t('Axis Pillar — 4F to 6F', 'Axis Pillar — 4º ao 6º andar'), TOP, 542, 566,
       ('4F has fourteen chests, including monster chests and a six-chest room. 5F has four before the boss. 6F has seven, with a monster chest, and the last one holds Athelas Balm EX ×4.',
        'O 4º andar tem catorze baús, incluindo baús de monstros e uma sala com seis. O 5º tem quatro antes do boss. O 6º tem sete, com um baú de monstros, e o último guarda Athelas Balm EX ×4.'),
       [DUNGEON], warnings=[
           ('The 566th chest earns the Treasure Hunter trophy. Make a backup save before the final elevator.',
            'O 566º baú rende o troféu Treasure Hunter. Faça um backup do save antes do elevador final.')])

# ------------------------------------------------------------------ Missables
c.item('missable', t('Battle entries before leaving the Glorious', 'Entradas de batalha antes de deixar o Glorious'), t('The Glorious', 'The Glorious'), GLORIOUS,
       t('The ship\'s enemies are new Combat Handbook entries this time. Defeat them before unlocking barrier No. 1; you should have 369 of 410.',
         'Os inimigos do navio são entradas novas do Combat Handbook desta vez. Derrote-os antes de destravar a barreira No. 1; você deve ter 369 de 410.'),
       0, [PART3], guidance={'warnings': [t('The ship closes for good once you unlock barrier No. 1.', 'O navio fecha para sempre quando você destrava a barreira No. 1.')]})
c.item('missable', t('Battle entry: Dawn Trapper', 'Entrada de batalha: Dawn Trapper'), t('Liber Ark — Core Sector', 'Liber Ark — Core Sector'), None,
       t('Scan the Dawn Trapper in the Core Sector. If you miss it, the tunnels near the very end give a second and final chance. Without it you cannot finish the Combat Handbook (410 entries).',
         'Faça o scan do Dawn Trapper no Core Sector. Se perder, os túneis perto do fim dão uma segunda e última chance. Sem ele você não completa o Combat Handbook (410 entradas).'),
       1, [BOSS])
c.item('missable', t('Optional fight: the toughest boss', 'Luta opcional: o boss mais difícil'), t('Top of the Axis Pillar', 'Topo do Axis Pillar'), None,
       t('The hardest fight in the game, and the only thing it gives is a trophy. You may retry after a Game Over, or choose "Proceed as is" to move on. Save before taking the final elevator.',
         'A luta mais difícil do jogo, e a única coisa que ela dá é um troféu. Você pode tentar de novo depois de um Game Over ou escolher "Proceed as is" para seguir em frente. Salve antes de pegar o elevador final.'),
       1, [DUNGEON, BOSS], guidance={
           'preparation': [t('At least one source each of Earth Wall, Gaia Shield, Sylpharion and Zodiac.', 'Pelo menos uma fonte de cada: Earth Wall, Gaia Shield, Sylpharion e Zodiac.'),
                           t('Several sources of Clock Up EX, and True Gems on everyone (True Nohval Gem above all).', 'Várias fontes de Clock Up EX e True Gems em todos (a True Nohval Gem acima de tudo).'),
                           t('Set Joshua\'s default S-Break to True Black Fang in the Camp Menu (Status, then his Black Fang craft).', 'Defina o S-Break padrão do Joshua como True Black Fang no Camp Menu (Status, depois o craft Black Fang dele).')],
           'optional': [t('On a lower difficulty the fight is easier; on Nightmare you can lose and continue.', 'Em dificuldades menores a luta é mais fácil; no Nightmare você pode perder e continuar.')],
           'overview': t('Expect several attempts; that is normal.', 'Espere várias tentativas; isso é normal.')})

# Added after the first release: new items go last so published ids stay the same.
c.item('collectible', t('Handbook count check by area (6)', 'Conferência da contagem do handbook por área (6)'), t('Combat Handbook, in the camp menu', 'Combat Handbook, no menu de acampamento'), None,
       t('Compare the number of enemies recorded at each stage. The Dawn Trapper, the last entry, is a separate item above.',
         'Compare o número de inimigos registrados em cada etapa. A última entrada, o Dawn Trapper, é um item separado acima.'),
       0, [PART1, PART2, PART3, DUNGEON, BOSS], steps=[
           t('After the Cradle and Residential District: 352 of 410.', 'Depois do Cradle e do Residential District: 352 de 410.'),
           t('After the Industrial District: 356 of 410.', 'Depois do Industrial District: 356 de 410.'),
           t('Before unlocking barrier No. 1 on the Glorious: 369 of 410.', 'Antes de destravar a barreira No. 1 no Glorious: 369 de 410.'),
           t('Before the Axis Pillar: 376 of 410.', 'Antes do Axis Pillar: 376 de 410.'),
           t('Before the last elevator: 399 of 410.', 'Antes do último elevador: 399 de 410.'),
           t('After the final fights: 410 of 410.', 'Depois das lutas finais: 410 de 410.'),
       ])
c.item('collectible', t('Orbment upgrades: all 12 members', 'Orbment upgrades: os 12 membros'), t('Arseille — orbal factory', 'Arseille — fábrica orbal'), None,
       t('Raise every character\'s orbment slots to the maximum. Josette, Julia and Mueller join late, so this cannot be finished earlier.',
         'Leve os slots de orbment de cada personagem ao máximo. Josette, Julia e Mueller entram tarde, então não dá para terminar antes.'),
       0, [PART1, PART3], steps=[t(n) for n in ['Estelle', 'Joshua', 'Scherazard', 'Olivier', 'Kloe', 'Agate', 'Tita', 'Zin', 'Kevin', 'Josette', 'Julia', 'Mueller']])
c.item('collectible', t('Arts: unlock every art', 'Arts: desbloquear todas as arts'), t('Orbment line of any character', 'Linha de orbment de qualquer personagem'), None,
       t('The easiest way is to equip quartz on Olivier until he reaches 9 in each of the seven elements of his orbment line.',
         'O jeito mais fácil é equipar quartzos no Olivier até ele chegar a 9 em cada um dos sete elementos da linha de orbment dele.'),
       0, [PART3], steps=[t(n) for n in ['Earth', 'Water', 'Fire', 'Wind', 'Time', 'Space', 'Mirage']])
c.item('collectible', t("Estelle's Support Ability: level 9", 'Support Ability da Estelle: nível 9'), t('Estelle\'s status screen', 'Tela de status da Estelle'), None,
       t('Estelle\'s Support Ability should be at level 9 around the time you reach the Axis Pillar.',
         'A Support Ability da Estelle deve estar no nível 9 por volta da chegada ao Axis Pillar.'),
       0, [PART3])

add_handbook(c)

# ------------------------------------------------------------------ Bosses
c.boss(t('Leor Gun-EZ and Vogel 235'), t('Residential District — east side', 'Residential District — lado leste'),
       t('Josette joins as an NPC and holds her own. The boss survives one lethal hit with Quick Repair and uses Laser Net, Micro Missile and Electric Anchor ailments, so keep a finishing S-Break.',
         'A Josette entra como NPC e se vira sozinha. O boss sobrevive a um golpe letal com Quick Repair e usa efeitos como Laser Net, Micro Missile e Electric Anchor, então guarde um S-Break para finalizar.'),
       sources=[PART1])
c.boss(t('Pale Apaches and Spindolls'), t('The Glorious — deck', 'The Glorious — convés'),
       t('Each destroyed Apache leaves a Spindoll behind. They are still weak to Stat Down and Delay, so cripple them and move on.',
         'Cada Apache destruído deixa um Spindoll. Continuam fracos a Stat Down e Delay, então enfraqueça-os e siga.'),
       sources=[PART3])
c.boss(t('Bone Legger+ waves and Armored Compe'), t('Arseille — Julia and Mueller\'s party', 'Arseille — equipe da Julia e do Mueller'),
       t('A good fight to learn Julia and Mueller. Use Attack Orders and wide attacks on the Bone Leggers (Seal/Mute, AT Delay), then Debuff Immunity against Armored Compe\'s Petrify and Deathblow.',
         'Uma boa luta para aprender a jogar com Julia e Mueller. Use Attack Orders e ataques em área nos Bone Leggers (Seal/Mute, AT Delay) e depois Debuff Immunity contra o Petrify e o Deathblow do Armored Compe.'),
       sources=[PART3])
c.boss(t('Gilbert and Riot Arms'), t('The Glorious — Bow, 1st level', 'The Glorious — Bow, 1º nível'),
       t('The machine is the real threat: it is vulnerable to Delay and Stat Down (Orbal Down is great) and survives one lethal blow with Quick Repair. Gilbert rages at half HP and also endures one hit.',
         'A máquina é a verdadeira ameaça: é vulnerável a Delay e Stat Down (Orbal Down é ótimo) e sobrevive a um golpe letal com Quick Repair. Gilbert entra em fúria na metade do HP e também resiste a um golpe.'),
       sources=[PART3])
c.boss(t('Nox Bringer'), t('Liber Ark Underground Tunnel 3', 'Liber Ark Underground Tunnel 3'),
       t('Same pattern as the Chapter 1 finale: Mirror Flaggers reflect your attacks and heal the others when they die. Use that fight\'s plan or nuke it all; it can revive once with Indomitable Will.',
         'Mesmo padrão do final do Capítulo 1: os Mirror Flaggers refletem seus ataques e curam os outros ao morrer. Use o plano daquela luta ou elimine tudo de uma vez; ele pode reviver uma vez com Indomitable Will.'),
       sources=[PART3])
c.boss(t('Riot Claw and Solid Seekers'), t('Outside the Axis Pillar', 'Fora do Axis Pillar'),
       t('The claw hits hard and the Seekers have high DEF. Delay and Orbal Down work well, and the Seekers can be Confused.',
         'A garra bate forte e os Seekers têm DEF alta. Delay e Orbal Down funcionam bem, e os Seekers podem ser confundidos.'),
       sources=[PART3])
c.boss(t('Bleublanc (rematch)', 'Bleublanc (revanche)'), t('Axis Pillar — 2F', 'Axis Pillar — 2º andar'),
       t('Like the first fight, but he hits much harder, so block with Perfect Guard or reflect. Below 60% HP he boosts out of turn and follows with Death Magic (likely lethal): buff first and dispel afterwards. Auto Thelas heals him and triggers the boost at a lethal blow.',
         'Como na primeira luta, mas ele bate bem mais forte, então bloqueie com Perfect Guard ou reflexo. Abaixo de 60% do HP ele reforça fora do turno e segue com Death Magic (provavelmente letal): reforce os buffs antes e dissipe depois. O Auto Thelas o cura e ativa o reforço num golpe letal.'),
       sources=[DUNGEON])
c.boss(t('Walter (rematch)', 'Walter (revanche)'), t('Axis Pillar — 3F', 'Axis Pillar — 3º andar'),
       t('Zin must be in the party. Same boost and auto-revive tricks as Bleublanc, with an Ultimate Blow after the boost. Earth Wall, Gaia Shield or Kevin\'s Grail Sphere are key; Zin can bait with Taunt.',
         'O Zin precisa estar na equipe. Mesmos truques de reforço e autorrevivência do Bleublanc, com um Ultimate Blow depois do reforço. Earth Wall, Gaia Shield ou o Grail Sphere do Kevin são essenciais; o Zin pode atrair golpes com Taunt.'),
       sources=[DUNGEON])
c.boss(t('Luciola (rematch)', 'Luciola (revanche)'), t('Axis Pillar — 4F', 'Axis Pillar — 4º andar'),
       t('Scherazard must be in the party. Her Shadow Replication leaves a copy that hits as hard as she does. Sylpharion\'s Arts Reflect blocks the Firestorm S-Craft she uses after boosting. She has no auto-revive.',
         'A Scherazard precisa estar na equipe. O Shadow Replication deixa uma cópia que bate tão forte quanto ela. O Arts Reflect do Sylpharion bloqueia o S-Craft Firestorm que ela usa depois de reforçar. Ela não tem autorrevivência.'),
       sources=[DUNGEON])
c.boss(t('Renne and Pater-Mater'), t('Axis Pillar — 5F', 'Axis Pillar — 5º andar'),
       t('Bring Deathblow protection and Debuff Immunity; Kevin helps. Renne rages at once and S-Breaks, then boosts again under 60% (Sylpharion can reflect it). Pater-Mater\'s Double Buster Cannon needs Immunity plus Invulnerability or Arts Reflect, and it can revive a fallen Renne.',
         'Leve proteção contra Deathblow e Debuff Immunity; o Kevin ajuda. Renne entra em fúria de cara e usa S-Break, depois reforça de novo abaixo de 60% (o Sylpharion pode refletir). O Double Buster Cannon do Pater-Mater exige Immunity mais Invulnerability ou Arts Reflect, e ele pode reviver a Renne caída.'),
       sources=[DUNGEON])
c.boss(t('The Bladelord', 'O Bladelord'), t('Top of the Axis Pillar (optional)', 'Topo do Axis Pillar (opcional)'),
       t('Three phases: before 60% HP, after the boost and Dead Emperor Sword, and after the revive with Demon Flames. Keep several layers of Immunity, Earth Wall and Arts Reflect, dispel his buffs after each S-Break, and kill the Riot Sabers early. Anti-Sept Zero drains all EP and only Earth Wall or Grail Sphere stops it.',
         'Três fases: antes de 60% do HP, depois do reforço e do Dead Emperor Sword, e depois da revivência com Demon Flames. Mantenha várias camadas de Immunity, Earth Wall e Arts Reflect, dissipe os buffs dele depois de cada S-Break e mate os Riot Sabers cedo. O Anti-Sept Zero drena todo o EP e só o Earth Wall ou o Grail Sphere o impede.'),
       sources=[BOSS])
c.boss(t('Reverie Dragion'), t('Top of the Axis Pillar', 'Topo do Axis Pillar'),
       t('Much easier than the optional fight, even with a missing party member. Use your normal buffs and dispel its stat boost when it enters Carnage Boost below half HP.',
         'Bem mais fácil que a luta opcional, mesmo com um membro a menos. Use seus buffs normais e dissipe o aumento de atributos quando ele entrar em Carnage Boost abaixo da metade do HP.'),
       sources=[BOSS])
c.boss(t('Weissmann'), t('Top of the Axis Pillar', 'Topo do Axis Pillar'),
       t('Debuff Immunity is essential and Sylpharion helps. He is slow, so set up first and clear the four Combat Shells. Dimensional Exile removes someone for six turns. Below 60% HP, and again when he auto-revives, he boosts and uses Chaos Dimension, which can one-shot on Nightmare: have Perfect Guard and Arts Reflect up.',
         'Debuff Immunity é essencial e o Sylpharion ajuda. Ele é lento, então prepare-se primeiro e elimine os quatro Combat Shells. O Dimensional Exile tira alguém da luta por seis turnos. Abaixo de 60% do HP, e de novo quando ele autorrevive, ele reforça e usa Chaos Dimension, que pode matar de um golpe no Nightmare: mantenha Perfect Guard e Arts Reflect.'),
       sources=[BOSS])
c.boss(t('Angel Weissmann (first phase)', 'Angel Weissmann (primeira fase)'), t('Top of the Axis Pillar', 'Topo do Axis Pillar'),
       t('He cannot be hurt at first; wait for the scene. Then kill the Greed Loopers first, and prepare Arts Reflect or Perfect Guard for the Angel Boost S-Break. He has no auto-revive.',
         'No começo ele é invulnerável; espere a cena. Depois elimine primeiro os Greed Loopers e prepare Arts Reflect ou Perfect Guard para o S-Break do Angel Boost. Ele não tem autorrevivência.'),
       sources=[BOSS])
c.boss(t('Angel Weissmann (final phase)', 'Angel Weissmann (fase final)'), t('Top of the Axis Pillar', 'Topo do Axis Pillar'),
       t('Kill the four Alpha Omegas first. His left core gives him Arts Reflect and the right core Physical Reflect, so destroy them to open him up. Step away from glowing tiles before Ruined World Naoba, watch his element changes (Time, Space and Mirage hurt when he absorbs the four elements) and block the S-Break after Reborn Angel Boost.',
         'Mate primeiro os quatro Alpha Omegas. O núcleo esquerdo dá a ele Arts Reflect e o direito Physical Reflect, então destrua-os para abri-lo. Saia dos hexágonos brilhantes antes do Ruined World Naoba, observe as trocas de elemento (Time, Space e Mirage machucam quando ele absorve os quatro elementos) e bloqueie o S-Break depois do Reborn Angel Boost.'),
       sources=[BOSS])

# ------------------------------------------------------------------ Fishing (the Final Chapter spots)
ids = {}
for i in range(9):
    data = json.loads((ROOT / 'sc' / 'chapters' / f'ch-{i:02d}.json').read_text())
    for fish in data.get('fish', []):
        ids[fish['name']['en']] = fish['id']
SPOTS = [
    ('Park District (Calmare)', ['Crab', 'Gold Angelfish', 'Kasago', 'Great Blackfish', 'Rockeater', 'Snakehead']),
    ('Residential District (Cradle)', ['Kasagin', 'Yamany', 'Valleria Bass', 'Rainbow Trout', 'Trout', 'Mahi-Mahi']),
    ('Industrial District (Factoria)', ['Tiger Rockfish', 'Sea Bass', 'Salmon', 'Claudine', 'Pearlglass', 'Garvelze']),
    ('Axis Pillar — outside', ['Liberl Carp', 'Carp', 'Eel', 'Octopus', 'Granakor', 'Gigangora', 'Blue Marlin']),
]
for where, names in SPOTS:
    for name in names:
        c.spot(ids[name], 'A', t(where, where.replace('outside', 'do lado de fora')))

# ------------------------------------------------------------------ Recipes
c.recipe('Bitter Omelet', t('Arseille cafeteria', 'Cafeteria da Arseille'), sources=[PART1])
c.recipe('Resurrection Jelly', t('Terminal in Residence 1, Residential District', 'Terminal na Residence 1, Residential District'), sources=[PART1])
c.recipe('Ancient Steak', t('Treasure chest in the Industrial District', 'Baú no Industrial District'), sources=[PART2])
c.recipe('Flamboyant Candy Lei', t('Have Olivier cook Aurora Beans', 'O Olivier cozinha Aurora Beans'), 'customized', sources=[PART2])
c.recipe("Mom's Omelet & Chicken Rice", t('Have Estelle cook Bitter Omelet', 'A Estelle cozinha Bitter Omelet'), 'customized', sources=[PART2])
c.recipe('Compote Jelly', t('Have Joshua cook Resurrection Jelly', 'O Joshua cozinha Resurrection Jelly'), 'customized', sources=[PART2])
c.recipe('Bustling Meatloaf', t('Have Kloe cook Ancient Steak', 'A Kloe cozinha Ancient Steak'), 'customized', sources=[PART2])

c.write()
