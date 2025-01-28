from graphics import Line, Point

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall)
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall)
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        self_center_x = self._x1 + ((self._x2 - self._x1) / 2)
        self_center_y = self._y1 + ((self._y2 - self._y1) / 2)
        other_center_x = to_cell._x1 + ((to_cell._x2 - to_cell._x1) / 2)
        other_center_y = to_cell._y1 + ((to_cell._y2 - to_cell._y1) / 2)
        line = Line(Point(self_center_x, self_center_y), Point(other_center_x, other_center_y))
        self._win.draw_line(line, fill_color = color)