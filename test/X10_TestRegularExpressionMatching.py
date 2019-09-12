import unittest
from X10_RegularExpressionMatching import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertFalse(sol.isMatch("aa", "a"))

        self.assertTrue(sol.isMatch("aa", "a*"))

        self.assertTrue(sol.isMatch("ab", ".*"))

        self.assertTrue(sol.isMatch("aab", "c*a*b"))

        self.assertFalse(sol.isMatch("mississippi", "mis*is*p*."))


if __name__ == "__main__":
    unittest.main()