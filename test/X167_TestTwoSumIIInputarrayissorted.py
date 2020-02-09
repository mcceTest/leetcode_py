import unittest
from X167_TwoSumIIInputarrayissorted import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        numbers = [2,7,11,15]
        target = 9
        self.assertListEqual(sol.twoSum(numbers, target), [1,2])

if __name__ == "__main__":
    unittest.main()