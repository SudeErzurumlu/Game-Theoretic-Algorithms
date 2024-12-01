# game_theory_algorithm.py

class Game:
    """
    A base class representing a generic two-player zero-sum game.
    In such games, one player's gain is another player's loss.
    """
    def __init__(self, matrix):
        """
        Initializes the game with the given payoff matrix.
        This matrix represents the payoffs for player 1.
        
        Args:
            matrix (list of list): A 2D list representing the payoff matrix for player 1.
                                   Player 2's payoffs are the negative of these values (zero-sum).
        """
        self.matrix = matrix
        self.rows = len(matrix)    # Number of strategies for Player 1
        self.columns = len(matrix[0])  # Number of strategies for Player 2

    def get_payoff(self, row, column):
        """
        Returns the payoff for player 1 given the row (strategy for player 1)
        and column (strategy for player 2) selected.
        
        Args:
            row (int): The row index representing Player 1's strategy.
            column (int): The column index representing Player 2's strategy.
        
        Returns:
            float: The payoff for player 1.
        """
        return self.matrix[row][column]

    def get_opponent_payoff(self, row, column):
        """
        Returns the payoff for player 2, which is the negative of player 1's payoff.
        
        Args:
            row (int): The row index representing Player 1's strategy.
            column (int): The column index representing Player 2's strategy.
        
        Returns:
            float: The payoff for player 2.
        """
        return -self.get_payoff(row, column)


class MinimaxAlgorithm:
    """
    A class to represent and solve the game using the Minimax algorithm.
    The Minimax algorithm is used for zero-sum games, where one player's gain is another player's loss.
    """
    def __init__(self, game):
        """
        Initializes the Minimax algorithm with the given game.
        
        Args:
            game (Game): An instance of the Game class.
        """
        self.game = game

    def minimax(self):
        """
        Implements the Minimax algorithm to find the optimal strategies for both players.
        The algorithm aims to minimize the maximum loss for Player 1, and maximize the minimum gain for Player 2.
        
        Returns:
            tuple: The optimal strategies for Player 1 and Player 2.
        """
        # Player 1's optimal strategy is to minimize the maximum of the payoffs (maximize their own outcome)
        # Player 2's optimal strategy is to maximize the minimum of the payoffs (minimize Player 1's outcome)
        
        # Calculate the minimax strategy for Player 1 (Row Player)
        row_optimal_strategy = []
        for row in range(self.game.rows):
            row_payoffs = [self.game.get_payoff(row, col) for col in range(self.game.columns)]
            row_optimal_strategy.append(min(row_payoffs))
        
        # Calculate the minimax strategy for Player 2 (Column Player)
        column_optimal_strategy = []
        for col in range(self.game.columns):
            col_payoffs = [self.game.get_payoff(row, col) for row in range(self.game.rows)]
            column_optimal_strategy.append(max(col_payoffs))
        
        # Now, we calculate the Nash equilibrium by finding the optimal strategy pair
        # Nash equilibrium: Player 1 chooses the row with the highest minimal payoff
        # Player 2 chooses the column with the lowest maximal payoff
        player_1_strategy = row_optimal_strategy.index(max(row_optimal_strategy))
        player_2_strategy = column_optimal_strategy.index(min(column_optimal_strategy))
        
        return player_1_strategy, player_2_strategy

    def get_payoff_for_strategies(self, player_1_strategy, player_2_strategy):
        """
        Returns the payoff for Player 1 and Player 2 given their chosen strategies.
        
        Args:
            player_1_strategy (int): The strategy (row index) chosen by Player 1.
            player_2_strategy (int): The strategy (column index) chosen by Player 2.
        
        Returns:
            tuple: Payoff for Player 1 and Player 2.
        """
        player_1_payoff = self.game.get_payoff(player_1_strategy, player_2_strategy)
        player_2_payoff = self.game.get_opponent_payoff(player_1_strategy, player_2_strategy)
        
        return player_1_payoff, player_2_payoff


if __name__ == "__main__":
    # Example of usage: a simple 2x2 game matrix for a zero-sum game
    matrix = [
        [3, -1],
        [-2, 4]
    ]
    
    # Initialize the game
    game = Game(matrix)
    
    # Initialize the Minimax algorithm with the game instance
    minimax_algorithm = MinimaxAlgorithm(game)
    
    # Find the optimal strategies using Minimax
    player_1_optimal, player_2_optimal = minimax_algorithm.minimax()
    
    # Get the payoff for the chosen strategies
    player_1_payoff, player_2_payoff = minimax_algorithm.get_payoff_for_strategies(player_1_optimal, player_2_optimal)
    
    # Output the results
    print(f"Optimal strategy for Player 1: {player_1_optimal}")
    print(f"Optimal strategy for Player 2: {player_2_optimal}")
    print(f"Payoff for Player 1: {player_1_payoff}")
    print(f"Payoff for Player 2: {player_2_payoff}")
