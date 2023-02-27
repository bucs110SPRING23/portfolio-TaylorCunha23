import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=500,width=500)

taylor = turtle.Turtle()
taylor.color("brown")
taylor.turtlesize(1)
taylor.shape("turtle")
turtle.Screen().bgcolor("light pink")

Heads_or_Tails = ["heads", "tails"]

message = """
        Flip a coin! 
        Press enter.
        """
response = input(message)

(x,y) = taylor.position()

while (True):
    for i in Heads_or_Tails:
        coinflip = random.choice(Heads_or_Tails)
        if coinflip == "heads":
            print("Heads!")
            taylor.left(90)
            taylor.forward(50)
            if taylor.position(-500 < x < 500):
                break
            taylor.undo()
            if taylor.position(-500 < y < 500):
                break
        if coinflip == "tails":
            print("Tails!")
            taylor.right(90)
            taylor.forward(50)
            if taylor.position(-500 < x < 500):
                break
            if taylor.position(-500 < y < 500):
                break
            taylor.undo()
    



turtle.exitonclick()