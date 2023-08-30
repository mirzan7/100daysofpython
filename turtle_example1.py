import turtle
from turtle import Turtle

t = Turtle()
screen = turtle.Screen()
for i in range(4):
    t.forward(100)
    t.left(90)

screen.exitonclick()
