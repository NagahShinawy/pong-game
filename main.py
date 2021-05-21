"""
created by Nagaj at 21/05/2021
"""

from config import screen_setup
from paddle import Paddle
from constants import RIGHT_UP, RIGHT_DOWN, LEFT_UP, LEFT_DOWN, LEFT_PADDLE_POSITION


screen = screen_setup()
right_paddle = Paddle()
left_paddle = Paddle(LEFT_PADDLE_POSITION)
screen.listen()
screen.update()


def play():
    is_game_on = True
    while is_game_on:
        screen.update()
        screen.onkey(key=RIGHT_UP, fun=right_paddle.to_up)
        screen.onkey(key=RIGHT_DOWN, fun=right_paddle.to_down)
        screen.onkey(key=LEFT_UP, fun=left_paddle.to_up)
        screen.onkey(key=LEFT_DOWN, fun=left_paddle.to_down)

    screen.exitonclick()


if __name__ == '__main__':
    play()
