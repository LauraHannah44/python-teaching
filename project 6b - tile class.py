import pygame

pygame.init()


class Tile:

    def __init__(self, tile_state, tile_pos, tile_dims, tile_colour):
        self.state = tile_state
        self.tile_number = tile_pos[0]
        self.row_number = tile_pos[1]
        self.width = tile_dims[0]
        self.height = tile_dims[1]
        self.colour = tile_colour

    def get_rect(self):
        tile_x = self.tile_number * self.width
        tile_y = self.row_number * self.height
        rect = pygame.Rect(tile_x, tile_y, self.width - 1, self.height - 1)
        return rect

    def get_colour(self):
        return self.colour[self.state]


screen_size = (1080, 720)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
board = list()

tile_dims = (10, 10)
tiles_per_row = round(screen_size[0] / tile_dims[0])
rows_per_board = round(screen_size[1] / tile_dims[1])

for row_number in range(rows_per_board):
    tile_list = list()
    for tile_number in range(tiles_per_row):
        colour = ((0, 0, 0), (255, 255, 255))
        tile = Tile(0, (tile_number, row_number), tile_dims, colour)
        tile_list.append(tile)
    board.append(tile_list)

#board_list[y][x]

while not done:
    #checks
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            done = True
    key_list = pygame.key.get_pressed()
    if key_list[pygame.K_ESCAPE]:
        done = True

    #maths

    #printing

    screen.fill((15, 15, 15))

    for tile_list in board:
        for tile in tile_list:
            rect = tile.get_rect()
            colour = tile.get_colour()
            pygame.draw.rect(screen, colour, rect)

    #flip

    pygame.display.flip()
    clock.tick(60)