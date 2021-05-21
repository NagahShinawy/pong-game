"""
created by Nagaj at 21/05/2021
"""
from turtle import Turtle

from constants import (
    PADDLE_WIDTH,
    PADDLE_LEN,
    RIGHT_PADDLE_POSITION,
    WHITE,
    SQUARE,
    MOVE_BY,
    HEIGHT,
    FASTEST,
)


class Paddle(Turtle):
    def __init__(self, position=RIGHT_PADDLE_POSITION):
        super().__init__()
        self.create(position)

    def create(self, position):
        self.shape(SQUARE)
        self.color(WHITE)
        self.penup()
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LEN)
        self.speed(FASTEST)
        self.goto(position)

    @property
    def is_free_to_move_up(self):
        return self.ycor() < (HEIGHT // 2) - 60

    @property
    def is_free_to_move_down(self):
        return self.ycor() > (- HEIGHT // 2) + 60

    def to_up(self):
        if self.is_free_to_move_up:
            self.goto(x=self.xcor(), y=self.ycor() + MOVE_BY)

    def to_down(self):
        if self.is_free_to_move_down:
            self.goto(x=self.xcor(), y=self.ycor() - MOVE_BY)
