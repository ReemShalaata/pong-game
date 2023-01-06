from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

HEIGHT=600
WIDTH=800

screen=Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

r_paddle=Paddle(position=(350,0))
l_paddle=Paddle(position=(-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Coliision with the right paddle and left paddle
    if  (ball.xcor()>330 and ball.distance(r_paddle) < 52) or (ball.xcor()<-330 and ball.distance(l_paddle) < 52):
        ball.bounce_x()

    #out of bounds
    if ball.xcor()>380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor()<-380:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()