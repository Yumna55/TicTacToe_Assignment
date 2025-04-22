import copy

HUMAN = 'O'
AI = 'X'
EMPTY = ' '

def get_actions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def result(board, action, player):
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player
    return new_board

def utility(winner):
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    else:
        return 0
