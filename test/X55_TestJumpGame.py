import unittest

from X55_JumpGame import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [2,3,1,1,4]

        self.assertTrue(sol.canJump(nums))
    

    def test2(self):
        sol = Solution()
        nums = [3,2,1,0,4]

        self.assertFalse(sol.canJump(nums))
    
       
if __name__ == "__main__":
    unittest.main()