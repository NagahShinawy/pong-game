"""
created by Nagaj at 21/05/2021
"""
import time

from config import screen_setup
from paddle import Paddle
from ball import Ball
from constants import (
    RIGHT_UP,
    RIGHT_DOWN,
    LEFT_UP,
    LEFT_DOWN,
    RIGHT_PADDLE_POSITION,
    LEFT_PADDLE_POSITION,
    CIRCLE,
    SQUARE,
)

# ############### ############### ############### ##############

screen = screen_setup()

# ############### ############### ############### ##############
right_paddle = Paddle(shape=SQUARE, position=RIGHT_PADDLE_POSITION)
left_paddle = Paddle(shape=SQUARE, position=LEFT_PADDLE_POSITION)
ball = Ball(shape=CIRCLE)

# ############## # ############### ############### ##############
screen.listen()
screen.onkey(key=RIGHT_UP, fun=right_paddle.to_up)
screen.onkey(key=RIGHT_DOWN, fun=right_paddle.to_down)
screen.onkey(key=LEFT_UP, fun=left_paddle.to_up)
screen.onkey(key=LEFT_DOWN, fun=left_paddle.to_down)

# ############### ############### ############### ##############


def play():
    is_game_on = True
    while is_game_on:
        time.sleep(0.1)
        screen.update()
        ball.move()
        if ball.is_collision_with_walls_up_or_down():   # detect collision with wall up or down
            ball.bounce()
        if ball.is_collision_with_right_paddle(right_paddle):
            ball.bounce_paddle()
        if ball.is_collision_with_left_paddle(left_paddle):
            ball.bounce_paddle()
    screen.exitonclick()


if __name__ == "__main__":
    play()
