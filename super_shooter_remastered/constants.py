"""
Variables that will be the same for all files
"""

from pathlib import Path


# Screen information
SCREEN_WIDTH = 32 * 30
SCREEN_HEIGHT = 32 * 20
SCREEN_TITLE = "Pyweek 33 Remake"

# Paths
PATHS = {
    # Root path
    "root": Path(__file__).parent.parent,
    # Assets path
    "assets": Path(__file__).parent.parent / "assets",
    "tiles": Path(__file__).parent.parent / "assets" / "tiles",
    "levels": Path(__file__).parent.parent / "assets" / "tiles" / "levels",
}
