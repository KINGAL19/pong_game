from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.move_speed = 0.1
        self.stepX = 10
        self.stepY = 10


    def move(self):
        new_x = self.xcor() + self.stepX
        new_y = self.ycor() + self.stepY
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.stepY *= -1

    def bounce_x(self):
        self.stepX *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        time.sleep(2)
        self.move_speed = 0.1
        self.bounce_x()

