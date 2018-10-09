#Python Text Role Playing Game
#Name WIP
#Copyright 2018 DragessTech

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player character setup
class player1:
    def __init__(self):
        self.name = ""  #Player choosen name
        self.race = ""  #Human, Elf, Dwarf, or Orc
        self.age = 20
        self.job = ""  #Player class: Warrior, Priest, Thief, etc
        self.hp = 0  #Player's health points
        self.mp = 0  #Player's magic points
        self.status_effects = []  #Poison, Paralyze, Burn
        self.position = 'home'  #Where player starts
        self.game_over = False
        self.strength = 0  #Controls how much damage done
        self.constitution = 0  #Controls how many Health Points and resistances
        self.wisdom = 0  #Controls how much magic/skill damage done
        self.intelligence = 0  #Controls how many Magic Points
        self.dexterity = 0  #Controls attack speed, and chance of dodge
        self.charisma = 0  #Used for charisma checks
        self.luck = 5  #Controls random chances

myPlayer = player1()  #Assignes the player class to myplayer variable

##### Player Stat Setup #####
#Create race, jobs, status effects, etc
        ### Races ###
                ## Human ##
                ## Elf ##
                ## Dwarf ##
                ## Orc ##
        ### Jobs ###
valid_jobs = ['warrior', 'priest', 'thief', 'tank', 'mage']
def player1_job():
                ## Warrior ##
    if myPlayer.job is 'warrior':
        self.hp = 100
        self.mp = 40
        self.strength = 0
        self.constitution = 0
        self.wisdom = 0
        self.intelligence = 0
        self.dexterity = 0
        self.charisma = 0

                ## Priest ##
    elif myPlayer.job is 'priest':
        self.hp = 40
        self.mp = 120
        self.strength = 0
        self.constitution = 0
        self.wisdom = 0
        self.intelligence = 0
        self.dexterity = 0
        self.charisma = 0

                ## Thief ##
    elif myPlayer.job is 'thief':
        self.hp = 60
        self.mp = 60
        self.strength = 0
        self.constitution = 0
        self.wisdom = 0
        self.intelligence = 0
        self.dexterity = 0
        self.charisma = 0

                ## Tank ##
    elif myPlayer.job is 'tank':
        self.hp = 120
        self.mp = 20
        self.strength = 0
        self.constitution = 0
        self.wisdom = 0
        self.intelligence = 0
        self.dexterity = 0
        self.charisma = 0

                ## Mage ##
    elif myPlayer.job is 'mage':
        self.hp = 60
        self.mp = 100
        self.strength = 0
        self.constitution = 0
        self.wisdom = 0
        self.intelligence = 0
        self.dexterity = 0
        self.charisma = 0
        ### Status Effects ###
                ## Poison ##
                ## Paralyze ##
                ## Burn ##
                ## Blindness ##
        ### Stat Breakdown ###
                ## Strength ##
                ## Constitution ##
                ## Wisdom ##
                ## Intelligence ##
                ## Dexterity ##
                ## Charisma ##

##### Game Functionality #####
#

##### Game Interactivity #####
#Game movement and actions
        ### Movement ###
def player_move(myAction):
    ask = "Where would you like to move to?"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.position][UP]
        movement_handler(destination)
        prompt()
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.position][DOWN]
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

def movement_handler():
    print('\n' + 'You have moved to the ' + destination + '.')
    myPlayer.position = destination
    print_location()

        ### Attacks ###
                ## Melee ##
                ## Magic ##
                ## Healing ##

        ### Non combat actions ###
                ## Look Around ##
def player_look():
    print("To my left is ") #Says what is to the left
    print("To my right is ") #Says what is to the right
    print("Up ahead is ") #Says what is forward
    print("Behind me is ") #Says what is to the rear
    prompt()

                ## Examine/Inspect ##
def player_examine():
    if zonemap[myPlayer.position][SOLVED]:
        print("I've already looked at everything here.")
        prompt()
    else:
        print("Let's see here...")
        prompt()
##### Map Creation #####
        ### MAP 1 ###
        ### MAP 2 ###
        ### MAP 3 ###
        ### MAP 4 ###
##### Game Run #####
#Game run
        ### Title Screen ###
def title_screen_selection():
    option = input('>> ')
    if option.lower() == ('play'):
        game_setup()  #Starts game
    elif option.lower() == ('help'):
        help_menu() #Shows help menu
    elif option.lower() == ('quit'):
        sys.exit() #Quits game

def title_screen():
    os.system('clear')
    print("#######################################") #40 #s
    print(" ## Welcome to Dragon Knight Arena  ## ")
    print("#######################################")
    print('#             - Play -                #')
    print('#             - Help -                #')
    print('#             - Quit -                #')
    print('#      Copyright 2018 DragessTech     #')
    print("#######################################")
    print("#######################################")
    title_screen_selection()

        ### Help Screen ###
def help_menu():
    print("#######################################")
    print(" ## Welcome to Dragon Knight Arena  ## ")
    print("#######################################")
    print(" - Type your commands to use them - ")
    print(" - Type up, down, left, right to move -")
    print(" - Type look to see movement options available -")
    print(" - Type examine to inspect items - ")
    print("#######################################")
    print("#######################################")
    title_screen_selection()

        ### Character Setup ###
def game_setup():
    print("Hello there.   Welcome to the world of Radiance.  This dark world is....")
    name_collection()
                ## Name Collection ##
def name_collection():
    print("Let's start with your name.")
    player_name = input(">> ")
    myPlayer.name = player_name
    age_collection()
                ## Age Collection ##
def age_collection():
    print("And how old are you?")
    player_age = input(">> ")
    myPlayer.age = player_age
    job_selection()
                ## Job Selection ##
def job_selection():
    print("You have a choice to choose your Race and Class, or you can answer some more questions and have that decide.")
    stat_creation = input(">> ")
    if stat_creation.lower() == 'yes':
        print("Hello")
        race_selection()
    elif stat_creation.lower() == 'no':
        print("World")
        questionare()
                ## Race Selection ##
def race_selection():
    print("")
    print("In our world, there are 4 known races.  The Humans, Elves, Dwarves, and Orcs.")
    print("The Humans are ...")
    print("The Elves are ...")
    print("The Dwarves are ...")
    print("The Orcs are ...")
    print("After hearing of these races, which do you align yourself with?")
    race_creation = input(">> ")
    myplayer.race = race_creation
    job_selection()

                ## Job Selection
def job_selection():
    print("")
    print("There are many branches of classes available to able adventures.")
    print("But everyone must start somewhere.  For you, 4 are available.")
    print("Warriors are ...")
    print("Mages are ...")
    print("Tanks are ...")
    print("Thieves are ...")
    print("Priests are ...")
    print("After hearing of these classes, which do you see your self being?")
    job_creation = input(">> ")
    myplayer.job = job_creation


                ## Questionare for Stats ##
def questionare():
    print("")


        ### Main Game ###
                ## Introduction ##
title_screen()


                ## Act 1 ##
                ## Act 2 ##
                ## Act 3 ##
                ## Act 4 ##
                ## Finale ##
