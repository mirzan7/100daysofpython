from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"score = {self.score}", False, align="center")
        self.high_score = 0

    def show_score(self):
        self.clear()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"score = {self.score} High score {self.high_score}", False, align="center")

    def add_score(self):
        self.score += 1
        self.show_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.show_score()
