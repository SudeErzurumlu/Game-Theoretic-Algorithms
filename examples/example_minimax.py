from minimax_algorithm import MinimaxAlgorithm

def example_minimax():
    # Initialize the Minimax algorithm with a specified depth for the search
    minimax = MinimaxAlgorithm(depth=3)

    # Sample game state (e.g., Tic-Tac-Toe board) where '1' is player 1, '0' is player 2, and '' represents an empty cell
    test_state = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    # Display the initial game state
    print("Initial Game State:")
    for row in test_state:
        print(row)

    # Use Minimax to determine the best move for player 1 (maximizing player)
    best_move = minimax.minimax(test_state, depth=3, maximizing_player=True)

    # Print the selected move (coordinates for Tic-Tac-Toe)
    print(f"Best Move for Player 1: {best_move}")

    # Test the evaluation function
    evaluation = minimax.evaluate_state(test_state, maximizing_player=True)
    print(f"Evaluation of Current State: {evaluation}")

    # Test alpha-beta pruning (with mock alpha and beta values)
    alpha = -float('inf')
    beta = float('inf')
    optimal_move = minimax.alpha_beta_pruning(test_state, depth=3, alpha=alpha, beta=beta, maximizing_player=True)
    print(f"Optimal Move (Alpha-Beta Pruning): {optimal_move}")

if __name__ == "__main__":
    example_minimax()
