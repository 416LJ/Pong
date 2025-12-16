from turtle import Screen
import time
from paddle import Paddle
import random

from scoreboard import Scoreboard
from the_court import TheCourt
from ball import Ball

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.listen()

red_paddle = Paddle((350, (random.randint(-250, 250))))
blue_paddle = Paddle((-350, (random.randint(-250, 250))))
blue_paddle.the_paddle.color("blue")
scoreboard = Scoreboard()
court = TheCourt()
screen.onkey(red_paddle.up, "Up")
screen.onkey(red_paddle.down, "Down")
screen.onkey(blue_paddle.up, "q")
screen.onkey(blue_paddle.down, "a")
screen.onkey(blue_paddle.up, "Q")
screen.onkey(blue_paddle.down, "A")

ball = Ball()
speed = .1
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(speed)
    ball.move()

    if ball.the_ball.ycor() > 280 or ball.the_ball.ycor() < -280:
        ball.ball_bounce_y()
    if 50 > ball.the_ball.distance(red_paddle.the_paddle) and 320 < ball.the_ball.xcor() or ball.the_ball.distance(blue_paddle.the_paddle) < 50 and ball.the_ball.xcor() < -320:
        speed /= 1.1
        ball.ball_bounce_x()
    if ball.the_ball.xcor() > 380:
        scoreboard.update_score_blue()
        ball.ball_reset()
    if ball.the_ball.xcor() < -380:
        # increase points for red paddle
        scoreboard.update_score_red()
        ball.ball_reset()

screen.exitonclick()