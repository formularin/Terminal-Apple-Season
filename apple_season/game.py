from os.path import join, dirname, abspath
import sys
import random
import time
import curses

cwd = dirname(dirname(abspath(__file__)))
if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.basket import Basket
from apple_season.apple import Apple
from apple_season.coords import Canvas


title_screen = """     ___      _____    _____            _______
    /   \    |     |  |     | |        |
   /_____\   |_____|  |_____| |        |____
  /       \  |        |       |        |
 /         \ |        |       |_______ |_______
 ____   ______     ___     _____   _____
|      |          /   \   |       |     | |\   |
|____  |____     /_____\  |_____  |     | | \  |
     | |        /       \       | |     | |  \ |
_____| |______ /         \ _____| |_____| |   \|

           ___        ______                               
           \  \      /     /                       
            \__\____/     / Press any key to start.
               /   /_____/  If nothing happens, raise an issue on     
              | O        |  https://github.com/lol-cubes/Terminal-Apple-Season/issues
              |          |
              |          |       
               \________/                         
                                                  """


def game_over(stdscr, caught_apples):

    missed_apples = 100 - caught_apples

    while True:
        stdscr.clear()
        stdscr.addstr(f'GAME OVER\nTotal: 100\nMissed: {missed_apples}\n__________\n\
Saves: {caught_apples}\n\n\nPress "q" to quit\nPress "a" to play again.')
        try:
            key = stdscr.getkey()
            if str(key) == "q":
                break
            if str(key) == "a":
                curses.wrapper(main)
                return
        except Exception:
            pass


def main(stdscr):

    curses.curs_set(0)
    dims = [curses.COLS - 1, curses.LINES - 1]  # pylint: disable=no-member

    stdscr.nodelay(True)
    stdscr.leaveok(True)
    key=""
    stdscr.clear()

    while True:
        stdscr.clear()
        try:
            stdscr.addstr(title_screen)
        except Exception:
            stdscr.clear()
            stdscr.addstr('Terminal window is too small. \n\
Quit the program by pressing "q" \n\
and start again in larger window.')
        try:
            key = stdscr.getkey()
            if str(key) == "q":
                sys.exit()
            break
        except Exception:
            pass

    canvas = Canvas(*dims)
    basket = Basket(canvas)

    apples = []
    frame = 0

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
            # decide whether or not to create new apple (1/50 chance per frame)
            num = random.randint(0, 50)
            if num == 25:
                apples.append(Apple(canvas, basket))

        stdscr.clear()

        try:
            key = stdscr.getkey()
            
            # pick up keyboard inputs
            # quit option
            if str(key) == "q":
                return

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
                if apple.y == basket.image.chars[0].y:
                    apple.check_caught()
                apple.fall()
                apple.render()
                
        # render objects
        basket.render()

        try:
            stdscr.addstr(canvas.display)
            
        except Exception:
            pass

        stdscr.refresh()
        time.sleep(0.02)
        frame += 1

    caught_apples = len([apple for apple in apples if apple.caught])

    curses.wrapper(game_over, caught_apples)
    return


curses.wrapper(main)
