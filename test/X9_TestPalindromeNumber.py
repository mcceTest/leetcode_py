import unittest
from X9_PalindromeNumber import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertTrue(sol.isPalindrome(121))

        self.assertFalse(sol.isPalindrome(-121))

        self.assertFalse(sol.isPalindrome(10))



if __name__ == "__main__":
    unittest.main()