import unittest

from X64_MinimumPathSum import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        grid = [
                [1,3,1],
                [1,5,1],
                [4,2,1]
                ]
        self.assertEqual(sol.minPathSum(grid), 7)

    

       
if __name__ == "__main__":
    unittest.main()