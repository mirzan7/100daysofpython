from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()

    def show_score(self):
        self.goto(-280, 280)
        self.write(f"LEVEL : {self.level}", FONT)

    def game_over(self):
        self.write("GAME OVER !!!!")

    def level_up(self):
        self.level += 1

