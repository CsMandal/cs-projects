import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        # is_game_on = False
        # score.game_over()
        score.reset_score()
        choice = screen.textinput("Game over !!", prompt=f"Your Score is {score.score}  wanna continue (y/n)").lower()
        if choice == 'y':
            snake.reset()
        else:
            is_game_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            choice = screen.textinput("Game over !!", prompt=f"Your Score is {score.score}  wanna continue (y/n)").lower()
            if choice == 'y':
                snake.reset()
            else:
                is_game_on = False
    snake.move()
screen.exitonclick()