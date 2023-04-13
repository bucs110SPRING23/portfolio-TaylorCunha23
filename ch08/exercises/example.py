# class == type
# Use 'class' for user-defined types
# 'complex-type'

# class data: instance variables

class Num:
    def __init__(self, n):
        self.data = n #instance variable for Num type objects

def main():
    mynum = Num(7)
    print(mynum.data)

main()
        