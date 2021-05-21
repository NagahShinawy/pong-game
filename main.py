"""
created by Nagaj at 21/05/2021
"""

from config import screen_setup
from paddle import Paddle
from constants import UP, DOWN, LEFT_PADDLE_POSITION


screen = screen_setup()
right_paddle = Paddle()
left_paddle = Paddle(LEFT_PADDLE_POSITION)
screen.listen()
screen.update()


def play():
    is_game_on = True
    while is_game_on:
        screen.update()
        screen.onkey(key=UP, fun=right_paddle.to_up)
        screen.onkey(key=DOWN, fun=right_paddle.to_down)

    screen.exitonclick()


if __name__ == '__main__':
    play()
