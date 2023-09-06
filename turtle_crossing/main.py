import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()
screen.setup(600, 600)
screen.tracer(0)
player = Player()
car = CarManager()
screen.listen()
screen.onkey(player.move_up, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.show_score()
    car.create_car()
    car.move_car()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            print("collided")
            score.game_over()
            game_is_on = False
    if player.detect_finish():
        print("finish line")
        player.clear()
        player.restart_at_beg()
        car.level_up()
        score.level_up()


screen.exitonclick()
