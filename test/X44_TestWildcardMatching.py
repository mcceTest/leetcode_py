import unittest

from X44_WildcardMatching import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "aa"
        p = "a"
        self.assertFalse(sol.isMatch(s, p))


    def test2(self):
        sol = Solution()
        s = "aa"
        p = "*"
        self.assertTrue(sol.isMatch(s, p))


    def test3(self):
        sol = Solution()
        s = "cb"
        p = "?a"
        self.assertFalse(sol.isMatch(s, p))

    def test4(self):
        sol = Solution()
        s = "adceb"
        p = "*a*b"
        self.assertTrue(sol.isMatch(s, p))

    def test5(self):
        sol = Solution()
        s = "acdcb"
        p = "a*c?b"
        self.assertFalse(sol.isMatch(s, p))


    
       
if __name__ == "__main__":
    unittest.main()