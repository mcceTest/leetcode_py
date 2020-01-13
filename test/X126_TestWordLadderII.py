import unittest
from X126_WordLadderII import Solution
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]

        self.assertListEqual(sorted(sol.findLadders(beginWord, endWord, wordList)),
                                sorted([
                                        ["hit","hot","dot","dog","cog"],
                                        ["hit","hot","lot","log","cog"]
                                        ]))

    def test2(self):
        sol = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]

        self.assertListEqual(sol.findLadders(beginWord, endWord, wordList), [])

    
   
if __name__ == "__main__":
    unittest.main()