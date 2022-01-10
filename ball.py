from turtle import Turtle
import random



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.x_cord = 10
        self.y_cord = 10
        self.move_speed = 0.1

        # self.l_user = 0
        # self.r_user = 0

    def move(self):
        x = self.xcor() + self.x_cord
        y = self.ycor() + self.y_cord
        self.goto(x, y)

    def bounce_y(self):
        self.y_cord *= -1

    def bounce_x(self):
        self.x_cord *= -1
        self.move_speed *= 0.9

    def goto_start(self, x, y):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_cord *= x
        self.y_cord *= y
