import pygame

pygame.init()


screen_size = (1080, 720)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False

while not done:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            done = True
    key_list = pygame.key.get_pressed()
    if key_list[pygame.K_ESCAPE]:
        done = True

screen.fill((0, 0, 0))

pygame.display.flip()
clock.tick(60)