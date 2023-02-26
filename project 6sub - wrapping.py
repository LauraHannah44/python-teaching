if WRAPPING:
    bottom_x = (x - 1, self.board.columns - 1)[x == 0]
    top_x = (x + 1, 0)[x == self.board.columns - 1]
    bottom_y = (y - 1, self.board.rows - 1)[y == 0]
    top_y = (y + 1, 0)[y == self.board.rows - 1]

    self.neighbors = [self.board.tiles[y][bottom_x],
                      self.board.tiles[y][top_x],
                      self.board.tiles[bottom_y][x],
                      self.board.tiles[top_y][x],
                      self.board.tiles[bottom_y][bottom_x],
                      self.board.tiles[top_y][top_x],
                      self.board.tiles[top_y][bottom_x],
                      self.board.tiles[bottom_y][top_x]]

else:
    self.neighbors = list()
    if x != 0:
        self.neighbors.append(self.board.tiles[y][x - 1])
    if x != self.board.columns - 1:
        self.neighbors.append(self.board.tiles[y][x + 1])

    if y != 0:
        self.neighbors.append(self.board.tiles[y - 1][x])
    if y != self.board.rows - 1:
        self.neighbors.append(self.board.tiles[y + 1][x])

    if x != 0 and y != 0:
        self.neighbors.append(self.board.tiles[y - 1][x - 1])
    if x != self.board.columns - 1 and y != self.board.rows - 1:
        self.neighbors.append(self.board.tiles[y + 1][x + 1])

    if x != 0 and y != self.board.rows - 1:
        self.neighbors.append(self.board.tiles[y + 1][x - 1])
    if x != self.board.columns - 1 and y != 0:
        self.neighbors.append(self.board.tiles[y - 1][x + 1])