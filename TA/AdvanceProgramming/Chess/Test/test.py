import unittest
from ..Chess.chess import Chess, Board, Position, Piece, King, Queen, Bishop, Knight, Rook, Pawn

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess_game = Chess()

    def test_turn_switching(self):
        print("CHECKING THE TURN SWITCHING")
        # Start with White's turn
        current_player = "White"

        # Loop through a series of moves
        moves = [("a1", "a2"), ("a6", "a5"), ("b1", "b2"), ("b6", "b4")]

        for start_pos, end_pos in moves:
            # Make the move
            self.assertTrue(self.chess_game.chess_set.board.move_piece(self.chess_game.from_algebraic(start_pos), self.chess_game.from_algebraic(end_pos)))

            # Check if the turn has switched
            current_player = "White"
            self.assertEqual(current_player, self.chess_game.current_player)

    def test_is_valid_input(self):
        print("CHECKING THE is_valid_input METHOD")
        self.assertTrue(self.chess_game.is_valid_input("a2", "a4"))
        self.assertTrue(self.chess_game.is_valid_input("g7", "g5"))
        self.assertTrue(self.chess_game.is_valid_input("c1", "b3"))
        self.assertFalse(self.chess_game.is_valid_input("a9", "a4"))
        self.assertFalse(self.chess_game.is_valid_input("z2", "a4"))
        self.assertTrue(self.chess_game.is_valid_input("h2", "h4"))
        self.assertFalse(self.chess_game.is_valid_input("a2", "a12"))
        self.assertFalse(self.chess_game.is_valid_input("a2", "b12"))

    def test_from_algebraic(self):
        print("CHECKING THE from_algebraic METHOD")
        self.assertEqual((self.chess_game.from_algebraic("a2").row, self.chess_game.from_algebraic("a2").col), (2, 0))
        self.assertEqual((self.chess_game.from_algebraic("g7").row, self.chess_game.from_algebraic("g7").col), (7, 6))
        self.assertEqual((self.chess_game.from_algebraic("c1").row, self.chess_game.from_algebraic("c1").col), (1, 2))

    def test_is_check(self):
        print("CHECKING THE is_check METHOD")
        # Reset the board to its initial state
        self.chess_game.chess_set.board = Board()
        # Test scenario: Black king in check from White knight
        # White knight at position (3, 3)
        self.chess_game.chess_set.board.place_piece(Knight("White", self.chess_game.chess_set.board), Position(3, 4))
        # Black king at position (5, 5)
        self.chess_game.chess_set.board.place_piece(King("Black", self.chess_game.chess_set.board), Position(5, 5))
        # Ensure Black king is indeed in check
        self.assertTrue(self.chess_game.is_check("Black"))

        # Additional test scenarios can be added to cover more cases

    def test_is_checkmate(self):
        print("CHECKING THE is_checkmate METHOD")
        # Reset the board to its initial state
        self.chess_game.chess_set.board = Board()
        # Test scenario: Black king in checkmate by White queen
        # White queen at position (2, 4)
        self.chess_game.chess_set.board.place_piece(Queen("White", self.chess_game.chess_set.board), Position(2, 4))
        # Black king at position (0, 0)
        self.chess_game.chess_set.board.place_piece(King("Black", self.chess_game.chess_set.board), Position(0, 0))
        # Ensure Black king is indeed in checkmate
        self.assertTrue(self.chess_game.is_checkmate("Black"))

        # Additional test scenarios can be added to cover more cases


if __name__ == '__main__':
    unittest.main()

