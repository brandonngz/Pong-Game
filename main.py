from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score, Lines
import time


# Set up the screen
screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# Create the paddles
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))

# Ball
ball = Ball()
scoreboard = Score()

# Draw the game area
lines = Lines()

screen.listen()
screen.onkeypress(key="u", fun=r_paddle.up)
screen.onkeypress(key="j", fun=r_paddle.down)
screen.onkeypress(key="r", fun=l_paddle.up)
screen.onkeypress(key="f", fun=l_paddle.down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # once the bounce function get triggered, the Y coordinate is now -10
        ball.bounce_y()

    # Detecting collisions with the paddle
    b_dis_r = ball.distance(r_paddle)
    b_dis_l = ball.distance(l_paddle)
    if b_dis_r < 50 and ball.xcor() > 330 or b_dis_l < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Restart the ball at the center and moving towards the other player.
    if ball.xcor() == 420:
        ball.goto_start(-1, -1)
        scoreboard.point_user_l()
    elif ball.xcor() == -420:
        ball.goto_start(-1, 1)
        scoreboard.point_user_r()




screen.exitonclick()

