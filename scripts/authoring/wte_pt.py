# Portuguese for Welcome to Elderfield names. The game has an official PT-BR translation, but the
# wiki only lists English names, so these are our own: a player may see a slightly different name
# in game. The app always shows the English name too and searches both, so either one finds it.
# Coined words with no clear meaning (Verdite, Blerpfish) are kept as they are.
import re

# Whole names and the building blocks the patterns below reuse.
WORDS = {
    # Basic materials
    'Stone': 'Pedra', 'Wood': 'Madeira', 'Hardwood': 'Madeira de Lei', 'Spiritwood': 'Madeira Espiritual',
    'Ancientwood': 'Madeira Ancestral', 'Vilewood': 'Madeira Vil', 'Coal': 'Carvão', 'String': 'Barbante', 'Wax': 'Cera',
    'Paper': 'Papel', 'Brick': 'Tijolo', 'Salt': 'Sal', 'Salt Rock': 'Pedra de Sal', 'Scrap Metal': 'Sucata',
    'Metal Rod': 'Barra de Metal', 'Iron Chain': 'Corrente de Ferro', 'Battery': 'Bateria', 'Leather': 'Couro',
    'Rawhide': 'Couro Cru', 'Thick Hide': 'Pele Grossa', 'Scraped Hide': 'Pele Raspada', 'Bloody Skin': 'Pele Ensanguentada',
    'Hardwood Plank': 'Tábua de Madeira de Lei', 'Raw Hay': 'Feno Cru', 'Weeds': 'Ervas Daninhas', 'Dead Leaves': 'Folhas Mortas',
    'Bat Guano': 'Guano de Morcego', 'Damp Dust': 'Pó Úmido', 'Damp Stone': 'Pedra Úmida', 'Corrupted Tar': 'Piche Corrompido',
    'Mysterious Ooze': 'Gosma Misteriosa', 'Eldritch Tears': 'Lágrimas Sobrenaturais', 'Whetstone': 'Pedra de Amolar',
    'Crafting Pattern': 'Molde de Criação', 'Godflesh': 'Carne Divina', 'Godscale': 'Escama Divina',
    'Radiant Scales': 'Escamas Radiantes', 'Soul Fragments': 'Fragmentos de Alma', 'Elder Coral': 'Coral Ancião',
    'Flesh Coral': 'Coral de Carne', 'Snow Pearls': 'Pérolas de Neve', 'Wishbone': 'Ossinho da Sorte',
    'Strange Fruit': 'Fruta Estranha', 'Soulroot': 'Raiz da Alma', 'Swiftroot': 'Raiz Veloz', 'Vileroot': 'Raiz Vil',
    'Vilebloom': 'Flor Vil', 'Voidbloom': 'Flor do Vazio', 'Slimeweed': 'Alga Gosmenta', 'Gravemoss': 'Musgo de Túmulo',
    'Deathleaf': 'Folha da Morte', 'Leadleaf': 'Folha de Chumbo', 'Eldersprout': 'Broto Ancião', 'Funneltop': 'Funil-de-flor',
    "Gorgon's Eye": 'Olho de Górgona', 'Gloom Hops': 'Lúpulo Sombrio', 'Spectral Rain': 'Chuva Espectral',
    # Body parts and creature goods
    'Bones': 'Ossos', 'bones': 'ossos', 'Hard Bones': 'Ossos Duros', 'Crushed Bones': 'Ossos Moídos', 'Cursed Bones': 'Ossos Amaldiçoados',
    'Cursed Bone Fragments': 'Fragmentos de Osso Amaldiçoados', 'Brain': 'Cérebro', 'Monkey Brains': 'Cérebro de Macaco',
    'Entrails': 'Entranhas', 'Viscera': 'Vísceras', 'Eyeball': 'Globo Ocular', 'Tooth': 'Dente', 'Tooth Dust': 'Pó de Dente',
    'Razor Tooth': 'Dente Afiado', 'Tentacle': 'Tentáculo', 'Beating Heart': 'Coração Pulsante', 'Creature Claw': 'Garra de Criatura',
    'Crimson Sinew': 'Tendão Carmesim', 'Goat Horn': 'Chifre de Cabra', 'Cursed Skull': 'Crânio Amaldiçoado',
    'Cursed Demon Skull': 'Crânio de Demônio Amaldiçoado', 'Jar of Blood': 'Pote de Sangue', 'Flask of Blood': 'Frasco de Sangue',
    'Blood of the Gods': 'Sangue dos Deuses', 'Mystery Meat': 'Carne Misteriosa', 'mystery meat': 'carne misteriosa',
    'Mystery Steak': 'Bife Misterioso', 'mystery steak': 'bife misterioso', 'Small Meat Chunk': 'Pedaço de Carne Pequeno',
    'Medium Meat Chunk': 'Pedaço de Carne Médio', 'Large Meat Chunk': 'Pedaço de Carne Grande', 'Huge Meat Chunk': 'Pedaço de Carne Enorme',
    'Stealth Musk': 'Almíscar Furtivo', 'Cursed Milk': 'Leite Amaldiçoado',
    # Ores, bars, metals
    'Copper': 'Cobre', 'Iron': 'Ferro', 'Gold': 'Ouro', 'Platinum': 'Platina', 'Steel': 'Aço', 'Crimson': 'Carmesim',
    'Blackiron': 'Ferro Negro', 'Blacksteel': 'Aço Negro', 'Verdite': 'Verdite', 'Void Crystal': 'Cristal do Vazio',
    'Dense Gold Ore': 'Minério de Ouro Denso', 'Dense Iron Ore': 'Minério de Ferro Denso', 'Bone Ingot': 'Lingote de Osso',
    'Gold Plate': 'Placa de Ouro', 'Raw Void Crystal': 'Cristal do Vazio Bruto', 'Perfect Opal': 'Opala Perfeita',
    # Crops, fruit, produce
    'Bean': 'Feijão', 'Cauliflower': 'Couve-flor', 'cauliflower': 'couve-flor', 'Celery': 'Aipo', 'Corn': 'Milho',
    'Pumpkin': 'Abóbora', 'Radish': 'Rabanete', 'Squash': 'Moranga', 'Tomato': 'Tomate', 'Wheat': 'Trigo', 'Peas': 'Ervilhas',
    'Pea': 'Ervilha', 'Strawberry': 'Morango', 'Watermelon': 'Melancia', 'Grapes': 'Uvas', 'Grape': 'Uva', 'Apple': 'Maçã',
    'Bloodberries': 'Bagas-de-sangue', 'Bloodberry': 'Baga-de-sangue', 'Cloudberry': 'Amora-ártica', 'Devilberries': 'Bagas-do-diabo',
    'Devilberry': 'Baga-do-diabo', 'Duskberries': 'Bagas-do-crepúsculo', 'Duskberry': 'Baga-do-crepúsculo',
    'Ghostberries': 'Bagas-fantasma', 'Ghostberry': 'Baga-fantasma', 'Goldberries': 'Bagas-douradas', 'Gemberries': 'Bagas-gema',
    'Voidberry': 'Baga-do-vazio', 'Spiralberry': 'Baga-espiral', 'Soulfruit': 'Fruta-da-alma', 'Fingerfruit': 'Fruta-dedo',
    'Duskmelon': 'Melão-do-crepúsculo', 'Void Plum': 'Ameixa-do-vazio', 'Dread Pepper': 'Pimenta do Pavor', 'Coffee Bean': 'Grão de Café',
    'Hay': 'Feno', 'Pumpkin Vine': 'Rama de Abóbora', 'Dreamleaf': 'Folha-dos-sonhos', 'Dreampearl': 'Pérola-dos-sonhos',
    'Eyeleaf': 'Folha-olho', 'Fungal Mound': 'Monte de Fungos', 'Headswarm': 'Enxame-de-cabeças', 'Spider Plant': 'Planta-aranha',
    'Toothbush': 'Arbusto-de-dentes', 'Wormsprout': 'Broto-minhoca',
    # Mushrooms
    'Ashy Mushroom': 'Cogumelo Cinzento', 'Bulbous Mushroom': 'Cogumelo Bulboso', 'Common Mushroom': 'Cogumelo Comum',
    'Corpse-Ear Mushroom': 'Cogumelo Orelha-de-cadáver', 'Dual-Sprout Mushroom': 'Cogumelo Broto-duplo',
    'Earthen Morel': 'Morchella Terrosa', 'Golden Mushroom': 'Cogumelo Dourado', 'Green Mushroom': 'Cogumelo Verde',
    'Night-Hood Mushroom': 'Cogumelo Capuz-noturno', 'Red Mushroom': 'Cogumelo Vermelho', 'Spiritcap Mushroom': 'Cogumelo Espiritual',
    'Whipstop Mushroom': 'Cogumelo Chicote', 'Whisptop Mushroom': 'Cogumelo Sussurrante', 'Bitter Herb': 'Erva Amarga',
    # Fish and bait
    'Aetherfin': 'Barbatana Etérea', 'Ancient Angler': 'Pescador Ancestral', 'Ancient Manta': 'Manta Ancestral',
    'Ancient Pike': 'Lúcio Ancestral', 'Blerpfish': 'Blerpfish', 'Blood Carp': 'Carpa de Sangue', 'Bonefish': 'Peixe-osso',
    'Bottom-Feeder': 'Comedor-de-fundo', 'Cave Serpent': 'Serpente das Cavernas', 'Corpsefish': 'Peixe-cadáver',
    'Dust Crab': 'Caranguejo de Poeira', 'Fog Eel': 'Enguia da Névoa', 'Ghost Flounder': 'Linguado Fantasma',
    'Glowfish': 'Peixe-brilhante', 'Gold Sturgeon': 'Esturjão Dourado', 'Goldfish': 'Peixe-dourado', 'Goldpuff': 'Baiacu-dourado',
    'Koi Fish': 'Carpa Koi', 'Lake Screamer': 'Gritador do Lago', 'Manefish': 'Peixe-juba', 'Midnight Crayfish': 'Lagostim da Meia-noite',
    'Mud Perch': 'Perca da Lama', 'Mud Serpent': 'Serpente da Lama', 'Razorfish': 'Peixe-navalha', 'Rock-Dweller': 'Morador-das-pedras',
    'Rot Puffer': 'Baiacu Podre', 'Shyfish': 'Peixe-tímido', 'Slimefish': 'Peixe-gosma', 'Stalktopus': 'Polvo-de-antenas',
    'Stonelurker': 'Espreitador-de-pedra', 'Stoneshell Turtle': 'Tartaruga Casco-de-pedra', 'Void-Floater': 'Flutuador do Vazio',
    'Bug': 'Inseto', 'Dragonfly': 'Libélula', 'Dustfly': 'Mosca-da-poeira', 'Firefly': 'Vaga-lume', 'Ladybug': 'Joaninha',
    'Leech': 'Sanguessuga', 'Lugworm': 'Minhoca-marinha', 'Maggot': 'Larva', 'Nightcrawler': 'Minhocão', 'Worm': 'Minhoca',
    'Shadewing Moth': 'Mariposa Asa-sombria', 'Jig Lure': 'Isca Jig', 'Crank Lure': 'Isca Crank', 'Premium Reel': 'Molinete Premium',
    'Golden Rod': 'Vara Dourada', 'Fish Finder': 'Localizador de Peixes', 'Bug Catching Net': 'Rede de Insetos',
    'Bait Pack (Tier 1)': 'Pacote de Iscas (Nível 1)', 'Bait Pack (Tier 2)': 'Pacote de Iscas (Nível 2)',
    # Animal products
    'Egg': 'Ovo', 'Small Egg': 'Ovo Pequeno', 'Large Egg': 'Ovo Grande', 'Ghost Egg': 'Ovo Fantasma', 'Meat Egg': 'Ovo de Carne',
    'Mystery Egg': 'Ovo Misterioso', 'Obsidian Egg': 'Ovo de Obsidiana', 'Slime Egg': 'Ovo de Gosma', 'Milk': 'Leite',
    'Small Milk': 'Leite Pequeno', 'Large Milk': 'Leite Grande', 'Small Goat Milk': 'Leite de Cabra Pequeno',
    'Large Goat Milk': 'Leite de Cabra Grande', 'Milk Bucket': 'Balde de Leite', 'Honey': 'Mel', 'Bone Honey': 'Mel de Osso',
    'Cheese': 'Queijo', 'Goat Cheese': 'Queijo de Cabra', 'Animal Feed': 'Ração Animal',
    # Food
    'Bread': 'Pão', 'Dough': 'Massa', 'Dough Ball': 'Bola de Massa', 'Cornmeal': 'Fubá', 'Cornbread': 'Pão de Milho',
    'Elder Flour': 'Farinha Anciã', 'Cooked Meat': 'Carne Cozida', 'Mayonnaise': 'Maionese', 'Secret Sauce': 'Molho Secreto',
    'secret sauce': 'molho secreto', 'Pizza': 'Pizza', 'Hotdog': 'Cachorro-quente', 'Sushi': 'Sushi', 'Takoyaki': 'Takoyaki',
    'Tempura': 'Tempurá', 'Fish Taco': 'Taco de Peixe', 'Ice Cream': 'Sorvete', 'Lemonade': 'Limonada', 'Smoothie': 'Vitamina',
    'Smootie': 'Vitamina', 'Soda Pop': 'Refrigerante', 'Bubble Gum': 'Chiclete', 'Bubble Tea': 'Chá de Bolhas',
    'Bubble-Tea': 'Chá de Bolhas', 'Cotton Candy': 'Algodão-doce', 'Chocolate Bar': 'Barra de Chocolate',
    'Chocolate Cake': 'Bolo de Chocolate', 'Hot Chocolate': 'Chocolate Quente', 'Cup of Coffee': 'Xícara de Café',
    'Cup of Tea': 'Xícara de Chá', 'Energy Drink': 'Energético', 'Protein Shake': 'Shake de Proteína', 'Grape Drink': 'Suco de Uva',
    'Strawberry Milk': 'Leite de Morango', 'Fingerfruit Juice': 'Suco de Fruta-dedo', 'Dusk Juice': 'Suco do Crepúsculo',
    'Blood Punch': 'Ponche de Sangue', 'Cloudberry Punch': 'Ponche de Amora-ártica', 'Gloom Ale': 'Cerveja Sombria',
    'Honey Mead': 'Hidromel', 'Aged Rum': 'Rum Envelhecido', 'Aged Gloom Ale': 'Cerveja Sombria Envelhecida',
    'Aged Honey Mead': 'Hidromel Envelhecido', 'Vegetable Cocktail': 'Coquetel de Legumes', 'Vegetable Smoothie': 'Vitamina de Legumes',
    'Vegetable Soup': 'Sopa de Legumes', 'Mushroom Soup': 'Sopa de Cogumelos', 'Blood Soup': 'Sopa de Sangue',
    'Serpent Soup': 'Sopa de Serpente', 'Soothing Soup': 'Sopa Calmante', 'Ghost Broth': 'Caldo Fantasma', 'Fog Broth': 'Caldo de Névoa',
    'Ghost Flounder Soup': 'Sopa de Linguado Fantasma', 'Razorfish Soup': 'Sopa de Peixe-navalha', 'Bean Stew': 'Ensopado de Feijão',
    'Harvest Stew': 'Ensopado da Colheita', 'Hearty Stew': 'Ensopado Reforçado', 'Soul Stew': 'Ensopado de Alma',
    'Super Stew': 'Superensopado', 'Stew of Six Curses': 'Ensopado das Seis Maldições', 'Hearty Omelette': 'Omelete Reforçada',
    'Honey-Glazed Bacon': 'Bacon com Mel', 'Light Salad': 'Salada Leve', 'Fruit Salad': 'Salada de Frutas',
    'Light Sandwich': 'Sanduíche Leve', 'Blood Sandwich': 'Sanduíche de Sangue', 'Flesh Sandwich': 'Sanduíche de Carne Crua',
    'Mystery Sandwich': 'Sanduíche Misterioso', 'Odd Sandwich': 'Sanduíche Esquisito', 'Special Burger': 'Hambúrguer Especial',
    'Special Donut': 'Rosquinha Especial', 'Special Hotdog': 'Cachorro-quente Especial', 'Slime Pizza': 'Pizza de Gosma',
    'Eldersprout Pizza': 'Pizza de Broto Ancião', 'Mana Muffin': 'Muffin de Mana', 'Mana Candy': 'Bala de Mana',
    'Pumpkin Muffin': 'Muffin de Abóbora', 'Pumpkin Pie': 'Torta de Abóbora', 'Strawberry Pie': 'Torta de Morango',
    'Void Plum Pie': 'Torta de Ameixa-do-vazio', 'Void Dinner': 'Jantar do Vazio', 'Duskberry Cake': 'Bolo de Baga-do-crepúsculo',
    'Duskmelon Cupcake': 'Cupcake de Melão-do-crepúsculo', 'Duskmelon Slice': 'Fatia de Melão-do-crepúsculo',
    'Baked Crab': 'Caranguejo Assado', 'Baked Fish Filet': 'Filé de Peixe Assado', 'Baked Fish Fillet': 'Filé de Peixe Assado',
    'Baked Serpent': 'Serpente Assada', 'Serpent Steak': 'Bife de Serpente', 'Ghost Sashimi': 'Sashimi Fantasma',
    'Void Sashimi': 'Sashimi do Vazio', 'Blood Skewer': 'Espetinho de Sangue', 'Simple Kebab': 'Kebab Simples',
    'Mystery Roast': 'Assado Misterioso', 'Pickled Eyeballs': 'Olhos em Conserva', 'Bitter Gel': 'Gel Amargo',
    'Failed Meal': 'Refeição Fracassada', 'Forbidden Snack': 'Lanche Proibido', 'Filling Platter': 'Travessa Farta',
    'Healthy Platter': 'Travessa Saudável', "Slayer's Feast": 'Banquete do Matador', 'Spoiled Rations': 'Rações Estragadas',
    'Perfect Cookie': 'Biscoito Perfeito', 'Rage Cookie': 'Biscoito da Fúria', 'Rich Cookie': 'Biscoito Rico',
    'Soft Cookie': 'Biscoito Macio', 'Sturdy Cookie': 'Biscoito Resistente', 'Sweet Cookie': 'Biscoito Doce',
    'Sour Lollipop': 'Pirulito Azedo', 'Sweet Lollipop': 'Pirulito Doce', 'Spicy Candy': 'Bala Apimentada',
    'Exploding Candy': 'Bala Explosiva', "Angler's Meal": 'Refeição do Pescador', "Hunter's Meal": 'Refeição do Caçador',
    "Rancher's Meal": 'Refeição do Rancheiro', "Expert Adventurer's Meal": 'Refeição do Aventureiro Experiente',
    "Expert Assassin's Meal": 'Refeição do Assassino Experiente', 'Expert BBQ Platter': 'Travessa de Churrasco Experiente',
    "Expert Cultist's Meal": 'Refeição do Cultista Experiente', 'Expert Garden Salad': 'Salada da Horta Experiente',
    "Expert Researcher's Meal": 'Refeição do Pesquisador Experiente', "Expert Wizard's Meal": 'Refeição do Mago Experiente',
    'Herbal Cake': 'Bolo de Ervas', 'Herbal Crab': 'Caranguejo com Ervas', 'Herbal Cupcake': 'Cupcake de Ervas',
    'Herbal Feast': 'Banquete de Ervas', 'Herbal Pie': 'Torta de Ervas', 'Herbal Pizza': 'Pizza de Ervas',
    'Herbal Platter': 'Travessa de Ervas', 'Herbal Roast': 'Assado com Ervas', 'Herbal Salve': 'Pomada de Ervas',
    'Herbal Serpent': 'Serpente com Ervas', 'Herbal Soup': 'Sopa de Ervas', 'Herbal Stew': 'Ensopado de Ervas',
    'Basic Herb Bundle': 'Maço de Ervas Básico', 'Potent Herb Bundle': 'Maço de Ervas Potente',
    'Simple Jerky': 'Charque Simples', 'Spiced Jerky': 'Charque Temperado', 'Simple Sausage': 'Linguiça Simples',
    'Spiced Sausage': 'Linguiça Temperada', 'Mana Sausage': 'Linguiça de Mana', 'Cured Mana Steak': 'Bife Curado de Mana',
    'Cured Simple Steak': 'Bife Curado Simples', 'Cured Spiced Steak': 'Bife Curado Temperado',
    # Potions and battle items
    "Angler's Potion": 'Poção do Pescador', "Farmer's Potion": 'Poção do Fazendeiro', "Forager's Potion": 'Poção do Coletor',
    "Miner's Potion": 'Poção do Minerador', "Rancher's Potion": 'Poção do Rancheiro', 'Night-Owl Potion': 'Poção da Coruja',
    'Experience Potion': 'Poção de Experiência', 'Love Potion': 'Poção do Amor', 'Rest Potion': 'Poção de Descanso',
    'Recall Potion': 'Poção de Retorno', 'Blood Potion': 'Poção de Sangue', 'Chaos Potion': 'Poção do Caos',
    'Hazard Potion': 'Poção do Perigo', 'Taunting Potion': 'Poção de Provocação', 'Soulbargain Potion': 'Poção do Pacto de Alma',
    'Potion of Commerce': 'Poção do Comércio', 'Potion of Debt': 'Poção da Dívida', 'Potion of Everything': 'Poção de Tudo',
    'Potion of Refuse': 'Poção do Lixo', 'Slime Tonic': 'Tônico de Gosma', 'Combat Drink': 'Bebida de Combate',
    'Forbidden Elixir': 'Elixir Proibido', 'Cleansing Balm': 'Bálsamo Purificador', 'Poison Vial': 'Frasco de Veneno',
    'Molotov Cocktail': 'Coquetel Molotov', 'Pocket Sand': 'Areia de Bolso', 'Spellbomb of Chaos': 'Bomba Mágica do Caos',
    'Spellbomb of Hex': 'Bomba Mágica da Maldição', 'Lesser Holy Water': 'Água Benta Menor', 'Greater Holy Water': 'Água Benta Maior',
    'Crystal Flask': 'Frasco de Cristal', 'Ashball': 'Bola de Cinzas',
    # Tools, stations, placeables
    'Axe': 'Machado', 'Pickaxe': 'Picareta', 'Scythe': 'Foice', 'Gardening Hoe': 'Enxada', 'Watering Can': 'Regador',
    'Fishing Rod': 'Vara de Pescar', 'Shovel': 'Pá', 'Rusty Scissors': 'Tesoura Enferrujada', 'Lifter': 'Levantador',
    'Magnifying Glass': 'Lupa', 'Torch': 'Tocha', 'Candles': 'Velas', 'Tent': 'Barraca', 'Extra Pouch': 'Bolsa Extra',
    'Equipment Pack': 'Pacote de Equipamento', 'Gem Bag': 'Bolsa de Gemas', 'Rare Gem Bag': 'Bolsa de Gemas Rara',
    'Blood-Soaked Gem Bag': 'Bolsa de Gemas Ensanguentada', 'Tiny Coin Pouch': 'Bolsinha de Moedas Minúscula',
    'Small Coin Pouch': 'Bolsinha de Moedas Pequena', 'Medium Coin Pouch': 'Bolsinha de Moedas Média', 'Large Coin Box': 'Caixa de Moedas Grande',
    'Treasure Casket': 'Baú do Tesouro', 'Goodie Bag': 'Sacola de Guloseimas', 'Small Mine Key': 'Chave Pequena da Mina',
    'Basic Skeleton Key': 'Chave Mestra Básica', 'Workbench': 'Bancada', "Craftsman's Bench": 'Bancada do Artesão',
    "Tinker's Desk": 'Mesa do Inventor', "Jeweler's Desk": 'Mesa do Joalheiro', 'Jeweller’s Desk': 'Mesa do Joalheiro',
    'Lapidary Table': 'Mesa de Lapidação', 'Prep Table': 'Mesa de Preparo', 'Grinder': 'Moedor', 'Witching Mortar': 'Pilão de Bruxaria',
    'Drying Rack': 'Varal de Secagem', 'Preserving Barrel': 'Barril de Conserva', 'Keg': 'Barril de Fermentação', 'Cask': 'Tonel',
    'Blast Kiln': 'Forno de Fundição', 'Furnace': 'Fornalha', 'Slicer': 'Fatiador', 'Food Processor': 'Processador de Alimentos',
    'Compost Bin': 'Composteira', 'Coffee Maker': 'Cafeteira', 'Feedmaker': 'Fabricante de Ração', 'Bee House': 'Colmeia',
    'Bat Box': 'Casa de Morcegos', 'Crab Pot': 'Armadilha de Caranguejo', 'Lightning Rod': 'Para-raios', 'Generator': 'Gerador',
    'Farm Computer': 'Computador da Fazenda', 'Toxic Waste Machine': 'Máquina de Lixo Tóxico', 'Ritual Brazier': 'Braseiro Ritual',
    'Pet House': 'Casinha de Bicho', 'Primary Storage Chest': 'Baú Principal', 'Small Wood Chest': 'Baú de Madeira Pequeno',
    'Forge Upgrade (t2)': 'Melhoria da Forja (n2)', 'Forge Upgrade (t3)': 'Melhoria da Forja (n3)', 'Floor Remover': 'Removedor de Piso',
    'Wallpaper Remover': 'Removedor de Papel de Parede', 'Bucket of Paint': 'Balde de Tinta', 'Garden Shelter': 'Abrigo de Jardim',
    'Medium Wooden Shelter': 'Abrigo de Madeira Médio', 'Large Wooden Shelter': 'Abrigo de Madeira Grande', 'Large Machine': 'Máquina Grande',
    'Ancient Shrine': 'Santuário Ancestral', 'Swingset': 'Balanço', 'Giant Broken Barrel': 'Barril Gigante Quebrado',
    'Giant Fountain': 'Fonte Gigante', 'Giant Rock': 'Rocha Gigante', 'Giant Skull Chalice': 'Cálice de Crânio Gigante',
    'Gnarled Lamp': 'Lâmpada Retorcida', 'Blue Bed': 'Cama Azul', 'Blue Tile Bathtub': 'Banheira de Azulejo Azul',
    'Brown Journal Desk': 'Escrivaninha Marrom', 'Brown Wardrobe': 'Guarda-roupa Marrom', 'Green Cooking Pot': 'Panela Verde',
    'Grey Fridge': 'Geladeira Cinza', 'Old Brown T.V.': 'TV Marrom Velha', 'Cemetery Fence': 'Cerca de Cemitério',
    'Rope Fence': 'Cerca de Corda', 'Wire Fence': 'Cerca de Arame', 'Wood Fence': 'Cerca de Madeira',
    'Cobblestone Path': 'Caminho de Paralelepípedo', 'Concrete Path': 'Caminho de Concreto', 'Gravel Path': 'Caminho de Cascalho',
    'Stone Path': 'Caminho de Pedra', 'Tile Path': 'Caminho de Azulejo', 'Wood Path': 'Caminho de Madeira',
    'Jack o\' Lantern': 'Lanterna de Abóbora', 'Contract: Stone Well': 'Contrato: Poço de Pedra',
    'Contract: Water Wheel': 'Contrato: Roda d\'Água', 'Contract: Wind Turbine': 'Contrato: Turbina Eólica',
    'Contract: Windmill': 'Contrato: Moinho de Vento',
    # Scarecrows, effigies, offerings, fertilizer
    'Scarecrow': 'Espantalho', 'Basic Scarecrow': 'Espantalho Básico', 'Ragged Scarecrow': 'Espantalho Esfarrapado',
    "Jack o' Scarecrow": 'Espantalho de Abóbora', 'Cornstalker Scarecrow': 'Espantalho Espreita-milho', 'Dripping Scarecrow': 'Espantalho Gotejante',
    'Floral Scarecrow': 'Espantalho Florido', 'Ghostly Scarecrow': 'Espantalho Fantasmagórico', 'Skeletal Scarecrow': 'Espantalho Esquelético',
    'Tortured Scarecrow': 'Espantalho Torturado', 'Wicker Scarecrow': 'Espantalho de Vime', 'Offering of The Void': 'Oferenda do Vazio',
    'Combat Offering': 'Oferenda de Combate', 'Lesser Rune of Growth': 'Runa do Crescimento Menor', 'Rune of the Dead God': 'Runa do Deus Morto',
    'Enchanted Pitchfork': 'Forcado Encantado', 'Kaal Idol': 'Ídolo de Kaal', 'Vile Relic': 'Relíquia Vil', 'Staring Orb': 'Orbe que Encara',
    'Void Sphere': 'Esfera do Vazio', 'Sign of Death': 'Sinal da Morte', 'Unmarked Seed': 'Semente sem Marca',
    'Creature Cluster Seed': 'Semente de Aglomerado de Criaturas', 'Sunflower Seeds': 'Sementes de Girassol',
    # Dice, books, tomes
    'Lucky Die': 'Dado da Sorte', 'Cursed Die': 'Dado Amaldiçoado', 'Crimson Die': 'Dado Carmesim', 'Experience Tome': 'Tomo de Experiência',
    'Book of Bone': 'Livro de Osso', 'The Book of Cookies': 'O Livro dos Biscoitos', 'Tome of Culinary Lore': 'Tomo da Arte Culinária',
    'Tome of Fine Relics': 'Tomo das Relíquias Finas', 'Tome of Lost Tinctures': 'Tomo das Tinturas Perdidas',
    'Tome of Vile Patterns': 'Tomo dos Moldes Vis', 'Tome of Warped Fusion': 'Tomo da Fusão Distorcida', 'Forbidden Lorebook': 'Livro do Saber Proibido',
    'Star Map of Valtris': 'Mapa Estelar de Valtris',
    # Equipment
    'Bark Armor': 'Armadura de Casca', 'Bloated Chestplate': 'Peitoral Inchado', 'Nomad Cloak': 'Manto do Nômade', 'Nomad Hood': 'Capuz do Nômade',
    'Plague Doctor Boots': 'Botas do Médico da Peste', 'Plague Doctor Legguards': 'Perneiras do Médico da Peste',
    'Plague Doctor Mask': 'Máscara do Médico da Peste', 'Plague Doctor Robe': 'Manto do Médico da Peste', 'Straw Hat': 'Chapéu de Palha',
    'Moonlight Shoes': 'Sapatos ao Luar', 'Wooden Stick': 'Graveto', 'Wooden Staff': 'Cajado de Madeira', 'Metal Bat': 'Taco de Metal',
    'Brutal Knife': 'Faca Brutal', 'Holy Bludgeon': 'Porrete Sagrado', 'Ritual Blade': 'Lâmina Ritual', 'Blade of Darkness': 'Lâmina das Trevas',
    'Staff of Darkness': 'Cajado das Trevas', 'Staff of Insight': 'Cajado da Percepção', 'Trident of the Deep': 'Tridente das Profundezas',
    'Whip of Delvek': 'Chicote de Delvek', 'Blade Pendant': 'Pingente da Lâmina', 'Blood Pendant': 'Pingente de Sangue',
    'Lightning Pendant': 'Pingente do Relâmpago', 'Occult Pendant': 'Pingente Oculto', 'Soul Pendant': 'Pingente da Alma',
    'Finger Necklace': 'Colar de Dedos', 'Star Necklace': 'Colar Estrelado', "Cat's Eye Necklace": 'Colar Olho-de-gato',
    'Necklace of Fortune': 'Colar da Fortuna', 'Necklace of Power': 'Colar do Poder', 'Necklace of Wit': 'Colar da Astúcia',
    'Earring of the Dark Sea': 'Brinco do Mar Sombrio', 'Opal Ring': 'Anel de Opala', 'Ring of Binding': 'Anel da Amarração',
    'Chestplate': 'Peitoral', 'Helmet': 'Elmo', 'Greaves': 'Grevas', 'Legguards': 'Perneiras', 'Shortsword': 'Espada Curta',
    'Greatsword': 'Espadão', 'Quickblade': 'Lâmina Ligeira', 'Staff': 'Cajado',
    # Crystals
    'Death Crystal': 'Cristal da Morte', 'Deep Crystal': 'Cristal das Profundezas', 'Dream Crystal': 'Cristal dos Sonhos',
    'Ghost Crystal': 'Cristal Fantasma', 'Light Crystal': 'Cristal de Luz', 'Moon Crystal': 'Cristal da Lua', 'Green Crystal': 'Cristal Verde',
}

# Gem names: "<Tier> <Kind> Gem" and plain "<Kind> Gem".
GEM_KINDS = {
    'Armor': 'de Armadura', 'Blood': 'de Sangue', 'Focus': 'do Foco', 'Magic': 'Mágica', 'Mind': 'da Mente', 'Rage': 'da Fúria',
    'Sharp': 'Afiada', 'Swift': 'Veloz', 'Greed': 'da Ganância', 'Soul': 'da Alma', 'Artery': 'da Artéria', 'Blasphemous': 'Blasfema',
    'Clear': 'Clara', 'Clot': 'do Coágulo', 'Coral': 'de Coral', 'Curse': 'da Maldição', 'Damp': 'Úmida', 'Darkness': 'das Trevas',
    'Dominating': 'Dominadora', 'Faithful': 'Fiel', 'Flesh': 'de Carne', 'Fog': 'da Névoa', 'Fortress': 'Fortaleza', 'Insanity': 'da Insanidade',
    'Insensate': 'Insensível', 'Insight': 'da Percepção', 'Light': 'da Luz', 'Meat': 'de Carne', 'Payback': 'da Revanche',
    'Rain': 'da Chuva', 'Reflection': 'do Reflexo', 'Riptide': 'da Correnteza', 'Sinew': 'do Tendão', 'Tidal': 'da Maré',
    'Treasure': 'do Tesouro', 'Viscera': 'de Vísceras',
}
GEM_TIERS = {'Chipped': 'Lascada', 'Lesser': 'Menor', 'Greater': 'Maior', 'Perfect': 'Perfeita'}
QUALITY = {'Basic': 'Básic{o}', 'Rusty': 'Enferrujad{o}', 'Sturdy': 'Resistente', 'Quality': 'de Qualidade', 'Superior': 'Superior',
           'Old': 'Velh{o}'}
FEMININE = {'Picareta', 'Foice', 'Enxada', 'Vara de Pescar', 'Espada Curta', 'Lâmina Ligeira'}
BLESSINGS = {'Brutalism': 'Brutalidade', 'Daring': 'Ousadia', 'Greed': 'Ganância', 'Panic': 'Pânico', 'Skepticism': 'Ceticismo',
             'Stubbornness': 'Teimosia', 'Zealotry': 'Fanatismo', 'Chaos': 'Caos', 'Doom': 'Ruína', 'Dread': 'Pavor', 'Fear': 'Medo',
             'Hex': 'Maldição', 'Sickness': 'Doença', 'Weakness': 'Fraqueza'}
STATS = {'Agility': 'Agilidade', 'Attack': 'Ataque', 'Defense': 'Defesa', 'HP': 'PV', 'MP': 'PM', 'Luck': 'Sorte',
         'M. Atk': 'Atq. Mágico', 'M. Def': 'Def. Mágica'}
SIZES = {'Lesser': 'Menor', 'Medium': 'Média', 'Greater': 'Maior'}
SKILLS = {
    'All or Nothing': 'Tudo ou Nada', 'Blade of Blood': 'Lâmina de Sangue', 'Energizing Strike': 'Golpe Energizante',
    'Frenzy Slash': 'Corte Frenético', 'Harvest Slash': 'Corte da Colheita', 'Heavy Blow': 'Golpe Pesado',
    'Heretical Blow': 'Golpe Herege', 'Light Pierce': 'Perfuração de Luz', 'Blood Mana': 'Mana de Sangue',
    'Chaos Thorns': 'Espinhos do Caos', 'Cosmic Premonition': 'Premonição Cósmica', 'Crystal Blast': 'Explosão de Cristal',
    'Dark Shield': 'Escudo Sombrio', 'Energizing Blast': 'Explosão Energizante', 'Frenzy Blast': 'Explosão Frenética',
    'Greater Mending': 'Cura Maior', 'Induce Anxiety': 'Induzir Ansiedade', 'Lesser Mending': 'Cura Menor',
    'Light Blast': 'Explosão de Luz', 'Mana Drain': 'Drenar Mana', 'Mark of Death': 'Marca da Morte',
    'Mark of Insight': 'Marca da Percepção', 'Mind Blast': 'Explosão Mental', 'Pumpkin Blast': 'Explosão de Abóbora',
    'Sludge Blast': 'Explosão de Lodo', 'Terror Blast': 'Explosão de Terror', 'Torrent of Darkness': 'Torrente de Trevas',
}


def _gender(noun, template):
    return template.format(o='a' if noun in FEMININE else 'o')


def tr(name):
    """Portuguese for an English name, or None when there is no confident translation."""
    if name in WORDS:
        return WORDS[name]
    rules = [
        (r'^(.+) Tree Seed$', lambda m: f'Semente de Árvore de {tr(m[1])}' if tr(m[1]) else None),
        (r'^(.+) Seeds?$', lambda m: f'Semente de {tr(m[1])}' if tr(m[1]) else None),
        (r'^Blueprint: (.+)$', lambda m: f'Projeto: {tr(m[1]) or m[1]}'),
        (r'^Recipe: (.+)$', lambda m: f'Receita: {tr(m[1]) or m[1]}'),
        (r'^Skill Tome: (.+)$', lambda m: f'Tomo de Habilidade: {SKILLS.get(m[1], m[1])}'),
        (r'^Ritual Tome: (.+)$', lambda m: f'Tomo de Ritual: {SKILLS.get(m[1], m[1])}'),
        (r'^Aged Wine \((.+)\)$', lambda m: f'Vinho Envelhecido ({tr(m[1]) or m[1]})'),
        (r'^Aged Wine$', lambda m: 'Vinho Envelhecido'),
        (r'^Wine \((.+)\)$', lambda m: f'Vinho ({tr(m[1]) or m[1]})'),
        (r'^Jelly \((.+)\)$', lambda m: f'Geleia ({tr(m[1]) or m[1]})'),
        (r'^Pickles \((.+)\)$', lambda m: f'Conserva ({tr(m[1]) or m[1]})'),
        (r'^Aged (Goat )?Cheese \((Artisan|Basic|Perfect|Quality)\)$', lambda m: 'Queijo {}Envelhecido ({})'.format(
            'de Cabra ' if m[1] else '', {'Artisan': 'Artesanal', 'Basic': 'Básico', 'Perfect': 'Perfeito', 'Quality': 'de Qualidade'}[m[2]])),
        (r'^(.+) \(Raw\)$', lambda m: f'{tr(m[1])} (Cru)' if tr(m[1]) else None),
        (r'^(.+) \(Wet\)$', lambda m: f'{tr(m[1])} (Úmido)' if tr(m[1]) else None),
        (r'^(Chipped|Lesser|Greater|Perfect) (\w+) Gem$', lambda m: f'Gema {GEM_KINDS[m[2]]} {GEM_TIERS[m[1]]}' if m[2] in GEM_KINDS else None),
        (r'^(\w+) Gem$', lambda m: f'Gema {GEM_KINDS[m[1]]}' if m[1] in GEM_KINDS else None),
        (r'^Damp Gem Cluster$', lambda m: 'Aglomerado de Gemas Úmidas'),
        (r'^Greater (\w+ Crystal)$', lambda m: f'{tr(m[1])} Maior' if tr(m[1]) else None),
        (r'^(\w+) Ore$', lambda m: f'Minério de {tr(m[1])}' if tr(m[1]) else None),
        (r'^(.+) Bar$', lambda m: f'Barra de {tr(m[1])}' if tr(m[1]) else None),
        (r'^(Copper|Iron|Platinum|Verdite|Stone) (Chestplate|Helmet|Greaves|Legguards|Shortsword|Greatsword|Quickblade|Staff)$',
         lambda m: f'{WORDS[m[2]]} de {tr(m[1])}'),
        (r'^(Basic|Rusty|Sturdy|Quality|Superior|Old) (Axe|Pickaxe|Scythe|Gardening Hoe|Watering Can|Fishing Rod)$',
         lambda m: f'{WORDS[m[2]]} {_gender(WORDS[m[2]], QUALITY[m[1]])}'),
        (r'^(Blessing|Fickle|Greater) Potion of (\w+)$', lambda m: '{} {}'.format(
            {'Blessing': 'Poção de Bênção:', 'Fickle': 'Poção Volúvel de', 'Greater': 'Poção Maior de'}[m[1]], BLESSINGS.get(m[2], m[2]))),
        (r'^Blessing Potion of \((.+)\)$', lambda m: 'Poção de Bênção (' + ', '.join(BLESSINGS.get(w.strip(), w.strip()) for w in m[1].split(',')) + ')'),
        (r'^Restore Potion of (\w+)$', lambda m: f'Poção Restauradora de {BLESSINGS.get(m[1], m[1])}'),
        (r'^Flask of the Gods \((.+)\)$', lambda m: 'Frasco dos Deuses (' + ', '.join(STATS.get(w.strip(), w.strip()) for w in m[1].split(',')) + ')'),
        (r'^(Lesser|Medium|Greater) (Fertility|Harvest) Effigy$', lambda m: 'Efígie {} {}'.format(
            {'Fertility': 'da Fertilidade', 'Harvest': 'da Colheita'}[m[2]], SIZES[m[1]])),
        (r'^(Lesser|Medium|Greater) Offering of Rain$', lambda m: f'Oferenda da Chuva {SIZES[m[1]]}'),
        (r'^(Dense|Fancy) Fertilizer \(Lv(\d)\)$', lambda m: '{} (Nv{})'.format(
            {'Dense': 'Fertilizante Denso', 'Fancy': 'Fertilizante Refinado'}[m[1]], m[2])),
        (r'^(Cured \w+ Steak|\w+ Jerky|\w+ Sausage) \(Raw\)$', lambda m: f'{tr(m[1])} (Cru)' if tr(m[1]) else None),
    ]
    for pattern, build in rules:
        match = re.match(pattern, name)
        result = build(match) if match else None
        if result:
            return result
    return None


def t2(name):
    """A localized name: Portuguese when known, English always."""
    pt = tr(name)
    return {'en': name, 'pt': pt} if pt and pt != name else {'en': name}

CREATURES = {
    'Ancient Hand': 'Mão Ancestral', 'Ancient Mushroom': 'Cogumelo Ancestral', 'Ancient Tree': 'Árvore Ancestral', 'Arm': 'Braço',
    'Arms': 'Braços', 'Bag Boy': 'Empacotador', 'Bag of Tricks': 'Saco de Truques', 'Beckoning Branch': 'Galho que Chama',
    'Best Friend': 'Melhor Amigo', 'Bighead': 'Cabeção', 'Bird': 'Pássaro', 'Bonefly': 'Mosca-de-osso', 'Bookmaster': 'Mestre dos Livros',
    'Candycorn': 'Milho-doce', 'Caveman': 'Homem das Cavernas', 'Chest Mimic': 'Baú Mímico', 'Coin Totem': 'Totem de Moedas',
    'Colossal Rat': 'Rato Colossal', 'Congregation': 'Congregação', 'Cornstalker': 'Espreita-milho', 'Corpsefly': 'Mosca-cadáver',
    'Denizen of the Deep-Fryer': 'Morador da Fritadeira', 'Door Mimic': 'Porta Mímica', 'Dripper': 'Gotejador',
    'Eldritch Angler': 'Pescador Sobrenatural', 'Emissary of Daeus': 'Emissário de Daeus', 'Emissary of Delvek': 'Emissário de Delvek',
    'Emissary of Kaal': 'Emissário de Kaal', 'Emissary of Xxarteck': 'Emissário de Xxarteck', 'Eye': 'Olho',
    'Failed Skeleton': 'Esqueleto Fracassado', 'Failed Twins': 'Gêmeos Fracassados', 'Farmer': 'Fazendeiro', 'Fingermen': 'Homens-dedo',
    'Fish-Man': 'Homem-peixe', 'Flesh Girl': 'Garota de Carne', 'Flesh Pile of Nezroth': 'Pilha de Carne de Nezroth',
    'Flower Bird': 'Pássaro-flor', 'Forest Dancers': 'Dançarinos da Floresta', 'Frog Baby': 'Bebê-sapo', 'Fungal Swarm': 'Enxame Fúngico',
    'Garbage Mimic': 'Lixeira Mímica', 'Gem Golem': 'Golem de Gemas', 'Giant Fish': 'Peixe Gigante', 'Giant Man-Fish': 'Homem-peixe Gigante',
    'Globule': 'Glóbulo', 'Glow Bear': 'Urso Brilhante', 'Grandma': 'Vovó', 'Gravemoss': 'Musgo de Túmulo',
    'Gravemoss Colony': 'Colônia de Musgo de Túmulo', 'Gravewarden': 'Guardião do Túmulo', 'Growth': 'Crescimento',
    'Hall Monitor': 'Monitor do Corredor', 'Head Crop': 'Plantação de Cabeças', 'Horde of Shoppers': 'Horda de Consumidores',
    'Hungry Plant': 'Planta Faminta', 'Hungry Sister': 'Irmã Faminta', 'Imperfect Creation': 'Criação Imperfeita',
    'Imposter Egg': 'Ovo Impostor', 'Laundry Man': 'Homem da Lavanderia', 'Leg': 'Perna', 'Living Rock': 'Rocha Viva',
    'Living Stump': 'Toco Vivo', 'Lollipop': 'Pirulito', 'Lost Schoolboy': 'Estudante Perdido', 'Lost Schoolgirl': 'Estudante Perdida',
    'Mall Administrator': 'Administrador do Shopping', 'Mask of Delvek': 'Máscara de Delvek', 'Mimic': 'Mímico', 'Minotaur': 'Minotauro',
    'Mr. Wiggles': 'Sr. Remexe', 'Mr. Wiggles v2': 'Sr. Remexe v2', 'Ms. Moody': 'Sra. Mal-humorada', 'Mutated Snowman': 'Boneco de Neve Mutante',
    'Office Slime': 'Gosma de Escritório', 'Pale Wiggler': 'Remexedor Pálido', 'Pipe Cleaner': 'Limpa-canos', 'Pretty Flower': 'Flor Bonita',
    'Rat': 'Rato', 'Scarecrow': 'Espantalho', 'Shopper': 'Consumidor', 'Silly Dog': 'Cachorro Bobo', 'Skeleball': 'Bola-esqueleto',
    'Skeletal Priest': 'Sacerdote Esquelético', 'Skeleton Mage': 'Mago Esqueleto', 'Skin Thief': 'Ladrão de Pele',
    'Skullcrawler': 'Rastejador de Crânios', 'Sleep, Demigod': 'Sono, Semideus', 'Sophia': 'Sophia', 'Soul Swarm': 'Enxame de Almas',
    'Soul Vessel': 'Receptáculo de Almas', 'Soul of the Catacombs': 'Alma das Catacumbas', 'Special Cat': 'Gato Especial',
    'Stoneface': 'Cara-de-pedra', 'Strange Light': 'Luz Estranha', 'Strange Plant': 'Planta Estranha', 'Tall Man': 'Homem Alto',
    'Teacher': 'Professora', "Teacher's Pet": 'Queridinho da Professora', 'Tentacle': 'Tentáculo', 'The Great Pumpkin': 'A Grande Abóbora',
    'The Necromancer': 'O Necromante', 'The Neighborhood Watcher': 'O Vigia do Bairro', 'Tickler': 'Fazedor de Cócegas',
    'Tomb Cleaner': 'Limpador de Tumbas', 'Toothache': 'Dor de Dente', 'Treasure Goblin': 'Goblin do Tesouro', 'Void Entity': 'Entidade do Vazio',
    'Wet Mouth': 'Boca Molhada', 'Wild Deer': 'Cervo Selvagem', 'Xxarteck Cultist': 'Cultista de Xxarteck', 'Xxarteck Monolith': 'Monólito de Xxarteck',
}

# Place words, replaced longest first inside place descriptions ("Mine F2 (The Old Woods Mines)").
PLACES = {
    'Town Outskirts': 'Arredores da Cidade', 'Town and Farm': 'Cidade e Fazenda', 'Farm Path': 'Caminho da Fazenda',
    'Farmhouse': 'Casa da Fazenda', 'Farm': 'Fazenda', 'Workshop': 'Oficina', 'Ranch': 'Rancho', 'Lakefront': 'Beira do Lago',
    'Town': 'Cidade', 'TownSouth': 'Cidade (Sul)', 'The Old Woods Mines': 'Minas do Bosque Antigo', 'The Old Woods': 'Bosque Antigo',
    'Old Woods': 'Bosque Antigo', 'The Deep Woods': 'Floresta Profunda', 'Deep Woods Village': 'Vila da Floresta Profunda',
    'Deep Woods': 'Floresta Profunda', 'DeepWoods': 'Floresta Profunda', 'Deep Catacombs': 'Catacumbas Profundas',
    'Catacombs Mines': 'Minas das Catacumbas', 'Catacombs': 'Catacumbas', 'Sealed Passage': 'Passagem Selada',
    'Sealed Chamber': 'Câmara Selada', 'Bone Chamber': 'Câmara dos Ossos', 'Hidden Manor': 'Mansão Oculta', 'Deep Mall': 'Shopping Profundo',
    'Mall BF': 'Subsolo do Shopping', 'Mall Mines': 'Minas do Shopping', 'Mall Parking Lot': 'Estacionamento do Shopping',
    'Mall Bus Stop': 'Ponto de Ônibus do Shopping', 'Mall Outside': 'Entrada do Shopping', 'Mall': 'Shopping',
    'Beginner Mines': 'Minas Iniciais', 'Mines': 'Minas', 'Mine': 'Mina', 'Sewers': 'Esgotos',
    'Shrine of Xxarteck': 'Santuário de Xxarteck', 'Shrine': 'Santuário', 'Greystone Estates': 'Residencial Greystone',
    'Elderfield High': 'Colégio Elderfield', 'Elderfield Saloon': 'Saloon de Elderfield', 'Library': 'Biblioteca',
    'Laundry Room': 'Lavanderia', 'Kitchen': 'Cozinha', 'Basement': 'Porão', 'Rooftop': 'Terraço', 'Apartment': 'Apartamento',
    'Home': 'Casa', 'Campsite': 'Acampamento', 'Abandoned Hovel': 'Casebre Abandonado', 'Abandoned Mill': 'Moinho Abandonado',
    'Abandoned Building': 'Prédio Abandonado', 'Mill': 'Moinho', "Grandma's Cabin": 'Cabana da Vovó', 'Cabin': 'Cabana',
    'The Pale Clearing': 'A Clareira Pálida', 'The Red Clearing': 'A Clareira Vermelha', 'Clearing': 'Clareira',
    'Corn Maze': 'Labirinto de Milho', 'Pumpkin Path': 'Trilha das Abóboras', 'Classroom': 'Sala de Aula', 'Front Office': 'Recepção',
    'Empty Shop': 'Loja Vazia', 'Bathroom': 'Banheiro', 'Hallway': 'Corredor', 'Office': 'Escritório', 'Closet': 'Armário',
    'Store': 'Loja', 'Fancy House': 'Casa Chique', 'Art Gallery': 'Galeria de Arte', 'Reward Room': 'Sala de Recompensas',
    "Klaus's House": 'Casa do Klaus', 'House': 'Casa', 'Room': 'Sala', 'ROOMS': 'Salas', 'Floor': 'Andar', 'Dwelling': 'Moradia',
    'Mimic Chest': 'Baú Mímico', 'Chest': 'Baú', 'Enhanced Loot': 'loot aprimorado', 'Loot': 'Loot',
    'North': 'Norte', 'South': 'Sul', 'East': 'Leste', 'West': 'Oeste', 'North East': 'Nordeste', 'North-East': 'Nordeste',
    'Encounter': 'Encontro', 'Boss Battle': 'Batalha de chefe', 'Exchange and reward': 'Troca e recompensa', 'Special encounters': 'Encontros especiais',
    # Shops and people's stalls
    "Travelling Merchant's shop": 'loja do Mercador Viajante', 'Travelling Merchant': 'Mercador Viajante', 'Farming Shop': 'Loja da Fazenda',
    'Garbage Shop': 'Loja do Lixo', 'Recipe Shop': 'Loja de Receitas', 'The Meat Man': 'O Homem da Carne', 'Seed Shop': 'Loja de Sementes',
    'Ranch Shop': 'Loja do Rancho', 'General Store': 'Armazém', 'Forge Shop': 'Loja da Forja', "Woodsman's Shop": 'Loja do Lenhador',
    'Vending Machine': 'Máquina de Vendas', 'Nursery': 'Viveiro', 'Mining Shop': 'Loja de Mineração', "Big Cat's Shop": 'Loja do Gatão',
    'Cursed Seed Shop': 'Loja de Sementes Amaldiçoadas', 'Snack Shop': 'Lanchonete', 'The Soggy Slice': 'The Soggy Slice',
    'Food Cart': 'Carrinho de Comida', 'Grocery Store': 'Mercearia', 'Building Shop': 'Loja de Construção', 'Furniture Shop': 'Loja de Móveis',
    'Lemonade Stand': 'Barraca de Limonada', 'Bait Shop': 'Loja de Iscas', 'Pet Shop': 'Pet Shop', 'Music Store': 'Loja de Música',
    'Potion Lab': 'Laboratório de Poções', 'Cooking Pot': 'Panela', 'Juicer': 'Espremedor', 'Oven': 'Forno', 'Forge': 'Forja',
    # Characters named in sources
    'Farmer Hans': 'Fazendeiro Hans', 'Old Man Crawford': 'Velho Crawford', 'Chef Elroy': 'Chef Elroy', 'Fisherman Herb': 'Pescador Herb',
    'Mall Rat': 'Rato do Shopping', 'Mall Admin': 'Administração do Shopping', 'Boss encounter': 'Encontro com chefe', 'Harvest Chamber': 'Câmara da Colheita', 'Grotto': 'Gruta', 'Stairs': 'Escada',
    'Statue': 'Estátua', 'Seed Stand': 'Barraca de Sementes', 'Villager': 'Morador',
}


def place_pt(text):
    """A place description with its place words in Portuguese; floors read "2º andar"."""
    out = text
    for en, pt in sorted(PLACES.items(), key=lambda kv: -len(kv[0])):
        out = re.sub(r'(?<![\w\'])' + re.escape(en) + r'(?![\w\'])', '\0' + str(list(PLACES).index(en)) + '\0', out)
    out = re.sub('\0(\\d+)\0', lambda m: PLACES[list(PLACES)[int(m[1])]], out)
    out = re.sub(r'\b(\d)F\b|\bF(\d)\b|\b(\d)f\b', lambda m: f'{m[1] or m[2] or m[3]}º andar', out)
    return out.replace(' and ', ' e ')

SEASON_PT = {'Rebirth': 'primavera', 'Harvest': 'verão', 'Witch': 'outono', 'Death': 'inverno'}


def _season(word):
    return SEASON_PT.get(word, word)

# Whole phrases of "how to get it", English → Portuguese. Item and place names inside them are
# translated afterwards by `terms_pt`.
PHRASES = [
    (r'Possible result from Gem Bags, gem nodes, digging treasure, God Shrine rewards, or other tiered gem rewards',
     'Pode vir de Bolsas de Gemas, veios de gemas, tesouros enterrados, recompensas de Santuários dos Deuses e outras recompensas de gemas'),
    (r'Possible reward from the Deep Woods God Shrine gem outcome', 'Pode vir do Santuário dos Deuses da Floresta Profunda (resultado de gemas)'),
    (r'Possible (small|large)-crystal reward, including Eldritch Angler and Mutated Snowman loot',
     lambda m: 'Pode vir de recompensas de cristal {} (inclusive do Pescador Sobrenatural e do Boneco de Neve Mutante)'.format(
         'pequeno' if m[1] == 'small' else 'grande')),
    (r'Possible reward while trick-or-treating', 'Pode vir de doces ou travessuras'),
    (r'Possible result from a mutant egg event', 'Pode vir de um evento de ovo mutante'),
    (r'Possible reward from investigating (?:the |a )?(.+?) mystery', lambda m: f'Pode vir ao investigar o mistério: {m[1]}'),
    (r'Possible reward from a special goat interaction', 'Pode vir de uma interação especial com cabra'),
    (r'Possible drop while chopping (\w+) trees', lambda m: f'Pode cair ao cortar árvores de {m[1]}'),
    (r'Possible box loot', 'Pode vir em caixas de loot'), (r'Monster loot', 'Loot de monstros'),
    (r'Possible reward', 'Possível recompensa'), (r'Possible result', 'Possível resultado'),
    (r'(.+?) Enhanced Loot', lambda m: f'{m[1]} (loot aprimorado)'),
    (r'Treasure Goblin [Ll]oot', 'Loot do Goblin do Tesouro'), (r'Weird Fish boss loot', 'Loot do chefe Peixe Esquisito'),
    (r'Fishing treasure', 'Tesouro de pesca'), (r'Treasure Casket', 'Baú do Tesouro'), (r'Mine book loot', 'Livro achado na mina'),
    (r'\(during raining days\)', '(em dias de chuva)'), (r'lucky roll', 'rolagem de sorte'), (r'Lucky roll', 'rolagem de sorte'),
    (r'\(mid - high roll\)', '(rolagem média a alta)'),
    (r'Age (.+?) in a (\w+); aging advances every 7 days', lambda m: f'Envelheça {m[1]} em: {m[2]} (avança a cada 7 dias)'),
    (r'Process the appropriate ingredient in a (.+)', lambda m: f'Processe o ingrediente certo em: {m[1]}'),
    (r'Process (?:a |an )?(.+?) with (.+?) in a (.+)', lambda m: f'Processe {m[1]} com {m[2]} em: {m[3]}'),
    (r'Process (?:a |an )?(.+?)(?: fruit)? in (?:a |an )?(.+?)(?: or (.+))?$',
     lambda m: f'Processe {m[1]} em: {m[2]}' + (f' ou {m[3]}' if m[3] else '')),
    (r'Smelt (.+?) in a (.+)', lambda m: f'Funda {m[1]} em: {m[2]}'),
    (r'Prepare at a prep table: (.+)', lambda m: f'Mesa de Preparo: {m[1]}'),
    (r'Prepare with a coffee maker: (.+)', lambda m: f'Cafeteira: {m[1]}'),
    (r"a craftsman's bench: (.+)", lambda m: f'Bancada do Artesão: {m[1]}'),
    (r"a tinker's desk: (.+)", lambda m: f'Mesa do Inventor: {m[1]}'),
    (r'^oven: (.+)', lambda m: f'Forno: {m[1]}'), (r'^Juice: (.+)', lambda m: f'Espremedor: {m[1]}'),
    (r'^Upgrade: (.+)', lambda m: f'Melhoria: {m[1]}'), (r'^Utility: (.+)', lambda m: f'Utilidades: {m[1]}'),
    (r'^Scarecrows: (.+)', lambda m: f'Espantalhos: {m[1]}'), (r'^Large Objects: (.+)', lambda m: f'Objetos grandes: {m[1]}'),
    (r'^Decorative: (.+)', lambda m: f'Decoração: {m[1]}'), (r'^Craft (\d+) at a (.+)', lambda m: f'Crie {m[1]} em: {m[2]}'),
    (r'Failed craft result at (?:Food: )?(.+?)(?= Failed|$)', lambda m: f'Resultado de receita que falhou: {m[1]}'),
    (r'; recipe learned from (.+?) at (.+)', lambda m: f'; receita aprendida com {m[1]} em: {m[2]}'),
    (r'Collect from (chickens|goats|cows) through Husbandry; size and quality depend on the animal and quality roll',
     lambda m: 'Colete {} pela criação de animais; tamanho e qualidade dependem do animal'.format(
         {'chickens': 'das galinhas', 'goats': 'das cabras', 'cows': 'das vacas'}[m[1]])),
    (r'Collect from a placed (.+)', lambda m: f'Colete de um(a) {m[1]} instalado(a)'),
    (r'Collect from (.+?) resource spawns', lambda m: f'Colete de pontos de {m[1]}'),
    (r'Forage from (.+?) resource spawns', lambda m: f'Colete de pontos de {m[1]}'),
    (r'Chop (.+?) resource trees', lambda m: f'Corte árvores de {m[1]}'),
    (r'Mine rare high-tier ore nodes in the Catacombs mines or deeper Mall Mines',
     'Minere veios raros de nível alto nas minas das Catacumbas ou no fundo das Minas do Shopping'),
    (r'Mine spawned (.+?) in the deeper Mall Mines', lambda m: f'Minere {m[1]} no fundo das Minas do Shopping'),
    (r'Harvest from the corresponding mature crop', 'Colha a planta madura correspondente'),
    (r'Harvest from a (.+?) tree', lambda m: f'Colha de uma árvore de {m[1]}'),
    (r'Collected from Lighting Rod the day after a thunder storm', 'Colete do Para-raios no dia seguinte a uma tempestade'),
    (r'Starts pre-placed in the Farmhouse; pick it up to add it to inventory', 'Já começa na Casa da Fazenda; pegue para pôr no inventário'),
    (r'Milk the "Tentacow" imposter when it appears on the Ranch', 'Ordenhe a impostora "Tentavaca" quando ela aparecer no Rancho'),
    (r'Feed Living Soul to Fallen Angel in Old Woods', 'Dê uma Alma Viva ao Anjo Caído no Bosque Antigo'),
    (r'Granted automatically when a Streamer Mode save is initialized', 'Vem automaticamente ao criar um save no Modo Streamer'),
    (r'Convert another bait type into a (.+?) through the fishing bait-swap menu', lambda m: f'Troque outra isca por {m[1]} no menu de troca de iscas'),
    (r'Chance to find after consuming an (.+)', lambda m: f'Pode aparecer ao usar um(a) {m[1]}'),
    (r'Gift from (\w+) during (?:a )?[Ff]arm visit', lambda m: f'Presente de {m[1]} numa visita à fazenda'),
    (r'(.+?) upon satisfying a cooking task', lambda m: f'{m[1]}, ao concluir uma tarefa de culinária'),
    (r'(.+?) upon completing the task (.+)', lambda m: f'{m[1]}, ao concluir a tarefa {m[2]}'),
    (r'(.+?) after completing (?:stage (\d) of )?"(.+?)" task', lambda m: f'{m[1]} depois de concluir ' + (f'a etapa {m[2]} de ' if m[2] else '') + f'a tarefa "{m[3]}"'),
    (r'Completing "(.+?)" task', lambda m: f'Ao concluir a tarefa "{m[1]}"'),
    (r'Purchased from (.+?) after completing "(.+?)" task', lambda m: f'Comprado de {m[1]} depois da tarefa "{m[2]}"'),
    (r'Purchased from (.+?) after building house upgrade (\d)(?: and Defeating the (.+))?',
     lambda m: f'Comprado de {m[1]} depois da melhoria {m[2]} da casa' + (f' e de derrotar: {m[3]}' if m[3] else '')),
    (r"(.+?)'s shop after (?:completing|finishing),? \"?(.+?)\"? [Tt]ask", lambda m: f'Loja do {m[1]}, depois da tarefa "{m[2]}"'),
    (r"(.+?)'s shop after building a barn or coop", lambda m: f'Loja do {m[1]}, depois de construir um celeiro ou galinheiro'),
    (r"(.+?)'s shop$", lambda m: f'Loja do {m[1]}'),
    (r'(.+?)\'s Tasks "(.+?)"', lambda m: f'Tarefas de {m[1]}: "{m[2]}"'),
    (r'Sold in (.+)', lambda m: f'Vendido em: {m[1]}'),
    (r'Lake Apparition event', 'Evento da Aparição do Lago'), (r'from a spawned blood-resource node', 'de um ponto de sangue que aparece no mapa'),
    (r'One of the Library rooms', 'Uma das salas da Biblioteca'), (r'the Chef in the Library', 'o Chef na Biblioteca'),
    (r'Farming Hay seed', 'Plantando Semente de Feno'), (r'Answering "knowledge" on one of Edwin\'s events', 'Respondendo "conhecimento" num evento do Edwin'),
    (r'Found in (.+?)\'s closet', lambda m: f'No armário de {m[1]}'), (r'Found in chests in (.+)', lambda m: f'Em baús de: {m[1]}'),
    (r'\(after an unlock\)', '(depois de liberar)'), (r'; stocked at (.+)', lambda m: f'; à venda em: {m[1]}'),
    (r'A gift after completing (.+?) tasks? (".+?")', lambda m: f'Presente depois das tarefas de {m[1]}: {m[2]}'),
    (r'Forged in the (.+)', lambda m: f'Forjado em: {m[1]}'), (r'Obtained during the (.+?) event', lambda m: f'Durante o evento {m[1]}'),
    (r'Gifts of (\w+)', lambda m: f'Dádivas de {m[1]}'), (r'(.+?) reward$', lambda m: f'{m[1]} (recompensa)'),
    (r'\((\d+) - (\d+) roll\)', lambda m: f'(rolagem {m[1]}–{m[2]})'), (r'(Low|Mid|High) roll', lambda m: {'Low': 'Rolagem baixa', 'Mid': 'Rolagem média', 'High': 'Rolagem alta'}[m[1]]),
    (r' from ', ' de '), (r'Can be purchased from the bait shop', 'Dá para comprar na Loja de Iscas'),
    (r'\(held on the 7th and 21st of every season\)', '(nos dias 7 e 21 de cada estação)'), (r'Room(\d)', lambda m: f'Sala {m[1]}'),
    (r'Beehive', 'Colmeia'), (r'Pumpkins', 'Abóboras'),
    (r' or better', ' ou melhor'), (r'(\w+) only', lambda m: f'só {m[1]}'), (r'(?<=; )(\w+) bait', lambda m: f'isca {m[1]}'),
    (r'\((\w+) improves odds\)', lambda m: f'({m[1]} aumenta a chance)'),
    (r'during (?:a )?Fishing Contest(?: days (\d+) and (\d+))?', lambda m: 'durante o Torneio de Pesca' + (f' (dias {m[1]} e {m[2]})' if m[1] else '')),
    (r'during contests', 'durante torneios'), (r' with ', ' com '), (r'Mall first-floor hallway', 'Corredor do 1º andar do Shopping'),
    (r'(\w+)/ ?(\w+) (daytime|nighttime|season)', lambda m: '{}/{} {}'.format(_season(m[1]), _season(m[2]), {'daytime': 'de dia', 'nighttime': 'à noite', 'season': ''}[m[3]]).strip()),
    (r'(\w+) (daytime|nighttime|season)', lambda m: '{} {}'.format(_season(m[1]), {'daytime': 'de dia', 'nighttime': 'à noite', 'season': ''}[m[2]]).strip()),
    (r'\bthe (Catacombs|Farm|Sewers|Deep Mall|Deep Woods|Deep Catacombs)\b', lambda m: m[1]),
    (r'Recipe Shop Purchased', 'Loja de Receitas; comprado'),
    (r'Rebirth', 'Rebirth'), (r'\bor\b', 'ou'), (r'\band\b', 'e'), (r' at ', ' em '),
]


def terms_pt(text):
    """Item, creature and place names inside a phrase, longest first, each replaced once."""
    names = {**{k: v for k, v in PLACES.items()}, **{k: v for k, v in CREATURES.items() if k not in PLACES}}
    words = sorted(set(names) | set(WORDS), key=len, reverse=True)
    out, slots = text, []
    for en in words:
        pattern = r'(?<![\w\'-])' + re.escape(en) + r'(?![\w\'-])'
        if re.search(pattern, out):
            pt = names.get(en) or WORDS.get(en)
            slots.append(pt)
            out = re.sub(pattern, f'\0{len(slots) - 1}\0', out)
    # Composite names the patterns know ("Jelly (Grape)", "Iron Bar") that are not whole words above.
    out = re.sub('\0(\\d+)\0', lambda m: slots[int(m[1])], out)
    return re.sub(r'\b(\d)F\b|\bF(\d)\b|\b(\d)f\b', lambda m: f'{m[1] or m[2] or m[3]}º andar', out)


TASK_NAMES = {}  # filled by wte.py from wte_tasks_pt, so quoted task names read in Portuguese too


def source_pt(where, item_names=()):
    """Portuguese for one "how to get it" text."""
    out = re.sub(r'"([^"]+)"', lambda m: f'"{TASK_NAMES.get(m[1], m[1])}"', where)
    for name in sorted(item_names, key=len, reverse=True):
        pt = tr(name)
        if pt and name in out:
            out = re.sub(r'(?<![\w\'-])' + re.escape(name) + r'(?![\w\'-])', pt, out)
    for pattern, repl in PHRASES:
        out = re.sub(pattern, repl, out)
    return terms_pt(out)
