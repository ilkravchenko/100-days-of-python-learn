from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

game_is_on = True
TIME_SLEEP = 0

input = screen.textinput('Select level:', 'What level you want choose? (easy/medium/hard)').lower()
if input == 'easy':
    TIME_SLEEP = 0.3
elif input == 'medium':
    TIME_SLEEP = 0.2
elif input == 'hard':
    TIME_SLEEP = 0.1

score_board = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(TIME_SLEEP)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_location()
        snake.increase_lenght()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
