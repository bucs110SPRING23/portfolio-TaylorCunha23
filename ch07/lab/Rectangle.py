class Rectangle:
    x = 0
    y = 0
    height = 20
    width = 50
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.height = h
        self.width = w
    def __str__(self):
        return f"The rectangle's x coordinate is {self.x}, y coordinate is {self.y}, height is {self.height}, and width is {self.width}"
myRectangle = Rectangle(0, 0, 20, 50)
print(myRectangle.__str__())
print(myRectangle)
print(str(myRectangle))
print(myRectangle.__repr__())

