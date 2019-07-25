from os.path import dirname, join
import sys

cwd = dirname(dirname(__file__))
if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.coords import Coords
from apple_season.assets import BASKET_IMAGE, Char, Image


class Basket(Coords):
    """Basket to catch apples. Controlled by left and right arrow keys."""

    def __init__(self, canvas):

        # initialize as Coords object as well as Basket
        Coords.__init__(self, int(canvas.width / 2), 2, BASKET_IMAGE, canvas)


    def move(self, direction):
        """Moves 5 spaces either left or right.
        Called on left and right arrow click events"""

        self.previous_x = self.x
        self.previous_y = self.y

        if direction == "right":

            # quit function if off the right edge
            for char in self.image.chars:
                if char.x + self.x + 5 > self.canvas.width:
                    return

            self.x += 5

        elif direction == "left":
            
            # quit function if off the left edge
            for char in self.image.chars:
                if char.x + self.x - 5 < 0:
                    return

            self.x -= 5
