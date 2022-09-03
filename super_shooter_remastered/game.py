"""
Remake of my Pyweek 33 entry in Arcade
"""

from constants import *
from sprites.player_sprite import Player
from sprites.zombie_sprite import Zombie

from loguru import logger

import arcade


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background_color = arcade.color.CORNFLOWER_BLUE

        self.player: Player = None

        self.scene: arcade.Scene = None
        self.camera: arcade.Camera = None

        self.tile_map: arcade.TileMap = None

        self.physics_engine: arcade.PymunkPhysicsEngine = None

        self.setup()

    def setup(self):
        """Set up the game"""

        # Set main camera
        self.camera = arcade.Camera(self.width, self.height)

        # Set up the tile map
        map_path = PATHS["levels"] / "level1.tmx"
        layer_options = {
            "Walls": {"use_spatial_hash": True},
            "Zombies": {"custom_class": Zombie},
            "Player": {"custom_class": Player},
        }

        tile_scaling = 1.0

        self.tile_map = arcade.load_tilemap(map_path, tile_scaling, layer_options)

        # Set up the scene
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Set up the physics engine
        self.physics_engine = arcade.PymunkPhysicsEngine()

    def on_draw(self):
        """Render the screen"""

        self.clear()

        self.scene.draw()

    def on_update(self, delta_time: float):
        """All the logic to move, and the game logic goes here"""

        self.scene.update()

        self.physics_engine.step()

        self.camera.update()
