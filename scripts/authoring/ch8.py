# Chapter 8 — rewritten in our own words from the Neoseeker walkthrough (facts only).
# All of Liberl is open: quests are grouped by region and share one point of no return.
# Once published, never reorder or remove items: ids are derived from order.
from lib import Chapter, src, t

INTRO = src('Chapter 8 - Introduction')
BOSE = src('Chapter 8 - Bose')
ROLENT = src('Chapter 8 - Rolent')
RUAN = src('Chapter 8 - Ruan')
ZEISS = src('Chapter 8 - Zeiss')
GRANCEL = src('Chapter 8 - Grancel')
FINAL = src('Chapter 8 - Final Part')

c = Chapter(8, 'Chapter 8', 'Capítulo 8')
PNR = c.cp('Choosing to contact the castle from a Bracer Guild (you cannot roam Liberl afterwards)',
           'Escolher contatar o castelo em uma guilda (depois disso não dá mais para percorrer Liberl)')
END = c.cp('The last event marker of Chapter 8', 'O último marcador de evento do Capítulo 8')


def L(*pairs):
    return [t(en, pt) for en, pt in pairs]


def quest(name, loc, until, reward, overview, steps=None, warnings=(), prep=(), req=(), srcs=(), type_='quest', level=0):
    """One checklist item with explicit guidance; the hint repeats it as the plain summary."""
    guidance = {'rewards': L(reward), 'overview': t(*overview)}
    if warnings:
        guidance['warnings'] = L(*warnings)
    if prep:
        guidance['preparation'] = L(*prep)
    if req:
        guidance['requirements'] = L(*req)
    hint_en = ' '.join([f'Reward: {reward[0]}', overview[0]] + [w[0] for w in warnings])
    hint_pt = ' '.join([f'Recompensa: {reward[1]}', overview[1]] + [w[1] for w in warnings])
    return c.item(type_, name, loc, until, t(hint_en, hint_pt), level, list(srcs),
                  steps=[t(*s) for s in steps] if steps else None, guidance=guidance)


# ------------------------------------------------------------------ Bose
LIFELINE = quest(
    t("Lugran's Lifeline"), t('Bose — Bracer Guild', 'Bose — guilda dos bracers'), PNR,
    ('+5 BP, +1 BP bonus.', '+5 BP, +1 BP de bônus.'),
    ('A fetch quest that crosses half of Liberl. Pick the third option (the embassy) when asked, to earn the extra BP.',
     'Uma quest de busca que cruza metade de Liberl. Escolha a terceira opção (a embaixada) quando perguntarem, para ganhar o BP extra.'),
    steps=[
        ('Talk to Lugran at the Bose guild, then to Sting in Ravennue Village, then go back to the guild.',
         'Fale com Lugran na guilda de Bose, depois com Sting em Ravennue Village e volte à guilda.'),
        ('Choose the third option, "Calvard Embassy", for the bonus BP.', 'Escolha a terceira opção, "Calvard Embassy", para o BP de bônus.'),
        ('Dragon Claw: talk to Orvid in Anterose Restaurant, go to Nebel Valley, fast travel to the entrance of Ancient Dragon\'s Lair and examine the plant at the north end of the boss room.',
         'Dragon Claw: fale com Orvid no Anterose Restaurant, vá a Nebel Valley, use a viagem rápida até a entrada de Ancient Dragon\'s Lair e examine a planta no extremo norte da sala do boss.'),
        ('Ox Bezoar: in Grancel, ask Ambassador Cochrane at the Calvard Embassy (East Block), follow her to the shop in the West Block, between the Cathedral and Baral Coffee House, and buy it for 5,000 mira.',
         'Ox Bezoar: em Grancel, fale com a embaixadora Cochrane na Calvard Embassy (East Block), siga-a até a loja no West Block, entre a Cathedral e o Baral Coffee House, e compre por 5.000 mira.'),
        ('Hand both items to Spence in the Bose Market.', 'Entregue os dois itens a Spence no Bose Market.'),
    ],
    warnings=[('Grancel has to be reached on foot first, so leave the Bezoar for when you pass through there.',
               'Grancel precisa ser alcançada a pé antes, então deixe o Bezoar para quando passar por lá.')],
    srcs=[BOSE, GRANCEL])
KRONE = quest(
    t('Krone Pass Monster'), t('West Bose Highway — Krone Trail', 'West Bose Highway — Krone Trail'), PNR,
    ('+5 BP. Guaranteed drop: Mute II.', '+5 BP. Drop garantido: Mute II.'),
    ('Red Fangs, like the Blade Fangs of Chapter 5. They survive a lethal hit and enter Rage Boost near death, so keep an S-Break ready.',
     'Red Fangs, como os Blade Fangs do Capítulo 5. Sobrevivem a um golpe letal e entram em Rage Boost perto da morte, então guarde um S-Break.'),
    srcs=[BOSE])
ANSEL = quest(
    t('Ansel Path Monster'), t('New Ansel Path — main intersection', 'New Ansel Path — cruzamento principal'), PNR,
    ('+5 BP. Guaranteed drop: Burn II.', '+5 BP. Drop garantido: Burn II.'),
    ('Doom Type S with weak helpers. Their Double Tomahawk can cause Deathblow and All Cancel, and they enter Rage Boost under half HP. Delay and Stat Down work well.',
     'Doom Type S com ajudantes fracos. O Double Tomahawk pode causar Deathblow e All Cancel, e eles entram em Rage Boost com menos da metade do HP. Delay e Stat Down funcionam bem.'),
    srcs=[BOSE])

# ------------------------------------------------------------------ Rolent
MILCH = quest(
    t('Milch Monster'), t('Milch Main Road — northeast of the middle intersection', 'Milch Main Road — nordeste do cruzamento do meio'), PNR,
    ('+5 BP. Guaranteed drop: Confuse II.', '+5 BP. Drop garantido: Confuse II.'),
    ('Devil Spears: nearly every attack poisons, and Deadly Poison Stinger can Deathblow. Block ailments with Debuff Immunity and budget an S-Break for their revive.',
     'Devil Spears: quase todo ataque envenena, e o Deadly Poison Stinger pode causar Deathblow. Bloqueie os efeitos com Debuff Immunity e reserve um S-Break para a revivência deles.'),
    srcs=[ROLENT])
ELIZE = quest(
    t('Elize Hwy Monster'), t('Elize Highway — Mistwald entrance', 'Elize Highway — entrada de Mistwald'), PNR,
    ('+5 BP. Guaranteed drop: Petrify II.', '+5 BP. Drop garantido: Petrify II.'),
    ('Two Vanguards with five Vogel 911 EX. Burst the Vogels down with S-Breaks. Vanguards explode when destroyed, so keep your distance.',
     'Dois Vanguards com cinco Vogel 911 EX. Derrube os Vogels rápido com S-Breaks. Os Vanguards explodem ao serem destruídos, então mantenha distância.'),
    srcs=[ROLENT])
MINERS = quest(
    t("Miners' Mayday"), t('Rolent — Malga Mine', 'Rolent — Malga Mine'), PNR,
    ('+9 BP.', '+9 BP.'),
    ('Rescue five trapped miners, then face the monster nest. Defeat at least one Baby Cancer on the way (see the battle entry below).',
     'Resgate cinco mineiros presos e enfrente o ninho de monstros. Derrote ao menos um Baby Cancer no caminho (veja a entrada de batalha abaixo).'),
    steps=[
        ('Hand in the Zero Field Generator at the Rolent guild to open Malga Trail.', 'Entregue o Zero Field Generator na guilda de Rolent para abrir Malga Trail.'),
        ('Enter Malga Mine, follow the rails, talk to the miners and ride the elevator down.', 'Entre em Malga Mine, siga os trilhos, fale com os mineiros e desça pelo elevador.'),
        ('Rescue Bones (southwest marker, four Killer Cancers).', 'Resgate Bones (marcador sudoeste, quatro Killer Cancers).'),
        ('Rescue Mine Chief Garton (south, four more Killer Cancers).', 'Resgate o Mine Chief Garton (sul, mais quatro Killer Cancers).'),
        ('Rescue Heine and Plim (southeast path, three Killer Cancers).', 'Resgate Heine e Plim (caminho sudeste, três Killer Cancers).'),
        ('Defeat the Armored Hydra in the nest to the northwest.', 'Derrote a Armored Hydra no ninho a noroeste.'),
    ],
    req=[('The Rolent Bracer Guild must already have its Zero Field Generator.', 'A guilda de Rolent já precisa ter recebido o Zero Field Generator.')],
    srcs=[ROLENT])

# ------------------------------------------------------------------ Ruan
MANORIA = quest(
    t('Manoria Byroad Monster'), t('Manoria Byroad — south route to Varenne Lighthouse', 'Manoria Byroad — rota sul para Varenne Lighthouse'), PNR,
    ('+5 BP. Guaranteed drop: Sleep II.', '+5 BP. Drop garantido: Sleep II.'),
    ('Balancing Clowns, the same helpers Bleublanc had. They stack many ailments and rage at 75%, 50% and 25% HP. Debuff Immunity plus Joshua or Agate S-Breaks end it quickly.',
     'Balancing Clowns, os mesmos ajudantes do Bleublanc. Acumulam vários efeitos e entram em fúria com 75%, 50% e 25% do HP. Debuff Immunity e S-Breaks do Joshua ou do Agate resolvem rápido.'),
    srcs=[RUAN])
SEASIDE = quest(
    t('Seaside Way Monster'), t('Branch to Vista Forest Road, near Ruan', 'Bifurcação para Vista Forest Road, perto de Ruan'), PNR,
    ('+5 BP. Guaranteed drop: Cloak.', '+5 BP. Drop garantido: Cloak.'),
    ('A Rising Panda with four Sasa Pandas. Its Deathblow chance is much higher than the regular pandas\'. Burst the small ones first, then buff and protect against its ailments.',
     'Um Rising Panda com quatro Sasa Pandas. A chance de Deathblow dele é bem maior que a dos pandas comuns. Derrube os pequenos primeiro e depois se proteja de seus efeitos.'),
    srcs=[RUAN])
SAPPHIRL = quest(
    t('Sapphirl Tower Monster'), t('Sapphirl Tower — entrance', 'Sapphirl Tower — entrada'), PNR,
    ('+5 BP. Guaranteed drop: Freeze II.', '+5 BP. Drop garantido: Freeze II.'),
    ('Ebony Scales, a palette swap of the Guilder Quake. World Shaker hits everyone with Seal, Mute, Blind and AT Delay, so protect the party first.',
     'Ebony Scales, uma variação do Guilder Quake. O World Shaker acerta todos com Seal, Mute, Blind e AT Delay, então proteja a equipe antes.'),
    srcs=[RUAN])
ACADEMY = quest(
    t('Academy Attack'), t('Ruan — Jenis Royal Academy', 'Ruan — Jenis Royal Academy'), PNR,
    ('+9 BP and the Mighty Essence recipe.', '+9 BP e a receita Mighty Essence.'),
    ('Joshua scouts the campus alone, then the party clears every building and frees the hostages before the final fight at the Old Schoolhouse.',
     'Joshua explora o campus sozinho; depois a equipe limpa todos os prédios e liberta os reféns antes da luta final no Old Schoolhouse.'),
    steps=[
        ('Hand in the Zero Field Generator at the Ruan guild, then go east to Vista Forest Road.', 'Entregue o Zero Field Generator na guilda de Ruan e vá a leste, para Vista Forest Road.'),
        ('As Joshua, look through the windows around the academy perimeter and unlock the Old Schoolhouse gate.', 'Como Joshua, olhe pelas janelas ao redor do perímetro da academia e destrave o portão do Old Schoolhouse.'),
        ('Clubhouse: win the second-floor fight; Deborah in the left room gives you Mighty Essence.', 'Clubhouse: vença a luta do 2º andar; Deborah, na sala da esquerda, dá a Mighty Essence.'),
        ('Main Building: win the fights on both floors and free the hostages.', 'Main Building: vença as lutas nos dois andares e liberte os reféns.'),
        ('Girl\'s Dorm and Boy\'s Dorm: win each fight, then enter the room on the left / right.', 'Girl\'s Dorm e Boy\'s Dorm: vença cada luta e entre na sala da esquerda / direita.'),
        ('Old Schoolhouse: free the last hostage and win the boss fight.', 'Old Schoolhouse: liberte o último refém e vença a luta contra o boss.'),
    ],
    req=[('The Ruan Bracer Guild must already have its Zero Field Generator.', 'A guilda de Ruan já precisa ter recebido o Zero Field Generator.')],
    srcs=[RUAN])

# ------------------------------------------------------------------ Zeiss
KALDIA = quest(
    t('Kaldia Tunnel Monster'), t('Kaldia Tunnel — south at the branch nearest Zeiss', 'Kaldia Tunnel — sul, na bifurcação mais próxima de Zeiss'), PNR,
    ('+5 BP. Guaranteed drop: Divine Cloth (needed for Divine Cloth Z).', '+5 BP. Drop garantido: Divine Cloth (necessário para a Divine Cloth Z).'),
    ('The Divine Pengu again, now alone. It survives one lethal blow; save an S-Break to finish it. It can Confuse the whole party, so wear Confuse protection.',
     'O Divine Pengu de novo, agora sozinho. Ele sobrevive a um golpe letal; guarde um S-Break para finalizar. Pode causar Confuse na equipe toda, então use proteção contra Confuse.'),
    prep=[('The tunnel is pitch dark: equip Night-Vision Goggles (sold by Paul Elk in the Bose Market).',
           'O túnel é totalmente escuro: equipe Night-Vision Goggles (vendidos por Paul Elk no Bose Market).')],
    srcs=[ZEISS])
TRATT = quest(
    t('Tratt Plains Monster'), t('Tratt Plains Road — south of the way to Wolf Fort', 'Tratt Plains Road — ao sul do caminho para Wolf Fort'), PNR,
    ('+5 BP. Guaranteed drop: Poison II.', '+5 BP. Drop garantido: Poison II.'),
    ('Eight Abyss Worms that answer attacks with Earth-Shaker. Do not play it safe: spam Joshua and Agate S-Breaks with Burst until they fall.',
     'Oito Abyss Worms que respondem aos ataques com Earth-Shaker. Não jogue no seguro: use S-Breaks do Joshua e do Agate com Burst até derrubá-los.'),
    srcs=[ZEISS])
RITTER = quest(
    t('Ritter Rd Monster'), t('Ritter Roadway — just outside Zeiss', 'Ritter Roadway — logo na saída de Zeiss'), PNR,
    ('+5 BP. Guaranteed drop: Blind II.', '+5 BP. Drop garantido: Blind II.'),
    ('A Blade Cougar+ with seven Blade Cougars. Same plan as the Abyss Worms, but every cougar has Endure and needs an extra S-Break. Buff up if the strongest one survives.',
     'Um Blade Cougar+ com sete Blade Cougars. Mesmo plano das Abyss Worms, mas todos têm Endure e pedem um S-Break extra. Se o mais forte sobreviver, reforce os buffs.'),
    srcs=[ZEISS])
HOTSPRING = quest(
    t('Hot Springs Salvation'), t('Elmo Village — Maple Leaf Inn', 'Elmo Village — Maple Leaf Inn'), PNR,
    ('+9 BP, Ultra-Concentrated Herbal Tea ×4 and hot spring outfits.', '+9 BP, Ultra-Concentrated Herbal Tea ×4 e roupas de fontes termais.'),
    ('Find the two parts the village pump needs. Tita must be in the party, and the Zeiss guild must already have its Zero Field Generator.',
     'Encontre as duas peças de que a bomba da vila precisa. A Tita precisa estar na equipe, e a guilda de Zeiss já precisa ter recebido o Zero Field Generator.'),
    steps=[
        ('Talk to Mao at the Maple Leaf Inn for the Pump Shed Key, then open the shed north of town with Tita in the party.',
         'Fale com Mao na Maple Leaf Inn para pegar a Pump Shed Key e abra o galpão ao norte da vila com a Tita na equipe.'),
        ('Talk to Maintenance Chief Gustav at the Landing Port.', 'Fale com o Maintenance Chief Gustav no porto de airships.'),
        ('Ask Kilika at the Zeiss guild to contact Leiston Fortress.', 'Peça à Kilika, na guilda de Zeiss, para contatar Leiston Fortress.'),
        ('Talk to the Royal Army soldiers on Tratt Plains Road, south of Carnelia Tower: Combustion Engine.', 'Fale com os soldados do Exército Real em Tratt Plains Road, ao sul da Carnelia Tower: Combustion Engine.'),
        ('Talk to Rudi in the Zeiss Central Factory basement: Factory Chief Letter.', 'Fale com Rudi no subsolo da Zeiss Central Factory: Factory Chief Letter.'),
        ('Go to Ruan South Block (fast travel works), talk to Chief Portos, then to Harg further west: Gasoline Tank.', 'Vá ao South Block de Ruan (a viagem rápida funciona), fale com o Chief Portos e depois com Harg, mais a oeste: Gasoline Tank.'),
        ('Return to Elmo Village with Tita and finish the repair in the Pump Shed.', 'Volte a Elmo Village com a Tita e conclua o conserto no Pump Shed.'),
    ],
    req=[('Tita in the party.', 'Tita na equipe.')],
    srcs=[ZEISS])

# ------------------------------------------------------------------ Grancel
ERBE = quest(
    t('Erbe Scenic Route Monster'), t('Erbe Scenic Route — south of Erbe Royal Villa', 'Erbe Scenic Route — ao sul da Erbe Royal Villa'), PNR,
    ('+5 BP. Guaranteed drop: Seal II.', '+5 BP. Drop garantido: Seal II.'),
    ('A Big Cactus with seven Lark Cacti. Clear the small ones with S-Breaks, then guard against Poison, Blind and Confuse. It survives a lethal blow and rages at two-thirds and one-third HP.',
     'Um Big Cactus com sete Lark Cacti. Elimine os pequenos com S-Breaks e depois se proteja de Poison, Blind e Confuse. Ele sobrevive a um golpe letal e entra em fúria com dois terços e um terço do HP.'),
    srcs=[GRANCEL])
SEWER = quest(
    t('Sewer Monster'), t('Grancel Sewers — West Block', 'Grancel Sewers — West Block'), PNR,
    ('+5 BP. Guaranteed drop: Elixir of Spirit.', '+5 BP. Drop garantido: Elixir of Spirit.'),
    ('Three Evil Streams with low HP and many ailments. Attack first: fast kills avoid their drain moves and the party-capturing Dark Vacuum.',
     'Três Evil Streams com pouco HP e muitos efeitos. Ataque primeiro: matá-los rápido evita os golpes de drenagem e o Dark Vacuum, que captura membros da equipe.'),
    srcs=[GRANCEL])

# ------------------------------------------------------------------ Missables
BABY = c.item('missable', t('Battle entry: Baby Cancer', 'Entrada de batalha: Baby Cancer'), t('Malga Mine', 'Malga Mine'), PNR,
              t("Defeat at least one Baby Cancer on the field during Miners' Mayday, or it cannot be recorded in the handbook.",
                "Derrote ao menos um Baby Cancer no campo durante Miners' Mayday, ou ele não poderá ser registrado no handbook."),
              0, [ROLENT], guidance={'warnings': L(("You will not return to the mine after the quest, so the entry is lost if you skip these fights.",
                                                      'Você não volta à mina depois da quest, então a entrada se perde se você pular essas lutas.'))})
REWARDS = c.item('missable', t('Rewards that get harder after Liberl closes', 'Recompensas que ficam mais difíceis quando Liberl se fecha'), t('All of Liberl', 'Todo Liberl'), PNR,
                 t('Three in-game rewards need Liberl: winning medals at Lavantar Bar & Casino, cutting grass or flowers, and defeating enemies at once. Check your progress on them before contacting the castle.',
                   'Três recompensas do jogo dependem de Liberl: ganhar medalhas no Lavantar Bar & Casino, cortar grama ou flores e derrotar inimigos de uma vez. Confira seu progresso nelas antes de contatar o castelo.'),
                 0, [FINAL], guidance={'warnings': L(('After the point of no return these become much harder or impossible.',
                                                      'Depois do ponto sem volta elas ficam bem mais difíceis ou impossíveis.')),
                                       'overview': t('Winning medals at Lavantar Bar & Casino, cutting grass or flowers, and defeating enemies at once.',
                                                     'Ganhar medalhas no Lavantar Bar & Casino, cortar grama ou flores e derrotar inimigos de uma vez.')})
CHECKLIST = c.item('missable', t('Final check before contacting the castle', 'Conferência final antes de contatar o castelo'), t('Any Bracer Guild except Grancel', 'Qualquer guilda de bracers, exceto a de Grancel'), PNR,
                   t('After contacting the castle you cannot roam Liberl again. Compare your progress with the numbers below and cook the new recipes.',
                     'Depois de contatar o castelo você não percorre mais Liberl. Compare seu progresso com os números abaixo e cozinhe as receitas novas.'),
                   0, [FINAL], steps=[
                       t('437 BP before the story quest (452 after it, Rank A).', '437 BP antes da quest da história (452 depois, Rank A).'),
                       t('67 of 70 recipes, 26 of 26 fish, 25 of 26 books, 435 of 566 treasure chests.', '67 de 70 receitas, 26 de 26 peixes, 25 de 26 livros, 435 de 566 baús.'),
                       t('Cook every new recipe (80 of 87 dishes, 67 of 70 peculiar dishes). Flamboyant Candy Lei is not possible yet.', 'Cozinhe todas as receitas novas (80 de 87 pratos, 67 de 70 pratos peculiares). Flamboyant Candy Lei ainda não é possível.'),
                       t('Buy monster ingredients from Orvid (about 30 of each) for the Final Chapter recipes.', 'Compre ingredientes de monstros com Orvid (cerca de 30 de cada) para as receitas do Final Chapter.'),
                       t('Check the Combat Handbook: only the last Extra entry should be empty (Shining Poms, Dimension Bugs, Weatherseeds, Baby Cancer, Steel Cougar).', 'Confira o Combat Handbook: só a última entrada de Extra deve estar vazia (Shining Poms, Dimension Bugs, Weatherseeds, Baby Cancer, Steel Cougar).'),
                       t('Farm sepith, mira and U-Material+ for Gem quartz and True Gems; caves and water caves are good spots.', 'Faça farm de sepith, mira e U-Material+ para os quartzos Gem e True Gems; cavernas e cavernas com água são bons lugares.'),
                   ], guidance={
                       'preparation': L(('Optional but helpful on Nightmare: four Kitty Jackets (O\'Neil\'s Duty-Free Shop, Ruan) upgraded with Crescent Charms, and four Kitty Boots (Bell Station, Zeiss) upgraded with T-Anklets.',
                                         'Opcional, mas útil no Nightmare: quatro Kitty Jackets (O\'Neil\'s Duty-Free Shop, Ruan) melhorados com Crescent Charms e quatro Kitty Boots (Bell Station, Zeiss) melhorados com T-Anklets.')),
                       'optional': L(('Farm T-Anklet+ and Crescent Charm+ from Shining Pom+ in Rolent and Bose, or by catching rank A Snakehead and Gigangora.',
                                      'Faça farm de T-Anklet+ e Crescent Charm+ com Shining Pom+ em Rolent e Bose, ou pescando Snakehead e Gigangora de rank A.')),
                       'overview': t('Use this list before choosing "Contact the castle" at any guild other than Grancel\'s.',
                                     'Use esta lista antes de escolher "Contact the castle" em qualquer guilda que não seja a de Grancel.')})

# ------------------------------------------------------------------ Collectibles
c.item('collectible', t('Liberl News Issue 10'), t('Grancel — Edel Department Store, E. Block', 'Grancel — Edel Department Store, E. Block'), PNR,
       t('Sold at the general goods section of the department store in the East Block.', 'Vendido na seção de produtos gerais da loja de departamentos do East Block.'), 0, [GRANCEL])
c.item('collectible', t('Gambler Jack — Vol. 11'), t('Rolent — Abend Bar area', 'Rolent — região do Abend Bar'), PNR,
       t("Talk to Serra after finishing Miners' Mayday and watching the wedding at the chapel.", "Fale com Serra depois de terminar Miners' Mayday e ver o casamento na capela."), 0, [ROLENT])
c.item('collectible', t('Gambler Jack — Vol. 12'), t('Ruan — Jenis Royal Academy, Main Building', 'Ruan — Jenis Royal Academy, Main Building'), PNR,
       t('Talk to Violet after finishing Academy Attack.', 'Fale com Violet depois de terminar Academy Attack.'), 0, [RUAN])
c.item('collectible', t('Gambler Jack — Vol. 13'), t('Wolf Fort', 'Wolf Fort'), PNR,
       t('Talk to CWO Pace after finishing Hot Springs Salvation.', 'Fale com o CWO Pace depois de terminar Hot Springs Salvation.'), 0, [ZEISS])
c.item('collectible', t('Gambler Jack — Vol. 14'), t('Bose — Market', 'Bose — Market'), PNR,
       t('Talk to Minuet once two Zero Field Generators have been delivered.', 'Fale com Minuet depois de entregar dois Zero Field Generators.'), 0, [RUAN, ZEISS])
c.item('collectible', t('Zemurian Ore: Gambler Jack set', 'Zemurian Ore: coleção Gambler Jack'), t('Grancel — Baral Coffee House, W. Block', 'Grancel — Baral Coffee House, W. Block'), END,
       t('Hand all 14 Gambler Jack volumes to Baral. The ore is only used in the Final Chapter to forge the strongest weapons. If you miss Baral here, he is on the guild\'s third floor after the point of no return.',
         'Entregue os 14 volumes de Gambler Jack a Baral. O minério só é usado no Final Chapter para forjar as armas mais fortes. Se perder o Baral aqui, ele estará no 3º andar da guilda depois do ponto sem volta.'),
       0, [GRANCEL, FINAL])
c.item('collectible', t('Recipes: Liberl shops and rewards (12)', 'Receitas: lojas e recompensas de Liberl (12)'), t('Bose, Ravennue, Valleria Shore, Ruan, Zeiss, Grancel', 'Bose, Ravennue, Valleria Shore, Ruan, Zeiss, Grancel'), PNR,
       t('Twelve new recipes. Missed ones can be bought later at Dalmore Company in Grancel.', 'Doze receitas novas. As que você perder podem ser compradas depois na Dalmore Company, em Grancel.'),
       0, [BOSE, RUAN, ZEISS, GRANCEL], steps=[
           t('Profound Paste — Buck\'s Produce Shop, Bose Market', 'Profound Paste — Buck\'s Produce Shop, Bose Market'),
           t('Boney Meat — Trayton Foods, Bose Market', 'Boney Meat — Trayton Foods, Bose Market'),
           t('Sadist Monster Stew — Kirsche Bar, Bose', 'Sadist Monster Stew — Kirsche Bar, Bose'),
           t("Aidios' Paradise — The Moonlight Path, Ravennue Village", "Aidios' Paradise — The Moonlight Path, Ravennue Village"),
           t('Aurora Beans — talk to Ray at Krone Pass Checkpoint', 'Aurora Beans — fale com Ray no Krone Pass Checkpoint'),
           t('Giblet Tempura — The Kingfisher Inn, Valleria Shore', 'Giblet Tempura — The Kingfisher Inn, Valleria Shore'),
           t('Pinkish Delight — The Kingfisher Inn, Valleria Shore', 'Pinkish Delight — The Kingfisher Inn, Valleria Shore'),
           t('Mighty Essence — given by Deborah during Academy Attack', 'Mighty Essence — dada por Deborah durante Academy Attack'),
           t('Mountain Man Stew — Maple Leaf Inn, Elmo Village', 'Mountain Man Stew — Maple Leaf Inn, Elmo Village'),
           t('Protein Hot Pot — Sanktheim Gate cafeteria', 'Protein Hot Pot — cafeteria do Sanktheim Gate'),
           t('Ultra-Concentrated Herbal Tea — reward for Hot Springs Salvation', 'Ultra-Concentrated Herbal Tea — recompensa de Hot Springs Salvation'),
           t('Ultima Ice Cream — Sorbet\'s Ice Cream Shop, Grancel East Block', 'Ultima Ice Cream — Sorbet\'s Ice Cream Shop, Grancel East Block'),
       ])
c.item('collectible', t('Divine Cloth Z', 'Divine Cloth Z'), t('Rooftops of the four towers', 'Terraços das quatro torres'), PNR,
       t('Defeat the Dimension Bug+ on each tower roof for an orb, add the Divine Cloth from the Kaldia Tunnel monster, and exchange the five items for Divine Cloth Z.',
         'Derrote o Dimension Bug+ no terraço de cada torre para obter um orbe, some o Divine Cloth do monstro do Kaldia Tunnel e troque os cinco itens pela Divine Cloth Z.'),
       0, [BOSE, ROLENT, RUAN, ZEISS], steps=[
           t('Amberl Tower (Bose region) — Shield Orb', 'Amberl Tower (região de Bose) — Shield Orb'),
           t('Esmelas Tower (Rolent, after delivering the generator) — Soul Orb', 'Esmelas Tower (Rolent, depois de entregar o gerador) — Soul Orb'),
           t('Sapphirl Tower (Ruan region) — Mind Orb', 'Sapphirl Tower (região de Ruan) — Mind Orb'),
           t('Carnelia Tower (Zeiss region) — Power Orb', 'Carnelia Tower (região de Zeiss) — Power Orb'),
           t('Divine Cloth — Kaldia Tunnel monster quest', 'Divine Cloth — quest do monstro do Kaldia Tunnel'),
       ])
c.item('collectible', t('Hades Gem', 'Hades Gem'), t('Wolf Fort', 'Wolf Fort'), PNR,
       t('Talk to Gundolf after defeating the Abyss Worms nearby.', 'Fale com Gundolf depois de derrotar as Abyss Worms nas proximidades.'), 0, [ZEISS])

# ------------------------------------------------------------------ Bosses
c.boss(t('Red Fangs'), t('West Bose Highway — Krone Trail', 'West Bose Highway — Krone Trail'),
       t('Only pure-damage attacks. When they are about to die they use Indomitable Will and rage, so hold an S-Break for the revive.',
         'Só ataques de dano puro. Quando estão para morrer usam Indomitable Will e entram em fúria, então guarde um S-Break para a revivência.'),
       related=KRONE, sources=[BOSE])
c.boss(t('Doom Type S'), t('New Ansel Path', 'New Ansel Path'),
       t('Weak to Delay and Stat Down. Double Tomahawk can Deathblow and All Cancel; they rage below half HP.',
         'Fracos a Delay e Stat Down. O Double Tomahawk pode causar Deathblow e All Cancel; entram em fúria com menos da metade do HP.'),
       related=ANSEL, sources=[BOSE])
c.boss(t('Devil Spears'), t('Milch Main Road', 'Milch Main Road'),
       t('Poison on nearly everything, plus Deathblow, All Cancel and a Venom Ring zone. Debuff Immunity first; keep an S-Break for their revive.',
         'Veneno em quase tudo, além de Deathblow, All Cancel e uma zona de Venom Ring. Debuff Immunity primeiro; guarde um S-Break para a revivência.'),
       related=MILCH, sources=[ROLENT])
c.boss(t('Vanguards and Vogel 911 EX'), t('Elize Highway — Mistwald entrance', 'Elize Highway — entrada de Mistwald'),
       t('The Vogels inflict Poison, Petrify, Burn, Seal and Blind and rage after losing a quarter of their HP. Kill them first with S-Breaks; the Vanguards explode when destroyed.',
         'Os Vogels causam Poison, Petrify, Burn, Seal e Blind e entram em fúria ao perder um quarto do HP. Elimine-os primeiro com S-Breaks; os Vanguards explodem ao serem destruídos.'),
       related=ELIZE, sources=[ROLENT])
c.boss(t('Armored Hydra'), t('Malga Mine — monster nest', 'Malga Mine — ninho de monstros'),
       t('A stronger Abyss Worm. It always answers hits with Earth-Shaker (big party damage and AT Delay) and calls Killer Cancers. Shields and Debuff Immunity soften it; wipe the cancers with S-Breaks, then focus the Hydra before it rages.',
         'Uma Abyss Worm mais forte. Responde a golpes sempre com Earth-Shaker (muito dano na equipe e AT Delay) e chama Killer Cancers. Escudos e Debuff Immunity amenizam; elimine os cancers com S-Breaks e depois foque na Hydra antes da fúria.'),
       related=MINERS, sources=[ROLENT])
c.boss(t('Balancing Clowns'), t('Manoria Byroad', 'Manoria Byroad'),
       t('Seal, Mute, Blind, Confuse, AT Delay and All Cancel, and Dazzling Climax drains EP and CP. Debuff Immunity, then burst them down.',
         'Seal, Mute, Blind, Confuse, AT Delay e All Cancel, e o Dazzling Climax drena EP e CP. Debuff Immunity e depois derrube-os rápido.'),
       related=MANORIA, sources=[RUAN])
c.boss(t('Rising Panda'), t('Near Ruan — Vista Forest Road branch', 'Perto de Ruan — bifurcação de Vista Forest Road'),
       t('Burst down the four Sasa Pandas, then buff with shields, Foresight and Debuff Immunity. It can rage with Requiem of the Panda if the fight drags on.',
         'Derrube rápido os quatro Sasa Pandas e depois use escudos, Foresight e Debuff Immunity. Pode entrar em fúria com Requiem of the Panda se a luta se arrastar.'),
       related=SEASIDE, sources=[RUAN])
c.boss(t('Ebony Scales'), t('Sapphirl Tower — entrance', 'Sapphirl Tower — entrada'),
       t('Heavy Tail Crush (AT Delay, Impede), World Shaker (Seal, Mute, Blind, AT Delay on everyone) and Ragna Blast (Seal). Be protected before it acts, and finish them before they rage.',
         'Heavy Tail Crush (AT Delay, Impede), World Shaker (Seal, Mute, Blind, AT Delay em todos) e Ragna Blast (Seal). Esteja protegido antes de ele agir e termine antes da fúria.'),
       related=SAPPHIRL, sources=[RUAN])
c.boss(t('Gilbert'), t('Jenis Royal Academy — Old Schoolhouse', 'Jenis Royal Academy — Old Schoolhouse'),
       t('Summons Vogel 235 reinforcements and Photon Laws, and hurts himself with some of his own moves. S-Break the Vogels at the start, then beat him down; he rages below half HP.',
         'Invoca reforços Vogel 235 e Photon Laws, e se machuca com alguns dos próprios golpes. Use S-Breaks nos Vogels no começo e depois derrube-o; ele entra em fúria com menos da metade do HP.'),
       related=ACADEMY, sources=[RUAN])
c.boss(t('Divine Pengu'), t('Kaldia Tunnel', 'Kaldia Tunnel'),
       t('Swordfish moves cause DEF/ADF Down and Deathblow, Samba de Pengu almost always Confuses, and it heals with Snacktime. Buff, burst it down before it rages, and S-Break through its Endure.',
         'Os golpes Swordfish causam DEF/ADF Down e Deathblow, o Samba de Pengu quase sempre causa Confuse e ele se cura com Snacktime. Reforce os buffs, derrube antes da fúria e use um S-Break para vencer o Endure.'),
       related=KALDIA, sources=[ZEISS])
c.boss(t('Abyss Worms (eight)', 'Abyss Worms (oito)'), t('Tratt Plains Road — toward Wolf Fort', 'Tratt Plains Road — rumo a Wolf Fort'),
       t('Unlike the Chapter 2 fight, go all out: Joshua\'s Phantom Raid with Burst on repeat, then Agate\'s Final Break II (not Dragon Dive) when out of CP, and Joshua again at 100 CP.',
         'Ao contrário da luta do Capítulo 2, vá com tudo: Phantom Raid do Joshua com Burst em repetição, depois o Final Break II do Agate (não o Dragon Dive) quando faltar CP, e o Joshua de novo com 100 CP.'),
       related=TRATT, sources=[ZEISS])
c.boss(t('Blade Cougar+ and Blade Cougars'), t('Ritter Roadway', 'Ritter Roadway'),
       t('Blade attacks cause Seal, Deathblow and AT Delay, and they rage at 75% and 25% HP. Spam S-Breaks with Burst as in the worm fight; the stronger cougar may be left, so protect yourself then.',
         'Os golpes de lâmina causam Seal, Deathblow e AT Delay, e eles entram em fúria com 75% e 25% do HP. Use S-Breaks com Burst como na luta das minhocas; o cougar mais forte pode sobrar, então se proteja nessa hora.'),
       related=RITTER, sources=[ZEISS])
c.boss(t('Big Cactus and Lark Cacti'), t('Erbe Scenic Route', 'Erbe Scenic Route'),
       t('S-Break the Lark Cacti, then guard against Pollen Explosion (Poison, Blind, Confuse) and Massive Needlecane (AT Delay, All Cancel, MOV Down). Burst cures ailments if you are hit first.',
         'Use S-Breaks nos Lark Cacti e depois proteja-se de Pollen Explosion (Poison, Blind, Confuse) e Massive Needlecane (AT Delay, All Cancel, MOV Down). O Burst cura efeitos se você for atingido primeiro.'),
       related=ERBE, sources=[GRANCEL])
c.boss(t('Evil Streams'), t('Grancel Sewers — West Block', 'Grancel Sewers — West Block'),
       t('Poison, Blind, Confuse, HP/EP/CP drain and summoned spiders. Their HP is low, so offense beats defense here.',
         'Poison, Blind, Confuse, drenagem de HP/EP/CP e aranhas invocadas. O HP é baixo, então ataque funciona melhor que defesa.'),
       related=SEWER, sources=[GRANCEL])
c.boss(t('Pale Apaches and Vogel 235'), t('Grancel — South Block gate', 'Grancel — portão do South Block'),
       t('Narrow arena and only one arts caster. S-Craft the Vogels at the start; the Apaches are fragile and weak to AT Delay and Stat Down.',
         'Arena estreita e só um conjurador de arts. Use S-Crafts nos Vogels no começo; os Apaches são frágeis e fracos a AT Delay e Stat Down.'),
       sources=[FINAL])

# ------------------------------------------------------------------ Fishing (the four new fish)
GRANAKOR = c.fish('Granakor', sources=[ROLENT])
GIGANGORA = c.fish('Gigangora', sources=[RUAN])
MARLIN = c.fish('Blue Marlin', sources=[RUAN])
DYNATRAD = c.fish('Dynatrad', sources=[BOSE])
c.spot(GRANAKOR, 'A', t('Rolent Sewers; Sapphirl Tower — 5F; Kaldia Tunnel bridge; Kaldia Limestone Cave; Grancel Sewers',
                        'Rolent Sewers; Sapphirl Tower — 5º andar; ponte do Kaldia Tunnel; Kaldia Limestone Cave; Grancel Sewers'))
c.spot(GIGANGORA, 'A', t('Manoria Byroad; Manoria Village; Gull Seaside Way — south end of the beach',
                         'Manoria Byroad; Manoria Village; Gull Seaside Way — ponta sul da praia'))
c.spot(MARLIN, 'A', t('Gull Seaside Way — north beach and south end', 'Gull Seaside Way — praia norte e ponta sul'))
c.spot(DYNATRAD, 'A', t('Valleria Shore — use the Metal Trident Rod or Lakelord II. Rewards a Zeram Powder and the Master Fisher Card.',
                        'Valleria Shore — use a Metal Trident Rod ou a Lakelord II. Dá um Zeram Powder e o Master Fisher Card.'), 'Salmon')

# ------------------------------------------------------------------ Recipes
for name, where in [
    ('Profound Paste', t("Buck's Produce Shop, Bose Market")),
    ('Boney Meat', t('Trayton Foods, Bose Market')),
    ('Sadist Monster Stew', t('Kirsche Bar, Bose')),
]:
    c.recipe(name, where, sources=[BOSE])
c.recipe("Aidios' Paradise", t('The Moonlight Path, Ravennue Village'), sources=[BOSE])
c.recipe('Aurora Beans', t('Ray at Krone Pass Checkpoint', 'Ray no Krone Pass Checkpoint'), sources=[BOSE])
c.recipe('Giblet Tempura', t('The Kingfisher Inn, Valleria Shore'), sources=[BOSE])
c.recipe('Pinkish Delight', t('The Kingfisher Inn, Valleria Shore'), sources=[BOSE])
c.recipe('Mighty Essence', t('Given by Deborah during Academy Attack', 'Dada por Deborah durante Academy Attack'), sources=[RUAN])
c.recipe('Mountain Man Stew', t('Maple Leaf Inn, Elmo Village'), sources=[ZEISS])
c.recipe('Protein Hot Pot', t('Sanktheim Gate cafeteria', 'Cafeteria do Sanktheim Gate'), sources=[ZEISS])
c.recipe('Ultra-Concentrated Herbal Tea', t('Reward for Hot Springs Salvation', 'Recompensa de Hot Springs Salvation'), sources=[ZEISS])
c.recipe('Ultima Ice Cream', t("Sorbet's Ice Cream Shop, Grancel East Block"), sources=[GRANCEL])
c.recipe('Taito School Hot Pot', t('Have Zin cook Mountain Man Stew', 'O Zin cozinha Mountain Man Stew'), 'customized', sources=[FINAL])

c.write()
