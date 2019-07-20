from os.path import join, dirname
import sys

cwd = dirname(dirname(__file__))
if cwd not in sys.path:
    sys.path.append(cwd)

from curses import wrapper

from apple_season.basket import Basket
from apple_season.coords import Canvas


canvas = Canvas(50, 50)
basket = Basket(canvas)


def main(stdscr):

    stdscr.nodelay(True)
    key=""
    stdscr.clear()

    while True:
        try:
            basket.render()
            key = stdscr.getkey()
            stdscr.clear()
            stdscr.addstr(canvas.display)
            stdscr.refresh()

            # quit option
            if str(key) == "q":
               break

            # right arrow
            elif str(key) == "KEY_RIGHT":
                basket.move('right')

            # left arrow
            elif str(key) == "KEY_LEFT":
                basket.move('left')

        except Exception as e:
            
            with open('test.log', 'a') as f:
                f.write(f'\n{e}')

if __name__ == "__main__":
    wrapper(main)
