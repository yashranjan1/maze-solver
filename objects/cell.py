from typing import TYPE_CHECKING, List

from graphics import Window
from objects.line import Line
from objects.point import Point

if TYPE_CHECKING:
    from tkinter import Canvas


class Cell:
    def __init__(
        self,
        has_left_wall: bool,
        has_right_wall: bool,
        has_top_wall: bool,
        has_bottom_val: bool,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        window: Window,
    ) -> None:
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_val = has_bottom_val
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.window = window

    def draw(self, canvas: "Canvas", fill_color: str) -> None:
        line_arr: List[Line] = []
        if self.has_left_wall:
            point_a = Point(self.x1, self.y1)
            point_b = Point(self.x1, self.y2)
            wall = Line(point_a, point_b)
            line_arr.append(wall)
        if self.has_right_wall:
            point_a = Point(self.x2, self.y1)
            point_b = Point(self.x2, self.y2)
            wall = Line(point_a, point_b)
            line_arr.append(wall)
        if self.has_top_wall:
            point_a = Point(self.x1, self.y1)
            point_b = Point(self.x2, self.y1)
            wall = Line(point_a, point_b)
            line_arr.append(wall)
        if self.has_bottom_val:
            point_a = Point(self.x1, self.y2)
            point_b = Point(self.x2, self.y2)
            wall = Line(point_a, point_b)
            line_arr.append(wall)
        for line in line_arr:
            line.draw(canvas, fill_color)
