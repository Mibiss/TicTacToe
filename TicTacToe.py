from IPython.display import clear_output


def display_board(board):
    clear_output()
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
            clear_output()
            print("Sorry that is not a digit!")
        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_values:
                within_range = True
            else:
                clear_output()
                print("Sorry, the number is out of acceptable range(1-9)")
                within_range = False

    return int(choice)


def replacement_choice(board, position):

    user_placement = input("Type the position: ")
    
    board[position] = user_placement
    
    return board


def gameon_choice():
    choice = 'wrong'

    while choice not in ['y','n']:

        choice = input("Would you like to keep playing? y or n ")
        if choice not in ['y','n']:
            clear_output()

            print('Sorry, I didnt understand. Make sure you choose y or n.')
    if choice == "y":
        return True
    else:
        return False

def win_check():
    pass

def space_check():
    pass

def full_board_check():
    pass

def player_input():
    pass




game_on = True
board = [' ']*10

while game_on:
    clear_output()
    display_board(board)
    position = position_choice()
    board = replacement_choice(board,position)
    clear_output()
    display_board(board)
    game_on = gameon_choice()