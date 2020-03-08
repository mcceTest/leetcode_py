import unittest
from X200_NumberofIslands import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        grid = [list('11110'),
                list('11010'),
                list('11000'),
                list('00000')]

        self.assertEqual(sol.numIslands(grid), 1)


    def test2(self):
        sol = Solution()
        grid = [list('11000'),
                list('11000'),
                list('00100'),
                list('00011')]

        self.assertEqual(sol.numIslands(grid), 3)

    

if __name__ == "__main__":
    unittest.main()