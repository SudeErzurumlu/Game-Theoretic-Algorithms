import unittest
from minimax_algorithm import MinimaxAlgorithm

class TestMinimaxAlgorithm(unittest.TestCase):
    
    def test_initialization(self):
        # Test if the MinimaxAlgorithm is initialized correctly
        minimax = MinimaxAlgorithm(depth=3)
        self.assertIsInstance(minimax, MinimaxAlgorithm)
        self.assertEqual(minimax.depth, 3)

    def test_minimax_evaluation(self):
        # Test if the evaluation function works correctly (assuming a specific evaluation function)
        minimax = MinimaxAlgorithm(depth=3)
        test_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Sample state
        evaluation = minimax.evaluate_state(test_state, maximizing_player=True)
        self.assertIsInstance(evaluation, int)
        self.assertGreaterEqual(evaluation, -1)  # Assuming evaluation is non-negative for a valid state

    def test_minimax_algorithm_selection(self):
        # Test if Minimax selects the correct move (mock evaluation)
        minimax = MinimaxAlgorithm(depth=3)
        test_state = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]  # Sample Tic-Tac-Toe state
        move = minimax.minimax(test_state, depth=3, maximizing_player=True)
        self.assertIn(move, [(0, 2), (2, 0)])  # Assuming these are valid optimal moves based on the state

    def test_alpha_beta_pruning(self):
        # Test if alpha-beta pruning is working correctly (mock test)
        minimax = MinimaxAlgorithm(depth=3)
        test_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Sample state
        alpha = -float('inf')
        beta = float('inf')
        optimal_move = minimax.alpha_beta_pruning(test_state, depth=3, alpha=alpha, beta=beta, maximizing_player=True)
        self.assertIsInstance(optimal_move, tuple)  # Alpha-Beta pruning should return a valid move

    def test_terminal_state(self):
        # Test if terminal state detection works (mock game over)
        minimax = MinimaxAlgorithm(depth=3)
        terminal_state = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]  # Win condition
        is_terminal = minimax.is_terminal_state(terminal_state)
        self.assertTrue(is_terminal)

if __name__ == "__main__":
    unittest.main()
