from turtle import *
import turtle
 
window = turtle.Screen()
turtle.screensize(1000,1000)
pen = turtle.Turtle()

def eyes(eyes_color, radius):
    pen.down()
    pen.fillcolor(eyes_color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.up()

def face(face_color,radius):
    pen.down()
    pen.fillcolor(face_color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.up()

def nose(nose_color, radius):
    pen.down()
    pen.fillcolor(nose_color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.up()

def mouth(mouth_color, radius, extent):
    pen.down()
    pen.fillcolor(mouth_color)
    pen.begin_fill()
    pen.circle(radius, extent)
    pen.end_fill()
    pen.up()

def get_colors():
    print("Customize your smiley face!")
    colors = {}
    colors["face"] = input("What color is the face?:")
    colors["eyes"] = input("What color are the eyes?:")
    colors["nose"] = input("What color is the nose?:")
    colors["mouth"] = input("What color is the mouth?:")
    return colors


def main():
    colors = get_colors()

    face(colors["face"],100)
    pen.goto(-40, 120)

    eyes(colors["eyes"], 15)
    pen.goto(-37, 125)
    pupils = "black"
    eyes(pupils, 5)
    pen.goto(40, 120)
    eyes(colors["eyes"], 15)
    pen.goto(40, 125)
    eyes(pupils, 5)
    pen.goto(0, 75)

    nose(colors["nose"], 8)
    pen.goto(-40, 85)
    pen.down()
    pen.right(90)
    pen.circle(40, 180)
    pen.up()
    pen.goto(-10, 45)
    pen.down()
    pen.right(180)
    
    mouth(colors["mouth"], 10, 180)
    pen.hideturtle()
    turtle.done()
    window.exitonclick()
main()

