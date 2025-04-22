from board import create_board, print_board, check_winner
from utils import HUMAN, AI, result
from minmax import minimax
from alphabeta import alpha_beta
from compare import compare_algorithms

def human_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if board[row][col] == ' ':
                return (row, col)
            else:
                print("Cell already taken. Try again.")
        except:
            print("Invalid input. Enter numbers 0-2.")

def choose_mode():
    print("\nChoose Mode:")
    print("1. Play Human vs AI")
    print("2. Compare Minimax vs Alpha-Beta")
    return input("Enter 1 or 2: ")

def choose_ai_strategy():
    print("\nChoose AI Strategy:")
    print("1. Minimax")
    print("2. Alpha-Beta Pruning")
    return input("Enter 1 or 2: ")

def play_game(ai_strategy):
    board = create_board()
    print_board(board)
    while True:
        move = human_move(board)
        board = result(board, move, HUMAN)
        print_board(board)
        if check_winner(board):
            break

        print("AI is thinking...")
        if ai_strategy == '1':
            _, ai_move, _ = minimax(board, True, 0)
        else:
            _, ai_move, _ = alpha_beta(board, True, float('-inf'), float('inf'), 0)

        board = result(board, ai_move, AI)
        print_board(board)
        if check_winner(board):
            break

    winner = check_winner(board)
    if winner == 'Draw':
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

if __name__ == "__main__":
    mode = choose_mode()
    if mode == '1':
        strategy = choose_ai_strategy()
        play_game(strategy)
    elif mode == '2':
        test_board = [
            ['X', 'O', ' '],
            [' ', 'X', ' '],
            [' ', ' ', 'O']
        ]
        compare_algorithms(test_board)
    else:
        print("Invalid choice. Exiting.")
