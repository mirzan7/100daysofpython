from turtle import Turtle, Screen
import time
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.t = Turtle()
        self.screen = Screen()
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for cubes in range(3):
            self.t = Turtle(shape="square")
            self.t.color("white")
            self.t.penup()
            self.t.goto(-20 * cubes, y=0)
            self.snake.append(self.t)

    def move(self):
        self.screen.update()
        time.sleep(0.1)
        for body in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[body - 1].xcor()
            new_y = self.snake[body - 1].ycor()
            self.snake[body].goto(new_x, new_y)
        self.head.forward(20)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.snake[0].setheading(0)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.snake[0].setheading(180)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.snake[0].setheading(270)


