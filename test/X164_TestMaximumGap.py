import unittest
from X164_MaximumGap import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [3,6,9,1]
        self.assertEqual(sol.maximumGap(nums), 3)

    def test2(self):
        sol = Solution()
        nums = [10]
        self.assertEqual(sol.maximumGap(nums), 0)

    def test3(self):
        sol = Solution()
        nums = [1,10000000]
        self.assertEqual(sol.maximumGap(nums), 9999999)


if __name__ == "__main__":
    unittest.main()