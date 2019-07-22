from os.path import join, dirname
import sys
import random
import logging

cwd = dirname(dirname(__file__))

if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.coords import Coords, Image, Char


logging.basicConfig(filename='apple.log', level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s: %(message)s')

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

        logging.debug(f'Apple Created at coords ({self.x}, {self.y})')

    def end(self):

        new_grid = [[' ' for i in range(3)] for x in range(3)]
        new_image_chars = []
        for r, row in enumerate(new_grid):
            for x, char in enumerate(row):
                new_image_chars.append(Char(x, len(new_grid) - 1 - r, char))
        self.image = Image(new_image_chars)
        self.has_fallen = True
        logging.debug(f'Apple has fallen at coords ({self.x}, {self.y})')

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
            logging.info(f'basket coords: {basket_char_coords}')
            logging.info(f'apple_coords: {self_char_coords}')
            logging.info(f'apple caught with overlap coords: ({basket_char_coords & self_char_coords})')
            self.caught = True
            self.end()
