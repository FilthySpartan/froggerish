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
    time.sleep(scoreboard.move_speed)

    for x in car_list:
        x.move_left()
        if x.xcor() < -340:
            x.reset_position()

    for x in car_list:
        if terry.distance(x.xcor() + 20, x.ycor()) < 20 or terry.distance(x.xcor() - 20, x.ycor()) < 20:
            game_is_on = False
            scoreboard.game_over()

    spawn_car_timer -= 1

    if terry.ycor() >= 300:
        scoreboard.next_level()
        terry.reset_position()

    if spawn_car_timer <= 0 and len(car_list) < 25:
        new_car = CarManager()
        car_list.append(new_car)
        spawn_car_timer = 5

    screen.update()

    print(len(car_list))
    print(f"move speed {scoreboard.move_speed}")


screen.exitonclick()
