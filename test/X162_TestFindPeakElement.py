import unittest
from X162_FindPeakElement import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,2,3,1]
        self.assertEqual(sol.findPeakElement(nums), 2)


    def test2(self):
        sol = Solution()
        nums = [1,2,1,3,5,6,4]
        self.assertIn(sol.findPeakElement(nums), [1,5])

    def test3(self):
        sol = Solution()
        nums = [1,2,3,4]
        self.assertEqual(sol.findPeakElement(nums), 3)

if __name__ == "__main__":
    unittest.main()