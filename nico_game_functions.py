
##################################################################################################################################
# game turns: computer and user

def turns(start, computer_shots, user_board, computer_hits, user_shots, computer_board, user_hits):
    
    import random
    import time 

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
