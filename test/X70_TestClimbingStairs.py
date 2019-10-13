import unittest

from X70_ClimbingStairs import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 2

        self.assertEqual(sol.climbStairs(n), 2)

    def test2(self):
        sol = Solution()
        n = 3

        self.assertEqual(sol.climbStairs(n), 3)

    

       
if __name__ == "__main__":
    unittest.main()