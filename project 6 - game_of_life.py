import pygame
import random
import os
import copy

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

pygame.init()


class Tile:

    def __init__(self, tile_state, tile_pos, tile_colour):
        self.state = tile_state
        self.tile_number = tile_pos[0]
        self.row_number = tile_pos[1]
        self.colour = tile_colour

    def set_adj(self):

        y = self.row_number
        x = self.tile_number

        bottom_x = (x - 1, tiles_per_row - 1)[x == 0]
        top_x    = (x + 1, 0)[x == tiles_per_row - 1]
        bottom_y = (y - 1, rows_per_board - 1)[y == 0]
        top_y    = (y + 1, 0)[y == rows_per_board - 1]

        self.adjacencies = [board[y][bottom_x],
                            board[y][top_x],
                            board[bottom_y][x],
                            board[top_y][x],
                            board[bottom_y][bottom_x],
                            board[top_y][top_x],
                            board[top_y][bottom_x],
                            board[bottom_y][top_x]]
                            #sets adjacent tiles to be checked, excludes overlaps at edges

    def get_rect(self):
        tile_x = round(screen_size[0] / 2 + (pan_offset[0] - board_size[0] / 2) * zoom_multiplier)
        tile_x += self.tile_number * tile_dims[0] * zoom_multiplier
        tile_y = round(screen_size[1] / 2 + (pan_offset[1] - board_size[1] / 2) * zoom_multiplier)
        tile_y += self.row_number * tile_dims[1] * zoom_multiplier
        rect = pygame.Rect(tile_x, tile_y, tile_dims[0] * zoom_multiplier, tile_dims[1] * zoom_multiplier)
        return rect
        #defines board accounting for pan and zoom

    def get_colour(self):
        return self.colour[self.state]
        #changes colour based on state of tile

    def check_adj(self):
        adj_cells = 0
        for cell in self.adjacencies:
            if cell.state:
                adj_cells += 1
                if adj_cells == 4:
                    break
        if self.state:
            if adj_cells in (2, 3):
                self.new_state = 1
            else:
                self.new_state = 0
        else:
            if adj_cells == 3:
                self.new_state = 1
            else:
                self.new_state = 0
        #conditions for a live cell to continue living, and for a dead cell to become alive

    def update_cell(self):
        self.state = self.new_state


def populate_board(alive_percentage=0):
    global board
    board = list()
    for row_number in range(rows_per_board):
        tile_list = list()
        for tile_number in range(tiles_per_row):
            colour = ((0, 0, 0), (255, 255, 255))
            is_alive = random.random() < alive_percentage
            tile = Tile(is_alive, (tile_number, row_number), colour)
            #creates instance of Tile class, passes in tile co-ordinates and colour
            tile_list.append(tile)
        board.append(tile_list)

    for tile_list in board:
        for tile in tile_list:
            tile.set_adj()


def get_board_rect():
    board_left = round(screen_size[0] / 2 + (pan_offset[0] - board_size[0] / 2) * zoom_multiplier) - board_size[0] * zoom_multiplier
    board_top  = round(screen_size[1] / 2 + (pan_offset[1] - board_size[1] / 2) * zoom_multiplier) - board_size[0] * zoom_multiplier
    board_rect = pygame.Rect(board_left, board_top, board_size[0] * zoom_multiplier * 3, board_size[1] * zoom_multiplier * 3)
    return board_rect
    #defines board accounting for pan and zoom offset/multiplier


screen_size = (1920, 1080)
screen = pygame.display.set_mode(screen_size, pygame.NOFRAME)
clock = pygame.time.Clock()
done = False
board_size = (150, 150)
frame_count = 0
pause = False
m1_held_down = False
marked_coord = False
pan_offset = [0, 0]
zoom_multiplier = 1
tile_dims = [1, 1]
tiles_per_row = round(board_size[0] / tile_dims[0])
rows_per_board = round(board_size[1] / tile_dims[1])
board_save = None

board_rect = get_board_rect()
populate_board(0.5)

while not done:

    event_list = pygame.event.get()

    for event in event_list:

        if event.type == pygame.VIDEORESIZE:
            screen_size = (event.w, event.h)
            screen = pygame.display.set_mode((event.w, event.h), pygame.NOFRAME)

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                pause = not pause
                #toggles pause variable

            if event.key == pygame.K_z:
                board_save = list()
                for tile_list in board:
                    tile_list_save = list()
                    for tile in tile_list:
                        tile_save = copy.copy(tile)
                        tile_list_save.append(tile_save)
                    board_save.append(tile_list_save)

            if event.key == pygame.K_x and board_save is not None:
                board = list()
                for tile_list_save in board_save:
                    tile_list = list()
                    for tile_save in tile_list_save:
                        tile = copy.copy(tile_save)
                        tile_list.append(tile)
                    board.append(tile_list)
                for tile_list in board:
                    for tile in tile_list:
                        tile.set_adj()

            if event.key == pygame.K_PERIOD and pause:
                for tile_list in board:
                    for tile in tile_list:
                        tile.check_adj()

                for tile_list in board:
                    for tile in tile_list:
                        tile.update_cell()

            if event.unicode in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                populate_board(int(event.unicode) / 10)
                #populates board with percentage

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mouse.get_rel()
                #resets relative mouse movement since last tick when called
                m1_held_down = True
                #checks for mouse hold

            if event.button == 3:
                marked_coord = pygame.mouse.get_pos()
                x_coord = marked_coord[0]
                y_coord = marked_coord[1]
                wrap_list = ((x_coord, y_coord),
                             (x_coord + board_size[0] * zoom_multiplier, y_coord),
                             (x_coord - board_size[0] * zoom_multiplier, y_coord),
                             (x_coord, y_coord + board_size[1] * zoom_multiplier),
                             (x_coord, y_coord - board_size[1] * zoom_multiplier),
                             (x_coord + board_size[0] * zoom_multiplier, y_coord + board_size[1] * zoom_multiplier),
                             (x_coord + board_size[0] * zoom_multiplier, y_coord - board_size[1] * zoom_multiplier),
                             (x_coord - board_size[0] * zoom_multiplier, y_coord + board_size[1] * zoom_multiplier),
                             (x_coord - board_size[0] * zoom_multiplier, y_coord - board_size[1] * zoom_multiplier))
                            #all co-ordinate points on screen + all 8 wrapped screens

                for tile_list in board:
                    for tile in tile_list:
                        for coord_set in wrap_list:
                            if tile.get_rect().collidepoint(*coord_set):
                                #unpacking co-ordinate tuple
                                tile.state = 1 - tile.state
                                break
                                #checks that mouse co-ordinate is within a specific tile, then toggles the state of that tile

            if event.button in (4, 5):
                increment = (-1, 1)[event.button == 4]
                if increment > 0 or zoom_multiplier > 1:
                    zoom_multiplier += increment
                board_rect = get_board_rect()
                #updating zoom multiplier and passing it into the board function

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                m1_held_down = False

        if event.type == pygame.MOUSEMOTION and m1_held_down:
            frame_offset = pygame.mouse.get_rel()
            #stores amount mouse has moved since last call
            pan_offset[0] += frame_offset[0] / zoom_multiplier
            pan_offset[1] += frame_offset[1] / zoom_multiplier
            #accounting for zoom multiplier
            board_rect = get_board_rect()

    key_list = pygame.key.get_pressed()
    if key_list[pygame.K_ESCAPE]:
        done = True

    screen.fill((20, 20, 20))

    pygame.draw.rect(screen, (0, 0, 0), board_rect)

    for tile_list in board:
        for tile in tile_list:
            if tile.state == 1:
                rect = tile.get_rect()
                if rect.right >= 0 and rect.bottom >= 0 and rect.left <= screen_size[0] and rect.top <= screen_size[1]:
                    pygame.draw.rect(screen, tile.get_colour(), rect)
                top_x_rect = rect.move(board_size[0] * zoom_multiplier, 0)
                bottom_x_rect = rect.move(-board_size[0] * zoom_multiplier, 0)
                top_y_rect = rect.move(0, board_size[1] * zoom_multiplier)
                bottom_y_rect = rect.move(0, -board_size[1] * zoom_multiplier)
                if top_x_rect.right >= 0 and rect.bottom >= 0 and top_x_rect.left <= screen_size[0] and rect.top <= screen_size[1]:
                    pygame.draw.rect(screen, tile.get_colour(), top_x_rect)
                if bottom_x_rect.right >= 0 and rect.bottom >= 0 and bottom_x_rect.left <= screen_size[0] and rect.top <= screen_size[1]:
                    pygame.draw.rect(screen, tile.get_colour(), bottom_x_rect)
                if rect.right >= 0 and top_y_rect.bottom >= 0 and rect.left <= screen_size[0] and top_y_rect.top <= screen_size[1]:
                    pygame.draw.rect(screen, tile.get_colour(), top_y_rect)
                if rect.right >= 0 and bottom_y_rect.bottom >= 0 and rect.left <= screen_size[0] and bottom_y_rect.top <= screen_size[1]:
                    pygame.draw.rect(screen, tile.get_colour(), bottom_y_rect)
                if top_x_rect.right >= 0 and top_y_rect.bottom >= 0 and top_x_rect.left <= screen_size[0] and top_y_rect.top <= screen_size[1]:
                    pygame.draw.rect(screen, tile.get_colour(), top_x_rect.move(0, board_size[1] * zoom_multiplier))
                if top_x_rect.right >= 0 and bottom_y_rect.bottom >= 0 and top_x_rect.left <= screen_size[0] and bottom_y_rect.top <= screen_size[1]:
                    pygame.draw.rect(screen, tile.get_colour(), top_x_rect.move(0, -board_size[1] * zoom_multiplier))
                if bottom_x_rect.right >= 0 and top_y_rect.bottom >= 0 and bottom_x_rect.left <= screen_size[0] and top_y_rect.top <= screen_size[1]:
                    pygame.draw.rect(screen, tile.get_colour(), bottom_x_rect.move(0, board_size[1] * zoom_multiplier))
                if bottom_x_rect.right >= 0 and bottom_y_rect.bottom >= 0 and bottom_x_rect.left <= screen_size[0] and bottom_y_rect.top <= screen_size[1]:
                    pygame.draw.rect(screen, tile.get_colour(), bottom_x_rect.move(0, -board_size[1] * zoom_multiplier))
                    #checks neighbours

    if frame_count % 2 == 0 and not pause:
        for tile_list in board:
            for tile in tile_list:
                tile.check_adj()
        for tile_list in board:
            for tile in tile_list:
                tile.update_cell()
        clock.tick(60)

    frame_count += 1
    pygame.display.flip()
