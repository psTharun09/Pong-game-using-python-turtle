from turtle import Turtle

class ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xm = 10
        self.ym = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xm
        new_y = self.ycor() + self.ym
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.ym *= -1

    def bounce_x(self):
        self.xm *= -1
        self.move_speed *= 0.9

    def resetposition(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()


