'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''

## Note: deep copy 2 dimentional array

import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 0:
            return []

        res = []
        curRes = [ ['.'] * n for _ in range(n) ]

        self.dfs(n, 0, curRes, res)

        result = []
        for r in res:
            tmp = []
            for row in r:
                tmp.append(''.join(row))
            result.append(tmp)

        return result

    
    def dfs(self, n, row, curRes, res):
        if row == n:
            res.append(copy.deepcopy(curRes))
            return

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
                self.dfs(n, row + 1, curRes, res)
                curRes[row][col] = '.'
                
            




    @staticmethod
    def main():
        sol = Solution()
        n = 2
        print(sol.solveNQueens(n))
        

if __name__ == "__main__":
    Solution.main() 