'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''

## TODO: when check validity, only need to compare the value of the cell with the others
from pprint import pprint as pp
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        x, y = self.nextDot(board, 0, -1)
        if x == -1:
            return

        self.dfs(board, x, y)


    def dfs(self, board, x, y):
        nextX, nextY = self.nextDot(board, x, y)

        for i in range(9):
            board[x][y] = chr(ord('1') + i)
            if not self.rowValid(x, board) or not self.colValid(y, board) or not self.cubeValid(x // 3, y // 3, board):
                continue
            
            if nextX != -1:
                if self.dfs(board, nextX, nextY):
                    return True
            else:
                return True

        board[x][y] = '.'
        
        return False



    def nextDot(self, board, x, y):
        
        while x < 9:
            y += 1
            if y == 9:
                y = 0
                x += 1

            if x < 9 and board[x][y] == '.':
                return (x, y)

        return (-1, -1)


    def rowValid(self, row, board):
        nums = list(filter(lambda x: x != '.', board[row]))
        return len(nums) == len(set(nums))
        

    def colValid(self, col, board):
        nums = [board[row][col] for row in range(9) if board[row][col] != '.']        
        return len(nums) == len(set(nums))


    def cubeValid(self, cubex, cubey, board):
        nums = []
        for i in range(3):
            for j in range(3):
                cur = board[cubex * 3 + i][cubey * 3 + j]
                if cur != '.': nums.append(cur)
        return len(nums) == len(set(nums))




    @staticmethod
    def main():
        sol = Solution()
        boards = [
                  ["5","3",".",".","7",".",".",".","."],
                  ["6",".",".","1","9","5",".",".","."],
                  [".","9","8",".",".",".",".","6","."],
                  ["8",".",".",".","6",".",".",".","3"],
                  ["4",".",".","8",".","3",".",".","1"],
                  ["7",".",".",".","2",".",".",".","6"],
                  [".","6",".",".",".",".","2","8","."],
                  [".",".",".","4","1","9",".",".","5"],
                  [".",".",".",".","8",".",".","7","9"]
                ]
        sol.solveSudoku(boards)

        pp(boards)


if __name__ == "__main__":
    Solution.main()   