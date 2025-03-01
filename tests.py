import unittest

from graphics import Window
from objects.maze import Maze


class Tests(unittest.TestCase):
    def test_maze_cell_creation(self):
        test_window = Window(100, 100)
        num_cols = 12
        num_rows = 10
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10, test_window)
        self.assertEqual(m1.get_cols(), num_cols)
        self.assertEqual(m1.get_rows(), num_rows)


if __name__ == "__main__":
    unittest.main()
