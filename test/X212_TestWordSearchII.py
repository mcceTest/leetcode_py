import unittest
from X212_WordSearchII import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        board = [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
        ]
        words = ["oath","pea","eat","rain"]
        self.assertListEqual(sorted(sol.findWords(board, words)), sorted(["eat","oath"]))


    def test2(self):
        sol = Solution()
        board = [
            ['a', 'a']
        ]
        words = ["aaa"]
        self.assertListEqual(sorted(sol.findWords(board, words)), sorted([]))

    def test3(self):
        sol = Solution()
        board = [
            ['a', 'a', 'a']
        ]
        words = ["aaa"]
        self.assertListEqual(sorted(sol.findWords(board, words)), sorted(['aaa']))

    def test4(self):
        sol = Solution()
        board = [
            ['a', 'a'],
            ['a', 'a']
        ]
        words = ["aaa", "aaaa", 'aaaaa']
        self.assertListEqual(sorted(sol.findWords(board, words)), sorted(['aaa', 'aaaa']))


    
    

if __name__ == "__main__":
    unittest.main()