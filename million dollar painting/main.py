import colorgram
import turtle
from turtle import Turtle
import random

color_list = [(235, 234, 233), (231, 233, 238), (233, 238, 235), (239, 233, 236),
              (16, 27, 55), (69, 94, 130), (186, 161, 120), (140, 88, 62),
              (138, 157, 181), (134, 75, 95), (62, 17, 9), (183, 140, 159)]

t = Turtle()
screen = turtle.Screen()
t.left(225)
t.penup()
t.hideturtle()
t.speed("fastest")
t.forward(300)
t.left(135)
number_of_dots = 100
for i in range(1, number_of_dots + 1):
    color = t.color(random.choice(color_list))
    t.dot(5, color)

    t.forward(20)
    if i % 10 == 0:
        t.setheading(90)
        t.forward(20)
        t.left(90)
        t.forward(200)
        t.right(180)

screen.exitonclick()
