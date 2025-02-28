import time
from turtle import Turtle,Screen
from Paddle import paddle
from Ball import ball
from Scoreboard import scoreboard
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle=paddle((350,0))
l_paddle=paddle((-350,0))
ball=ball()
scoreboard = scoreboard()

r_paddle.movement("Up","Down")
l_paddle.movement("w","s")


on = True
while on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320) :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.resetposition()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.resetposition()
        scoreboard.r_point()




screen.exitonclick()
