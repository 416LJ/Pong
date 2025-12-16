from random import randint
from turtle import Turtle
import random

class Ball:
    def __init__(self):
        self.the_ball = Turtle(shape="circle")
        self.the_ball.penup()
        self.the_ball.speed("slowest")
        self.the_ball.color("yellow")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.the_ball.xcor() + self.x_move
        new_y = self.the_ball.ycor() + self.y_move
        self.the_ball.goto(x=new_x,y=new_y)

    def ball_bounce_y(self):
        self.y_move *= -1

    def ball_bounce_x(self):
        self.x_move *= -1

    def ball_reset(self):
        self.the_ball.goto(0,0)
        self.ball_bounce_x()
