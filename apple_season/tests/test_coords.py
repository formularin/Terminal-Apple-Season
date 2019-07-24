# these tests will most likely fail if run, because my code has changed a lot since I wrote these

import unittest
from os.path import join, dirname
import sys

cwd = dirname(dirname(dirname(__file__)))
if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season import coords
from apple_season.apple import apple_image


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
