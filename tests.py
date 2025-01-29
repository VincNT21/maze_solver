import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
        num_cols2 = 1
        num_rows2 = 100
        m2 = Maze(0, 0, num_rows2, num_cols2, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols2
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows2
        )
        num_cols3 = 50
        num_rows3 = 1
        m3 = Maze(0, 0, num_rows3, num_cols3, 10, 10)
        self.assertEqual(
            len(m3._cells),
            num_cols3
        )
        self.assertEqual(
            len(m3._cells[0]),
            num_rows3
        )
        

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False
        )

    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=0)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False
                )

if __name__ == '__main__':
    unittest.main()