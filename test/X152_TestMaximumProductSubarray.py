import unittest
from X152_MaximumProductSubarray import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [2,3,-2,4]
        self.assertEqual(sol.maxProduct(nums), 6)


    def test2(self):
        sol = Solution()
        nums =  [-2,0,-1]
        self.assertEqual(sol.maxProduct(nums), 0)

if __name__ == "__main__":
    unittest.main()