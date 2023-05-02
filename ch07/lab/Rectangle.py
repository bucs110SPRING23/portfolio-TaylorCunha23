class Rectangle:
    def __init__(self, x, y, height, width):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(height)
        self.width = abs(width)

    def __str__(self):
        return f"The rectangle's x coordinate is {self.x}, y coordinate is {self.y}, height is {self.height}, and width is {self.width}"

