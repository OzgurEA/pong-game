
import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = t.Screen()

screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(800, 600)
screen.tracer(0)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.moving_ball()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.paddle_bounce()

    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
