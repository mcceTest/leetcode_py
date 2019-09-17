import unittest
from X16_3SumClosest import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertEqual(sol.threeSumClosest([-1, 2, 1, -4], 1), 2)
        
       
if __name__ == "__main__":
    unittest.main()