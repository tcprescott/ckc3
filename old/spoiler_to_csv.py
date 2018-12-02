import json
import csv
import sys

f=open(sys.argv[1], "r")

spoiler_data = json.loads(f.read())

with open('entrances.csv', mode='w') as entrance_file:
	fieldnames = ['entrance', 'exit','direction']
	entrance_writer = csv.DictWriter(entrance_file, fieldnames=fieldnames)
	entrance_writer.writeheader()
	for entrance in spoiler_data['Entrances']:
		entrance_writer.writerow(entrance)

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
	"Ganons Tower",
	"Special"
]

ignore_locs = [
	'Frog',
	'Agahnim 1',
	'Agahnim 2',
	'Ganon',
	
	
]

with open('items.csv', mode='w') as item_file:
	fieldnames = ['region','location','item']
	item_writer = csv.writer(item_file)
	item_writer.writerow(['region','location','item'])
	for region in regions:
		for loc in spoiler_data[region]:
			if not loc in ignore_locs:
				item_writer.writerow([region,loc,spoiler_data[region].get(loc)])
