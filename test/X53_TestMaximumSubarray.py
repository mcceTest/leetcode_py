import unittest

from X53_MaximumSubarray import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]

        self.assertEqual(sol.maxSubArray(nums), 6)


    
    
    
       
if __name__ == "__main__":
    unittest.main()