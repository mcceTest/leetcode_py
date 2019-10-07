import unittest

from X52_NQueensII import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 4
        self.assertEqual(sol.totalNQueens(n), 2)


    
    
    
       
if __name__ == "__main__":
    unittest.main()