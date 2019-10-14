import unittest

from X75_SortColors import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [2,0,2,1,1,0]

        sol.sortColors(nums)
        self.assertListEqual(nums, [0,0,1,1,2,2])

    def test2(self):
        sol = Solution()
        nums = [1,0,2,1,1,0]

        sol.sortColors(nums)
        self.assertListEqual(nums, [0,0,1,1,1,2])

    def test3(self):
        sol = Solution()
        nums = [0,0,2,1,1,0]

        sol.sortColors(nums)
        self.assertListEqual(nums, [0,0,0,1,1,2])

    def test4(self):
        sol = Solution()
        nums = [2,0]

        sol.sortColors(nums)
        self.assertListEqual(nums, [0,2])


if __name__ == "__main__":
    unittest.main()