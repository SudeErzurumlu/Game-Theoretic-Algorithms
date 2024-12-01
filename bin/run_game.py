import argparse
from game_theory_algorithm import GameTheoryAlgorithm

def run_game():
    # Set up argument parser for command line interface
    parser = argparse.ArgumentParser(description="Run the Game Theory-based Game with Minimax Algorithm.")
    parser.add_argument(
        "--play", 
        action="store_true", 
        help="Flag to start and play a new game."
    )
    parser.add_argument(
        "--depth", 
        type=int, 
        default=3, 
        help="Set the depth for the Minimax algorithm (default is 3)."
    )
    parser.add_argument(
        "--visualize", 
        action="store_true", 
        help="Flag to visualize the game state after each move."
    )

    args = parser.parse_args()

    # Initialize the game with the given depth for the Minimax algorithm
    game_algorithm = GameTheoryAlgorithm(minimax_depth=args.depth)

    # Start the game if the --play flag is passed
    if args.play:
        print("Starting the game with depth:", args.depth)
        print("Initial Game State:")
        initial_state = game_algorithm.get_initial_game_state()
        game_algorithm.print_game_state(initial_state)

        game_result = game_algorithm.play_game(visualize=args.visualize)
        print(f"Game Result: {game_result}")
    else:
        print("Run the game with the --play flag to start a new game.")

if __name__ == "__main__":
    run_game()
