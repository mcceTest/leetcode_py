import unittest
from X211_AddandSearchWord import WordDictionary


class TestSum(unittest.TestCase):

    def test1(self):
        sol = WordDictionary()
        sol.addWord("bad")
        sol.addWord("dad")
        sol.addWord("mad")

        self.assertFalse(sol.search("pad"))
        self.assertTrue(sol.search("bad"))
        self.assertTrue(sol.search(".ad"))
        self.assertTrue(sol.search("b.."))
        self.assertFalse(sol.search(""))

        sol.addWord("")
        self.assertTrue(sol.search(""))
    

if __name__ == "__main__":
    unittest.main()