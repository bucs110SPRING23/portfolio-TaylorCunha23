class Surface:
    def __init__(self, filename, Rectangle, x, y, h, w):
        self.image = filename
        self.rect = Rectangle
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    def getRect(self):
        return self.rect
        r1 = Rectangle('name', 0, 0, 20, 50)


#def main():
#def rectangle(self):