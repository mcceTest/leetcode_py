import unittest
from X166_FractiontoRecurringDecimal import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        numerator = 1
        denominator = 2
        self.assertEqual(sol.fractionToDecimal(numerator, denominator), "0.5")


    def test2(self):
        sol = Solution()
        numerator = 2
        denominator = 1
        self.assertEqual(sol.fractionToDecimal(numerator, denominator), "2")

    def test3(self):
        sol = Solution()
        numerator = 2
        denominator = 3
        self.assertEqual(sol.fractionToDecimal(numerator, denominator), "0.(6)")


    def test4(self):
        sol = Solution()
        numerator = 20
        denominator = -3
        self.assertEqual(sol.fractionToDecimal(numerator, denominator), "-6.(6)")


if __name__ == "__main__":
    unittest.main()