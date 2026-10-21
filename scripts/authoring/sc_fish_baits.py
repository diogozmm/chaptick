"""Which bait catches each fish in Trails in the Sky 2nd Chapter (Neoseeker Fishing Notes).

The bait decides what bites, and fish caught earlier work as bait for bigger ones. The chapter
files were edited by hand after they were generated, so their JSON is the source and this script
adds `baits` and `fishBaits` to every fish. Idempotent.
"""
import json

from lib import ROOT

# bait -> fish it catches, in the order of the guide's table.
BAITS = {
    'Earthworm': ['Crab', 'Tiger Rockfish', 'Rainbow Trout', 'Carp', 'Rockeater', 'Trout', 'Eel', 'Pearlglass'],
    'Larva': ['Kasagin', 'Yamany', 'Tiger Rockfish', 'Liberl Carp', 'Rainbow Trout', 'Rockeater', 'Salmon'],
    'Salmon Roe': ['Kasagin', 'Yamany', 'Tiger Rockfish', 'Rainbow Trout', 'Rockeater', 'Trout', 'Salmon'],
    'Red Fly': ['Kasagin', 'Yamany', 'Tiger Rockfish', 'Liberl Carp', 'Trout'],
    'Dumpling': ['Liberl Carp', 'Carp', 'Pearlglass'],
    'Pond Snail': ['Carp', 'Rockeater', 'Pearlglass'],
    'Frog': ['Valleria Bass', 'Rockeater', 'Snakehead'],
    'Marine Worm': ['Crab', 'Gold Angelfish', 'Kasago', 'Great Blackfish', 'Claudine'],
    'Shrimp': ['Crab', 'Gold Angelfish', 'Kasago', 'Great Blackfish', 'Sea Bass', 'Trout', 'Octopus'],
}
FISH_BAITS = {
    'Crab': ['Carp', 'Rockeater', 'Claudine', 'Octopus', 'Granakor'],
    'Kasagin': ['Great Blackfish', 'Valleria Bass', 'Sea Bass', 'Rockeater', 'Salmon', 'Claudine', 'Snakehead', 'Mahi-Mahi'],
    'Yamany': ['Valleria Bass', 'Rockeater', 'Snakehead'],
    'Kasago': ['Sea Bass', 'Claudine', 'Octopus', 'Gigangora'],
    'Sea Bass': ['Mahi-Mahi', 'Gigangora', 'Blue Marlin'],
    'Carp': ['Snakehead', 'Garvelze'],
    'Trout': ['Snakehead', 'Garvelze', 'Dynatrad'],
    'Salmon': ['Snakehead', 'Mahi-Mahi', 'Garvelze', 'Gigangora', 'Blue Marlin', 'Dynatrad'],
    'Eel': ['Snakehead', 'Garvelze'],
}

seen = set()
for path in sorted((ROOT / 'sc' / 'chapters').glob('ch-*.json')):
    data = json.loads(path.read_text())
    for fish in data.get('fish', []):
        name = fish['name']['en']
        baits = [b for b, caught in BAITS.items() if name in caught]
        fish_baits = [b for b, caught in FISH_BAITS.items() if name in caught]
        assert baits or fish_baits, f'no bait found for {name}'
        fish['baits'], fish['fishBaits'] = baits, fish_baits
        if not baits:
            del fish['baits']
        if not fish_baits:
            del fish['fishBaits']
        seen.add(name)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
assert len(seen) == 26, seen
print('baits set for', len(seen), 'fish')
