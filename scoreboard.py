from turtle import Turtle, Screen
import time

ALIGNMENT = "center"
FONT = ("Hind Siliguri", 30, "bold")

screen = Screen()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_user = 0
        self.r_user = 0
        self.score()

    def score(self):
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=302)
        self.color('white')
        self.write(f"{self.l_user}       {self.r_user}", move=True, align=ALIGNMENT, font=FONT)
        time.sleep(0.1)

    def point_user_l(self):
        self.clear()
        self.l_user += 1
        self.score()

    def point_user_r(self):
        self.clear()
        self.r_user += 1
        self.score()


class Lines(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(-400, 300)
        self.pendown()
        self.forward(800)
        self.penup()
        self.goto(-400, -300)
        self.pendown()

        self.forward(800)
        self.goto(0, -300)
        self.left(90)
        self.hideturtle()
        for _ in range(60):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(5)


