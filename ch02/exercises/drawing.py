import turtle             
my_window = turtle.Screen() 
my_window.bgcolor("light blue")      
my_pen = turtle.Turtle()     
my_pen.color("white")
my_pen.pensize(1)

sides = int(input("Enter the number of sides of your shape:"))
print = sides
var1 = sides

length = int(input("Enter the length of each side:"))
print = length
var2= length

for i in range(sides):
    turtle.forward(length)
    turtle.right(360 /sides)

my_window.exitonclick()
