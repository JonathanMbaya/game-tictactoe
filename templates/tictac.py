import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("1000x1000")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self, text="", font=("Arial", 24), width=16, height=6,
                                   command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.buttons.append(row)

    def click(self, i, j):
        if self.board[i][j] == "":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
