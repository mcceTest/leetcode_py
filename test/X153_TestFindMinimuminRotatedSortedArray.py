import unittest
from X153_FindMinimuminRotatedSortedArray import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [3,4,5,1,2] 
        self.assertEqual(sol.findMin(nums), 1)


    def test2(self):
        sol = Solution()
        nums = [4,5,6,7,0,1,2]
        self.assertEqual(sol.findMin(nums), 0)

if __name__ == "__main__":
    unittest.main()