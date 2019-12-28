import unittest
from X115_DistinctSubsequences import Solution
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        S = "rabbbit"
        T = "rabbit"
        self.assertEqual(sol.numDistinct(S, T), 3)

    def test2(self):
        sol = Solution()
        S = "babgbag"
        T = "bag"
        self.assertEqual(sol.numDistinct(S, T), 5)

    def test3(self):
        sol = Solution()
        S = "babgbag"
        T = ""
        self.assertEqual(sol.numDistinct(S, T), 1)

    def test4(self):
        sol = Solution()
        S = ""
        T = "bag"
        self.assertEqual(sol.numDistinct(S, T), 0)


if __name__ == "__main__":
    unittest.main()