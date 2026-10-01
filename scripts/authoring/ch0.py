# Prologue extras (bosses, recipes). The prologue items themselves were written by hand in
# content/sc/chapters/ch-00.json; this script only (re)writes the extra arrays.
# Append only: ids are derived from order.
from lib import Chapter, gf, src, t

P1 = src('Prologue - Part 1')
P2 = src('Prologue - Part 2')

c = Chapter.load(0)

c.boss(t('Kurt'), t('Balstar Channel — end of the training course', 'Balstar Channel — fim do treinamento'),
       t('Keep the party spread out: both of his main attacks hit an area, and one can block arts. Before pushing him below half HP, heal everyone and raise DEF, because he then acts several times in a row and fires his S-Break. Once you survive it, use Overdrive and finish him.',
         'Mantenha a equipe espalhada: os dois ataques principais dele atingem uma área, e um pode bloquear arts. Antes de deixá-lo abaixo da metade do HP, cure todos e aumente a DEF, porque ele passa a agir várias vezes seguidas e usa o S-Break. Depois de sobreviver, use Overdrive e finalize.'),
       sources=[P1])
c.boss(t('Jaeger (first night)', 'Jaeger (primeira noite)'), t('Le Locle — lodge', 'Le Locle — hospedaria'),
       t('Harmless until half HP, then it enters Rage Boost. Save S-Crafts to burst it through that threshold. On high difficulties, keep Anelace free to strip its buffs with Fallen Leaves and let Estelle land the hit that crosses half HP.',
         'Inofensivo até a metade do HP; depois entra em Rage Boost. Guarde os S-Crafts para passar desse limite de uma vez. Em dificuldades altas, deixe a Anelace livre para remover os buffs com Fallen Leaves e faça a Estelle dar o golpe que passa da metade.'),
       related='sc-ch0-mi-02', sources=[P1])
c.boss(t('Female Jaeger'), t('Saint-Croix Forest — event marker', 'Saint-Croix Forest — marcador de evento'),
       t('Each of her three attacks brings an ailment (Freeze, Poison, Impede). Equip the accessories from the forest chests and claim the tier-2 quartz in Rewards first, for arts like Earth Guard and Saint. Burst her before Rage Boost, or strip the buffs with Fallen Leaves.',
         'Cada um dos três ataques dela traz um efeito (Freeze, Poison, Impede). Equipe os acessórios dos baús da floresta e resgate antes os quartz de nível 2 em Rewards, para arts como Earth Guard e Saint. Derrube-a antes do Rage Boost ou remova os buffs com Fallen Leaves.'),
       sources=[P2])
c.boss(t('Jaeger (fortress)', 'Jaeger (fortaleza)'), t('Grimsel Fortress — final marker', 'Grimsel Fortress — último marcador'),
       t('It opens by raising its own defenses: dispel them with Fallen Leaves. Its small-area attack can Mute, so keep characters apart. Clock Up, Earth Guard and Petal Dance carry the fight; keep CP to strip the Rage Boost buffs.',
         'Começa aumentando as próprias defesas: remova com Fallen Leaves. O ataque em área pequena pode causar Mute, então mantenha os personagens afastados. Clock Up, Earth Guard e Petal Dance sustentam a luta; guarde CP para remover os buffs do Rage Boost.'),
       sources=[P2])

c.recipe("Nature's Font", t('Given by Phyllis at the lodge (story)', 'Dado pela Phyllis na hospedaria (história)'), sources=[P1])
c.recipe('Herb Sandwich', t("Buy at Phyllis' Kitchen in the lodge", "Compre na Phyllis' Kitchen, na hospedaria"), sources=[P1])
c.recipe('Jam Cookie', t('Treasure chest in Balstar Channel', 'Baú no Balstar Channel'), sources=[P1])

# ---------------------------------------------------------------- routes (append-only once published)
c.set_steps('sc-ch0-co-04', [
    t('East room: lower the water, then take the uncovered path north — Silver Earrings', 'Sala leste: baixe a água e siga o caminho descoberto ao norte — Silver Earrings'),
    t('End of that passage (3 chests) — Thelas Balm ×2, Curia Balm ×2, Tear Balm ×3', 'Fim dessa passagem (3 baús) — Thelas Balm ×2, Curia Balm ×2, Tear Balm ×3'),
    t('Back at the start, the center switch turns the bridge west; south end (3 chests) — Evade 1, Tear Balm ×2, EP Charge I ×2', 'De volta ao início, a alavanca central vira a ponte para oeste; extremo sul (3 baús) — Evade 1, Tear Balm ×2, EP Charge I ×2'),
    t('Second half: switch to the east, then the east path — Strike 1', 'Segunda metade: alavanca a leste, depois o caminho leste — Strike 1'),
    t('Center, buried among the boxes — Pearl Earrings', 'Centro, escondido entre as caixas — Pearl Earrings'),
    t('Drain the center, far northwest of the lower area — monster chest: EP Cut 1', 'Drene o centro; no extremo noroeste da parte baixa — baú de monstros: EP Cut 1'),
    t('Steps south of the lower area (3 chests) — EP Charge I ×3, Jam Cookie, Thelas Balm ×3', 'Degraus ao sul da parte baixa (3 baús) — EP Charge I ×3, Jam Cookie, Thelas Balm ×3'),
    t('Northeast passage, northwest path — Curia Balm ×3', 'Passagem nordeste, caminho noroeste — Curia Balm ×3'),
], source=P1)
c.set_steps('sc-ch0-co-07', [
    t('First split, northeast — Reinforced Leather', 'Primeira bifurcação, nordeste — Reinforced Leather'),
    t('Three-way split, northeast — Enhanced Boots', 'Bifurcação tripla, nordeste — Enhanced Boots'),
    t('Same split, west end — monster chest: Breeze', 'Mesma bifurcação, extremo oeste — baú de monstros: Breeze'),
    t('Second three-way split, northeast path (2 chests) — Thelas Balm ×3, Enhanced Boots', 'Segunda bifurcação tripla, caminho nordeste (2 baús) — Thelas Balm ×3, Enhanced Boots'),
    t('Middle path north — Reinforced Leather', 'Caminho do meio, ao norte — Reinforced Leather'),
    t('On the river, northwest side — EP Charge I ×3', 'No rio, lado noroeste — EP Charge I ×3'),
    t('Across the river, in the middle — Tear Balm ×3', 'Depois do rio, no meio — Tear Balm ×3'),
    t('Passage south of the Orbment Station — Flame Zippo', 'Passagem ao sul da Orbment Station — Flame Zippo'),
], source=P2)
c.set_steps('sc-ch0-co-10', [
    t('1F, the two rooms left of the start — S-Tablet ×5, Droplet of Life', '1F, as duas salas à esquerda do início — S-Tablet ×5, Droplet of Life'),
    t('1F, east room off the hallway — monster chest: Glam Choker', '1F, sala leste do corredor — baú de monstros: Glam Choker'),
    t('2F, room on the west side of the dark room — Night-Vision Goggles (equip them)', '2F, sala no lado oeste da sala escura — Night-Vision Goggles (equipe)'),
    t('2F dark room, east, then right at the split — EP 1', '2F, sala escura, leste e depois à direita na bifurcação — EP 1'),
    t('3F, the chest marked as a story marker — ID Unit', '3F, o baú marcado como evento da história — ID Unit'),
], source=P2)

c.write()
