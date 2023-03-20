import pygame
pygame.init()
pygame.display.init
screen = pygame.display.set_mode((1000, 1000))

def threenp1(n):
    count = 0
    while n > 1:
        count = count + 1
        if n % 2 == 0:
            n = n / 2
            # count += 1
        else:
            n = 3 * n + 1
            # count += 1    
    return count

def threenp1range(upper_limit):
    upper_limit = 10
    objs_in_sequence = {}
    for i in range(2,upper_limit):
        iters = threenp1(i)
        objs_in_sequence[i] = iters
    return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict):
    upper_limit = 10
    n = int(input("Positive integer:"))
    count = threenp1(n)
    objs_in_sequence = threenp1range(upper_limit)
    threenplus1_iters_dict = dict.items(objs_in_sequence)
    
        

def main():
    upper_limit = 10
    objs_in_sequence = threenp1range(upper_limit)
    n = int(input("Positive integer:"))
    #num_seq = []
    count = threenp1(n)
    print("Number you started with:", n)
    print("Iterations:", objs_in_sequence)
    print("Number of iterations:", count)
    threenplus1_iters_dict = dict.items(objs_in_sequence)
    keys = objs_in_sequence.keys()
    x = objs_in_sequence  
    y = count
   # pairs = zip(dict.values(x), dict.keys(y))
    #points = []
    #for x in objs_in_sequence:
       # points.append(x)
       # points.append(y)
    #return points
    graph_coordinates(threenplus1_iters_dict)

    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))

main()