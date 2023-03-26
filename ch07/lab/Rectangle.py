class Rectangle:
    x = 0
    y = 0
    height = 20
    width = 50
    def __init__(self, xcoordinate, ycoordinate, height, width):
        self.x = xcoordinate
        self.y = ycoordinate
        self.height = height
        self.width = width
    def __str__(self):
        return f"The rectangle's x coordinate is {self.x}, y coordinate is {self.y}, height is {self.height}, and width is {self.width}"
myRectangle = Rectangle(0, 0, 20, 50)
print(myRectangle.__str__())
print(myRectangle)
print(str(myRectangle))
print(myRectangle.__repr__())

