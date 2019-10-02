import unittest

from X34_FindFirstandLastPositionofElementinSortedArray import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [5,7,7,8,8,10]
        target = 8

        self.assertListEqual(sol.searchRange(nums, target), [3, 4])

    def test2(self):
        sol = Solution()
        nums = [5,7,7,8,8,10]
        target = 6

        self.assertListEqual(sol.searchRange(nums, target), [-1, -1])


    def test3(self):
        sol = Solution()
        nums = [1]
        target = 1

        self.assertListEqual(sol.searchRange(nums, target), [0, 0])
        
       
if __name__ == "__main__":
    unittest.main()