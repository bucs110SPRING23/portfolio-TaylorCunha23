import pygame
pygame.init()

screen = pygame.display.set_mode()
screen = pygame.display.set_mode()
screen.fill("light blue")
pygame.display.flip()
pygame.time.wait(1000)


screen_size = screen.get_size()

pygame.draw.circle(screen,"white", (1000,270), 100, width= 0)

pygame.draw.circle(screen, "white", (1000,500), 150, width= 0)

pygame.draw.circle(screen, "white", (1000,800), 200, width= 0)

pygame.display.flip()
input()
