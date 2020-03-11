import unittest
from X205_IsomorphicStrings import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "egg"
        t = "add"
        self.assertTrue(sol.isIsomorphic(s, t))


    def test2(self):
        sol = Solution()
        s = "foo"
        t = "bar"
        self.assertFalse(sol.isIsomorphic(s, t))


    def test3(self):
        sol = Solution()
        s = "paper"
        t = "title"
        self.assertTrue(sol.isIsomorphic(s, t))


    def test4(self):
        sol = Solution()
        s = ""
        t = ""
        self.assertTrue(sol.isIsomorphic(s, t))


    def test5(self):
        sol = Solution()
        s = "paper"
        t = ""
        self.assertFalse(sol.isIsomorphic(s, t))


    def test6(self):
        sol = Solution()
        s = "aba"
        t = "baa"
        self.assertFalse(sol.isIsomorphic(s, t))
    

    def test7(self):
        sol = Solution()
        s = "ab"
        t = "aa"
        self.assertFalse(sol.isIsomorphic(s, t))
    

if __name__ == "__main__":
    unittest.main()