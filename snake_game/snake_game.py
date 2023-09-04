from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

is_game_live = True
while is_game_live:
    score.show_score()
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect food.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_body()
        score.add_score()

    # collision .
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        is_game_live = False
        score.game_over()

    for body in snake.segment[1:]:
        if snake.head.distance(body) < 10:
            is_game_live = False
            score.game_over()

screen.exitonclick()
