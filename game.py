#Python Text RPG
#Dragess Tech

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####
class player:
	def __init__(self):
		self.name = ''
		self.job = ''
		self.hp = 0
		self.mp = 0
		self.status_effects = []
		self.position = 'b2'
		self.gameOver = False
myPlayer = player()

##### Title Screen #####
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("play"):
		setup_game()
	elif option.lower() == ("help"):
		help_menu()
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play', 'help', 'quit']:
		print("Please enter a valid command.")
		option = input("> ")
		if option.lower() == ("play"):
			setup_game()
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()

def title_screen():
	os.system('clear')
	print('############################')
	print('# Welcome to the Text RPG! #')
	print('############################')
	print('          - Play -          ')
	print('          - Help -          ')
	print('          - Quit -          ')
	print(' Copyright 2018 DragessTech ')
	print('############################')
	print('############################')
	title_screen_selections()

def help_menu():
	print('############################')
	print('# Welcome to the Text RPG! #')
	print('############################')
	print('- Use up, down, left, right to move')
	print('- Type your commands to do them')
	print('- Use "look" to inspect something')
	print('- Good Luck and have fun')
	print(' Copyright 2018 DragessTech ')
	print('############################')
	print('############################')
	title_screen_selections()


##### MAP #####

#a1, a2... #PLAYER STARTS AT B2
#---------
#| | | | | a4
#---------
#| | | | | b4
#---------
#| | | | |
#---------
#| | | | |
#---------

ZONENAME = 'zonename'
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
				'b1': False, 'b2': False, 'b3': False, 'b4': False,
				'c1': False, 'c2': False, 'c3': False, 'c4': False,
				'd1': False, 'd2': False, 'd3': False, 'd4': False,	
					}

zonemap = {
	'a1': {
		ZONENAME: "House 4",
		DESCRIPTION: '',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: 'b1',
		LEFT: '',
		RIGHT: 'a2',
	},
	'a2': {
		ZONENAME: "Town Entrance",
		DESCRIPTION: 'The main entrance to the town.',
		EXAMINATION: 'The route north of us leads to the neighboring village.',
		SOLVED: False,
		UP: '',
		DOWN: 'b2',
		LEFT: 'a1',
		RIGHT: 'a3',
	},
	'a3': {
		ZONENAME: "Mayor's House",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP:'',
		DOWN: 'b3',
		LEFT: 'a2',
		RIGHT: 'a4',
	},
	'a4': {
		ZONENAME: "House 6",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: 'b4',
		LEFT: 'a3',
		RIGHT: '',
	},
	'b1': {
		ZONENAME: "Inn",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP:'a1',
		DOWN: 'c1',
		LEFT: '',
		RIGHT: 'b2',
	},
	'b2': {
		ZONENAME: "Home",
		DESCRIPTION: 'This is your home!',
		EXAMINATION: 'Your home looks the same',
		SOLVED: False,
		UP: 'a2',
		DOWN: 'c2',
		LEFT: 'b1',
		RIGHT: 'b3',
	},
	'b3': {
		ZONENAME: "House 5",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: 'a3',
		DOWN: 'c3',
		LEFT: 'b2',
		RIGHT: 'b4',
	},
	'b4': {
		ZONENAME: "House 2",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: 'a4',
		DOWN: 'c4',
		LEFT: 'b3',
		RIGHT:'',
	},
	'c1': {
		ZONENAME: "**Rival's House",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: 'b1',
		DOWN: 'd1',
		LEFT: "The city wall prevents you from moving this way", 'c1',
		RIGHT: '',
	},
	'c2': {
		ZONENAME: "Town Market Entrance",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: '',
		LEFT: '',
		RIGHT: '',
	},
	'c3': {
		ZONENAME: "House 1",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: '',
		LEFT: '',
		RIGHT: '',
	},
	'c4': {
		ZONENAME: "House 7",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: '',
		LEFT: '',
		RIGHT: '',
	},
	'd1': {
		ZONENAME: "Armor Shop",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: '',
		LEFT: '',
		RIGHT: '',
	},
	'd2': {
		ZONENAME: "Item Store",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: '',
		LEFT: '',
		RIGHT: '',
	},
	'd3': {
		ZONENAME: "Weapon Store",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: '',
		LEFT: '',
		RIGHT: '',
	},
	'd4': {
		ZONENAME: "Barracks",
		DESCRIPTION: 'description',
		EXAMINATION: 'examine',
		SOLVED: False,
		UP: '',
		DOWN: '',
		LEFT: '',
		RIGHT: '',
	},

}

##### GAME INTERACTIVITY #####
def print_location():
	print('\n' + ('#' * (4 + len(myPlayer.position))))
	print('#' + myPlayer.position.upper() + '#')
	print('#' + zonemap[myPlayer.position][DESCRIPTION] + '#')
	print('\n' + ('#' * (4 + len(myPlayer.position))))

def prompt():
	print("\n" + "======================")
	print("What would you like to do?")
	action = input("> ")
	acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
	while action.lower() not in acceptable_actions:
		print("Unknown action, try again")
		action = input("> ")
	if action.lower() == 'quit':
		sys.exit()
	elif action.lower() in ['move', 'go', 'travel', 'walk']:
		player_move(action.lower())
	elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
		player_examine(action.lower())

def player_move(myAction):
	ask = "Where would you like to move to?\n"
	dest = input(ask)
	if dest in ['up', 'north']:
		destination = zonemap[myPlayer.position][UP]
		movement_handler(destination)
		prompt()
	elif dest in ['left', 'west']:
		destination = zonemap[myPlayer.position][LEFT]
		movement_handler(destination)
		prompt()
	elif dest in ['right', 'east']:
		destination = zonemap[myPlayer.position][RIGHT]
		movement_handler(destination)
		prompt()
	elif dest in ['down', 'south']:
		destination = zonemap[myPlayer.position][DOWN]
		movement_handler(destination)
		prompt()

def movement_handler(destination):
	print("\n" + "You have moved to the " + destination + ".")
	myPlayer.position = destination
	print_location()

def player_examine(action):
	if zonemap[myPlayer.position][SOLVED]:
		print("You have already exhausted this zone.")
		prompt()
	else:
		print("You can trigger a puzzle here.")
		prompt()



##### GAME FUNCTIONALITY #####

def main_game_loop():
	while myPlayer.gameOver is False:
		prompt()
		#Handle if puzzles have been solved, boss defeated, explored everything.

def setup_game():
	os.system('clear')

	### NAME ###
	question1 = "Hello, what's your name?\n"
	for character in question1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	player_name = input("> ")
	myPlayer.name = player_name

	### JOB ###
	question2 = "And what role(class) do you want to be?\n"
	question2added = "(You can play as a Warrior, Priest, or Mage)\n"
	for character in question2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in question2added:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.01)
	player_job = input("> ")
	valid_jobs = ['warrior', 'mage', 'priest']
	if player_job.lower() in valid_jobs:
		myPlayer.job = player_job
		print("You are now a " + player_job + "!\n")
	while player_job.lower() not in valid_jobs:
		print("Invalid input, please try again.")
		print("Would you like to be a Warrior, Priest, or Mage?")
		player_job = input("> ")
		if player_job.lower() in valid_jobs:
			myPlayer.job = player_job
			print("You are now a " + player_job + "!\n")

	### PLAYER STATS ###
	if myPlayer.job is 'warrior':
		self.hp = 120
		self.mp = 20
		
	elif myPlayer.job is 'priest':
		self.hp = 40
		self.mp = 120
		
	elif myPlayer.job is 'mage':
		self.hp = 60
		self.mp = 100
		

	### INTRODUCTION ###
	question3 = "Welcome, " + player_name + " the " + player_job +".\n"
	for character in question3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	

	speech1 = "Welcome to this fantasy world.\n"
	speech2 = "I hope it greets you well.\n"
	speech3 = "Just make sure you don't get too lost...\n"
	speech4 = "Hehehehe.....\n"
	for character in speech1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	for character in speech2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)	
	for character in speech3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.1)
	for character in speech4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.2)

	os.system('clear')
	print("######################")
	print("#   Let's start now!  ")
	print("######################")
	main_game_loop()

title_screen()