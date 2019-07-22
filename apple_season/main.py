from os.path import join, dirname
import sys
import random
import time
import curses
import logging

cwd = dirname(dirname(__file__))
if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.basket import Basket
from apple_season.apple import Apple
from apple_season.coords import Canvas


logging.basicConfig(filename='apple.log', level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s: %(message)s')


def main(stdscr):

    curses.curs_set(0)
    dims = [curses.COLS - 1, curses.LINES - 1]  # pylint: disable=no-member
    logging.info(f'terminal dims - width: {curses.COLS - 1} and height: {curses.LINES - 1}')  # pylint: disable=no-member

    stdscr.nodelay(True)
    stdscr.leaveok(True)
    key=""
    stdscr.clear()

    canvas = Canvas(*dims)

    logging.debug(f'canvas created with width: {canvas.width} and height: {canvas.height}')

    basket = Basket(canvas)

    apples = []
    i = 0

    def finished_apples():
      if len(apples) <= 100:
         return False
      else:
         for apple in apples:
            if not apple.has_fallen:
               return False
         return True

    while not finished_apples():



        if len(apples) <= 100:  # don't make more if there are already 100
            # decide whether or not to create new apple (1/100 chance per frame)
            num = random.randint(0, 100)
            if num == 25:
                apples.append(Apple(canvas))

        stdscr.clear()

        try:
            key = stdscr.getkey()
            
            # pick up keyboard inputs
            # quit option
            if str(key) == "q":
                break

            # right arrow
            elif str(key) == "KEY_RIGHT":
                basket.move('right')

            # left arrow
            elif str(key) == "KEY_LEFT":
                basket.move('left')

        except Exception:
            pass

        for apple in apples:
            if apple.has_fallen:
                apple.render()
            else:
                if '.0' not in str(i / 2):  # check if i is even (drop every other frame)
                    apple.fall()
                    apple.render()

        # render objects
        basket.render()

        try:
            stdscr.addstr(canvas.display)
            
        except Exception:
            logging.error(f'cursor position: {str(stdscr.getyx())}')

        stdscr.refresh()
        i += 1
        time.sleep(0.01)

if __name__ == "__main__":
    curses.wrapper(main)
