import unittest
from X87_ScrambleString import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s1 = "great"
        s2 = "rgeat"
        self.assertTrue(sol.isScramble(s1, s2))

    def test2(self):
        sol = Solution()
        s1 = "abcde"
        s2 = "caebd"
        self.assertFalse(sol.isScramble(s1, s2))


    def test3(self):
        sol = Solution()
        s1 = "abcdefghijklmnopq"
        s2 = "efghijklmnopqcadb"
        self.assertFalse(sol.isScramble(s1, s2))


if __name__ == "__main__":
    unittest.main()