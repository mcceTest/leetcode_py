import unittest

from X76_MinimumWindowSubstring import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        S = "ADOBECODEBANC"
        T = "ABC"
        self.assertEqual(sol.minWindow(S, T), "BANC")


    def test2(self):
        sol = Solution()
        S = "ADOBEC"
        T = "ABC"
        self.assertEqual(sol.minWindow(S, T), "ADOBEC")

    def test3(self):
        sol = Solution()
        S = "ADOBEC"
        T = "A"
        self.assertEqual(sol.minWindow(S, T), "A")

    


if __name__ == "__main__":
    unittest.main()