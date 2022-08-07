from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('The Pong Game')
screen.tracer(0)

playR = Paddle(350, 0)
playL = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(playR.up, 'Up')
screen.onkey(playR.down, 'Down')
screen.onkey(playL.up, 'w')
screen.onkey(playL.down, 's')
screen.listen()

is_on = True

while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        print(ball.position())

    if ball.distance(playR) < 50 and ball.xcor() > 330 or ball.distance(playL) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        print('-------1------')


    if ball.xcor() > 360:
        print('-------2------')
        ball.reset_position()
        scoreboard.lscore += 1
        if scoreboard.check():
            is_on = False

    elif ball.xcor() < -360:
        print('-------3------')
        ball.reset_position()
        scoreboard.rscore += 1
        if scoreboard.check():
            is_on = False

    scoreboard.refresh()





screen.exitonclick()
