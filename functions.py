# GAME FUNCTIONS
import random
import time 

# FUNCTION: TURNS
def turns(start, computer_shots, user_board, computer_hits, user_shots, computer_board, user_hits):
    ''' game turns: computer and user
    
    '''


    while user_hits != 20 and computer_hits != 20:
        # user turn
        if start == True: 
            correct = True
            while correct == True:
                print(user_shots)
                user_shot_coords = input("Choose where you'd like to shoot, introduce coordinated: x,y")
                shot_coords = user_shot_coords.split(",")
                x = int(shot_coords[0]) -1
                y = int(shot_coords[1]) -1
                if user_shots[x,y] == ' ':
                    if computer_board[x,y] == 'O':
                        computer_board[x, y] = 'X'
                        user_shots[x,y] = 'X'
                        user_hits += 1
                        correct = True
                        start = True
                        print(f"Oh no, you hit my boat... you can go again. For now, you've hit me: {user_hits} times, this is your shot record: \n {user_shots}")
                    else:
                        user_shots[x,y] = '-'
                        correct = False
                        start = False
                        print(f"you failed, these are your shots for now: \n {user_shots}")
                else:
                    print('you already shot there... try again, these are the places you\'ve shot already \n {user_shots}')
                print(f"You got {user_hits} hits \n")

        # turno del ordenador
        if start == False: 
            correct = True
            while correct == True :
                random_row = random.randint(0,9)
                random_column = random.randint(0,9)
                if computer_shots[random_row,random_column] == ' ' :
                    if user_board[random_row, random_column] == 'O':
                        user_board[random_row, random_column] = 'X'
                        computer_shots[random_row,random_column] = 'X'
                        time.sleep(2)
                        computer_hits += 1
                        print(f"I hit you on {random_row, random_column}, I've hit you {computer_hits} times")
                        start = False
                        correct = True
                    else:
                        user_board[random_row, random_column] = '-'
                        computer_shots[random_row,random_column] = '-'
                        time.sleep(2)
                        print(f"Ah, I missed. You've got water at {random_row, random_column} you're turn")
                        start = True
                        correct = False 
            print(f"I'm on {computer_hits} hits \n")

    if computer_hits == 20: 
        print("I win!")
    else: 
        print("Congratulations, you beat me.") 

##################################################################################################################################

# function that evaluates how the player wants to place their boats on their board
import time
import numpy as np
import random

def personalize_your_board(user_board):
    
    try:
        choose_your_board = input("Would you like to place your own boats, or have them places randomly? Yes or no? ")
    except ValueError as e:
        print("I need you to type in your answer")
    else:
        if choose_your_board.lower() == 'yes' or choose_your_board.lower() == 'y' :
            print("You will have to position 10 boats in total. You have 4 boats which are 1 block long, 3 which are 2 blocks, 2 which are 3 blocks and 1 which is 4.\n This is the board where you'll have to place them. ")
            print(np.full((10,10), ' '))
            time.sleep(0.5)
            boat_position(user_board)
            time.sleep(1)
        elif choose_your_board.lower() == 'no' or choose_your_board.lower() == 'n':
            ran_boat_positions(user_board)
            print("Cool, your boats have been randomly placed")
            print(user_board)
            time.sleep(0.5)
        else:
            print("I need you to type in your answer")
            # personalize_your_board(user_board)

    return user_board


# Two functions that position boats in different ways: 1 according to inputs and the other randomly

def boat_position(board):
    # inputs -->
    #           outputs --> array “board”

    board_count = np.count_nonzero(board == 'O')
    num_barco = 0

    while board_count != 4:
        try:
            coords = input(f"Give me a pair of (x,y) coordinates for your boat nº{num_barco + 1} of 1 length: ")
            barco_coordenadas = coords.split(",")
            # Coordinates adjusted to python indices
            x = int(barco_coordenadas[0]) -1
            y = int(barco_coordenadas[1]) -1
        except (ValueError, IndexError) as e:
            print("I need you to give me two numbers between 1 and 10")
        else:
            try:
                board[x,y]
            except IndexError as e:
                print("Don't get too big for the board...")
            else:
                if board[x,y]== 'O':
                    print('You already have a boat there...')
                else:
                    board[x,y] = 'O'
                    board_count += 1
                    num_barco += 1
                    print(board)

    while board_count != 10:
        boat_size = 2
        try:
            coords = input(f"Give me a pair of (x,y) coordinates for your boat nº{num_barco + 1}, 2 blocks long: ")
            barco_coordenadas = coords.split(",")
            x = int(barco_coordenadas[0]) -1
            y = int(barco_coordenadas[1]) -1
        except (ValueError, IndexError) as e:
            print("I need you to give me two numbers between 1 and 10, separated by a ',' ")
        else:
            try:
                board[x,y]
            except IndexError as e:
                print("Don't get too big for the board...")
            else:
                if board[x,y]==' ':
                    dir = input("Choose a direction: North, South, East, West ")
                    # First condition: to check for human error in direction input
                    if is_direction(dir) == True:
                        # Second condition: to make sure it will fit on the board in that direction 
                        if (dir.lower() == 'north' or dir.lower() == 'n') and ((x -1 ) > 0):
                            # Third condition: to make sure the boat isn't overlapping with other boats 
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x-(boat_size-1) : x+1, y] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        elif (dir.lower() == 'east' or dir.lower() == 'e') and ((y + 1) < len(board)):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x, y: y + (boat_size)] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        elif (dir.lower() == 'south' or dir.lower() == 's') and ((x +1) < len(board)):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x: x + (boat_size), y] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        elif (dir.lower() =='west' or dir.lower() == 'w') and ((y - 1) > 0):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x, y-(boat_size-1): y+1] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        else:
                            print("Don't get too big for the board... try a different combination! ")
                    else:
                        print('I asked for a direction: N, E, S, W')
                else:
                    print('You already have a boat there...')

    while board_count != 16:
        boat_size = 3
        try:
            coords = input(f"Give me a pair of (x,y) coordinates for your boat nº{num_barco + 1}, 3 blocks long: ")
            barco_coordenadas = coords.split(",")
            x = int(barco_coordenadas[0]) -1
            y = int(barco_coordenadas[1]) -1
        except (ValueError, IndexError) as e:
            print("I need you to give me two numbers between 1 and 10, separated by a ',' ")
        else:
            try:
                board[x,y]
            except IndexError as e:
                print("Don't get too big for the board...")
            else:
                if board[x,y]==' ':
                    dir = input("Choose a direction: North, South, East, West ")
                    if is_direction(dir) == True:
                        if (dir.lower() == 'north' or dir.lower() == 'n') and ((x -1 ) > 0):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x-(boat_size-1) : x+1, y] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        elif (dir.lower() == 'east' or dir.lower() == 'e') and ((y + 1) < len(board)):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x, y: y + (boat_size)] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        elif (dir.lower() == 'south' or dir.lower() == 's') and ((x +1) < len(board)):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x: x + (boat_size), y] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        elif (dir.lower() =='west' or dir.lower() == 'w') and ((y - 1) > 0):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x, y-(boat_size-1): y+1] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        else:
                            print("Don't get too big for the board... or try a different combination! ")
                    else:
                        print('I asked for a direction: N, E, S, W')
                else:
                    print('You already have a boat there...')

    while board_count != 20:
        boat_size = 4
        try:
            coords = input(f"Give me a pair of (x,y) coordinates for your boat nº{num_barco + 1}, 4 blocks long: ")
            barco_coordenadas = coords.split(",")
            x = int(barco_coordenadas[0]) -1
            y = int(barco_coordenadas[1]) -1
        except (ValueError, IndexError) as e:
            print("I need you to give me two numbers between 1 and 10, separated by a ',' ")
        else:
            try:
                board[x,y]
            except IndexError as e:
                print("Don't get too big for the board...")
            else:
                if board[x,y]==' ':
                    dir = input("Choose a direction: North, South, East, West ")
                    if is_direction(dir) == True:
                        if (dir.lower() == 'north' or dir.lower() == 'n') and ((x -1 ) > 0):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x-(boat_size-1) : x+1, y] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        elif (dir.lower() == 'east' or dir.lower() == 'e') and ((y + 1) < len(board)):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x, y: y + (boat_size)] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        elif (dir.lower() == 'south' or dir.lower() == 's') and ((x +1) < len(board)):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x: x + (boat_size), y] = 'O'
                                board_count += boat_size
                                num_barco += 1
                                print(board)
                        elif (dir.lower() =='west' or dir.lower() == 'w') and ((y - 1) > 0):
                            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                                board[x, y-(boat_size-1): y+1] = 'O'
                                board_count += boat_size
                                num_barco += 1
                        else:
                            print("Don't get too big for the board... try again")
                    else:
                        print('I asked for a direction: N, E, S, W')
                else:
                    print('You already have a boat there...')

        print(f"Great, here's how it looks: \n {board}")

    return board

###############################################################################################################################################
# Creating a random board

def ran_boat_positions(board):
    # 10 boats positioned on 10x10 board randomly 
    # only 1 boat in each position
    # inputs -->
    #           outputs --> array “board with boat”

    board_count = np.count_nonzero(board== 'O')

    while board_count != 4:
        x = random.randint(0,9)
        y = random.randint(0,9)
        if board[x,y] == 'O':
            continue
        else:
            board[x,y] = 'O'
            board_count += 1

    while board_count != 10:
        boat_size = 2
        x = random.randint(0,9)
        y = random.randint(0,9)
        dir = random.choice(['N','E','S','W'])
        if dir == 'N' and (x - (boat_size-1)) < - (len(board)):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x - (boat_size-1) : x+1, y] = 'O'
                board_count += 2
        elif dir == 'E' and (y + (boat_size)) < len(board):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x, y: y + (boat_size)] = 'O'
                board_count += 2
        elif dir == 'S' and (x + (boat_size)) < len(board):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x: x + (boat_size), y] = 'O'
                board_count += 2
        elif dir == 'W' and (y - (boat_size-1)) < -len(board):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x, y-(boat_size-1): y+1] = 'O'
                board_count += 2

    while board_count != 16:
        boat_size = 3
        x = random.randint(0,9)
        y = random.randint(0,9)
        dir = random.choice(['N','E','S','W'])
        if dir == 'N' and (x - (boat_size-1)) < - (len(board)):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x - (boat_size-1) : x+1, y] = 'O'
                board_count += 3
        elif dir == 'E' and (y + (boat_size)) < len(board):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x, y: y + (boat_size)] = 'O'
                board_count += 3
        elif dir == 'S' and (x + (boat_size)) < len(board):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x: x + (boat_size), y] = 'O'
                board_count += 3
        elif dir == 'W' and (y - (boat_size-1)) < -len(board):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x, y-(boat_size-1): y+1] = 'O'
                board_count += 3

    while board_count != 20:
        boat_size = 4
        x = random.randint(0,9)
        y = random.randint(0,9)
        dir = random.choice(['N','E','S','W'])
        if dir == 'N' and (x - (boat_size-1)) < - (len(board)):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x - (boat_size-1) : x+1, y] = 'O'
                board_count += 4
        elif dir == 'E' and (y + (boat_size)) < len(board):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x, y: y + (boat_size)] = 'O'
                board_count += 4
        elif dir == 'S' and (x + (boat_size)) < len(board):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x: x + (boat_size), y] = 'O'
                board_count += 4
        elif dir == 'W' and (y - (boat_size-1)) < -len(board):
            if is_posible(board, boat_size, dir, board_count, x, y) == True:
                board[x, y-(boat_size-1): y+1] = 'O'
                board_count += 4
        
    return board

###############################################################################################################################################
# CONDITIONAL FUNCTIONS
###############################################################################################################################################

 def is_posible(tablero_ordena, boat_size, dir, board_count, x,y):
   
    # funcion que se asegura de que no haya ya un barco donde se va a posicionar el barco nuevo 
    # segun sus coordinadas y la direccion 

    # input --> tablero_ordena = array 
    #           boat_size = int
    #           dir = str
    #           coordinadas = int(tupla)
    #                                   output --> booleano : True or False             
    import numpy as np
    aux = []
    
    # NORTE
    if dir.lower() == 'n' or dir.lower() == 'north':
        aux = tablero_ordena.copy()
        aux[x - (boat_size-1) : x+1, y]  = 'O'
    if np.count_nonzero(aux == 'O') == (board_count + boat_size):
        return True 
    # ESTE
    if dir.lower() == 'e' or dir.lower() == 'east':
        aux = tablero_ordena.copy()
        aux[x, y: y + (boat_size)]  = 'O'
        if np.count_nonzero(aux == 'O') == (board_count + boat_size):
            return True 
    # SUR
    if dir.lower() == 's' or dir.lower() == 'south':
        aux = tablero_ordena.copy()
        aux[x: x + (boat_size), y] = 'O'
        if np.count_nonzero(aux == 'O') == (board_count + boat_size):
            return True 
    # OESTE 
    if dir.lower() == 'w' or dir.lower() == 'west':
        aux = tablero_ordena.copy()
        aux[x, y-(boat_size-1): y+1]  = 'O'
        if np.count_nonzero(aux == 'O') == (board_count + boat_size):
            return True 

def is_direction(dir):
    return type(dir) == str and ( dir.lower() == 'n' or dir.lower() == 's' or dir.lower() == 'e' or dir.lower() == 'w' or dir.lower() == 'north' or dir.lower() == 'south' or dir.lower() == 'east' or dir.lower() == 'west')

