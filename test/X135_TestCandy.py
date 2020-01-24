import unittest
from X135_Candy import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        ratings = [1,0,2]
        self.assertEqual(sol.candy(ratings), 5)


    def test2(self):
        sol = Solution()
        ratings = [1,2,2]
        self.assertEqual(sol.candy(ratings), 4)


if __name__ == "__main__":
    unittest.main()