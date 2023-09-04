import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()
        self.t = Turtle()
        self.t.goto(-290, -290)
        self.t.color("white")
        for _ in range(4):
            self.t.forward(580)
            self.t.left(90)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
