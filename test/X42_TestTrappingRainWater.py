import unittest

from X42_TrappingRainWater import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        height = [0,1,0,2,1,0,1,3,2,1,2,1]

        self.assertEqual(sol.trap(height), 6)
    
        
       
if __name__ == "__main__":
    unittest.main()