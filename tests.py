import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        print(f"Length of _cells: {len(m1._cells)}")
        print(f"Length of first column: {len(m1._cells[0])}")
        self.assertEqual(
            len(m1._cells),
            num_rows,  
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,  
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

if __name__ == "__main__":
    unittest.main()