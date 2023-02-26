import pygame
import math


def v_round(vector):
    return int(vector.x), int(vector.y)


def get_angle(key_list):
    keys = 0
    angle = 0
    arrow_key_list = (key_list[pygame.K_RIGHT], key_list[pygame.K_DOWN], key_list[pygame.K_LEFT], key_list[pygame.K_UP])
    for index, is_pressed in enumerate(arrow_key_list):
        keys += is_pressed
        if index == 0 and key_list[pygame.K_UP]:
            index = 4
        angle += is_pressed * index * 90
    angle /= keys

    return angle


pygame.init()

#region definitions
screen_size = pygame.Vector2(1080, 720)

screen = pygame.display.set_mode((round(screen_size.x), round(screen_size.y)), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False

frame = 0

obj1_dim = pygame.Vector2(5, 5)
obj1_pos = screen_size / 2 - obj1_dim / 2
obj1_vel = pygame.Vector2(0, 0)

do_trace = False
trace_rects = list()
#endregion

while not done:
    #region keychecks
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.VIDEORESIZE:
            screen_size.update(event.w, event.h)
            screen = pygame.display.set_mode((round(screen_size.x), round(screen_size.y)), pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            do_trace = not do_trace
    key_list = pygame.key.get_pressed()
    if key_list[pygame.K_ESCAPE]:
        done = True

    if key_list[pygame.K_RIGHT] or key_list[pygame.K_UP] or key_list[pygame.K_LEFT] or key_list[pygame.K_DOWN]:
        obj1_acc.from_polar((300, get_angle(key_list)))
    else:
        obj1_acc = pygame.Vector2(0, 0)

    if key_list[pygame.K_r]:
        trace_rects = list()

    #endregion

    obj1_pos += obj1_vel / 60
    obj1_vel += obj1_acc / 60
    obj1_vel *= 0.9

    if frame % 4 == 0:
        if pygame.Rect(*v_round(obj1_pos), 1, 1) not in trace_rects and do_trace:
            trace_rects.append(pygame.Rect(*v_round(obj1_pos), 1, 1))

    screen.fill((0, 0, 0))
    for trace_rect in trace_rects:
        pygame.draw.ellipse(screen, (164, 164, 255), trace_rect)

    object1 = pygame.Rect(*v_round(obj1_pos - obj1_dim / 2), *v_round(obj1_dim))

    pygame.draw.rect(screen, (255, 255, 255), object1)
    pygame.display.flip()
    frame += 1
    clock.tick(60)