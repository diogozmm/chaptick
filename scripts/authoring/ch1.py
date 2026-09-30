# Chapter 1 — rewritten in our own words from the Neoseeker walkthrough (facts only).
# Once published, never reorder or remove items here: ids are derived from order and saved
# progress points at them. Append new items at the end of each type.
from lib import Chapter, src, t

RUAN = src('Chapter 1 - Ruan')
MERCIA = src('Chapter 1 - Mercia Orphanage')
CH2_RUAN = src('Chapter 2 - Ruan')
LEAVE_RUAN = 'sc-ch2-cp-01'  # boarding the airliner out of Ruan, early in Chapter 2

c = Chapter(1, 'Chapter 1', 'Capítulo 1')
BOARD = c.cp('Boarding the airship in Grancel at the start of the chapter',
             'Embarcar no airship em Grancel, no início do capítulo')
ACADEMY = c.cp('Passing through the gate at the end of Vista Forest Road',
               'Atravessar o portão no fim da Vista Forest Road')
END = c.cp('The last event marker of Chapter 1', 'O último marcador de evento do Capítulo 1')

# Quests
c.item('quest', t('Seaside Way Monster'), t('Gull Seaside Way — north beach'), LEAVE_RUAN,
       t('+3 BP. The monster waits at the entrance of the north beach, by the wall. Easier once a third party member joins; fire arts work well.',
         '+3 BP. O monstro fica na entrada da praia norte, junto ao muro. Fica mais fácil com um terceiro membro na equipe; arts de fogo funcionam bem.'),
       0, [RUAN])
c.item('quest', t('Ingredient Inquiry'), t('Manoria Village — The White Magnolia, upstairs', 'Manoria Village — The White Magnolia, andar de cima'), LEAVE_RUAN,
       t('2 +2 BP. Bring all 6 ingredients missing from his list for the bonus: Monster Bird Egg and Monster Tender (Roadrun), Monster Bone (Tatuunon), Monster Fang (Gourd Boar), Monster Horn (Flying Shrimp), Monster Roe (Mars Gel or Sharkagator).',
         '2 +2 BP. Entregue os 6 ingredientes que faltam na lista dele para ganhar o bônus: Monster Bird Egg e Monster Tender (Roadrun), Monster Bone (Tatuunon), Monster Fang (Gourd Boar), Monster Horn (Flying Shrimp), Monster Roe (Mars Gel ou Sharkagator).'),
       0, [RUAN, CH2_RUAN])
c.item('quest', t('Vista Forest Rd Monster'), t('Vista Forest Road — east end', 'Vista Forest Road — extremo leste'), LEAVE_RUAN,
       t('+3 BP. Nasty status effects: bring Confuse protection and take out the two smaller foes first.',
         '+3 BP. Muitos efeitos negativos: leve proteção contra Confuse e derrube os dois inimigos menores primeiro.'),
       0, [RUAN])
c.item('quest', t('Sapphirl Snapshot'), t('Sapphirl Tower — rooftop', 'Sapphirl Tower — terraço'), ACADEMY,
       t('2 +2 BP. Take it from Santos at Hotel Blanche. On the rooftop, step a little forward and try the camera until Estelle says the spot might be perfect, then shoot.',
         '2 +2 BP. Pegue com o Santos no Hotel Blanche. No terraço, avance um pouco e teste a câmera até a Estelle dizer que o lugar pode ser perfeito; então tire a foto.'),
       0, [RUAN])
c.item('quest', t('Sunday Scholar'), t('Ruan Chapel'), ACADEMY,
       t('3 +2 BP. Answer every question right for the bonus. Answers in order: 2nd, 1st, 3rd, 3rd, 2nd, 2nd, 3rd, 2nd, 2nd, 3rd.',
         '3 +2 BP. Acerte todas as perguntas para ganhar o bônus. Respostas em ordem: 2ª, 1ª, 3ª, 3ª, 2ª, 2ª, 3ª, 2ª, 2ª, 3ª.'),
       0, [MERCIA])
c.item('quest', t('Drawbridge Defect'), t('Ruan — Aqua Rossa Bar, 2F', 'Ruan — Aqua Rossa Bar, 2º andar'), ACADEMY,
       t('2 +1 BP. After talking to every tourist by the drawbridge, pick the 2nd option in the scene that follows. Ends with a tough fight.',
         '2 +1 BP. Depois de falar com todos os turistas perto da ponte levadiça, escolha a 2ª opção na cena seguinte. Termina com uma luta difícil.'),
       0, [MERCIA])
c.item('quest', t('Krone Pass Monster'), t('Krone Trail area', 'Região da Krone Trail'), LEAVE_RUAN,
       t('+3 BP. Poison-heavy fight: shields and speed buffs keep it simple.',
         '+3 BP. Luta cheia de veneno: escudos e buffs de velocidade simplificam.'),
       0, [MERCIA])
c.item('quest', t('Aina Cswy Monster'), t('Aina Causeway'), LEAVE_RUAN,
       t('+3 BP. Three wolves that power up when one falls: try to finish them together.',
         '+3 BP. Três lobos que ficam mais fortes quando um cai: tente derrotá-los juntos.'),
       0, [MERCIA])
c.item('hidden_quest', t('Lighthouse Learning'), t('Varenne Lighthouse — top floor', 'Varenne Lighthouse — último andar'), LEAVE_RUAN,
       t('2 +1 BP. Not on the board. Talk to Vogt and pick the 1st option. Order: both dials LOW, power ON, pressure MID, stabilizer MID, pressure HIGH, stabilizer HIGH, then the machine on the far left. Before finishing, pick the 2nd option for the bonus.',
         '2 +1 BP. Não aparece no quadro. Fale com o Vogt e escolha a 1ª opção. Ordem: os dois controles em LOW, energia ON, pressão MID, estabilizador MID, pressão HIGH, estabilizador HIGH e, por fim, a máquina mais à esquerda. Antes de concluir, escolha a 2ª opção para o bônus.'),
       0, [RUAN])

# Missables
c.item('missable', t('Bonus BP: question at the bridge', 'BP bônus: pergunta na ponte'), t('Ruan — Langland Bridge'), ACADEMY,
       t('+3 BP. When asked during the scene at the bridge, pick the 2nd option.',
         '+3 BP. Quando perguntarem durante a cena na ponte, escolha a 2ª opção.'),
       1, [MERCIA])

# Collectibles
c.item('collectible', t('Liberl News Issue 2'), t('Grancel — Landing Port Waiting Room', 'Grancel — sala de espera do porto'), BOARD,
       t('Buy it from Filder before boarding. You cannot explore Grancel at this point.',
         'Compre com o Filder antes de embarcar. Não dá para explorar Grancel neste momento.'),
       0, [RUAN])
c.item('collectible', t('Gambler Jack — Vol. 2'), t('Ruan — Lavantar Bar & Casino, 2F', 'Ruan — Lavantar Bar & Casino, 2º andar'), LEAVE_RUAN,
       t('Exchange 200 medals. You can buy medals with mira if the games are not going well.',
         'Troque por 200 medalhas. Dá para comprar medalhas com mira se os jogos não estiverem ajudando.'),
       0, [RUAN])
c.item('collectible', t('Fishing rod: Marine Star', 'Vara de pesca: Marine Star'), t('Ruan — Lavantar Bar & Casino, 2F', 'Ruan — Lavantar Bar & Casino, 2º andar'), LEAVE_RUAN,
       t('Exchange 100 medals.', 'Troque por 100 medalhas.'), 0, [RUAN])
c.item('collectible', t('Recipes: Ruan (3)', 'Receitas: Ruan (3)'), t('Ruan'), LEAVE_RUAN,
       t('Azelia Kiss at Lavantar Bar & Casino; Roasted Fish Belly and Sea Breeze Soup at Aqua Rossa Bar. Eat each dish to learn it.',
         'Azelia Kiss no Lavantar Bar & Casino; Roasted Fish Belly e Sea Breeze Soup no Aqua Rossa Bar. Coma cada prato para aprender.'),
       0, [RUAN])
c.item('collectible', t('Recipes: Manoria Village (2)', 'Receitas: Manoria Village (2)'), t('Manoria Village — The White Magnolia'), LEAVE_RUAN,
       t('Ocean Froth and Seaside Paradise, sold by Rex.', 'Ocean Froth e Seaside Paradise, vendidos pelo Rex.'), 0, [RUAN])
c.item('collectible', t("Recipe: Minnow's Keep", "Receita: Minnow's Keep"), t('Air-Letten — cafeteria', 'Air-Letten — cafeteria'), LEAVE_RUAN,
       t('Buy it when the story takes you to Air-Letten.', 'Compre quando a história levar você a Air-Letten.'), 0, [MERCIA])
c.item('collectible', t('Recipes: academy cafeteria (3)', 'Receitas: cafeteria da academia (3)'), t('Jenis Royal Academy'), END,
       t('Toasty Potato Wedges, Royal Gelato and Young Lady Platter, downstairs.',
         'Toasty Potato Wedges, Royal Gelato e Young Lady Platter, no andar de baixo.'),
       0, [MERCIA])
c.item('collectible', t('Squirrel Medal'), t("Manoria Village — Fiore's General Goods"), LEAVE_RUAN,
       t('1st of 5 animal medals that can later be traded together for a Beast Medal.',
         '1ª de 5 medalhas de animais que depois podem ser trocadas juntas por uma Beast Medal.'),
       0, [RUAN])
c.item('collectible', t('Gull Seaside Way treasure chests (11)', 'Baús da Gull Seaside Way (11)'), t('Gull Seaside Way'), LEAVE_RUAN,
       t('Includes a monster chest with crabs, an ammonite and a panda. Red-highlighted rocks and boxes hide extra loot.',
         'Inclui um baú de monstros com caranguejos, uma amonite e um panda. Pedras e caixas destacadas em vermelho escondem itens extras.'),
       0, [RUAN])
c.item('collectible', t('Manoria Byroad treasure chests (5)', 'Baús da Manoria Byroad (5)'), t('Manoria Byroad'), LEAVE_RUAN,
       t('Both branches of the fork have chests.', 'Os dois lados da bifurcação têm baús.'), 0, [RUAN])
c.item('collectible', t('Krone Trail treasure chests (3)', 'Baús da Krone Trail (3)'), t('Krone Trail'), LEAVE_RUAN,
       t('Break the boulder near the bushes below the ladders to open a hidden cave. Also touch Krone Pass to unlock fast travel.',
         'Quebre a rocha perto dos arbustos abaixo das escadas para abrir uma caverna escondida. Passe também pela Krone Pass para liberar a viagem rápida.'),
       0, [RUAN])
c.item('collectible', t('Vista Forest Road treasure chests (4)', 'Baús da Vista Forest Road (4)'), t('Vista Forest Road'), LEAVE_RUAN,
       t('One is a hard monster chest (a big Jabba with three instant-KO birds). Consider waiting for a full party.',
         'Um é um baú de monstros difícil (um Jabba grande com três aves de KO instantâneo). Vale esperar a equipe completa.'),
       0, [RUAN])
c.item('collectible', t('Aina Causeway treasure chests (3)', 'Baús da Aina Causeway (3)'), t('Aina Causeway'), LEAVE_RUAN,
       t('The hidden cave before Air-Letten has sepith veins, not chests.', 'A caverna escondida antes de Air-Letten tem veios de sepith, não baús.'),
       0, [RUAN])
c.item('collectible', t('Sapphirl Tower treasure chests (10)', 'Baús da Sapphirl Tower (10)'), t('Sapphirl Tower'), LEAVE_RUAN,
       t('Includes Rotund Meatballs (eat it for the recipe) and a brutal monster chest with five Aqua Trappers on 3F: earth arts help. Helm Cancers reflect physical hits; use arts.',
         'Inclui Rotund Meatballs (coma para ganhar a receita) e um baú de monstros brutal com cinco Aqua Trappers no 3F: arts de terra ajudam. Helm Cancers refletem golpes físicos; use arts.'),
       0, [RUAN])
c.item('collectible', t('Underground ruins treasure chests (19)', 'Baús das ruínas subterrâneas (19)'), t('Jenis Royal Academy — beneath the old schoolhouse', 'Jenis Royal Academy — sob a escola antiga'), END,
       t('Includes a monster chest with three Puppet Flagger+. Collect everything before the last healing station.',
         'Inclui um baú de monstros com três Puppet Flagger+. Pegue tudo antes da última estação de cura.'),
       1, [MERCIA])

c.write()
