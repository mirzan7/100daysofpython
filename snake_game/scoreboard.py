from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"score = {self.score}", False, align="center")

    def show_score(self):
        self.clear()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"score = {self.score}", False, align="center")

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("game over :( ", align="center")
