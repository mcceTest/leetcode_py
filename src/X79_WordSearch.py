'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True

        nrow = len(board)
        if nrow == 0:
            return False

        ncol = len(board[0])
        if ncol == 0:
            return False

        used = [ [False] * ncol for _ in range(nrow)] 

        for i in range(nrow):
            for j in range(ncol):
                if self.dfs(board, word, 0, used, i, j, nrow, ncol):
                    return True

        return False

    def dfs(self, board, word, idx, used, i, j, nrow, ncol):
        if idx == len(word):
            return True

        if not used[i][j] and board[i][j] == word[idx]:
            used[i][j] = True
            if j < ncol - 1:
                if self.dfs(board, word, idx + 1, used, i, j + 1, nrow, ncol):
                    return True

            if j > 0:
                if self.dfs(board, word, idx + 1, used, i, j - 1, nrow, ncol):
                    return True

            if i > 0:
                if self.dfs(board, word, idx + 1, used, i - 1, j, nrow, ncol):
                    return True

            if i < nrow - 1:
                if self.dfs(board, word, idx + 1, used, i + 1, j, nrow, ncol):
                    return True

            used[i][j] = False

        return False

    @staticmethod
    def main():
        sol = Solution()
        board = [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
                ]
        word = "ABCCED"
        print(sol.exist(board, word))
        

if __name__ == "__main__":
    Solution.main() 