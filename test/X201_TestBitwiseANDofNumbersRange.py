import unittest
from X201_BitwiseANDofNumbersRange import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        m = 5
        n = 7
        self.assertEqual(sol.rangeBitwiseAnd(m, n), 4)

    def test2(self):
        sol = Solution()
        m = 0
        n = 1
        self.assertEqual(sol.rangeBitwiseAnd(m, n), 0)


    def test3(self):
        sol = Solution()
        m = 0
        n = 2147483647
        self.assertEqual(sol.rangeBitwiseAnd(m, n), 0)

    

if __name__ == "__main__":
    unittest.main()