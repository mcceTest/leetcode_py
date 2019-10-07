import unittest

from X45_JumpGameII import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        nums = [2,3,1,1,4]
        self.assertEqual(sol.jump(nums), 2)


    
       
if __name__ == "__main__":
    unittest.main()