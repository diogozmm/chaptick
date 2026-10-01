# Ys X: Proud Nordics — rewritten in our own words from the Neoseeker walkthrough (names follow
# Neoseeker), cross-checked with GameFAQs (facts only). Quests with deadlines and a few character
# notes are what is lost for good; treasure chests are listed in the chapter where they can FIRST be
# opened (buried ones need Mana Sense, learned at the end of Chapter 4), with no deadline because
# every area can be revisited, except the Chapter 10 ones, which close with the final battle.
# Chests that the story forces you to open (keys, Rune Tablets, Gullinboard...) are left out.
# Once published, never reorder or remove anything: ids are derived from order.
import re

from lib import Chapter, t

G = 'ysx'
NEO = lambda page: f'guide: Neoseeker Ys X walkthrough, {page}'
GF = lambda page: f'guide: GameFAQs Ys X walkthrough, {page}'
CH = {}
B = True  # buried treasure: needs Mana Sense


def chapter(order, en, pt):
    CH[order] = Chapter(order, en, pt, game=G)
    return CH[order]


def fish(c, name, spots, sources):
    fid = c.fish(name, sources=sources)
    for where, bait in spots:
        c.spot(fid, None, where, bait)
    return fid


def qty(name):
    return re.sub(r' x ?(\d)', r' ×\1', name)


def chests(c, area, rows, hint, sources, until=None, title=None):
    """One checklist entry per area; every chest is a step. rows: (item, where_en, where_pt[, buried])."""
    steps = []
    for row in rows:
        item, w_en, w_pt = qty(row[0]), row[1], row[2]
        buried = len(row) > 3 and row[3]
        en = f'{w_en} — {item}' if w_en else item
        pt = f'{w_pt} — {item}' if w_pt else item
        steps.append(t(en + (' (buried)' if buried else ''), pt + (' (enterrado)' if buried else '')))
    n = len(rows)
    name = t(f'{title[0]} ({n})', f'{title[1]} ({n})') if title else t(f'{area[0]} treasure chests ({n})', f'Baús de {area[1]} ({n})')
    c.item('collectible', name, t(*area), until, t(*hint), 0, sources, steps=steps)


# ======================================================================== Prologue
c = chapter(0, 'Prologue', 'Prólogo')
c.boss(t('Masked Woman', 'Mulher mascarada'), t('Passenger liner Adamas', 'Navio de passageiros Adamas'),
       t('A tutorial fight that still hits hard: guard or dodge her swings and practise the timed guard, which blocks all damage and opens a counterattack.',
         'Uma luta tutorial que ainda bate forte: defenda ou desvie dos golpes e treine a defesa no tempo certo, que bloqueia todo o dano e abre um contra-ataque.'),
       sources=[NEO('Prologue')])

# ======================================================================== Chapter 1
c = chapter(1, 'Chapter 1', 'Capítulo 1')
c.boss(t('Armed Biter'), t('Haagen Highway lighthouse', 'Farol da Haagen Highway'),
       t('Equip the Double Smash duo skill before the fight. When it glows red and leaps, hold the duo guard at the peak of the jump to counter; after its armor breaks it gets faster, so keep the guard ready.',
         'Equipe a habilidade em dupla Double Smash antes da luta. Quando ele brilhar em vermelho e saltar, segure a defesa em dupla no ápice do salto para contra-atacar; depois que a armadura quebra ele fica mais rápido, então mantenha a defesa pronta.'),
       sources=[NEO('Chapter 1'), GF('Chapter 1: Carnac')])
chests(c, ('Haagen Highway lighthouse; Mysterious Island', 'Farol da Haagen Highway; Mysterious Island'), [
    ('150 Gold', 'Lighthouse — first area, after the wolf pack', 'Farol — primeira área, depois da matilha de lobos'),
    ('Breath Water', 'Mysterious Island — short detour southwest before the red marker', 'Mysterious Island — pequeno desvio a sudoeste antes do marcador vermelho'),
], ('Breath Water permanently adds one more potion to your stock: grab it on this visit.',
    'A Breath Water adiciona para sempre mais uma poção ao seu estoque: pegue nesta visita.'),
    [NEO('Chapter 1')], title=('Chapter 1 treasure chests', 'Baús do Capítulo 1'))

# ======================================================================== Chapter 2
c = chapter(2, 'Chapter 2', 'Capítulo 2')
c.boss(t('Ziomander'), t('Cavern of Rite', 'Cavern of Rite'),
       t("Burn its vine shield with Adol's Mana Burst. Dash, not guard, through its blue speed attacks and the circling water laser. Near death it spams lightning: step away from the faint glow on the ground.",
         'Queime o escudo de vinhas com o Mana Burst do Adol. Use o dash, não a defesa, contra os ataques rápidos azuis e o laser de água giratório. Perto de morrer ele solta raios sem parar: saia do brilho fraco no chão.'),
       sources=[NEO('Chapter 2'), GF('Chapter 2: Shield Brethren')])
c.boss(t('Iði'), t('Cavern of Rite — Runestone', 'Cavern of Rite — Runestone'),
       t('The Double Smasher duo skill is your best tool. Duo guard his charged ground slam to fill the Revenge Gauge; his arm sweep hits up to four times with a shockwave at the end. When he jumps back, a speed attack is coming: dash instead of guarding.',
         'A habilidade em dupla Double Smasher é sua melhor arma. Use a defesa em dupla contra o golpe no chão carregado para encher o Revenge Gauge; a varrida de braço acerta até quatro vezes, com uma onda de choque no fim. Quando ele pula para trás, vem um ataque rápido: use o dash em vez de defender.'),
       sources=[NEO('Chapter 2'), GF('Chapter 2: Shield Brethren')])
c.recipe('Plain Box Lunch', t('Given by Karja on Lecto Island', 'Dada pela Karja em Lecto Island'), sources=[NEO('Chapter 10 - Trophy Cleanup')])
S2 = [NEO('Chapter 2')]
chests(c, ('Lecto Island', 'Lecto Island'), [
    ('Basic Ingredients x10', 'Beach area, before the cave at the top', 'Área da praia, antes da caverna no alto'),
    ('Stimulant x2', 'Beach area', 'Área da praia'),
    ('Arion Charm', 'Beach area', 'Área da praia'),
], ('Two buried treasures marked "???" open in Chapter 5, once you have Mana Sense.',
    'Dois tesouros enterrados marcados com "???" abrem no Capítulo 5, quando você tiver o Mana Sense.'), S2)
chests(c, ('Cavern of Rite', 'Cavern of Rite'), [
    ('Armor Seal', 'Room after the arrow trap', 'Sala depois da armadilha de flechas'),
    ('Warrior Bandana', 'Room on the right behind vines (burn them with Adol)', 'Sala à direita atrás de vinhas (queime com o Adol)'),
    ('Breath Formula', 'Opposite side of the same room', 'Lado oposto da mesma sala'),
    ('Cure Leaf x3', 'Pendulum room, right corner', 'Sala do pêndulo, canto direito'),
    ('Axe Seal', 'Pendulum room, left corner', 'Sala do pêndulo, canto esquerdo'),
], ('Use Karja\'s ice pillar to reach the higher platforms. Two buried treasures open in Chapter 5.',
    'Use o pilar de gelo da Karja para alcançar as plataformas altas. Dois tesouros enterrados abrem no Capítulo 5.'), S2)
chests(c, ('Mysterious Island', 'Mysterious Island'), [
    ('Lyre Seal', 'North past the vines: drop to the center of the big open area', 'Ao norte, depois das vinhas: desça ao centro da grande área aberta'),
    ('Red Strong-Arm', 'End of the southeast passage (Mana String on the trees), by the cave', 'Fim da passagem sudeste (Mana String nas árvores), junto à caverna'),
    ('Blessed Paper Scrap', 'Inside the cave (burn the vines)', 'Dentro da caverna (queime as vinhas)'),
], ('The Blessed Paper Scrap unlocks an accessory slot. The three locked gray chests in the cave open later with story keys.',
    'O Blessed Paper Scrap libera um espaço de acessório. Os três baús cinza trancados na caverna abrem mais tarde com chaves da história.'), S2)

# ======================================================================== Chapter 3
c = chapter(3, 'Chapter 3', 'Capítulo 3')
END3 = c.cp('The last event marker of Chapter 3 (the rescue in Carnac)', 'O último marcador de evento do Capítulo 3 (o resgate em Carnac)')
c.item('quest', t('Cargo A-Go-Go'), t('Sandras — talk to Grenn on the lower deck', 'Sandras — fale com o Grenn no convés inferior'), END3,
       t('Long deadline. Pick up the three supply boxes at the green markers: behind Balta Island, between Carnac and Balta Island, and far southwest of Carnac near Tyrant Hills (blast the pillars with the cannon first).',
         'Prazo longo. Recolha as três caixas de suprimentos nos marcadores verdes: atrás de Balta Island, entre Carnac e Balta Island, e bem a sudoeste de Carnac, perto de Tyrant Hills (destrua os pilares com o canhão antes).'),
       0, [NEO('Chapter 3 - Balta Island'), GF('Chapter 3: Where the Light Leads')])
c.boss(t('Magna Diga'), t('Termina Island'),
       t('Proud Nordics reworked this fight: ride the Mana Board (Mana Ride) to reach it fast, which also keeps you safe from the quicksand ailments. It burrows to reposition. Below half HP it adds body slams and bite combos: guard to build the Revenge Gauge, then unleash Cross Edge.',
         'O Proud Nordics refez esta luta: use a Mana Board (Mana Ride) para chegar rápido, o que também evita os efeitos da areia movediça. Ele se enterra para mudar de lugar. Abaixo da metade do HP, ele adiciona pancadas com o corpo e combos de mordida: defenda para encher o Revenge Gauge e solte o Cross Edge.'),
       sources=[NEO('Chapter 3 - Termina Island')])
c.recipe('Meunière Meetup', t('Automatic once the Sandras has a kitchen', 'Automática quando o Sandras ganha cozinha'), sources=[NEO('Chapter 10 - Trophy Cleanup')])
c.recipe('Steak Kickoff Rally', t('Buy from the merchant ship Baudin & Co.', 'Compre no navio mercante Baudin & Co.'), sources=[NEO('Chapter 10 - Trophy Cleanup')])
S3 = [NEO('Chapter 3 - Termina Island'), GF('Chapter 3: Where the Light Leads')]
fish(c, 'Sadina', [(t('Termina Island — entrance', 'Termina Island — entrada'), None)], S3)
fish(c, 'Soldier Crab', [(t('Termina Island — entrance and eastern ledge', 'Termina Island — entrada e borda leste'), 'Fishing Bait S')], S3)
fish(c, 'Saman', [(t('Termina Island — eastern ledge; Viewpoint Isle — pond', 'Termina Island — borda leste; Viewpoint Isle — lago'), 'Fishing Bait M')], S3)
fish(c, 'Marine Amana', [(t('Viewpoint Isle — by the old man; Inlet Isle — beach', 'Viewpoint Isle — perto do velho; Inlet Isle — praia'), 'Fishing Bait S')], S3)
fish(c, 'Ryunga', [(t('Termina Island — cave; Haze Island — hill', 'Termina Island — caverna; Haze Island — colina'), 'Fishing Bait M')], S3)
fish(c, 'Obelia Herring', [(t('Carnac; Balta Island — port', 'Carnac; Balta Island — porto'), 'Fishing Bait S')], S3)
chests(c, ('Fishscale Island', 'Fishscale Island'), [
    ('Red Drop x3', 'Northeast corner', 'Canto nordeste'),
], ('Two buried treasures open in Chapter 5, once you have Mana Sense.',
    'Dois tesouros enterrados abrem no Capítulo 5, quando você tiver o Mana Sense.'), [NEO('Chapter 3 - Fishscale Island')])
chests(c, ('Termina Island', 'Termina Island'), [
    ('Fishing Bait x3', 'Beach: center north, at the top of the hill', 'Praia: centro-norte, no alto da colina'),
    ('Gale Boots', 'East side, across the muddy water with Mana Ride (after Viewpoint Isle)', 'Lado leste, atravessando a água lamacenta com Mana Ride (depois de Viewpoint Isle)'),
    ('Antidote x2', 'Cave: left corner by the shallow water', 'Caverna: canto esquerdo junto à água rasa'),
    ('Sword Seal+', 'Cave: north path at the fork, dead end', 'Caverna: caminho norte na bifurcação, beco sem saída'),
    ("Sea God's Incense", 'Cave: Mana String spot to the left, halfway along the mana stream', 'Caverna: ponto de Mana String à esquerda, no meio do fluxo de mana'),
    ('Sparkling Whitesand x15 (Proud)', 'Cave: just before the exit', 'Caverna: logo antes da saída'),
    ('Basic Craft Stock x25', 'Rear side: jump off the mana stream halfway', 'Lado de trás: pule do fluxo de mana no meio do caminho'),
    ('Mead', 'Rear side: mana stream to the northeast', 'Lado de trás: fluxo de mana a nordeste'),
    ('Fishing Bait S x3', 'Rear side: high spot reached on the way back to the cave', 'Lado de trás: ponto alto alcançado na volta para a caverna'),
    ('Chalice Seal+', 'Second cave: left at the fork, across the puddle', 'Segunda caverna: à esquerda na bifurcação, depois da poça'),
    ('Celadon Clay', 'Second cave: end of the stream at the highest point', 'Segunda caverna: fim do fluxo no ponto mais alto'),
    ('Shield Seal+', 'Second cave: blue chest on the stream to the east', 'Segunda caverna: baú azul no fluxo para o leste'),
    ('Armament Blueprint: Fireball', 'Second cave: red chest behind a gate; press the switch panel by the northwest exit', 'Segunda caverna: baú vermelho atrás de um portão; pise no painel perto da saída noroeste'),
    ('Heartfire Tome', 'Last part: small passage left of the mana stream', 'Última parte: passagem pequena à esquerda do fluxo de mana'),
    ('1000 Gold', 'Last part: below the next ruins', 'Última parte: abaixo das ruínas seguintes'),
], ('Celadon Clay counts for the Sandras Spruce-Up quest in Chapter 4. Seven buried treasures here open in Chapter 5.',
    'A Celadon Clay conta para a quest Sandras Spruce-Up no Capítulo 4. Sete tesouros enterrados aqui abrem no Capítulo 5.'), S3)
chests(c, ('Viewpoint Isle', 'Viewpoint Isle'), [
    ('Luck Elixir', 'Marsh: north side, behind a tree', 'Pântano: lado norte, atrás de uma árvore'),
    ('Sweet Remedy x5', 'South corner, past the ledge to the west side', 'Canto sul, depois da borda para o lado oeste'),
    ('Yellow Strong-Arm+', 'Blue chest midway on the way north to the old man', 'Baú azul no meio do caminho ao norte até o velho'),
], ('Cross the marsh with Mana Ride; falling into the water sends you back.',
    'Atravesse o pântano com o Mana Ride; cair na água leva você de volta.'), S3)

# ======================================================================== Chapter 4
c = chapter(4, 'Chapter 4', 'Capítulo 4')
FOG = c.cp('Following the red marker into the white fog', 'Seguir o marcador vermelho até a névoa branca')
END4 = c.cp('The last event marker of Chapter 4', 'O último marcador de evento do Capítulo 4')
S4 = [GF('Chapter 4: The Whiteshade')]
c.item('quest', t('Sandras Spruce-Up'), t('Sandras — Mirabel on the lower deck', 'Sandras — Mirabel no convés inferior'), FOG,
       t('Long deadline. Hand over Basic Craft Stock ×50, Celadon Clay ×3 and Aged Wood ×3. Afterwards, rest in the Captain\'s Quarters for an event.',
         'Prazo longo. Entregue Basic Craft Stock ×50, Celadon Clay ×3 e Aged Wood ×3. Depois, descanse no Captain\'s Quarters para um evento.'),
       0, [NEO('Chapter 4 - Balta Island')] + S4)
c.item('quest', t('Invaluable Memory'), t('Sandras — Momina; ship southeast of the recaptured island', 'Sandras — Momina; navio a sudeste da ilha retomada'), FOG,
       t('Long deadline. Go to the green marker southeast of the island you recaptured in the Ozmid Expanse and beat the Griegrs on the missing ship. Rewards a Plain Box Lunch (XL) and new stock in her store.',
         'Prazo longo. Vá ao marcador verde a sudeste da ilha retomada em Ozmid Expanse e derrote os Griegrs no navio desaparecido. Dá um Plain Box Lunch (XL) e itens novos na loja dela.'),
       0, [NEO('Chapter 4 - Ozmid Expanse')] + S4)
c.item('quest', t('Many Mappy Returns'), t('Sandras — Dogi at the helm; Great Tidal Reef', 'Sandras — Dogi no timão; Great Tidal Reef'), FOG,
       t('Long deadline. Sail to the far south (Great Tidal Reef), go to the quest marker in the northeast corner, beat the enemies, then report to Dogi.',
         'Prazo longo. Navegue até o extremo sul (Great Tidal Reef), vá ao marcador da quest no canto nordeste, derrote os inimigos e fale com o Dogi.'),
       0, [NEO('Chapter 4 - Ozmid Expanse')] + S4)
c.item('quest', t('Clicking Together'), t('Sandras — Ashley on the deck', 'Sandras — Ashley no convés'), FOG,
       t('Long deadline. Watch the dolphins with the spyglass near the island where Ashley was rescued, then repeat at each new marker. Rewards a Blessed Paper Scrap.',
         'Prazo longo. Observe os golfinhos com a luneta perto da ilha onde a Ashley foi resgatada e repita em cada marcador novo. Dá um Blessed Paper Scrap.'),
       0, [NEO('Chapter 4 - Ozmid Expanse')] + S4)
c.item('quest', t('Treasure Trawl A'), t('Sea chart — orange circle', 'Mapa marítimo — círculo laranja'), FOG,
       t('Long deadline. Starts with Hidden Treasure Chart A (a chest on Anchor Island). Hold the button at the glowing spot in the orange circle. Rewards 3,000 Gold. All six Treasure Trawls lead to a character note later.',
         'Prazo longo. Começa com o Hidden Treasure Chart A (um baú em Anchor Island). Segure o botão no ponto brilhante do círculo laranja. Dá 3.000 Gold. Os seis Treasure Trawls levam a uma nota de personagem mais tarde.'),
       0, [NEO('Chapter 4 - Anchor Island')] + S4)
c.boss(t('Gilveros'), t('Dieback Isle (optional challenge)', 'Dieback Isle (desafio opcional)'),
       t('Level 47 challenge: fine to come back later. Its black gas curses you; keep moving around it and punish its snapping lunges. Rewards a Veteran Necklace.',
         'Desafio de nível 47: dá para voltar depois. O gás negro amaldiçoa; continue se movendo ao redor e castigue as investidas de mordida. Dá um Veteran Necklace.'),
       sources=[NEO('Chapter 4 - Carnac Waters (Optional Content)')] + S4)
c.boss(t('Olcypete'), t('Haze Island'),
       t('Three harpies with one HP bar. Focus one at a time and use Mana String to keep up when they fly over the mud. When all three gather in the center they unleash a howling storm: back away.',
         'Três harpias com uma barra de HP. Foque uma de cada vez e use o Mana String para acompanhar quando voarem sobre a lama. Quando as três se juntam no centro, soltam uma tempestade de uivos: afaste-se.'),
       sources=[NEO('Chapter 4 - Haze Island')] + S4)
c.boss(t('Belladonna'), t('Haze Island — the foggy Carnac, Rusveri Inn', 'Haze Island — a Carnac na névoa, Rusveri Inn'),
       t('She teleports constantly: use Mana Sense to spot her and dash through her chasing blue fireballs. As her HP drops she adds an unguardable grab that can wipe a character: keep your distance while she teleports.',
         'Ela se teleporta o tempo todo: use o Mana Sense para achá-la e use o dash contra as bolas de fogo azuis que perseguem você. Com o HP baixo, ela ganha um agarrão que não pode ser defendido e pode derrubar um personagem: mantenha distância enquanto ela se teleporta.'),
       sources=[NEO('Chapter 4 - Haze Island')] + S4)
for name, src in [('Plain Box Lunch XL', "Reward for Invaluable Memory, or buy the recipe at Momina's store|Recompensa da Invaluable Memory, ou compre a receita na loja da Momina"),
                  ('Fish Fry Box Lunch', 'Report Fishing to Joel after catching 6 kinds of fish|Relate a pesca ao Joel depois de pegar 6 tipos de peixe'),
                  ('Gamey Box Lunch', 'Ozmid Expanse — first island recapture, rank A|Primeira retomada de ilha em Ozmid Expanse, rank A'),
                  ('Shellfish Paella Box Lunch', "Buy at Old Lady Amone's stall, Anchor Island|Compre na barraca da velha Amone, Anchor Island"),
                  ('Clam Chowder Banquet', 'Treasure chest on Haze Island|Baú em Haze Island')]:
    en, pt = src.split('|')
    c.recipe(name, t(en, pt), sources=[NEO('Chapter 10 - Trophy Cleanup')])
S4H = [NEO('Chapter 4 - Haze Island')]
fish(c, 'Salmon', [(t('Balta Island'), 'Fishing Bait')], S4)
fish(c, 'Onyx Tuna', [(t('Open sea — southeast of the recaptured island in Ozmid Expanse', 'Mar aberto — sudeste da ilha retomada em Ozmid Expanse'), 'Fishing Bait G')], [NEO('Chapter 4 - Ozmid Expanse')] + S4)
fish(c, 'Robushu', [(t('Great Tidal Reef; Hidden Isle', 'Great Tidal Reef; Hidden Isle'), 'Fishing Bait S')], S4 + [NEO('Chapter 5 - Sandras')])
fish(c, 'Boleh', [(t('Haze Island — entrance and hill', 'Haze Island — entrada e colina'), 'Fishing Bait S')], S4H)
fish(c, 'North Tuna', [(t('Breezy Isle; Hidden Isle', 'Breezy Isle; Hidden Isle'), 'Fishing Bait L')], S4 + [NEO('Chapter 5 - Sandras')])
fish(c, 'Mud Wells', [(t('Haze Island — entrance', 'Haze Island — entrada'), 'Fishing Bait M')], S4H)
fish(c, 'Purch', [(t('Haze Island — entrance', 'Haze Island — entrada'), 'Fishing Bait M')], S4H)
fish(c, 'Jumpi', [(t('Haze Island — entrance', 'Haze Island — entrada'), 'Fishing Bait EX')], S4H)
fish(c, 'Rowana', [(t('Haze Island — hill', 'Haze Island — colina'), 'Fishing Bait M')], S4H)
S4C = [NEO('Chapter 4 - Carnac Waters (Optional Content)')]
chests(c, ('Inlet Isle', 'Inlet Isle'), [
    ('Xiphoid Bone x3', 'Southwest, next to a Runestone', 'Sudoeste, ao lado de uma Runestone'),
    ('800 Gold', 'Around the open field', 'Pelo campo aberto'),
    ('Yellow Drop x3', 'Southeast corner', 'Canto sudeste'),
], ('The optional event with Lux and Sache sends you back to the ship: return for the southeast chest. Two buried treasures open in Chapter 5.',
    'O evento opcional com o Lux e a Sache leva você de volta ao navio: volte para pegar o baú do sudeste. Dois tesouros enterrados abrem no Capítulo 5.'), S4C)
chests(c, ('Dieback Isle', 'Dieback Isle'), [
    ('Supple Leather x5', 'East side', 'Lado leste'),
    ('Blue Drop x3', 'West cliff, across the muddy water', 'Penhasco oeste, depois da água lamacenta'),
    ('Defense Elixir', 'Red chest behind Gilveros (optional level 47 challenge)', 'Baú vermelho atrás do Gilveros (desafio opcional de nível 47)'),
], ('Gilveros can wait until you are stronger. Three buried treasures open in Chapter 5.',
    'O Gilveros pode esperar até você ficar mais forte. Três tesouros enterrados abrem no Capítulo 5.'), S4C)
S4O = [NEO('Chapter 4 - Ozmid Expanse')]
chests(c, ('Great Tidal Reef', 'Great Tidal Reef'), [
    ('Suzhen Charm', 'On the way to the quest marker in the northeast', 'No caminho até o marcador da quest, no nordeste'),
    ('Repair Kit x3', 'On the way to the quest marker in the northeast', 'No caminho até o marcador da quest, no nordeste'),
], ('Far south of the Ozmid Expanse (Many Mappy Returns). Two buried treasures open in Chapter 5.',
    'No extremo sul de Ozmid Expanse (Many Mappy Returns). Dois tesouros enterrados abrem no Capítulo 5.'), S4O)
chests(c, ('Breezy Isle', 'Breezy Isle'), [
    ('Shield Star', 'Around the island', 'Pela ilha'),
    ("Dvergr's Hammer", "Near the shut-in's tent (gift for Cruz)", 'Perto da barraca do recluso (presente para o Cruz)'),
], ('Westernmost blue marker of the Ozmid Expanse. Two buried treasures open in Chapter 5.',
    'O marcador azul mais a oeste de Ozmid Expanse. Dois tesouros enterrados abrem no Capítulo 5.'), S4O)
chests(c, ('Krangal Island', 'Krangal Island'), [
    ('Extinguisher x3', 'Around the island', 'Pela ilha'),
    ('Sword Star', 'Around the island', 'Pela ilha'),
    ('1000 Gold', 'Inside the mine', 'Dentro da mina'),
], ('Not on the map: sail due west from Breezy Isle.', 'Não aparece no mapa: navegue direto para oeste a partir de Breezy Isle.'), S4O)
chests(c, ('Anchor Island — Village Outskirts', 'Anchor Island — Village Outskirts'), [
    ('Sword Star', 'Detour to the northwest corner', 'Desvio até o canto noroeste'),
    ('Jester Cloak', 'Clifftop in the middle: Mana Ride from the opposite side', 'Topo do penhasco no meio: Mana Ride a partir do lado oposto'),
    ('Repair Kit x3', 'Drop off the cliff before the Mana String spot, by the barrels', 'Desça do penhasco antes do ponto de Mana String, junto aos barris'),
    ('Hidden Treasure Chart A', 'On the water before the event marker: freeze it with Karja, burn the vines with Adol', 'Sobre a água antes do marcador de evento: congele com a Karja e queime as vinhas com o Adol'),
], ('The chart starts Treasure Trawl A. Three buried treasures open in Chapter 5.',
    'O mapa começa a Treasure Trawl A. Três tesouros enterrados abrem no Capítulo 5.'), [NEO('Chapter 4 - Anchor Island')])
chests(c, ('Haze Island', 'Haze Island'), [
    ('Fishing Bait EX x3', 'End of the first path, by a fishing spot', 'Fim do primeiro caminho, junto a um pesqueiro'),
    ('Misericorde', 'Southeast where the path splits', 'Sudeste, onde o caminho se divide'),
    ('Dark Drop x3', "Behind the Druid's Monocle chest", 'Atrás do baú do Druid\'s Monocle', B),
    ('Red Lump x3', 'Near the first fishing spot', 'Perto do primeiro pesqueiro', B),
    ('Armor Seal+', 'Along the hill', 'Ao longo da colina', B),
    ('Sin Seal', 'Along the hill', 'Ao longo da colina', B),
    ('1500 Gold', 'Just past the gate (open it with Mana Sense)', 'Logo depois do portão (abra com o Mana Sense)', B),
    ('Beastwing Battle-Axe', "Blue chest at the top of the Mana String spot (Karja's weapon)", 'Baú azul no alto do ponto de Mana String (arma da Karja)'),
    ('Blue Lump x3', 'Appears after the boss', 'Aparece depois do chefe', B),
    ('Punishment Seal', 'Back half: first dead end', 'Metade de trás: primeiro beco sem saída', B),
    ('Armor Star', 'Back half: behind the nearest breakable boulder', 'Metade de trás: atrás da rocha quebrável mais próxima'),
    ('Lyre Seal+', 'Back half: past the next boulder', 'Metade de trás: depois da rocha seguinte', B),
    ('Sedative x3', 'Back half: boulder to the southwest', 'Metade de trás: rocha a sudoeste'),
    ('Aurora Cloak', 'Back half: boulder to the northwest, in a corner', 'Metade de trás: rocha a noroeste, num canto'),
    ('Luncheon Recipe: Chowder', 'Back half: boulder to the southeast', 'Metade de trás: rocha a sudeste'),
    ('Strength Elixir', 'Back half: open area to the north', 'Metade de trás: área aberta ao norte', B),
], ('Buried treasures open with Mana Sense, which you learn on Viewpoint Isle partway through the island. One red chest in the back half only opens in Chapter 9.',
    'Os tesouros enterrados abrem com o Mana Sense, que você aprende em Viewpoint Isle no meio da ilha. Um baú vermelho na metade de trás só abre no Capítulo 9.'), S4H)
chests(c, ('Viewpoint Isle — the cave', 'Viewpoint Isle — a caverna'), [
    ('Crystal Shard x500', 'Under the tree', 'Embaixo da árvore', B),
    ("Tactician's Earrings", 'Southwest, across the invisible platforms', 'Sudoeste, depois das plataformas invisíveis'),
    ('Yellow Lump x3', 'Southwest, same spot', 'Sudoeste, no mesmo ponto', B),
    ("Ascetic's Arcanum", 'North platforms, left branch', 'Plataformas ao norte, ramo da esquerda'),
    ('Sweet Remedy x5', 'North platforms, right branch', 'Plataformas ao norte, ramo da direita'),
    ('Fishing Bait M x5', 'Northeast section', 'Seção nordeste', B),
    ('Chalice Star', 'Northeast, a little further', 'Nordeste, um pouco adiante'),
    ('Break Elixir', 'Northernmost point', 'Ponto mais ao norte', B),
], ('Equip the Eagle Eye Doubloon (Report Adventures) so buried treasures show on the map while Mana Sense lasts. Use Mana Sense on the eye engravings to reveal the platforms.',
    'Equipe o Eagle Eye Doubloon (Report Adventures) para os tesouros enterrados aparecerem no mapa enquanto o Mana Sense durar. Use o Mana Sense nos entalhes de olho para revelar as plataformas.'), S4H)

# ======================================================================== Chapter 5
c = chapter(5, 'Chapter 5', 'Capítulo 5')
ISAAC = c.cp('Talking to Chief Isaac in Ilmer Village', 'Falar com o Chief Isaac em Ilmer Village')
WHALE = c.cp('Approaching the event marker after the fight on Moonview Isle', 'Aproximar-se do marcador de evento depois da luta em Moonview Isle')
END5 = c.cp('The last event marker of Chapter 5', 'O último marcador de evento do Capítulo 5')
END7 = 'ysx-ch7-cp-03'  # Chapter 7's last checkpoint (created further down)
S5 = [GF('Chapter 5: Beacon of Reprisal')]
S5S = [NEO('Chapter 5 - Sandras')]
c.item('missable', t("Momina's character note #1", 'Nota de personagem da Momina #1'), t('Sandras — lower deck', 'Sandras — convés inferior'), ISAAC,
       t('One of only three time-limited character notes. After the fight in Ilmer Village, before talking to the village elder, go back to the ship and talk to Momina and Rafe on the lower deck. Missing it blocks the all-notes trophy.',
         'Uma das três únicas notas de personagem com tempo limitado. Depois da luta em Ilmer Village, antes de falar com o ancião da vila, volte ao navio e fale com a Momina e o Rafe no convés inferior. Perder impede o troféu de todas as notas.'),
       0, [NEO('Chapter 5 - Falun Island')])
c.item('missable', t("Hugill's character note #1", 'Nota de personagem do Hugill #1'), t('Raufos Island — next to the Hewnstone', 'Raufos Island — ao lado da Hewnstone'), END7,
       t('Time-limited character note. Right after arriving on Raufos Island, talk to Hugill standing beside the Hewnstone with a bag. If you miss it, there is one more chance in Chapter 7: talk to him at the Dvergr Coast camp after the Falaise Runestone.',
         'Nota de personagem com tempo limitado. Logo ao chegar a Raufos Island, fale com o Hugill, parado ao lado da Hewnstone com uma bolsa. Se perder, há mais uma chance no Capítulo 7: fale com ele no acampamento da Dvergr Coast depois da Runestone de Falaise.'),
       0, [NEO('Chapter 5 - Raufos Island'), NEO('Chapter 7 - Falaise Peninsula')])
c.item('quest', t('Barrels of Unfun'), t('Anchor Island — Ivalde in Mynorca Village', 'Anchor Island — Ivalde em Mynorca Village'), ISAAC,
       t('Long deadline. Sail to every green marker at sea and destroy the explosive barrels, then report to Ivalde. Rewards a Pirate\'s Necklace, plus an Axe Star+ and a Vitality Elixir.',
         'Prazo longo. Navegue até cada marcador verde no mar e destrua os barris explosivos, depois fale com a Ivalde. Dá um Pirate\'s Necklace, além de um Axe Star+ e um Vitality Elixir.'),
       0, S5S + S5)
c.item('quest', t('Peerless Practice'), t('The Norgest — northeast of the Ozmid Expanse', 'O Norgest — nordeste de Ozmid Expanse'), ISAAC,
       t("Long deadline. From Gunnar's letter. Pick the first option on his ship and win the duel. Rewards the Brave General's Belt.",
         'Prazo longo. Vem da carta do Gunnar. Escolha a primeira opção no navio dele e vença o duelo. Dá o Brave General\'s Belt.'),
       0, S5S + S5)
c.item('quest', t('Cull the Griegr: Lecto'), t('Lecto Island — Cavern Depths', 'Lecto Island — Cavern Depths'), ISAAC,
       t('Long deadline. Added automatically. Fast travel to the Cavern Depths and beat the two knight-type Griegrs. Rewards the Martial Formula.',
         'Prazo longo. Entra sozinha no diário. Viaje até a Cavern Depths e derrote os dois Griegrs do tipo cavaleiro. Dá a Martial Formula.'),
       0, S5S + S5)
c.item('quest', t('EX: Öland Island Investigation (Proud)', 'EX: Öland Island Investigation (Proud)'), t('Öland Island — north of the center of Carnac Waters', 'Öland Island — ao norte do centro de Carnac Waters'), None,
       t('Proud Nordics only. Read Hugill\'s letter "EX: Suspicious Ship", sail to the blue point north of the center of Carnac Waters and clear Blindman\'s Darkroad. Rewards Abiding Love and an Almighty Star. The guide gives no deadline: do it in this chapter to be safe.',
         'Só no Proud Nordics. Leia a carta do Hugill "EX: Suspicious Ship", navegue até o ponto azul ao norte do centro de Carnac Waters e termine o Blindman\'s Darkroad. Dá Abiding Love e um Almighty Star. O guia não informa prazo: faça neste capítulo por segurança.'),
       0, [NEO('Chapter 5 - Öland Island (Proud Only)'), NEO('Chapter 5 - Buried Treasure')])
c.item('collectible', t("Astrid's character note #1 (Proud)", 'Nota de personagem da Astrid #1 (Proud)'), t('Öland Island — coliseum', 'Öland Island — coliseu'), None,
       t('Proud Nordics only. After the Darkroad, talk to Astrid at the coliseum; this also opens the coliseum challenges. Character notes count for the all-notes trophy.',
         'Só no Proud Nordics. Depois do Darkroad, fale com a Astrid no coliseu; isso também libera os desafios do coliseu. As notas de personagem contam para o troféu de todas as notas.'),
       0, [NEO('Chapter 5 - Öland Island (Proud Only)')])
c.item('collectible', t('Öland coliseum — unique rewards (Proud)', 'Coliseu de Öland — recompensas únicas (Proud)'), t('Öland Island — coliseum', 'Öland Island — coliseu'), None,
       t('Proud Nordics only. Three sets (duo, Adol alone, Karja alone) against Solid Boar, Brugand, Ras-Gublins and Gilveros. Most rewards are materials, Elding Fragments and Sparkling Whitesand; these are the one-offs.',
         'Só no Proud Nordics. Três séries (dupla, só o Adol, só a Karja) contra Solid Boar, Brugand, Ras-Gublins e Gilveros. A maioria das recompensas são materiais, Elding Fragments e Sparkling Whitesand; estas são as únicas.'),
       0, [NEO('Chapter 5 - Öland Island (Proud Only)')],
       steps=[t('Duo — Solid Boar: Chibi Pikkard', 'Dupla — Solid Boar: Chibi Pikkard'),
              t('Adol — Solid Boar: Ancient Trove Chart 1', 'Adol — Solid Boar: Ancient Trove Chart 1'),
              t('Adol — Gilveros: Ancient Trove Chart 4', 'Adol — Gilveros: Ancient Trove Chart 4'),
              t('Karja — Solid Boar: Phylleia Noggin', 'Karja — Solid Boar: Phylleia Noggin'),
              t('Karja — Gilveros: Chibi Hugill 2', 'Karja — Gilveros: Chibi Hugill 2'),
              t('Brugand (any set): Fleeting Hope', 'Brugand (qualquer série): Fleeting Hope')])
c.boss(t('Gunnar'), t('The Norgest — northeast of the Ozmid Expanse', 'O Norgest — nordeste de Ozmid Expanse'),
       t('Wide spear sweeps, a charged thrust and a charged ground slam. After half HP he leaps and dives with his spear: dodge away when he jumps.',
         'Golpes amplos de lança, uma estocada carregada e uma pancada no chão carregada. Depois da metade do HP, ele salta e mergulha com a lança: afaste-se quando ele pular.'),
       related='ysx-ch5-q-02', sources=S5S + S5)
c.boss(t("Blindman's Darkroad boss (Proud)", 'Chefe do Blindman\'s Darkroad (Proud)'), t('Öland Island — end of the Darkroad', 'Öland Island — fim do Darkroad'),
       t('Proud Nordics only. Level 36 with about 93,000 HP, far more than the other bosses of this chapter: stock up at the Hewnstone right before it and bring plenty of healing.',
         'Só no Proud Nordics. Nível 36 com cerca de 93.000 de HP, bem mais que os outros chefes do capítulo: abasteça na Hewnstone logo antes e leve bastante cura.'),
       related='ysx-ch5-q-04', sources=[NEO('Chapter 5 - Öland Island (Proud Only)')])
c.boss(t('Volgadyne R'), t('Odd Rock Isle (optional challenge)', 'Odd Rock Isle (desafio opcional)'),
       t('Level 72 but slow: dash behind it and keep hitting until the Revenge Gauge is ready. Rewards a Veteran Seal and opens the last chest of the island.',
         'Nível 72, mas lento: passe por trás com o dash e continue batendo até o Revenge Gauge ficar pronto. Dá um Veteran Seal e libera o último baú da ilha.'),
       sources=[NEO('Chapter 6 - Sonnelia Basin'), GF("Chapter 6: Heaven's Mirror")])
c.boss(t('Gang'), t('Kalon Island — third area', 'Kalon Island — terceira área'),
       t('A bigger cousin of Iði: watch for the crouch before its jump attack, and its war cry only knocks you back. Guard its overhead punch.',
         'Um primo maior do Iði: observe o agachamento antes do ataque com salto; o grito de guerra só empurra você. Defenda o soco de cima para baixo.'),
       sources=[NEO('Chapter 5 - Falun Island')])
c.boss(t('Blob Jurion'), t('Moonview Isle'),
       t('Poison gas below it, electric orbs and tentacle slams; Duo Guard its leaping slam. Breaking its durability exposes faster pincers, and it burrows to strike from below. At the end it splits into small laser jellyfish: a few combos clear them.',
         'Gás venenoso embaixo dele, orbes elétricos e golpes de tentáculo; use a Duo Guard contra a pancada com salto. Quebrar a resistência expõe pinças mais rápidas, e ele se enterra para atacar por baixo. No fim, ele se divide em águas-vivas pequenas que soltam laser: alguns combos resolvem.'),
       sources=[NEO('Chapter 5 - Raufos Island')] + S5)
c.boss(t('Jörð'), t('Raufos Island — the fort roof', 'Raufos Island — telhado do forte'),
       t('Duo guard her red sword combo. After her durability breaks she gets faster: in her four-slash red frenzy guard every hit for a counter, and retreat when she charges blue. She also throws claw missiles.',
         'Use a defesa em dupla contra o combo da espada vermelha. Quando a resistência quebra, ela fica mais rápida: no frenesi vermelho de quatro golpes, defenda cada um para contra-atacar, e recue quando ela carregar em azul. Ela também lança garras como projéteis.'),
       sources=[NEO('Chapter 5 - Raufos Island')] + S5)
for name in ['Stimulative Box Lunch', 'Sedating Box Lunch', 'Antidotal Box Lunch', 'Relaxative Box Lunch']:
    c.recipe(name, t("Order one at The Seagull's Shanty, Ilmer Village", "Peça um na The Seagull's Shanty, Ilmer Village"), sources=[NEO('Chapter 10 - Trophy Cleanup')])
S5F = [NEO('Chapter 5 - Falun Island')]
S5P = [NEO('Chapter 5 - Öland Island (Proud Only)')]
fish(c, 'Blue Saddie', [(t('Falun Island — shore and river', 'Falun Island — margem e rio'), 'Fishing Bait S')], S5F)
fish(c, 'Glass Corp', [(t('Falun Island — river', 'Falun Island — rio'), 'Fishing Bait M')], S5F)
fish(c, 'Mercenary Crab', [(t('Viewpoint Isle — by the Hewnstone; Ilmer Village — dock', 'Viewpoint Isle — junto à Hewnstone; Ilmer Village — doca'), 'Fishing Bait M')], S5F)
fish(c, 'Sunny Saman', [(t('Ilmer Village — dock', 'Ilmer Village — doca'), 'Fishing Bait L')], S5F)
fish(c, 'Kily (Proud)', [(t('Öland Island — west river', 'Öland Island — rio a oeste'), 'Fishing Bait S')], S5P)
fish(c, 'Hermia (Proud)', [(t("Öland Island — Blindman's Darkroad, pitch-black room", "Öland Island — Blindman's Darkroad, sala escura"), 'Fishing Bait')], S5P)
S5B = [NEO('Chapter 5 - Buried Treasure'), GF('Chapter 3: Where the Light Leads')]
chests(c, ('Carnac Waters', 'Carnac Waters'), [
    ('Dark Lump x3', 'Fishscale Island — southwest of the Red Drop chest, by the central rocks', 'Fishscale Island — sudoeste do baú do Red Drop, nas rochas centrais', B),
    ('Shell Rock x3', 'Fishscale Island — northwest corner', 'Fishscale Island — canto noroeste', B),
    ('650 Gold', 'Lecto Island', 'Lecto Island', B),
    ('Rainbow Drop x3', 'Lecto Island', 'Lecto Island', B),
    ('Shield Star', 'Lecto Island — Cavern of Rite', 'Lecto Island — Cavern of Rite', B),
    ('Black Strong-Arm', 'Lecto Island — Cavern of Rite', 'Lecto Island — Cavern of Rite', B),
    ('800 Gold', 'Termina Island — up the first hill, under a tree by the wall ruins', 'Termina Island — no alto da primeira colina, embaixo de uma árvore junto às ruínas', B),
    ('Dark Drop x5', 'Termina Island — north of it, also under a tree', 'Termina Island — ao norte dele, também embaixo de uma árvore', B),
    ('Rainbow Drop x5', 'Termina Island — cave, near the end before going outside', 'Termina Island — caverna, perto do fim antes de sair', B),
    ('Axe Star', 'Termina Island — rear side, behind the Basic Craft Stock chest', 'Termina Island — lado de trás, atrás do baú do Basic Craft Stock', B),
    ('Empty Lunch Box', 'Termina Island — end of the mana ride, tree to the right', 'Termina Island — fim do mana ride, árvore à direita', B),
    ('Lyre Star', 'Termina Island — after the second cave, by the wall ruins', 'Termina Island — depois da segunda caverna, junto às ruínas', B),
    ('Fishing Bait S x5', 'Termina Island — last part, between the two chests', 'Termina Island — última parte, entre os dois baús', B),
    ('Tough Leather x3', 'Inlet Isle', 'Inlet Isle', B),
    ('Blue Drop x10', 'Inlet Isle', 'Inlet Isle', B),
    ('Aged Wood x5', 'Dieback Isle', 'Dieback Isle', B),
    ('Red Drop x10', 'Dieback Isle', 'Dieback Isle', B),
    ('Fishing Bait x3', 'Dieback Isle', 'Dieback Isle', B),
], ('First chance: they all need Mana Sense, learned at the end of Chapter 4. Equip the Eagle Eye Doubloon to see them on the map. On Termina Island, a Silver Pikkard hides in a muddy puddle (visible with Mana Sense).',
    'Primeira chance: todos precisam do Mana Sense, aprendido no fim do Capítulo 4. Equipe o Eagle Eye Doubloon para vê-los no mapa. Em Termina Island, um Silver Pikkard se esconde numa poça de lama (visível com o Mana Sense).'),
    S5B, title=('Buried treasures in Carnac Waters', 'Tesouros enterrados em Carnac Waters'))
chests(c, ('Ozmid Expanse', 'Ozmid Expanse'), [
    ('Fishing Bait S x3', 'Great Tidal Reef', 'Great Tidal Reef', B),
    ('Chalice Star', 'Great Tidal Reef', 'Great Tidal Reef', B),
    ('Yellow Drop x10', 'Breezy Isle', 'Breezy Isle', B),
    ('Strength Elixir', 'Breezy Isle', 'Breezy Isle', B),
    ('Dark Drop x5', 'Anchor Island — Village Outskirts', 'Anchor Island — Village Outskirts', B),
    ('1250 Gold', 'Anchor Island — Village Outskirts', 'Anchor Island — Village Outskirts', B),
    ('Punishment Seal+', 'Anchor Island — Village Outskirts', 'Anchor Island — Village Outskirts', B),
], ('First chance: they need Mana Sense, learned at the end of Chapter 4.',
    'Primeira chance: precisam do Mana Sense, aprendido no fim do Capítulo 4.'),
    [NEO('Chapter 5 - Buried Treasure')], title=('Buried treasures in the Ozmid Expanse', 'Tesouros enterrados em Ozmid Expanse'))
chests(c, ('Hidden Isle', 'Hidden Isle'), [
    ('Fishing Bait G x3', 'Hill to the northwest', 'Colina a noroeste'),
    ('Basic Beast Parts x50', 'To the right of it', 'À direita dele', B),
    ('Steely Bone x3', 'Northeast past the puddle, by a tree', 'Nordeste depois da poça, junto a uma árvore', B),
    ('Defroster x3', 'Further north: climb the ledge and swing with Mana String', 'Mais ao norte: suba a borda e balance com o Mana String'),
    ('2000 Gold', 'By the tree to the north', 'Junto à árvore ao norte', B),
    ('Mayura Charm', 'Blue chest on the ledge left of the big pond', 'Baú azul na borda à esquerda do lago grande'),
    ('Bitter Remedy', 'Ledge to the southeast', 'Borda a sudeste', B),
    ('Repair Kit x3', 'Southeast, by the cliff edge', 'Sudeste, na beira do penhasco', B),
    ('Luck Elixir', 'West, up another ledge', 'Oeste, subindo outra borda', B),
], ('Reached with the Mana Barrier: southeast blue marker of the Ozmid Expanse. A Speedy Pikkard runs around the island.',
    'Acessada com a Mana Barrier: marcador azul a sudeste de Ozmid Expanse. Um Speedy Pikkard corre pela ilha.'), S5S)
chests(c, ('Öland Island (Proud)', 'Öland Island (Proud)'), [
    ('Basic Beast Parts x35', 'Below the cliff after the first mana stream', 'Embaixo do penhasco depois do primeiro fluxo de mana', B),
    ('Sword Star', 'Left side, a little higher up', 'Lado esquerdo, um pouco mais acima'),
    ('Shell Rock x3', 'Right side', 'Lado direito'),
    ('Red Crest', 'Outer edge of the coliseum', 'Borda externa do coliseu'),
    ('Crystal Shard x500', 'Outer edge of the coliseum', 'Borda externa do coliseu'),
    ('Luck Elixir', 'Storage room near the coliseum (spends the Red Crest)', 'Depósito perto do coliseu (gasta o Red Crest)'),
    ('Dominative Star', "Storage house next to the coliseum (Small Steel Key from the Darkroad)", 'Casa de depósito ao lado do coliseu (Small Steel Key do Darkroad)'),
], ('Proud Nordics only. You get one Red Crest here: spend it on the coliseum storage room (Luck Elixir) or on the red door in Blindman\'s Darkroad (Sin Star+); the other one waits for a later visit. Another storeroom has chests that cannot be opened yet. Cutting the glowing flowers gives Sparkling Whitesand.',
    'Só no Proud Nordics. Você ganha um Red Crest aqui: gaste no depósito do coliseu (Luck Elixir) ou na porta vermelha do Blindman\'s Darkroad (Sin Star+); a outra fica para uma visita futura. Outro depósito tem baús que ainda não abrem. Cortar as flores brilhantes dá Sparkling Whitesand.'), S5P)
chests(c, ("Blindman's Darkroad (Proud)", "Blindman's Darkroad (Proud)"), [
    ('1500 Gold', 'Second room, by the water near the vines', 'Segunda sala, junto à água perto das vinhas'),
    ('Sin Star+', 'Red-crest door in the next room', 'Porta do brasão vermelho na sala seguinte'),
    ('Basic Ingredients x50', 'Next to that door', 'Ao lado dessa porta'),
    ('Armor Star', 'South split, west room up the steps', 'Divisão ao sul, sala oeste subindo os degraus'),
    ('Elding Fragment x10', "Dark east room, at the top (light the lanterns with Adol's Mana Burst)", 'Sala escura a leste, no alto (acenda as lanternas com o Mana Burst do Adol)'),
    ('Yellow Lump x3', 'Next area, around the middle', 'Área seguinte, perto do meio', B),
    ('Basic Craft Stock x50', 'Following hallway', 'Corredor seguinte', B),
    ('Small Steel Key', 'Red chest up the climb', 'Baú vermelho no alto da subida'),
    ('Super Relaxant x2', 'Next room', 'Sala seguinte'),
    ('Sparkling Whitesand x20', 'Room to the right', 'Sala à direita'),
    ('Rainbow Drop x5', 'Corner of the following area', 'Canto da área seguinte', B),
    ('Basic Reagents x40', 'Pitch-black room, around the middle', 'Sala totalmente escura, perto do meio', B),
], ('Proud Nordics only. Open the tower gate on Öland Island with the Obsidian Key from the coliseum fight.',
    'Só no Proud Nordics. Abra o portão da torre em Öland Island com a Obsidian Key da luta no coliseu.'), S5P)
chests(c, ('Falun Island', 'Falun Island'), [
    ('Sword Star+', 'North end of the shore', 'Extremo norte da margem', B),
    ('Melg Flower x3', 'South, detour east to the cliffs', 'Sul, desvio a leste até os penhascos'),
    ('Rainbow Drop x3', 'Southwest corner', 'Canto sudoeste', B),
    ('Scoundrel Gloves', 'Across the river logs to the northeast: jump to the last log and burn the vines with Adol in midair', 'Do outro lado dos troncos no rio, a nordeste: pule até o último tronco e queime as vinhas com o Adol no ar'),
    ('Green Turban Ear Clips', 'Northwest end before the village exit (gift for Rosalind)', 'Extremo noroeste antes da saída para a vila (presente para a Rosalind)'),
], ('The Scoundrel Gloves chest is meant for a later ability, but the midair Mana Burst trick reaches it now.',
    'O baú das Scoundrel Gloves é pensado para uma habilidade futura, mas o truque do Mana Burst no ar já alcança agora.'), S5F)
chests(c, ('Viewpoint Isle — south', 'Viewpoint Isle — sul'), [
    ('Crystal Shard x750', 'By the Hewnstone', 'Junto à Hewnstone', B),
    ('Bitter Remedy x3', 'Center, before the stream', 'Centro, antes do riacho'),
    ('Fishing Bait G x3', 'East section, upper spot', 'Seção leste, ponto de cima', B),
    ('Break Elixir', 'East section, lower spot', 'Seção leste, ponto de baixo', B),
    ('Fishing Bait L x3', 'East section, on top of the middle pillars', 'Seção leste, em cima dos pilares do meio'),
    ('Defense Elixir', 'Far east end', 'Extremo leste'),
    ("Hermit's Remedy", 'West of the stream, halfway', 'A oeste do riacho, no meio do caminho'),
    ('Shield Star+', 'Southwest', 'Sudoeste', B),
], ('Opens after the stone tablet in the cave, with Enhanced Mana Sense (hold the button).',
    'Abre depois da tábua de pedra na caverna, com o Enhanced Mana Sense (segure o botão).'), S5F)
chests(c, ('Kalon Island', 'Kalon Island'), [
    ('Basic Beast Parts x50', 'Below the cliffs near the start', 'Embaixo dos penhascos perto do início', B),
    ('Fighter Helmet', 'Blue chest at the south end of the river', 'Baú azul no extremo sul do rio'),
    ('Armor Star+', 'Northwest corner', 'Canto noroeste', B),
    ('Relaxant x3', 'Northwest corner', 'Canto noroeste'),
    ('Blue Lump x3', 'Northern corner', 'Canto norte', B),
    ('2500 Gold', 'Ledge to the southwest, before the drawbridge', 'Borda a sudoeste, antes da ponte levadiça'),
    ('2000 Gold', 'Second area: grass patch', 'Segunda área: trecho de grama', B),
    ('Mason Medal', 'Second area: crystal path to the left', 'Segunda área: caminho de cristais à esquerda'),
    ('Vitality Elixir', 'Second area: lower water path, midway', 'Segunda área: caminho de água de baixo, no meio', B),
    ('Blessed Paper Scrap', 'Second area: red chest at the end of the lower path', 'Segunda área: baú vermelho no fim do caminho de baixo'),
    ('Fishing Bait M x5', 'Second area: lower ground past the bridge', 'Segunda área: parte baixa depois da ponte'),
    ('Chalice Star+', 'Third area: by a tree after the fight', 'Terceira área: junto a uma árvore depois da luta', B),
    ('Holy Formula II', 'Third area: south path at the split', 'Terceira área: caminho sul na divisão'),
], ('Rune Tablet Part Two (red chest, northeast) is needed to move on, so it is not listed.',
    'A Rune Tablet Part Two (baú vermelho, nordeste) é necessária para avançar, por isso não está na lista.'), S5F)
S5O = [NEO('Chapter 6 - Sonnelia Basin')]
chests(c, ('Odd Rock Isle', 'Odd Rock Isle'), [
    ('Relaxant x3', 'North, before climbing the ledges', 'Norte, antes de subir as bordas', B),
    ('Extinguisher x3', 'Northeast end', 'Extremo nordeste'),
    ('Fishing Bait M x3', 'Northwest, on the higher rocks', 'Noroeste, nas rochas mais altas', B),
    ('Basic Craft Stock x50', 'Further northwest, past a Mana String gap', 'Mais a noroeste, depois de um vão com Mana String', B),
    ('1850 Gold', 'Southwest corner', 'Canto sudoeste'),
    ('Axe Star+', 'South: beat the challenge enemy Volgadyne R first', 'Sul: derrote antes o inimigo desafio Volgadyne R'),
], ('Not marked on the map: northwest of Falun Island. The guides come here at the start of Chapter 6, but the Sonnelia Basin can already be explored late in Chapter 5, once Ilmer Village is freed.',
    'Não aparece no mapa: a noroeste de Falun Island. Os guias vêm aqui no começo do Capítulo 6, mas a Sonnelia Basin já pode ser explorada no fim do Capítulo 5, depois que Ilmer Village é libertada.'), S5O)
chests(c, ('Outcast Isle', 'Outcast Isle'), [
    ('Fishing Bait x5', 'Right side of the map', 'Lado direito do mapa', B),
    ('Raiju Charm', 'Right side of the map', 'Lado direito do mapa'),
], ('Southeast of the merchant ship Thrúd\'s Barge in the Sonnelia Basin. Same timing note as Odd Rock Isle.',
    'A sudeste do navio mercante Thrúd\'s Barge na Sonnelia Basin. Mesma observação de tempo de Odd Rock Isle.'), S5O)
chests(c, ('Moonview Isle', 'Moonview Isle'), [
    ('Battle-Tested Talisman', 'Around the boss arena', 'Ao redor da arena do chefe'),
    ('Empty Bottle', 'Around the boss arena', 'Ao redor da arena do chefe', B),
    ('Fishing Bait EX x3', 'Around the boss arena', 'Ao redor da arena do chefe', B),
], ('Grab them before walking to the event marker: it moves the story on and you can only come back next chapter.',
    'Pegue antes de ir ao marcador de evento: ele avança a história e você só volta no próximo capítulo.'), [NEO('Chapter 5 - Raufos Island')])
chests(c, ('Raufos Island', 'Raufos Island'), [
    ('Break Elixir', 'On the ledge at the start', 'Na borda do início', B),
    ('Gwyllgi Charm', 'Blue chest behind the Hewnstone', 'Baú azul atrás da Hewnstone'),
    ('Extinguisher x3', 'To the right, before the wooden ledge', 'À direita, antes da borda de madeira', B),
    ('Basic Craft Stock x75', 'Detour south before the fort', 'Desvio ao sul antes do forte'),
    ('Heal Potion III', 'Fort: red chest at the bottom of the stairs, guarded by a spear mini-boss', 'Forte: baú vermelho no pé da escada, guardado por um mini-chefe de lança'),
    ("Warrior's Glove", 'Outer yard: blue chest to the right', 'Pátio externo: baú azul à direita'),
    ('3000 Gold', 'Outer yard', 'Pátio externo', B),
    ('Lyre Star+', 'Outer yard', 'Pátio externo', B),
    ('Spirit Charm', 'By the gate', 'Junto ao portão'),
    ('Dark Drop x5', 'West side', 'Lado oeste', B),
    ('Sin Seal+', 'Northeast, via the gondola', 'Nordeste, pela gôndola'),
    ('Repair Kit x5', 'South end (pull the crate with Mana String)', 'Extremo sul (puxe o caixote com o Mana String)'),
    ('Fishing Bait G x3', 'Second half of the fort, to the left', 'Segunda metade do forte, à esquerda'),
    ('Peculiar Hárr Woodcarving', 'Red chest at the south end (gift for Karja)', 'Baú vermelho no extremo sul (presente para a Karja)'),
    ('Barriermancy Text', 'Outside, under the wooden bridge before the roof', 'Lado de fora, embaixo da ponte de madeira antes do telhado'),
], ('Talk to Hugill by the first Hewnstone here for his time-limited character note.',
    'Fale com o Hugill junto à primeira Hewnstone daqui para a nota de personagem com tempo limitado.'), [NEO('Chapter 5 - Raufos Island')])

# ======================================================================== Chapter 6
c = chapter(6, 'Chapter 6', 'Capítulo 6')
BAY = c.cp('Sailing into Specular Bay at the red marker past Fuling Island', 'Entrar em Specular Bay pelo marcador vermelho depois de Fuling Island')
END6 = c.cp('The last event marker of Chapter 6', 'O último marcador de evento do Capítulo 6')
S6 = [GF("Chapter 6: Heaven's Mirror")]
S6S = [NEO('Chapter 6 - Sonnelia Basin')]
S6B = [NEO('Chapter 6 - Specular Bay')]
c.item('quest', t('Fellowship with Flavor'), t('Sandras — Rosalind on the mast', 'Sandras — Rosalind no mastro'), BAY,
       t('SHORT deadline and easy to miss. It appears once Cohen, Father Cuthbert and Milette are rescued (Milette comes from the Southern Fort recapture), so it can show up already late in Chapter 5. Get the item from Magni on Balta Island\'s shore and bring it to Rosalind before the story moves on.',
         'Prazo CURTO e fácil de perder. Aparece quando o Cohen, o Father Cuthbert e a Milette estão resgatados (a Milette vem da retomada do Southern Fort), então pode surgir já no fim do Capítulo 5. Pegue o item com o Magni na praia de Balta Island e leve à Rosalind antes de a história avançar.'),
       0, S6S + S6)
c.item('quest', t('Foraging Ahead'), t('Balta Island — Gunhilda in Balta Village', 'Balta Island — Gunhilda em Balta Village'), BAY,
       t('Medium deadline. Collect Fly Agarics (Anchor Island — Village Outskirts, bottom center), Henbane Blossoms (Lecto Island beach, northeast corner) and Bellflowers (Kalon Island mountain peak, near the start).',
         'Prazo médio. Colete Fly Agarics (Anchor Island — Village Outskirts, centro de baixo), Henbane Blossoms (praia de Lecto Island, canto nordeste) e Bellflowers (pico de Kalon Island, perto do início).'),
       0, S6S + S6)
c.item('quest', t('Slay the Beasts: Kalon'), t('Kalon Island — second area, before the drawbridge', 'Kalon Island — segunda área, antes da ponte levadiça'), BAY,
       t('Long deadline. Added automatically. Several waves of beasts; dash through their speed attacks or Duo Guard their power attacks for big counters. Rewards a Gwyllgi Amulet.',
         'Prazo longo. Entra sozinha no diário. Várias ondas de feras; use o dash contra os ataques rápidos ou a Duo Guard contra os poderosos para grandes contra-ataques. Dá um Gwyllgi Amulet.'),
       0, S6S + S6)
c.item('quest', t('Fun in the Sunfish'), t('Sandras — Ashley on the deck', 'Sandras — Ashley no convés'), BAY,
       t('Long deadline. Use the spyglass at both green markers in the Sonnelia Basin, talk to Ashley, then visit the northernmost of the three new markers.',
         'Prazo longo. Use a luneta nos dois marcadores verdes da Sonnelia Basin, fale com a Ashley e depois visite o mais ao norte dos três marcadores novos.'),
       0, S6S + S6)
c.item('quest', t('Treasure Trawl B'), t("Sea chart — chart from Gregorio's Curio", "Mapa marítimo — mapa do Gregorio's Curio"), BAY,
       t("Long deadline. Buy Hidden Treasure Chart B from Gregorio's Curio and salvage the glowing spot. Rewards the Foreign Gauntlet (gift for Dogi).",
         'Prazo longo. Compre o Hidden Treasure Chart B no Gregorio\'s Curio e resgate o ponto brilhante. Dá a Foreign Gauntlet (presente para o Dogi).'),
       0, S6S + S6)
c.item('quest', t('Going for Gold'), t('Fuling Island — the cave at night', 'Fuling Island — a caverna à noite'), BAY,
       t('Long deadline. Appears when you return to Fuling Island after its event. Accepting turns it to night; several mini-bosses wait at the far end of the cave. Rewards a Holy Potion II.',
         'Prazo longo. Aparece quando você volta a Fuling Island depois do evento dela. Aceitar faz anoitecer; vários mini-chefes esperam no fundo da caverna. Dá uma Holy Potion II.'),
       0, S6S + S6)
c.item('quest', t('Pikkard Coral'), t('Sprout Atoll'), END6,
       t('Long deadline. The mysterious old man asks you to catch his scattered pikkards at the green markers; for the one near the water, mana ride toward it and jump at the right moment. Rewards a Pickaback Pikkard (White).',
         'Prazo longo. O velho misterioso pede para você pegar os pikkards espalhados nos marcadores verdes; para o que está perto da água, deslize até ele e pule na hora certa. Dá um Pickaback Pikkard (White).'),
       0, S6B + S6)
c.item('quest', t('Treasure Trawl C'), t('Sonnelia Basin — south, orange circle', 'Sonnelia Basin — sul, círculo laranja'), END6,
       t("Long deadline. Hidden Treasure Chart C comes from the Southern Castle recapture at rank C or better. Avoid the invulnerable Blade Shark. Rewards the Dancer's Shawl.",
         'Prazo longo. O Hidden Treasure Chart C vem da retomada do Southern Castle com rank C ou melhor. Evite o Blade Shark, que é invulnerável. Dá o Dancer\'s Shawl.'),
       0, S6B + S6)
c.item('quest', t('Turtle-Tale'), t('Sandras — Ashley on the mast', 'Sandras — Ashley no mastro'), END6,
       t("Long deadline. Watch the sea turtles at both green markers in Specular Bay, use the quest button after shopping at Anika's Goods, then camp until night at the Orlen Islands' East Beach.",
         'Prazo longo. Observe as tartarugas nos dois marcadores verdes de Specular Bay, use o botão de quest depois de comprar na Anika\'s Goods e acampe até a noite na East Beach de Orlen Islands.'),
       0, S6B + S6)
c.boss(t('Lǫgr'), t('Ruined Capital of Ribe — interior', 'Ruined Capital of Ribe — interior'),
       t('Dash through his homing orbs and the beam barrage (both are speed attacks), then time a Duo Guard on the giant red sword that ends it for a big counter. After his durability breaks he summons clones: kill them fast. At low HP he fires orbs while still attacking.',
         'Use o dash contra os orbes teleguiados e a rajada de feixes (ambos são ataques rápidos) e acerte a Duo Guard na espada vermelha gigante do final para um grande contra-ataque. Quando a resistência quebra, ele invoca clones: derrube rápido. Com pouco HP, ele dispara orbes enquanto ataca.'),
       sources=[NEO('Chapter 6 - Ruined Capital of Ribe')] + S6)
for name, src in [('Mushroom Sauté Box Lunch', 'Reward for Foraging Ahead|Recompensa da Foraging Ahead'),
                  ('Fungi Fricassee Feast', 'Reward for Fellowship with Flavor|Recompensa da Fellowship with Flavor'),
                  ('Sizzling Gratin Box Lunch', 'Specular Bay — Northern Citadel recapture, rank S|Retomada da Northern Citadel em Specular Bay, rank S'),
                  ('Pizza-Making Showdown', 'Treasure chest in the Ruined Capital of Ribe|Baú na Ruined Capital of Ribe')]:
    en, pt = src.split('|')
    c.recipe(name, t(en, pt), sources=[NEO('Chapter 10 - Trophy Cleanup')])
fish(c, 'Hineria', [(t('Orlen Islands — pond', 'Orlen Islands — lago'), None)], S6B)
fish(c, 'Queen Boleh', [(t('Ruined Capital of Ribe — middle of the sunken city', 'Ruined Capital of Ribe — meio da cidade submersa'), 'Fishing Bait M')], [NEO('Chapter 6 - Ruined Capital of Ribe')])
chests(c, ('Fuling Island', 'Fuling Island'), [
    ('Bitter Remedy', 'Ledge to the southwest', 'Borda a sudoeste'),
    ('Defroster x3', 'Further south', 'Mais ao sul'),
    ('Super Repair Kit x3', 'Tree near the mini-boss', 'Árvore perto do mini-chefe', B),
    ('Armor Star+', 'Blue chest after pushing the large log', 'Baú azul depois de empurrar o tronco grande'),
    ('Chalice Star+', 'Northeast point', 'Ponto nordeste', B),
    ('Dark Lump x3', 'Around the waterfall, once the boulder is gone', 'Perto da cachoeira, depois que a rocha sai', B),
    ('Vitality Elixir', 'Cave: red chest outside the north exit', 'Caverna: baú vermelho do lado de fora da saída norte'),
    ('Arion Amulet', 'Cave: blue chest in the center', 'Caverna: baú azul no centro'),
    ('Lyre Star+', 'Cave: by the water in the center', 'Caverna: junto à água no centro', B),
    ('Panacea x3', 'Cave: corner before the log bridge', 'Caverna: canto antes da ponte de tronco'),
    ('Super Stimulant x2', 'Cave: end of the log bridge', 'Caverna: fim da ponte de tronco', B),
    ('Silver Cheese x3', 'Outside the southeast exit of the cave', 'Do lado de fora da saída sudeste da caverna'),
], ('Needs the Mana Barrier, southeast of Raufos Island. The island opens fully after the first event with Nanna. To clear the boulder near the lake, talk to the two green-marked people first, then call Dogi.',
    'Precisa da Mana Barrier, a sudeste de Raufos Island. A ilha abre por completo depois do primeiro evento com a Nanna. Para tirar a rocha perto do lago, fale antes com as duas pessoas marcadas em verde e depois chame o Dogi.'), S6S)
chests(c, ('Orlen Islands', 'Orlen Islands'), [
    ('Red Lump x3', 'East Beach: down to the southeast', 'East Beach: descendo a sudeste', B),
    ('Glare Bangle', 'Behind the house past the event marker', 'Atrás da casa depois do marcador de evento'),
    ('4500 Gold', 'Debris near the house', 'Destroços perto da casa', B),
    ('Sin Star', 'Southeast corner', 'Canto sudeste', B),
    ('Red Herb x3', 'Northwest corner of the shore', 'Canto noroeste da margem'),
    ('Fishing Bait L x3', 'Just before the south exit', 'Logo antes da saída sul'),
    ('Punishment Star', 'Next area: beside the house', 'Área seguinte: ao lado da casa'),
    ('Basic Craft Stock x75', 'Southeast corner', 'Canto sudeste', B),
    ('3000 Gold', 'West path', 'Caminho oeste'),
    ('Full Potion', 'Red chest on a high ledge by the pond (Mana Ride from higher ground)', 'Baú vermelho numa borda alta junto ao lago (Mana Ride a partir de um ponto mais alto)'),
    ('Defense Elixir', 'Northwest corner, by a tree', 'Canto noroeste, junto a uma árvore', B),
    ("Angler's Headband", 'Southeast corner', 'Canto sudeste'),
    ('Repair Kit x3', 'Southeast corner', 'Canto sudeste', B),
    ('Rainbow Lump x3', 'Just before the top, near the event marker', 'Logo antes do topo, perto do marcador de evento', B),
    ('Blessed Paper Scrap', 'Red chest next to the Specular Grass', 'Baú vermelho ao lado da Specular Grass'),
], ('Specular Bay blocks the way back until you finish here, but the islands stay open afterwards.',
    'Specular Bay bloqueia a volta até você terminar aqui, mas as ilhas continuam abertas depois.'), S6B)
chests(c, ('Sprout Atoll', 'Sprout Atoll'), [
    ('Blue Crystal Water x2', None, None, B),
    ('Blacksilver Sand x3', None, None),
    ('Basic Beast Parts x75', None, None),
    ('3300 Gold', None, None, B),
], ('Southwest edge of Specular Bay, after the Northern Citadel recapture (Pikkard Coral).',
    'Borda sudoeste de Specular Bay, depois da retomada da Northern Citadel (Pikkard Coral).'), S6B)
chests(c, ('Eversummer Isle', 'Eversummer Isle'), [
    ('Blessed Paper Scrap', 'Around the island', 'Pela ilha'),
    ('Rainbow Drop x6', 'Around the island', 'Pela ilha', B),
], ('East of the Southern Castle recapture, where Guila joins.', 'A leste da retomada do Southern Castle, onde a Guila entra.'), S6B)
chests(c, ('Ruined Capital of Ribe', 'Ruined Capital of Ribe'), [
    ('Defroster x3', 'City: under a puddle after the merman enemies', 'Cidade: embaixo de uma poça depois dos inimigos tritões', B),
    ('Yellow Lump x3', 'City: west, corner by the concrete wall', 'Cidade: oeste, canto junto ao muro de concreto', B),
    ('Blacksilver Sand x3', 'City, west route: wall corner', 'Cidade, rota oeste: canto do muro', B),
    ('Basic Ingredients x75', 'City, west route: behind a house', 'Cidade, rota oeste: atrás de uma casa'),
    ('Blue Lump x3', 'City, west route: rooftop and Mana Ride', 'Cidade, rota oeste: telhado e Mana Ride'),
    ('Empty Bottle', 'City: northeast of the water area', 'Cidade: nordeste da área com água', B),
    ('Yellow Lump x3', 'City: behind a house a little further west', 'Cidade: atrás de uma casa um pouco mais a oeste'),
    ('Rainbow Lump x3', 'City: southern section (Mana Ride from the roof)', 'Cidade: seção sul (Mana Ride a partir do telhado)', B),
    ('Super Sedative x3', 'City: eastern corner of the wall', 'Cidade: canto leste do muro'),
    ("Hunter's Bracelet", 'City: blue chest on high ground (rooftop jump)', 'Cidade: baú azul no alto (salto do telhado)'),
    ('Basic Craft Stock x100', 'Sunken city: north corner by the wall', 'Cidade submersa: canto norte junto ao muro', B),
    ('Pink Pearl Ring', 'Sunken city: red chest opposite (timed Mana Ride jump; gift for Mirabel)', 'Cidade submersa: baú vermelho do lado oposto (salto com Mana Ride; presente para a Mirabel)'),
    ('Red Herb x3', 'Sunken city: northwest across the water, by a fishing spot', 'Cidade submersa: noroeste, do outro lado da água, junto a um pesqueiro'),
    ('Fishing Bait M x3', 'Floodgate entrance: under a tree', 'Entrada da comporta: embaixo de uma árvore', B),
    ('Dark Lump x3', 'Floodgate entrance: below the collapsed bridge', 'Entrada da comporta: embaixo da ponte desabada', B),
    ('Silver Cheese x3', 'Floodgate entrance: across the broken bridge', 'Entrada da comporta: do outro lado da ponte quebrada'),
    ('Basic Beast Parts x100', 'Floodgate entrance: right next to you after the event', 'Entrada da comporta: bem ao seu lado depois do evento', B),
    ('Punishment Star+', 'Floodgate (split party): blue chest along the first route', 'Comporta (dupla separada): baú azul na primeira rota'),
    ('Chevalier Shield', 'Floodgate: blue chest past the lowered bridge', 'Comporta: baú azul depois da ponte abaixada'),
    ('3500 Gold', 'Floodgate: chest hanging above the Griegr room', 'Comporta: baú suspenso acima da sala dos Griegrs'),
    ('Fishing Bait G x3', 'Floodgate: right of the drawbridge', 'Comporta: à direita da ponte levadiça'),
    ('Luncheon Recipe: Pizza', 'Floodgate: red chest by the Runestone', 'Comporta: baú vermelho junto à Runestone'),
    ('Super Repair Kit x3', 'Interior: past the flying enemies', 'Interior: depois dos inimigos voadores', B),
    ('Red Lump x3', 'Interior: top of the stairs, right', 'Interior: alto da escada, à direita'),
    ('Mayura Amulet', 'Interior: room with the switch', 'Interior: sala do interruptor'),
    ('Blue Lump x6', 'Interior: northwest corner before the gate', 'Interior: canto noroeste antes do portão', B),
    ('4000 Gold', 'Interior: right corner past the gate', 'Interior: canto direito depois do portão', B),
    ('Taurus Ring', 'Final room, after the boss', 'Sala final, depois do chefe'),
], ('The Raven Boundstones split Adol and Karja: one stands on a switch while the other moves on.',
    'As Raven Boundstones separam o Adol e a Karja: um fica no interruptor enquanto o outro avança.'), [NEO('Chapter 6 - Ruined Capital of Ribe')])

# ======================================================================== Chapter 7
c = chapter(7, 'Chapter 7', 'Capítulo 7')
GROTTO = c.cp('Heading to the red marker after Grotto Isle', 'Seguir para o marcador vermelho depois de Grotto Isle')
NORGEST = c.cp('Talking to Grenn and Grimson to begin the attack', 'Falar com o Grenn e o Grimson para começar o ataque')
if c.cp('The last event marker of Chapter 7', 'O último marcador de evento do Capítulo 7') != END7:
    raise SystemExit('END7 id drifted')
S7 = [GF('Chapter 7: The Battle of Flumen Strait')]
S7F = [NEO('Chapter 7 - Flumen Strait')]
S7D = [NEO('Chapter 7 - Dvergr Coast')]
S7P = [NEO('Chapter 7 - Falaise Peninsula')]
c.item('missable', t("Lux's character note #1", 'Nota de personagem do Lux #1'), t('Sandras — lower deck', 'Sandras — convés inferior'), NORGEST,
       t("The third time-limited character note. While you are stationed on Grimson's ship, go back to the Sandras and talk to Lux twice on the lower deck, before talking to Grenn.",
         'A terceira nota de personagem com tempo limitado. Enquanto estiver no navio do Grimson, volte ao Sandras e fale duas vezes com o Lux no convés inferior, antes de falar com o Grenn.'),
       0, S7D)
c.item('quest', t('Old Haunts'), t('Anchor Island — Magni on the Mynorca Village shore', 'Anchor Island — Magni na praia de Mynorca Village'), GROTTO,
       t('Medium deadline. Head to the green marker near Krangal Island, beat the ships in the fog and the jellyfish boss on the ghost ship. Rewards the Shield Cannons.',
         'Prazo médio. Vá ao marcador verde perto de Krangal Island, derrote os navios na névoa e o chefe água-viva no navio fantasma. Dá os Shield Cannons.'),
       0, S7F + S7)
c.item('quest', t('Breakout Performance'), t('Grotto Isle (from a Hugill letter)', 'Grotto Isle (de uma carta do Hugill)'), GROTTO,
       t("Medium deadline. Read Hugill's letter near the blue marker south of Gregorio's Curio, talk to him on the mast, and clear Grotto Isle. Rewards 5,000 Gold and frees the last Carnac townsperson.",
         'Prazo médio. Leia a carta do Hugill perto do marcador azul ao sul do Gregorio\'s Curio, fale com ele no mastro e explore Grotto Isle até o fim. Dá 5.000 Gold e liberta o último morador de Carnac.'),
       0, S7F + S7)
c.item('quest', t('Treasure Trawl D'), t('Specular Bay — near the Northern Citadel', 'Specular Bay — perto da Northern Citadel'), GROTTO,
       t("Long deadline. Hidden Treasure Chart D is sold at Gregorio's Curio in the Flumen Strait. Rewards Fleeting Hope+.",
         'Prazo longo. O Hidden Treasure Chart D é vendido no Gregorio\'s Curio, em Flumen Strait. Dá Fleeting Hope+.'),
       0, S7F + S7)
c.item('quest', t('Cull the Griegr: Orlen'), t('Orlen Islands — West Side, far southwest', 'Orlen Islands — West Side, extremo sudoeste'), NORGEST,
       t('Long deadline. From the Norman soldier on the Norgest. A bird-like humanoid Griegr with small flying Watz that keep shooting. Rewards a Blessed Paper Scrap.',
         'Prazo longo. Vem do soldado normando no Norgest. Um Griegr humanoide parecido com pássaro, com pequenos Watz voadores que não param de atirar. Dá um Blessed Paper Scrap.'),
       0, S7D + S7)
c.item('quest', t('Nest of Kin'), t('Sandras — Ashley on the deck', 'Sandras — Ashley no convés'), NORGEST,
       t("Long deadline. From Gregorio's Curio, sail west and spot the nest with the spyglass; follow the new markers (the one near the merchant ship, then the southeast one).",
         'Prazo longo. Saindo do Gregorio\'s Curio, navegue a oeste e ache o ninho com a luneta; siga os marcadores novos (o perto do navio mercante e depois o do sudeste).'),
       0, S7D + S7)
c.item('quest', t('EX: Smooth Sailing? (Proud)', 'EX: Smooth Sailing? (Proud)'), t('Sandras — Hugill\'s letters', 'Sandras — cartas do Hugill'), None,
       t('Proud Nordics only. Added by the Hugill letter "EX: Smooth Sailing?" at the start of the chapter. The guide gives no steps or deadline: do it in this chapter to be safe.',
         'Só no Proud Nordics. Entra com a carta do Hugill "EX: Smooth Sailing?" no começo do capítulo. O guia não dá passos nem prazo: faça neste capítulo por segurança.'),
       0, S7F)
c.boss(t('Blob Weiser'), t('The ghost ship near Krangal Island', 'O navio fantasma perto de Krangal Island'),
       t('Lure it out from between the stairs for a better camera. Most spins break Duo Guard; it spits Slow globs, poison gas and can curse. When it dies it releases skull enemies.',
         'Atraia-o para fora da escada para a câmera ajudar. A maioria dos giros quebra a Duo Guard; ele cospe bolas que deixam lento, gás venenoso e pode amaldiçoar. Ao morrer, libera inimigos-caveira.'),
       related='ysx-ch7-q-01', sources=S7F + S7)
c.boss(t('Óðr and the Naglfar Core', 'Óðr e o Naglfar Core'), t('Ironclad Warship Naglfar'),
       t('Óðr cannot be killed: the target is the Naglfar Core, which vanishes and drops in elsewhere. Blocking his red power attack stuns him for a while, so you can focus the core; keep the guard held. Destroying the core ends the fight.',
         'O Óðr não pode ser derrotado: o alvo é o Naglfar Core, que some e reaparece em outro ponto. Bloquear o ataque poderoso vermelho dele o atordoa por um tempo, para você focar o núcleo; mantenha a defesa. Destruir o núcleo encerra a luta.'),
       sources=S7P + S7)
c.boss(t('Thelx Sirène'), t('Ironclad Warship Naglfar — deck', 'Ironclad Warship Naglfar — convés'),
       t('Duo guard her leaping slam. Her lower mouth bites and breathes poison, and she can curse. After her durability breaks she summons small newts and dives; she homes in when she surfaces, so keep guarding and attacking.',
         'Use a defesa em dupla contra a pancada com salto. A boca de baixo morde e solta veneno, e ela pode amaldiçoar. Quando a resistência quebra, ela invoca salamandras pequenas e mergulha; ela persegue você ao emergir, então continue defendendo e atacando.'),
       sources=S7P + S7)
c.recipe('Lucky Potato Pie Box Lunch', t('Flumen Strait — Abandoned Mine recapture, rank S', 'Retomada da Abandoned Mine em Flumen Strait, rank S'), sources=[NEO('Chapter 10 - Trophy Cleanup')])
c.recipe('Colorful Dessert Box Lunch', t("Treasure on the Falaise Peninsula side road, or buy at Gregorio's Curio", "Baú na estrada lateral da Falaise Peninsula, ou compre no Gregorio's Curio"), sources=[NEO('Chapter 10 - Trophy Cleanup')])
fish(c, 'Ponffer', [(t('Grotto Isle — shore; Dvergr Coast', 'Grotto Isle — margem; Dvergr Coast'), 'Fishing Bait M')], S7F + S7D)
chests(c, ('Grotto Isle', 'Grotto Isle'), [
    ('Super Repair Kit x3', 'South, behind the rock pillar', 'Sul, atrás do pilar de rocha', B),
    ('Green Crystal Water x2', 'Far southeast corner', 'Extremo sudeste'),
    ('Sin Star+', 'Blue chest at the west corner', 'Baú azul no canto oeste'),
    ('Dark Lump x5', 'North, by a tree', 'Norte, junto a uma árvore', B),
    ('Basic Craft Stock x100', 'Underground: first wide area, after clearing the monsters', 'Subterrâneo: primeira área ampla, depois de limpar os monstros'),
    ('Punishment Star+', 'Underground: next open room', 'Subterrâneo: sala aberta seguinte', B),
    ('Rage Formula', 'Underground: red chest in the same room', 'Subterrâneo: baú vermelho na mesma sala'),
    ('Yellow Seastone x3', 'Underground: hallway after it', 'Subterrâneo: corredor seguinte', B),
], ('Opened by the Breakout Performance quest.', 'Aberta pela quest Breakout Performance.'), S7F)
chests(c, ('Falaise Peninsula — Fortress Entrance', 'Falaise Peninsula — Fortress Entrance'), [
    ('Blue Lump x6', 'Left, by the trees', 'Esquerda, junto às árvores', B),
    ('Basic Reagents x100', 'Right, behind a pillar', 'Direita, atrás de um pilar'),
    ('Basic Craft Stock x100', 'North route, where the vines were', 'Rota norte, onde estavam as vinhas', B),
    ('Fishing Bait G x3', 'North dead end', 'Beco sem saída ao norte'),
    ('Golden Potato x3', 'South route, by trees near the ruins', 'Rota sul, junto às árvores perto das ruínas', B),
    ('Breath Water II', 'Red chest past the burnt vines to the south', 'Baú vermelho depois das vinhas queimadas ao sul'),
    ('Sin Star+', 'Near the spring', 'Perto da nascente', B),
    ('Axe Soul', 'Blue chest at the western end', 'Baú azul no extremo oeste'),
    ('Fishing Bait M x5', 'Fortress side, near the scouting marker', 'Lado da fortaleza, perto do marcador de reconhecimento', B),
    ('Basic Craft Stock x100', 'Fortress side, same spot', 'Lado da fortaleza, no mesmo ponto'),
], ('North of the Dvergr Coast camp. Breath Water II adds one more potion to your stock.',
    'Ao norte do acampamento da Dvergr Coast. A Breath Water II adiciona mais uma poção ao estoque.'), S7D + S7)
chests(c, ('Falaise Peninsula — Side Road', 'Falaise Peninsula — Side Road'), [
    ('Basic Ingredients x100', 'South, behind vines near the small cave', 'Sul, atrás de vinhas perto da caverna pequena'),
    ('Red Lump x6', 'West, by a tree', 'Oeste, junto a uma árvore', B),
    ('Dark Lump x6', 'Southern part, by the debris', 'Parte sul, junto aos destroços', B),
    ('Yellow Lump x6', 'Southwest end', 'Extremo sudoeste'),
    ('Strength Elixir', 'Northwest, by a tree', 'Noroeste, junto a uma árvore', B),
    ("Warrior's Earrings", 'Blue chest above it, behind vines', 'Baú azul acima, atrás de vinhas'),
    ('Armor Soul', 'Northeast corner', 'Canto nordeste'),
    ('Colorful Dessert Box Lunch', 'Red chest left of the event marker', 'Baú vermelho à esquerda do marcador de evento'),
], ('Opens after the attack begins (talking to Grenn and Grimson on the Norgest): take the south exit of the Dvergr Coast.',
    'Abre depois que o ataque começa (falar com o Grenn e o Grimson no Norgest): pegue a saída sul da Dvergr Coast.'), S7P + S7)
chests(c, ('Grugal Fortress', 'Grugal Fortress'), [
    ('4000 Gold', 'Below the fortress, far southwest', 'Embaixo da fortaleza, extremo sudoeste', B),
    ('Yellow Lump x6', 'East, before a tree', 'Leste, antes de uma árvore', B),
    ('Inferno Bracelet', 'Blue chest under the northwest side of the fortress', 'Baú azul embaixo do lado noroeste da fortaleza'),
    ('Everlasting Leather x3', 'Interior: pull the crate under it with Mana String', 'Interior: puxe o caixote para baixo dele com o Mana String'),
    ('Fishing Bait L x5', 'Outside, to the left', 'Do lado de fora, à esquerda'),
    ('Sword Soul', 'Second interior: end of the path past the drawbridge', 'Segundo interior: fim do caminho depois da ponte levadiça'),
    ('Shield Soul', 'Second interior: northeast corner, after the Draculea', 'Segundo interior: canto nordeste, depois do Draculea', B),
    ('Red Lump x6', 'Next section: left of the Hewnstone', 'Seção seguinte: à esquerda da Hewnstone'),
    ('True Barriermancy Text', 'Red chest in the middle, via the wooden pallet and Mana String', 'Baú vermelho no meio, pelo palete de madeira e o Mana String'),
    ('Suzhen Amulet', 'Blue chest past the harpy', 'Baú azul depois da harpia'),
    ('Golden Potato x3', 'Last part: east corner', 'Última parte: canto leste'),
], ('After an event in the second interior you cannot go back to the earlier sections until Chapter 9, when the main entrance also opens.',
    'Depois de um evento no segundo interior, não dá para voltar às seções anteriores até o Capítulo 9, quando a entrada principal também abre.'), S7P + S7)

# ======================================================================== Chapter 8
c = chapter(8, 'Chapter 8', 'Capítulo 8')
S8 = [GF('Chapter 8: Lila')]
S8N = [NEO('Chapter 8 - Eastern Rogue Sea')]
c.boss(t('Lǫgr (true form)', 'Lǫgr (forma verdadeira)'), t('Serenes Island — cave depths', 'Serenes Island — fundo da caverna'),
       t('A melee fighter now. He covers the floor with vines and summons twin tornadoes that shrink your space while he keeps attacking. Breaking his durability only makes him more aggressive; dodge his spear dive.',
         'Agora ele luta corpo a corpo. Ele cobre o chão com vinhas e invoca dois tornados que diminuem seu espaço enquanto continua atacando. Quebrar a resistência só o deixa mais agressivo; desvie do mergulho com a lança.'),
       sources=S8N + S8)
c.recipe('Dazzling Potato Platter', t('Treasure chest on Serenes Island', 'Baú em Serenes Island'), sources=[NEO('Chapter 10 - Trophy Cleanup')])
fish(c, 'Aqua Marina', [(t('Soleli Island — ocean spot near the event marker', 'Soleli Island — pesqueiro no mar perto do marcador de evento'), 'Fishing Bait L')], S8N)
fish(c, 'Calamitis', [(t('Serenes Island — shore', 'Serenes Island — margem'), 'Fishing Bait M')], S8N)
chests(c, ('Soleli Island', 'Soleli Island'), [
    ('Blaze Gloves', 'West corner', 'Canto oeste'),
    ('Basic Craft Stock x125', 'Right side of the map', 'Lado direito do mapa'),
    ('5000 Gold', 'Right side of the map', 'Lado direito do mapa'),
], ('Talking to Lǫgr moves you on, but the island can be visited again later.',
    'Falar com o Lǫgr leva você adiante, mas a ilha pode ser visitada de novo depois.'), S8N)
chests(c, ('Serenes Island', 'Serenes Island'), [
    ('Fishing Bait EX x3', 'West, by a tree where the path opens up', 'Oeste, junto a uma árvore onde o caminho se abre', B),
    ('Super Antidote x3', 'North end', 'Extremo norte'),
    ('Hail Bracelet', 'Blue chest past the blue gate (split party at the Ravenbound Statue)', 'Baú azul depois do portão azul (dupla separada na Ravenbound Statue)'),
    ('Panacea x3', 'Past the purple gate', 'Depois do portão roxo'),
    ('Break Elixir', 'Split room, on the mini-boss side', 'Sala dividida, no lado do mini-chefe', B),
    ('Dark Lump x5', 'Second area: by trees near the first Mana Cluster', 'Segunda área: junto às árvores perto do primeiro Mana Cluster', B),
    ('Lyre Soul', 'Second area: blue chest at the eastern end', 'Segunda área: baú azul no extremo leste'),
    ('Dryad Tear x3', "Second area: by a barrel past the river's west end", 'Segunda área: junto a um barril depois do fim do rio, a oeste', B),
    ('Empty Bottle', 'Second area: patch near a tree to the northwest', 'Segunda área: trecho perto de uma árvore a noroeste', B),
    ('Basic Reagents x125', 'Second area: before the next Mana Stream', 'Segunda área: antes do próximo fluxo de mana'),
    ('Rainbow Lump x3', 'Second area: southwest, near trees', 'Segunda área: sudoeste, perto de árvores', B),
    ('Yellow Seastone x3', 'Second area: far eastern end after the river', 'Segunda área: extremo leste depois do rio'),
    ('6500 Gold', 'Second area: by the Mana String spot near the end', 'Segunda área: junto ao ponto de Mana String perto do fim', B),
], ('Rune Tablet Part Three (red chest, needed to move on) lets Mana Ride go up water streams.',
    'A Rune Tablet Part Three (baú vermelho, necessária para avançar) permite subir correntezas com o Mana Ride.'), S8N)
chests(c, ('Serenes Island — cave', 'Serenes Island — caverna'), [
    ("Sea God's Incense", 'Red chest after the first Mana Ride', 'Baú vermelho depois do primeiro Mana Ride'),
    ('Super Stimulant x2', 'By the jars', 'Junto aos jarros', B),
    ('Blue Seastone x3', 'Behind the lamppost to the west', 'Atrás do poste a oeste', B),
    ('Fishing Bait L x3', 'Up the Mana String sword to the south', 'Subindo pela espada do Mana String ao sul'),
    ('Blizzard Gloves', 'Before the end of the path', 'Antes do fim do caminho'),
    ('Red Seastone x3', 'Second part: behind the jars', 'Segunda parte: atrás dos jarros', B),
    ('Chalice Soul', 'Second part: blue chest after the invisible floor', 'Segunda parte: baú azul depois do chão invisível'),
    ('Basic Craft Stock x150', 'Second part: far east side', 'Segunda parte: extremo leste', B),
    ('Fishing Bait G x3', 'Second part: far east side', 'Segunda parte: extremo leste'),
    ('Luncheon Recipe: Potatoes', 'Second part: red chest behind the northwest timed gate (slow time with Mana Sense)', 'Segunda parte: baú vermelho atrás do portão temporizado noroeste (desacelere o tempo com o Mana Sense)'),
    ('Rainbow Lump x3', 'Second part: past the northeast timed gate', 'Segunda parte: depois do portão temporizado nordeste', B),
    ('6750 Gold', 'Depths: behind the elevator', 'Fundo: atrás do elevador', B),
    ('Aurora Berries x3', 'Depths: across the Mana String', 'Fundo: depois do Mana String', B),
    ("Hermit's Remedy", 'Depths: jump off the stream halfway', 'Fundo: pule do fluxo no meio do caminho'),
    ('Hellblaze Tome', "Depths: red chest after Karja's Mana Burst jump", 'Fundo: baú vermelho depois do salto com o Mana Burst da Karja'),
    ('Defense Elixir', 'Depths: near the last Hewnstone', 'Fundo: perto da última Hewnstone', B),
], ('Three floors linked by elevators; the boss waits past the last Hewnstone.',
    'Três andares ligados por elevadores; o chefe espera depois da última Hewnstone.'), S8N)

# ======================================================================== Chapter 9
c = chapter(9, 'Chapter 9', 'Capítulo 9')
VORTEX = c.cp('Approaching the Vortex Path red marker in Raoul Darksea', 'Aproximar-se do marcador vermelho do Vortex Path em Raoul Darksea')
END9 = c.cp('The last event marker of Chapter 9', 'O último marcador de evento do Capítulo 9')
S9 = [GF('Chapter 9: The Waters of Creation')]
S9O = [NEO('Chapter 9 - Optional Activities')]
S9R = [NEO('Chapter 9 - Raoul Darksea')]
S9M = [NEO('Chapter 9 - Marine Triangle')]
c.item('quest', t('No Good Deed…'), t('Krangal Island — the mine', 'Krangal Island — a mina'), VORTEX,
       t('Long deadline. From the Hugill letter "ST OP ME". Land on the island for an event, then beat the Armed Biter in the mine. Rewards a Luminous Bangle.',
         'Prazo longo. Vem da carta do Hugill "ST OP ME". Desembarque na ilha para um evento e derrote o Armed Biter na mina. Dá um Luminous Bangle.'),
       0, S9O + S9)
c.item('quest', t('Riddle Me Timbers'), t('Sandras — Ezer', 'Sandras — Ezer'), VORTEX,
       t('Medium deadline. Green marker in the middle of Moonview Isle, then the event marker on Fishscale Island (naval battle), then the event marker on the Orlen Islands\' West Side (boss).',
         'Prazo médio. Marcador verde no meio de Moonview Isle, depois o marcador de evento em Fishscale Island (batalha naval) e por fim o marcador de evento no West Side de Orlen Islands (chefe).'),
       0, S9O + S9)
c.item('quest', t('Specular Synthesis'), t('Sandras — Dr. Flair on the lower deck', 'Sandras — Dr. Flair no convés inferior'), VORTEX,
       t('Medium deadline. Fight the Griegrs at the green marker of Grugal Fortress — Entrance, then reach the event marker on Redsand Isle (south end of Raoul Darksea) and report back. Rewards the Full-Heal Formula.',
         'Prazo médio. Enfrente os Griegrs no marcador verde de Grugal Fortress — Entrance, depois chegue ao marcador de evento em Redsand Isle (extremo sul de Raoul Darksea) e volte para relatar. Dá a Full-Heal Formula.'),
       0, S9R + S9)
c.item('quest', t('Slay the Beasts: Haze'), t('Haze Island — back half', 'Haze Island — metade de trás'), VORTEX,
       t('Long deadline. From Lila. Haze Island is northwest of Serenes Island; fast travel to the back half. The targets are fragile but hit very hard; stay out of the slowing water. Rewards the Panacea Formula III.',
         'Prazo longo. Vem da Lila. Haze Island fica a noroeste de Serenes Island; viaje até a metade de trás. Os alvos são frágeis, mas batem muito forte; fique fora da água que deixa lento. Dá a Panacea Formula III.'),
       0, S9O + S9)
c.item('quest', t('Treasure Trawl E'), t('Raoul Darksea — north, near the entrance', 'Raoul Darksea — norte, perto da entrada'), VORTEX,
       t('Long deadline. Hidden Treasure Chart E comes from the Eastern Fortress recapture at rank S. Rewards the Cycloid Crown. With every Treasure Trawl done, Mandy has one more treasure (northwest of Termina Island) that unlocks his character note.',
         'Prazo longo. O Hidden Treasure Chart E vem da retomada da Eastern Fortress com rank S. Dá a Cycloid Crown. Com todos os Treasure Trawls feitos, o Mandy tem mais um tesouro (a noroeste de Termina Island) que libera a nota de personagem dele.'),
       0, S9R + S9)
c.boss(t('Gigas Wing'), t('Gigantavis Isle (optional challenge)', 'Gigantavis Isle (desafio opcional)'),
       t('Level 85 with no durability meter. Use Mana String to catch up when it runs, and watch for poison and lightning. Rewards the last Blessed Paper Scrap.',
         'Nível 85, sem medidor de resistência. Use o Mana String para alcançá-lo quando fugir, e cuidado com veneno e raios. Dá o último Blessed Paper Scrap.'),
       sources=S9M + S9)
c.boss(t('Gunnar and Phylleia', 'Gunnar e Phylleia'), t('Seabed Temple of Ægir'),
       t('Shared HP bar. Focus Phylleia: her projectiles and fast combos land just as Gunnar attacks. Her dash is a speed attack: dodge it on time for a QTE counter.',
         'Barra de HP compartilhada. Foque a Phylleia: os projéteis e combos rápidos dela chegam junto com os ataques do Gunnar. A investida dela é um ataque rápido: desvie na hora para um contra-ataque com QTE.'),
       sources=S9R + S9)
c.boss(t('Óðr'), t('Seabed Temple of Ægir — sanctum', 'Seabed Temple of Ægir — santuário'),
       t('As his durability drops he adds a tornado that pulls you in and water pillars that fire from several directions (dodging them can open a counter). He is much stronger in Proud Nordics.',
         'Conforme a resistência cai, ele adiciona um tornado que puxa você e pilares de água que disparam de várias direções (desviar deles pode abrir um contra-ataque). Ele é bem mais forte no Proud Nordics.'),
       sources=S9R + S9)
c.recipe('Luxury Steak-Stravaganza', t('Reward for Riddle Me Timbers', 'Recompensa da Riddle Me Timbers'), sources=[NEO('Chapter 10 - Trophy Cleanup')])
c.recipe('Sweet Treat Rondo', t('Treasure chest on Redsand Isle', 'Baú em Redsand Isle'), sources=[NEO('Chapter 10 - Trophy Cleanup')])
fish(c, 'General Crab', [(t('Redsand Isle — shore', 'Redsand Isle — margem'), 'Fishing Bait L')], S9R)
fish(c, 'Gold Borsas', [(t('Redsand Isle — shore', 'Redsand Isle — margem'), 'Fishing Bait EX')], S9R)
fish(c, 'Cobalt Corp', [(t('Seabed Temple of Ægir — bridge', 'Seabed Temple of Ægir — ponte'), 'Fishing Bait EX')], S9R)
fish(c, 'Empress Saman', [(t('Seabed Temple of Ægir — sunken pillar, back half', 'Seabed Temple of Ægir — pilar submerso, metade de trás'), 'Fishing Bait L')], S9R)
chests(c, ('Grugal Fortress; Haze Island', 'Grugal Fortress; Haze Island'), [
    ('Rainbow Seastone x2', 'Grugal Fortress — northwest corner (the main entrance is open now)', 'Grugal Fortress — canto noroeste (a entrada principal está aberta agora)', B),
    ("Ascetic's Arcanum", 'Grugal Fortress — at the gate behind the mini-boss', 'Grugal Fortress — no portão atrás do mini-chefe'),
    ('Luck Elixir', 'Haze Island back half — the red chest that was out of reach (Slay the Beasts: Haze)', 'Metade de trás de Haze Island — o baú vermelho que estava fora de alcance (Slay the Beasts: Haze)'),
], ('Chests that only open now in areas from earlier chapters.', 'Baús que só abrem agora em áreas de capítulos anteriores.'),
    S9O, title=('Revisits: chests that open now', 'Revisitas: baús que abrem agora'))
chests(c, ('Gigantavis Isle', 'Gigantavis Isle'), [
    ('Dark Seastone x5', 'Northwest, up the ledges', 'Noroeste, subindo as bordas'),
    ('Blue Seastone x3', 'Top of the southern ledge', 'Alto da borda sul', B),
    ('Panacea II x3', 'Eastern dead end, by trees', 'Beco sem saída a leste, junto às árvores', B),
    ('Sin Soul+', 'Southeast corner', 'Canto sudeste'),
    ('Fishing Bait L x3', 'Ledges south of the middle part', 'Bordas ao sul da parte do meio', B),
    ('7000 Gold', 'Near the Hewnstone, by the vine-covered sword', 'Perto da Hewnstone, junto à espada coberta de vinhas'),
], ('Last blue marker of the Marine Triangle. The Ebon Mindgem on the eastern summit gives Guila\'s character note later.',
    'O último marcador azul do Marine Triangle. A Ebon Mindgem no topo leste dá a nota de personagem da Guila depois.'), S9M)
chests(c, ('Redsand Isle', 'Redsand Isle'), [
    ('Red Seastone x3', 'East side, behind two monsters', 'Lado leste, atrás de dois monstros', B),
    ('Luncheon Recipe: Sweets', 'Red chest at the south end, after pushing the log', 'Baú vermelho no extremo sul, depois de empurrar o tronco'),
], ('South end of Raoul Darksea, during Specular Synthesis.', 'Extremo sul de Raoul Darksea, durante a Specular Synthesis.'), S9R)
chests(c, ('Seabed Temple of Ægir — front half', 'Seabed Temple of Ægir — metade da frente'), [
    ('Panacea II x3', 'Before the temple: patch of land to the left', 'Antes do templo: trecho de terra à esquerda', B),
    ('Sin Soul', 'West, in a collapsed floor', 'Oeste, num piso desabado', B),
    ('Yellow Seastone x4', 'West, by another collapsed floor', 'Oeste, junto a outro piso desabado'),
    ('Venom Gloves', 'Upper level, northeast', 'Nível de cima, nordeste'),
    ('Vitality Elixir', 'West passage, before the debris', 'Passagem oeste, antes dos destroços', B),
    ('6500 Gold', 'Top floor', 'Último andar'),
    ('Super Relaxant x3', 'Second hall: drop below instead of riding the stream', 'Segundo salão: desça em vez de seguir o fluxo', B),
    ('Pyrope Sword', "Second hall: red chest in the north center (Adol's weapon)", 'Segundo salão: baú vermelho no centro-norte (arma do Adol)'),
    ("Sorcerer's Medal", 'Second hall: east of it', 'Segundo salão: a leste dele'),
    ('7500 Gold', 'Second hall: west room', 'Segundo salão: sala oeste', B),
    ('Basic Beast Parts x175', 'Second hall: west room', 'Segundo salão: sala oeste'),
    ('Sword Soul+', 'Second hall: south center', 'Segundo salão: centro-sul'),
    ('Soul Timber x3', 'Second hall: southwest room, by the switch', 'Segundo salão: sala sudoeste, junto ao interruptor'),
    ('R Potion', 'Second hall: southeast corner once the gate opens', 'Segundo salão: canto sudeste quando o portão abre'),
    ('Dryad Tear x3', 'Third hall: eastern corner', 'Terceiro salão: canto leste', B),
    ('Defense Elixir', 'Third hall: patch of land to the north', 'Terceiro salão: trecho de terra ao norte', B),
    ('Punishment Soul', 'Third hall: same patch', 'Terceiro salão: mesmo trecho'),
    ('Dark Seastone x3', 'Third hall: past the Mana String poles', 'Terceiro salão: depois dos postes do Mana String'),
    ('Red Seastone x4', 'Third hall: same stretch', 'Terceiro salão: mesmo trecho'),
    ('Haüyne Axe', "Third hall: red chest behind the mini-boss (Karja's weapon)", 'Terceiro salão: baú vermelho atrás do mini-chefe (arma da Karja)'),
    ('Raiju Guardstone', 'Blue chest after the Gunnar and Phylleia fight', 'Baú azul depois da luta contra o Gunnar e a Phylleia'),
    ('Defroster x5', 'Next to it', 'Ao lado dele', B),
], ("Northwest corner of Raoul Darksea, through the Vortex Path. Karja's Mana Burst freezes water to reach higher ledges.",
    'Canto noroeste de Raoul Darksea, pelo Vortex Path. O Mana Burst da Karja congela a água para alcançar bordas mais altas.'), S9R)
chests(c, ('Seabed Temple of Ægir — back half', 'Seabed Temple of Ægir — metade de trás'), [
    ('Extinguisher x5', 'Beside the hole at the start', 'Ao lado do buraco do início', B),
    ('Super Repair Kit x3', 'East corner', 'Canto leste'),
    ('Armor Soul+', 'Upper platform: blue chest behind the monsters on the east side', 'Plataforma de cima: baú azul atrás dos monstros no lado leste'),
    ('Blue Seastone x4', 'East end of the water path', 'Extremo leste do caminho de água'),
    ('Shield Soul+', 'Second part: blue chest in the north center', 'Segunda parte: baú azul no centro-norte'),
    ('Panacea x3', 'Second part: right as you enter the large area', 'Segunda parte: logo ao entrar na área grande', B),
    ('Basic Craft Stock x200', 'Second part: southeast corner, in the water', 'Segunda parte: canto sudeste, na água', B),
    ('Chalice Soul+', 'Second part: blue chest past the gate opened by the switch', 'Segunda parte: baú azul depois do portão aberto pelo interruptor'),
    ("Sea God's Incense", 'Second part: red chest on the east side after the swing', 'Segunda parte: baú vermelho no lado leste depois do balanço'),
    ('Luck Elixir', 'Second part: third section', 'Segunda parte: terceira seção'),
    ('Blue Crystal Water x2', 'Second part: north corner, by the Empress Saman fishing spot', 'Segunda parte: canto norte, junto ao pesqueiro do Empress Saman'),
    ('Ultimate Beast Meat x3', 'Second part: south end after the stairs', 'Segunda parte: extremo sul depois da escada'),
    ('Dark Seastone x3', 'Third part: to the right of the start', 'Terceira parte: à direita do início', B),
    ('8000 Gold', 'Third part: northeast patch of land', 'Terceira parte: trecho de terra a nordeste', B),
    ('Green Crystal Water x2', 'Third part: east side after the chandeliers', 'Terceira parte: lado leste depois dos lustres'),
    ("Martialist's Gauntlets", 'Third part: blue chest at the south end', 'Terceira parte: baú azul no extremo sul'),
    ('Defense Elixir', 'Third part: red chest south of the Hewnstone', 'Terceira parte: baú vermelho ao sul da Hewnstone'),
    ("Spellbook: Nixie's Blessing", 'Sanctum: after the boss', 'Santuário: depois do chefe'),
], ('The spellbook is a blueprint for the Sandras.', 'O spellbook é um projeto para o Sandras.'), S9R)
chests(c, ('Viewpoint Isle', 'Viewpoint Isle'), [
    ('Vitality Elixir', 'Areas visited before', 'Áreas já visitadas', B),
    ('Crystal Shard x300', 'Areas visited before', 'Áreas já visitadas', B),
    ('Fishing Bait S x3', 'Areas visited before', 'Áreas já visitadas', B),
    ('Crystal Shard x2500', 'Northeast quadrant (ride up the water path)', 'Quadrante nordeste (suba pelo caminho de água)', B),
    ('Mega Ulti-Meat Box Lunch', 'Northeast quadrant', 'Quadrante nordeste'),
    ('Defense Elixir', 'Northeast quadrant', 'Quadrante nordeste', B),
    ('Axe Soul+', 'Northeast quadrant', 'Quadrante nordeste'),
    ('Vitality Elixir', 'Northeast quadrant', 'Quadrante nordeste'),
    ('Rainbow Lump x3', 'Northeast quadrant', 'Quadrante nordeste', B),
], ('The northeast is confusing because the map ignores height: use Mana Sense often. Reaching the old man ends the chapter, but you can come back in Chapter 10.',
    'O nordeste confunde porque o mapa ignora a altura: use o Mana Sense com frequência. Chegar ao velho encerra o capítulo, mas dá para voltar no Capítulo 10.'), S9R)

# ======================================================================== Chapter 10
c = chapter(10, 'Chapter 10', 'Capítulo 10')
FINAL = c.cp('Going through the doors to the final battle (point of no return)', 'Passar pelas portas da batalha final (ponto sem volta)')
S10 = [GF("Chapter 10: The Normans' Paradise Lost")]
S10S = [NEO('Chapter 10 - Sandras')]
S10R = [NEO('Chapter 10 - Rogue Sea')]
S10F = [NEO('Chapter 10 - Final Area')]
c.item('quest', t('Return to Ribe'), t('Sandras — Lila in the cabin', 'Sandras — Lila na cabine'), FINAL,
       t('Short deadline. Visit the three event markers in the city of Ribe, then fast travel to the depths of the capital and examine the glowing object underwater. Rewards Abiding Love+ and Lila\'s character note.',
         'Prazo curto. Visite os três marcadores de evento na cidade de Ribe, depois viaje até o fundo da capital e examine o objeto brilhante debaixo d\'água. Dá Abiding Love+ e a nota de personagem da Lila.'),
       0, S10S + S10)
c.item('quest', t('Rushed off Their Fleet'), t('Anchor Island — Village Chiefs Nel and Isaac in Mynorca Village', 'Anchor Island — Village Chiefs Nel e Isaac em Mynorca Village'), FINAL,
       t('Short deadline. Three rounds against the Undying Fleet, each a naval battle plus a land battle: near Anchor Island, near Falun Island and at Carnac (fast travel to the Seagull Flock). Upgrade the Sandras first. Rewards a Sverkite.',
         'Prazo curto. Três rodadas contra a Undying Fleet, cada uma com batalha naval e batalha em terra: perto de Anchor Island, perto de Falun Island e em Carnac (viaje até o Seagull Flock). Melhore o Sandras antes. Dá uma Sverkite.'),
       0, S10S + S10)
c.item('quest', t('Cull the Griegr: Crescent'), t('Crescent Moons Isle', 'Crescent Moons Isle'), FINAL,
       t('Short deadline. Added when you land. Defeat every Griegr on the island; the target then appears in the northeast corner. Rewards Crystal Shards ×25,000.',
         'Prazo curto. Entra ao desembarcar. Derrote todos os Griegrs da ilha; o alvo então aparece no canto nordeste. Dá Crystal Shards ×25.000.'),
       0, S10R + S10)
c.item('quest', t('Treasure Trawl F'), t('Rogue Sea — east of Soleli Island', 'Rogue Sea — a leste de Soleli Island'), FINAL,
       t('Short deadline. Buy Hidden Treasure Chart F from the merchant Gøsta, north of the second Rogue Sea recapture. Rewards 50,000 Gold.',
         'Prazo curto. Compre o Hidden Treasure Chart F do mercador Gøsta, ao norte da segunda retomada do Rogue Sea. Dá 50.000 Gold.'),
       0, S10R)
c.item('quest', t('Whale of Fortune'), t('Sandras — Ashley at the bow', 'Sandras — Ashley na proa'), FINAL,
       t("Short deadline. Needs all three Rogue Sea islands recaptured, or some markers never appear. Use the spyglass at every green marker; the last one appears west of Gøsta's ship. Rewards a Spirit Necklace.",
         'Prazo curto. Exige as três ilhas do Rogue Sea retomadas, senão alguns marcadores nunca aparecem. Use a luneta em cada marcador verde; o último aparece a oeste do navio do Gøsta. Dá um Spirit Necklace.'),
       0, S10R + S10)
c.item('quest', t('An Axe to Regrind'), t("Giant's Hand Isle, then Ivalde on Balta Island", "Giant's Hand Isle e depois a Ivalde em Balta Island"), FINAL,
       t("Short deadline. Examine the axe at the end of Giant's Hand Isle, then bring Ivalde Crystalucent Coral ×3 (Gamellion, Seabed Temple) and Vajra Bone ×3 (Zylk Biter, Rollo's Ark). Rewards Karja's strongest weapon.",
         'Prazo curto. Examine o machado no fim de Giant\'s Hand Isle e leve à Ivalde Crystalucent Coral ×3 (Gamellion, Seabed Temple) e Vajra Bone ×3 (Zylk Biter, Rollo\'s Ark). Dá a arma mais forte da Karja.'),
       0, S10R + S10)
c.item('missable', t('Ship upgrades for the trophy', 'Melhorias do navio para o troféu'), t('Sandras'), FINAL,
       t('Not lost at the final battle, but ship refits do not carry over to New Game+: buy them all in one playthrough if you want "All Decked Out".',
         'Não se perdem na batalha final, mas as melhorias do navio não passam para o New Game+: compre todas na mesma jogada se quiser o "All Decked Out".'),
       0, S10 + [NEO('Chapter 10 - Trophy Cleanup')])
c.boss(t('Grimson'), t("Rollo's Ark"),
       t('Duo guard his leaping downward slash. Below half HP a pink aura makes him faster and stronger, but he gains no new moves.',
         'Use a defesa em dupla contra o golpe para baixo com salto. Abaixo da metade do HP, uma aura rosa o deixa mais rápido e forte, mas ele não ganha golpes novos.'),
       sources=[NEO('Chapter 10 - Cicatrix')] + S10)
c.boss(t('Vermóðr'), t('Jötunn Island (optional, level 99)', 'Jötunn Island (opcional, nível 99)'),
       t('The toughest fight, a stronger take on Iði: bring paralysis protection and plenty of medicine and box lunches. Its electric smash fills the arena with lightning and its darkness orb curses. Rewards the Ancient Strength Formula.',
         'A luta mais difícil, uma versão mais forte do Iði: leve proteção contra paralisia e muitos remédios e marmitas. A pancada elétrica enche a arena de raios e o orbe de trevas amaldiçoa. Dá a Ancient Strength Formula.'),
       sources=S10R + S10)
c.boss(t('The final battle', 'A batalha final'), t('Beyond the last doors', 'Além das últimas portas'),
       t('Shared HP bar for both foes. Focus the melee fighter while keeping the ranged one in view; they are open to ailments such as paralysis. In the last phase an unblockable grab is signalled by a charging fist: keep your distance.',
         'Barra de HP compartilhada pelos dois inimigos. Foque o lutador corpo a corpo sem perder o de longe de vista; eles são vulneráveis a efeitos como paralisia. Na última fase, um agarrão que não pode ser defendido é anunciado por um punho carregando: mantenha distância.'),
       sources=S10F + S10)
for name, src in [('Premium Seafood BBQ', 'Give every large fish to the Reticent Penguin (Ozmid Expanse)|Entregue todos os peixes grandes ao Reticent Penguin (Ozmid Expanse)'),
                  ('Mega Ulti-Meat Box Lunch', 'Report Adventures at 80% exploration, or a chest on Viewpoint Isle|Relate as aventuras com 80% de exploração, ou um baú em Viewpoint Isle'),
                  ('Seafood Supreme Box Lunch', 'Report Fishing after 24 kinds of fish, or a chest in Faarlundheim|Relate a pesca depois de 24 tipos de peixe, ou um baú em Faarlundheim')]:
    en, pt = src.split('|')
    c.recipe(name, t(en, pt), sources=[NEO('Chapter 10 - Trophy Cleanup')])
fish(c, 'Murgleys', [(t('Crescent Moons Isle — shore', 'Crescent Moons Isle — margem'), 'Fishing Bait EX')], S10R)
fish(c, 'Wishstar', [(t('Viewpoint Isle — Forbidden Lands, left spot at the entrance', 'Viewpoint Isle — Forbidden Lands, pesqueiro da esquerda na entrada'), 'Fishing Bait EX')], S10F)
fish(c, 'Megalofang', [(t('Viewpoint Isle — Forbidden Lands, behind the last Runestone', 'Viewpoint Isle — Forbidden Lands, atrás da última Runestone'), 'Fishing Bait EX')], S10F)
LAST = ('Lost once you go through the doors to the final battle.', 'Perdido quando você passa pelas portas da batalha final.')
chests(c, ("Rollo's Ark", "Rollo's Ark"), [
    ('Blue Crystal Water x3', 'Entrance: locked first-floor room, reached from the raised pillar (Enhanced Mana Sense)', 'Entrada: sala trancada do primeiro andar, alcançada pelo pilar erguido (Enhanced Mana Sense)'),
    ('Fishing Bait G x3', 'Entrance: second floor, north room', 'Entrada: segundo andar, sala norte'),
    ('Thunder Gloves', "Entrance: hole with spider webs in the northeast (burn them with Adol)", 'Entrada: buraco com teias no nordeste (queime com o Adol)'),
    ('Axe Soul+', 'Midpoint: room on the right', 'Meio: sala à direita'),
    ("Hermit's Remedy x2", 'Midpoint: west room, after pulling the switch', 'Meio: sala oeste, depois de puxar o interruptor'),
    ('Green Crystal Water x3', 'Third floor: top platform, by a lever', 'Terceiro andar: plataforma de cima, junto a uma alavanca'),
    ('Break Elixir', 'Third floor: red chest across the raised pillars', 'Terceiro andar: baú vermelho depois dos pilares erguidos'),
    ('Basic Beast Parts x200', 'Third floor: room past the gate unlocked earlier', 'Terceiro andar: sala depois do portão destrancado antes'),
    ('Lyre Soul+', 'Third floor: southwest corner, via the moving pole', 'Terceiro andar: canto sudoeste, pelo poste móvel'),
    ('Esoteric Bounding Text', 'Third floor: red chest at the event marker', 'Terceiro andar: baú vermelho no marcador de evento'),
], LAST, [NEO('Chapter 10 - Cicatrix')], until=FINAL)
chests(c, ('Crescent Moons Isle', 'Crescent Moons Isle'), [
    ('Super Repair Kit x3', 'South, near the lizard mini-boss', 'Sul, perto do mini-chefe lagarto', B),
    ('Punishment Soul+', 'West end of the ledge in the north center', 'Extremo oeste da borda no centro-norte', B),
    ('Supreme Fish Meat x2', 'South of the northwest Runestone', 'Ao sul da Runestone do noroeste'),
    ('Break Elixir', 'Red chest in a hidden drop by the east Mana String spot', 'Baú vermelho numa queda escondida junto ao ponto de Mana String do leste'),
], LAST, S10R, until=FINAL)
chests(c, ("Giant's Hand Isle", "Giant's Hand Isle"), [
    ('Dark Seastone x3', 'Patch of land by the lake fishing spot, to the east', 'Trecho de terra junto ao pesqueiro do lago, a leste', B),
    ('Panacea III x2', 'Far northwest corner', 'Extremo noroeste', B),
    ('Vajra Bone x2', 'Southeast corner', 'Canto sudeste'),
    ('Ancient Defense Formula', 'Red chest in the north center (drop through and ride the stream)', 'Baú vermelho no centro-norte (caia pelo buraco e siga o fluxo)'),
], LAST, S10R, until=FINAL)
chests(c, ('Viewpoint Isle', 'Viewpoint Isle'), [
    ('Axe Seal+', None, None, B),
    ('Crystal Shard x200', None, None, B),
    ('Luck Elixir', None, None, B),
    ('Strength Elixir', None, None, B),
    ('Fishing Bait x10', None, None, B),
    ('Dark Drop', None, None, B),
], ('Six buried treasures: one near the cottage, two on the east side and three on the west side, which only opens fully once you enter the treasure room. Lost once you go through the doors to the final battle.',
    'Seis tesouros enterrados: um perto da cabana, dois no lado leste e três no lado oeste, que só abre por completo quando você entra na sala do tesouro. Perdidos quando você passa pelas portas da batalha final.'),
    S10F, until=FINAL, title=('Viewpoint Isle — last buried treasures', 'Viewpoint Isle — últimos tesouros enterrados'))
chests(c, ('Viewpoint Isle — Forbidden Lands', 'Viewpoint Isle — Forbidden Lands'), [
    ('Blue Seastone x5', 'Entrance, on the first visit', 'Entrada, na primeira visita', B),
    ('Yellow Seastone x5', 'Behind the plant mini-boss to the northeast, by a tree', 'Atrás do mini-chefe planta a nordeste, junto a uma árvore', B),
    ('Red Seastone x5', 'Southwest: platform to the northwest', 'Sudoeste: plataforma a noroeste', B),
    ('Rainbow Seastone x3', 'North, guarded by monsters', 'Norte, guardado por monstros'),
    ('Lightning Boots', 'Blue chest west of the second plant mini-boss', 'Baú azul a oeste do segundo mini-chefe planta'),
    ('Fishing Bait EX x5', 'East platform, halfway along the Mana String', 'Plataforma leste, no meio do Mana String'),
    ('Strength Elixir', 'Northeast, near a plant enemy by a tree', 'Nordeste, perto de um inimigo planta junto a uma árvore', B),
    ('Chalice Soul+', 'Blue chest below, before the two harpies', 'Baú azul embaixo, antes das duas harpias'),
    ('Rainbow Seastone x5', 'By the wall where Karja starts talking', 'Junto à parede onde a Karja começa a falar', B),
    ('Luck Elixir', 'Red chest on the platform below the double mana stream', 'Baú vermelho na plataforma abaixo do fluxo de mana duplo'),
], LAST, S10F, until=FINAL)
chests(c, ('Faarlundheim', 'Faarlundheim'), [
    ('Panacea II x2', 'Part 1: behind the starting gate', 'Parte 1: atrás do portão do início', B),
    ("Hermit's Remedy", 'Part 1: behind the rock wall east of the northwest cluster', 'Parte 1: atrás da parede de rocha a leste do cluster do noroeste'),
    ('Sword Soul+', 'Part 1: blue chest on the islet past the red platform (slow time)', 'Parte 1: baú azul na ilhota depois da plataforma vermelha (desacelere o tempo)'),
    ('10000 Gold', 'Part 1: center, by a rock pillar', 'Parte 1: centro, junto a um pilar de rocha', B),
    ('Seafood Supreme Box Lunch', 'Part 1: southeast corner', 'Parte 1: canto sudeste'),
    ('Break Elixir', 'Part 1: behind the end of the high ledge on the north route', 'Parte 1: atrás do fim da borda alta na rota norte', B),
    ('Punishment Soul+', 'Part 1: north dead end', 'Parte 1: beco sem saída ao norte', B),
    ('Crystalucent Coral x5', 'Part 1: west after swinging on the red pillar', 'Parte 1: oeste depois de balançar no pilar vermelho'),
    ("Sea God's Incense", 'Part 1: red chest via the southwest mana stream', 'Parte 1: baú vermelho pelo fluxo de mana do sudoeste'),
    ('Gwyllgi Guardstone', 'Part 1: blue chest on a southeast platform below the northeast stream', 'Parte 1: baú azul numa plataforma a sudeste abaixo do fluxo do nordeste'),
    ('Lyre Soul+', 'Part 1: ledge just below it', 'Parte 1: borda logo abaixo', B),
    ('Basic Ingredients x350', 'Part 2: hidden platform in the southeast', 'Parte 2: plataforma escondida no sudeste', B),
    ('Crystal Shard x5000', 'Part 2: northwest tunnel', 'Parte 2: túnel noroeste', B),
    ('Vitality Elixir', 'Part 2: red chest in the same tunnel', 'Parte 2: baú vermelho no mesmo túnel'),
    ('Basic Beast Parts x350', 'Part 2: under the giant statue', 'Parte 2: embaixo da estátua gigante', B),
    ('Shield Soul+', 'Part 2: blue chest after the monster room (break the boulder)', 'Parte 2: baú azul depois da sala de monstros (quebre a rocha)'),
    ('Basic Reagents x350', 'Part 2: end of that path', 'Parte 2: fim desse caminho', B),
    ('Skill Potion', 'Part 2: red chest on the abandoned ship', 'Parte 2: baú vermelho no navio abandonado'),
    ('Basic Craft Stock x350', "Part 2: tunnel reached from the ship's mana stream", 'Parte 2: túnel alcançado pelo fluxo de mana do navio', B),
    ("Hero's Gauntlets", 'Part 2: blue chest via the red pillar on the east route', 'Parte 2: baú azul pelo pilar vermelho na rota leste'),
    ("Ascetic's Arcanum", 'Part 2: northeast corner before the northwest route', 'Parte 2: canto nordeste antes da rota noroeste', B),
    ('10000 Gold', 'Part 2: behind the brick wall by the Ravenbound Statue', 'Parte 2: atrás do muro de tijolos junto à Ravenbound Statue'),
    ('Luck Elixir', "Part 2: Karja's path, by the cages", 'Parte 2: caminho da Karja, junto às jaulas', B),
    ('Chevalier Gloves', 'Part 3: blue chest on the east route', 'Parte 3: baú azul na rota leste'),
    ('Fleeting Hope', 'Part 3: west route', 'Parte 3: rota oeste', B),
    ('Armor Soul+', 'Part 3: blue chest north of the northwest stream (jump with momentum)', 'Parte 3: baú azul ao norte do fluxo do noroeste (pule com impulso)'),
    ('Panacea III x3', 'Part 3: north corner of the north-central area', 'Parte 3: canto norte da área centro-norte'),
    ('Abiding Love', 'Part 3: southeast wall of the same area', 'Parte 3: parede sudeste da mesma área', B),
    ('Dark Seastone x3', 'Part 3: southwest ledge of the northeast section', 'Parte 3: borda sudoeste da seção nordeste', B),
    ('Limitless Courage+', 'Part 3: red chest at the top center', 'Parte 3: baú vermelho no centro, no alto'),
], LAST, S10F, until=FINAL)

# ======================================================================== Epilogue
c = chapter(11, 'Epilogue', 'Epílogo')
LEAVE = c.cp('Departing from the Carnac docks', 'Partir das docas de Carnac')
c.item('missable', t('Last character notes in Carnac (6)', 'Últimas notas de personagem em Carnac (6)'), t('Carnac'), LEAVE,
       t('Talk to these six before talking to Karja at the pier, or the all-notes trophy is lost. A bonus Runestone scene waits in the Lighthouse depths, by the west wall.',
         'Fale com estes seis antes de falar com a Karja no píer, ou o troféu de todas as notas se perde. Uma cena bônus de Runestone espera no fundo do farol, junto à parede oeste.'),
       0, [NEO('Epilogue'), GF('Epilogue')],
       steps=[t('Gunnar — near the Lighthouse entrance (Haagen Highway)', 'Gunnar — perto da entrada do farol (Haagen Highway)'),
              t('Sache — town square', 'Sache — praça da cidade'),
              t('Mayor Clement — by the Vigilante Corps Office', 'Prefeito Clement — junto ao escritório do Vigilante Corps'),
              t('Cohen — north of Grenn', 'Cohen — ao norte do Grenn'),
              t('Corinne — outside the Rusveri Inn', 'Corinne — em frente à Rusveri Inn'),
              t('Momina — southeast side of town', 'Momina — lado sudeste da cidade')])

for c in CH.values():
    c.write()
