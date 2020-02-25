import unittest
from X189_RotateArray import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,2,3,4,5,6,7]
        k = 3
        sol.rotate(nums, k)
        self.assertListEqual(nums, [5,6,7,1,2,3,4])

    def test2(self):
        sol = Solution()
        nums = [-1,-100,3,99]
        k = 2
        sol.rotate(nums, k)
        self.assertListEqual(nums, [3,99,-1,-100])

if __name__ == "__main__":
    unittest.main()