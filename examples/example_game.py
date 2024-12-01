from game_theory_algorithm import GameTheoryAlgorithm

def example_game():
    # Initialize the game theory algorithm
    game_algorithm = GameTheoryAlgorithm()

    # Start a game simulation
    print("Starting a new game...")

    # Get the initial state of the game
    initial_state = game_algorithm.get_initial_game_state()

    # Print the initial game state
    print("Initial Game State:")
    game_algorithm.print_game_state(initial_state)

    # Play the game by selecting moves using the game theory algorithm
    game_result = game_algorithm.play_game()

    # Print the result of the game
    print(f"Game Result: {game_result}")

if __name__ == "__main__":
    example_game()
