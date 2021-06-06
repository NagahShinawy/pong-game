"""
created by Nagaj at 21/05/2021
"""
import time

from ball import Ball
from config import screen_setup
from constants import (
    RIGHT_UP,
    RIGHT_DOWN,
    LEFT_UP,
    LEFT_DOWN,
    RIGHT_PADDLE_POSITION,
    LEFT_PADDLE_POSITION,
    CIRCLE,
    SQUARE,
    SCORE_POSITION,
)
from paddle import Paddle
from scoreboard import ScoreBoard

# ############### ############### ############### ##############

screen = screen_setup()

# ############### ############### ############### ##############
right_paddle = Paddle(shape=SQUARE, position=RIGHT_PADDLE_POSITION)
left_paddle = Paddle(shape=SQUARE, position=LEFT_PADDLE_POSITION)
ball = Ball(shape=CIRCLE)
scoreboard = ScoreBoard(position=SCORE_POSITION)
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
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if scoreboard.is_finished():
            scoreboard.show_winner()
            is_game_on = False

        if ball.is_missed_left():
            ball.reset_position()
            scoreboard.round_to_right()

        if ball.is_missed_right():
            ball.reset_position()
            scoreboard.round_to_left()

        if (
                ball.is_collision_with_walls_up_or_down()
        ):  # detect collision with wall up or down
            ball.bounce_y()
        if ball.is_collision_with_right_paddle(
                right_paddle
        ) or ball.is_collision_with_left_paddle(left_paddle):
            ball.bounce_x()


def main():
    play()
    screen.exitonclick()


if __name__ == "__main__":
    main()
