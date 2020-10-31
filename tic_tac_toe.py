import os
import random
import time

def welcome_menu():
    print("Welcome to TICTACTOE game")
    print()
    print("1. HUMAN-HUMAN")
    print("2. HUMAN-AI")
    print("3. AI-AI")
    print()

def init_board():
    """Returns an empty 3-by-3 board (with .)."""

    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    return board

def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    
    row, col = (0, 0)
    correct_coordinates = False

    while not correct_coordinates:
    
        player_move = input(f"Player {player} turn: ").lower()
        
        if player_move == "quit":
            row, col = (0, 0)
        elif player_move == "A1" or player_move == "a1" and board[0][0] == ".":
            row, col = (1, 1)
        elif player_move == "A2" or player_move == "a2" and board[0][1] == ".":
            row, col = (1, 2)
        elif player_move == "A3" or player_move == "a3" and board[0][2] == ".":
            row, col = (1, 3)
        elif player_move == "B1" or player_move == "b1" and board[1][0] == ".":
            row, col = (2, 1)
        elif player_move == "B2" or player_move == "b2" and board[1][1] == ".":
            row, col = (2, 2)
        elif player_move == "B3" or player_move == "b3" and board[1][2] == ".":
            row, col = (2, 3)
        elif player_move == "C1" or player_move == "c1" and board[2][0] == ".":
            row, col = (3, 1)
        elif player_move == "C2" or player_move == "c2" and board[2][1] == ".":
            row, col = (3, 2)
        elif player_move == "C3" or player_move == "c3" and board[2][2] == ".":
            row, col = (3, 3)
        else:
            continue

        correct_coordinates = True
    return row, col

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""

    row, col = (0, 0)

    possible_move_list = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == ".":
                row = x + 1
                col = y + 1
                possible_move_list.append((row, col))

    row, col = random.choice(possible_move_list)

    return row, col

#Tutaj bym dodał tudny AI żeby było można w opcjach wybrać gre z łatwym albo trudnym AI
# def get_hard_ai_move(board, player):
#     """Returns the coordinates of a valid move for player on board."""


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""

    if row == 1 and col == 1:
        board[0][0] = player
    elif row == 1 and col == 2:
        board[0][1] = player
    elif row == 1 and col == 3:
        board[0][2] = player
    elif row == 2 and col == 1:
        board[1][0] = player
    elif row == 2 and col == 2:
        board[1][1] = player
    elif row == 2 and col == 3:
        board[1][2] = player
    elif row == 3 and col == 1:
        board[2][0] = player
    elif row == 3 and col == 2:
        board[2][1] = player
    elif row == 3 and col == 3:
        board[2][2] = player   

    return mark


def has_won(board, player):
    """Returns True if player has won the game."""

    player1 = "X"
    player2 = "0"
    has_won = False

    if board[0][0] == board[0][1] == board[0][2] == player1 or \
        board[1][0] == board[1][1] == board[1][2] == player1 or \
        board[2][0] == board[2][1] == board[2][2] == player1 or \
        board[0][0] == board[1][0] == board[2][0] == player1 or \
        board[0][1] == board[1][1] == board[2][1] == player1 or \
        board[0][2] == board[1][2] == board[2][2] == player1 or \
        board[0][0] == board[1][1] == board[2][2] == player1 or \
        board[2][0] == board[1][1] == board[0][2] == player1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(board)
        has_won = True
    elif board[0][0] == board[0][1] == board[0][2] == player2 or \
        board[1][0] == board[1][1] == board[1][2] == player2 or \
        board[2][0] == board[2][1] == board[2][2] == player2 or \
        board[0][0] == board[1][0] == board[2][0] == player2 or \
        board[0][1] == board[1][1] == board[2][1] == player2 or \
        board[0][2] == board[1][2] == board[2][2] == player2 or \
        board[0][0] == board[1][1] == board[2][2] == player2 or \
        board[2][0] == board[1][1] == board[0][2] == player2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(board)
        has_won = True

    
    return has_won
   

    

def is_full(board):
    """Returns True if board is full."""
    is_full = False
    
    if not '.' in board[0] and not '.' in board[1] and not '.' in board[2]:
        is_full = True 

    return is_full

def print_board(board):

    """Prints a 3-by-3 board on the screen with borders."""
    print("  1   2   3")
    print(f'A {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print(" ---+---+---")
    print(f'B {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print(" ---+---+---")
    print(f'C {board[2][0]} | {board[2][1]} | {board[2][2]}')
    print()


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner != 1:
        print(f"Congrats {winner} is the champion!")
        print()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("It's a tie")
        print()

def tictactoe_game(mode):

    if mode == 'HUMAN-HUMAN':
        board = init_board()
        player = "0"
        playing = True
        while playing:
            os.system('cls' if os.name == 'nt' else 'clear')

            if player == "0":
                player = "X"
            else:
                player = "0"
            
            print_board(board)
            row, col = get_move(board, player)
            if (row, col) != (0, 0):
                mark(board, player, row, col)

                if has_won(board, player) == True:
                    winner = player
                    playing = False
                    print_result(winner)
                    if input("Do you want to play again? Y or N: ").lower() == "y":
                        main_menu()

                if is_full(board) == True:
                    winner = 1
                    playing = False
                    print_result(winner)
                    if input("Do you want to play again? Y or N: ").lower() == "y":
                        main_menu()
            else:
                playing = False
    elif mode == 'HUMAN-AI':
        board = init_board()
        player = "0"
        playing = True
        while playing:
            os.system('cls' if os.name == 'nt' else 'clear')

            if player == "0":
                player = "X"
            else:
                player = "0"
            
            print_board(board)
            if player == "X":
                row, col = get_move(board, player)
            elif player == "0":
                row, col = get_ai_move(board, player)
                time.sleep(1.8)
            if (row, col) != (0, 0):
                mark(board, player, row, col)

                if has_won(board, player) == True:
                    winner = player
                    playing = False
                    print_result(winner)
                    if input("Do you want to play again? Y or N: ").lower() == "y":
                        main_menu()

                if is_full(board) == True:
                    winner = 1
                    playing = False
                    print_result(winner)
                    if input("Do you want to play again? Y or N: ").lower() == "y":
                        main_menu()
            else:
                playing = False
    elif mode == 'AI-AI':
        board = init_board()
        player = "0"
        playing = True
        while playing:
            os.system('cls' if os.name == 'nt' else 'clear')

            if player == "0":
                player = "X"
            else:
                player = "0"
            
            print_board(board)
            if player == "X":
                row, col = get_ai_move(board, player)
                time.sleep(1.8)
            elif player == "0":
                row, col = get_ai_move(board, player)
                time.sleep(1.8)
            if (row, col) != (0, 0):
                mark(board, player, row, col)

                if has_won(board, player) == True:
                    winner = player
                    playing = False
                    print_result(winner)
                    if input("Do you want to play again? Y or N: ").lower() == "y":
                        main_menu()

                if is_full(board) == True:
                    winner = 1
                    playing = False
                    print_result(winner)
                    if input("Do you want to play again? Y or N: ").lower() == "y":
                        main_menu()
            else:
                playing = False
    


def main_menu():
    game_over = False
    while not game_over:
        os.system('cls' if os.name == 'nt' else 'clear')
        welcome_menu()
        game_mode = input("Choose game mode: ")
        #game_mode = input("Choose game mode:\n 1. HUMAN-HUMAN\n 2. HUMAN-AI\n 3. AI-AI\n ")

        if game_mode == "1":
            tictactoe_game('HUMAN-HUMAN')
            game_over = True
        elif game_mode == "2":
            tictactoe_game('HUMAN-AI')
            game_over = True
        elif game_mode == "3":
            tictactoe_game('AI-AI')
            game_over = True
        else:
            print()
            print("Choose correct option, 1, 2 or 3")
            print()
            time.sleep(3.0)
            continue

if __name__ == '__main__':
    main_menu()
