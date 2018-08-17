# libraries
from ohmysportsfeedspy import MySportsFeeds
from pprint import pprint
from pathlib import Path
import json

# functions
def get_output_from_api(username, password):
	# where api json file is stored
	path = 'results/roster_players-nfl-2017-2018-regular.json'

	# load json from results cache
	if Path(path).exists():
		with open(path, 'r') as f:
			output = json.load(f)
	# make request to API if no cache
	else:
		msf = MySportsFeeds(version="1.2", verbose=True)
		msf.authenticate(username, password)
		output = msf.msf_get_data(league='nfl', season='2017-2018-regular', feed='roster_players', format='json')

	return output

def get_player(entry):
	# store each player as an object
	player = {}

	# add respective fields for players
	try:
		player['name'] = entry['player']['FirstName'] + ' ' + entry['player']['LastName']
		player['position'] = entry['player']['Position']
		player['height'] = entry['player']['Height']
		player['weight'] = entry['player']['Weight']

	# in the case that information is missing, set field to 'N/A'
	except KeyError as error:
		attribute = str(error).strip('\'').lower()
		player[attribute] = 'N/A'

	return player

def get_team_players(output):
	# stores teams as keys and a list of player as values
	teams = {}

	# add every player from output
	for entry in output['rosterplayers']['playerentry']:
		# get player information in an object
		player = get_player(entry)

		# initializes list once from each team
		if entry['team']['Name'] not in teams:
			teams[entry['team']['Name']] = []

		# adds player to the appropriate team list
		teams[entry['team']['Name']].append(player)

	return teams

def save_to_file(teams):
	# opens file with write permissions
	f = open('results.txt', 'w')

	# converts dictionary to string and saves in file
	f.write(str(teams))

	# closes file stream
	f.close()

# commands
username = '8663abc5-a99a-4f33-90c4-c1d697'
password = 'Dk30RQHT'

output = get_output_from_api(username, password)

teams = get_team_players(output)

pprint(teams)

save_to_file(teams)
