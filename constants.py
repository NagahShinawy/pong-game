"""
created by Nagaj at 21/05/2021
"""

# ########  SCREEN  #################
WIDTH = 800
HEIGHT = 600
BLACK = "black"
SCREEN_TITLE = "Pong Game"

# ########   PADDLE    #################
SQUARE = "square"
WHITE = "white"
FASTEST = "fastest"
PADDLE_WIDTH = 5
PADDLE_LEN = 1
RIGHT_PADDLE_POSITION = ((WIDTH // 2) - 50, 0)    # 350
LEFT_PADDLE_POSITION = ((-WIDTH // 2) + 50, 0)    # -350
MOVE_BY = 20

# #########  KEYS #############
RIGHT_UP = "Up"
RIGHT_DOWN = "Down"

LEFT_UP = "w"
LEFT_DOWN = "s"

# ######## BALL  ################
CIRCLE = "circle"
CENTER = (0, 0)
MISSED_RIGHT = 380
MISSED_LEFT = -380
# ######### WALL ##############
END_OF_UP_WALL = (HEIGHT // 2) - 20
END_OF_DOWN_WALL = (-HEIGHT // 2) + 20
