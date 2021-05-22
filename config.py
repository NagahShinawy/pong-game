"""
created by Nagaj at 21/05/2021
"""
from turtle import Screen, Turtle

from constants import WIDTH, HEIGHT, BLACK, SCREEN_TITLE, WHITE, FASTEST, CENTER


def screen_setup():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BLACK)
    screen.title(SCREEN_TITLE)
    screen.tracer(0)  # stop/ turn of animation
    return screen


class TurtleConfig(Turtle):

    def __init__(self, shape, position=CENTER, *args, **kwargs):
        super(TurtleConfig, self).__init__(*args, **kwargs)
        self.create(shape, position)

    def create(self, shape, position):
        self.shape(shape)
        self.color(WHITE)
        self.penup()
        self.speed(FASTEST)
        self.goto(position)

