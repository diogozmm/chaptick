# Chapter 4 — rewritten in our own words from the Neoseeker walkthrough (facts only).
# The source guide stops at the night in Rolent, so this chapter is partial: append later
# items at the end, never reorder (ids are derived from order).
from lib import Chapter, gf, src, t

FORT = src('Chapter 4 - Sky Pirate Stronghold')
ROLENT = src('Chapter 4 - Rolent')
GF_OPEN = gf('Chapter 4 - Opening Act')
GF1 = gf('Chapter 4 - Day 1')
GF2 = gf('Chapter 4 - Day 2')
GF_CH5 = gf('Chapter 5 - Day 1')

c = Chapter(4, 'Chapter 4', 'Capítulo 4')
STRONGHOLD = c.cp('Crossing the plank at the top of the first area', 'Atravessar a prancha no topo da primeira área')
NIGHT = c.cp('Returning to Rolent from Esmelas Tower (night falls)', 'Voltar para Rolent vindo da Esmelas Tower (a noite cai)')
NIGHT_END = c.cp('Ending the night in Rolent', 'Encerrar a noite em Rolent')
FINALE = c.cp('Following the red marker into the back of Mistwald on the second day',
              'Seguir o marcador vermelho até o fundo de Mistwald no segundo dia')

# Quests
c.item('quest', t('Betrothal Band Bandit'), t('Rolent Chapel'), NIGHT,
       t('+4 BP. Talk to Armand and Ellie. The ring is on the rooftop of Esmelas Tower, by the broken pillar on the left.',
         '+4 BP. Fale com Armand e Ellie. O anel está no terraço da Esmelas Tower, junto ao pilar quebrado à esquerda.'),
       0, [ROLENT])
c.item('quest', t('Fishing Spot Scout'), t('Gurune Gate — talk to Pecheur', 'Gurune Gate — fale com o Pecheur'), 'sc-ch5-cp-01',
       t("3 +2 BP. Start it first: only catches made after accepting count. Catch any fish at each of Rolent's 7 spots (Elize Highway, Bright Family House, Malga Trail water cave, Rolent Sewers, Milch Main Road, Verte Bridge, and one that opens at the start of Chapter 5), then report before leaving Rolent.",
         '3 +2 BP. Aceite antes: só contam as pescas feitas depois disso. Pesque qualquer peixe em cada um dos 7 pesqueiros de Rolent (Elize Highway, casa da família Bright, caverna com água da Malga Trail, Rolent Sewers, Milch Main Road, Verte Bridge e um que abre no início do Capítulo 5) e entregue antes de sair de Rolent.'),
       0, [ROLENT, GF1, GF_CH5])
c.item('quest', t('Elize Hwy Monster'), t('Elize Highway — near Gurune Gate', 'Elize Highway — perto do Gurune Gate'), NIGHT,
       t('+4 BP. Petrify, delay and stat-down attacks: equip protection and use arts reflect.',
         '+4 BP. Ataques de Petrify, atraso e redução de atributos: equipe proteção e use reflexo de arts.'),
       0, [ROLENT])
c.item('quest', t('Milch Monster'), t('Milch Main Road — west end', 'Milch Main Road — extremo oeste'), NIGHT,
       t('+4 BP. It buffs itself constantly: dispel at 2–3 stacks and bring Freeze protection.',
         '+4 BP. Ele se fortalece o tempo todo: remova os buffs com 2 ou 3 acúmulos e leve proteção contra Freeze.'),
       0, [ROLENT])
c.item('quest', t('Find That Feline'), t('Rolent — Hotel Rolent, 1F', 'Rolent — Hotel Rolent, 1º andar'), NIGHT_END,
       t('+4 BP. Only during the night. Skyler by the landing port warehouse → Captain Petrov in Abend Bar → Quint in the orbal factory → Zosimov by the tree at the port entrance → Fabree on the deck → bottom level of the airliner.',
         '+4 BP. Só durante a noite. Skyler no depósito do porto → Captain Petrov no Abend Bar → Quint na fábrica orbal → Zosimov na árvore da entrada do porto → Fabree no deck → nível mais baixo do airliner.'),
       1, [ROLENT])

# Missables
c.item('missable', t("Bonus BP: Aina's two questions", 'BP bônus: as duas perguntas da Aina'), t('Rolent — Bracer Guild'), NIGHT_END,
       t('+6 BP. When you report the night investigation, pick the 2nd option, then the 3rd.',
         '+6 BP. Ao relatar a investigação da noite, escolha a 2ª opção e depois a 3ª.'),
       1, [ROLENT])

# Collectibles
c.item('collectible', t('Stronghold treasure chests (13)', 'Baús da fortaleza (13)'), t('First area of the chapter', 'Primeira área do capítulo'), STRONGHOLD,
       t('One-time visit. Check the first room on the left on 2F and circle the 3F before going up.',
         'Visita única. Olhe a primeira sala à esquerda no 2F e dê a volta no 3F antes de subir.'),
       1, [FORT])
c.item('collectible', t('Battle Notes: stronghold (5)', 'Battle Notes: fortaleza (5)'), t('First area of the chapter', 'Primeira área do capítulo'), STRONGHOLD,
       t('Fight every enemy type you meet on the way up; you cannot come back. Sources disagree on whether these entries count toward the enemy trophy.',
         'Enfrente todos os tipos de inimigo no caminho para cima; não dá para voltar. As fontes divergem sobre essas entradas contarem para o troféu de inimigos.'),
       1, [FORT, GF_OPEN])
c.item('collectible', t('Liberl News Issue 6'), t("Rolent — Rinon's General Goods"), NIGHT_END,
       t('Sold at the general store.', 'Vendido no armazém.'), 0, [ROLENT])
c.item('collectible', t('Gambler Jack — Vol. 6'), t('Rolent — apartment next to Abend Bar, 2F', 'Rolent — apartamento ao lado do Abend Bar, 2º andar'), NIGHT_END,
       t('Talk to Serra.', 'Fale com a Serra.'), 0, [ROLENT])
c.item('collectible', t('Recipes: Abend Bar (4)', 'Receitas: Abend Bar (4)'), t('Rolent — Abend Bar'), NIGHT_END,
       t('Silken Soup, Spring Spiral Noodles, Strawberry Supreme Crepe and Three-Egg Rice Porridge.',
         'Silken Soup, Spring Spiral Noodles, Strawberry Supreme Crepe e Three-Egg Rice Porridge.'),
       0, [ROLENT])
c.item('collectible', t('Bear Medal'), t("Rolent — Rinon's General Goods"), NIGHT_END,
       t('4th of the 5 animal medals.', '4ª das 5 medalhas de animais.'), 0, [ROLENT])
c.item('collectible', t('Rolent Sewers treasure chests (2)', 'Baús do Rolent Sewers (2)'), t('Rolent Sewers'), NIGHT,
       t('Enter through the grate behind the chapel.', 'Entre pela grade atrás da capela.'), 0, [ROLENT])
c.item('collectible', t('Elize Highway treasure chests (5)', 'Baús da Elize Highway (5)'), t('Elize Highway'), NIGHT,
       t('Spread along the highway south of Rolent.', 'Espalhados pela estrada ao sul de Rolent.'), 0, [ROLENT])
c.item('collectible', t('Mistwald treasure chests (7)', 'Baús de Mistwald (7)'), t('Mistwald'), NIGHT,
       t('Includes a monster chest with Death Speculars and Picorns.', 'Inclui um baú de monstros com Death Speculars e Picorns.'), 0, [ROLENT])
c.item('collectible', t('Milch Main Road treasure chests (8)', 'Baús da Milch Main Road (8)'), t('Milch Main Road'), NIGHT,
       t('Large open map with few landmarks; includes a monster chest with rhino beetles.',
         'Mapa grande e aberto, com poucos pontos de referência; inclui um baú de monstros com besouros-rinoceronte.'),
       0, [ROLENT])
c.item('collectible', t('Malga Trail treasure chests (8)', 'Baús da Malga Trail (8)'), t('Malga Trail'), NIGHT,
       t('Visit both Esmelas Tower (west) and Malga Mine (north) to unlock fast travel. A breakable wall on the way to the tower hides a cave.',
         'Visite a Esmelas Tower (oeste) e a Malga Mine (norte) para liberar a viagem rápida. Uma parede quebrável a caminho da torre esconde uma caverna.'),
       0, [ROLENT])
c.item('collectible', t('Esmelas Tower treasure chests (11)', 'Baús da Esmelas Tower (11)'), t('Esmelas Tower'), NIGHT,
       t('Includes Maelstrom Soup (eat it for the recipe) and a monster chest with Wind Trappers.',
         'Inclui Maelstrom Soup (coma para ganhar a receita) e um baú de monstros com Wind Trappers.'),
       0, [ROLENT])

# ---------------------------------------------------------------- Day 2 (from GameFAQs; the Neoseeker guide stopped before it)
c.item('quest', t('Esmelas Tower Monster'), t('Outside Esmelas Tower', 'Do lado de fora da Esmelas Tower'), FINALE,
       t('+4 BP. Medium deadline. Its defense is so high that physical hits do nothing: bring water arts and orbal-gun users, spread the party, and resist Seal, Mute and Blind.',
         '+4 BP. Prazo médio. A defesa é tão alta que golpes físicos não causam dano: leve arts de água e quem usa arma orbal, espalhe a equipe e resista a Seal, Mute e Blind.'),
       0, [GF2])
c.item('quest', t('Milch Monster 2'), t('Milch Main Road'), FINALE,
       t('+4 BP. Medium deadline. Like the Mistwald monster chest: bring Confuse and Deathblow protection; its allies absorb water and wind but are weak to earth and fire.',
         '+4 BP. Prazo médio. Parecido com o baú de monstros de Mistwald: leve proteção contra Confuse e Deathblow; os aliados absorvem água e vento, mas são fracos contra terra e fogo.'),
       0, [GF2])
c.item('missable', t('Bonus BP: the maze in the mist', 'BP bônus: o labirinto na névoa'), t('Mistwald — beyond the red marker', 'Mistwald — além do marcador vermelho'), FINALE,
       t('+3 BP when you reach the end. Follow the high bell sound and the flowers by each correct exit; lowering the music volume helps.',
         '+3 BP ao chegar ao fim. Siga o som agudo de sino e as flores junto a cada saída certa; baixar o volume da música ajuda.'),
       1, [GF2])
c.item('collectible', t('Chest in the maze (Breeze)', 'Baú no labirinto (Breeze)'), t('Mistwald — beyond the red marker', 'Mistwald — além do marcador vermelho'), FINALE,
       t('Where two exits both have flowers, head toward the chest icon on the minimap.',
         'Onde duas saídas têm flores, vá na direção do ícone de baú no minimapa.'),
       1, [GF2])

# ---------------------------------------------------------------- bosses
c.boss(t('Stronghold commander', 'Comandante da fortaleza'), t('First area of the chapter — top', 'Primeira área do capítulo — topo'),
       t('A gentle fight. Open with Earth Guard and Sylphen Wing, heal as needed and steal his AT bonuses with an Orbal Bomb. In Rage Boost he removes your buffs and S-Breaks: reapply the shield and keep going.',
         'Uma luta tranquila. Comece com Earth Guard e Sylphen Wing, cure quando precisar e roube os bônus de AT dele com uma Orbal Bomb. No Rage Boost ele remove seus buffs e usa o S-Break: reaplique o escudo e siga.'),
       sources=[FORT])
c.boss(t('Master Wisdom ×3'), t('Elize Highway — near Gurune Gate', 'Elize Highway — perto do Gurune Gate'),
       t('Force of Nature delays, lowers all stats and can Petrify; their hits also heal them. Most of their damage is magic, so Sylpharion (arts reflect and debuff immunity) does a lot of the work. They spam Force of Nature in Rage Boost.',
         'O Force of Nature atrasa, reduz todos os atributos e pode causar Petrify; os golpes deles também os curam. A maior parte do dano é mágico, então o Sylpharion (reflexo de arts e imunidade a debuffs) faz boa parte do trabalho. No Rage Boost eles repetem o Force of Nature.'),
       related='sc-ch4-q-03', sources=[ROLENT])
c.boss(t('Big the Yeti'), t('Milch Main Road — west end', 'Milch Main Road — extremo oeste'),
       t('It keeps stacking Bulk Up, which also clears its debuffs. Dispel at two or three stacks or after a Rage Boost (below two thirds and one third HP), and bring Freeze protection.',
         'Ele acumula Bulk Up o tempo todo, o que também limpa os debuffs dele. Remova os buffs com dois ou três acúmulos ou depois de um Rage Boost (abaixo de dois terços e de um terço do HP), e leve proteção contra Freeze.'),
       related='sc-ch4-q-04', sources=[ROLENT])

# ---------------------------------------------------------------- fishing
CRAB, TROUT = 'sc-ch1-fi-01', 'sc-ch1-fi-06'
KASAGIN, YAMANY, TIGER, LCARP, VBASS, RTROUT, CARP, ROCK, SALMON, SNAKE = (f'sc-ch2-fi-{n:02d}' for n in range(1, 11))
PEARL = 'sc-ch3-fi-01'
GARVELZE = c.fish('Garvelze', sources=[ROLENT])
c.spot(GARVELZE, 'B', t('Rolent Sewers'))
c.spot(CRAB, 'A', t('Rolent Sewers'))
c.spot(KASAGIN, 'A', t('Rolent Sewers; Bright Family House pond', 'Rolent Sewers; lago da casa da família Bright'))
c.spot(LCARP, 'A', t('Rolent Sewers; Milch Main Road — northeastern pond', 'Rolent Sewers; Milch Main Road — lago a nordeste'))
c.spot(CARP, 'A', t('Rolent Sewers, Bright Family House pond, Elize Highway stream, Verte Bridge', 'Rolent Sewers, lago da casa Bright, riacho da Elize Highway, Verte Bridge'))
c.spot(ROCK, 'A', t('Bright Family House pond; Verte Bridge', 'Lago da casa da família Bright; Verte Bridge'))
c.spot(VBASS, 'A', t('Elize Highway — stream', 'Elize Highway — riacho'))
c.spot(YAMANY, 'A', t('Verte Bridge'))
c.spot(TIGER, 'A', t('Verte Bridge'))
c.spot(TROUT, 'B', t('Elize Highway stream; Verte Bridge', 'Riacho da Elize Highway; Verte Bridge'))
c.spot(RTROUT, 'B', t('Verte Bridge'))
c.spot(SNAKE, 'B', t('Elize Highway stream; Milch Main Road pond', 'Riacho da Elize Highway; lago da Milch Main Road'))
c.spot(PEARL, 'C', t('Elize Highway stream; Milch Main Road pond', 'Riacho da Elize Highway; lago da Milch Main Road'))

# ---------------------------------------------------------------- recipes
c.recipe('Silken Soup', t('Abend Bar, Rolent'), sources=[ROLENT])
c.recipe('Spring Spiral Noodles', t('Abend Bar, Rolent'), sources=[ROLENT])
c.recipe('Strawberry Supreme Crepe', t('Abend Bar, Rolent'), sources=[ROLENT])
c.recipe('Three-Egg Rice Porridge', t('Abend Bar, Rolent'), sources=[ROLENT])
c.recipe('Maelstrom Soup', t('Treasure chest in Esmelas Tower', 'Baú na Esmelas Tower'), sources=[ROLENT])

c.boss(t('Guilder Quake'), t('Outside Esmelas Tower', 'Do lado de fora da Esmelas Tower'),
       t('Physical damage does nothing; use water arts and keep characters apart so its tail sweep hits only one. Its field-wide move inflicts delay, Seal, Mute and Blind, so resist those.',
         'Dano físico não funciona; use arts de água e mantenha os personagens separados para o golpe de cauda acertar só um. O ataque em todo o campo causa atraso, Seal, Mute e Blind, então resista a eles.'),
       related='sc-ch4-q-06', sources=[GF2])
c.boss(t('Death Specular+'), t('Milch Main Road'),
       t('Comes with four Picorn+ (absorb water and wind, weak to earth and fire). Misfortune puts a random ailment on every action, so keep Weiss Aura or Sylphen Wing ready, plus Confuse and Deathblow protection.',
         'Vem com quatro Picorn+ (absorvem água e vento, fracos contra terra e fogo). O Misfortune aplica um efeito aleatório a cada ação, então tenha Weiss Aura ou Sylphen Wing à mão, além de proteção contra Confuse e Deathblow.'),
       related='sc-ch4-q-07', sources=[GF2])
c.boss(t('Guardians at the heart of the mist', 'Guardiões no coração da névoa'), t('Mistwald — the end of the maze', 'Mistwald — o fim do labirinto'),
       t('Two bosses with opposite gimmicks: one only takes physical damage and can grab a party member, the other only takes arts and puts everyone to sleep. Bring Sleep, Blind, Seal and Mute protection, clear the summoned flowers with an area art, beat the grabber first with physical attacks, then the other with arts.',
         'Dois bosses com truques opostos: um só recebe dano físico e pode agarrar alguém da equipe; o outro só recebe arts e faz todos dormirem. Leve proteção contra Sleep, Blind, Seal e Mute, limpe as flores invocadas com uma art em área, derrube primeiro o que agarra com ataques físicos e depois o outro com arts.'),
       sources=[GF2])

c.write()
