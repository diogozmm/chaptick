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
