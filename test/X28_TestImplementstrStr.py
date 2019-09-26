import unittest

from X28_ImplementstrStr import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        haystack = "hello"
        needle = "ll"

        self.assertEqual(sol.strStr(haystack, needle), 2)


    def test2(self):
        sol = Solution()

        haystack = "aaaaa"
        needle = "bba"

        self.assertEqual(sol.strStr(haystack, needle), -1)

    def test3(self):
        sol = Solution()

        haystack = ""
        needle = ""

        self.assertEqual(sol.strStr(haystack, needle), 0)


    def test4(self):
        sol = Solution()

        haystack = "a"
        needle = "a"

        self.assertEqual(sol.strStr(haystack, needle), 0)
        
        
       
if __name__ == "__main__":
    unittest.main()