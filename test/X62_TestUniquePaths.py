import unittest

from X62_UniquePaths import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        m = 3
        n = 2

        self.assertEqual(sol.uniquePaths(m, n), 3)


    def test2(self):
        sol = Solution()
        m = 7
        n = 3

        self.assertEqual(sol.uniquePaths(m, n), 28)

    def test3(self):
        sol = Solution()
        m = 7
        n = 1

        self.assertEqual(sol.uniquePaths(m, n), 1)

    
       
if __name__ == "__main__":
    unittest.main()