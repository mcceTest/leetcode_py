import unittest

from X79_WordSearch import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        board = [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
                ]
        word = "ABCCED"
        self.assertTrue(sol.exist(board, word))

    def test2(self):
        sol = Solution()
        board = [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
                ]
        word = "SEE"
        self.assertTrue(sol.exist(board, word))

    def test3(self):
        sol = Solution()
        board = [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
                ]
        word = "ABCB"
        self.assertFalse(sol.exist(board, word))

    def test4(self):
        sol = Solution()
        board = [
                ['a']
                ]
        word = "a"
        self.assertFalse(sol.exist(board, word))


if __name__ == "__main__":
    unittest.main()