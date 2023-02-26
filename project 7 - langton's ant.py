import pygame
import os

pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"


class Board:

    def __init__(self, size, tile_dimensions, tile_colours):
        self.size = size
        self.tile_dimensions = tile_dimensions
        self.no_of_rows = self.size[1] // self.tile_dimensions[1]
        self.no_of_columns = self.size[0] // self.tile_dimensions[0]
        self.tile_colours = tile_colours

    def populate(self):
        self.tiles = list()
        for row_number in range(self.no_of_rows):
            row = list()
            for column_number in range(self.no_of_columns):
                state = 0
                #(row_number % 4 in (0, 1)) ^ (column_number % 4 in (0, 1))
                tile = Tile(board, (column_number, row_number), state)
                row.append(tile)
            self.tiles.append(row)

    def get_rect(self):
        rect_left = round(screen_size[0] / 2 - self.size[0] / 2) + pan_offset[0] * self.tile_dimensions[0]
        rect_top = round(screen_size[1] / 2 - self.size[1] / 2) + pan_offset[1] * self.tile_dimensions[1]
        rect = pygame.Rect(rect_left, rect_top, self.size[0], self.size[1])
        return rect

    def draw(self):
        pygame.draw.rect(screen, self.tile_colours[0], self.get_rect())

    def draw_tiles(self):
        for row in self.tiles:
            for tile in row:
                if tile.state:
                    tile.draw()


class Tile:

    def __init__(self, board, position, state):
        self.board = board
        self.column = position[0]
        self.row = position[1]
        self.state = state

    def get_colour(self):
        return self.board.tile_colours[self.state]

    def get_rect(self):
        board_rect = self.board.get_rect()
        rect_left = board_rect.left + self.board.tile_dimensions[0] * self.column
        rect_top = board_rect.top + self.board.tile_dimensions[1] * self.row
        rect = pygame.Rect(rect_left, rect_top, self.board.tile_dimensions[0], self.board.tile_dimensions[1])
        return rect

    def draw(self):
        pygame.draw.rect(screen, self.get_colour(), self.get_rect())


class Ant:

    def __init__(self, board, position, rules, orientation=1):
        self.board = board
        self.position = position
        self.rules = rules
        self.orientation = orientation

    def update(self):
        tile = self.board.tiles[self.position[1]][self.position[0]]
        action = self.rules[tile.state % len(self.rules)]
        turn_amount = action_dict[action]

        self.orientation += turn_amount
        self.orientation %= 4

        tile.state += 1
        tile.state %= len(self.rules)
        tile.draw()

        self.move()

    def move(self):
        vector = orientation_vectors[self.orientation]
        self.position[0] += vector[0]
        self.position[0] %= self.board.no_of_columns
        self.position[1] += vector[1]
        self.position[1] %= self.board.no_of_rows


def refresh_screen():
    screen.fill((5, 5, 5))

    board.draw()

    board.draw_tiles()

    frame_update()


def frame_update():
    global frame
    frame += 1
    text_surface = FONT.render(str(frame), False, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.bottomright = (screen_size[0], screen_size[1])
    pygame.draw.rect(screen, (0, 0, 0), text_rect)
    screen.blit(text_surface, text_rect.topleft)


def generate_colours(colours):
    R, F, L, B = 0, 0, 0, 0
    temp_ruleset = ruleset[len(colours) - 1:len(ruleset) - 1]
    for action in temp_ruleset:
        if action == "R":
            hex_code = R * 128 // temp_ruleset.count(action)
            R += 1
            colour = (hex_code, hex_code, hex_code)
        elif action == "F":
            hex_code = 255 - F * 128 // temp_ruleset.count(action)
            F += 1
            colour = (255, 255, hex_code)
        elif action == "L":
            hex_code = 255 - L * 128 // temp_ruleset.count(action)
            L += 1
            colour = (255, hex_code, 255)
        else:
            hex_code = 255 - B * 128 // temp_ruleset.count(action)
            B += 1
            colour = (hex_code, 255, 255)
        colours.append(colour)
    return colours


screen_size = (1920, 1080)
screen = pygame.display.set_mode(screen_size, pygame.NOFRAME)
clock = pygame.time.Clock()
action_dict = {"F": 0, "L": 1, "B": 2, "R": 3}
orientation_vectors = ((1, 0), (0, -1), (-1, 0), (0, 1))

ruleset = list("LRLLRRLRLRRRRLR")
#colours = generate_colours()
colours = [(0, 0, 0), (255, 255, 255), (255, 50, 50), (255, 255, 50), (50, 255, 50), (50, 255, 255), (50, 50, 255), (255, 50, 255)]
colours = generate_colours(colours)
FONT = pygame.font.SysFont("Consolas", 45)

default_board_size = [300, 300]
tile_dimensions = [1, 1]
board = Board(default_board_size, tile_dimensions, colours)

starting_position = [board.no_of_columns // 2, board.no_of_rows // 2]
ant = Ant(board, starting_position, ruleset)

pan_offset = [0, 0]

done = False
pause = False
left_mouse_held = False
frame = 0

board.populate()

refresh_screen()

while not done:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_PERIOD and pause:
                ant.update()
                frame_update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                left_mouse_held = True
                pygame.mouse.get_rel()
            if event.button in (4, 5):
                if event.button == 4:
                    board.tile_dimensions[0] += 1
                    board.tile_dimensions[1] += 1
                if event.button == 5 and board.tile_dimensions[0] != 1 and board.tile_dimensions[1] != 1:
                    board.tile_dimensions[0] -= 1
                    board.tile_dimensions[1] -= 1
                board.size[0] = board.tile_dimensions[0] * board.no_of_columns
                board.size[1] = board.tile_dimensions[1] * board.no_of_rows
                refresh_screen()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_mouse_held = False
        if event.type == pygame.MOUSEMOTION and left_mouse_held:
            relative_offset = pygame.mouse.get_rel()
            pan_offset[0] += relative_offset[0] / tile_dimensions[0]
            pan_offset[1] += relative_offset[1] / tile_dimensions[1]
            refresh_screen()

    pygame.display.flip()

    if not pause:
        ant.update()
        frame_update()
#    clock.tick(60)
