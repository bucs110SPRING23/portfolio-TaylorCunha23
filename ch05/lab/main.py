import pygame

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
    # upper_limit = 10
    objs_in_sequence = {}
    max_so_far = 0
    max_int = 0
    for i in range(2,upper_limit):
        iters = threenp1(i)
        objs_in_sequence[i] = iters
        if iters > max_so_far:
            max_so_far = iters
            max_int = i
    # print(objs_in_sequence, max_int, max_so_far)
    print(objs_in_sequence, max_so_far)
    return objs_in_sequence, max_so_far

def graph_coordinates(threenplus1_iters_dict):
    upper_limit = 30
    x = list(threenplus1_iters_dict.keys())
    y = list(threenplus1_iters_dict.values())
    points = []
    for i in range(len(x)):
        points.append((x[i], y[i]))
    return points
    
        

def main():
    pygame.init()
    pygame.display.init()
    display = pygame.display.set_mode((800, 800))
    width = 800
    height = 800
    upper_limit = 30
    objs_in_sequence, max_so_far = threenp1range(upper_limit)
    n = int(input("Positive integer:"))
    #num_seq = []
    count = threenp1(n)
    print("Number you started with:", n)
    print("Iterations:", objs_in_sequence)
    print("Number of iterations:", count)
    points = graph_coordinates(objs_in_sequence)

    run = True
    while run:
    # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if len(points) > 1:
            new_display = pygame.Surface((height, width))
            new_display.fill((0, 0, 0))
            pygame.draw.lines(new_display, (255, 255, 255), False, points, 10)
            new_display = pygame.transform.flip(new_display, False, True)
            width, height = new_display.get_size()
            new_display = pygame.transform.scale(new_display, (width * 10, height * 10))
            # new_display = pygame.transform.rotate(new_display, 270)
            display.blit(pygame.transform.scale(new_display, (width, height)), (0, 0))
            pygame.display.update()
            # new_display = pygame.transform.scale(new_display, (height * 5, width * 5))
            # display.blit(new_display, (0, 0))
            # pygame.display.update()
            font = pygame.font.Font(None, 30)
            title_msg = font.render("The Graph:", True, 'Red')
            display.blit(title_msg, (10, 10))
            max_msg = font.render(f"Max iterations so far: {max_so_far}", True, 'Red')
            display.blit(max_msg, (10, 50))
            pygame.display.update()
    pygame.quit()

main()