import unittest

from X72_EditDistance import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        word1 = "horse"
        word2 = "ros"

        self.assertEqual(sol.minDistance(word1, word2), 3)

    def test2(self):
        sol = Solution()
        word1 = "intention"
        word2 = "execution"

        self.assertEqual(sol.minDistance(word1, word2), 5)
    

       
if __name__ == "__main__":
    unittest.main()