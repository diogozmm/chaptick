# Chapter 3 — rewritten in our own words from the Neoseeker walkthrough (facts only).
# Once published, never reorder or remove items: ids are derived from order.
from lib import Chapter, src, t

ZEISS = src('Chapter 3 - Zeiss')
GRANCEL = src('Chapter 3 - Grancel')
VILLA = src('Chapter 3 - Erbe Royal Villa')
GURUNE = src('Chapter 3 - Gurune Gate')

c = Chapter(3, 'Chapter 3', 'Capítulo 3')
LEAVE_ZEISS = c.cp('Boarding the airliner from Zeiss to Grancel', 'Embarcar no airliner de Zeiss para Grancel')
VISITS = c.cp('Finishing the round of visits in the capital (the time of day changes)',
              'Terminar a rodada de visitas na capital (o horário do dia muda)')
END = c.cp('Boarding the airliner at the end of Chapter 3', 'Embarcar no airliner no fim do Capítulo 3')

# Quests
c.item('quest', t('Guest Gone Missing'), t('Zeiss — Zahnrad Hotel'), LEAVE_ZEISS,
       t('+5 BP. Leads into Kaldia Limestone Cave, off Kaldia Tunnel. Bring Confuse and Seal protection, and keep the person you escort alive in the final fight.',
         '+5 BP. Leva à Kaldia Limestone Cave, a partir do Kaldia Tunnel. Leve proteção contra Confuse e Seal, e mantenha vivo quem você escolta na luta final.'),
       0, [ZEISS])
c.item('quest', t('Sewer Monster'), t('Grancel Sewers — W. Block, far end', 'Grancel Sewers — W. Block, no fim'), END,
       t('+4 BP. Trees that cripple stats and heal from damage: shields and debuff immunity; fire arts on the small ones first.',
         '+4 BP. Árvores que derrubam atributos e se curam causando dano: escudos e imunidade a debuffs; arts de fogo nas menores primeiro.'),
       0, [GRANCEL])
c.item('quest', t('Erbe Scenic Route Monster'), t('Erbe Scenic Route — middle intersection', 'Erbe Scenic Route — cruzamento central'), END,
       t('+4 BP. Blocks the way to the villa. Straightforward: buff up and burst when stunned.',
         '+4 BP. Bloqueia o caminho para a mansão. Direto ao ponto: faça buffs e ataque forte quando atordoar.'),
       0, [GRANCEL])
c.item('quest', t('Exhibit Enigma'), t('Grancel — History Museum, 2F', 'Grancel — History Museum, 2º andar'), VISITS,
       t("+4 BP. Cards: grandfather clock upstairs in General Morgan's house (next to the cathedral); the South Block fountain; Calvard Embassy, right room, The Doll Knight vol. 15; then the Grand Arena through the southern waiting room. Bring Freeze protection for the fight.",
         '+4 BP. Cartões: relógio de pêndulo no andar de cima da casa do General Morgan (ao lado da catedral); a fonte do South Block; embaixada de Calvard, sala à direita, The Doll Knight vol. 15; por fim, a Grand Arena pela sala de espera sul. Leve proteção contra Freeze para a luta.'),
       1, [VILLA])
c.item('quest', t('Sewer Monster 2'), t('Grancel Sewers — E. and N. Blocks', 'Grancel Sewers — E. e N. Blocks'), END,
       t('+4 BP. The North Block entrance is a breakable wall at the end of the East Block.',
         '+4 BP. A entrada do North Block é uma parede quebrável no fim do East Block.'),
       1, [VILLA])
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
c.item('collectible', t('Erbe Scenic Route treasure chests (6)', 'Baús da Erbe Scenic Route (6)'), t('Erbe Scenic Route'), END,
       t('Monster chest near the Earth Monument: burst the bone fish before they rage. A hidden sepith cave sits behind bushes at the Water Monument.',
         'Baú de monstros perto do Earth Monument: derrube os peixes-esqueleto antes que entrem em fúria. Uma caverna de sepith escondida fica atrás de arbustos no Water Monument.'),
       0, [GRANCEL])
c.item('collectible', t('Grancel Sewers E. & N. Blocks treasure chests (9)', 'Baús do Grancel Sewers E. e N. Blocks (9)'), t('Grancel Sewers — E. and N. Blocks'), END,
       t('Includes Bone-In Meat (eat it for the recipe). The North Block monster chest (four moles) is the hardest fight of the chapter; it can wait until the end.',
         'Inclui Bone-In Meat (coma para ganhar a receita). O baú de monstros do North Block (quatro toupeiras) é a luta mais difícil do capítulo; dá para deixar para o fim.'),
       1, [VILLA])

c.write()
