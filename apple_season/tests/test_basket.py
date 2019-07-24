# these tests will most likely fail if run, because my code has changed a lot since I wrote these

import unittest
from os.path import join, dirname
import sys

cwd = dirname(dirname(dirname(__file__)))
if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season import basket
from apple_season import coords


class TestBasket(unittest.TestCase):

    def test_move(self):
        
        canvas = coords.Canvas(50, 50)
        b = basket.Basket(canvas)

        for i in range(20):
            b.render()
            with open(f'basket/{i}.txt', 'w+') as f:
                f.write(canvas.display)
            b.move("right")

        self.assertEqual(b.x, 20)
        self.assertEqual(b.previous_x, 19)


if __name__ == '__main__':
    unittest.main()
