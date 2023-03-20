import pygame
pygame.init()


def threenp1(n):
    count = 0
    num_seq = []
    if n < 1:
       return []
    while n > 1:
        count = count + 1
        if n % 2 == 0:
            n = n / 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
        num_seq.append(n)    
    return num_seq
    return count

def threenp1range(upper_limit):
    

def main():
    n = int(input("Positive integer:"))
    num_seq = []
    count = threenp1(n)
    print("Number you started with:", n)
    print("Iterations:", count)
    print("Number of iterations:", len(count))
main()