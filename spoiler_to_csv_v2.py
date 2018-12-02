import json
import csv
import sys
# from collections import OrderedDict
from itertools import islice

f=open(sys.argv[1], "r")

spoiler_data = json.loads(f.read())

with open('csv/entrances.csv', mode='w') as entrance_file:
	fieldnames = ['entrance', 'exit','direction']
	entrance_writer = csv.DictWriter(entrance_file, fieldnames=fieldnames)
	entrance_writer.writeheader()
	for entrance in spoiler_data['Entrances']:
		entrance_writer.writerow(entrance)

ignore_paths = [
	'Sanctuary',
	'Zora\'s Ledge',
	'Mushroom',
	'King Zora',
	'Sunken Treasure',
	'Bottle Merchant',
]

dungeon_prefix = [
	'Eastern Palace - ',
	'Desert Palace - ',
	'Tower of Hera - ',
	'Palace of Darkness - ',
	'Swamp Palace - ',
	'Skull Woods - ',
	'Thieves\' Town - ',
	'Ice Palace - ',
	'Misery Mire - ',
	'Turtle Rock - ',
	'Ganons Tower - '
]

ignore_entrances = [
	'Agahnim 1',
	'Agahnim 2',
	'Blind Fight',
	'Ganons Tower (Before Moldorm)',
	'Ganons Tower (Firesnake Room)',
	'Ganons Tower (Firesnake Room)',
	'Ganons Tower (Hookshot Room)',
	'Ganons Tower (Hookshot Room)',
	'Ganons Tower (Moldorm)',
	'Ganons Tower (Teleport Room)',
	'Ganons Tower (Teleport Room)',
	'Ganons Tower (Top)',
	'Ice Palace (East Top)',
	'Ice Palace (East)',
	'Ice Palace (East)',
	'Ice Palace (Kholdstare)',
	'Ice Palace (Main)',
	'Misery Mire (Final Area)',
	'Misery Mire (Main)',
	'Misery Mire (Vitreous)',
	'Misery Mire (West)',
	'Palace of Darkness (Bonk Section)',
	'Palace of Darkness (Center)',
	'Palace of Darkness (Final Section)',
	'Paradox Cave Chest Area',
	'Skull Woods Final Section (Mothula)',
	'Skull Woods First Section (Right)',
	'Swamp Palace (Center)',
	'Swamp Palace (First Room)',
	'Swamp Palace (First Room)',
	'Swamp Palace (North)',
	'Swamp Palace (Starting Area)',
	'Thieves Town (Deep)',
	'Thieves Town (Deep)',
	'Tower of Hera (Top)',
	'Tower of Hera (Top)',
	'Turtle Rock (First Section)',
	'Turtle Rock (First Section)',
	'Turtle Rock (Trinexx)',
	'Links House Exit',
	'Links House',
]

def paths_to_export(spoiler_data):
	arr = []
	for path in spoiler_data['paths']:
		if path.startswith(tuple(dungeon_prefix)) and not path.endswith(' - Prize'):
			pass
		else:
			arr.append(path)
	return(arr)

def build_path(spoiler_data):
	dict = {}
	paths_to_use = paths_to_export(spoiler_data)
	for path in spoiler_data['paths']:
		print(path)
		patharr = []
		pathsteps = spoiler_data['paths'].get(path)
		stepnum = 0
		entrance = pathsteps[0][1]
		for i, step in enumerate(pathsteps):
			exit = step[0]
			if (not entrance in ignore_entrances and not exit in ignore_entrances) and path in paths_to_use:
				stepnum += 1
				record = {
					'entrance': entrance,
					'exit': exit,
					'step': stepnum,
				}
				patharr.append(record)

			entrance = step[1]


		# try:
		# 	del patharr[-1]
		# 	shortpath = path.split(' - ')[0]
		# 	dict[shortpath] = patharr
		# except IndexError:
		# 	pass
		shortpath = path.split(' - ')[0]
		dict[shortpath] = patharr
	return dict



with open('csv/paths.csv', mode='w') as path_file:
	fieldnames = ['path','entrance1','exit1','step1','entrance2','exit2','step2','steptotal']
	path_writer = csv.writer(path_file)
	path_writer.writerow(fieldnames)
	pathset = build_path(spoiler_data)
	for pathname in pathset:
		i = 0
		print(pathname)
		path = pathset.get(pathname)
		while i < len(path):
			print(i)
			entrance1 = path[i]['entrance']
			exit1 = path[i]['exit']
			step1 = path[i]['step']
			i += 1
			try:
				entrance2 = path[i]['entrance']
				exit2 = path[i]['exit']
				step2 = path[i]['step']
			except IndexError:
				entrance2 = ''
				exit2 = ''
				step2 = ''
			i += 1
			steptotal = len(path)
			path_writer.writerow([pathname,entrance1,exit1,step1,entrance2,exit2,step2,steptotal])

regions = [
	"Light World",
	"Dark World",
	"Caves",
	"Hyrule Castle",
	"Eastern Palace",
	"Desert Palace",
	"Tower of Hera",
	"Agahnims Tower",
	"Palace of Darkness",
	"Thieves Town",
	"Skull Woods",
	"Swamp Palace",
	"Ice Palace",
	"Misery Mire",
	"Turtle Rock",
	"Ganons Tower"
]

ignore_locs = [
	'Frog',
	'Agahnim 1',
	'Agahnim 2',
	'Ganon',
	'Dark Blacksmith Ruins',
	'Missing Smith',
	'Floodgate',
]

always_include_locs = [
	'Master Sword Pedestal',
	'Purple Chest',
	'Catfish',
	'King Zora',
	'Hobo',
	'Library',


]

ignore_items = [
	'Arrows (10)',
	'Piece of Heart',
	'Bombs (3)',
	'Bombs (10)',
	'Rupee (1)',
	'Rupees (5)',
	'Rupees (20)',
	'Rupees (50)',
	'Rupees (100)',
	'Map (Escape)',
	'Map (Misery Mire)',
	'Map (Tower of Hera)',
	'Map (Swamp Palace)',
	'Map (Palace of Darkness)',
	'Map (Thieves Town)',
	'Map (Eastern Palace)',
	'Map (Ganons Tower)',
	'Map (Ice Palace)',
	'Map (Skull Woods)',
	'Map (Desert Palace)',
	'Map (Turtle Rock)',
	'Compass (Misery Mire)',
	'Compass (Tower of Hera)',
	'Compass (Swamp Palace)',
	'Compass (Palace of Darkness)',
	'Compass (Thieves Town)',
	'Compass (Eastern Palace)',
	'Compass (Ganons Tower)',
	'Compass (Ice Palace)',
	'Compass (Skull Woods)',
	'Compass (Desert Palace)',
	'Compass (Turtle Rock)'
]

with open('csv/items.csv', mode='w') as item_file:
	fieldnames = ['region','location','item']
	item_writer = csv.writer(item_file)
	item_writer.writerow(['region','location','item'])
	for region in regions:
		for loc in spoiler_data[region]:
			item = spoiler_data[region].get(loc)
			if (not loc in ignore_locs and not item in ignore_items) or loc in always_include_locs:
				item_writer.writerow([region,loc,item])

ignore_dungeons = [
	'Ganon',
	'Ganons Tower',
	'Hyrule Castle',
]

with open('csv/bosses.csv', mode='w') as item_file:
	fieldnames = ['dungeon','boss']
	item_writer = csv.writer(item_file)
	item_writer.writerow(['dungeon','boss'])
	for dungeon in spoiler_data['Bosses']:
		boss = spoiler_data['Bosses'].get(dungeon)
		if not dungeon in ignore_dungeons:
			item_writer.writerow([dungeon,boss])
