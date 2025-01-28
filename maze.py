from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for col in range(self._num_cols):
            cells_col = []
            for row in range(self._num_rows):
                cells_col.append(Cell(self._win))
            self._cells.append(cells_col)
        i = -1
        for col in self._cells:
            i += 1
            j = -1
            for cell in self._cells[i]:
                j += 1
                self._draw_cell(cell, i, j)

    def _draw_cell(self, cell, i, j):
            x1 = self._x1 + (self._cell_size_x * i)
            x2 = self._x1 + (self._cell_size_x * (i + 1))
            y1 = self._y1 + (self._cell_size_y * j)
            y2 = self._y1 + (self._cell_size_y * (j + 1))
            cell.draw(x1, x2, y1, y2)
            self._animate()

    def _animate(self):
         self._win.redraw()
         time.sleep(0.1)
            



