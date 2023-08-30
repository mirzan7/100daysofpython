import turtle
import random as rdm
from turtle import Turtle

t = Turtle()
screen = turtle.Screen()
starting_angle = 180


def draw_shape(sides, angle_of_sides, colour_of_the_shape):
    for _ in range(sides):
        t.pencolor(colour_of_the_shape)
        t.forward(100)
        t.right(angle_of_sides)


def find_angle(side):
    total_internal_angle = 180+((side-3)*180)
    return 180-(total_internal_angle/side)

angle = 0
for i in range(3, 10):
    red = rdm.random()
    green = rdm.random()
    blue = rdm.random()
    colour = (red, green, blue)
    angle = find_angle(i)
    draw_shape(i, angle, colour)
    angle += 1

screen.exitonclick()
