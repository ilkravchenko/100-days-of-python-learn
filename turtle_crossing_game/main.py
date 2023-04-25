import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turt = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(key='Up', fun=turt.move)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Check fo Finish
    if turt.ycor() > 280:
        turt.refresh_position()
        scoreboard.increase_level()
        cars.increase_speed()

    # Moving and adding cars
    cars.create_cars()
    cars.move()

    # Detecting collision with car
    for car in cars.cars:
        if car.distance(turt) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()