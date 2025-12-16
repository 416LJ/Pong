from turtle import Turtle

UP = 90
DOWN = 270

class Paddle:
    def __init__(self,position):
        self.y_cord = 0
        self.the_paddle = Turtle(shape="square")
        self.the_paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.the_paddle.penup()
        self.the_paddle.speed("fastest")
        self.the_paddle.color("red")
        self.the_paddle.goto(position)
        self.score = 0

    def up(self):
        new_y = self.the_paddle.ycor() + 20
        self.the_paddle.goto(self.the_paddle.xcor(),new_y)

    def down(self):
        new_y = self.the_paddle.ycor() - 20
        self.the_paddle.goto(self.the_paddle.xcor(), new_y)



