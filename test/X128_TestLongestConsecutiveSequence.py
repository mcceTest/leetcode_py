import unittest
from X128_LongestConsecutiveSequence import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(sol.longestConsecutive(nums), 4)

    def test2(self):
        sol = Solution()
        nums = [1,2,0,1]
        self.assertEqual(sol.longestConsecutive(nums), 3)

if __name__ == "__main__":
    unittest.main()