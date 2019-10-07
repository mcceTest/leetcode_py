'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''



class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        curRes = [ ['.'] * n for _ in range(n) ]

        return self.dfs(n, 0, curRes)

    
    def dfs(self, n, row, curRes):
        if row == n:
            return 1

        count = 0

        for col in range(n):
            isValid = True
            for r in range(row):
                if curRes[r][col] == 'Q':
                    isValid = False
                    break
                leftCornor = col - (row - r)
                if leftCornor >= 0 and curRes[r][leftCornor] == 'Q':
                    isValid = False
                    break
                rightCornor = col + (row - r)
                if rightCornor < n and curRes[r][rightCornor] == 'Q':
                    isValid = False
                    break

            if isValid:
                curRes[row][col] = 'Q'
                count += self.dfs(n, row + 1, curRes)
                curRes[row][col] = '.'

        return count

    @staticmethod
    def main():
        sol = Solution()
        n = 4
        print(sol.totalNQueens(n))
        

if __name__ == "__main__":
    Solution.main() 