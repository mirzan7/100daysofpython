import turtle
from turtle import Turtle

t = Turtle()
screen = turtle.Screen()
line = 7
gap = 3
for _ in range(100):
    t.forward(line)
    t.penup()
    t.forward(gap)
    t.pendown()

screen.exitonclick()