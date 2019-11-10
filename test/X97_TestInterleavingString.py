import unittest
from X97_InterleavingString import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"

        self.assertTrue(sol.isInterleave(s1, s2, s3))


    def test2(self):
        sol = Solution()
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"

        self.assertFalse(sol.isInterleave(s1, s2, s3))
        
                           
if __name__ == "__main__":
    unittest.main()