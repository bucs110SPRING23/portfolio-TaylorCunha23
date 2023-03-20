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

def main():
    print("Customize your smiley face!")

    face_color = input("What color is the face?:")
    face(face_color,100)
    pen.goto(-40, 120)

    eye_color = input("What color are the eyes?:")
    eyes(eye_color, 15)
    pen.goto(-37, 125)
    pupils = "black"
    eyes(pupils, 5)
    pen.goto(40, 120)
    eyes(eye_color, 15)
    pen.goto(40, 125)
    eyes(pupils, 5)
    pen.goto(0, 75)

    nose_color = input("What color is the nose?:")
    nose(nose_color, 8)
    pen.goto(-40, 85)
    pen.down()
    pen.right(90)
    pen.circle(40, 180)
    pen.up()
    pen.goto(-10, 45)
    pen.down()
    pen.right(180)
    
    mouth_color = input("What color is the mouth?:")
    mouth(mouth_color, 10, 180)
    pen.hideturtle()
    turtle.done()
    window.exitonclick()
main()
