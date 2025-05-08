import tkinter as tk
from tkinter import messagebox


class NQueenGame:
    def __init__(self, N=4):
        self.N = N
        self.window = tk.Tk()
        self.window.title("N-Queen Game")

        self.board = [[None for _ in range(N)] for _ in range(N)]
        self.queens = []

        self.create_board()
        self.window.mainloop()

    def create_board(self):
        for row in range(self.N):
            for col in range(self.N):
                btn = tk.Button(self.window, text="", font=("Arial", 18), height=2, width=5,
                                command=lambda r=row, c=col: self.place_queen(r, c))
                btn.grid(row=row, column=col)
                self.board[row][col] = btn

    def place_queen(self, row, col):
        if self.board[row][col]["text"] == "" and self.is_valid_move(row, col):
            self.board[row][col]["text"] = "Q"
            self.queens.append((row, col))

            if len(self.queens) == self.N:
                self.window.after(100, self.show_game_over)
        else:
            messagebox.showwarning("Invalid Move", "You cannot place a queen here!")

    def is_valid_move(self, row, col):
        for r, c in self.queens:
            if r == row or c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def show_game_over(self):
        play_again = messagebox.askyesno("Game Over",
                                         "You have successfully placed all queens!\nDo you want to play again?")
        if play_again:
            self.reset_board()
        else:
            self.window.destroy()

    def reset_board(self):
        for row in range(self.N):
            for col in range(self.N):
                self.board[row][col]["text"] = ""
        self.queens.clear()


if __name__ == "__main__":
    NQueenGame(4)
