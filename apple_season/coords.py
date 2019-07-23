class Canvas:
    """Canvas for displaying coords objects"""

    def replace(self, x, y, char):
        """Replaces a char with other char at certain location on canvas"""

        if len(char) != 1:
            raise ValueError('can only replace one char at a time')

        self.grid[len(self.grid) - 1 - y][x] = char

    def __init__(self, width, height):

        self.width = width
        self.height = height
        
        self.grid = [[' ' for x in range(self.width)] for y in range(self.height)]

        for i, char in enumerate(reversed('press "q" to quit'), 1):
            self.replace(self.width - i, self.height - 1, char)

        
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


class Coords:
    """An object with a location on the canvas"""

    def __init__(self, x, y, image, canvas):  # x and y are represented by bottom-left most char in Coords object design
        
        self.canvas = canvas  # Canvas Object
        self.image = image  # Image object
        self.x = x
        self.y = y
        self.previous_x = self.x
        self.previous_y = self.y

    def render(self):
        """Alter canvas to display coords object in its current position"""

        # clear previous rendering on canvas
        for char in self.image.chars:
            
            # location of previous char on canvas
            canvas_x = char.x + self.previous_x
            canvas_y = char.y + self.previous_y

            try:
                self.canvas.replace(canvas_x, canvas_y, ' ')
            except IndexError:
                pass
        
        # add new rendering on canvas
        for char in self.image.chars:
            
            # location of char on canvas
            canvas_x = char.x + self.x
            canvas_y = char.y + self.y

            try:
                self.canvas.replace(canvas_x, canvas_y, char.char)
            except IndexError:
                pass
