from turtle import Turtle

class TheCourt:
    def __init__(self):
        self.the_boundary = Turtle()
        self.the_boundary.color("white")
        self.the_boundary.penup()
        self.the_boundary.hideturtle()
        self.the_boundary.goto(x=0,y=-300)
        self.the_boundary.setheading(90)
        while self.the_boundary.ycor() < 300:
            self.the_boundary.forward(20)
            self.the_boundary.penup()
            self.the_boundary.forward(20)
            self.the_boundary.pendown()






