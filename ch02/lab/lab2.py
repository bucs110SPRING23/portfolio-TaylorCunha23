# Part A
import random
import time
import turtle

TURTLE_SIZE = 25
bonnie  = turtle.Turtle(shape = "turtle")
bonnie.hideturtle()
bonnie.color("pink")
clyde = turtle.Turtle(shape = "turtle")
clyde.hideturtle()
clyde.color("purple")

window = turtle.Screen()
turtle.screensize(1000,1000)

bonnie.penup()
clyde.penup()

# Race 1
bonnie.goto(-100,20)
clyde.goto(-100,-20)
bonnie.showturtle()
clyde.showturtle()

time.sleep(2)


bonnie.forward(random.randrange(1,100))
bonnie.speed(1)
clyde.forward(random.randrange(1,100))
clyde.speed(1)

time.sleep(2)
print("Race 1 is over!")

bonnie.goto(-100,20)
clyde.goto(-100,-20)

# Race 2
for i in range(10):
    bonnie.forward(random.randrange(1,100))
    clyde.forward(random.randrange(1,100))
time.sleep(2)
print("Race 2 is over!")
bonnie.goto(-100,20)
clyde.goto(-100,-20)

window.exitonclick()

# Part B
import math
import pygame
pygame.init()
window = pygame.display.set_mode()

points = []

for i in range(3):
    triangle_num_sides = 3
    angle = 360/triangle_num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)

points.append(x,y)

def drawTriangle(screen, "black", numSides, tiltAngle, x, y, radius):
  pts = []
  for i in range(numSides):
    x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / numSides)
    y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / numSides)
    pts.append([int(x), int(y)])
  pygame.draw.polygon(surf, color, pts)
