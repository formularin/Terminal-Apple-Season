from os.path import join, dirname
import sys

cwd = dirname(dirname(__file__))

if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.coords import Coords, Image, Char


basket_string = """\------------------/
 \                /
  \              /
   \____________/"""

basket_grid = [list(row) for row in basket_string.split('\n')]

chars = []
for r, row in enumerate(basket_grid):
    for x, char in enumerate(row):
        chars.append(Char(x, len(basket_grid) - 1 - r, char))

basket_image = Image(chars)


class Basket(Coords):

    def __init__(self, canvas):

        Coords.__init__(self, int(canvas.width / 2), 0, basket_image, canvas)


    def move(self, direction):

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
