import random
from snake import Snake
from turtle import Turtle, Screen
import time

t = Turtle()
screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")


is_game_live = True
while is_game_live:
    snake.move()

screen.exitonclick()

