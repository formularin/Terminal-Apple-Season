class Canvas:
    """Canvas for displaying coords objects"""

    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        self.grid = [[' ' for x in width] for y in height]
        
    @property
    def display(self):
        """Returns string representation of current state"""
        return '\n'.join([''.join(i) for i in self.grid])

    def replace(self, x, y, char):
        """Replaces a char with other char at certain location on canvas"""
        self.grid[y][x] = char


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

            self.canvas.replace(canvas_x, canvas_y, ' ')
        
        # add new rendering on canvas
        for char in self.image.chars:
            
            # location of char on canvas
            canvas_x = char.x + self.x
            canvas_y = char.y + self.y

            self.canvas.replace(canvas_x, canvas_y, char.char)
