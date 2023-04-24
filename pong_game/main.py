from scoreboard import ScoreBoard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

game_is_on = True
time_sleep= 0.1

screen.listen()
screen.onkeypress(key="Up", fun=paddle_r.move_up)
screen.onkeypress(key="Down", fun=paddle_r.move_down)

screen.onkeypress(key="w", fun=paddle_l.move_up)
screen.onkeypress(key="s", fun=paddle_l.move_down)

while game_is_on:
    screen.update()
    time.sleep(time_sleep)
    ball.move()

    # Detecting collision with upper and down walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        if time_sleep > 0.01:
            time_sleep -= 0.01
    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if time_sleep > 0.01:
            time_sleep -= 0.01

    # Detecting when the ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_ball()
        time_sleep = 0.1
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        time_sleep = 0.1
        scoreboard.r_point()

screen.exitonclick()
