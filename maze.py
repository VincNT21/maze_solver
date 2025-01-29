import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            cells_col = []
            for j in range(self._num_rows):
                cells_col.append(Cell(self._win))
            self._cells.append(cells_col)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
            x1 = self._x1 + (self._cell_size_x * i)
            x2 = self._x1 + (self._cell_size_x * (i + 1))
            y1 = self._y1 + (self._cell_size_y * j)
            y2 = self._y1 + (self._cell_size_y * (j + 1))
            self._cells[i][j].draw(x1, x2, y1, y2)
            self._animate()

    def _animate(self):
        if self._win is None: # in test case
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        curr_cell = self._cells[i][j]
        curr_cell.visited = True
        while True:
            next_index_list = []
            
            # check left cell
            if i > 0 and not self._cells[i-1][j].visited:
                next_index_list.append((i-1, j))
            # check right cell
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                next_index_list.append((i+1, j))
            # check top cell
            if j > 0 and not self._cells[i][j-1].visited:
                next_index_list.append((i, j-1))
            # check bottom cell
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                next_index_list.append((i, j+1))
            
            # nowhere to go = break out the loop
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return
            
            # choose a random direction
            random_direction = random.randrange(0, len(next_index_list))
            next_index = next_index_list[random_direction]

            # break walls
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # top
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            # bottom
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            
            # move to chosen cell
            self._break_walls_r(next_index[0], next_index[1])


            



