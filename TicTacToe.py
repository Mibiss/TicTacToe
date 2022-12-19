from random import randint
import os


def display_board(board: list) -> None:

    """This is where the game board is displayed"""

    os.system("cls")
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


def player_choice() -> int:

    """The player chooses a position,
    gets checked that the position is avaliable
    and if it is within avaliable range"""

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(
        board=board, position=position
    ):
        position = int(input("Choose a position: (1-9): "))

    return position


def place_marker(board: list, marker: tuple, position: int) -> None:
    """Substitues the blank space with a marker"""
    board[position] = marker


def replay() -> bool:

    """Asks if you want to play again"""

    choice = input("Play again? Enter Yes or No: ").upper()

    return choice == "YES"


def win_check(marker: tuple, board: list) -> bool:

    """Looping through win condition,
    to check if anyone won the game"""

    wincon = [
        [board[1], board[2], board[3]],
        [board[4], board[5], board[6]],
        [board[7], board[8], board[9]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[3], board[6], board[9]],
        [board[1], board[5], board[9]],
        [board[7], board[5], board[3]],
    ]

    for i in wincon:
        if i[0] == i[1] == i[2] == marker:
            return True


def space_check(board: list, position: int) -> bool:

    """Checks if position is empty or taken"""

    return board[position] == " "


def full_board_check(board: list) -> bool:

    """Checks if the board is full"""

    for i in range(1, 10):
        if space_check(board=board, position=i):
            return False

    return True


def player_input() -> tuple:

    """Chooses what marker Player 1 is"""

    marker = ""

    while marker != "X" and marker != "O":
        marker = input("Pick X or O: ").upper()

        if marker == "X":
            return ("X", "O")
        else:
            return ("O", "X")


def choose_first() -> str:

    """Randomly picks a Player"""

    flip = randint(0, 1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


if __name__ == "__main__":

    print("Welcome to Tic Tac Toe! ")

    while True:

        # Starting board and picking player marker
        board = [" "] * 10
        player1_marker, player2_marker = player_input()

        # Picking who goes first
        turn = choose_first()
        print(turn + "will go first! ")

        # Check to start game
        play_game = input("Ready to play? y or n? ")

        if play_game == "y":
            game_on = True
        else:
            game_on = False

        while game_on:

            # Turn of the Player 1
            if turn == "Player 1":

                # Displaying board
                display_board(board=board)

                # Picking position and placing the marker
                position = player_choice()
                place_marker(board=board, marker=player1_marker, position=position)

                # Checking if Player 1 did a winning move
                if win_check(marker=player1_marker, board=board):
                    display_board(board=board)
                    print("Player 1 has won! ")
                    game_on = False

                # Checking if the game is a Tie
                else:
                    if full_board_check(board=board):
                        display_board(board=board)
                        print("Tie Game! ")
                        game_on = False

                    else:
                        turn = "Player 2"

            # Turn of the Player 2
            else:
                # Displaying board
                display_board(board=board)

                # Picking position and placing the marker
                position = player_choice()
                place_marker(board=board, marker=player2_marker, position=position)

                # Checking if Player 1 did a winning move
                if win_check(marker=player2_marker, moard=board):
                    display_board(board=board)
                    print("Player 2 has won! ")
                    game_on = False

                # Checking if the game is a Tie
                else:
                    if full_board_check(board=board):
                        display_board(board=board)
                        print("Tie Game!")
                        game_on = False

                    else:
                        turn = "Player 1"

        # Asking to play again
        if not replay():
            break
