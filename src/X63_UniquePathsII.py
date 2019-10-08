'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

## TODO: use 1-d array to memo the result for the entire column or row

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0: return 0

        n = len(obstacleGrid[0])
        if n == 0: return 0

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        memo = [ [0] * n for _ in range(m)]
        memo[0][0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                memo[0][i] = 0
            else:
                memo[0][i] = memo[0][i - 1]

        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                memo[i][0] = 0
            else:
                memo[i][0] = memo[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    memo[i][j] = 0
                else:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[m - 1][n - 1]


    @staticmethod
    def main():
        sol = Solution()
        obstacleGrid = [
                        [0,0,0],
                        [0,1,0],
                        [0,0,0]
                        ]
        print(sol.uniquePathsWithObstacles(obstacleGrid))

if __name__ == "__main__":
    Solution.main() 