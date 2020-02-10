import unittest
from X172_FactorialTrailingZeroes import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        n = 3
        self.assertEqual(sol.trailingZeroes(n), 0)


    def test2(self):
        sol = Solution()
        n = 5
        self.assertEqual(sol.trailingZeroes(n), 1)

    def test3(self):
        sol = Solution()
        n = 9
        self.assertEqual(sol.trailingZeroes(n), 1)


    


if __name__ == "__main__":
    unittest.main()