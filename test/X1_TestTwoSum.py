import unittest
import X1_TwoSum

class TestSum(unittest.TestCase):

    def test1(self):
        sol = X1_TwoSum.Solution()

        nums = [2, 7, 11, 15]
        target = 9

        self.assertEqual( (0, 1), sol.twoSum(nums, target))


if __name__ == "__main__":
    import sys
    unittest.main()