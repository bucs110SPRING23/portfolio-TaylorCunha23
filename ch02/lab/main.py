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
screen = pygame.display.set_mode()
screen.fill("pink")
pygame.display.flip()
pygame.time.wait(50)

side_length = 400
xpos = 1000
ypos = 500

shapes = [3,4,6,20,100,360]

for num_sides in shapes:
  points = []
  for i in range(int(num_sides)):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y]) 
    pygame.display.flip()
  pygame.time.wait(1000)
  screen.fill("pink")
  pygame.display.flip()
  pygame.draw.polygon(screen, "white", (points))
  pygame.time.wait(1000)




