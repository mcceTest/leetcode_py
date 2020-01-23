import unittest
from X130_SurroundedRegions import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        sol.solve(board)
        self.assertListEqual(board, [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']])

    def test2(self):
        sol = Solution()
        board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
        sol.solve(board)
        self.assertListEqual(board, [["X","O","X","O","X","O"],["O","X","X","X","X","X"],["X","X","X","X","X","O"],["O","X","O","X","O","X"]])



if __name__ == "__main__":
    unittest.main()