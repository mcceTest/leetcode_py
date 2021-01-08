import unittest
from X213_HouseRobberII import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [2,3,2]
        self.assertEqual(sol.rob(nums), 3)


    def test2(self):
        sol = Solution()
        nums = [1,2,3,1]
        self.assertEqual(sol.rob(nums), 4)


    
    

if __name__ == "__main__":
    unittest.main()