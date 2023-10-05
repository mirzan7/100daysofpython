import turtle
from turtle import Turtle
t = Turtle()
screen = turtle.Screen()
drawing = True


def move_up():
    t.forward(10)


def move_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)


def move_left():
    new_heading = t.heading()+10
    t.setheading(new_heading)


def move_back():
    t.backward(10)


def clear():
    t.home()
    
    t.clear()


screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(move_back, "s")
screen.onkey(clear, "c")
screen.exitonclick()
