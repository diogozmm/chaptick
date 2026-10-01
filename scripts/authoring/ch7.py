# Chapter 7 — rewritten in our own words from the GameFAQs walkthrough by shockinblue (facts only).
# Chest counts per tower are approximate (counted from a route description).
# Once published, never reorder or remove items: ids are derived from order.
from lib import Chapter, gf, t

G = gf('Chapter 7 - Tetracyclic Towers')

c = Chapter(7, 'Chapter 7', 'Capítulo 7')
T1 = c.cp('The boss at the top of the first tower', 'O boss no topo da primeira torre')
T2 = c.cp('The boss at the top of the second tower', 'O boss no topo da segunda torre')
T3 = c.cp('The boss at the top of the third tower', 'O boss no topo da terceira torre')
T4 = c.cp('The boss at the top of the fourth tower (end of Chapter 7)', 'O boss no topo da quarta torre (fim do Capítulo 7)')

c.item('collectible', t('Liberl News Issue 9'), t('Your airship — cafeteria', 'Seu airship — cafeteria'), T4,
       t('Sold at the cafeteria counter.', 'Vendido no balcão da cafeteria.'), 0, [G])
c.item('collectible', t('Recipes: airship cafeteria (3)', 'Receitas: cafeteria do airship (3)'), t('Your airship — cafeteria', 'Seu airship — cafeteria'), T4,
       t('Seafood Gelatin, Victor\'s Steak and Platinum Risotto.', 'Seafood Gelatin, Victor\'s Steak e Platinum Risotto.'), 0, [G])
c.item('collectible', t('Gambler Jack — Vol. 10'), t('Your airship — south deck', 'Seu airship — convés sul'), T4,
       t('Talk to Antoine after the second tower.', 'Fale com o Antoine depois da segunda torre.'), 0, [G])
c.item('collectible', t('Data crystals: first tower (4)', 'Cristais de dados: primeira torre (4)'), t('Shadow Esmelas Tower — 4th level', 'Shadow Esmelas Tower — 4º nível'), T1,
       t('One at the red marker, three at the optional terminals around the ring-shaped floor. Hand them to the professor on the airship.',
         'Um no marcador vermelho e três nos terminais opcionais ao redor do andar em anel. Entregue ao professor no airship.'),
       0, [G])
c.item('collectible', t('Data crystals: second tower (4)', 'Cristais de dados: segunda torre (4)'), t('Shadow Carnelia Tower — 3rd level', 'Shadow Carnelia Tower — 3º nível'), T2,
       t('All four sit along the circular path on the 3rd level.', 'Os quatro ficam ao longo do caminho circular do 3º nível.'), 0, [G])
c.item('collectible', t('Data crystals: third tower (4)', 'Cristais de dados: terceira torre (4)'), t('Shadow Sapphirl Tower'), T3,
       t('One terminal on each level from the 2nd to the 5th, after each ambush.', 'Um terminal em cada nível, do 2º ao 5º, depois de cada emboscada.'), 0, [G])
c.item('collectible', t('Data crystals: fourth tower (4)', 'Cristais de dados: quarta torre (4)'), t('Shadow Amberl Tower — 5th level', 'Shadow Amberl Tower — 5º nível'), T4,
       t('Two on the west side early on, two at the terminals you reach at the end of the big loop.', 'Dois no lado oeste logo no início e dois nos terminais que você alcança no fim da grande volta.'),
       0, [G])
c.item('collectible', t('Shadow Esmelas Tower treasure chests (~22)', 'Baús da Shadow Esmelas Tower (~22)'), t('Shadow Esmelas Tower'), T1,
       t('Two teleporters on the 3rd level each lead to a room with five chests. Monster chest on the 3rd level (Photon Judge E+ survives one lethal hit). Some armor is gender-locked.',
         'Dois teletransportes no 3º nível levam cada um a uma sala com cinco baús. Baú de monstros no 3º nível (o Photon Judge E+ sobrevive a um golpe letal). Algumas armaduras são exclusivas por gênero.'),
       0, [G])
c.item('collectible', t('Shadow Carnelia Tower treasure chests (~35)', 'Baús da Shadow Carnelia Tower (~35)'), t('Shadow Carnelia Tower'), T2,
       t('Seven right at the start. The monster chest is reached through a teleporter down to the 2nd level. The 5th level is a chain of platforms with chests on every fork.',
         'Sete logo no início. O baú de monstros fica depois de um teletransporte que desce ao 2º nível. O 5º nível é uma sequência de plataformas com baús em cada bifurcação.'),
       0, [G])
c.item('collectible', t('Shadow Sapphirl Tower treasure chests (~23)', 'Baús da Shadow Sapphirl Tower (~23)'), t('Shadow Sapphirl Tower'), T3,
       t('Look behind the big teleporter walls on the 5th level. Monster chest on the west side of the 5th level. Blue electricity on the floor causes Mute.',
         'Olhe atrás das paredes dos teletransportes grandes no 5º nível. Baú de monstros no lado oeste do 5º nível. A eletricidade azul no chão causa Mute.'),
       0, [G])
c.item('collectible', t('Shadow Amberl Tower treasure chests (~30)', 'Baús da Shadow Amberl Tower (~30)'), t('Shadow Amberl Tower'), T4,
       t('The floors form one big loop of teleporters; activate the healing device on the 5th level for fast travel. The monster chest is in the grid on the 4th level.',
         'Os andares formam uma grande volta de teletransportes; ative o dispositivo de cura no 5º nível para a viagem rápida. O baú de monstros fica na grade do 4º nível.'),
       0, [G])

# ---------------------------------------------------------------- routes (append-only once published)
c.set_steps('sc-ch7-co-08', [
    t('2nd level, second fork east — U-Material+ ×2', '2º nível, segunda bifurcação a leste — U-Material+ ×2'),
    t('First fork east, upstairs past the shock floor — Tearal Balm', 'Primeira bifurcação a leste, subindo depois do piso de choque — Tearal Balm'),
    t('North at the fork — Caledfwlch', 'Ao norte na bifurcação — Caledfwlch'),
    t('Continue east — EP Charge III', 'Siga a leste — EP Charge III'),
    t('3rd level, left fork: teleporter up to a room with 5 chests', '3º nível, bifurcação esquerda: teletransporte até uma sala com 5 baús'),
    t('3rd level, right fork then north: teleporter to another room with 5 chests', '3º nível, bifurcação direita e depois norte: teletransporte até outra sala com 5 baús'),
    t('3rd level, the remaining path — monster chest: Esmelas Earrings', '3º nível, o caminho restante — baú de monstros: Esmelas Earrings'),
    t('North of it — Droplet of Defense', 'Ao norte dele — Droplet of Defense'),
    t('4th level, right in front — Taiji Gi', '4º nível, logo em frente — Taiji Gi'),
    t('4th level, south before the teleporter — Bagua Gi', '4º nível, ao sul antes do teletransporte — Bagua Gi'),
    t('5th level, east fork with three S-Pom the Origin (4 chests) — Elixir of Defense, All Sepith ×300, Time\'s Edge, Athelas Balm EX', '5º nível, bifurcação leste com três S-Pom the Origin (4 baús) — Elixir of Defense, All Sepith ×300, Time\'s Edge, Athelas Balm EX'),
], source=G)
c.set_steps('sc-ch7-co-09', [
    t('1st level, seven chests right ahead', '1º nível, sete baús logo à frente'),
    t('2nd level, east and up the stairs — Tearal Balm', '2º nível, leste e escada acima — Tearal Balm'),
    t('2nd level, west across the lava, past the teleporter to the end — Droplet of Strength', '2º nível, oeste pela lava, depois do teletransporte até o fim — Droplet of Strength'),
    t('3rd level, north fork (3 chests) — Xuanwu Shell, Tearal Balm, Zheque Bow', '3º nível, bifurcação norte (3 baús) — Xuanwu Shell, Tearal Balm, Zheque Bow'),
    t('3rd level west, teleporter down to the 2nd level, south (3 chests) — All Sepith ×300, U-Material+, EP Charge III', '3º nível a oeste, teletransporte ao 2º nível, sul (3 baús) — All Sepith ×300, U-Material+, EP Charge III'),
    t('Same spot — monster chest: Carnelia Bracelet', 'Mesmo lugar — baú de monstros: Carnelia Bracelet'),
    t('North teleporter back to the 3rd level, downstairs (2 chests) — EP Charge III, Athelas Balm ×2', 'Teletransporte norte de volta ao 3º nível, escada abaixo (2 baús) — EP Charge III, Athelas Balm ×2'),
    t('Along that path (2 chests) — Tearal Balm, Droplet of Life', 'Nesse caminho (2 baús) — Tearal Balm, Droplet of Life'),
    t('4th level, west teleporter to the 5th (3 chests) — EP Charge III, U-Material+, Blue Falcon', '4º nível, teletransporte oeste até o 5º (3 baús) — EP Charge III, U-Material+, Blue Falcon'),
    t('Northeast teleporter to the 5th (2 chests) — Taiji Gi, Tearal Balm', 'Teletransporte nordeste até o 5º (2 baús) — Taiji Gi, Tearal Balm'),
    t('Main 5th level, southeast — EP Charge III', '5º nível principal, sudeste — EP Charge III'),
    t('Southwest platform (2 chests) — All Sepith ×300, U-Material+ ×2', 'Plataforma sudoeste (2 baús) — All Sepith ×300, U-Material+ ×2'),
    t('South path, east platform (2 chests) — Tearal Balm, Carnelia Gem', 'Caminho sul, plataforma leste (2 baús) — Tearal Balm, Carnelia Gem'),
    t('Next platform (2 chests) — Athelas Balm EX, EP Charge III', 'Plataforma seguinte (2 baús) — Athelas Balm EX, EP Charge III'),
    t('Next platform — Elixir of Strength', 'Plataforma seguinte — Elixir of Strength'),
    t('Last platform before the healing device (2 chests) — Tear All Balm, EP Charge IV', 'Última plataforma antes do dispositivo de cura (2 baús) — Tear All Balm, EP Charge IV'),
], source=G)
c.set_steps('sc-ch7-co-10', [
    t('2nd level, south (6 chests) — All Sepith ×300, U-Material+, Droplet of Spirit, U-Material+ ×2, Tearal Balm, EP Charge III', '2º nível, ao sul (6 baús) — All Sepith ×300, U-Material+, Droplet of Spirit, U-Material+ ×2, Tearal Balm, EP Charge III'),
    t('3rd level, first chest — Avenger', '3º nível, primeiro baú — Avenger'),
    t('3rd level, the next four — All Sepith ×300, Droplet of Life, Tearal Balm, EP Charge III', '3º nível, os quatro seguintes — All Sepith ×300, Droplet of Life, Tearal Balm, EP Charge III'),
    t('4th level, first chest — Dragon\'s Tooth', '4º nível, primeiro baú — Dragon\'s Tooth'),
    t('4th level, the next three — Tearal Balm, Bagua Gi, EP Charge IV', '4º nível, os três seguintes — Tearal Balm, Bagua Gi, EP Charge IV'),
    t('5th level, behind the teleporter wall — Sapphirl Gem', '5º nível, atrás da parede do teletransporte — Sapphirl Gem'),
    t('5th level, west — monster chest: Sapphirl Ring', '5º nível, oeste — baú de monstros: Sapphirl Ring'),
    t('5th level, the other five — Tear All Balm, Athelas Balm EX, Regina Girders, Elixir of Spirit, U-Material+ ×2', '5º nível, os outros cinco — Tear All Balm, Athelas Balm EX, Regina Girders, Elixir of Spirit, U-Material+ ×2'),
    t('Behind the north teleporter — U-Material+', 'Atrás do teletransporte norte — U-Material+'),
], source=G)
c.set_steps('sc-ch7-co-11', [
    t('1st level, both sides of the north teleporter (2 chests) — All Sepith ×300, Curia Balm ×3', '1º nível, dos dois lados do teletransporte norte (2 baús) — All Sepith ×300, Curia Balm ×3'),
    t('2nd level (2 chests) — U-Material+ ×2, Tearal Balm', '2º nível (2 baús) — U-Material+ ×2, Tearal Balm'),
    t('3rd level (2 chests) — EP Charge III ×2', '3º nível (2 baús) — EP Charge III ×2'),
    t('5th level, start of the loop — Esmelas Gem', '5º nível, início da volta — Esmelas Gem'),
    t('4th level grid, west then north — Tempest Cannon', 'Grade do 4º nível, oeste e depois norte — Tempest Cannon'),
    t('4th level grid (3 chests) — EP Charge IV, Tear All Balm, U-Material+', 'Grade do 4º nível (3 baús) — EP Charge IV, Tear All Balm, U-Material+'),
    t('4th level grid, south — monster chest: Amberl Necklace', 'Grade do 4º nível, sul — baú de monstros: Amberl Necklace'),
    t('3rd level, southwest — Amberl Gem', '3º nível, sudoeste — Amberl Gem'),
    t('2nd level, southwest past the S-Poms (4 chests) — All Sepith ×300, EP Charge III, Tearal Balm, Droplet of Magic', '2º nível, sudoeste depois dos S-Poms (4 baús) — All Sepith ×300, EP Charge III, Tearal Balm, Droplet of Magic'),
    t('3rd level, northeast — Tearal Balm', '3º nível, nordeste — Tearal Balm'),
    t('5th level, northeast (2 chests) — Elixir of Magic, Arhat Staff', '5º nível, nordeste (2 baús) — Elixir of Magic, Arhat Staff'),
    t('5th level, around the healing device (3 chests) — All Sepith ×300, Athelas Balm EX, Droplet of Life', '5º nível, ao redor do dispositivo de cura (3 baús) — All Sepith ×300, Athelas Balm EX, Droplet of Life'),
    t('3rd level, northwest — U-Material+ ×2', '3º nível, noroeste — U-Material+ ×2'),
    t('2nd level, northwest (4 chests) — Droplet of Life, U-Material+, Tearal Balm, Zeram Capsule', '2º nível, noroeste (4 baús) — Droplet of Life, U-Material+, Tearal Balm, Zeram Capsule'),
    t('3rd level, southeast — All Sepith ×300', '3º nível, sudeste — All Sepith ×300'),
    t('4th level, southeast — EP Charge III', '4º nível, sudeste — EP Charge III'),
], source=G)

# ---------------------------------------------------------------- bosses
c.boss(t('Bleublanc'), t('Shadow Esmelas Tower — top', 'Shadow Esmelas Tower — topo'),
       t('Two strong earth arts clear his clowns. He fills the field with copies (a wide S-Craft wipes them) and loves ailments, including Pommify and Misfortune: bring debuff-curing crafts or plenty of Curia Balms.',
         'Duas arts de terra fortes eliminam os palhaços. Ele enche o campo de cópias (um S-Craft amplo apaga todas) e adora efeitos negativos, inclusive Pommify e Misfortune: leve crafts que curam debuffs ou muitos Curia Balms.'),
       sources=[G])
c.boss(t('Walter'), t('Shadow Carnelia Tower — top', 'Shadow Carnelia Tower — topo'),
       t('Comes with three Steel Cougars and survives one lethal hit. Shields and Earth Guard matter: one of his attacks breaks through a shield and nearly kills. Ends Rage Boost with an area S-Break.',
         'Vem com três Steel Cougars e sobrevive a um golpe letal. Escudos e Earth Guard importam: um dos ataques dele atravessa o escudo e quase mata. Termina o Rage Boost com um S-Break em área.'),
       sources=[G])
c.boss(t('Luciola'), t('Shadow Sapphirl Tower — top', 'Shadow Sapphirl Tower — topo'),
       t('Brings back weaker versions of the mist guardians from Chapter 4 (physical-only and arts-only). Bring Sleep protection first, then Burn; her S-Break burns an area.',
         'Traz versões mais fracas dos guardiões da névoa do Capítulo 4 (um só apanha de golpes físicos, o outro só de arts). Leve primeiro proteção contra Sleep e depois contra Burn; o S-Break dela queima uma área.'),
       sources=[G])
c.boss(t('The last tower\'s two-stage fight', 'A luta em duas fases da última torre'), t('Shadow Amberl Tower — roof', 'Shadow Amberl Tower — terraço'),
       t('Bring Deathblow protection (Grail Locket, Blue Sphere+, Skull Pendant+). Use Earth Wall or Gaia Shield, since Earth Guard does little against the second phase, a giant machine that reflects attacks during its boost.',
         'Leve proteção contra Deathblow (Grail Locket, Blue Sphere+, Skull Pendant+). Use Earth Wall ou Gaia Shield, porque o Earth Guard pouco adianta contra a segunda fase, uma máquina gigante que reflete ataques durante o reforço.'),
       sources=[G])

# ---------------------------------------------------------------- recipes
for name in ('Seafood Gelatin', "Victor's Steak", 'Platinum Risotto'):
    c.recipe(name, t('Airship cafeteria', 'Cafeteria do airship'), sources=[G])

c.write()
