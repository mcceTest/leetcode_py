'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

## TODO: could save space if change visited 'O' to some other char (not 'X'), and then change back to 'O' at last
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        nrow = len(board)
        if nrow < 2:
            return

        ncol = len(board[0])
        if ncol < 2:
            return

        for i in range(ncol):
            self.dfs(board, nrow, ncol, 0, i)
            self.dfs(board, nrow, ncol, nrow - 1, i)

        for i in range(1, nrow - 1):
            self.dfs(board, nrow, ncol, i, 0)
            self.dfs(board, nrow, ncol, i, ncol - 1)

        for x in range(nrow):
            for y in range(ncol):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'Q':
                    board[x][y] = 'O'


    def dfs(self, board, nrow, ncol, x, y):
        if x < 0 or x >= nrow or y < 0 or y >= ncol:
            return

        if board[x][y] == 'X' or board[x][y] == 'Q':
            return

        board[x][y] = 'Q'
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            self.dfs(board, nrow, ncol, x + dx, y + dy)


    def solve2(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        nrow = len(board)
        if nrow < 2:
            return

        ncol = len(board[0])
        if ncol < 2:
            return

        visited = [ [False] * ncol for _ in range(nrow)]

        for i in range(ncol):
            self.dfs2(board, nrow, ncol, 0, i, visited)
            self.dfs2(board, nrow, ncol, nrow - 1, i, visited)

        for i in range(1, nrow - 1):
            self.dfs2(board, nrow, ncol, i, 0, visited)
            self.dfs2(board, nrow, ncol, i, ncol - 1, visited)

        for x in range(nrow):
            for y in range(ncol):
                if board[x][y] == 'O' and not visited[x][y]:
                    board[x][y] = 'X'


    def dfs2(self, board, nrow, ncol, x, y, visited):
        if x < 0 or x >= nrow or y < 0 or y >= ncol:
            return

        if visited[x][y] or board[x][y] == 'X':
            return

        visited[x][y] = True
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            self.dfs2(board, nrow, ncol, x + dx, y + dy, visited)


        

    @staticmethod
    def main():
        sol = Solution()
        board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        sol.solve(board)
        print(board)


if __name__ == "__main__":
    Solution.main() 
        