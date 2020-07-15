#Daoud Ali Simple TicTacToe Python Game

#Create function to display game board
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1] +" | "+ board[2] + " | " + board[3])
    print("---------")
    print(board[4] +" | "+ board[5] + " | " + board[6])
    print("---------")
    print(board[7] +" | "+ board[8] + " | " + board[9])

#Create function to let player1 choose "X" or "O"
def player_choice():

    choice1 = ""

    while choice1 != "X" and choice1 != "O": #Keep asking for marker choice until "X" or "O" received
        choice1 = input("Please choose either 'X' or 'O': ") 

    player1 = choice1 #Set player1 marker as the chosen marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return(player1,player2)

player1_marker, player2_marker = player_choice()