"""
created by Nagaj at 21/05/2021
"""
from turtle import Screen
from constants import WIDTH, HEIGHT, BLACK, SCREEN_TITLE


def screen_setup():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BLACK)
    screen.title(SCREEN_TITLE)
    screen.tracer(0)  # stop/ turn of animation
    return screen
