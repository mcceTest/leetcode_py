import unittest
from X131_PalindromePartitioning import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "aab"
        self.assertListEqual(sorted(sol.partition(s)), sorted([
                                ["aa","b"],
                                ["a","a","b"]
                                ]))

    def test2(self):
        sol = Solution()
        s = "a"
        self.assertListEqual(sorted(sol.partition(s)), sorted([
                                ["a"],
                                ]))


if __name__ == "__main__":
    unittest.main()