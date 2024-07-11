from turtle import Screen,shape,colormode
from car import Car
from control import Control
import time
from score import Score

speed = 0.5

screen = Screen()
screen.tracer(0)
colormode(255)
screen.title("Car Race Game")
image = 'track.gif'
screen.addshape(image)
shape(image)
car = Car()
score =Score()

screen.listen()
block = 0

block_list = []
game_is_on = True
screen.onkeypress(car.move_left, 'Left')
screen.onkeypress(car.move_right, 'Right')

while game_is_on:
    time.sleep(speed)
    score.update()
    if block == 7:
        control = Control()
        block_list.append(control)
        block = 0
    block += 1
    for blocks in block_list:
        blocks.move()
        if blocks.ycor() == -310:
            score.increase_score()
            blocks.clear()
    if score.score %10 ==0:
        speed *= 0.9      
    if car.xcor() > 190 or car.xcor() < -190:
        game_is_on = False
        screen.clear()
        score.game_over()
    for blocks in block_list:
        if car.distance(blocks) < 50:
            game_is_on = False
            screen.clear()
            score.game_over()
    screen.update()

screen.exitonclick()