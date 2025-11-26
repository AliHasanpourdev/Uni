class Move:
    def __init__(self, piece, start_pos, end_pos):
        self.piece = piece
        self.start_pos = start_pos
        self.end_pos = end_pos

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)] #initialize the board
        self.last_move = None

    def place_piece(self, piece, position):
        piece.position = position
        self.board[position.row][position.col] = piece

    def remove_piece(self, piece):
        self.board[piece.position.row][piece.position.col] = None

    def move_piece(self, start_pos, end_pos):
        piece = self.board[start_pos.row][start_pos.col]
        if piece:
            if piece.move(end_pos):
                last_move_start = self.last_move.start_pos if self.last_move else None
                last_move_end = self.last_move.end_pos if self.last_move else None
                last_move_row_diff = abs(last_move_start.row - last_move_end.row) if self.last_move else None
                captured_piece = self.last_move.piece if self.last_move else None
                # En passant capture
                if captured_piece and isinstance(piece, Pawn) and self.is_enemy_piece(Position(end_pos.row - abs(start_pos.row-end_pos.row),end_pos.col - abs(start_pos.col-end_pos.col)), captured_piece.color) and isinstance(captured_piece, Pawn) and isinstance(self.last_move.piece, Pawn) and last_move_row_diff==2:
                    print("EN PASSANT SHOULD REMOVE PIECE NOW!")
                    print(captured_piece)

                    # Check if there's a piece to capture
                    self.remove_piece(captured_piece)

                self.remove_piece(piece)
                self.place_piece(piece,end_pos)
                piece.has_moved = True
                self.last_move = Move(piece, start_pos, end_pos)
                return True
        else:
            print("No piece at the starting position.")
            return False

    def revert_move(self, start_pos, end_pos, captured_piece):
        piece = self.board[end_pos.row][end_pos.col]
        self.board[start_pos.row][start_pos.col] = piece
        self.board[end_pos.row][end_pos.col] = captured_piece
        piece.position = start_pos
        piece.has_moved = False
        self.last_move = None  # Reset last move when reverting move


    def is_square_empty(self, position):
        return self.board[position.row][position.col] is None

    def is_enemy_piece(self, position, color):
        piece = self.board[position.row][position.col]
        if piece:
            if piece.color == color:
                return False
            else:
                return True

    def is_inside_board(self, position):
        if (position.row <= 7 and position.row >=0) and (position.col <= 7 and position.col >=0):
            return True

        return False

    def print_board(self):
        print(" | a b c d e f g h")
        print("------------------")
        for i, row in enumerate(self.board):
            row_str = str(i) + "| "
            for piece in row:
                if piece:
                    row_str += f"{piece} "
                else:
                    row_str += ". "
            print(row_str)
        print("\n")

class ChessSet:
    def __init__(self):
        self.board = Board()
        self.setup_board()

    def setup_board(self):
        # Place white pieces
        self.board.place_piece(Rook("White",self.board), Position(0, 0))
        self.board.place_piece(Knight("White",self.board), Position(0, 1))
        self.board.place_piece(Bishop("White",self.board), Position(0, 2))
        self.board.place_piece(Queen("White",self.board), Position(0, 3))
        self.board.place_piece(King("White",self.board), Position(0, 4))
        self.board.place_piece(Bishop("White",self.board), Position(0, 5))
        self.board.place_piece(Knight("White",self.board), Position(0, 6))
        self.board.place_piece(Rook("White",self.board), Position(0, 7))

        self.board.place_piece(Pawn("White",self.board), Position(1, 0))
        self.board.place_piece(Pawn("White",self.board), Position(1, 1))
        self.board.place_piece(Pawn("White",self.board), Position(1, 2))
        self.board.place_piece(Pawn("White",self.board), Position(1, 3))
        self.board.place_piece(Pawn("White",self.board), Position(1, 4))
        self.board.place_piece(Pawn("White",self.board), Position(1, 5))
        self.board.place_piece(Pawn("White",self.board), Position(1, 6))
        self.board.place_piece(Pawn("White",self.board), Position(1, 7))

        # Place black pieces
        self.board.place_piece(Rook("Black",self.board), Position(7, 0))
        self.board.place_piece(Knight("Black",self.board), Position(7, 1))
        self.board.place_piece(Bishop("Black",self.board), Position(7, 2))
        self.board.place_piece(Queen("Black",self.board), Position(7, 3))
        self.board.place_piece(King("Black",self.board), Position(7, 4))
        self.board.place_piece(Bishop("Black",self.board), Position(7, 5))
        self.board.place_piece(Knight("Black",self.board), Position(7, 6))
        self.board.place_piece(Rook("Black",self.board), Position(7, 7))

        self.board.place_piece(Pawn("Black",self.board), Position(6, 0))
        self.board.place_piece(Pawn("Black",self.board), Position(6, 1))
        self.board.place_piece(Pawn("Black",self.board), Position(6, 2))
        self.board.place_piece(Pawn("Black",self.board), Position(6, 3))
        self.board.place_piece(Pawn("Black",self.board), Position(6, 4))
        self.board.place_piece(Pawn("Black",self.board), Position(6, 5))
        self.board.place_piece(Pawn("Black",self.board), Position(6, 6))
        self.board.place_piece(Pawn("Black",self.board), Position(6, 7))

    def print_board(self):
        self.board.print_board()

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def match(self,list_pos):
        for p in list_pos:
            if p.row == self.row and p.col == self.col:
                return True

        return False

class Piece:
    def __init__(self, color, board, position=None):
        self.color = color
        self.board = board
        self.has_moved = False
        self.position = position

    def move(self,end_pos):
        #print([(i.row,i.col) for i in self.possible_moves()], "list in move method")
        #print(end_pos.row, end_pos.col, "end_pos in move method")
        #print(end_pos in self.possible_moves(), "check in move method")
        if end_pos.match(self.possible_moves()):
            return True
        else:
            return False

    def possible_moves(self):
        # This is a generic method for the Piece class, it will be overridden
        pass

    def __str__(self):
        # This is a generic string representation method for the Piece class, it can be overridden
        pass

class King(Piece):
    def __init__(self,color,board,position=None):
        super().__init__(color,board,position)
        self.piece_type = "king"

    def possible_moves(self):
        moves = []
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1),
                   (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dr, dc in offsets:
            new_pos = Position(self.position.row + dr, self.position.col + dc)
            if self.board.is_inside_board(new_pos) and (self.board.is_square_empty(new_pos) or self.board.is_enemy_piece(new_pos, self.color)):
                moves.append(new_pos)
        # Castling
        if not self.board.board[self.position.row][self.position.col].has_moved:
            # Check kingside castling
            if self.board.board[self.position.row][7] and not self.board.board[self.position.row][7].has_moved:
                if all(self.board.is_square_empty(Position(self.position.row, c)) for c in range(self.position.col + 1, 7)):
                    moves.append(Position(self.position.row, self.position.col + 2))
            # Check queenside castling
            if  self.board.board[self.position.row][0] and not self.board.board[self.position.row][0].has_moved:
                if all(self.board.is_square_empty(Position(self.position.row, c)) for c in range(1, self.position.col)):
                    moves.append(Position(self.position.row, self.position.col - 2))
        return moves

    def __str__(self):
        if self.color == "White":
            return "K"
        return "k"

class Bishop(Piece):
    def __init__(self, color, board, position=None):
        super().__init__(color, board, position)
        self.piece_type = "bishop"

    def possible_moves(self):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            row, col = self.position.row + dr, self.position.col + dc
            while self.board.is_inside_board(Position(row, col)):
                new_pos = Position(row, col)
                if self.board.is_square_empty(new_pos):
                    moves.append(new_pos)
                elif self.board.is_enemy_piece(new_pos, self.color):
                    moves.append(new_pos)
                    break
                else:
                    break
                row += dr
                col += dc

        return moves

    def __str__(self):
        if self.color == "White":
            return "B"
        return "b"


class Pawn(Piece):
    def __init__(self, color, board, position=None):
        super().__init__(color, board, position)
        self.piece_type = "pawn"
        self.has_moved_twice = False

    def possible_moves(self):
        moves = []
        direction = 1 if self.color == "White" else -1
        start_row = 1 if self.color == "White" else 6

        # Moves for regular pawn advance
        new_pos = Position(self.position.row + direction, self.position.col)
        if self.board.is_inside_board(new_pos) and self.board.is_square_empty(new_pos):
            moves.append(new_pos)
        # Special two-square move from starting position
        if self.position.row == start_row:
            new_pos = Position(self.position.row + 2 * direction, self.position.col)
            if self.board.is_inside_board(new_pos) and self.board.is_square_empty(new_pos):
                moves.append(new_pos)

        # Moves for capturing diagonally
        for dc in (-1, 1):
            new_pos = Position(self.position.row + direction, self.position.col + dc)
            if self.board.is_inside_board(new_pos) and self.board.is_enemy_piece(new_pos, self.color):
                moves.append(new_pos)

        # UN PASSANT IMPLEMENTATION
        if self.board.last_move and isinstance(self.board.last_move.piece, Pawn):
            last_move_start = self.board.last_move.start_pos
            last_move_end = self.board.last_move.end_pos
            last_move_row_diff = abs(last_move_start.row - last_move_end.row)

            # Check if the last move was a two-square pawn advance
            if last_move_row_diff == 2:
                # Check if the enemy pawn is adjacent and on the same row
                if abs(last_move_end.row - self.position.row) == 0 and abs(last_move_end.col - self.position.col) == 1:
                    # Add the en passant move
                    new_pos = Position(self.position.row + direction, last_move_end.col)
                    moves.append(new_pos)

        return moves

    def __str__(self):
        if self.color == "White":
            return "P"
        return "p"

class Rook(Piece):
    def __init__(self, color, board, position=None):
        super().__init__(color, board, position)
        self.piece_type = "rook"
        
    def possible_moves(self):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for dr, dc in directions:
            row, col = self.position.row + dr, self.position.col + dc
            while self.board.is_inside_board(Position(row, col)):
                new_pos = Position(row, col)
                if self.board.is_square_empty(new_pos):
                    moves.append(new_pos)
                elif self.board.is_enemy_piece(new_pos, self.color):
                    moves.append(new_pos)
                    break
                else:
                    break
                row += dr
                col += dc

        return moves

    def __str__(self):
        if self.color == "White":
            return "R"
        return "r"


class Knight(Piece):
    def __init__(self, color, board, position=None):
        super().__init__(color, board, position)
        self.piece_type = "knight"

    def possible_moves(self):
        moves = []
        offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                   (1, -2), (1, 2), (2, -1), (2, 1)]

        for dr, dc in offsets:
            new_pos = Position(self.position.row + dr, self.position.col + dc)
            if self.board.is_inside_board(new_pos) and (self.board.is_square_empty(new_pos) or self.board.is_enemy_piece(new_pos, self.color)):
                moves.append(new_pos)

        return moves

    def __str__(self):
        if self.color == "White":
            return "N"
        return "n"


class Queen(Piece):
    def __init__(self, color, board, position=None):
        super().__init__(color, board, position)
        self.piece_type = "queen"

    def possible_moves(self):
        moves = []

        # Define offsets for rook-like moves (horizontal and vertical)
        rook_offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Define offsets for bishop-like moves (diagonal)
        bishop_offsets = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

        # Check rook-like moves
        for dr, dc in rook_offsets:
            r, c = self.position.row, self.position.col
            while True:
                r, c = r + dr, c + dc
                new_pos = Position(r, c)
                if not self.board.is_inside_board(new_pos):
                    break
                if self.board.is_square_empty(new_pos):
                    moves.append(new_pos)
                elif self.board.is_enemy_piece(new_pos, self.color):
                    moves.append(new_pos)
                    break
                else:
                    break

        # Check bishop-like moves
        for dr, dc in bishop_offsets:
            r, c = self.position.row, self.position.col
            while True:
                r, c = r + dr, c + dc
                new_pos = Position(r, c)
                if not self.board.is_inside_board(new_pos):
                    break
                if self.board.is_square_empty(new_pos):
                    moves.append(new_pos)
                elif self.board.is_enemy_piece(new_pos, self.color):
                    moves.append(new_pos)
                    break
                else:
                    break

        return moves

    def __str__(self):
        if self.color == "White":
            return "Q"
        return "q"


class Chess:
    def __init__(self):
        self.chess_set = ChessSet()
        self.current_player = "White"

    def start_game(self):
        print("Welcome to Chess!\n")

        while True:
            self.chess_set.print_board()
            print(f"\n{self.current_player}'s turn:")
            start_pos = input("Enter the position of the piece you want to move (e.g., 'a2'): ")
            end_pos = input("Enter the position to move the piece to (e.g., 'a4'): ")

            #TODONE - check if the input is according to the expected format
            if not self.is_valid_input(start_pos,end_pos):
                print("Invalid input. Please enter positions in the format 'a2' to 'h8'.")
                continue

            # Simulate the move and check if the king is still in check
            start_pos = self.from_algebraic(start_pos)
            end_pos = self.from_algebraic(end_pos)
            captured_piece = self.chess_set.board.board[end_pos.row][end_pos.col]

            #TODONE - move the piece if it is possible, otherwise notify the user to select other moves
            if not self.chess_set.board.move_piece(start_pos, end_pos):
                print("Select Other Moves!")
                continue

            if self.is_check(self.current_player):
                print(self.current_player,"King is in check!")
                continue

            #TODONE - print the board
            #self.chess_set.print_board()

            #TODONE - check if the king is in checkmate (much simpler than real-world chess)
            if self.is_checkmate(self.current_player):
                print(['White', 'Black'][self.current_player=='White'], "Wins!")
                break

            #TODONE - switch the turns
            self.current_player = ['White', 'Black'][self.current_player=='White']


    def is_valid_input(self, start_pos, end_pos):
        #TODONE - check each of the inputs have length of two elements and the first letter is an alphabet and the second one is a digit
        if len(start_pos) == 2 and start_pos[0].isalpha() and start_pos[0].islower() and end_pos[1].isdigit() and len(end_pos) == 2 and end_pos[0].isalpha() and end_pos[0].islower() and end_pos[1].isdigit() and self.chess_set.board.is_inside_board(self.from_algebraic(start_pos)) and self.chess_set.board.is_inside_board(self.from_algebraic(end_pos)):
            return True

        return False

    def is_check(self, current_player):
        # Find current player's king on the board
        king_position = None
        for row in range(8):
            for col in range(8):
                piece = self.chess_set.board.board[row][col]
                if piece and piece.piece_type == "king" and piece.color == current_player:
                    king_position = Position(row, col)
                    break
            if king_position:
                break

        # Check if the king is under threat (in check)
        for row in range(8):
            for col in range(8):
                piece = self.chess_set.board.board[row][col]
                if piece and piece.color != current_player:
                    if king_position.match(piece.possible_moves()):
                        return True
        return False

    def is_checkmate(self, current_player):
        # For simplicity, we consider losing the king as checkmate
        enemy = "Black" if current_player == "White" else "White"
        for i in range(8):
            for j in range(8):
                piece = self.chess_set.board.board[i][j]
                if piece and piece.piece_type == "king" and piece.color == enemy:
                    return False
        return True

    def from_algebraic(self,algebraic_notation):
        col = ord(algebraic_notation[0]) - ord('a')
        row = int(algebraic_notation[1])
        return Position(row,col)

if __name__ == "__main__":
    chess_game = Chess()
    chess_game.start_game()
