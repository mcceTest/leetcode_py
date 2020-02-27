import unittest
from X198_HouseRobber import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [1,2,3,1]
        self.assertEqual(sol.rob(nums), 4)

    def test2(self):
        sol = Solution()
        nums = [2,7,9,3,1]
        self.assertEqual(sol.rob(nums), 12)

    def test3(self):
        sol = Solution()
        nums = [1,2,3]
        self.assertEqual(sol.rob(nums), 4)

    def test4(self):
        sol = Solution()
        nums = [2,1,1,2]
        self.assertEqual(sol.rob(nums), 4)

    

if __name__ == "__main__":
    unittest.main()