from random import randint
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


def player_choice():

    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9): '))
    
    return position


def place_marker(board, marker, position):

    board[position] = marker


def replay():
    
    choice = input("Play again? Enter Yes or No: ").upper()

    return choice == 'YES'


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
    
    return board[position] == ' '


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Pick X or O: ').upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return('O', 'X')


def choose_first():
    flip = randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


if __name__ == "__main__":

    print('Welcome to Tic Tac Toe! ')
    
    while True:
        board = [' ']*10
        player1_marker, player2_marker = player_input()
        
        turn = choose_first()
        print(turn + 'will go first! ')
        
        play_game = input('Ready to play? y or n? ')
        
        if play_game == 'y':
            game_on = True
        else:
            game_on = False
        
        while game_on:
            if turn == 'Player 1':
                display_board(board)
                position = player_choice()
                place_marker(board,player1_marker, position)
                
                if win_check(player1_marker, board):
                        display_board(board)
                        print('Player 1 has won! ')
                        game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('Tie Game! ')
                        game_on = False
                    else:
                        turn = 'Player 2'
            else:
                display_board(board)
                position = player_choice()
                place_marker(board,player2_marker, position)
                
                if win_check(player2_marker, board):
                        display_board(board)
                        print('Player 2 has won! ')
                        game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('Tie Game!')
                        game_on = False
                    else:
                        turn = 'Player 1'
        
        
        if not replay():
            break