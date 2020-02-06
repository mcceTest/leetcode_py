import unittest
from X151_ReverseWordsinaString import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "the sky is blue"
        self.assertEqual(sol.reverseWords(s), "blue is sky the")

    def test2(self):
        sol = Solution()
        s = "  hello world!  "
        self.assertEqual(sol.reverseWords(s), "world! hello")

    def test3(self):
        sol = Solution()
        s = "a good   example"
        self.assertEqual(sol.reverseWords(s), "example good a")

if __name__ == "__main__":
    unittest.main()