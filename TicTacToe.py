
from random import randint


def display_board(board):

    print("Here is the current game board: ")
    print("     |     |")
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9])
    print("     |     |")
    print("-----------------")
    print("     |     |")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6])
    print("     |     |")
    print("-----------------")
    print("     |     |")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3])
    print("     |     |")


def position_choice():

    choice = 'WRONG'
    acceptable_values = range(1,10)
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input("Please enter a number between (1-9): ")

        # DIGIT CHECK
        if choice.isdigit() == False:

            print("Sorry that is not a digit!")
        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_values:
                within_range = True
            else:

                print("Sorry, the number is out of acceptable range(1-9)")
                within_range = False

    return int(choice)


def place_marker(board, marker, position):
   
    board[position] = marker

    return board


def replay():
    choice = 'wrong'

    while choice not in ['y','n']:

        choice = input("Would you like to keep playing? y or n ")

        if choice not in ['y','n']:

            print('Sorry, I didnt understand. Make sure you choose y or n.')

    if choice == "y":
        return True
    else:
        return False


def win_check(marker):
    wincon = [[board[1],board[2],board[3]],
              [board[4],board[5],board[6]],  
              [board[7],board[8],board[9]],
              [board[1],board[4],board[7]],
              [board[2],board[5],board[8]],
              [board[3],board[6],board[9]],  
              [board[1],board[5],board[9]],
              [board[7],board[5],board[3]],]
    
    a = 0

    for combination in wincon:
        for i in combination:
            if combination[i]==marker:
                a += 1
    if a == 3:
        return True
    else:
        return False


def space_check(board, position):
    mpty = ' '

    if board[position] != mpty:
        print("This spot is already taken, please choose another one. ")
    else:
        return board


def full_board_check(board):
    n = 0
    for i in board:
        if i != ' ':
            n += 1
        else:
            pass
    if n == 9:
        return "Board is full"



def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Pick x or o: ').upper()

        player1 = marker

        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    return (player1, player2)


def choose_first():
    x = randint(0,1)
    if x == 0:
        return "Player1 goes first!"
    else:
        return "Player2 goes first!"

game_on = True
board = [' ']*10

player_input()


"""
while game_on:
    clear_output()
    display_board(board)
    position = position_choice()
    board = replacement_choice(board,position)
    clear_output()
    display_board(board)
    game_on = replay()
"""