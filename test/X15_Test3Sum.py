import unittest
from X15_3Sum import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertListEqual(sorted(sol.threeSum([-1, 0, 1, 2, -1, -4])), sorted([
                                                                            [-1, 0, 1],
                                                                            [-1, -1, 2]
                                                                            ]))

        self.assertListEqual(sorted(sol.threeSum([-2,0,0,2,2])), sorted([
                                                                    [-2, 0, 2]
                                                                    ]))
       
if __name__ == "__main__":
    unittest.main()