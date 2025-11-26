import tkinter as tk
import tkinter.messagebox as messagebox
from chess import Chess, Position

class ChessGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chess")
        self.chess_game = Chess()
        self.board_canvas = tk.Canvas(master, width=400, height=400, bg="white")
        self.board_canvas.pack()
        self.draw_board()
        self.selected_square = None
        self.board_canvas.bind("<Button-1>", self.on_square_clicked)

        # Add label to display current player's turn
        self.turn_label = tk.Label(master, text="White's Turn", font=("Arial", 14))
        self.turn_label.pack(pady=10)

    def draw_board(self):
        self.board_canvas.delete("all")  # Clear the canvas

        for i in range(8):
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "gray"
                x0, y0 = j * 50, i * 50
                x1, y1 = x0 + 50, y0 + 50
                self.board_canvas.create_rectangle(x0, y0, x1, y1, fill=color)

        self.draw_pieces()


    def draw_pieces(self):
        self.piece_images = {}
        for row in range(8):
            for col in range(8):
                piece = self.chess_game.chess_set.board.board[row][col]
                if piece:
                    piece_name = piece.__class__.__name__.lower()
                    color = piece.color.lower()
                    try:
                        image = tk.PhotoImage(file=f"images/{color}_{piece_name}.png")
                        x, y = col * 50 + 25, row * 50 + 25
                        self.board_canvas.create_image(x, y, image=image)
                        self.piece_images[(row, col)] = image  # Store the image in the dictionary
                    except Exception as e:
                        print(f"Error loading image: {e}")


    def on_square_clicked(self, event):

        col = event.x // 50
        row = (event.y // 50)  # Adjusted to calculate the correct row
        file = chr(col + 97)
        rank = row  # Adjusted to calculate the correct rank
        square = f"{file}{rank}"
        print(f"Square clicked: {square}")

        if not self.chess_game.is_checkmate(self.chess_game.current_player):
            if self.selected_square:
                start_pos = self.selected_square
                end_pos = square
                # Check if it's the current player's turn
                start_pos_algebraic = self.chess_game.from_algebraic(start_pos)
                piece = self.chess_game.chess_set.board.board[start_pos_algebraic.row][start_pos_algebraic.col]
                if piece.color != self.chess_game.current_player:
                    print("It's not your turn to move.")
                    self.selected_square = None
                    return

                # Simulate the move and check if the king is still in check
                start_pos_algebraic = self.chess_game.from_algebraic(start_pos)
                end_pos_algebraic = self.chess_game.from_algebraic(end_pos)
                captured_piece = self.chess_game.chess_set.board.board[end_pos_algebraic.row][end_pos_algebraic.col]

                # Move the piece if it is possible, otherwise notify the user to select other moves
                if not self.chess_game.chess_set.board.move_piece(start_pos_algebraic, end_pos_algebraic):
                    print("Select Other Moves!")
                    self.selected_square = None
                    return

                # Check if the move puts the current player's king in check
                if self.chess_game.is_check(self.chess_game.current_player):
                    print(self.chess_game.current_player, "king is is now in check!")

                # Redraw the board after the move is made
                self.draw_board()
                self.selected_square = None

                # Check if the king is in checkmate
                if self.chess_game.is_checkmate(self.chess_game.current_player):
                    print(['White', 'Black'][self.chess_game.current_player == 'White'], "Wins!")
                    winner = ['White', 'Black'][self.chess_game.current_player != 'White']
                    messagebox.showinfo("Game Over", f"{winner} Wins!")
                    self.reset_game()
                    return

                # Switch the turns
                self.chess_game.current_player = ['White', 'Black'][self.chess_game.current_player == 'White']
                self.update_turn_label()
            else:
                self.selected_square = square

    def reset_game(self):
        # Reset the game by creating a new instance of Chess and redrawing the board
        self.chess_game = Chess()
        self.draw_board()

    def update_turn_label(self):
        # Update the turn label with the current player's turn
        current_turn = "White's Turn" if self.chess_game.current_player == 'White' else "Black's Turn"
        self.turn_label.config(text=current_turn)




if __name__ == "__main__":
    root = tk.Tk()
    app = ChessGUI(root)
    root.mainloop()
