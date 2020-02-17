import unittest
from X179_LargestNumber import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [3,30,34,5,9]
        self.assertEqual(sol.largestNumber(nums), "9534330")

    def test2(self):
        sol = Solution()
        nums = [10,2]
        self.assertEqual(sol.largestNumber(nums), "210")

    def test3(self):
        sol = Solution()
        nums = [39]
        self.assertEqual(sol.largestNumber(nums), "39")


    def test4(self):
        sol = Solution()
        nums = []
        self.assertEqual(sol.largestNumber(nums), "")

    def test5(self):
        sol = Solution()
        nums = [0, 0]
        self.assertEqual(sol.largestNumber(nums), "0")

    def test6(self):
        sol = Solution()
        nums = [0]
        self.assertEqual(sol.largestNumber(nums), "0")


if __name__ == "__main__":
    unittest.main()