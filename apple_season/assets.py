from copy import deepcopy


class Canvas:
    """Canvas for displaying coords objects"""

    def replace(self, x, y, char):
        """Replaces a char with other char at certain location on canvas"""

        if len(char) != 1:
            raise ValueError('can only replace one char at a time')

        self.grid[self.height - 1 - y][x] = char

    def __init__(self, width, height):

        self.width = width
        self.height = height
        
        self.grid = [[' ' for x in range(self.width)] for y in range(self.height)]

        for i, char in enumerate(reversed('press "q" to quit'), 1):
            self.replace(self.width - i, self.height - 1, char)

        # permanent grid of what is behind the images
        self.background = deepcopy(self.grid)

        
    @property
    def display(self):
        """Returns string representation of current state"""
        return '\n'.join([''.join(i) for i in self.grid])


class Char:
    """A single character that is part of an Image"""

    def __init__(self, x, y, char):

        self.x = x
        self.y = y
        self.char = char  # string


class Image:
    """A collection of chars that create an object in the game"""

    def __init__(self, chars):

        self.chars = chars


def image_from_string(string):
    """Converts string to image object."""

    # create Char object for each character in string
    grid = [list(row) for row in string.split('\n')]
    chars = []
    for r, row in enumerate(grid):
        for x, char in enumerate(row):
            chars.append(Char(x, len(grid) - 1 - r, char))

    # combine chars into Image object
    image = Image(chars)

    return image

BASKET_STRING = """\------------------/
 \                /
  \              /
   \____________/"""

BASKET_IMAGE = image_from_string(BASKET_STRING)

# strings containing different states of apples
# (different points in rotation cycle)
APPLE_STRINGS = [
    "  /\n/ \\\n\\_/",
    "/ \\\n\\_/\\",
    "/ \\\n\\_/\n/",
    "\\/ \\\n \\_/"
]

APPLE_IMAGES = [image_from_string(state) for state in APPLE_STRINGS]

TITLE_SCREEN = """     ___      _____    _____            _______
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