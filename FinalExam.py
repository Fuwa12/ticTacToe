from tkinter import *
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.players = ["X", "O"]
        self.current_player = random.choice(self.players)
        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]
        self.setup_ui()

    def setup_ui(self):
        self.label = Label(self.master, text=self.current_player + " turn", font=('consolas', 40))
        self.label.pack(side="top")

        reset_button = Button(self.master, text="Restart", font=('consolas', 20), command=self.new_game)
        reset_button.pack(side="top")

        frame = Frame(self.master)
        frame.pack()

        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                                    command=lambda r=row, c=column: self.next_turn(r, c))
                self.buttons[row][column].grid(row=row, column=column)

    def next_turn(self, row, column):
        if self.buttons[row][column]['text'] == "" and not self.check_winner():
            self.buttons[row][column]['text'] = self.current_player

            if self.check_winner():
                self.label.config(text=self.current_player + " wins")
            elif self.empty_spaces():
                self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
                self.label.config(text=self.current_player + " turn")
            else:
                self.label.config(text="Tie!")

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                self.buttons[row][0].config(bg="green")
                self.buttons[row][1].config(bg="green")
                self.buttons[row][2].config(bg="green")
                return True

        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                self.buttons[0][column].config(bg="green")
                self.buttons[1][column].config(bg="green")
                self.buttons[2][column].config(bg="green")
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.buttons[0][0].config(bg="green")
            self.buttons[1][1].config(bg="green")
            self.buttons[2][2].config(bg="green")
            return True

        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.buttons[0][2].config(bg="green")
            self.buttons[1][1].config(bg="green")
            self.buttons[2][0].config(bg="green")
            return True

        elif self.empty_spaces() is False:
            for row in range(3):
                for column in range(3):
                    self.buttons[row][column].config(bg="yellow")
            return False

        else:
            return False

    def empty_spaces(self):
        return any(button['text'] == "" for row in self.buttons for button in row)

    def new_game(self):
        self.current_player = random.choice(self.players)
        self.label.config(text=self.current_player + " turn")

        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="", bg="#F0F0F0")


if __name__ == "__main__":
    window = Tk()
    window.title("Tic-Tac-Toe")
    game = TicTacToe(window)
    window.mainloop()
