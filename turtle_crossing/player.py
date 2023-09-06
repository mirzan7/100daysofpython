from turtle import Turtle

STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POINT)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def detect_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

    def restart_at_beg(self):
        self.goto(STARTING_POINT)
