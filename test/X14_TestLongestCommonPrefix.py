import unittest
from X14_LongestCommonPrefix import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertEqual(sol.longestCommonPrefix(["flower","flow","flight"]), "fl")

        self.assertEqual(sol.longestCommonPrefix(["dog","racecar","car"]), "")

       
if __name__ == "__main__":
    unittest.main()