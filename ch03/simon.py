## Events

## Operating system handles events
## Your program --> OS: anything happening?

## OS -> event
## type of event == operation

import pygame

pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "green", "blue", "yellow"]

for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(250)

message = """
    Simon says:
    UP: RED
    DOWN: BLUE
    LEFT: GREEN
    RIGHT: YELLOW
"""
response = input(message)

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("UP")
        elif event.key == pygame.K_DOWN:
            screen.fill("blue")
            user_sequence.append("blue")
        elif event.key == pygame.K_LEFT:
            screen.fill("green")
            user_sequence.append("green")
        elif event.key == pygame.K_RIGHT:
            screen.fill("yellow")
            user_sequence.append("yellow")
    

if user_sequence == colors:
    print("You win!")
    