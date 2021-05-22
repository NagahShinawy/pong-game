"""
created by Nagaj at 21/05/2021
"""
from config import TurtleConfig

from constants import (
    PADDLE_WIDTH,
    PADDLE_LEN,
    MOVE_BY,
    HEIGHT,
)


class Paddle(TurtleConfig):
    def create(self, shape, position):
        super().create(shape, position)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LEN)

    @property
    def is_free_to_move_up(self):
        return self.ycor() < (HEIGHT // 2) - 60

    @property
    def is_free_to_move_down(self):
        return self.ycor() > (-HEIGHT // 2) + 60

    def to_up(self):
        if self.is_free_to_move_up:
            self.goto(x=self.xcor(), y=self.ycor() + MOVE_BY)

    def to_down(self):
        if self.is_free_to_move_down:
            self.goto(x=self.xcor(), y=self.ycor() - MOVE_BY)

    def win(self):
        pass
