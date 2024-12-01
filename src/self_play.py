# self_play.py

from minimax_algorithm import MinimaxAlgorithm, Game, Node


class SelfPlay:
    """
    A class that simulates self-play for a two-player zero-sum game.
    This class allows the game to be played out with both players using the Minimax algorithm
    to select the optimal move at each turn.
    """

    def __init__(self, game, minimax_algorithm):
        """
        Initializes the SelfPlay simulation with a given game and the Minimax algorithm.
        
        Args:
            game (Game): An instance of the Game class that represents the zero-sum game.
            minimax_algorithm (MinimaxAlgorithm): An instance of the MinimaxAlgorithm to be used for decision-making.
        """
        self.game = game
        self.minimax_algorithm = minimax_algorithm
        self.current_turn = 1  # Player 1 starts

    def play(self):
        """
        Simulates a game between two players using the Minimax algorithm.
        It alternates between players, selecting the optimal move for each player
        based on the Minimax algorithm.
        
        Returns:
            str: The outcome of the game (win/loss/draw).
        """
        # Initialize the game state
        game_state = self.game

        # Loop to play the game until it ends
        while not game_state.is_terminal():
            # Print the current game state (optional)
            print(f"Current game state:\n{game_state}")

            if self.current_turn == 1:
                print("Player 1's turn (Maximizing player)...")
                best_score, best_move = self.minimax_algorithm.minimax(game_state, depth=3, maximizing_player=True)
            else:
                print("Player 2's turn (Minimizing player)...")
                best_score, best_move = self.minimax_algorithm.minimax(game_state, depth=3, maximizing_player=False)

            # Apply the chosen move to the game state
            game_state = game_state.make_move(best_move)
            
            # Alternate between players
            self.current_turn = 2 if self.current_turn == 1 else 1

        # At the end of the game, return the outcome
        return self.get_game_outcome(game_state)

    def get_game_outcome(self, game_state):
        """
        Determines the outcome of the game (win/loss/draw).
        
        Args:
            game_state (GameState): The final game state after the game ends.
        
        Returns:
            str: The outcome of the game ("Player 1 wins", "Player 2 wins", or "Draw").
        """
        if game_state.evaluate() > 0:
            return "Player 1 wins"
        elif game_state.evaluate() < 0:
            return "Player 2 wins"
        else:
            return "Draw"


class GameStateExample(Game):
    """
    An example of a specific game state for a zero-sum game.
    In this example, we use a simple 2x2 game for demonstration purposes.
    """

    def __init__(self):
        # Example matrix: Player 1's payoff matrix for a simple 2x2 game
        matrix = [
            [3, -1],
            [-2, 4]
        ]
        super().__init__(matrix)

    def is_terminal(self):
        """
        Determines if the game has reached a terminal state (end of the game).
        For simplicity, we end the game after a few moves in this example.
        
        Returns:
            bool: True if the game is terminal, False otherwise.
        """
        # For the purpose of this example, the game ends after a few moves
        # This should be replaced with actual game-ending logic
        return False  # To simulate ongoing play in the example.

    def evaluate(self):
        """
        Evaluates the game state and returns the score. Positive values are favorable for Player 1, negative for Player 2.
        In this example, the score will be based on the current state and matrix.
        
        Returns:
            int: The evaluation score for the current game state.
        """
        # The evaluation function could be more complex depending on the game
        return 1 if self.current_player == 1 else -1

    def get_possible_moves(self):
        """
        Generate all possible moves from the current state.
        In this simplified example, just return a fixed list of moves.
        
        Returns:
            list: A list of possible moves.
        """
        return [0, 1]  # Simulating a 2x2 matrix (0: row 1, 1: row 2)

    def make_move(self, move):
        """
        Make the move for the current player and return a new game state.
        
        Args:
            move (int): The move to make.
        
        Returns:
            GameState: A new game state after the move.
        """
        new_state = GameStateExample()
        new_state.current_player = 2 if self.current_player == 1 else 1
        return new_state


if __name__ == "__main__":
    # Create an instance of the game
    game = GameStateExample()

    # Create an instance of the Minimax algorithm
    minimax_algorithm = MinimaxAlgorithm(game)

    # Create the self-play simulation
    self_play_simulation = SelfPlay(game, minimax_algorithm)

    # Start the self-play game and get the outcome
    result = self_play_simulation.play()
    print(f"Game Over: {result}")
