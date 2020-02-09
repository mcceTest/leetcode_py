import unittest
from X154_FindMinimuminRotatedSortedArrayII import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,3,5]
        self.assertEqual(sol.findMin(nums), 1)


    def test2(self):
        sol = Solution()
        nums = [2,2,2,0,1]
        self.assertEqual(sol.findMin(nums), 0)

if __name__ == "__main__":
    unittest.main()