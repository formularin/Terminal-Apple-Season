from os.path import join, dirname
import sys

cwd = dirname(dirname(__file__))

if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.coords import Coords


with open(join(cwd, 'images/basket.txt'), 'r') as f:
    BASKET_IMAGE = f.read()


class Basket(Coords):

    def __init__(self, canvas):
        Coords.__init__(self, 0, 0, BASKET_IMAGE, canvas)


    def move(self, direction):
        
        if direction == "right":
            self.x += 1

        elif direction == "left":
            self.x -= 1
