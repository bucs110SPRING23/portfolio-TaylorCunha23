value = input("Enter the number of rows:")
value = int(value)

def star_pyramid(value):
    myList = []
    for i in range(1,value+1):
        myList.append("*"*i)
    print("\n".join(myList))

star_pyramid(value)
