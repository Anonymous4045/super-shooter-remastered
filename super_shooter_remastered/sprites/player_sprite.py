"""
The player class
"""

from constants import *

import arcade


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(PATHS["sprites"] / "player.png")

        self.setup()

    def setup(self):
        self.position = (32 * 2, 32 * 3)
