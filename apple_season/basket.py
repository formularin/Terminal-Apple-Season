from os.path import join, dirname
import sys

cwd = dirname(dirname(__file__))

if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.coords import Coords, Image, Char


with open(join(cwd, 'images/basket.txt'), 'r') as f:
    basket_string = f.read()

basket_grid = [list(row) for row in basket_string.split('\n')]

chars = []
for r, row in enumerate(basket_grid):
    for x, char in enumerate(row):
        chars.append(Char(x, len(basket_grid) - 1 - r, char))

basket_image = Image(chars)


class Basket(Coords):

    def __init__(self, canvas):

        Coords.__init__(self, int(canvas.width / 2), 1, basket_image, canvas)


    def move(self, direction):
        
        self.previous_x = self.x
        self.previous_y = self.y

        if direction == "right":
            self.x += 5

        elif direction == "left":
            self.x -= 5
