from tkinter import BOTH, Canvas, Tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from objects.line import Line


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed.... ")

    def close(self):
        self.__running = False

    def draw_line(self, line: "Line", fill_color: str = "white") -> None:
        line.draw(self.__canvas, fill_color)
