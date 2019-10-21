import unittest

from X80_RemoveDuplicatesfromSortedArrayII import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,1,1,2,2,3]
        self.assertEqual(sol.removeDuplicates(nums), 5)

    def test2(self):
        sol = Solution()
        nums = [0,0,1,1,1,1,2,3,3]
        self.assertEqual(sol.removeDuplicates(nums), 7)


if __name__ == "__main__":
    unittest.main()