import turtle

# stimulate pen and paper
# module: turtle, command: Turtle
# variable = module.function()
pen = turtle.Turtle()
pen2 = turtle.Turtle()
pen2.shape("turtle")
pen2.color("purple")
pen.color("orange")
pen.speed(1)
pen2.speed(0)
window = turtle.Screen()
pen.forward(100)
pen.left(90)
# var = math.pi

# interface: what can I tell it to do
# state:

#Always must be the last turtle command
window.exitonclick()