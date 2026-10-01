# Chapter 5 — rewritten in our own words from the GameFAQs walkthrough by shockinblue (facts only).
# Once published, never reorder or remove items: ids are derived from order.
from lib import Chapter, gf, t

D1 = gf('Chapter 5 - Day 1')
D2 = gf('Chapter 5 - Day 2')

c = Chapter(5, 'Chapter 5', 'Capítulo 5')
LEAVE_ROLENT = c.cp('Boarding the airliner from Rolent to Bose', 'Embarcar no airliner de Rolent para Bose')
LUGRAN = c.cp('Reporting to Lugran at the Bose guild after Nebel Valley (the market closes)',
              'Falar com o Lugran na guilda de Bose depois do Nebel Valley (o mercado fecha)')
WAIT = c.cp('Choosing to wait for the airship in Bose', 'Escolher esperar o airship em Bose')
END = c.cp('The last event marker of Chapter 5', 'O último marcador de evento do Capítulo 5')

# Quests — Rolent, start of the chapter
c.item('quest', t('Recipe Reminiscence'), t('Rolent — Abend Bar kitchen', 'Rolent — cozinha do Abend Bar'), LEAVE_ROLENT,
       t('+4 BP. Ask Lao at the counter, Bloom on the 2F of the general store and Rhett in the apartment next to the bar; read the recipe book in Rhett\'s room. Everything can be bought except 2 Monster Bone (Dirty Rat, Crop Muncher). Rewards the Spiced Stew recipe.',
         '+4 BP. Pergunte ao Lao no balcão, à Bloom no 2F do armazém e ao Rhett no apartamento ao lado do bar; leia o livro de receitas no quarto do Rhett. Tudo pode ser comprado, menos 2 Monster Bone (Dirty Rat, Crop Muncher). A recompensa é a receita Spiced Stew.'),
       0, [D1])
c.item('quest', t('Dabbling with Diaset'), t('Rolent — top of the clock tower', 'Rolent — topo da torre do relógio'), LEAVE_ROLENT,
       t('+4 BP. Hand Anton 5 Monster Shell (Russet Beetle), 5 Monster Seed (Lily Mover, Pine Plant), 5 Monster Powder (Garphase, Killer Hornet) and 1 Pearlglass (fish it on Milch Main Road or Elize Highway). Olivier has to step out of the party for a moment.',
         '+4 BP. Entregue ao Anton 5 Monster Shell (Russet Beetle), 5 Monster Seed (Lily Mover, Pine Plant), 5 Monster Powder (Garphase, Killer Hornet) e 1 Pearlglass (pesque na Milch Main Road ou na Elize Highway). O Olivier precisa sair da equipe por um momento.'),
       0, [D1])
c.item('quest', t('Commission Caper'), t("Rolent — Mine Chief Garton's residence", 'Rolent — residência do Mine Chief Garton'), LEAVE_ROLENT,
       t('+5 BP. Clues: the chair on the chapel balcony upstairs, the crates on the south side of the Mayor\'s house, the forge behind the arms shop, then the locked door in Rolent Sewers (fight inside; the document is on the table).',
         '+5 BP. Pistas: a cadeira na sacada do andar de cima da capela, as caixas no lado sul da casa do prefeito, a forja atrás da loja de armas e, por fim, a porta trancada no Rolent Sewers (luta lá dentro; o documento está na mesa).'),
       0, [D1])
# Quests — Bose
c.item('quest', t("Ambassador's Assignment"), t('Bose — Frieden Hotel, 2F', 'Bose — Frieden Hotel, 2º andar'), WAIT,
       t('+5 BP. Clues: the basket of red flowers outside the 2F door of the orbal factory, the desk with an open book on the guild 3F, the crate on the forklift at the landing port, and the book on the altar upstairs in the chapel (side door).',
         '+5 BP. Pistas: a cesta de flores vermelhas do lado de fora da porta do 2F da fábrica orbal, a mesa com um livro aberto no 3F da guilda, a caixa na empilhadeira do porto e o livro no altar do andar de cima da capela (porta lateral).'),
       0, [D1])
c.item('quest', t('Delicacy Delivery'), t('Bose — Anterose Restaurant'), LUGRAN,
       t('4 +2 BP. Deliver 10 each of Monster Horn, Fang, Shell, Bone, Tail, Eye, Fish Meat and Roe. Orvid, outside the market\'s south entrance, chips in 7 of each, so you only need 3 more of each; you still get the bonus.',
         '4 +2 BP. Entregue 10 de cada: Monster Horn, Fang, Shell, Bone, Tail, Eye, Fish Meat e Roe. O Orvid, do lado de fora da entrada sul do mercado, contribui com 7 de cada, então só faltam 3 de cada; o bônus continua valendo.'),
       0, [D1])
c.item('quest', t('Damsel Disappearance'), t('Bose — Anterose Restaurant'), LUGRAN,
       t('4 +1 BP. Leads to Krone Pass. When talking to the girl there, pick the option that calls her a coward.',
         '4 +1 BP. Leva à Krone Pass. Ao falar com a garota lá, escolha a opção que a chama de covarde.'),
       0, [D1])

# Missables
c.item('missable', t('Bonus BP: report after the valley', 'BP bônus: relato depois do vale'), t('Nebel Valley'), LUGRAN,
       t('+2 BP. After the last required monster request, pick the option saying the monsters were agitated.',
         '+2 BP. Depois do último pedido obrigatório de monstro, escolha a opção que diz que os monstros estavam agitados.'),
       1, [D1])
c.item('missable', t('Bonus BP: the plan at the guild', 'BP bônus: o plano na guilda'), t('Bose — Bracer Guild', 'Bose — Bracer Guild'), LUGRAN,
       t('+3 BP. In the scene after talking to Lugran, choose to make a plan first.',
         '+3 BP. Na cena depois de falar com o Lugran, escolha fazer um plano primeiro.'),
       1, [D1])

# Collectibles
c.item('collectible', t('Recipe: Herbal Squeeze', 'Receita: Herbal Squeeze'), t('Perzel Farm'), LEAVE_ROLENT,
       t('Talk to Hanna inside the farmhouse before leaving Rolent.', 'Fale com a Hanna dentro da casa da fazenda antes de sair de Rolent.'),
       0, [D1])
c.item('collectible', t('Gambler Jack — Vol. 7'), t('Krone Pass checkpoint', 'Posto da Krone Pass'), LUGRAN,
       t('Talk to Private Mikey.', 'Fale com o Private Mikey.'), 0, [D1])
c.item('collectible', t('Liberl News Issue 7'), t('Bose Market — Grocery Minuet'), WAIT,
       t('Also sold at the general store in Ravennue Village.', 'Também vendido no armazém de Ravennue Village.'), 0, [D1])
c.item('collectible', t('Liberl News — Special Edition'), t('Bose — Frieden Hotel, 2F', 'Bose — Frieden Hotel, 2º andar'), WAIT,
       t('Sold by the grocer while the market stalls are set up inside the hotel.', 'Vendido pelo merceeiro enquanto as barracas do mercado ficam dentro do hotel.'),
       1, [D2])
c.item('collectible', t('Plain Medal'), t('Bose Market — Paul Elk'), WAIT,
       t('The 5th animal medal. With all five, trade them for the Beast Medal through the Customize menu at the orbal factory.',
         'A 5ª medalha de animal. Com as cinco, troque pela Beast Medal no menu Customize da fábrica orbal.'),
       0, [D1])
c.item('collectible', t('West Bose Highway treasure chests (4)', 'Baús da West Bose Highway (4)'), t('West Bose Highway'), END,
       t('One holds a weapon for Olivier, across the bridge to the east.', 'Um guarda uma arma do Olivier, depois da ponte a leste.'), 0, [D1])
c.item('collectible', t('Krone Trail treasure chests (5)', 'Baús da Krone Trail (5)'), t('Krone Trail'), END,
       t('Includes a monster chest with scorpions and a Hapilsag. Drop down the ladders for extra field items.',
         'Inclui um baú de monstros com escorpiões e um Hapilsag. Desça pelas escadas para pegar itens de campo extras.'),
       0, [D1])
c.item('collectible', t('New Ansel Path treasure chests (6)', 'Baús da New Ansel Path (6)'), t('New Ansel Path'), END,
       t('The last one sits right outside Amberl Tower.', 'O último fica logo na frente da Amberl Tower.'), 0, [D1])
c.item('collectible', t('Amberl Tower treasure chests (22)', 'Baús da Amberl Tower (22)'), t('Amberl Tower'), END,
       t('Spread across all five floors; the 3F and 4F outer loops hide several. The 5F monster chest has three Ground Trappers: wind arts, and they explode when defeated.',
         'Espalhados pelos cinco andares; os anéis externos do 3F e do 4F escondem vários. O baú de monstros do 5F tem três Ground Trappers: use arts de vento, e eles explodem quando caem.'),
       0, [D1])
c.item('collectible', t('Eisen Road and East Bose Highway treasure chests (5)', 'Baús da Eisen Road e da East Bose Highway (5)'), t('Eisen Road, East Bose Highway'), END,
       t('East Bose Highway has a monster chest with turtles uphill along the south wall, and a breakable wall leading to a water cave.',
         'A East Bose Highway tem um baú de monstros com tartarugas na subida junto à parede sul, e uma parede quebrável que leva a uma caverna com água.'),
       0, [D1])
c.item('collectible', t('Nebel Valley treasure chests (3)', 'Baús do Nebel Valley (3)'), t('Nebel Valley'), END,
       t('One is just before the old stronghold entrance. Whemler, in his hut, gives you Dark Stew if you accept his stew on the second talk.',
         'Um fica logo antes da entrada da antiga fortaleza. O Whemler, na cabana dele, dá Dark Stew se você aceitar o ensopado na segunda conversa.'),
       0, [D1])
c.item('collectible', t('Ravennue Trail treasure chests (9)', 'Baús da Ravennue Trail (9)'), t('Ravennue Trail'), END,
       t('Explore both branches past the village; one holds a weapon for Zin.', 'Explore os dois ramos depois da vila; um guarda uma arma do Zin.'), 0, [D1])
c.item('collectible', t('Abandoned mine treasure chests (5)', 'Baús da mina abandonada (5)'), t('Mine near Ravennue Village', 'Mina perto de Ravennue Village'), WAIT,
       t('One is hidden behind breakables on the north fork near the start.', 'Um fica escondido atrás de objetos quebráveis no ramo norte, perto do início.'),
       1, [D1])
c.item('collectible', t('Dragon lair treasure chests (11)', 'Baús do covil do dragão (11)'), t('North of Nebel Valley', 'Ao norte do Nebel Valley'), END,
       t('A side cave on the left holds two, and a dead end near the last healing device has three, including a monster chest (Master Cryon and its Cryons).',
         'Uma caverna lateral à esquerda guarda dois, e um beco perto do último dispositivo de cura tem três, incluindo um baú de monstros (Master Cryon e seus Cryons).'),
       1, [D2])

# ---------------------------------------------------------------- routes (append-only once published)
c.set_steps('sc-ch5-co-06', [
    t('Follow the south wall from the start — Zeram Powder', 'Siga a parede sul desde o início — Zeram Powder'),
    t('Uphill, across the bridge to the east, then south — Phantom II', 'Suba, cruze a ponte a leste e vá ao sul — Phantom II'),
    t('At the fork, south wall (Shining Poms nearby) — Tearal Balm', 'Na bifurcação, parede sul (Shining Poms por perto) — Tearal Balm'),
    t('West past the cave entrance — Droplet of Defense', 'A oeste, depois da entrada da caverna — Droplet of Defense'),
], source=D1)
c.set_steps('sc-ch5-co-07', [
    t('At the end of the scorpion stretch — Impede 4', 'No fim do trecho dos escorpiões — Impede 4'),
    t('Back on the main road — U-Material+', 'De volta à estrada principal — U-Material+'),
    t('Next chest — monster chest: General\'s Mantle (a Hapilsag with scorpions)', 'Próximo baú — baú de monstros: General\'s Mantle (um Hapilsag com escorpiões)'),
    t('Drop down the ladders east of it; at the bottom — Droplet of Life', 'Desça pelas escadas a leste dele; lá embaixo — Droplet of Life'),
    t('Back on the main road, next chest — All Sepith ×250', 'De volta à estrada principal, próximo baú — All Sepith ×250'),
], source=D1)
c.set_steps('sc-ch5-co-08', [
    t('Along the east wall — EP Charge III', 'Junto à parede leste — EP Charge III'),
    t('Next chest — U-Material ×3', 'Próximo baú — U-Material ×3'),
    t('Next chest — HP 4', 'Próximo baú — HP 4'),
    t('West fork toward Amberl Tower, north wall — Droplet of Magic', 'Bifurcação oeste rumo à Amberl Tower, parede norte — Droplet of Magic'),
    t('Next chest — Athelas Balm ×2', 'Próximo baú — Athelas Balm ×2'),
    t('Right outside Amberl Tower — Droplet of Spirit', 'Logo na frente da Amberl Tower — Droplet of Spirit'),
], source=D1)
c.set_steps('sc-ch5-co-09', [
    t('1F, by the stairs (2 chests) — Droplet of Defense, Buster Gear', '1F, junto à escada (2 baús) — Droplet of Defense, Buster Gear'),
    t('2F, southeast to the end — All Sepith ×250', '2F, sudeste até o fim — All Sepith ×250'),
    t('3F, top of the stairs (2 chests) — U-Material+, Tearal Balm', '3F, no alto da escada (2 baús) — U-Material+, Tearal Balm'),
    t('3F, past the center room at the foot of the stairs (2 chests) — Zeram Powder, Athelas Balm ×2', '3F, depois da sala central, ao pé da escada (2 baús) — Zeram Powder, Athelas Balm ×2'),
    t('3F, end of the stairs toward 4F (3 chests) — EP Charge III, All Sepith ×250, Athelas Balm ×2', '3F, fim da escada rumo ao 4F (3 baús) — EP Charge III, All Sepith ×250, Athelas Balm ×2'),
    t('Outer loop, south path (2 chests) — Break 4, EP Charge III', 'Anel externo, caminho sul (2 baús) — Break 4, EP Charge III'),
    t('Outer loop toward the north stairs (2 chests) — Tearal Balm, Droplet of Life', 'Anel externo rumo à escada norte (2 baús) — Tearal Balm, Droplet of Life'),
    t('4F (2 chests) — Droplet of Strength, Tearal Balm', '4F (2 baús) — Droplet of Strength, Tearal Balm'),
    t('Up to 5F, around the outside and down the south stairs (2 chests) — Droplet of Magic, U-Material ×3', 'Suba ao 5F, contorne por fora e desça a escada sul (2 baús) — Droplet of Magic, U-Material ×3'),
    t('5F, center room (3 chests) — EP Charge III, Droplet of Spirit, Ebony Shoes', '5F, sala central (3 baús) — EP Charge III, Droplet of Spirit, Ebony Shoes'),
    t('5F, southwest — monster chest: Ingenuity (wind arts; they explode)', '5F, sudoeste — baú de monstros: Ingenuity (arts de vento; eles explodem)'),
], source=D1)
c.set_steps('sc-ch5-co-10', [
    t('Eisen Road, along the west wall — Droplet of Strength', 'Eisen Road, junto à parede oeste — Droplet of Strength'),
    t('Eisen Road, next chest — Ebony Suit', 'Eisen Road, próximo baú — Ebony Suit'),
    t('East Bose Highway, south wall going uphill east — monster chest: Heal', 'East Bose Highway, parede sul subindo a leste — baú de monstros: Heal'),
    t('The chest icon below the hill (reach it from underneath) — U-Material+', 'O ícone de baú abaixo da colina (chegue por baixo) — U-Material+'),
    t('Further east — Strike 4', 'Mais a leste — Strike 4'),
], source=D1)
c.set_steps('sc-ch5-co-11', [
    t('Where the path splits, left across the bridge — Droplet of Spirit', 'Onde o caminho se divide, à esquerda depois da ponte — Droplet of Spirit'),
    t('Right path — Misty Veil', 'Caminho da direita — Misty Veil'),
    t('Last stretch, just before the old stronghold — Arondight', 'Último trecho, logo antes da antiga fortaleza — Arondight'),
], source=D1)
c.set_steps('sc-ch5-co-12', [
    t('Before the slope, near the start — U-Material+', 'Antes da subida, perto do início — U-Material+'),
    t('Past the village: right path, then southeast — Baihu Claws', 'Depois da vila: caminho da direita e depois sudeste — Baihu Claws'),
    t('Northeast — All Sepith ×250', 'Nordeste — All Sepith ×250'),
    t('Around the bend to the north (2 chests) — Tearal Balm, Droplet of Life', 'Depois da curva, ao norte (2 baús) — Tearal Balm, Droplet of Life'),
    t('Back at the start, left path, first north fork — EP Charge III', 'De volta ao início, caminho da esquerda, primeira bifurcação ao norte — EP Charge III'),
    t('West, then south — Droplet of Magic', 'Oeste e depois sul — Droplet of Magic'),
    t('Southwest of the Fate Spinner — U-Material ×3', 'A sudoeste do Fate Spinner — U-Material ×3'),
    t('Northwest — Athelas Balm ×2', 'Noroeste — Athelas Balm ×2'),
], source=D1)
c.set_steps('sc-ch5-co-13', [
    t('Right at the start, north fork, behind breakables — Tearal Balm', 'À direita no início, bifurcação norte, atrás de objetos quebráveis — Tearal Balm'),
    t('South fork right after the red marker — Evade 4', 'Bifurcação sul logo depois do marcador vermelho — Evade 4'),
    t('West fork off the main path (2 chests) — U-Material+, U-Material ×3', 'Bifurcação oeste da trilha principal (2 baús) — U-Material+, U-Material ×3'),
    t('Next fork, north — Droplet of Life', 'Próxima bifurcação, ao norte — Droplet of Life'),
], source=D1)
c.set_steps('sc-ch5-co-14', [
    t('First fork, north (2 chests) — Tearal Balm, U-Material+', 'Primeira bifurcação, ao norte (2 baús) — Tearal Balm, U-Material+'),
    t('Outside, the cave entrance on the left (2 chests) — Zeram Capsule, Droplet of Defense', 'Do lado de fora, a entrada da caverna à esquerda (2 baús) — Zeram Capsule, Droplet of Defense'),
    t('Back inside, east fork with the Shining Poms (2 chests) — Cast 4, EP Charge III', 'De volta para dentro, bifurcação leste com os Shining Poms (2 baús) — Cast 4, EP Charge III'),
    t('West along the north wall — Droplet of Life', 'Oeste pela parede norte — Droplet of Life'),
    t('After the red marker, east fork then north — All Sepith ×250', 'Depois do marcador vermelho, bifurcação leste e depois norte — All Sepith ×250'),
    t('West of the healing device, dead end (2 chests) — Droplet of Strength, Athelas Balm ×2', 'A oeste do dispositivo de cura, beco (2 baús) — Droplet of Strength, Athelas Balm ×2'),
    t('Same dead end, east — monster chest: Holy Bottle', 'Mesmo beco, a leste — baú de monstros: Holy Bottle'),
], source=D2)

# ---------------------------------------------------------------- bosses
c.boss(t('Blade Fang ×2'), t('Krone Trail'),
       t('Huge HP and little else. They sometimes confuse themselves; each survives one lethal hit, so keep a follow-up ready.',
         'Muito HP e pouco mais. Às vezes eles se confundem sozinhos; cada um sobrevive a um golpe letal, então tenha um ataque extra pronto.'),
       sources=[D1])
c.boss(t('Octobone ×4'), t('Amberl Tower — roof', 'Amberl Tower — terraço'),
       t('Petrify and Burn protection; high-tier fire arts work well. Their basic attack drains HP, EP and CP.',
         'Proteção contra Petrify e Burn; arts de fogo fortes funcionam bem. O ataque básico deles drena HP, EP e CP.'),
       sources=[D1])
c.boss(t('Ghost Epitaph'), t('Nebel Valley'),
       t('Bring Freeze and Petrify protection (Red Sphere+ covers both) and strong wind arts. Keep Earth Guard up and some CP to steal its zero-arts bonus.',
         'Leve proteção contra Freeze e Petrify (a Red Sphere+ cobre os dois) e arts de vento fortes. Mantenha o Earth Guard e guarde CP para roubar o bônus de arts instantâneas.'),
       sources=[D1])
c.boss(t('Gold Spinner'), t('Ravennue Trail'),
       t('Lots of HP; bring Petrify protection and wind arts.', 'Muito HP; leve proteção contra Petrify e arts de vento.'),
       sources=[D2])
c.boss(t('Ragnard'), t('Dragon lair — summit', 'Covil do dragão — topo'),
       t('Big but not hard. Get behind its head for back-attack bonuses, resist Blind and Burn, shield the party after its half-HP scene, and strip its boost with Anti-Sept.',
         'Grande, mas não difícil. Vá para trás da cabeça para ganhar bônus de ataque pelas costas, resista a Blind e Burn, proteja a equipe com escudo depois da cena na metade do HP e remova o reforço com Anti-Sept.'),
       sources=[D2])

# ---------------------------------------------------------------- fishing
TROUT, EEL = 'sc-ch1-fi-06', 'sc-ch1-fi-08'
KASAGIN, YAMANY, TIGER, LCARP, VBASS, RTROUT, CARP, ROCK, SALMON = (f'sc-ch2-fi-{n:02d}' for n in range(1, 10))
GARVELZE = 'sc-ch4-fi-01'
VALLERIA = t('Valleria Shore — by the docks', 'Valleria Shore — junto às docas')
for fish in (VBASS, ROCK, TROUT, SALMON, GARVELZE):
    c.spot(fish, 'A', VALLERIA)
for fish in (KASAGIN, CARP, EEL):
    c.spot(fish, 'A', t('Ravennue Village — docks', 'Ravennue Village — docas'))
for fish in (YAMANY, TIGER, LCARP):
    c.spot(fish, 'A', t('Mistwald — bridge at the back (opens this chapter)', 'Mistwald — ponte no fundo (abre neste capítulo)'))

# ---------------------------------------------------------------- recipes
c.recipe('Spiced Stew', t('Reward for Recipe Reminiscence', 'Recompensa da Recipe Reminiscence'), sources=[D1])
c.recipe('Herbal Squeeze', t('Hanna at Perzel Farm', 'Hanna, na Perzel Farm'), sources=[D1])
c.recipe('Crimson Monster Stew', t('Kirsche Bar, Bose'), sources=[D1])
c.recipe('Toasty Side Soup', t('Kirsche Bar, Bose'), sources=[D1])
c.recipe('Refreshing Jelly', t("Caterina's Shop, Bose Market"), sources=[D1])
c.recipe('Angular Castella', t("Caterina's Shop, Bose Market"), sources=[D1])
c.recipe('Eastern Fried Fish', t('The Kingfisher Inn, Valleria Shore'), sources=[D1])
c.recipe('Miso Simmered Fish', t('The Kingfisher Inn, Valleria Shore'), sources=[D1])
c.recipe('Berserker Fish', t('The Kingfisher Inn, Valleria Shore'), sources=[D1])
c.recipe('Attention Grabber', t('Haken Gate rest area', 'Área de descanso do Haken Gate'), sources=[D1])
c.recipe('Dark Stew', t("Whemler's hut, Nebel Valley (accept the stew on the second talk)", 'Cabana do Whemler, Nebel Valley (aceite o ensopado na segunda conversa)'), sources=[D1])
c.recipe('Mighty Juice', t('The Moonlight Path 2F, Ravennue Village', 'The Moonlight Path, 2º andar, Ravennue Village'), sources=[D1])

c.write()
