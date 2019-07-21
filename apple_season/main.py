from os.path import join, dirname
import sys
import time

cwd = dirname(dirname(__file__))
if cwd not in sys.path:
    sys.path.append(cwd)

from curses import wrapper
from _curses import error as CursesError

from apple_season.basket import Basket
from apple_season.coords import Canvas


canvas = Canvas(100, 25)
basket = Basket(canvas)


def main(stdscr):

    stdscr.nodelay(True)
    key=""
    stdscr.clear()

    while True:

        try:
            key = stdscr.getkey()

            # quit option
            if str(key) == "q":
                break

            # right arrow
            elif str(key) == "KEY_RIGHT":
                basket.move('right')

            # left arrow
            elif str(key) == "KEY_LEFT":
                basket.move('left')
            
            basket.render()
            stdscr.clear()
            stdscr.addstr(canvas.display)
            stdscr.refresh()

        except Exception:
            pass

if __name__ == "__main__":
    wrapper(main)
