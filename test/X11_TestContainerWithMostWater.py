import unittest
from X11_ContainerWithMostWater import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertEqual(sol.maxArea([1,8,6,2,5,4,8,3,7]), 49)

        


if __name__ == "__main__":
    unittest.main()