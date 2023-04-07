import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kółko i Krzyżyk")
        self.board = [""] * 9
        self.current_player = "X"

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text="", width=10, height=3, command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner(self.current_player):
                messagebox.showinfo(f"Wygryna", f"Gracz {self.current_player} wygrywa!")
                self.reset_board()
            elif not any(cell == "" for cell in self.board):
                messagebox.showinfo("Remis", "Gra zakończona remisem!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        winnig_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in winnig_combinations:
            if self.board[a] == self.board[b] == self.board[c] == player:
                return True
        return False

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "O" if self.current_player == "X" else "X"

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
