import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=500, height=400)
is_game_live = False
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race:  ")
colors = ["red", "yellow", "orange", "blue", "violet", "green"]

all_turtle = []
for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(-230, -100+(turtle_index*30))
    all_turtle.append(t)

if user_bet :
    is_game_live = True

while is_game_live:
    for turtle in all_turtle:
        if turtle.xcor()>220:
            is_game_live = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won the race {winning_color}!!!")
            else:
                print(f"you have lost the game, the winner is {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()