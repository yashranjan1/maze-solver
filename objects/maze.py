from typing import TYPE_CHECKING, List

from objects.cell import Cell
from objects.point import Point

if TYPE_CHECKING:
    from graphics import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: "Window",
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells: List["Cell"] = []
        self.__create_cells()

    def __create_cells(self) -> None:
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                top_left = Point(
                    self.x1 + self.cell_size_x * col, self.y1 + self.cell_size_y * row
                )
                bottom_right = Point(
                    self.x1 + self.cell_size_x * (col + 1),
                    self.y1 + self.cell_size_y * (row + 1),
                )
                cell = Cell(
                    self.win, top_left.x, top_left.y, bottom_right.x, bottom_right.y
                )
                self.__cells.append(cell)
        for cell in self.__cells:
            self.__draw_cell(cell)

    def __draw_cell(self, cell: "Cell") -> None:
        cell.draw()
