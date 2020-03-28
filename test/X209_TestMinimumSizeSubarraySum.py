import unittest
from X209_MinimumSizeSubarraySum import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = 7
        nums = [2,3,1,2,4,3]
        self.assertEqual(sol.minSubArrayLen(s, nums), 2)


    def test2(self):
        sol = Solution()
        s = 7
        nums = [2,3]
        self.assertEqual(sol.minSubArrayLen(s, nums), 0)


    def test3(self):
        sol = Solution()
        s = 7
        nums = [7,2,3]
        self.assertEqual(sol.minSubArrayLen(s, nums), 1)


    def test4(self):
        sol = Solution()
        s = 7
        nums = [1,1,2,3,1]
        self.assertEqual(sol.minSubArrayLen(s, nums), 4)

    def test5(self):
        sol = Solution()
        s = 7
        nums = [1,1,2,3,3]
        self.assertEqual(sol.minSubArrayLen(s, nums), 3)

    
    

if __name__ == "__main__":
    unittest.main()