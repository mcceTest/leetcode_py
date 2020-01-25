import unittest
from X139_WordBreak import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(sol.wordBreak(s, wordDict))

    def test2(self):
        sol = Solution()
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(sol.wordBreak(s, wordDict))

    def test3(self):
        sol = Solution()
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(sol.wordBreak(s, wordDict))


if __name__ == "__main__":
    unittest.main()