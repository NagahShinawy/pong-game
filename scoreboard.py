"""
created by Nagaj at 22/05/2021
"""
from config import TurtleConfig
from constants import CENTER, DEFAULT_TURTLE, CENTER_TEXT, DEFAULT_FONT, GAME_OVER, SCORE_INFO, WINNER_FONT


class ScoreBoard(TurtleConfig):

    def __init__(self, shape=DEFAULT_TURTLE, position=CENTER, *args, **kwargs):
        self.right_score = 0
        self.left_score = 0
        self.score_info = SCORE_INFO
        super().__init__(shape, position, *args, **kwargs)

    def create(self, shape, position):
        super().create(shape, position)
        self.hideturtle()
        self.update_dashboard(text=self.updated_scores())

    def updated_scores(self):
        return self.score_info.format(self.left_score, self.right_score)

    def update_dashboard(self, text, font=DEFAULT_FONT):
        self.clear()
        self.write(text,  align=CENTER_TEXT, font=font)

    def round_to_right(self):
        """
        right win the round
        :return:
        """
        self.right_score += 1
        self.update_dashboard(self.updated_scores())

    def round_to_left(self):
        """
        left win the round
        :return:
        """
        self.left_score += 1
        self.update_dashboard(self.updated_scores())

    def is_finished(self):
        return self.right_score == GAME_OVER or self.left_score == GAME_OVER

    def show_winner(self):
        """
        who won the game left or right ?
        :return:
        """
        if self.right_score > self.left_score:
            winner = f"RIGHT IS THE WINNER {self.updated_scores()}"
        else:
            winner = f"LEFT IS THE WINNER {self.updated_scores()}"
        self.update_dashboard(text=winner, font=WINNER_FONT)
