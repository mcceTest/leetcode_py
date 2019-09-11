import unittest
from X8_StringtoInteger import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertEqual(sol.myAtoi("42"), 42)

        self.assertEqual(sol.myAtoi(" -42"), -42)

        self.assertEqual(sol.myAtoi("4193 with words"), 4193)

        self.assertEqual(sol.myAtoi("-91283472332"), -2147483648)

        self.assertEqual(sol.myAtoi("+1"), 1)



if __name__ == "__main__":
    unittest.main()