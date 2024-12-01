import unittest
from game_theory_algorithm import GameTheoryAlgorithm
from minimax_algorithm import MinimaxAlgorithm

class TestGameTheoryAlgorithm(unittest.TestCase):
    
    def test_initialization(self):
        # Test if the GameTheoryAlgorithm is initialized correctly
        game_algorithm = GameTheoryAlgorithm()
        self.assertIsInstance(game_algorithm, GameTheoryAlgorithm)

    def test_minimax_algorithm_initialization(self):
        # Test MinimaxAlgorithm initialization within GameTheoryAlgorithm
        game_algorithm = GameTheoryAlgorithm()
        minimax = game_algorithm.minimax_algorithm
        self.assertIsInstance(minimax, MinimaxAlgorithm)

    def test_algorithm_move_selection(self):
        # Test if the algorithm selects the correct move
        game_algorithm = GameTheoryAlgorithm()
        initial_state = game_algorithm.get_initial_game_state()  # Assuming a method to get the initial state
        move = game_algorithm.select_move(initial_state)
        self.assertIn(move, game_algorithm.get_possible_moves(initial_state))

    def test_game_play(self):
        # Test if the game can be played correctly through multiple steps
        game_algorithm = GameTheoryAlgorithm()
        game_result = game_algorithm.play_game()
        self.assertIn(game_result, ["win", "draw", "loss"])

if __name__ == "__main__":
    unittest.main()
