from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.red_score = 0
        self.blue_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(+225, 270)
        self.write(arg=f"{self.red_score}", align="center", move=False, font=(f"courier", 20, "normal"))
        self.goto(-225, 270)
        self.write(arg=f"{self.blue_score}", align="center", move=False, font=(f"courier", 20, "normal"))


    def update_score_blue(self):
        self.blue_score += 1
        self.update_score()

    def update_score_red(self):
        self.red_score += 1
        self.update_score()



