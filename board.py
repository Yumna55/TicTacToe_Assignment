EMPTY = ' '

def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row))
    print()

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    for row in board:
        if EMPTY in row:
            return None
    return 'Draw'
