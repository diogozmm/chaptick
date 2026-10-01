# Chapter 3 — rewritten in our own words from the Neoseeker walkthrough (facts only).
# Once published, never reorder or remove items: ids are derived from order.
from lib import Chapter, gf, src, t

ZEISS = src('Chapter 3 - Zeiss')
GRANCEL = src('Chapter 3 - Grancel')
VILLA = src('Chapter 3 - Erbe Royal Villa')
GURUNE = src('Chapter 3 - Gurune Gate')
GF1 = gf('Chapter 3 - Day 1')
GF2 = gf('Chapter 3 - Day 2')

c = Chapter(3, 'Chapter 3', 'Capítulo 3')
LEAVE_ZEISS = c.cp('Boarding the airliner from Zeiss to Grancel', 'Embarcar no airliner de Zeiss para Grancel', order=1)
VISITS = c.cp('Finishing the round of visits in the capital (the time of day changes)',
              'Terminar a rodada de visitas na capital (o horário do dia muda)', order=3)
END = c.cp('Boarding the airliner at the end of Chapter 3', 'Embarcar no airliner no fim do Capítulo 3', order=5)
# Added after cross-checking with GameFAQs; ids keep creation order, `order` places them in time.
VILLA_IN = c.cp('Entering Erbe Royal Villa (the road back is closed for a while)',
                'Entrar na Erbe Royal Villa (o caminho de volta fica fechado por um tempo)', order=2)
SEARCH = c.cp('Triggering the event near the landing port during the search in the capital',
              'Ativar o evento perto do porto de airships durante a busca na capital', order=4)

# Quests
c.item('quest', t('Guest Gone Missing'), t('Zeiss — Zahnrad Hotel'), LEAVE_ZEISS,
       t('+5 BP. Leads into Kaldia Limestone Cave, off Kaldia Tunnel. Bring Confuse and Seal protection, and keep the person you escort alive in the final fight.',
         '+5 BP. Leva à Kaldia Limestone Cave, a partir do Kaldia Tunnel. Leve proteção contra Confuse e Seal, e mantenha vivo quem você escolta na luta final.'),
       0, [ZEISS])
c.item('quest', t('Sewer Monster'), t('Grancel Sewers — W. Block, far end', 'Grancel Sewers — W. Block, no fim'), SEARCH,
       t('+4 BP. Trees that cripple stats and heal from damage: shields and debuff immunity; fire arts on the small ones first. Its deadline shortens mid-chapter, so finish it before advancing the search in the capital.',
         '+4 BP. Árvores que derrubam atributos e se curam causando dano: escudos e imunidade a debuffs; arts de fogo nas menores primeiro. O prazo encurta no meio do capítulo, então termine antes de avançar a busca na capital.'),
       0, [GRANCEL, GF2])
c.item('quest', t('Erbe Scenic Route Monster'), t('Erbe Scenic Route — middle intersection', 'Erbe Scenic Route — cruzamento central'), VILLA_IN,
       t('+4 BP. Blocks the way to the villa. Straightforward: buff up and burst when stunned.',
         '+4 BP. Bloqueia o caminho para a mansão. Direto ao ponto: faça buffs e ataque forte quando atordoar.'),
       0, [GRANCEL])
c.item('quest', t('Exhibit Enigma'), t('Grancel — History Museum, 2F', 'Grancel — History Museum, 2º andar'), VISITS,
       t("+4 BP. Cards: grandfather clock upstairs in General Morgan's house (next to the cathedral); the South Block fountain; Calvard Embassy, right room, The Doll Knight vol. 15; then the Grand Arena through the southern waiting room. Bring Freeze protection for the fight.",
         '+4 BP. Cartões: relógio de pêndulo no andar de cima da casa do General Morgan (ao lado da catedral); a fonte do South Block; embaixada de Calvard, sala à direita, The Doll Knight vol. 15; por fim, a Grand Arena pela sala de espera sul. Leve proteção contra Freeze para a luta.'),
       1, [VILLA])
c.item('quest', t('Sewer Monster 2'), t('Grancel Sewers — E. and N. Blocks', 'Grancel Sewers — E. e N. Blocks'), SEARCH,
       t('+4 BP. The North Block entrance is a breakable wall at the end of the East Block. Medium deadline: do it before advancing the search in the capital.',
         '+4 BP. A entrada do North Block é uma parede quebrável no fim do East Block. Prazo médio: faça antes de avançar a busca na capital.'),
       1, [VILLA, GF2])
c.item('quest', t('Piscine Pilferer'), t('Grancel Castle — entrance hall', 'Grancel Castle — saguão de entrada'), END,
       t('+4 BP. Needs Kloe in the party; talk to Hilda. You stay in the sewers until it ends, so prepare first.',
         '+4 BP. Precisa da Kloe na equipe; fale com a Hilda. Você fica nos esgotos até terminar, então se prepare antes.'),
       1, [GURUNE])
c.item('quest', t('Kirsche Avenue Monster'), t('Kirsche Avenue'), END,
       t('+4 BP. A big bird with Seal and all-stat-down attacks: debuff immunity plus arts reflect is ideal.',
         '+4 BP. Uma ave grande com ataques de Seal e redução de todos os atributos: imunidade a debuffs com reflexo de arts é o ideal.'),
       1, [GURUNE])

# Missables
c.item('missable', t('Bonus BP: the search at the villa', 'BP bônus: a busca na mansão'), t('Erbe Royal Villa'), VISITS,
       t('+3 BP. Do not give up and ask the butler for help. After checking every marker, examine the counter next to him in the Lounge.',
         '+3 BP. Não desista nem peça ajuda ao mordomo. Depois de checar todos os marcadores, examine o balcão ao lado dele no Lounge.'),
       1, [VILLA])
c.item('missable', t('Bonus BP: question at the guild', 'BP bônus: pergunta na guilda'), t('Grancel — Bracer Guild'), END,
       t('+2 BP. In the scene at the guild after visiting the Liberl News, pick the 2nd option.',
         '+2 BP. Na cena da guilda depois de visitar o Liberl News, escolha a 2ª opção.'),
       1, [VILLA])
c.item('missable', t('Bonus BP: question on the southern wall', 'BP bônus: pergunta na muralha sul'), t('Gurune Gate'), END,
       t('+3 BP. At the end of the southern wall, pick the 2nd option.', '+3 BP. No fim da muralha sul, escolha a 2ª opção.'),
       1, [GURUNE])

# Collectibles
c.item('collectible', t('Liberl News Issue 4'), t('Grancel — Edel Department Store, E. Block', 'Grancel — Edel Department Store, E. Block'), END,
       t('General goods counter.', 'Balcão de artigos gerais.'), 0, [GRANCEL])
c.item('collectible', t('Liberl News Issue 5'), t('Grancel — Edel Department Store, E. Block', 'Grancel — Edel Department Store, E. Block'), END,
       t('Appears later in the chapter at the same counter.', 'Aparece mais tarde no capítulo, no mesmo balcão.'), 0, [VILLA])
c.item('collectible', t('Gambler Jack — Vol. 4'), t('Grancel — embassy library, E. Block', 'Grancel — biblioteca da embaixada, E. Block'), None,
       t('Talk to Nathan in the library after the meeting upstairs. If missed, Edel Department Store sells it at the end of the chapter.',
         'Fale com o Nathan na biblioteca depois da reunião no andar de cima. Se perder, a Edel Department Store vende no fim do capítulo.'),
       1, [VILLA, GURUNE])
c.item('collectible', t('Gambler Jack — Vol. 5'), t('Grancel — Baral Coffee House, W. Block'), None,
       t('Talk to Connor. If missed, Edel Department Store sells it at the end of the chapter.',
         'Fale com o Connor. Se perder, a Edel Department Store vende no fim do capítulo.'),
       0, [VILLA, GURUNE])
c.item('collectible', t('Fishing rod: Bamboo Fishing Rod', 'Vara de pesca: Bamboo Fishing Rod'), t("Grancel — Helmut's Home, N. Block"), END,
       t('Talk to Noche upstairs.', 'Fale com a Noche no andar de cima.'), 0, [GRANCEL])
c.item('collectible', t('Recipes: Grancel shops (9)', 'Receitas: lojas de Grancel (9)'), t('Grancel'), END,
       t("Nonna's Crepe Shop (2) and Gaspard's Popcorn (1) in South Block; Sunnybell Inn (2) in South Block; Sorbet's Ice Cream (2) in East Block; Baral Coffee House (2) in West Block.",
         "Nonna's Crepe Shop (2) e Gaspard's Popcorn (1) no South Block; Sunnybell Inn (2) no South Block; Sorbet's Ice Cream (2) no East Block; Baral Coffee House (2) no West Block."),
       0, [GRANCEL])
c.item('collectible', t('Recipe: Dual-Layer Tempura', 'Receita: Dual-Layer Tempura'), t('Gurune Gate — cafeteria'), END,
       t('Reached from the east exit of Kirsche Avenue.', 'Acesso pela saída leste da Kirsche Avenue.'), 0, [GRANCEL])
c.item('collectible', t('Deer Medal'), t('Grancel — Edel Department Store accessories', 'Grancel — acessórios da Edel Department Store'), END,
       t('3rd of the 5 animal medals.', '3ª das 5 medalhas de animais.'), 0, [GRANCEL])
c.item('collectible', t('Kaldia Limestone Cave treasure chests (9)', 'Baús da Kaldia Limestone Cave (9)'), t('Kaldia Limestone Cave'), LEAVE_ZEISS,
       t('Includes one Kaldia Tunnel chest that only opens now.', 'Inclui um baú do Kaldia Tunnel que só abre agora.'), 0, [ZEISS])
c.item('collectible', t('Grancel Sewers W. Block treasure chests (6)', 'Baús do Grancel Sewers W. Block (6)'), t('Grancel Sewers — W. Block'), END,
       t('Southeast corner monster chest: sheep that reflect; dispel with Anti-Sept All. Two out-of-reach chests belong to a later block.',
         'Baú de monstros no canto sudeste: ovelhas que refletem; remova com Anti-Sept All. Dois baús fora de alcance pertencem a outro bloco, mais tarde.'),
       0, [GRANCEL])
c.item('collectible', t('Kirsche Avenue treasure chests (4)', 'Baús da Kirsche Avenue (4)'), t('Kirsche Avenue'), END,
       t('West and east paths. A breakable wall near the Erbe exit opens a water cave.',
         'Caminhos oeste e leste. Uma parede quebrável perto da saída para Erbe abre uma caverna com água.'),
       0, [GRANCEL])
c.item('collectible', t('Erbe Scenic Route treasure chests (6)', 'Baús da Erbe Scenic Route (6)'), t('Erbe Scenic Route'), VILLA_IN,
       t('Monster chest near the Earth Monument: burst the bone fish before they rage. A hidden sepith cave sits behind bushes at the Water Monument.',
         'Baú de monstros perto do Earth Monument: derrube os peixes-esqueleto antes que entrem em fúria. Uma caverna de sepith escondida fica atrás de arbustos no Water Monument.'),
       0, [GRANCEL])
c.item('collectible', t('Grancel Sewers E. & N. Blocks treasure chests (9)', 'Baús do Grancel Sewers E. e N. Blocks (9)'), t('Grancel Sewers — E. and N. Blocks'), END,
       t('Includes Bone-In Meat (eat it for the recipe). The North Block monster chest (four moles) is the hardest fight of the chapter; it can wait until the end.',
         'Inclui Bone-In Meat (coma para ganhar a receita). O baú de monstros do North Block (quatro toupeiras) é a luta mais difícil do capítulo; dá para deixar para o fim.'),
       1, [VILLA])

# ---------------------------------------------------------------- routes (append-only once published)
c.set_steps('sc-ch3-co-09', [
    t('Kaldia Tunnel, the newly opened path to the cave — All Sepith ×100', 'Kaldia Tunnel, o caminho recém-aberto até a caverna — All Sepith ×100'),
    t('In the cave, next fork north — Onyx Guard', 'Na caverna, próxima bifurcação ao norte — Onyx Guard'),
    t('North fork — Droplet of Defense', 'Bifurcação norte — Droplet of Defense'),
    t('South fork — Droplet of Life', 'Bifurcação sul — Droplet of Life'),
    t('At the next fork keep west — Teara Balm', 'Na próxima bifurcação siga a oeste — Teara Balm'),
    t('Back, north, then east — Droplet of Strength', 'Volte, norte e depois leste — Droplet of Strength'),
    t('West, following the bend southwest — Droplet of Spirit', 'Oeste, seguindo a curva a sudoeste — Droplet of Spirit'),
    t('Back north, first fork west — Droplet of Magic', 'De volta ao norte, primeira bifurcação a oeste — Droplet of Magic'),
    t('Back to the west — Thelas Balm ×2', 'De volta a oeste — Thelas Balm ×2'),
], source=GF1)
c.set_steps('sc-ch3-co-10', [
    t('First fork east — fishing bait (Dumpling, Pond Snail, Frog)', 'Primeira bifurcação a leste — iscas (Dumpling, Pond Snail, Frog)'),
    t('Next fork west, all the way down — Deathblow', 'Próxima bifurcação a oeste, até o fim — Deathblow'),
    t('Then left — Droplet of Strength', 'Depois à esquerda — Droplet of Strength'),
    t('Right path, the chest in the center — Edel Armor', 'Caminho da direita, o baú no centro — Edel Armor'),
    t('Southeast corner — monster chest: Silver Gauntlets (sheep that reflect)', 'Canto sudeste — baú de monstros: Silver Gauntlets (ovelhas que refletem)'),
    t('Near the end — Droplet of Defense', 'Perto do fim — Droplet of Defense'),
], source=GF2)
c.set_steps('sc-ch3-co-11', [
    t('West path, toward Sanktheim Gate — Droplet of Spirit', 'Caminho oeste, rumo ao Sanktheim Gate — Droplet of Spirit'),
    t('East at the fork, along the south wall — All Sepith ×250', 'Leste na bifurcação, junto à parede sul — All Sepith ×250'),
    t('A little further south on the same wall — U-Material ×10', 'Um pouco mais ao sul, na mesma parede — U-Material ×10'),
    t('East, then uphill to the north end — Silver Guard', 'Leste e depois subindo até o extremo norte — Silver Guard'),
], source=GF1)
c.set_steps('sc-ch3-co-12', [
    t('First fork west, behind the monument — Mute', 'Primeira bifurcação a oeste, atrás do monumento — Mute'),
    t('Main road west, north wall — Zeram Powder', 'Estrada principal a oeste, parede norte — Zeram Powder'),
    t('Next fork south — monster chest: Trickster (burst the bone fish early)', 'Próxima bifurcação ao sul — baú de monstros: Trickster (derrube os peixes-esqueleto cedo)'),
    t('Next fork — Holy Cloth', 'Próxima bifurcação — Holy Cloth'),
    t('Southwest fork, along the left wall — Athelas Balm', 'Bifurcação sudoeste, junto à parede esquerda — Athelas Balm'),
    t('Northeast fork — Droplet of Magic', 'Bifurcação nordeste — Droplet of Magic'),
    t('One guide also lists a chest by the east wall at the next fork (Droplet of Spirit)', 'Um dos guias também cita um baú junto à parede leste na próxima bifurcação (Droplet of Spirit)'),
], source=GF1)
c.set_steps('sc-ch3-co-13', [
    t('E. Block, around to the north side: room on the left — Athelas Balm', 'E. Block, contornando até o lado norte: sala à esquerda — Athelas Balm'),
    t('Room on the right — Golden Guard', 'Sala à direita — Golden Guard'),
    t('East hallway down to the next section, right at the split — Crystal Heels', 'Corredor leste até a próxima seção, à direita na divisão — Crystal Heels'),
    t('Fork to the left, at the end — Zeram Powder', 'Bifurcação à esquerda, no fim — Zeram Powder'),
    t('Back, north to the end of the hallway — Bone-In Meat', 'Volte, norte até o fim do corredor — Bone-In Meat'),
    t('N. Block (breakable wall), all the way south — Edel Girders', 'N. Block (parede quebrável), todo o caminho ao sul — Edel Girders'),
    t('West, then north to the end, behind the big crocodile — Confuse', 'Oeste e depois norte até o fim, atrás do crocodilo grande — Confuse'),
    t('At the end — monster chest: Proxy Puppet L (the hardest fight of the chapter)', 'No fim — baú de monstros: Proxy Puppet L (a luta mais difícil do capítulo)'),
    t('Upstairs, northern room, top-left side room — All Sepith ×250', 'No andar de cima, sala norte, sala lateral do canto superior esquerdo — All Sepith ×250'),
], source=GF2)

# ---------------------------------------------------------------- bosses
c.boss(t('Divine Pengu'), t('Kaldia Limestone Cave — northwest depths', 'Kaldia Limestone Cave — fundo a noroeste'),
       t('It is game over if the boy you are protecting falls, so clear the small pengus quickly. After Rage Boost it S-Breaks with a line attack (a Taunt can redirect it). Below half HP its dance confuses everyone (debuff immunity or Lily Necklace+) and calls pengus that take its damage: sweep them with area attacks. It survives one lethal hit.',
         'É game over se o garoto que você protege cair, então derrube rápido os pengus pequenos. Depois do Rage Boost ele usa um S-Break em linha (um Taunt pode desviar). Abaixo da metade do HP a dança dele confunde todos (imunidade a debuffs ou Lily Necklace+) e chama pengus que absorvem o dano: varra-os com ataques em área. Ele sobrevive a um golpe letal.'),
       related='sc-ch3-q-01', sources=[ZEISS])
c.boss(t('Giant Tree and Mad Trees', 'Giant Tree e Mad Trees'), t('Grancel Sewers — W. Block'),
       t('They cripple stats, delay you and heal from the damage they deal (the big one heals ten times as much). Use shields and debuff immunity, burn the Mad Trees first with fire arts; they are also vulnerable to Deathblow.',
         'Elas derrubam atributos, atrasam e se curam com o dano que causam (a grande cura dez vezes mais). Use escudos e imunidade a debuffs e queime primeiro as Mad Trees com arts de fogo; elas também são vulneráveis a Deathblow.'),
       related='sc-ch3-q-02', sources=[GRANCEL])
c.boss(t('Rhinoking'), t('Erbe Scenic Route — middle intersection', 'Erbe Scenic Route — cruzamento central'),
       t('A straight damage race. Buff up, add Foresight or debuff immunity, and expect a sleep-inducing scent at 75%, 50% and 25% HP.',
         'Uma disputa direta de dano. Faça os buffs, adicione Foresight ou imunidade a debuffs e espere um aroma que causa sono em 75%, 50% e 25% do HP.'),
       related='sc-ch3-q-03', sources=[GRANCEL])
c.boss(t('Master Cryon'), t('Grancel — Grand Arena'),
       t('Bring Freeze protection. The Cryon Flakes walk up and explode after a turn, so burst the Flakes and Bits right away with S-Breaks or a Burst, then deal with the master using your usual buffs.',
         'Leve proteção contra Freeze. Os Cryon Flakes se aproximam e explodem depois de um turno, então derrube Flakes e Bits na hora com S-Breaks ou Burst; depois cuide do mestre com os buffs de sempre.'),
       related='sc-ch3-q-04', sources=[VILLA])
c.boss(t('Special Ops machine', 'Máquina das Special Ops'), t('Grancel Sewers — N. Block'),
       t('An easy one: very vulnerable to Seal, and debuff immunity plus stat buffs cover its single real attack.',
         'Uma luta fácil: muito vulnerável a Seal, e imunidade a debuffs com buffs de atributos cobrem o único ataque de verdade dela.'),
       sources=[VILLA])
c.boss(t('King Pengu'), t('Grancel Sewers — side room by the E. Block entrance', 'Grancel Sewers — sala lateral na entrada do E. Block'),
       t('Bring Confuse protection. Sweep the small pengus with area attacks; if they all fall, it spends a turn reviving them at 30% HP. Rage Boost below 55% and 35% HP, and it survives one lethal hit.',
         'Leve proteção contra Confuse. Varra os pengus pequenos com ataques em área; se todos caírem, ele gasta um turno revivendo-os com 30% do HP. Rage Boost abaixo de 55% e de 35% do HP, e ele sobrevive a um golpe letal.'),
       related='sc-ch3-q-06', sources=[GURUNE])
c.boss(t('Hurricane Velg'), t('Kirsche Avenue'),
       t('Most attacks Seal, and Feather Shower lowers every stat. Sylpharion (debuff immunity and arts reflect) handles it, then Zodiac and Foresight. Try to burst it before it reaches half HP.',
         'A maioria dos ataques causa Seal, e o Feather Shower reduz todos os atributos. O Sylpharion (imunidade a debuffs e reflexo de arts) resolve; depois use Zodiac e Foresight. Tente derrubá-lo antes da metade do HP.'),
       related='sc-ch3-q-07', sources=[GURUNE])
c.boss(t('Battles at the port warehouse', 'Batalhas no depósito do porto'), t('Grancel — port district', 'Grancel — distrito do porto'),
       t('Several fights back to back with no rest, so pace EP and CP. In the last one, clear the summoned reinforcements before they close in, then chip the leader down; she survives one lethal hit, so keep an S-Break for right after.',
         'Várias lutas seguidas sem descanso, então dose EP e CP. Na última, derrube os reforços invocados antes que se aproximem e depois desgaste a líder; ela sobrevive a um golpe letal, então guarde um S-Break para logo depois.'),
       sources=[GURUNE])

# ---------------------------------------------------------------- fishing
CRAB, TROUT, EEL = 'sc-ch1-fi-01', 'sc-ch1-fi-06', 'sc-ch1-fi-08'
KASAGIN, YAMANY, TIGER, LCARP, VBASS, RTROUT, CARP, ROCK, SALMON, SNAKE = (f'sc-ch2-fi-{n:02d}' for n in range(1, 11))
PEARL = c.fish('Pearlglass', sources=[VILLA])
c.spot(VBASS, 'B', t('Kaldia Limestone Cave — entrance', 'Kaldia Limestone Cave — entrada'))
c.spot(RTROUT, 'B', t('Kaldia Limestone Cave — depths (after the quest); Grancel port and North Block', 'Kaldia Limestone Cave — fundo (depois da quest); porto e North Block de Grancel'))
c.spot(CRAB, 'A', t('Erbe Scenic Route — Romal Pond'))
c.spot(KASAGIN, 'A', t('Grancel Sewers — W. Block and E. Block entrance', 'Grancel Sewers — W. Block e entrada do E. Block'))
c.spot(YAMANY, 'A', t('Grancel Sewers — E. Block', 'Grancel Sewers — E. Block'))
c.spot(TIGER, 'A', t('Grancel Sewers — E. Block, near the N. Block', 'Grancel Sewers — E. Block, perto do N. Block'))
c.spot(LCARP, 'B', t('Grancel Sewers'))
c.spot(CARP, 'A', t('Grancel Sewers E. Block near the N. Block; Erbe Scenic Route — Romal Pond', 'Grancel Sewers E. Block perto do N. Block; Erbe Scenic Route — Romal Pond'))
c.spot(EEL, 'A', t('Erbe Scenic Route — Romal Pond'))
c.spot(ROCK, 'B', t('Grancel Sewers; Erbe Scenic Route — Romal Pond'))
c.spot(TROUT, 'B', t('Grancel — North Block'))
c.spot(SALMON, 'A', t('Grancel — port (the only Rank A spot in the capital; the port closes later, so fish it while you can)', 'Grancel — porto (único Rank A da capital; o porto fecha mais tarde, então pesque enquanto der)'))
c.spot(SNAKE, 'B', t('Grancel — port', 'Grancel — porto'))
c.spot(PEARL, 'C', t('Erbe Royal Villa — front courtyard', 'Erbe Royal Villa — pátio da frente'))

# ---------------------------------------------------------------- recipes
c.recipe('Sweet Crepe', t("Nonna's Crepe Shop, Grancel South Block"), sources=[GRANCEL])
c.recipe('Mystery Crepe', t("Nonna's Crepe Shop, Grancel South Block"), sources=[GRANCEL])
c.recipe('Agile Popcorn', t("Gaspard's Popcorn Shop, Grancel South Block"), sources=[GRANCEL])
c.recipe('Homemade Faux Pie', t('Sunnybell Inn, Grancel South Block'), sources=[GRANCEL])
c.recipe('Refined Carapace', t('Sunnybell Inn, Grancel South Block'), sources=[GRANCEL])
c.recipe('Sunshine Ice Cream', t("Sorbet's Ice Cream Shop, Grancel East Block"), sources=[GRANCEL])
c.recipe('Moonlight Ice Cream', t("Sorbet's Ice Cream Shop, Grancel East Block"), sources=[GRANCEL])
c.recipe("Sandman's Demise", t('Baral Coffee House, Grancel West Block'), sources=[GRANCEL])
c.recipe('Curry of Dreams', t('Baral Coffee House, Grancel West Block'), sources=[GRANCEL])
c.recipe('Dual-Layer Tempura', t('Gurune Gate cafeteria', 'Cafeteria do Gurune Gate'), sources=[GRANCEL])
c.recipe('Bone-In Meat', t('Treasure chest in Grancel Sewers N. Block', 'Baú no Grancel Sewers N. Block'), sources=[VILLA])
c.recipe('White Chiffon Cake', t('Have Kloe cook Fruit Kingdom', 'A Kloe cozinha Fruit Kingdom'), 'customized', sources=[ZEISS])
c.recipe('Omelet Pilaf', t('Have Tita cook Passionate Egg Roll', 'A Tita cozinha Passionate Egg Roll'), 'customized', sources=[ZEISS])
c.recipe('Red Wine Curry', t('Have Olivier cook Curry of Dreams', 'O Olivier cozinha Curry of Dreams'), 'customized', sources=[GURUNE])

c.write()
