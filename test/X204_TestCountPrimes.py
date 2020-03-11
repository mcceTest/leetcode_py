import unittest
from X204_CountPrimes import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 10
        self.assertEqual(sol.countPrimes(n), 4)

    def test2(self):
        sol = Solution()
        n = 1
        self.assertEqual(sol.countPrimes(n), 0)

    def test3(self):
        sol = Solution()
        n = 2
        self.assertEqual(sol.countPrimes(n), 0)

    def test4(self):
        sol = Solution()
        n = 3
        self.assertEqual(sol.countPrimes(n), 1)

    def test5(self):
        sol = Solution()
        n = 4
        self.assertEqual(sol.countPrimes(n), 2)
    

if __name__ == "__main__":
    unittest.main()