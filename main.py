from graphics import Window
from objects.maze import Maze


def main() -> None:
    win = Window(800, 800)
    fixed_seed = 10
    m1 = Maze(10, 10, 10, 10, 50, 50, win, fixed_seed)
    win.wait_for_close()


if __name__ == "__main__":
    main()
