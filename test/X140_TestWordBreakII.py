import unittest
from X140_WordBreakII import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        self.assertListEqual(sorted(sol.wordBreak(s, wordDict)), sorted([
                                                                "cats and dog",
                                                                "cat sand dog"
                                                                ]))


    def test2(self):
        sol = Solution()
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        self.assertListEqual(sorted(sol.wordBreak(s, wordDict)), sorted([
                                                        "pine apple pen apple",
                                                        "pineapple pen apple",
                                                        "pine applepen apple"
                                                        ]))

    def test3(self):
        sol = Solution()
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertListEqual(sorted(sol.wordBreak(s, wordDict)), sorted([]))

    def test4(self):
        sol = Solution()
        s = ""
        wordDict = ["", "dog", "sand", "and", "cat"]
        self.assertListEqual(sorted(sol.wordBreak(s, wordDict)), sorted(['']))


    def test5(self):
        sol = Solution()
        s =  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        
        self.assertListEqual(sorted(sol.wordBreak(s, wordDict)), sorted([]))
   


if __name__ == "__main__":
    unittest.main()