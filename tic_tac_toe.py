def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.', ' | ', '.', ' | ', '.'],['.', ' | ', '.', ' | ', '.'],['.', ' | ', '.', ' | ', '.']]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    
    row, col = (0, 0)
    correct_coordinates = False

    while not correct_coordinates:
        
        player_move = input("Give your coordinates: ")

        if player_move == "A1" or player_move == "a1" and board[0][0] == ".":
            row, col = (1, 1)

        elif player_move == "A2" or player_move == "a2" and board[0][2] == ".":
            row, col = (1, 2)

        elif player_move == "A3" or player_move == "a3" and board[0][4] == ".":
            row, col = (1, 3)

        elif player_move == "B1" or player_move == "b1" and board[1][0] == ".":
            row, col = (2, 1)

        elif player_move == "B2" or player_move == "b2" and board[1][2] == ".":
            row, col = (2, 2)

        elif player_move == "B3" or player_move == "b3" and board[1][4] == ".":
            row, col = (2, 3)

        elif player_move == "C1" or player_move == "c1" and board[2][0] == ".":
            row, col = (3, 1)

        elif player_move == "C2" or player_move == "c2" and board[2][2] == ".":
            row, col = (3, 2)

        elif player_move == "C3" or player_move == "c3" and board[2][4] == ".":
            row, col = (3, 3)
            
        else:
            continue

        correct_coordinates = True
        
    return(row, col)


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""

    player = "X"
    
    if row == 1 and col == 1:
        board[0][0] = player
    elif row == 1 and col == 2:
        board[0][2] = player
    elif row == 1 and col == 3:
        board[0][4] = player
    elif row == 2 and col == 1:
        board[1][0] = player
    elif row == 2 and col == 2:
        board[1][2] = player
    elif row == 2 and col == 3:
        board[1][4] = player
    elif row == 3 and col == 1:
        board[2][0] = player
    elif row == 3 and col == 2:
        board[2][2] = player
    elif row == 3 and col == 3:
        board[2][4] = player
    
    if player == "X":
        player = "0"
    else:
        player = "X"
    
    return board


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print("   1     2     3")
    print("A " + str(board[0]).replace("[", " ").replace("]", "").replace("'", "").replace(",","" ))
    print("  ----+-----+----")
    print("B " + str(board[1]).replace("[", " ").replace("]", "").replace("'", "").replace(",","" ))
    print("  ----+-----+----")
    print("C " + str(board[2]).replace("[", " ").replace("]", "").replace("'", "").replace(",","" ))
    


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
