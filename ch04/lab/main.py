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
        There are two players, Red vs Blue.
        Red player's darts that hit the target are red.
        Blue player's darts that hit the target are blue.
        Darts that miss the target are white, regardless of which player threw them.
        """
    response = input(message)

message = """
        Which player will win?
        To pick Red Player: Press 1
        To pick Blue Player: Press 2
        """
    response = input(message)
if event.type == pygame.KEYDOWN:
                    print(event.key)
                if event.key == pygame.K_1:
                    print("You picked Red Player.")
                elif event.key == pygame.K_2:
                    print("You picked Blue Player.")    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
            pygame.display.flip()

for darts in range(10):
    x1 = random.randrange(0,1000)
    y1 = random.randrange(0,1000)
    x2 = random.randrange(0,1000)
    y2 = random.randrange(0,1000)
    distance_from_center1 = math.hypot(x1-500, y1-500)
    distance_from_center2 = math.hypot(x2-500, y2-500)
    is_in_circle1 = distance_from_center1 <= screen_width/2
    is_in_circle2 = distance_from_center2 <= screen_width/2
    print(distance_from_center1, screen_width/2)
    print(is_in_circle1)
    print(distance_from_center2, screen_width/2)
    print(is_in_circle2)
    if is_in_circle1:
        pygame.draw.circle(screen, (255,0,0), [x1,y1], 10)
    else:
        pygame.draw.circle(screen, (255, 255, 255), [x1,y1], 10) 
    if is_in_circle2:
        pygame.draw.circle(screen, (0, 0, 255), [x2,y2], 10)
    else: 
        pygame.draw.circle(screen, (255, 255, 255), [x2,y2], 10)
pygame.display.flip()
pygame.time.wait(10000)

screen.fill((153, 184, 152))
run = True
while run:
    dartgame = pygame.event.get()
        for event in dartgame:
            if event.type == pygame.MOUSEBUTTONUP:
            pygame.draw.circle(screen, (183, 152, 184), (500,500), 500, width=0)
            pygame.draw.circle(screen, (0, 0, 0), (500,500), 500, width=3)
            pygame.draw.line(screen, "black", (500,-1000), (500,1000), width=3)
            pygame.draw.line(screen, "black", (0,500), (1000,500), width=3)
            pygame.display.update()
            message = """
                    Which player will win?
                    To pick Player 1: Press 1
                    To pick Player 2: Press 2
                    """
                    response = input(message)

                for darts in range(10):
                    x1 = random.randrange(0,1000)
                    y1 = random.randrange(0,1000)
                    x2 = random.randrange(0,1000)
                    y2 = random.randrange(0,1000)
                    pygame.draw.circle(screen, (255,255,255), [x1,y1], 10)
                    pygame.draw.circle(screen, (255, 255, 0), [x2,y2], 10)
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                if event.key == pygame.K_1:
                    print("You picked Player 1. Red darts miss the target. White darts hit the target.")
                elif event.key == pygame.K_2:
                    print("You picked Player 2. Red darts miss the target. White darts hit the target.")    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
            pygame.display.flip()


