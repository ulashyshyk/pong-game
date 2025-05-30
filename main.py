from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
pen = Turtle()
circle = Turtle()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

#Middle line
pen.color("white")
pen.goto(0,400)
pen.goto(0,-400)

#Starting Circle
circle.width(10)
circle.shape("circle")
circle.shapesize(2)
circle.color("white","black")



r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.tracer(1)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(key="Up",fun=r_paddle.move_up)
screen.onkeypress(key="Down",fun=r_paddle.move_down)

screen.onkeypress(key="w",fun=l_paddle.move_up)
screen.onkeypress(key="s",fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -270:
        ball.bounce_y()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 320  or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 370:
        ball.reset()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        scoreboard.update_scoreboard()


    screen.update()

screen.exitonclick()