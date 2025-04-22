from board import check_winner
from utils import result, get_actions, utility, AI, HUMAN

def alpha_beta(board, is_maximizing, alpha, beta, count):
    winner = check_winner(board)
    if winner:
        return utility(winner), None, count + 1

    best_move = None
    if is_maximizing:
        best = float('-inf')
        for action in get_actions(board):
            new_board = result(board, action, AI)
            val, _, count = alpha_beta(new_board, False, alpha, beta, count)
            if val > best:
                best = val
                best_move = action
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best, best_move, count + 1
    else:
        best = float('inf')
        for action in get_actions(board):
            new_board = result(board, action, HUMAN)
            val, _, count = alpha_beta(new_board, True, alpha, beta, count)
            if val < best:
                best = val
                best_move = action
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best, best_move, count + 1
