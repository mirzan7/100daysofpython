from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = 3
        self.t = Turtle()
        self.segment = []
        self.create_snake(self.body)
        self.head = self.segment[0]

    def create_snake(self, body):
        for cubes in range(body):
            self.t = Turtle(shape="square")
            self.t.color("white")
            self.t.penup()
            self.t.goto(-20 * cubes, y=0)
            self.segment.append(self.t)

    def move(self):
        for body in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[body - 1].xcor()
            new_y = self.segment[body - 1].ycor()
            self.segment[body].goto(new_x, new_y)
        self.head.forward(20)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(0)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(180)

    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(270)

    def add_body(self):
        self.t = Turtle(shape="square")
        self.t.color("white")
        self.t.penup()
        x_coordinate = self.segment[-1].xcor()
        y_coordinate = self.segment[-1].ycor()
        self.t.goto(x_coordinate, y_coordinate)
        self.segment.append(self.t)
