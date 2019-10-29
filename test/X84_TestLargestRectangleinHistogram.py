import unittest

from listNode import ListNode
from X84_LargestRectangleinHistogram import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        height = [2,1,5,6,2,3]

        self.assertEqual(sol.largestRectangleArea(height), 10)

    def test2(self):
        sol = Solution()
        height = [1]

        self.assertEqual(sol.largestRectangleArea(height), 1)


if __name__ == "__main__":
    unittest.main()