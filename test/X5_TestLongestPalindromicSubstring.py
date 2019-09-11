import unittest
from X5_LongestPalindromicSubstring import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertEqual(sol.longestPalindrome("cbbd"), "bb")

        self.assertIn(sol.longestPalindrome("babad"), ["bab", "aba"])
        


if __name__ == "__main__":
    unittest.main()