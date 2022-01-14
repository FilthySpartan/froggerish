import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
MAX_CARS = (scoreboard.level + 1) * 10

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
terry = Player()

car_list = []
screen.listen()
screen.onkeypress(terry.move, "Up")
scoreboard.update_scoreboard()

for i in range(0, 15):
    new_car = CarManager()
    new_car.starting_cars()
    car_list.append(new_car)

screen.tracer(1)

cars_generated = False
spawn_car_timer = 5

game_is_on = True
while game_is_on:
    time.sleep(0.001)
    for x in car_list:
        x.move_left()

    screen.update()

    if spawn_car_timer <= 0:
        for i in range(0, (scoreboard.level + 1) * 3):
            new_car = CarManager()
            car_list.append(new_car)
            spawn_car_timer = 10

    spawn_car_timer -= 1

    if terry.ycor() >= 300:
        scoreboard.next_level()
        terry.reset_position()


screen.exitonclick()