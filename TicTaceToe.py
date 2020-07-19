#Daoud Ali Simple TicTacToe Python Game

#Create function to display game board

def display_board(board):

    print(board[1] +" | "+ board[2] + " | " + board[3])
    print("---------")
    print(board[4] +" | "+ board[5] + " | " + board[6])
    print("---------")
    print(board[7] +" | "+ board[8] + " | " + board[9])

#Create function to let player1 choose "X" or "O"
def player_choice():

    choice1 = ""

    while choice1 != "X" and choice1 != "O":                    # Keep asking for marker choice until "X" or "O" received
        choice1 = input("Please choose either 'X' or 'O': ") 

    player1 = choice1                                           # Set player1 marker as the chosen marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return(player1,player2)


#Create function to place markers ("X" and "O") on the board so players can play 
def place_marker(board, marker, position):

    board[position] = marker


#Create a function to check a board and a marker to see if anyone has won
def win_check(board, marker):

    if (board[1] == marker and board[2] == marker and board[3] == marker):
        return True
    elif (board[4] == marker and board[5] == marker and board[6] == marker):
        return True 
    elif (board[7] == marker and board[8] == marker and board[9] == marker):
        return True 
    elif (board[1] == marker and board[5] == marker and board[9] == marker): #Right Diagonal 
        return True
    elif (board[3] == marker and board[5] == marker and board[7] == marker): #Left Diagonal 
        return True
    elif (board[3] == marker and board[6] == marker and board[9] == marker):
        return True 
    elif (board[2] == marker and board[5] == marker and board[8] == marker):
        return True
    elif (board[1] == marker and board[4] == marker and board[7] == marker):
        return True 
    else:
        return False

#Create function that randomly decides which player goes first
import random

def choose_first():

    x = random.randint(1,10)            # Choose a number between 1 and 10 inclusive (5 odd, 5 even numbers)
    if x % 2 == 0:                      # If random num even then player 1 goes first
        print("Player 1 goes first!")
        return("Player 1")
    else:
        print("Player 2 goes first!")
        return("Player 2")

#Function to check if space is free on board
def space_check(board, position):

    if board[position] != " ":
        print("Sorry! The chosen position is not vacant.")
        return False
    else:
        return True

#Funciton to check if board is full
def full_board_check(board):

    full = True                 # Assume board is full
    for pos in range(1,10):
        if board[pos] == " ":   # If vacant position found, set full equal to False
            full = False
    return full

#Function to let players choose position on board
def choose_pos(board):

    pos = 0
    while pos not in range(1,10) or not space_check(board,pos):
        pos  = int(input("Please choose a vacant position between 1 to 9: "))
    return pos

#Replay Game function
def replay():

    return input('Play again? Enter Yes or No: ').lower().startswith('y')

#Game Logic 
print("Let's Play Tic-Tac-Toe! By Daoud Ali.")

while True:

    gameboard = [" "," "," "," "," "," "," "," "," "," "]       #Create empty board
    marker1, marker2 = player_choice()                          #Choose Player Markers
    turn = choose_first()                                       #Choose first player
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(gameboard)
            position = choose_pos(gameboard)
            place_marker(gameboard, marker1, position)

            if win_check(gameboard, marker1):
                display_board(gameboard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(gameboard):
                    display_board(gameboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            
            
            display_board(gameboard)
            position = choose_pos(gameboard)
            place_marker(gameboard, marker2, position)

            if win_check(gameboard, marker2):
                display_board(gameboard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(gameboard):
                    display_board(gameboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break