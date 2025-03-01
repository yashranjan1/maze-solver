import time
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
        self.__cells: List[List["Cell"]] = []
        self.__create_cells()
        self.__break_entrance_and_exit_wall()

    def __create_cells(self) -> None:
        for col in range(self.num_cols):
            cell_col: List["Cell"] = []
            for row in range(self.num_rows):
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
                cell_col.append(cell)
            self.__cells.append(cell_col)
        for row in self.__cells:
            for cell in row:
                self.__draw_cell(cell)

    def __draw_cell(self, cell: "Cell") -> None:
        cell.draw()
        self.__animate()

    def __break_entrance_and_exit_wall(self):
        if not (len(self.__cells) > 0 and len(self.__cells[0]) > 0):
            raise Exception(
                "maze does not have enough cells for making an exit and entrance"
            )
        self.__cells[0][0].has_top_wall = False
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.__cells[0][0])
        self.__draw_cell(self.__cells[-1][-1])

    def __animate(self) -> None:
        self.win.redraw()
        time.sleep(0.05)

    def get_cols(self) -> int:
        return len(self.__cells)

    def get_rows(self) -> int:
        if len(self.__cells) > 0:
            return len(self.__cells[0])
        return 0
