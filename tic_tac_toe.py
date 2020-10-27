import os


def init_board():
    """Returns an empty 3-by-3 board (with .)."""

    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    return board

def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    
    row, col = (0, 0)
    correct_coordinates = False

    while not correct_coordinates:
    
        player_move = input("Give your coordinates: ")

        if player_move == "A1" or player_move == "a1" and board[0][0] == ".":
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

    row, col = 0, 0
    return row, col


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


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner != 1:
        print(f"Congrats {winner} is the champion!")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("It's a tie")
    


def tictactoe_game(mode='HUMAN-HUMAN'):

    board = init_board()
    player = "0"
    
    playing = True
    while playing:
        os.system('cls' if os.name == 'nt' else 'clear')


        if player == "0":
            player = "X"
        else:
            player = "0"
        
        # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
        print_board(board)
        row, col = get_move(board, player)
        mark(board, player, row, col)

        if has_won(board, player) == True:
            winner = player
            playing = False
            print_result(winner)

        if is_full(board) == True:
            winner = 1
            playing = False
            print_result(winner)

    


        


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
