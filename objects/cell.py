import math
from typing import TYPE_CHECKING

from objects.line import Line
from objects.point import Point

if TYPE_CHECKING:
    from graphics import Window


class Cell:
    def __init__(self, win: "Window", x1: int, y1: int, x2: int, y2: int) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self) -> None:
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        color = "gray"
        if not undo:
            color = "red"

        start = Point(
            math.floor((self._x1 + self._x2) / 2), math.floor((self._y1 + self._y2) / 2)
        )
        end = Point(
            math.floor((to_cell._x1 + to_cell._x2) / 2),
            math.floor((to_cell._y1 + to_cell._y2) / 2),
        )

        line = Line(start, end)
        self._win.draw_line(line, color)
