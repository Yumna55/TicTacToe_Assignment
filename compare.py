import time
import math
from board import print_board
from utils import result, AI
from minmax import minimax
from alphabeta import alpha_beta

def compare_algorithms(board):
    print_board(board)

    print("=== Minimax Analysis ===")
    start_time = time.time()
    _, move_minimax, nodes_minimax = minimax(board, True, 0)
    end_time = time.time()
    print(f"Minimax chose move: {move_minimax}")
    print(f"Minimax nodes visited: {nodes_minimax}")
    print(f"Minimax time: {end_time - start_time:.4f} seconds")
    board_after_minimax = result(board, move_minimax, AI)
    print_board(board_after_minimax)

    print("=== Alpha-Beta Analysis ===")
    start_time = time.time()
    _, move_ab, nodes_ab = alpha_beta(board, True, -math.inf, math.inf, 0)
    end_time = time.time()
    print(f"Alpha-Beta chose move: {move_ab}")
    print(f"Alpha-Beta nodes visited: {nodes_ab}")
    print(f"Alpha-Beta time: {end_time - start_time:.4f} seconds")
    board_after_ab = result(board, move_ab, AI)
    print_board(board_after_ab)

if __name__ == "__main__":
    test_board = [
        ['X', 'O', ' '],
        [' ', 'X', ' '],
        [' ', ' ', 'O']
    ]
    compare_algorithms(test_board)
