from graphics import Window
from objects.maze import Maze


def main() -> None:
    win = Window(800, 800)
    m1 = Maze(10, 10, 10, 10, 50, 50, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
