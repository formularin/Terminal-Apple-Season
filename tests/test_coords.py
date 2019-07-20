import unittest
from os.path import join, dirname
import sys

cwd = dirname(dirname(__file__))
if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season import coords


with open(join(cwd, 'images/apple.txt'), 'r') as f:
    apple_string = f.read()

apple_grid = [list(row) for row in apple_string.split('\n')]

chars = []
for r, row in enumerate(apple_grid):
    for x, char in enumerate(row):
        chars.append(coords.Char(x, len(row) - 1 - r, char))

apple_image = coords.Image(chars)


class TestCanvas(unittest.TestCase):

    def test_display(self):

        canvas = coords.Canvas(10, 10)

        self.assertEqual(canvas.display, '\n'.join(['          ' for _ in range(10)]))

    def test_replace(self):

        canvas = coords.Canvas(5, 5)
        canvas.replace(0, 0, '/')
        self.assertEqual(canvas.display, '     \n     \n     \n     \n/    ')

        with self.assertRaises(ValueError):
            canvas.replace(1, 1, 'apple')


class TestCoords(unittest.TestCase):

    def test_render(self):
        
        canvas = coords.Canvas(3, 3)
        apple = coords.Coords(0, 0, apple_image, canvas)

        apple.render()

        self.assertEqual(canvas.display, '  /\n/ \\\n\\_/')


if __name__ == '__main__':
    unittest.main()
