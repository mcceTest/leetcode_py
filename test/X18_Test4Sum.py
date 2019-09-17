import unittest
from X18_4Sum import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertListEqual(sorted(sol.fourSum([1, 0, -1, 0, -2, 2], 0)), 
                            sorted([
                                    [-1,  0, 0, 1],
                                    [-2, -1, 1, 2],
                                    [-2,  0, 0, 2]
                                    ]))


        self.assertListEqual(sorted(sol.fourSum([-3,-2,-1,0,0,1,2,3], 0)), 
                            sorted([[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]))
        
        self.assertListEqual(sorted(sol.fourSum([-5,5,4,-3,0,0,4,-2], 4)), 
                            sorted([[-5,0,4,5],[-3,-2,4,5]]))
        
       
if __name__ == "__main__":
    unittest.main()