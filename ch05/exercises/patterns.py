value = input("Enter the number of rows:")
value = int(value)

def star_pyramid(value):
    myList = []
    for i in range(1,value+1):
        myList.append("*"*i)
    print("\n".join(myList))

print("In order:")
star_pyramid(value)

def rstar_pyramid(value):
    for i in range (value, 0, -1):
        print((value-i) * ' ' + i * '*')

print("In reverse order:")
rstar_pyramid(value)
