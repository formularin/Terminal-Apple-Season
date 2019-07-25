from os.path import join, dirname
import random
import sys

cwd = dirname(dirname(__file__))
if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.coords import Coords
from apple_season.assets import APPLE_IMAGES, Char, Image


class Apple(Coords):
    """An Apple that you're supposed to catch with the basket."""

    def __init__(self, canvas, basket):

        self.basket = basket

        # initialize apple at any point at the top of the screen
        # between zero and 'press "q" to quit' text
        y = canvas.height - 2
        x = random.randint(1, canvas.width - 21)

        self.has_fallen = False
        self.caught = False
        self.frame = 0

        # initialize as Coords object as well as Apple
        Coords.__init__(self, x, y, APPLE_IMAGES[0], canvas)


    def end(self):
        """Turns image into a 3x3 grid of blank spaces
        and changes has_fallen attribute to True"""

        new_grid = [[' ' for i in range(3)] for x in range(3)]
        new_image_chars = []
        for r, row in enumerate(new_grid):
            for x, char in enumerate(row):
                new_image_chars.append(Char(x, len(new_grid) - 1 - r, char))
        self.image = Image(new_image_chars)
        self.has_fallen = True

    def fall(self):
        """Moves apple down 1 line. Ends if apple has fallen"""

        self.previous_y = self.y
        self.y -= 1

        if not self.has_fallen:
            # change image to rotate apple
            new_index = APPLE_IMAGES.index(self.image) + 1
            if new_index == 4:
                new_index = 0
            self.image = APPLE_IMAGES[new_index]

        if self.y <= 0:
            self.end()

    def check_caught(self):
        """Checks to see if apple has been caught.
        Returns Boolean and ends if caught"""
        
        # x values for basket and apple
        basket_char_coords = set([char.x + self.basket.x for char in self.basket.image.chars])
        self_char_coords = set([char.x + self.x for char in self.image.chars])

        overlapping = bool(basket_char_coords & self_char_coords != set())

        if overlapping:
            self.caught = True
            self.end()
            return True
        else:
            return False
