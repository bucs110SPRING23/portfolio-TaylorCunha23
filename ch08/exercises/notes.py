import pygame

class Snowman(pygame. sprite. Sprite):
    def __init__(self,x,y,img="assets/snowman.png"): #img is not applicable based on this computer
        super().__init__()

        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y