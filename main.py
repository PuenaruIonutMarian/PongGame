from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))

left_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(key="Up", fun=right_paddle.go_up)
screen.onkeypress(key="Down", fun=right_paddle.go_down)
screen.onkeypress(key="w", fun=left_paddle.go_up)
screen.onkeypress(key="s", fun=left_paddle.go_down)


ball = Ball()

game_is_on = True

while game_is_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
