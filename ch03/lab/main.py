import pygame
import random
import math
pygame.init()
pygame.display.set_caption("Dartboard")
screen_width=1000
screen_height=1000
screen=pygame.display.set_mode([screen_width, screen_height])
screen.fill((153, 184, 152))
pygame.draw.circle(screen, (183, 152, 184), (500,500), 500, width=0)


pygame.draw.circle(screen, (0, 0, 0), (500,500), 500, width=3)
pygame.draw.line(screen, "black", (500,-1000), (500,1000), width=3)
pygame.draw.line(screen, "black", (0,500), (1000,500), width=3)
pygame.display.update()
message = """
        10 darts will be randomly thrown. 
        The darts that hit the target are in white. 
        The darts that miss the target are in red. 
        Press enter.
        """
response = input(message)

for darts in range(10):
    x = random.randrange(0,1000)
    y = random.randrange(0,1000)
    distance_from_center = math.hypot(x-500, y-500)
    is_in_circle = distance_from_center <= screen_width/2 #screen width
    print(distance_from_center, screen_width/2)
    print(is_in_circle)
    if is_in_circle:
        pygame.draw.circle(screen, (255,255,255), [x,y], 10)
    else:
        pygame.draw.circle(screen, (255, 0, 0), [x,y], 10) 
pygame.display.flip()
pygame.time.wait(10000)
# screen.fill((153, 184, 152))
# run = True
# while run:
#         dartgame = pygame.event.get()
#         for event in dartgame:
#             if event.type == pygame.MOUSEBUTTONUP:
#                 pygame.draw.circle(screen, (183, 152, 184), (500,500), 500, width=0)
#                 pygame.draw.circle(screen, (0, 0, 0), (500,500), 500, width=3)
#                 pygame.draw.line(screen, "black", (500,-1000), (500,1000), width=3)
#                 pygame.draw.line(screen, "black", (0,500), (1000,500), width=3)
#                 pygame.display.update()
#                 message = """
#                         Which player will win?
#                         To pick Player 1: Press 1
#                         To pick Player 2: Press 2
#                         """
#                 response = input(message)

#                 for darts in range(10):
#                     x1 = random.randrange(0,1000)
#                     y1 = random.randrange(0,1000)
#                     x2 = random.randrange(0,1000)
#                     y2 = random.randrange(0,1000)
#                     pygame.draw.circle(screen, (255,255,255), [x1,y1], 10)
#                     pygame.draw.circle(screen, (255, 255, 0), [x2,y2], 10)
#             if event.type == pygame.KEYDOWN:
#                 print(event.key)
#                 if event.key == pygame.K_1:
#                     print("You picked Player 1. Red darts miss the target. White darts hit the target.")
#                 elif event.key == pygame.K_2:
#                     print("You picked Player 2. Red darts miss the target. White darts hit the target.")    
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 run = False
#         pygame.display.flip()

