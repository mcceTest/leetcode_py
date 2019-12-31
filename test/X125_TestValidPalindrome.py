import unittest
from X125_ValidPalindrome import Solution
class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(sol.isPalindrome(s))

    def test2(self):
        sol = Solution()
        s = "race a car"
        self.assertFalse(sol.isPalindrome(s))

    def test3(self):
        sol = Solution()
        s = ""
        self.assertTrue(sol.isPalindrome(s))

    def test4(self):
        sol = Solution()
        s = ":"
        self.assertTrue(sol.isPalindrome(s))

    def test5(self):
        sol = Solution()
        s = "a "
        self.assertTrue(sol.isPalindrome(s))

    def test6(self):
        sol = Solution()
        s = "a: "
        self.assertTrue(sol.isPalindrome(s))

    def test7(self):
        sol = Solution()
        s = "0P"
        self.assertFalse(sol.isPalindrome(s))

if __name__ == "__main__":
    unittest.main()