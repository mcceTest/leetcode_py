import unittest
from X132_PalindromePartitioningII import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "aab"
        self.assertEqual(sol.minCut(s), 1)

    def test2(self):
        sol = Solution()
        s = "a"
        self.assertEqual(sol.minCut(s), 0)


    def test3(self):
        sol = Solution()
        s = "aa"
        self.assertEqual(sol.minCut(s), 0)

    def test4(self):
        sol = Solution()
        s = "aba"
        self.assertEqual(sol.minCut(s), 0)

if __name__ == "__main__":
    unittest.main()