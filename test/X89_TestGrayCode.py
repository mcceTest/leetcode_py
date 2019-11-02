import unittest
from X89_GrayCode import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        self.assertListEqual(sol.grayCode(0), [0])

        self.assertListEqual(sol.grayCode(1), [0, 1])

        self.assertListEqual(sol.grayCode(2), [0, 1, 3, 2])

if __name__ == "__main__":
    unittest.main()