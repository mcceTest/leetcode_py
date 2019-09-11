import unittest
from X6_ZigZagConversion import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertEqual(sol.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

        self.assertEqual(sol.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        
        self.assertEqual(sol.convert("A", 1), "A")
        

if __name__ == "__main__":
    unittest.main()