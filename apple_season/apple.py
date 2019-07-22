from os.path import join, dirname
import sys
import random

cwd = dirname(dirname(__file__))

if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.coords import Coords, Image, Char


apple_string = """  /
/ \\
\_/"""

apple_grid = [list(row) for row in apple_string.split('\n')]

chars = []
for r, row in enumerate(apple_grid):
    for x, char in enumerate(row):
        chars.append(Char(x, len(apple_grid) - 1 - r, char))

apple_image = Image(chars)


class Apple(Coords):

    def __init__(self, canvas, basket):

        self.basket = basket

        y = canvas.height
        x = random.randint(1, canvas.width - 4)

        self.has_fallen = False
        self.caught = False

        Coords.__init__(self, x, y, apple_image, canvas)


    def end(self):

        new_grid = [[' ' for i in range(3)] for x in range(3)]
        new_image_chars = []
        for r, row in enumerate(new_grid):
            for x, char in enumerate(row):
                new_image_chars.append(Char(x, len(new_grid) - 1 - r, char))
        self.image = Image(new_image_chars)
        self.has_fallen = True

    def fall(self):

        self.previous_y = self.y
        self.y -= 1

        if self.y <= 0:
            self.end()

    def check_caught(self):

        basket_char_coords = set(
            [(char.x + self.basket.x, char.y + self.basket.y) 
            for char in self.basket.image.chars])
        self_char_coords = set(
            [(char.x + self.x, char.y + self.y) 
            for char in self.image.chars])

        overlapping = bool(basket_char_coords & self_char_coords != set())

        if overlapping:
            self.caught = True
            self.end()
