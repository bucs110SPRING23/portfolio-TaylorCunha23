import pygame
pygame.init()

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
    dict.items()
    pygame.draw.lines()

def main():
    upper_limit = 10
    objs_in_sequence = threenp1range(upper_limit)
    n = int(input("Positive integer:"))
    num_seq = []
    count = threenp1(n)
    print("Number you started with:", n)
    print("Iterations:", objs_in_sequence)
    print("Number of iterations:", count)


main()