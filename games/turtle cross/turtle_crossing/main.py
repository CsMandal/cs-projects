import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
speed = 0.1

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car.create_car()
    car.move_car()
    if car.collision(player.position()):
        game_is_on = False
        screen.clear()
        score.game_over()
    if player.ycor() > 280:
        score.update()
        speed *= 0.5
        player.starting_position()

screen.exitonclick()


