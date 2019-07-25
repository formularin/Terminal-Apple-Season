from apple_season.assets import APPLE_IMAGES, Char, Image


class Coords:
    """An object with a location on the canvas"""

    def __init__(self, x, y, image, canvas):  # x and y are represented by bottom-left most char in Coords object design
        
        self.canvas = canvas  # Canvas Object
        self.image = image  # Image object
        self.x = x
        self.y = y
        self.previous_x = self.x
        self.previous_y = self.y

    def render(self, image_has_rotated=False):
        """Alter canvas to display coords object in its current position"""

        previous_image = self.image

        # clear previous rendering on canvas
        if str(type(self)) == "<class 'apple_season.apple.Apple'>":
            if not self.has_fallen:
                if image_has_rotated:
                    previous_image = APPLE_IMAGES[APPLE_IMAGES.index(self.image) - 1]

        for char in previous_image.chars:

            # location of previous char on canvas
            canvas_x = char.x + self.previous_x
            canvas_y = char.y + self.previous_y

            bg_char = self.canvas.background[self.canvas.height - 1 - canvas_y][canvas_x]

            try:
                self.canvas.replace(canvas_x, canvas_y, bg_char)
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
