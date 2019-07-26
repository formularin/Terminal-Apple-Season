import curses
from os.path import abspath, dirname, join
import random
import sys
import time

from playsound import playsound

cwd = dirname(dirname(abspath(__file__)))
if cwd not in sys.path:
    sys.path.append(cwd)

from apple_season.apple import Apple
from apple_season.assets import (Canvas, Image,
    TITLE_SCREEN, GAME_OVER_SCREEN, SMALL_WINDOW_MESSAGE, COUNTER)
from apple_season.basket import Basket
from apple_season.coords import Coords


def game_over(stdscr, caught_apples):
    """Contains mainloop for game over screen."""

    missed_apples = 100 - caught_apples

    stdscr.clear()
    stdscr.addstr(GAME_OVER_SCREEN % (missed_apples, caught_apples))

    while True:
        try:
            key = stdscr.getkey()
            if str(key) == "q":
                break
            if str(key) == "a":
                curses.wrapper(main)
                return
        except Exception:  # no input
            pass


def main(stdscr):
    """Contains mainloops for title screen and gameplay."""

    # don't see cursor
    curses.curs_set(0)

    # clear screen so it doesn't overflow
    stdscr.clear()

    screen_is_big_enough = False
    try:
        stdscr.addstr(TITLE_SCREEN)
        screen_is_big_enough = True

    except Exception:

        stdscr.clear()
        stdscr.addstr(SMALL_WINDOW_MESSAGE)

    # make input non-blocking, and add initialize key variable
    stdscr.nodelay(True)
    key=""

    while True: 
        try:
            key = stdscr.getkey()
            if str(key) == "q":
                sys.exit()
            if screen_is_big_enough:
                break
        except Exception:
            pass

    dims = [curses.COLS - 1, curses.LINES - 1]
    canvas = Canvas(*dims)
    basket = Basket(canvas)

    apples = []

    def finished_apples():
        """Checks to see if 100 apples have fallen."""
        if len(apples) <= 100:
            return False
        else:
            for apple in apples:
                if not apple.has_fallen:
                    return False
                else:
                    return True

    stdscr.clear()
    
    frame = 0

    while not finished_apples():

        if len(apples) <= 100:  # don't make more if there are already 100
            # decide whether or not to create new apple (1/25 chance per frame)
            num = random.randint(0, 25)
            if num == 10:
                apples.append(Apple(canvas, basket))

        try:
            # pick up keyboard inputs
            key = stdscr.getkey()
            
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
            
            if not apple.has_fallen:
                
                # if bottom of apple is on the same line as top of basket.
                if apple.y == basket.image.chars[0].y:
                    # play sound if apple caught
                    if apple.check_caught():
                        playsound(join(cwd, 'apple_season/caught.wav'), block=False)
                        apple.render()
                
                if not apple.has_fallen:
                    rotate = False
                    if '.0' in str(frame / 2):
                        rotate = True
                    
                apple.fall(rotate)

            if '.0' in str(frame / 2):
                apple.render(True)
            else:
                apple.render()
                
        # render objects
        basket.render()

        try:
            # update screen for current frame

            for i, char in enumerate(canvas.grid[-1]):
                canvas.replace(i, 1, '-')

            stdscr.clear()
            stdscr.addstr(canvas.display)
            stdscr.addstr(COUNTER % (
                len([apple for apple in apples if apple.caught]),
                len([apple for apple in apples if not apple.caught])))
            
        except Exception:
            pass

        stdscr.refresh()
        time.sleep(0.02)
        frame += 1

    # display game over screen
    caught_apples = len([apple for apple in apples if apple.caught])
    curses.wrapper(game_over, caught_apples)


curses.wrapper(main)
