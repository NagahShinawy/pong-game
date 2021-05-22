"""
created by Nagaj at 22/05/2021
"""
from config import TurtleConfig
from constants import END_OF_UP_WALL, END_OF_DOWN_WALL, CENTER
from paddle import Paddle


class Ball(TurtleConfig):

    def __init__(self, shape, position=CENTER, *args, **kwargs):
        super().__init__(shape, position, *args, **kwargs)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def is_collision_with_walls_up_or_down(self):
        return self.ycor() >= END_OF_UP_WALL or self.ycor() <= END_OF_DOWN_WALL

    def bounce(self):  # revert y when collision with up/down wall
        self.y_move *= -1

    def is_collision_with_right_paddle(self, right_paddle: Paddle):
        return self.distance(right_paddle) < 50 and self.xcor() >= 327

    def is_collision_with_left_paddle(self, left_paddle: Paddle):
        return self.distance(left_paddle) < 50 and self.xcor() <= -327

    def bounce_paddle(self):  # revert x when collision with paddle
        self.x_move *= -1

