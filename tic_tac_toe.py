def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.', ' | ', '.', ' | ', '.'],['.', ' | ', '.', ' | ', '.'],['.', ' | ', '.', ' | ', '.']]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    player_move = input()
    row, col = 0, 0

    if player_move == "A1":
        row, col = 1, 1
    if player_move == "A2":
        row, col = 1, 2
    if player_move == "A3":
        row, col = 1, 3
    if player_move == "B1":
        row, col = 2, 1
    if player_move == "B2":
        row, col = 2, 2
    if player_move == "B3":
        row, col = 2, 3
    if player_move == "C1":
        row, col = 3, 1
    if player_move == "C2":
        row, col = 3, 2
    if player_move == "C3":
        row, col = 3, 3

    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if row == 1 and col == 1:
        pass
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print(" 1     2     3")
    print(str(board[0]).replace("[", " ").replace("]", "").replace("'", "").replace(",","" ))
    print("----+-----+----")
    print(str(board[1]).replace("[", " ").replace("]", "").replace("'", "").replace(",","" ))
    print("----+-----+----")
    print(str(board[2]).replace("[", " ").replace("]", "").replace("'", "").replace(",","" ))
    


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
