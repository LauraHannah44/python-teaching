import pygame

pygame.init()

screen_size = (1700, 850)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("Project 5")
clock = pygame.time.Clock()
done = False
rect1w = 111
rect1h = 111
rect1vx = 0
rect1vy = 0
red   = 255
green = 255
blue  = 255

while not done:
    #checks
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.VIDEORESIZE:
            screen_size = (event.w, event.h)
            screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    key_list = pygame.key.get_pressed()
    if key_list[pygame.K_ESCAPE]:
        done = True
    if key_list[pygame.K_UP]:
        rect1vy -= 0.5
    if key_list[pygame.K_DOWN]:
        rect1vy += 0.5
    if key_list[pygame.K_LEFT]:
        rect1vx -= 0.5
    if key_list[pygame.K_RIGHT]:
        rect1vx += 0.5
    if key_list[pygame.K_q] and red < 255:
        red += 1
    if key_list[pygame.K_a] and red > 0:
        red -= 1
    if key_list[pygame.K_w] and green < 255:
        green += 1
    if key_list[pygame.K_s] and green > 0:
        green -= 1
    if key_list[pygame.K_e] and blue < 255:
        blue += 1
    if key_list[pygame.K_d] and blue > 0:
        blue -= 1

    #maths
    rect1h += rect1vy
    rect1w += rect1vx
    rect1vy /= 1.05
    rect1vx /= 1.05

    rect1_colour = ((red, green, blue), (255 - red, 255 - green, 255 - blue))[rect1w * rect1h <= 0]

    #printing
    screen.fill((0, 0, 0))
    rect1 = pygame.Rect(round(screen_size[0] / 2 - rect1w / 2),
                        round(screen_size[1] / 2 - rect1h / 2),
                        rect1w, rect1h)
    rect2 = pygame.Rect(round(screen_size[0] / 2 - rect1w / 2) + rect1w - 5,
                        round(screen_size[1] / 2 - rect1h / 2) + rect1h - 5,
                        10, 10)
    pygame.draw.rect(screen, rect1_colour, rect1)
    pygame.draw.rect(screen, (164, 164, 255), rect2)

    #flip
    pygame.display.flip()
    clock.tick(60)
