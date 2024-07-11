import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
screen = Screen()
screen.setup(width=800, height=600)
screen.title("pong Game")
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(r_paddle.go_up, 'Up')

screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
