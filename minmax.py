from board import check_winner
from utils import result, get_actions, utility, AI, HUMAN

def minimax(board, is_maximizing, count):
    winner = check_winner(board)
    if winner:
        return utility(winner), None, count + 1

    best_move = None
    if is_maximizing:
        best = float('-inf')
        for action in get_actions(board):
            new_board = result(board, action, AI)
            val, _, count = minimax(new_board, False, count)
            if val > best:
                best = val
                best_move = action
        return best, best_move, count + 1
    else:
        best = float('inf')
        for action in get_actions(board):
            new_board = result(board, action, HUMAN)
            val, _, count = minimax(new_board, True, count)
            if val < best:
                best = val
                best_move = action
        return best, best_move, count + 1
