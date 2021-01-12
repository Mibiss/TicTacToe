
def display_game(g_listh,g_listv,board):
    print("Here is the current list: ")
    print(g_listv)
    print(' ' + board[7] + ' | '+ board[8] + ' | ' + board[9])
    print(g_listv)
    print(g_listh)
    print(g_listv)
    print(' ' + board[4] + ' | '+ board[5] + ' | ' + board[6])
    print(g_listv)
    print(g_listh)
    print(g_listv)
    print(' ' + board[1] + ' | '+ board[2] + ' | ' + board[3])
    print(g_listv)


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
                whithin_range = True
            else:
                print("Sorry, the number is out of acceptable range(1-9)")
                within_range = False

    return int(choice)
position_choice()
def replacement_choice(game_list, position):
    pass


def gameon_choice():
    pass

game_on = True
g_listh = "-----------"
g_listv = "   |   |"
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
'''
while game_on:
    # display_game(g_listh,g_listv,board)
    position_choice()
    break
'''
