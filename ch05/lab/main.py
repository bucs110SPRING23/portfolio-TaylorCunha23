import pygame
pygame.init()


def threenp1(n):
    num_seq = [n]
    count = 0
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

def main():
    n = int(input("Positive integer:"))
    count = threenp1(n)
    print("Number you started with:", n)
    print("Iterations:", count)

main()