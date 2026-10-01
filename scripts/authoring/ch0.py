# Prologue extras (bosses, recipes). The prologue items themselves were written by hand in
# content/sc/chapters/ch-00.json; this script only (re)writes the extra arrays.
# Append only: ids are derived from order.
from lib import Chapter, src, t

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

c.write()
