import unittest
from X12_IntegertoRoman import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertEqual(sol.intToRoman(3), "III")

        self.assertEqual(sol.intToRoman(4), "IV")

        self.assertEqual(sol.intToRoman(9), "IX")

        self.assertEqual(sol.intToRoman(58), "LVIII")

        self.assertEqual(sol.intToRoman(1994), "MCMXCIV")

        


if __name__ == "__main__":
    unittest.main()