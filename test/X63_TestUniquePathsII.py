import unittest

from X63_UniquePathsII import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        obstacleGrid = [
                        [0,0,0],
                        [0,1,0],
                        [0,0,0]
                        ]

        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), 2)

    def test2(self):
        sol = Solution()
        obstacleGrid = [
                        [1]
                        ]

        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), 0)


       
if __name__ == "__main__":
    unittest.main()