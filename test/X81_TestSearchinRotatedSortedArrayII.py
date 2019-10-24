import unittest

from listNode import ListNode
from X81_SearchinRotatedSortedArrayII import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [2,5,6,0,0,1,2]
        target = 0
        self.assertTrue(sol.search(nums, target))
    
    def test2(self):
        sol = Solution()
        nums = [2,5,6,0,0,1,2]
        target = 3
        self.assertFalse(sol.search(nums, target))


if __name__ == "__main__":
    unittest.main()