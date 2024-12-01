# minimax_algorithm.py

class MinimaxAlgorithm:
    """
    A class to represent and solve a game using the Minimax algorithm.
    The Minimax algorithm is used for zero-sum games where one player's gain is another player's loss.
    This implementation supports two main approaches:
    1. Standard Minimax (Recursive)
    2. Minimax with Iterative Deepening
    """

    def __init__(self, game, depth_limit=None):
        """
        Initializes the Minimax algorithm with the given game and depth limit.
        
        Args:
            game (Game): An instance of the Game class that represents the zero-sum game.
            depth_limit (int, optional): The maximum depth to search in the game tree for iterative deepening. Defaults to None.
        """
        self.game = game
        self.depth_limit = depth_limit

    def minimax(self, node, depth, maximizing_player):
        """
        The recursive Minimax algorithm.
        It computes the best move for a player based on their perspective (maximizing or minimizing their outcome).
        
        Args:
            node (Node): The current game state or node.
            depth (int): The current depth of the search tree.
            maximizing_player (bool): Whether the current player is trying to maximize (True) or minimize (False) their payoff.
        
        Returns:
            int: The best score found for the current player.
            int: The best move associated with the best score.
        """
        if depth == 0 or node.is_terminal():
            return node.evaluate(), node.best_move()

        if maximizing_player:
            best_score = float('-inf')
            best_move = None
            for child in node.get_children():
                score, move = self.minimax(child, depth - 1, False)
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for child in node.get_children():
                score, move = self.minimax(child, depth - 1, True)
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move

    def iterative_deepening(self):
        """
        Implements Iterative Deepening for the Minimax algorithm.
        This allows us to search deeper in the game tree over time, providing better moves as more time is available.
        
        Returns:
            int: The best score found after the search.
            int: The best move associated with the best score.
        """
        best_move = None
        for depth in range(1, self.depth_limit + 1):
            print(f"Searching at depth {depth}...")
            best_score, best_move = self.minimax(self.game.root, depth, True)
        return best_score, best_move


class Node:
    """
    A class representing a node in the game tree. Each node corresponds to a game state
    and has information about the state, its possible moves, and the associated payoffs.
    """

    def __init__(self, state, parent=None):
        """
        Initializes the node with the game state and its parent node.
        
        Args:
            state (GameState): The current state of the game.
            parent (Node, optional): The parent node. Defaults to None.
        """
        self.state = state
        self.parent = parent
        self.children = []
        self.best_move = None

    def is_terminal(self):
        """
        Check if the current node represents a terminal state (a win, loss, or draw).
        
        Returns:
            bool: True if the node is terminal, False otherwise.
        """
        return self.state.is_terminal()

    def evaluate(self):
        """
        Evaluate the current game state and return the payoff (or utility).
        
        Returns:
            int: The evaluation score for the state.
        """
        return self.state.evaluate()

    def get_children(self):
        """
        Generate and return all possible child nodes from the current state.
        
        Returns:
            list of Node: The list of child nodes.
        """
        if not self.children:  # Generate children only if not already generated
            moves = self.state.get_possible_moves()
            for move in moves:
                child_state = self.state.make_move(move)
                child_node = Node(child_state, parent=self)
                self.children.append(child_node)
        return self.children

    def best_move(self):
        """
        Get the best move associated with the current state.
        
        Returns:
            int: The best move for the current state.
        """
        return self.best_move


class GameState:
    """
    A class representing the state of the game. This is an abstract class and should be extended
    to represent specific game states (e.g., Tic-Tac-Toe, Chess).
    """
    def __init__(self):
        self.current_player = 1

    def is_terminal(self):
        """
        Check if the game is over (win, loss, or draw).
        Should be implemented in the subclass.
        
        Returns:
            bool: True if the game is over, False otherwise.
        """
        raise NotImplementedError

    def evaluate(self):
        """
        Evaluate the state and return a numeric value representing the outcome (e.g., +1 for a win, -1 for a loss).
        Should be implemented in the subclass.
        
        Returns:
            int: The evaluation score for the current state.
        """
        raise NotImplementedError

    def get_possible_moves(self):
        """
        Generate all possible moves from the current state.
        Should be implemented in the subclass.
        
        Returns:
            list: A list of possible moves.
        """
        raise NotImplementedError

    def make_move(self, move):
        """
        Apply the move and return the new game state.
        Should be implemented in the subclass.
        
        Args:
            move: The move to apply.
        
        Returns:
            GameState: The new game state after the move.
        """
        raise NotImplementedError
