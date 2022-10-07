from random import choice
from IPython.display import clear_output


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


def replacement_choice(board, marker, position):
   
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


def win_check(marker, board):
    wincon = [[board[1],board[2],board[3]],
              [board[4],board[5],board[6]],  
              [board[7],board[8],board[9]],
              [board[1],board[4],board[7]],
              [board[2],board[5],board[8]],
              [board[3],board[6],board[9]],  
              [board[1],board[5],board[9]],
              [board[7],board[5],board[3]],]

    for i in wincon:
        if i[0] == i[1] == i[2] == marker:
            return True
        

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
    if n == 9:
        return True


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Pick X or O: ').upper()

        p1 = marker

        if p1 == 'X':
            p2 = 'O'
        else:
            p2 = 'X'

    return (p1, p2)


def choose_first(p1,p2):
    lst = [p1,p2]
    first = choice(lst)
    lst.remove(first)
    second = lst[0]

    return first,second


game_on = True
board = [' ']*10

players = player_input()
print(f"Player1 = {players[0]}")
print(f"Player2 = {players[1]}")

first_player = choose_first(players[0], players[1])
second_player = 

print(first_player + " goes first!")

display_board(board=board)

if __name__ == "__main__":

    while game_on:



        if win_check(marker=p1,board=board) == True:
            print("Player1 won!")
            break
        elif win_check(marker=p2,board=board) == True:
            print("Player2 won!")
            break
        elif full_board_check(board=board) == True:
            print("The game is a tie!")
        
        

        pos = position_choice()
        
        space_check(board=board, position=pos)

        board = replacement_choice(board=board,marker=first_player,position=pos)


        display_board(board=board)
        clear_output()