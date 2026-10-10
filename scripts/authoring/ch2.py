# Chapter 2 — rewritten in our own words from the Neoseeker walkthrough (facts only).
# Once published, never reorder or remove items: ids are derived from order.
from lib import Chapter, gf, src, t

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
       t('Reward: +5 BP. You cannot leave the hotel until this quest ends.', 'Recompensa: +5 BP. Você não pode sair do hotel até terminar a missão.'),
       1, [RUAN], steps=[
           t('Talk to Nial and Dorothy downstairs to start.', 'Fale com Nial e Dorothy no andar de baixo para começar.'),
           t('Ask about every topic until no new ones appear.', 'Pergunte sobre todos os assuntos até não aparecerem novos tópicos.'),
           t('Final question 1: choose option 6.', 'Pergunta final 1: escolha a 6ª opção.'),
           t('Final question 2: choose option 2.', 'Pergunta final 2: escolha a 2ª opção.'),
           t('Final question 3: choose option 2.', 'Pergunta final 3: escolha a 2ª opção.'),
           t('Final question 4: choose option 2.', 'Pergunta final 4: escolha a 2ª opção.'),
       ])
c.item('quest', t('Winners Wanted'), t('Ruan — Lavantar Bar & Casino'), LEAVE_RUAN,
       t('Reward: +4 BP. A wrong choice fails the quest.\nWith Scherazard:\n• Estelle: 1st, then 1st.\n• Olivier: 1st, then 2nd.\n• Scherazard: 2nd.\nWith Agate:\n• Agate: 1st, then 1st.\n• Olivier: 1st, then 2nd.\n• Estelle: 2nd.', 'Recompensa: +4 BP. Uma escolha errada faz a missão falhar.\nCom Scherazard:\n• Estelle: 1ª, depois 1ª.\n• Olivier: 1ª, depois 2ª.\n• Scherazard: 2ª.\nCom Agate:\n• Agate: 1ª, depois 1ª.\n• Olivier: 1ª, depois 2ª.\n• Estelle: 2ª.'),
       0, [RUAN])
c.item('quest', t('Stolen Sign'), t('Zeiss'), LEAVE_ZEISS,
       t('Reward: +4 BP. Follow the clues through Zeiss.', 'Recompensa: +4 BP. Siga as pistas por Zeiss.'),
       0, [ZEISS], steps=[
           t('Ask Kilika about the missing sign.', 'Pergunte a Kilika sobre a placa desaparecida.'),
           t('Check the back of the clock tower in the plaza.', 'Examine a parte de trás da torre do relógio na praça.'),
           t('Use the factory 5F terminal: Central Factory → All Orbal Technology → Bracer Guild Sign.', 'Use o terminal no 5º andar da fábrica: Central Factory → All Orbal Technology → Bracer Guild Sign.'),
           t('Look under the three chimneys behind Forgel Bar.', 'Procure embaixo das três chaminés atrás do Forgel Bar.'),
           t('Talk to Fey by the conveyor on B1F.', 'Fale com Fey junto à esteira no B1F.'),
       ])
c.item('quest', t('Firearm Field Test'), t('Zeiss Central Factory — 3F', 'Zeiss Central Factory — 3º andar'), LEAVE_ZEISS,
       t('BP: 3 +2. Ten battles meet the minimum; win fifteen for the bonus.', 'BP: 3 +2. Dez batalhas cumprem o mínimo; vença quinze para receber o bônus.'),
       0, [ZEISS, CH3], steps=[
           t('Get the gun from Karl and equip it on Olivier.', 'Pegue a arma com Karl e equipe-a em Olivier.'),
           t('Win 15 Command Battles on Tratt Plains Road with that gun equipped.', 'Vença 15 Command Battles em Tratt Plains Road com essa arma equipada.'),
           t('Report back after the battles.', 'Volte para entregar a missão após as batalhas.'),
       ])
c.item('quest', t('Drill Duty'), t('Leiston Fortress — end of Soldat Army Road', 'Leiston Fortress — fim da Soldat Army Road'), FORT,
       t('3 +2 BP.\nThree rounds with no healing in between; you must win the last one for the bonus.', '3 +2 BP.\nTrês rodadas sem cura entre elas; é preciso vencer a última para ganhar o bônus.'),
       0, [ZEISS])
c.item('quest', t('Kaldia Tunnel Monster'), t('Kaldia Tunnel'), LEAVE_ZEISS,
       t('+3 BP.\nWhale frogs swallow allies: hit the frog three times to free them.', '+3 BP.\nOs sapos-baleia engolem aliados: acerte o sapo três vezes para libertá-los.'),
       0, [ZEISS])
c.item('quest', t('Tratt Plains Monster'), t('Tratt Plains Road — east, before the fort path', 'Tratt Plains Road — leste, antes do caminho do forte'), LEAVE_ZEISS,
       t('+3 BP.\nLots of ailments: debuff immunity makes it manageable. Do not wander into the fort by accident.', '+3 BP.\nMuitos efeitos negativos: imunidade a debuffs deixa a luta administrável. Cuidado para não entrar no forte sem querer.'),
       0, [ZEISS])
c.item('quest', t('Probe for Parts'), t('Zeiss Central Factory — ground floor', 'Zeiss Central Factory — térreo'), LEAVE_ZEISS,
       t('BP: 3 +2. Find all eight parts for the bonus.', 'BP: 3 +2. Encontre as oito peças para receber o bônus.'),
       1, [WOLF], steps=[
           t('Find 3 parts in the 3F Workshop.', 'Encontre 3 peças na Workshop do 3º andar.'),
           t('Find 4 parts in the 4F Laboratory.', 'Encontre 4 peças no Laboratory do 4º andar.'),
           t('Find 1 part by the cat in the 4F Clinic.', 'Encontre 1 peça junto ao gato na Clinic do 4º andar.'),
       ])
c.item('quest', t('Vanquish the Voyeurs'), t('Elmo Village — Maple Leaf Inn'), CAVE,
       t('+4 BP.\nEquip Confuse and Sleep protection before talking to Mao.', '+4 BP.\nEquipe proteção contra Confuse e Sleep antes de falar com a Mao.'),
       1, [WOLF])
c.item('quest', t('Tratt Plains Monster 2'), t('Tratt Plains Road — southwest cliff fishing spot', 'Tratt Plains Road — pesqueiro no penhasco a sudoeste'), LEAVE_ZEISS,
       t('+3 BP.\nA swarm that drains EP and blinds: wind arts and big S-Crafts clear it fast.', '+3 BP.\nUm enxame que drena EP e cega: arts de vento e S-Crafts fortes resolvem rápido.'),
       1, [WOLF])
c.item('quest', t('Army Road Monster'), t('Soldat Army Road — near Leiston Fortress', 'Soldat Army Road — perto da Leiston Fortress'), LEAVE_ZEISS,
       t('+3 BP.\nHits very hard: stack HP and keep buffs up.', '+3 BP.\nBate muito forte: aumente o HP e mantenha os buffs.'),
       1, [WOLF])

# Missables
c.item('missable', t('Bonus BP: talk to Rudi in Kaldia Tunnel', 'BP bônus: falar com o Rudi no Kaldia Tunnel'), t('Kaldia Tunnel — near the factory exit', 'Kaldia Tunnel — perto da saída da fábrica'), FORT,
       t('+3 BP just for talking to him.', '+3 BP só por conversar com ele.'), 0, [ZEISS])
c.item('missable', t('Bonus BP: question in the storeroom', 'BP bônus: pergunta no depósito'), t('Sanktheim Gate'), CAVE,
       t('+3 BP.\nIn the scene with Warrant Officer Talbot, pick the 3rd option.', '+3 BP.\nNa cena com o Warrant Officer Talbot, escolha a 3ª opção.'),
       1, [WOLF])
c.item('missable', t("Bonus BP: question in the professor's office", 'BP bônus: pergunta na sala do professor'), t('Zeiss Central Factory — 5F', 'Zeiss Central Factory — 5º andar'), CAVE,
       t('+2 BP.\nWhen asked where to go, pick the 3rd option.', '+2 BP.\nQuando perguntarem para onde ir, escolha a 3ª opção.'),
       1, [WOLF])

# Collectibles
c.item('collectible', t('Gambler Jack — Vol. 3'), t('Airliner to Zeiss', 'Airliner para Zeiss'), None,
       t('Talk to Olivier a second time after his scene on board. If you miss it, Bell Station in Zeiss sells a copy in Chapter 3.',
         'Fale com o Olivier uma segunda vez depois da cena dele a bordo. Se perder, a Bell Station em Zeiss vende uma cópia no Capítulo 3.'),
       0, [RUAN, CH3])
c.item('collectible', t('Liberl News Issue 3'), t('Zeiss — Bell Station'), LEAVE_ZEISS,
       t('Sold at Bell Station.', 'Vendido na Bell Station.'), 0, [ZEISS])
c.item('collectible', t('Recipes: Zeiss (4)', 'Receitas: Zeiss (4)'), t('Zeiss'), LEAVE_ZEISS,
       t('Obtain and eat each dish to learn its recipe.', 'Obtenha e coma cada prato para aprender sua receita.'),
       0, [ZEISS], steps=[
           t('Magma Wings — Forgel Bar.', 'Magma Wings — Forgel Bar.'),
           t('Acerbic Tomato Sandwich — Forgel Bar; Ben also gives one.', 'Acerbic Tomato Sandwich — Forgel Bar; Ben também dá um.'),
           t('Fruit Kingdom — Forgel Bar.', 'Fruit Kingdom — Forgel Bar.'),
           t('Mysterious Paste — Priam’s Drink Shop, outside the factory.', 'Mysterious Paste — Priam’s Drink Shop, fora da fábrica.'),
       ])
c.item('collectible', t('Recipe: Golden Risotto', 'Receita: Golden Risotto'), t('Sanktheim Gate — cafeteria'), LEAVE_ZEISS,
       t('Take the northeast branch of Ritter Roadway.', 'Siga pelo ramo nordeste da Ritter Roadway.'), 0, [ZEISS])
c.item('collectible', t('Recipes: Elmo Village (3)', 'Receitas: Elmo Village (3)'), t('Elmo Village — Maple Leaf Inn'), LEAVE_ZEISS,
       t('Obtain and eat each dish to learn its recipe.', 'Obtenha e coma cada prato para aprender sua receita.'), 0, [ZEISS], steps=[
           t('Continental Eggs', 'Continental Eggs'),
           t('Passionate Egg Roll', 'Passionate Egg Roll'),
           t('Top-Rated Shake', 'Top-Rated Shake'),
       ])
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

# ---------------------------------------------------------------- routes (append-only once published)
GF2 = gf('Chapter 2 - The Raging Land')
c.set_steps('sc-ch2-co-07', [
    t('North, along the west wall — Droplet of Defense', 'Ao norte, junto à parede oeste — Droplet of Defense'),
    t('Skip the northwest fork, continue east along the wall — U-Material', 'Ignore a bifurcação noroeste e siga a leste pela parede — U-Material'),
    t('Next chest — Jade Guard', 'Próximo baú — Jade Guard'),
], source=GF2)
c.set_steps('sc-ch2-co-08', [
    t('First chest along the road — Curia Balm ×2', 'Primeiro baú da estrada — Curia Balm ×2'),
    t('Next — Droplet of Spirit', 'Próximo — Droplet of Spirit'),
    t('Next — U-Material ×2', 'Próximo — U-Material ×2'),
    t('Monster chest (grasshoppers) — Red Sphere', 'Baú de monstros (gafanhotos) — Red Sphere'),
], source=GF2)
c.set_steps('sc-ch2-co-09', [
    t('First fork south (2 chests) — Salmon Roe ×5, EP Charge II', 'Primeira bifurcação ao sul (2 baús) — Salmon Roe ×5, EP Charge II'),
    t('West; a "statue" on the north wall is a monster. Next fork south — Gemini Boots', 'Oeste; uma "estátua" na parede norte é um monstro. Próxima bifurcação ao sul — Gemini Boots'),
    t('The splits at the end, left to right (3 chests) — U-Material ×2, Freeze, Red Fly ×5', 'As divisões no fim, da esquerda para a direita (3 baús) — U-Material ×2, Freeze, Red Fly ×5'),
], source=GF2)
c.set_steps('sc-ch2-co-10', [
    t('East path, southeast along the wall — Droplet of Strength', 'Caminho leste, sudeste junto à parede — Droplet of Strength'),
    t('Main road south — Petrify', 'Estrada principal ao sul — Petrify'),
    t('Northeast — Larva ×5', 'Nordeste — Larva ×5'),
    t('East — Teara Balm', 'Leste — Teara Balm'),
    t('Further south — Droplet of Magic', 'Mais ao sul — Droplet of Magic'),
    t('East along the north wall — Pisces Heart (fishing rod)', 'Leste pela parede norte — Pisces Heart (vara de pesca)'),
    t('Further east along the north wall — EP Charge II', 'Mais a leste pela parede norte — EP Charge II'),
    t('South along the east wall — U-Material ×2', 'Ao sul pela parede leste — U-Material ×2'),
    t('Monster chest (sheep and mantises) — Green Sphere', 'Baú de monstros (ovelhas e louva-a-deus) — Green Sphere'),
    t('Back in the southwest of this part — All Sepith ×100', 'De volta ao sudoeste desta parte — All Sepith ×100'),
    t('East along the south wall — Sleep', 'Leste pela parede sul — Sleep'),
    t('East, then south — Zeram Powder', 'Leste e depois sul — Zeram Powder'),
    t('Northwest — Thelas Balm ×2', 'Noroeste — Thelas Balm ×2'),
], source=GF2)
c.set_steps('sc-ch2-co-11', [
    t('1F, both sides of the roundabout and near the stairs (4 chests) — EP Charge II, Droplet of Defense, All Sepith ×100, Thelas Balm ×2', '1F, dos dois lados da rotatória e perto da escada (4 baús) — EP Charge II, Droplet of Defense, All Sepith ×100, Thelas Balm ×2'),
    t('2F, center of the room — Droplet of Strength', '2F, centro da sala — Droplet of Strength'),
    t('West fork up to 3F — U-Material', 'Bifurcação oeste até o 3F — U-Material'),
    t('East fork up to 3F — Seal', 'Bifurcação leste até o 3F — Seal'),
    t('4F, all the way south (2 chests) — Teara Balm, Droplet of Spirit', '4F, todo o caminho ao sul (2 baús) — Teara Balm, Droplet of Spirit'),
    t('5F (east stairs are closer), south — Cashmere Sweater', '5F (a escada leste fica mais perto), ao sul — Cashmere Sweater'),
    t('5F, around the central room (5 chests) — Accelerators, Droplet of Magic, Five-Ring Staff, Red Jacket and a monster chest with Vajra (five Fire Trappers)', '5F, ao redor da sala central (5 baús) — Accelerators, Droplet of Magic, Five-Ring Staff, Red Jacket e um baú de monstros com Vajra (cinco Fire Trappers)'),
], source=GF2)
c.set_steps('sc-ch2-co-12', [
    t('East fork — Thelas Balm ×2', 'Bifurcação leste — Thelas Balm ×2'),
    t('West fork — monster chest: Machine Planker', 'Bifurcação oeste — baú de monstros: Machine Planker'),
    t('South, then east, among the Ya-Kahs — Gemini Boots+', 'Sul e depois leste, entre os Ya-Kahs — Gemini Boots+'),
    t('Back, then south — Septium Jelly Beans', 'Volte e siga ao sul — Septium Jelly Beans'),
    t('Back, then west near the Faerie Epitaph — Zeram Powder', 'Volte e siga a oeste, perto do Faerie Epitaph — Zeram Powder'),
    t('Fork north — Cashmere Sweater+', 'Bifurcação ao norte — Cashmere Sweater+'),
    t('West, then southeast with the Shining Poms — All Sepith ×100', 'Oeste e depois sudeste, junto aos Shining Poms — All Sepith ×100'),
    t('Side branch by the hot spring near the end (2 chests) — Teara Balm, EP Charge II', 'Desvio da fonte termal perto do fim (2 baús) — Teara Balm, EP Charge II'),
], source=GF2)

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
