import unittest
from X136_SingleNumber import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [2,2,1]
        self.assertEqual(sol.singleNumber(nums), 1)


    def test2(self):
        sol = Solution()
        nums = [4,1,2,1,2]
        self.assertEqual(sol.singleNumber(nums), 4)


if __name__ == "__main__":
    unittest.main()