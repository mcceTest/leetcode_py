import unittest

from X69_Sqrtx import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        x = 4

        self.assertEqual(sol.mySqrt(x), 2)

    def test2(self):
        sol = Solution()
        x = 8

        self.assertEqual(sol.mySqrt(x), 2)

    

       
if __name__ == "__main__":
    unittest.main()