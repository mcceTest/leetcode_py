import unittest
from X202_HappyNumber import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 19
        self.assertTrue(sol.isHappy(n))

    

if __name__ == "__main__":
    unittest.main()