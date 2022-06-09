# import dependencies
import random 
from functions import ran_boat_positions, personalize_your_board, turns
from classes import Board
from colorama import Fore
import pyfiglet 

# Interact with player: get main info (name)
print("Hello! This is: \n" ) 
title = pyfiglet.figlet_format( " BATTLESHIP \n", font = 'standard', justify= 'centre')
print(Fore.BLUE + title)
user_name = input(Fore.WHITE + "What's your name? ")
print(Fore.WHITE +f"{user_name} let's play Battleship!\n ")

# explain game
rules = f"The aim of the game is to sink all of your opponents battleships before they sink yours. \n Both you and your opponent, in this case the computer, get 10 boats that will be positioned on the board. You then take turns to shoot at each other. It's easy {user_name}, you'll get the hang of it. "
print(rules)

# initialize user board
# allows user to decide whether to place their own boats or have them randomly placed
user_board = Board.start_board(user_name)
user_board = personalize_your_board(user_board)

# initialize computer board (random)
computer_board = Board.start_board('computer')
computer_board = ran_boat_positions(computer_board)
print( "I've placed my boats but you can't see where... hahaha")

# initialize boards to track shots 
computer_shots = Board.start_board('c_shots')
user_shots = Board.start_board('u_shots')
print(f"Here is where you will track your shots: {user_shots}")
user_hits = 0
computer_hits = 0

# flip a coin to decide who starts game, input result into main game turns
quien_empieza = input("Heads or Tails ")
cara_cruz = random.choice(['Heads','Tails'])

if quien_empieza.lower() == cara_cruz.lower() : 
    print("You start!")
    start = True
else: 
    print("I start!")
    start = False

turns(start, computer_shots, user_board, computer_hits, user_shots, computer_board, user_hits)