import unittest

from X60_PermutationSequence import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 3
        k = 3

        self.assertEqual(sol.getPermutation(n, k), "213")

    def test2(self):
        sol = Solution()
        n = 4
        k = 9

        self.assertEqual(sol.getPermutation(n, k), "2314")


    def test3(self):
        sol = Solution()
        n = 2
        k = 2

        self.assertEqual(sol.getPermutation(n, k), "21")
   
    
       
if __name__ == "__main__":
    unittest.main()