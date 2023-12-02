from tkinter import *
import random

global gameStatus  # this is global variable
gameStatus = True

class TicTacToe():
    def next_turn(self, row, column):  # Add self parameter

        global player

        if buttons[row][column]['text'] == "" and self.check_winner() is False:

            if player == players[0]:

                buttons[row][column]['text'] = player

                if self.check_winner() is False:
                    player = players[1]
                    label.config(text=(players[1]+" turn"))

                elif self.check_winner() is True:
                    label.config(text=(players[0]+" wins"))

                elif self.check_winner() == "Tie":
                    label.config(text="Tie!")

            else:

                buttons[row][column]['text'] = player

                if self.check_winner() is False:
                    player = players[0]
                    label.config(text=(players[0]+" turn"))

                elif self.check_winner() is True:
                    label.config(text=(players[1]+" wins"))

                elif self.check_winner() == "Tie":
                    label.config(text="Tie!")

    def check_winner(self):

        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                return True

        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                buttons[0][column].config(bg="green")
                buttons[1][column].config(bg="green")
                buttons[2][column].config(bg="green")
                return True

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True

        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            return True

        elif self.empty_spaces() is False:

            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="yellow")
            return "Tie"

        else:
            return False

    def empty_spaces(self):
        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] == "":
                    return True
        return False


def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")


window = Tk()
game = TicTacToe()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]



label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: game.next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()
