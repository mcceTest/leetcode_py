import unittest
from X214_ShortestPalindrome import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "aacecaaa"
        self.assertEqual(sol.shortestPalindrome(s), "aaacecaaa") 


    def test2(self):
        sol = Solution()
        s = "abcd"
        self.assertEqual(sol.shortestPalindrome(s), "dcbabcd") 

    def test3(self):
        sol = Solution()
        s = "aabba"
        self.assertEqual(sol.shortestPalindrome(s), "abbaabba") 
    
    

if __name__ == "__main__":
    unittest.main()