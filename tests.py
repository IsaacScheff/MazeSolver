import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,  
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,  
        )

    def test_maze_create_cells_large(self):
        num_cols = 8
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
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            True,
        )
        self.assertEqual(
            m1._cells[9][9].has_right_wall,
            True,
        )
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m1._cells[9][9].has_right_wall,
            False,
        )

if __name__ == "__main__":
    unittest.main()