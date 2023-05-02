from Rectangle import Rectangle
import pygame

class Surface:
    def __init__(self, filename, x, y, h, w):
        self.image = pygame.image.load(filename)
        self.rect = Rectangle(x, y, h, w)
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)

    def getRect(self):
        return self.rect

