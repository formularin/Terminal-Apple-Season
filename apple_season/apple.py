from os.path import join, dirname
import sys
import random

cwd = dirname(dirname(__file__))

if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.coords import Coords, Image, Char


with open(join(cwd, 'images/apple.txt'), 'r') as f:
    apple_string = f.read()

apple_grid = [list(row) for row in apple_string.split('\n')]

chars = []
for r, row in enumerate(apple_grid):
    for x, char in enumerate(row):
        chars.append(Char(x, len(apple_grid) - 1 - r, char))

apple_image = Image(chars)


class Apple(Coords):

    def fall(self):

        while self.y > 0:
            self.previous_y = self.y
            self.y -= 2

        self.image = '   \n   \n   '

    def __init__(self, canvas):

        y = canvas.height
        x = random.randint(0, canvas.width)

        Coords.__init__(self, x, y, apple_image, canvas)

        self.fall()


